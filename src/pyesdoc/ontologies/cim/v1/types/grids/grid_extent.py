"""
.. module:: cim.v1.types.grids.grid_extent.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.188574.

"""

# Module imports.
import datetime
import types
import uuid



class GridExtent(object):
    """A concrete class within the cim v1 type system.

    DataType for recording the geographic extent of a gridMosaic or gridTile.
    """

    def __init__(self):
        """Constructor"""
        super(GridExtent, self).__init__()
        self.maximum_latitude = str()                # type = str
        self.maximum_longitude = str()               # type = str
        self.minimum_latitude = str()                # type = str
        self.minimum_longitude = str()               # type = str
        self.units = str()                           # type = str


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
        append(d, 'maximum_latitude', self.maximum_latitude, False, True, False)
        append(d, 'maximum_longitude', self.maximum_longitude, False, True, False)
        append(d, 'minimum_latitude', self.minimum_latitude, False, True, False)
        append(d, 'minimum_longitude', self.minimum_longitude, False, True, False)
        append(d, 'units', self.units, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

