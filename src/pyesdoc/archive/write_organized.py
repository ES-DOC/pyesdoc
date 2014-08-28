"""
.. module:: write_organized.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Writes set of parsed documents to file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import datetime
import os
from multiprocessing.dummy import Pool as ThreadPool

from . import io
from .parsers.doc_parser import parse as parse_doc
from ..constants import ESDOC_ENCODING_JSON as _ENCODING
from ..extensions import extend as extend_doc
from ..io import (
    read as read_doc,
    write as write_doc
    )
from ..utils import runtime as rt



# Original encoding type literal.
_ORIGINAL = "original"


class _DecodingException(Exception):
    """Exception raised when document decoding fails."""
    pass


class _IOException(Exception):
    """Exception raised when document i/o fails."""
    pass


class _DocumentContextInfo(object):
    """Encapsulates document processing information."""
    def __init__(self, project, source, fpath, index, verbose):
        self.dirname = os.path.dirname(fpath)
        self.encoding = fpath.split('.')[-1]
        self.error = None
        self.index = index
        self.fpath = fpath
        self.fpath_parsed = fpath.replace(io.DIR_RAW, io.DIR_PARSED) \
                                 .replace(self.encoding, _ENCODING)
        self.fpath_error = fpath.replace(io.DIR_RAW, io.DIR_PARSED_ERROR)
        self.project = project
        self.source = source
        self.verbose = verbose

        self.exists = os.path.exists(self.fpath_parsed)


    def __repr__(self):
        return "{0} :: {1}".format(self.project.name, self.fpath)


def _log_start(ctx):
    """Writes a processing start message to standard output."""
    if ctx.verbose:
        msg = "processing document {0}: {1} --> {2} --> {3}"
        msg = msg.format(ctx.index, ctx.project, ctx.source, ctx.fpath)
        rt.log(msg)


def _decode(ctx):
    """Decodes a document."""
    # Use pyesdoc to decode raw file.
    try:
        ctx.decoded = read_doc(ctx.fpath, encoding=ctx.encoding)
    except Exception as err:
        raise _DecodingException(err)


def _parse(ctx):
    """Parses a document."""
    # Parse document.
    parse_doc(ctx.project, ctx.source, ctx.decoded)

    # Extend document.
    extend_doc(ctx.decoded)


def _write_parsed(ctx):
    """Writes a parsed document to the file system."""
    try:
        write_doc(ctx.decoded, _ENCODING, ctx.fpath_parsed)
    except IOError as err:
        raise _IOException(err)
    else:
        ctx.exists = True
        os.symlink(ctx.fpath, ctx.fpath_parsed.replace(_ENCODING, _ORIGINAL))


def _write_organized(ctx):
    """Writes symbolic links."""
    # Set organized document type directory.
    dirname = io.get_organized_dir(ctx.project, ctx.source, ctx.decoded)

    # Set organized file name.
    fname = "{0}_{1}".format(ctx.decoded.meta.id, ctx.decoded.meta.version)
    fpath = os.path.join(dirname, fname)

    # Set links.
    os.symlink(ctx.fpath, fpath + ".orginal")
    os.symlink(ctx.fpath_parsed, fpath + "." + _ENCODING)


def _log_error(ctx):
    """Write processing error message to standard output."""
    msg = "ARCHIVE ERROR :: processing document {0}: {1} --> {2} --> {3}"
    msg = msg.format(ctx.index, ctx.project, ctx.source, ctx.fpath)
    rt.log(msg)


def _write_error(ctx):
    """Writes document processing error to file system."""
    try:
        with open(ctx.fpath_error, 'wb') as output:
            output.seek(0)
            output.write(u"------------------------------------------------------------\n")
            output.write(u"ES-DOC ARCHIVE UPLOAD ERROR @ {} \n".format(datetime.datetime.now()))
            output.write(u"------------------------------------------------------------\n")
            output.write(u"An error occurred whilst uploading a document to the db:\n\n")
            output.write(u"\tPROJECT = {0};\n".format(ctx.project))
            output.write(u"\tSOURCE = {0};\n".format(ctx.source))
            output.write(u"\tFILEPATH = {0};\n".format(ctx.fpath))
            output.write(u"\tERROR = {0}.".format(unicode(ctx.error)))
            output.write(u"\tERROR TYPE = {0}.".format(type(ctx.error)))
    except IOError:
        rt.log("Document processing error handling failed.")


def _log_processing_stats(scanned, processed, errors):
    """Logs processing stats."""
    rt.log("{0} documents scanned of which {1} required processing" \
        .format(scanned, processed))
    if errors:
        rt.log("WARNING :: {0} processing errors occurred".format(errors))


def _get_documents(throttle, verbose):
    """Yields documents for processing."""
    scanned = 0
    yielded = 0
    for project, source, fpath in io.get_documents(io.DIR_RAW):
        scanned = scanned + 1
        ctx = _DocumentContextInfo(project, source, fpath, yielded + 1, verbose)
        if not ctx.exists:
            yielded = yielded + 1
            yield ctx

        # ... apply throttle
        if throttle and throttle == yielded:
            break

    # Log processing stats.
    _log_processing_stats(scanned, yielded, io.get_count(io.DIR_PARSED_ERROR))


def _process(ctx):
    """Processes a downloaded document."""
    rt.invoke(ctx,
              (_log_start, _decode, _parse, _write_parsed, _write_organized),
              (_log_error,_write_error))


def execute(throttle=0, verbose=False):
    """Writes parsed documents to file system.

    :param int throttle: Limits number of documents to be processed.
    :param bool verbose: Flag indicating whether logging is verbose.

    """
    pool = ThreadPool()
    pool.map(_process, _get_documents(throttle, verbose))
    pool.close()
