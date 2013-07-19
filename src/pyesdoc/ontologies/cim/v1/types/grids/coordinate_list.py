"""
.. module:: cim.v1.types.grids.coordinate_list.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.188157.

"""

# Module imports.
import datetime
import types
import uuid



class CoordinateList(object):
    """A concrete class within the cim v1 type system.

    The CoordList type may be used to specify a list of coordinates, typically for the purpose of defining coordinates along the X, Y or Z axes. The length of the coordinate list is given by the attribute of that name. This may be used by software to allocate memory in advance of storing the coordinate values. The hasConstantOffset attribute may be used to indicate that the coordinate list consists of values with constant offset (spacing). In this case only the first coordinate value and the offset (spacing) value need to be specified; however, the length attribute must still define the final as-built size of the coordinate list.
    """

    def __init__(self):
        """Constructor"""
        super(CoordinateList, self).__init__()
        self.has_constant_offset = bool()            # type = bool
        self.length = int()                          # type = int
        self.uom = str()                             # type = str


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
        append(d, 'has_constant_offset', self.has_constant_offset, False, True, False)
        append(d, 'length', self.length, False, True, False)
        append(d, 'uom', self.uom, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

