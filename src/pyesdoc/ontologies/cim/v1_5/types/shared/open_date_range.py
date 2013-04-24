"""
.. module:: cim.v1_5.types.shared.open_date_range.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1.5 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-04-17 17:20:28.700872.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1_5.types.shared.date_range import DateRange


class OpenDateRange(DateRange):
    """A concrete class within the cim v1.5 type system.

    A date range without a specified start and/or end point.
    """

    def __init__(self):
        """Constructor"""
        super(OpenDateRange, self).__init__()
        self.end = datetime.datetime.now()           # type = datetime.datetime
        self.start = datetime.datetime.now()         # type = datetime.datetime


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
        d = dict(super(OpenDateRange, self).as_dict())
        append(d, 'end', self.end, False, True, False)
        append(d, 'start', self.start, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

