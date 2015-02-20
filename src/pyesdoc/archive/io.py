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

from pyesdoc import constants
from pyesdoc.archive import config
from pyesdoc.archive.folder_info import FolderInfo
from pyesdoc.archive.file_info import FileInfo
from pyesdoc.extensions import extend as extend_doc
from pyesdoc.io import (
    read as read_doc,
    write as write_doc
    )
from pyesdoc.utils import runtime as rt


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
    DIR_ORGANIZED_ERROR,
    DIR_PARSED,
    DIR_PARSED_ERROR,
    DIR_RAW,
    DIR_RAW_ERROR
}

# Set of folders.
_FOLDERS = []


def get_folder(project, source, managed, sub_dir=None):
    """Returns an archive folder wrapper.

    """
    # Set managed directory.
    path = config.DIR_ARCHIVE
    for name in (managed, project, source):
        path = os.path.join(path, name)

    # Set sub-directory.
    if sub_dir:
        path = os.path.join(path, sub_dir)

    # Ensure directory exists.
    if not os.path.exists(path):
        os.makedirs(path)

    return FolderInfo(project, source, managed, path)


def _init():
    """Initializes file system in readiness for IO.

    """
    if _FOLDERS:
        return

    rt.log("Initializing archive folders")
    _init_config_folders()

    # Walk archive sub-directories.
    root_level = len(config.DIR_ARCHIVE.split('/'))
    for path in (x[0] for x in os.walk(config.DIR_ARCHIVE)):
        parts = path.split('/')
        if len(parts) - root_level == 3:
            offset = 0
        elif len(parts) - root_level == 4:
            offset = -1
        else:
            continue

        managed = parts[offset - 3]
        project = parts[offset - 2]
        source = parts[offset - 1]

        _FOLDERS.append(FolderInfo(project, source, managed, path))


def _init_config_folders():
    """Initializes archive folders from pyesdoc.conf.

    """
    for project, source in config.get_project_sources():
        for managed in MANAGED_FOLDERS:
            path = config.DIR_ARCHIVE
            path = os.path.join(path, managed)
            path = os.path.join(path, project)
            path = os.path.join(path, source)
            if not os.path.exists(path):
                os.makedirs(path)


def _init_doc_folders(doc):
    """Initializes archive folders for a new document.

    """
    for managed_dir in (
        DIR_ORGANIZED,
        DIR_ORGANIZED_ERROR,
        DIR_INGESTED,
        DIR_INGESTED_ERROR
        ):
        doc_folder = get_doc_folder(doc, managed_dir)
        cached = [f for f in get_folders(managed_dir)
                  if f.path == doc_folder.path]
        if not cached:
            _FOLDERS.append(doc_folder)


def get_folders(managed_filter=None):
    """Returns set of folders for processing.

    """
    _init()
    if managed_filter:
        managed_filter = managed_filter.lower()
        return [f for f in _FOLDERS if f.managed_dir == managed_filter]
    else:
        return _FOLDERS


def get_doc_file(doc, managed_dir):
    """Returns a folder into which document information will be written.

    """
    folder = get_doc_folder(doc, managed_dir)
    fname = "{0}_{1}.json".format(doc.meta.id, doc.meta.version)
    fpath = os.path.join(folder.path, fname)

    return FileInfo(folder, fpath)


def get_doc_folder(doc, managed_dir, project=None, source=None):
    """Returns a folder into which document information will be written.

    """
    if project is None:
        project = doc.meta.project
    if source is None:
        source = doc.meta.source
    if managed_dir != DIR_ORGANIZED:
        type_dir = None
    else:
        try:
            type_dir = doc.meta.type.replace(".", "-").lower()
        except AttributeError:
            type_dir = doc.lower()

    return get_folder(project, source, managed_dir, type_dir)


def get_doc_organized_folder(doc, project=None, source=None):
    """Returns a document's organized folder.

    :param str project: Name of a supported project.
    :param str source: Name of a document source (e.g. esdoc-q).
    :param doc: A document or a document type.
    :type doc: str \ object

    :returns Pointer to an organized document directory.:
    :rtype: str

    """
    return get_doc_folder(doc, DIR_ORGANIZED, project, source)


def yield_raw():
    """Yields raw files.

    :returns: Set of raw files pulled from ATOM feeds.
    :rtype: generator

    """
    for folder in get_folders(DIR_RAW):
        for raw_file in folder.yield_files():
            yield raw_file


def yield_ingestable():
    """Yields ingestable documents.

    :return: Documents to be ingested.
    :rtype: generator

    """
    for organized in get_folders(DIR_ORGANIZED):
        ingested = get_folder(organized.project, organized.source, DIR_INGESTED)
        for organized_file in organized.yield_files("*.json"):
            ingested_fpath = os.path.join(ingested.path, organized_file.name)
            if not os.path.exists(ingested_fpath):
                yield organized_file, FileInfo(ingested, ingested_fpath)


def delete_files(managed_dir):
    """Deletes file from a managed folder.

    """
    for folder in get_folders(managed_dir):
        folder.delete_files()


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


def _get_latest_version_id(uid):
    """Returns id of latest version.

    """
    fname = "{0}*.*".format(uid)
    for folder in get_folders(DIR_ORGANIZED):
        fpath = os.path.join(folder.path, fname)
        versions = [int(f.split('/')[-1].split('.')[0].split('_')[1])
                    for f in glob.glob(fpath)]
        if versions:
            return max(versions)


def get_organized_filepath(uid, version, load_original=False):
    """Returns filepath to an organized document.

    """
    if version == constants.ESDOC_DOC_VERSION_LATEST:
        version = _get_latest_version_id(uid)
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
        raise IOError("Document does not exist within archive: {0}-{1}.".format(uid, version))


def write(doc):
    """Writes a document to archive.

    :returns: File information.
    :rtype: pyesdoc.archive.FileInfo

    """
    # Initialize archive folders.
    _init_doc_folders(doc)

    # Write document.
    doc_file = get_doc_file(doc, DIR_ORGANIZED)
    write_doc(doc, fpath=doc_file.path)

    return doc_file


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
        if doc:
            return extend_doc(doc) if extend else doc


def delete(uid, version):
    """Deletes a document from archive.

    :param str uid: Document unique identifier.
    :param str version: Document version.

    """
    filepath = get_organized_filepath(uid, version)
    if filepath:
        os.remove(filepath)
