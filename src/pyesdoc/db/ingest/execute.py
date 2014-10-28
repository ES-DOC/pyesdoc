"""
.. module:: execute.py
   :platform: Unix
   :synopsis: Executes ingestion process from document archive.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import datetime, os
from multiprocessing.dummy import Pool as ThreadPool

from . import (
    set_drs,
    set_external_id,
    set_is_latest,
    set_primary,
    set_summary,
    validate
    )
from .. import session as db_session
from ... import archive
from ... utils import config, rt



class DocumentProcessingInfo(object):
    """Encapsulates document processing information.

    """
    def __init__(self, doc, fpath, fpath_ingested, index):
        """Object constructor.

        """
        self.doc = doc
        self.error = None
        self.fpath = fpath
        self.fpath_ingested = fpath_ingested
        self.fpath_error = fpath_ingested.replace("ingested", "ingested_error")
        self.index = index


    def __repr__(self):
        """Object representation.

        """
        return "Processing ID = {0} :: Doc ID = {1} :: Doc Version = {2}".format(
            self.index,
            self.doc.meta.id,
            self.doc.meta.version)


def _write_error(ctx):
    """Writes document processing error to file system.

    """
    # Escape if writing controlled loop exit errors.
    if isinstance(ctx.error, StopIteration):
        return

    # Create parent directory.
    try:
        os.makedirs(os.path.dirname(ctx.fpath_error))
    except OSError:
        pass

    # Create error file.
    try:
        with open(ctx.fpath_error, 'wb') as output:
            output.seek(0)
            output.write(u"------------------------------------------------------------\n")
            output.write(u"ES-DOC API DB INGEST ERROR @ {} \n".format(datetime.datetime.now()))
            output.write(u"------------------------------------------------------------\n")
            output.write(u"An error occurred whilst uploading a document to the db:\n\n")
            output.write(u"\tPROJECT = {0};\n".format(ctx.doc.meta.project))
            output.write(u"\tSOURCE = {0};\n".format(ctx.doc.meta.source))
            output.write(u"\tFILEPATH = {0};\n".format(ctx.fpath))
            output.write(u"\tERROR = {0};\n".format(unicode(ctx.error)))
            output.write(u"\tERROR TYPE = {0}.".format(type(ctx.error)))
    except IOError:
        rt.log_warning("Document processing error handling failed.")


def _log_error(ctx):
    """Write processing error message to standard output.

    """
    # Escape if writing controlled loop exit errors.
    if isinstance(ctx.error, StopIteration):
        return

    rt.log("INGEST ERROR :: {0} :: {1} :: {2}".format(ctx, ctx.error, type(ctx.error)))


def _write_ingested(ctx):
    """Writes ingested file to archive.

    """
    # Create parent directory.
    try:
        os.makedirs(os.path.dirname(ctx.fpath_ingested))
    except OSError:
        pass

    # Create symbolic link to original file.
    os.symlink(ctx.fpath, ctx.fpath_ingested)


def _get_documents(throttle=0):
    """Yields documents for processing.

    """
    yielded = 0
    for doc, fpath, fpath_ingested in archive.yield_ingestable():
        yielded += + 1
        yield DocumentProcessingInfo(doc, fpath, fpath_ingested, yielded)
        if throttle and throttle == yielded:
            break


def process(ctx):
    """Ingests a document.

    """
    tasks = (
        validate.execute,
        set_primary.execute,
        set_is_latest.execute,
        set_summary.execute,
        set_drs.execute,
        set_external_id.execute,
        _write_ingested
        )

    error_tasks = (
        _write_error,
        _log_error
        )

    rt.invoke(ctx, tasks, error_tasks)


def process_archived(throttle=0):
    """Ingests files from archive.

    :param int throttle: Limits the number of documents to process.

    """
    for ctx in _get_documents(throttle):
        process(ctx)
