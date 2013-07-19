"""
.. module:: cim.v1.types.software.spatial_regridding_user_method.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.222874.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.data.data_object import DataObject
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference


class SpatialRegriddingUserMethod(object):
    """A concrete class within the cim v1 type system.

    Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.
    """

    def __init__(self):
        """Constructor"""
        super(SpatialRegriddingUserMethod, self).__init__()
        self.file = None                             # type = data.DataObject
        self.file_reference = None                   # type = shared.CimReference
        self.name = str()                            # type = str


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
        append(d, 'file', self.file, False, False, False)
        append(d, 'file_reference', self.file_reference, False, False, False)
        append(d, 'name', self.name, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

