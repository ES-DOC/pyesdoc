"""
.. module:: cim.v1_5.types.data.data_extent_temporal.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1.5 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-04-17 17:20:28.668519.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1_5.types.data.data_extent_time_interval import DataExtentTimeInterval


class DataExtentTemporal(object):
    """A concrete class within the cim v1.5 type system.

    A data object temporal extent represents the temporal coverage associated with a data object.
    """

    def __init__(self):
        """Constructor"""
        super(DataExtentTemporal, self).__init__()
        self.begin = datetime.date(1900, 1, 1)       # type = datetime.date
        self.end = datetime.date(1900, 1, 1)         # type = datetime.date
        self.time_interval = None                    # type = data.DataExtentTimeInterval


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
        append(d, 'begin', self.begin, False, True, False)
        append(d, 'end', self.end, False, True, False)
        append(d, 'time_interval', self.time_interval, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

