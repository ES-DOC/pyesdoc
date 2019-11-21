"""
.. module:: file_info.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
    :synopsis: An archived document file wrapper.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import glob
import os

import pyesdoc
from pyesdoc import exceptions



class ArchiveFileInfo(object):
    """Represents an archived file.

    """
    def __init__(self, folder, path):
        """Instance constructor.

        """
        name = path.split("/")[-1]
        parts = name.split('.')[0].split("_")

        self.encoding = name.split('.')[-1]
        self.hashid = parts[3] if len(parts) == 4 else parts[0]
        self.folder = folder
        self.name = name
        self.parts = parts
        self.path = path
        self.path_error = "{}.ERROR".format(path.split('.')[0])
        self.type = parts[0] if len(parts) == 4 else None
        self.uid = parts[1] if len(parts) == 4 else None
        self.version = parts[2] if len(parts) == 4 else None


    def __repr__(self):
        """Instance representation.

        """
        return self.path


    @property
    def exists(self):
        """Gets flag indicating whether a matching file exists.

        """
        if os.path.exists(self.path):
            return True
        else:
            path = "*{0}.{1}".format(self.hashid, self.encoding)
            path = os.path.join(self.folder.path, path)
            return len(glob.glob(path)) == 1

    @property
    def is_raw(self):
        """Gets flag indicating whether the file is a raw unparsed file.

        """
        return len(self.parts) == 1

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


    def delete(self):
        """Deletes underlying file from local file system.

        """
        if self.exists:
            os.remove(self.path)


    def get_document(self, extend=True):
        """Returns deserialized document.

        :returns: Deserialized archived document.
        :rtype: object

        """
        # Read from file system.
        try:
            document = pyesdoc.read(self.path)
        except Exception as err:
            raise exceptions.LoadingException(err)

        # Parse - performs project/source specific processing.
        try:
            pyesdoc.archive.parse(document, self.encoding, self.project, self.source)
        except Exception as err:
            raise exceptions.ParsingException(err)

        # Extend - performs generic processing.
        if extend:
            try:
                pyesdoc.extend(document)
            except exceptions.ExtendingException as err:
                raise err
            except Exception as err:
                raise exceptions.ExtendingException(err)

        return document


    def get_content(self, encoding):
        """Returns content of an archived file in the desired encoding.

        :param str encoding: Desired document content encoding.

        :returns: The contents of an archived file in the desired encoding.
        :rtype: unicode

        """
        return pyesdoc.encode(self.get_document(), encoding)
