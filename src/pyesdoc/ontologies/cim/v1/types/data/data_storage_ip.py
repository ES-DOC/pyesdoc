"""
.. module:: cim.v1.types.data.data_storage_ip.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:08.053348.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.data.data_storage import DataStorage


class DataStorageIp(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a database file.
    """

    def __init__(self):
        """Constructor"""
        super(DataStorageIp, self).__init__()
        self.file_name = str()                       # type = str
        self.host = str()                            # type = str
        self.path = str()                            # type = str
        self.protocol = str()                        # type = str


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
        d = dict(super(DataStorageIp, self).as_dict())
        append(d, 'file_name', self.file_name, False, True, False)
        append(d, 'host', self.host, False, True, False)
        append(d, 'path', self.path, False, True, False)
        append(d, 'protocol', self.protocol, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

