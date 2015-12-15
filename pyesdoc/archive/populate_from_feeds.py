# -*- coding: utf-8 -*-
"""
.. module:: populate_from_feeds.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Populates archive with documents pulled from 3rd party ATOM feeds.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import hashlib
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

import feedparser

from pyesdoc.archive import manager as archive
from pyesdoc.archive import config
from pyesdoc.archive import feed_entry_processor
from pyesdoc.utils import runtime



class _FeedEntryInfo(object):
    """Encapsulates feed entry information.

    """
    def __init__(self, project, feed, entry):
        """Object constructor.

        """
        self.encoding = feed.encoding
        self.project = project.name
        self.source = feed.source
        self.url = entry.links[0]['href']
        self.url_hash = hashlib.md5(self.url).hexdigest()


class _DocumentProcessingInfo(object):
    """Encapsulates document processing information.

    """
    def __init__(self, archive, entry, index, verbose):
        """Object constructor.

        :param ArchiveInfo archive: Archive manager.
        :param _FeedEntryInfo entry: Feed entry information.
        :param int index: Document processing id.
        :param bool verbose: Logging level flag.

        """
        self.content = None
        self.download = None
        self.entry = entry
        self.error = None
        self.file = archive.get_file(entry.project,
                                     entry.source,
                                     entry.url_hash,
                                     entry.encoding)
        self.index = index
        self.project = entry.project
        self.source = entry.source
        self.verbose = verbose


    def __repr__(self):
        """Object representation.

        """
        return "{0} :: {1} :: {2} :: {3} :: {4}".format(
            self.project,
            self.source,
            self.file.name,
            self.entry.url,
            self.file.exists
            )

    @property
    def folder(self):
        """Gets associated archive folder.

        """
        return self.file.folder


def _log(msg):
    """Logging helper function.

    """
    runtime.log(msg)


def _yield_feeds(project_filter=None):
    """Yields feeds to be processed.

    """
    for project in config.get_projects():
        if project_filter and project.name != project_filter:
            continue
        for feed in [f for f in project.feeds if f.is_active]:
            msg = "processing feed: {0} --> {1} --> {2}"
            msg = msg.format(project.name, feed.source, feed.url)
            _log(msg)
            yield project, feed


def _yield_feed_entries(project_filter=None):
    """Yields active feed entries.

    """
    for project, feed in _yield_feeds(project_filter):
        for entry in feedparser.parse(feed.url).entries:
            yield _FeedEntryInfo(project, feed, entry)


def _yield_documents(archive, project, throttle, verbose):
    """Yields documents for processing.

    """
    scanned = yielded = 0
    for entry in _yield_feed_entries(project):
        scanned += 1
        ctx = _DocumentProcessingInfo(archive, entry, yielded + 1, verbose)
        if not ctx.file.exists:
            yielded += 1
            yield ctx

        # ... apply throttle
        if throttle and throttle == yielded:
            break

    # Log processing stats.
    msg = "{0} feed entries scanned: {1} requires processing"
    msg = msg.format(scanned, yielded)
    _log(msg)
    errors = archive.get_error_count()
    if errors:
        msg = "WARNING :: {0} processing errors occurred".format(errors)
        _log(msg)


def execute(throttle, project=None, in_parallel=True):
    """Writes pulled documents to local file system.

    :param int throttle: A limit upon the number of documents to pull.
    :param str project: Name of a supported project (e.g. cmip6).
    :param bool in_parallel: Flag indicating whether job will leverage multiple cores.

    """
    archive.delete_error_files()
    pool = Pool() if in_parallel else ThreadPool()
    pool.map(feed_entry_processor.process,
             _yield_documents(archive, project, throttle, throttle > 0))
    pool.close()
