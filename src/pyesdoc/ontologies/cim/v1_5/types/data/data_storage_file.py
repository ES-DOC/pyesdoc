"""
.. module:: cim.v1_5.types.data.data_storage_file.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1.5 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-04-17 17:20:28.674535.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1_5.types.data.data_storage import DataStorage


class DataStorageFile(DataStorage):
    """A concrete class within the cim v1.5 type system.

    Contains attributes to describe a DataObject stored as a single file.
    """

    def __init__(self):
        """Constructor"""
        super(DataStorageFile, self).__init__()
        self.file_name = str()                       # type = str
        self.file_system = str()                     # type = str
        self.path = str()                            # type = str


    def as_dict(self):
        """Returns a deep dictionary representation.

        """
        def append(d, key, value, is_iterative, is_primitive, is_enum):
            if value is None:
                if is_iterative:
                    value = []
            elif is_primitive == False and is_enum == False:
                if is_iterative:
                    value = map(lambda i : i.as_dict(), value)
                else:
                    value = value.as_dict()
            d[key] = value

        # Populate a deep dictionary.
        d = dict(super(DataStorageFile, self).as_dict())
        append(d, 'file_name', self.file_name, False, True, False)
        append(d, 'file_system', self.file_system, False, True, False)
        append(d, 'path', self.path, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

