# -*- coding: utf-8 -*-
"""
.. module:: write_organized.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Writes set of organized documents to file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import datetime, os
from multiprocessing.dummy import Pool as ThreadPool

from . import io
from .. import constants
from .parsers.doc_parser import parse as parse_doc
from ..extensions import extend as extend_doc
from ..io import (
    read as read_doc,
    write as write_doc
    )
from ..utils import runtime as rt



# Default document encoding.
_ENCODING = constants.ESDOC_ENCODING_JSON

# Original encoding type literal.
_ORIGINAL = "original"


class _DecodingException(Exception):
    """Exception raised when document decoding fails.

    """
    pass


class _IOException(Exception):
    """Exception raised when document i/o fails.

    """
    pass


class _DocumentProcessingInfo(object):
    """Encapsulates document processing information.

    """
    def __init__(self, raw_file, index, verbose):
        """Object constructor.

        """
        self.decoded = None
        self.encoding = raw_file.encoding
        self.error = None
        self.index = index
        self.raw = raw_file
        self.verbose = verbose


    def __repr__(self):
        """Object representation.

        """
        return "{0} :: {1}".format(self.project, self.raw)


    @property
    def fpath(self):
        """Gets raw filepath.

        """
        return self.raw.path


    @property
    def fpath_parsed(self):
        """Gets parsed filepath.

        """
        return self.raw.path.replace(io.DIR_RAW, io.DIR_PARSED) \
                            .replace(self.raw.encoding, _ENCODING)


    @property
    def fpath_parsed_original(self):
        """Gets original parsed filepath.

        """
        return self.raw.path.replace(io.DIR_RAW, io.DIR_PARSED) \
                            .replace(self.raw.encoding, _ORIGINAL)


    @property
    def fpath_error(self):
        """Gets error filepath.

        """
        return self.raw.path.replace(io.DIR_RAW, io.DIR_PARSED_ERROR) \
                            .replace(self.raw.encoding, _ENCODING)


    @property
    def fname_organized(self):
        """Gets organized file name.

        """
        return "{0}_{1}.{2}".format(self.decoded.meta.id,
                                    self.decoded.meta.version,
                                    _ENCODING)


    @property
    def fpath_organized(self):
        """Gets organized file path.

        """
        return "{0}/{1}".format(self.organized_dir, self.fname_organized)


    @property
    def fname_organized_original(self):
        """Gets organized original file name.

        """
        return "{0}_{1}.{2}".format(self.decoded.meta.id,
                                    self.decoded.meta.version,
                                    _ORIGINAL)

    @property
    def fpath_organized_original(self):
        """Gets organized original file path.

        """
        return "{0}/{1}".format(self.organized_dir,
                                self.fname_organized_original)


    @property
    def organized_dir(self):
        """Gets organized document directory.

        """
        return io.get_doc_organized_folder(self.decoded,
                                           self.project,
                                           self.source)


    @property
    def is_processed(self):
        """Gets flag indicating whether this file has already been processed.

        """
        return os.path.exists(self.fpath_parsed)


    @property
    def project(self):
        """Gets associated document project.

        """
        return self.raw.project


    @property
    def source(self):
        """Gets associated document source.

        """
        return self.raw.source


def _log_start(ctx):
    """Writes a processing start message to standard output.

    """
    if ctx.verbose:
        msg = "processing document {0}: {1} --> {2} --> {3}"
        msg = msg.format(ctx.index, ctx.project, ctx.source, ctx.fpath)
        rt.log(msg)


def _decode(ctx):
    """Decodes a document.

    """
    try:
        ctx.decoded = read_doc(ctx.raw.path, encoding=ctx.raw.encoding)
    except Exception as err:
        raise _DecodingException(err)


def _parse_and_extend(ctx):
    """Parses and extends a document.

    """
    parse_doc(ctx.project, ctx.source, ctx.decoded)
    extend_doc(ctx.decoded)


def _write_parsed(ctx):
    """Writes a parsed document to the file system.

    """
    try:
        write_doc(ctx.decoded, _ENCODING, ctx.fpath_parsed)
    except IOError as err:
        raise _IOException(err)
    else:
        os.symlink(ctx.fpath, ctx.fpath_parsed_original)


def _write_organized(ctx):
    """Writes symbolic links to organized folder.

    """
    os.symlink(ctx.fpath, ctx.fpath_organized_original)
    os.symlink(ctx.fpath_parsed, ctx.fpath_organized)


def _delete_written(ctx):
    """Deletes written file from file system in event of a processing error.

    """
    try:
        os.remove(ctx.fpath_parsed)
    except IOError:
        pass
    try:
        os.remove(ctx.fpath_parsed_original)
    except IOError:
        pass


def _log_error(ctx):
    """Write processing error message to standard output.

    """
    msg = "ARCHIVE ERROR :: processing document {0}: {1} --> {2} --> {3}"
    msg = msg.format(ctx.index, ctx.project, ctx.source, ctx.fpath)
    rt.log(msg)


def _write_error(ctx):
    """Writes document processing error to file system.

    """
    try:
        with open(ctx.fpath_error, 'wb') as output:
            output.seek(0)
            output.write(u"------------------------------------------------------------\n")
            output.write(u"ES-DOC ARCHIVE ERROR @ {} \n".format(datetime.datetime.now()))
            output.write(u"------------------------------------------------------------\n")
            output.write(u"An error occurred whilst organizing a document:\n\n")
            output.write(u"\tPROJECT = {0};\n".format(ctx.project))
            output.write(u"\tSOURCE = {0};\n".format(ctx.source))
            output.write(u"\tFILEPATH = {0};\n".format(ctx.fpath))
            output.write(u"\tERROR = {0};\n".format(unicode(ctx.error)))
            output.write(u"\tERROR TYPE = {0}.".format(type(ctx.error)))
    except IOError:
        rt.log("Document processing error handling failed.")


def _log_processing_stats(scanned, processed, errors):
    """Logs processing stats.

    """
    rt.log("{0} documents scanned of which {1} required processing" \
        .format(scanned, processed))
    if errors:
        rt.log("WARNING :: {0} processing errors occurred".format(errors))


def _get_documents(throttle, verbose):
    """Yields documents for processing.

    """
    scanned = 0
    yielded = 0
    for raw_file in io.yield_raw():
        scanned = scanned + 1
        ctx = _DocumentProcessingInfo(raw_file, yielded + 1, verbose)
        if not ctx.is_processed:
            yielded = yielded + 1
            yield ctx

        # ... apply throttle
        if throttle and throttle == yielded:
            break

    # Log processing stats.
    _log_processing_stats(scanned, yielded, io.get_count(io.DIR_PARSED_ERROR))


def _process(ctx):
    """Processes a downloaded document.

    """
    tasks = (
        _log_start,
        _decode,
        _parse_and_extend,
        _write_parsed,
        _write_organized
        )

    error_tasks = (
        _delete_written,
        _log_error,
        _write_error
        )

    rt.invoke(ctx, tasks, error_tasks)


def execute(throttle=0, verbose=False):
    """Writes parsed documents to file system.

    :param int throttle: Limits number of documents to be processed.
    :param bool verbose: Flag indicating whether logging is verbose.

    """
    io.delete_files(io.DIR_ORGANIZED_ERROR)
    io.delete_files(io.DIR_PARSED_ERROR)

    for ctx in _get_documents(throttle, verbose):
        _process(ctx)

    return

    pool = ThreadPool()
    pool.map(_process, _get_documents(throttle, verbose))
    pool.close()
