"""
.. module:: cim.v1.types.data.data_extent.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:08.044653.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.data.data_extent_geographical import DataExtentGeographical
from pyesdoc.ontologies.cim.v1.types.data.data_extent_temporal import DataExtentTemporal


class DataExtent(object):
    """A concrete class within the cim v1 type system.

    A data object extent represents the geographical and temporal coverage associated with a data object.
    """

    def __init__(self):
        """Constructor"""
        super(DataExtent, self).__init__()
        self.geographical = None                     # type = data.DataExtentGeographical
        self.temporal = None                         # type = data.DataExtentTemporal


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
        append(d, 'geographical', self.geographical, False, False, False)
        append(d, 'temporal', self.temporal, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

