# -*- coding: utf-8 -*-
"""
.. module:: folder_info.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: An archive file information wrapper.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os


class FileInfo(object):
    """Represents an archived file.

    """
    def __init__(self, folder, fpath):
        """Object constructor.

        """
        self.folder = folder
        self.path = fpath
        self.encoding = fpath.split('.')[-1]


    @property
    def project(self):
        """Gets project with which file is associated.

        """
        return self.folder.project


    @property
    def source(self):
        """Gets source with which file is associated.

        """
        return self.folder.source


    @property
    def managed_dir(self):
        """Gets name of managed directory with which file is associated.

        """
        return self.folder.managed_dir


    @property
    def name(self):
        """Get file name.

        """
        return self.path.split("/")[-1]


    @property
    def exists(self):
        """Gets flag indicating whether file exists.

        """
        return os.path.exists(self.path)
