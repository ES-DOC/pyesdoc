"""
.. module:: cim.v1_5.types.grids.vertical_coordinate_list.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1.5 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-04-17 17:20:28.683766.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1_5.types.grids.coordinate_list import CoordinateList
from pyesdoc.ontologies.cim.v1_5.types.grids.grid_property import GridProperty


class VerticalCoordinateList(CoordinateList):
    """A concrete class within the cim v1.5 type system.

    There are some specific attributes that are associated with vertical coordinates.
    """

    def __init__(self):
        """Constructor"""
        super(VerticalCoordinateList, self).__init__()
        self.form = str()                            # type = str
        self.properties = []                         # type = grids.GridProperty
        self.type = str()                            # type = str


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
        d = dict(super(VerticalCoordinateList, self).as_dict())
        append(d, 'form', self.form, False, True, False)
        append(d, 'properties', self.properties, True, False, False)
        append(d, 'type', self.type, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

