"""
.. module:: io.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: IO utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# -*- coding: utf-8 -*-

# Module imports.
import glob
import os

from . import config
from ..io import read as read_doc
from ..extensions import extend as extend_doc



# Ingested sub-directory.
DIR_INGESTED = "ingested"

# Ingest error sub-directory.
DIR_INGESTED_ERROR = "ingested_error"

# Organized sub-directory.
DIR_ORGANIZED = "organized"

# Parsed sub-directory.
DIR_PARSED = "parsed"

# Parsed error sub-directory.
DIR_PARSED_ERROR = "parsed_error"

# Raw sub-directory.
DIR_RAW = "raw"

# Raw error sub-directory.
DIR_RAW_ERROR = "raw_error"

# Set of sub-directories.
SUB_DIRECTORIES = {
    DIR_INGESTED,
    DIR_INGESTED_ERROR,
    DIR_ORGANIZED,
    DIR_PARSED,
    DIR_PARSED_ERROR,
    DIR_RAW,
    DIR_RAW_ERROR
}


def _init():
    """Initialize document directories.

    """
    for project, source in config.get_project_sources():
        for sub_dir in SUB_DIRECTORIES:
            doc_dir = config.DIR_ARCHIVE
            for name in (project, source, sub_dir):
                doc_dir = os.path.join(doc_dir, name)
                if not os.path.exists(doc_dir):
                    os.makedirs(doc_dir)
_init()


def get_doc_dir(project, source, sub_dir):
    """Returns a project directory pointer in readiness for io.

    :param str project: Name of a supported project.
    :param str source: Name of a document source (e.g. esdoc-q).
    :param str sub_dir: Name of a sub-directory.

    :rtype: str

    """
    folder = config.DIR_ARCHIVE
    for name in (project, source, sub_dir):
        folder = os.path.join(folder, name)

    return folder


def get_organized_dir(project, source, doc):
    """Returns an organized document directory pointer.

    :param str project: Name of a supported project.
    :param str source: Name of a document source (e.g. esdoc-q).
    :param object doc: A document or a document type.

    :rtype: str

    """
    # Set document type.
    try:
        doc_type = doc.meta.type.replace(".", "-").lower()
    except AttributeError:
        doc_type = doc.lower()

    # Set organized root directory.
    doc_dir = get_doc_dir(project, source, DIR_ORGANIZED)

    # Set organized document type sub-directory.
    doc_dir = os.path.join(doc_dir, doc_type)

    # JIT create.
    if not os.path.exists(doc_dir):
        os.makedirs(doc_dir)

    return doc_dir


def yield_doc_dir(sub_dir):
    """Yields set of document directories.

    :param str sub_dir: Document sub-directory.

    :rtype: generator

    """
    for project, source in config.get_project_sources():
        yield get_doc_dir(project, source, sub_dir)


def yield_organized_dirs():
    """Yields organized directories.

    :rtype: generator

    """
    for organized_dir in yield_doc_dir(DIR_ORGANIZED):
        for doc_type in os.listdir(organized_dir):
            yield os.path.join(organized_dir, doc_type)


def yield_organized_documents(type_filter=None):
    """Yields organized documents.

    :param str type_filter: Limits the type of documents to process.

    :rtype: generator

    """
    for organized_dir in yield_doc_dir(DIR_ORGANIZED):
        for doc_type in os.listdir(organized_dir):
            doc_dir = os.path.join(organized_dir, doc_type)
            doc_dir = os.path.join(doc_dir, "*.json")
            for doc_fpath in glob.iglob(doc_dir):
                yield extend_doc(read_doc(doc_fpath))


def yield_ingestable_documents():
    """Yields ingestable documents.

    :rtype: generator

    """
    for organized_dir in yield_doc_dir(DIR_ORGANIZED):
        for doc_type in os.listdir(organized_dir):
            dirpath = os.path.join(organized_dir, doc_type)
            dirpath = os.path.join(dirpath, "*.json")
            for fpath in glob.iglob(dirpath):
                fpath_ingested = fpath.replace(DIR_ORGANIZED, DIR_INGESTED)
                if not os.path.exists(fpath_ingested):
                    yield extend_doc(read_doc(fpath)), fpath, fpath_ingested


def get_documents(sub_dir):
    """Yields documents for processing.

    :param str sub_dir: Sub-directory to be processed.

    :rtype: generator

    """
    for project, source in config.get_project_sources():
        doc_dir = get_doc_dir(project, source, sub_dir)
        doc_files = os.path.join(doc_dir, "*.*")
        for doc_fpath in glob.iglob(doc_files):
            yield project, source, doc_fpath


def get_count(sub_dir):
    """Returns sub-directory document count.

    :param str sub_dir: Sub-directory to be processed.

    :rtype: int

    """
    count = 0
    for project, source in config.get_project_sources():
        doc_dir = get_doc_dir(project, source, sub_dir)
        doc_dir = os.path.join(doc_dir, "*.*")
        count = count + len(glob.glob(doc_dir))

    return count


def get_counts():
    """Returns sub-directory document counts.

    :rtype: int

    """
    counts = []
    for project, source in config.get_project_sources():
        for sub_dir in SUB_DIRECTORIES:
            doc_dir = get_doc_dir(project, source, sub_dir)
            doc_dir = os.path.join(doc_dir, "*.*")
            counts.append(("{0}/{1}/{2}".format(project, source, sub_dir),
                           len(glob.glob(doc_dir))))

    return tuple(counts)


def get(uid, version, original=False):
    """Returns a document from archive.

    :param str uid: Document unique identifier.
    :param str version: Document version.
    :param bool original: Flag indicating whether original document is to be returned or not.

    :rtype: object | None

    """
    fname = "{0}_{1}.json" if not original else "{0}_{1}.original"
    for doc_dir in yield_organized_dirs():
        fpath = fname.format(uid, version)
        fpath = os.path.join(doc_dir, fpath)
        try:
            with open(fpath, 'r') as fcontent:
                return fcontent.read()
        except IOError as err:
            pass
