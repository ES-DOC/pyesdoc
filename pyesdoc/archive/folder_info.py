"""
.. module:: file_info.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
    :synopsis: An archived document folder wrapper.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import glob
import os

import pyesdoc
from pyesdoc.archive import constants
from pyesdoc.archive.file_info import ArchiveFileInfo
from pyesdoc.constants import DEFAULT_ENCODING
from pyesdoc._extensions import extend as extend_doc
from pyesdoc._io import read as read_doc



def _get_file_filterset():
    """Returns set of supported file filters.

    """
    result = constants.FILE_FILTER_SET
    for doc_type in pyesdoc.ontologies.get_doc_type_keyset():
        result.add("{}_*.*".format(doc_type.replace(".", "-").lower()))

    return result


class ArchiveFolderInfo(object):
    """An archive folder.

    """
    def __init__(self, project, source, path):
        """Instance constructor.

        """
        self.path = path
        self.project = project.lower()
        self.source = source.lower()
        self._paths = \
            { ff: os.path.join(path, ff) for ff in _get_file_filterset() }


    def __repr__(self):
        """Instance representation.

        """
        return "{0}".format(self.path)


    @property
    def exists(self):
        """Gets flag indicating whether folder exists.

        """
        return os.path.exists(self.path)


    def delete(self):
        """Deletes underlying folder from local file system.

        """
        if self.exists:
            os.remove(self.path)


    def get_count(self, file_filter=None):
        """Returns file count.

        """
        if not file_filter:
            file_filter = constants.FILE_FILTER_ALL
        return len(glob.glob(self._paths[file_filter]))


    def yield_documents(self, file_filter=None):
        """Yields set of documents.

        :param str file_filter: Optional file filter.

        :returns: Set of file paths.
        :rtype: generator

        """
        for file_info in self.yield_files(file_filter):
            yield extend_doc(read_doc(file_info.path))


    def yield_files(self, file_filter=None):
        """Yields set of files.

        :param str file_filter: Optional file filter.

        :returns: Set of file paths.
        :rtype: generator

        """
        if file_filter is None or file_filter == "*":
            file_filter = constants.FILE_FILTER_ALL
        elif file_filter != constants.FILE_FILTER_ERROR and file_filter.find("_") == -1:
            file_filter = "{}_*.*".format(file_filter)
        for fpath in glob.iglob(self._paths[file_filter]):
            yield ArchiveFileInfo(self, fpath)


    def find_file(self, uid, version):
        """Yields files for processing.

        :param str uid: Document unique identifier.
        :param str version: Document version.

        :returns: A file wrapper to be processed.
        :rtype: pyesdoc.archive.ArchiveFileInfo

        """
        try:
            int(version)
        except ValueError:
            file_filter = "*_{}_*.*".format(uid)
        else:
            file_filter = "*_{}_{}_*.*".format(uid, version)
        files = glob.glob(os.path.join(self.path, file_filter))
        if files:
            return ArchiveFileInfo(self, sorted(files)[-1])


    def write(self, doc):
        """Writes a document to the archive.

        :param object doc: Document to be written.

        :returns: Pointer to archive file.
        :rtype: pyesdoc.archive.ArchiveFileInfo

        """
        # Ensure document is extended.
        extend_doc(doc)

        # Set file path.
        fname = "{}_{}_{}.{}".format(doc.meta.type, doc.meta.id, doc.meta.version, DEFAULT_ENCODING)
        fpath = os.path.join(self.path, fname)

        # Write to file system.
        with open(fpath, 'w') as fstream:
            fstream.write(pyesdoc.encode(doc, DEFAULT_ENCODING))

        # Return file wrapper.
        return ArchiveFileInfo(self, fpath)
