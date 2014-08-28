"""
.. module:: write_pulled.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Writes set of pulled documents to file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import datetime
import hashlib
import os
from multiprocessing.dummy import Pool as ThreadPool

import feedparser
import requests

from . import io
from .parsers import content_parser
from ..utils import runtime as rt



# Default document encoding.
_ENCODING = 'utf-8'

# Requests session.
_SESSION = requests.Session()
_SESSION.mount('http://', requests.adapters.HTTPAdapter(
    pool_connections=100, pool_maxsize=100))


class _DownloadException(Exception):
    """Exception raised when a download fails."""
    pass


class _EncodingException(Exception):
    """Exception raised when raw document encoding fails."""
    pass


class _IOException(Exception):
    """Exception raised when document io fails."""
    pass


class _DocumentInfo(object):
    """Encapsulates document processing information."""
    def __init__(self, project, source, url, encoding, index, verbose):
        self.content = None
        self.encoding = encoding
        self.error = None
        self.fname = "{0}.{1}".format(hashlib.md5(url).hexdigest(), encoding)
        self.index = index
        self.project = project
        self.source = source
        self.url = url
        self.verbose = verbose

        self.dirname = io.get_doc_dir(project, source, io.DIR_RAW)
        self.fpath = os.path.join(self.dirname, self.fname)
        self.fpath_error = self.fpath.replace(io.DIR_RAW, io.DIR_RAW_ERROR)
        self.exists = os.path.exists(self.fpath)


    def __repr__(self):
        return "{0} :: {1} :: {2} :: {3} :: {4} :: {5}".format(
            self.project, self.source, io.DIR_RAW, self.fname, self.url, self.exists)


def _get_feeds():
    """Returns generator of active feeds."""
    for project in io.config.projects:
        for feed in (f for f in project.feeds if f.is_active):
            msg = "processing feed: {0} --> {1} --> {2}"
            rt.log(msg.format(project.name, feed.source, feed.url))
            yield project, feed


def _get_feed_entries():
    """Returns generator of active feeds."""
    for project, feed in _get_feeds():
        for entry in feedparser.parse(feed.url).entries:
            yield project.name, feed.source, entry.links[0]['href'], feed.encoding


def _log_processing_stats(scanned, processed, errors):
    """Logs processing stats."""
    rt.log("{0} feed entries scanned of which {1} required processing" \
        .format(scanned, processed))
    if errors:
        rt.log("WARNING :: {0} processing errors occurred".format(errors))


def _get_documents(throttle, verbose):
    """Yields documents for processing."""
    scanned = 0
    yielded = 0
    for project, source, url, encoding in _get_feed_entries():
        scanned = scanned + 1
        ctx = _DocumentInfo(project, source, url, encoding, yielded + 1, verbose)
        if not ctx.exists:
            yielded = yielded + 1
            yield ctx

        # ... apply throttle
        if throttle and throttle == yielded:
            break

    # Log processing stats.
    _log_processing_stats(scanned, yielded, io.get_count(io.DIR_RAW_ERROR))


def _log_start(ctx):
    """Writes a processing start message to standard output."""
    if ctx.verbose:
        msg = "processing doc {0}: {1} --> {2} --> {3}"
        rt.log(msg.format(ctx.index, ctx.project, ctx.source, ctx.url))


def _download(ctx):
    """Attempts to download document from remote endpoint."""
    try:
        ctx.r = _SESSION.get(ctx.url)
    except Exception as err:
        raise _DownloadException(err)
    else:
        if ctx.r.status_code != 200:
            raise _DownloadException()


def _encode_content(ctx):
    """Encodes document content."""
    try:
        ctx.content = ctx.r.text.encode(_ENCODING)
    except Exception as err:
        raise _EncodingException(err)


def _parse_content(ctx):
    """Parses document content."""
    ctx.content = \
        content_parser.parse(ctx.project, ctx.source, ctx.content)


def _write_raw(ctx):
    """Writes a downloaded document to the file system."""
    try:
        with open(ctx.fpath, 'w') as output:
            output.seek(0)
            output.write(str(ctx.content))
    except IOError as err:
        raise _IOException(err)
    else:
        ctx.exists = True


def _log_error(ctx):
    """Write processing error message to standard output."""
    msg = "ARCHIVE ERROR :: processing document {0}: {1} ---> {2}"
    msg = msg.format(ctx.index, ctx.project, ctx.error)
    rt.log(msg)


def _write_error(ctx):
    """Writes document processing error to file system."""
    try:
        with open(ctx.fpath_error, 'wb') as output:
            output.seek(0)
            output.write(u"------------------------------------------------------------\n")
            output.write(u"ES-DOC ARCHIVE BUILD ERROR @ {} \n".format(datetime.datetime.now()))
            output.write(u"------------------------------------------------------------\n")
            output.write(u"An error occurred whilst pulling a document from a remote source:\n\n")
            output.write(u"\tPROJECT = {0};\n".format(ctx.project))
            output.write(u"\tDOCUMENT URL = {0};\n".format(ctx.url))
            output.write(u"\tDOCUMENT ENCODING = {0};\n".format(ctx.encoding))
            output.write(u"\tERROR = {0}.".format(unicode(ctx.error)))
    except IOError:
        rt.log("Document processing error handling failed.")


def _process(ctx):
    """Document processor."""
    rt.invoke(ctx,
              (_log_start, _download, _encode_content, _parse_content, _write_raw),
              (_log_error, _write_error))


def execute(throttle=0, verbose=False):
    """Writes pulled documents to file system.

    :param int throttle: Limits number of documents to be pulled.
    :param bool verbose: Flag indicating whether logging is verbose.

    """
    pool = ThreadPool()
    pool.map(_process, _get_documents(throttle, verbose))
    pool.close()
