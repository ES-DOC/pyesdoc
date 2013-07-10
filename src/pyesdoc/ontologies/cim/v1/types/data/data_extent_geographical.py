"""
.. module:: cim.v1.types.data.data_extent_geographical.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.229412.

"""

# Module imports.
import datetime
import types
import uuid



class DataExtentGeographical(object):
    """A concrete class within the cim v1 type system.

    A data object geographical extent represents the geographical coverage associated with a data object.
    """

    def __init__(self):
        """Constructor"""
        super(DataExtentGeographical, self).__init__()
        self.east = float()                          # type = float
        self.north = float()                         # type = float
        self.south = float()                         # type = float
        self.west = float()                          # type = float


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
        d = dict()
        append(d, 'east', self.east, False, True, False)
        append(d, 'north', self.north, False, True, False)
        append(d, 'south', self.south, False, True, False)
        append(d, 'west', self.west, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

