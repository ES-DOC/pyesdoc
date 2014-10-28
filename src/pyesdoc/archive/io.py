# -*- coding: utf-8 -*-
"""
.. module:: io.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: IO utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import glob, os

from . import config
from ..io import (
    read as read_doc,
    write as write_doc
    )
from ..extensions import extend as extend_doc
from folder_info import FolderInfo



# Ingested sub-directory.
DIR_INGESTED = "ingested"

# Ingest error sub-directory.
DIR_INGESTED_ERROR = "ingested_error"

# Organized sub-directory.
DIR_ORGANIZED = "organized"

# Organized error sub-directory.
DIR_ORGANIZED_ERROR = "organized_error"

# Parsed sub-directory.
DIR_PARSED = "parsed"

# Parsed error sub-directory.
DIR_PARSED_ERROR = "parsed_error"

# Raw sub-directory.
DIR_RAW = "raw"

# Raw error sub-directory.
DIR_RAW_ERROR = "raw_error"

# Set of managed folders.
MANAGED_FOLDERS = {
    DIR_INGESTED,
    DIR_INGESTED_ERROR,
    DIR_ORGANIZED,
    DIR_PARSED,
    DIR_PARSED_ERROR,
    DIR_RAW,
    DIR_RAW_ERROR
}


def get_folder(project, source, managed, sub_dir=None):
    """Returns an archive folder wrapper.

    """
    # Set managed directory.
    path = config.DIR_ARCHIVE
    for name in (project, source, managed):
        path = os.path.join(path, name)

    # Set sub-directory.
    if sub_dir:
        path = os.path.join(path, sub_dir)

    # Ensure directory exists.
    if not os.path.exists(path):
        os.makedirs(path)

    return FolderInfo(project, source, managed, path)


def get_folders(managed_filter=None):
    """Returns set of folders for processing.

    """
    result = []

    for project, source in config.get_project_sources():
        for managed in MANAGED_FOLDERS:
            # Escape if out of scope.
            if managed_filter and managed != managed_filter:
                continue

            # Set managed folder directory path.
            path = config.DIR_ARCHIVE
            for name in (project, source, managed):
                path = os.path.join(path, name)

            # Ensure directory exists.
            if not os.path.exists(path):
                os.makedirs(path)

            # Set sub-drectories.
            sub_dirs = [os.path.join(path, d) for d in os.listdir(path) \
                        if os.path.isdir(os.path.join(path, d))]

            # Append folders.
            if sub_dirs:
                for sub_dir in sub_dirs:
                    result.append(FolderInfo(project, source, managed, sub_dir))
            else:
                result.append(FolderInfo(project, source, managed, path))

    return result


def get_doc_organized_folder(project, source, doc):
    """Returns a document's organized folder.

    :param str project: Name of a supported project.
    :param str source: Name of a document source (e.g. esdoc-q).
    :param doc: A document or a document type.
    :type doc: str \ object

    :returns Pointer to an organized document directory.:
    :rtype: str

    """
    try:
        doc_type = doc.meta.type.replace(".", "-").lower()
    except AttributeError:
        doc_type = doc.lower()

    return get_folder(project, source, DIR_ORGANIZED, doc_type)


def yield_raw():
    """Yields raw files.

    :returns: Set of raw files pulled from ATOM feeds.
    :rtype: generator

    """
    for folder in get_folders(DIR_RAW):
        for raw_file in folder.yield_files():
            yield raw_file


def yield_organized():
    """Yields organized documents.

    :returns: Set of organized directories.
    :rtype: generator

    """
    for folder in get_folders(DIR_ORGANIZED):
        return folder.yield_documents(file_filter="*.json")


def yield_ingestable():
    """Yields ingestable documents.

    :return: Documents to be ingested.
    :rtype: generator

    """
    for folder in get_folders(DIR_ORGANIZED):
        for fpath in folder.yield_files():
            fpath_ingested = fpath.replace(DIR_ORGANIZED, DIR_INGESTED)
            if not os.path.exists(fpath_ingested):
                doc = extend_doc(read_doc(fpath))
                yield doc, fpath, fpath_ingested


def get_counts():
    """Returns sub-directory document counts.

    :rtype: int

    """
    counts = []
    for folder in get_folders():
        counts.append((folder.path, folder.get_file_count()))

    return tuple(counts)


def get_count(managed_dir):
    """Returns managed directory document count.

    :param str managed_dir: Managed directory to be processed.

    :rtype: int

    """
    count = 0
    for folder in get_folders(managed_dir):
        count += folder.get_file_count()

    return count


def get_count_all():
    """Returns count of all documents in archive.

    :rtype: int

    """
    count = 0
    for folder in get_folders():
        count += folder.get_file_count()

    return count


def get_organized_filepath(uid, version, load_original=False):
    """Returns filepath to an organized document.

    """
    fname = "{0}_{1}.json" if not load_original else "{0}_{1}.original"
    fname = fname.format(uid, version)
    for folder in get_folders(DIR_ORGANIZED):
        fpath = os.path.join(folder.path, fname)
        if os.path.exists(fpath):
            return fpath


def exists(uid, version):
    """Returns flag indicating whether a document is already archived.

    :param str uid: Document unique identifier.
    :param str version: Document version.

    :returns: Flag indicating whether a document is already archived.
    :rtype: boolean

    """
    return get_organized_filepath(uid, version) is not None


def load(uid, version, load_original=False, must_exist=False):
    """Loads a document from archive.

    :param str uid: Document unique identifier.
    :param str version: Document version.
    :param bool load_original: Flag indicating whether original document is to be returned or not.
    :param bool must_exist: Flag indicating whether the document is expected to exist within the archive.

    :rtype: object | None

    """
    fpath = get_organized_filepath(uid, version, load_original)
    if fpath:
        try:
            with open(fpath, 'r') as fcontent:
                return fcontent.read()
        except IOError:
            pass

    # Exception if the document was expected to exist.
    if must_exist:
        raise IOError("Document does not exist within archive: {0}.".format(fname))


def write(doc):
    """Writes a document to archive.

    """
    fname = "{0}_{1}.json"
    fname = fname.format(doc.meta.id, doc.meta.version)
    folder = get_doc_organized_folder(doc.meta.project, doc.meta.source, doc)
    fpath = os.path.join(folder.path, fname)

    write_doc(doc, fpath=fpath)


def read(uid, version, extend=True):
    """Reads a document from archive.

    :param str uid: Document unique identifier.
    :param str version: Document version.
    :param bool extend: Flag instructing whether to extend document.

    :returns: A document.
    :rtype: object

    """
    filepath = get_organized_filepath(uid, version)
    if filepath:
        doc = read_doc(filepath)
        return extend_doc(doc) if extend else doc


def delete(uid, version):
    """Deletes a document from archive.

    :param str uid: Document unique identifier.
    :param str version: Document version.

    """
    filepath = get_organized_filepath(uid, version)
    if filepath:
        os.remove(filepath)
