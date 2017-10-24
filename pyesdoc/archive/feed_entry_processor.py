# -*- coding: utf-8 -*-
"""
.. module:: downloader.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Downloads a document pulled from a 3rd party ATOM feed.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import datetime

import requests

import pyesdoc
from pyesdoc.utils import convert
from pyesdoc.utils import runtime



# Requests session - improves download times by pooling connection.
_SESSION = requests.Session()
_SESSION.mount('http://', requests.adapters.HTTPAdapter(
    pool_connections=100, pool_maxsize=100))


# Error file template.
_ERROR = """
------------------------------------------------------------
ES-DOC ARCHIVE ERROR @ {0}
------------------------------------------------------------
An error occurred whilst pulling a document from a remote source:

PROJECT = {1};
SOURCE = {2};
DOCUMENT URL = {3};
DOCUMENT ENCODING = {4};
ERROR TYPE = {5};
ERROR = {6}.

"""


class _DownloadException(Exception):
    """Exception raised when a download fails.

    """
    pass


class _EncodingException(Exception):
    """Exception raised when raw document encoding fails.

    """
    pass


class _IOException(Exception):
    """Exception raised when document io fails.

    """
    pass


class _ParsingException(Exception):
    """Exception raised when document parsing fails.

    """
    pass


def _log_start(ctx):
    """Writes a processing start message to standard output.

    """
    if ctx.verbose:
        msg = "processing doc {0}: {1} --> {2} --> {3}"
        pyesdoc.log(msg.format(ctx.index, ctx.project, ctx.source, ctx.entry.url))


def _download(ctx):
    """Attempts to download document from remote endpoint.

    """
    try:
        ctx.download = _SESSION.get(ctx.entry.url)
    except Exception as err:
        raise _DownloadException(err)
    else:
        if ctx.download.status_code != 200:
            raise _DownloadException()


def _set_content(ctx):
    """Set document content to be written to file system.

    """
    try:
        ctx.content = convert.unicode_to_str(ctx.download.text)
    except Exception as err:
        raise _EncodingException(err)


def _parse_content(ctx):
    """Parses document content.

    """
    try:
        ctx.content = pyesdoc.archive.parse(ctx.content,
                                            ctx.entry.encoding,
                                            ctx.project,
                                            ctx.source,
                                            "content")
    except Exception as err:
        raise _ParsingException(err)


def _write_content(ctx):
    """Writes downloaded document content to the file system.

    """
    try:
        with open(ctx.file.path, 'w') as output:
            output.write(ctx.content)
    except IOError as err:
        raise _IOException(err)


def _log_error(ctx):
    """Write processing error message to standard output.

    """
    msg = "ARCHIVE ERROR :: processing document {0}: {1} ---> {2}"
    msg = msg.format(ctx.index, ctx.project, ctx.error)
    pyesdoc.log_error(msg)


def _write_error(ctx):
    """Writes document processing error to file system.

    """
    try:
        with open(ctx.file.path_error, 'wb') as output:
            output.seek(0)
            output.write(_ERROR.format(
                datetime.datetime.now(),
                ctx.project,
                ctx.source,
                ctx.entry.url,
                ctx.entry.encoding,
                type(ctx.error),
                ctx.error
                ))
    except IOError:
        pyesdoc.log_error("Document processing error handling failed.")


def process(ctx):
    """Processes a document from a remote feed.

    :param object ctx: Document processing context.

    """
    tasks = (
        _log_start,
        _download,
        _set_content,
        _parse_content,
        _write_content
        )

    error_tasks = (
        _log_error,
        _write_error
        )

    runtime.invoke(ctx, tasks, error_tasks)
