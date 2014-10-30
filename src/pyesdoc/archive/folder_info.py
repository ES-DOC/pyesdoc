# -*- coding: utf-8 -*-
"""
.. module:: folder_info.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: An archive folder information wrapper.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import glob, os

from . import config
from ..extensions import extend as extend_doc
from ..io import read as read_doc
from file_info import FileInfo



# Organized folder.
_FOLDER_ORGANIZED = "organized"

# Raw folder.
_FOLDER_RAW = "raw"

# All files filter.
_FILE_FILTER_ALL = "*.*"


class FolderInfo(object):
    """An archive folder.

    """
    def __init__(self, project, source, managed_dir, path):
        """Object constructor.

        """
        self.managed_dir = managed_dir.lower()
        self.path = path
        self.path_all_files = os.path.join(self.path, _FILE_FILTER_ALL)
        self.project = project.lower()
        self.source = source.lower()


    def __repr__(self):
        """Object representation.

        """
        return "{0}".format(self.path)


    @property
    def is_organized(self):
        """Get flag indicating whether this is an organized folder."""
        return self.managed_dir == _FOLDER_ORGANIZED


    @property
    def is_raw(self):
        """Get flag indicating whether this is an organized folder."""
        return self.managed_dir == _FOLDER_RAW


    def yield_files(self, file_filter=None):
        """Yields set of files.

        :param str file_filter: Optional file filter.

        :returns: Set of file paths.
        :rtype: generator

        """
        if not file_filter:
            file_filter = _FILE_FILTER_ALL
        for fpath in glob.iglob(os.path.join(self.path, file_filter)):
            yield FileInfo(self, fpath)


    def yield_documents(self, file_filter=None):
        """Yields set of documents.

        :param str file_filter: Optional file filter.

        :returns: Set of file paths.
        :rtype: generator

        """
        for file_info in self.yield_files(file_filter):
            yield extend_doc(read_doc(file_info.path))


    def get_file_count(self):
        """Returns file count.

        """
        return len(glob.glob(self.path_all_files))


    def delete_files(self, file_filter=None):
        """Deletes folder files.

        """
        for file_info in self.yield_files(file_filter):
            os.remove(file_info.path)
