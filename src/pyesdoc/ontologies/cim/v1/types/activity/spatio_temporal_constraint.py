"""
.. module:: cim.v1.types.activity.spatio_temporal_constraint.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.227528.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.activity.numerical_requirement import NumericalRequirement
from pyesdoc.ontologies.cim.v1.types.shared.date_range import DateRange
from pyesdoc.ontologies.cim.v1.types.activity.resolution_type import ResolutionType


class SpatioTemporalConstraint(NumericalRequirement):
    """A concrete class within the cim v1 type system.

    Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.
    """

    def __init__(self):
        """Constructor"""
        super(SpatioTemporalConstraint, self).__init__()
        self.date_range = None                       # type = shared.DateRange
        self.spatial_resolution = ''                 # type = activity.ResolutionType

        self.requirement_type = str("spatioTemporalConstraint")


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
        d = dict(super(SpatioTemporalConstraint, self).as_dict())
        append(d, 'date_range', self.date_range, False, False, False)
        append(d, 'spatial_resolution', self.spatial_resolution, False, False, True)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

