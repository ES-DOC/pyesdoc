"""
.. module:: cim.v1.types.software.spatial_regridding_property.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.271425.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.property import Property


class SpatialRegriddingProperty(Property):
    """A concrete class within the cim v1 type system.

    Used for OASIS-specific regridding information (ie: masked, order, normalisation, etc.)
    """

    def __init__(self):
        """Constructor"""
        super(SpatialRegriddingProperty, self).__init__()

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
        d = dict(super(SpatialRegriddingProperty, self).as_dict())
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

