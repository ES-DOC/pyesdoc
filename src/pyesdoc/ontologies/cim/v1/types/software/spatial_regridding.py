"""
.. module:: cim.v1.types.software.spatial_regridding.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:08.100250.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.software.spatial_regridding_dimension_type import SpatialRegriddingDimensionType
from pyesdoc.ontologies.cim.v1.types.software.spatial_regridding_property import SpatialRegriddingProperty
from pyesdoc.ontologies.cim.v1.types.software.spatial_regridding_standard_method_type import SpatialRegriddingStandardMethodType
from pyesdoc.ontologies.cim.v1.types.software.spatial_regridding_user_method import SpatialRegriddingUserMethod


class SpatialRegridding(object):
    """A concrete class within the cim v1 type system.

    Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.
    """

    def __init__(self):
        """Constructor"""
        super(SpatialRegridding, self).__init__()
        self.dimension = ''                          # type = software.SpatialRegriddingDimensionType
        self.properties = []                         # type = software.SpatialRegriddingProperty
        self.standard_method = ''                    # type = software.SpatialRegriddingStandardMethodType
        self.user_method = None                      # type = software.SpatialRegriddingUserMethod


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
        append(d, 'dimension', self.dimension, False, False, True)
        append(d, 'properties', self.properties, True, False, False)
        append(d, 'standard_method', self.standard_method, False, False, True)
        append(d, 'user_method', self.user_method, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

