"""
.. module:: cim.v1.types.data.data_extent_time_interval.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.182750.

"""

# Module imports.
import datetime
import types
import uuid



class DataExtentTimeInterval(object):
    """A concrete class within the cim v1 type system.

    A data object temporal extent represents the temporal coverage associated with a data object.
    """

    def __init__(self):
        """Constructor"""
        super(DataExtentTimeInterval, self).__init__()
        self.factor = int()                          # type = int
        self.radix = int()                           # type = int
        self.unit = str()                            # type = str


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
        append(d, 'factor', self.factor, False, True, False)
        append(d, 'radix', self.radix, False, True, False)
        append(d, 'unit', self.unit, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

