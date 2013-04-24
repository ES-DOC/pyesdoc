"""
.. module:: cim.v1_5.types.activity.experiment_relationship.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1.5 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-04-17 17:20:28.655320.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1_5.types.shared.cim_relationship import CimRelationship
from pyesdoc.ontologies.cim.v1_5.types.activity.experiment_relationship_target import ExperimentRelationshipTarget
from pyesdoc.ontologies.cim.v1_5.types.activity.experiment_relationship_type import ExperimentRelationshipType


class ExperimentRelationship(CimRelationship):
    """A concrete class within the cim v1.5 type system.

    Contains a set of relationship types specific to a experiment document that can be used to describe its genealogy.
    """

    def __init__(self):
        """Constructor"""
        super(ExperimentRelationship, self).__init__()
        self.target = None                           # type = activity.ExperimentRelationshipTarget
        self.type = ''                               # type = activity.ExperimentRelationshipType


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
        d = dict(super(ExperimentRelationship, self).as_dict())
        append(d, 'target', self.target, False, False, False)
        append(d, 'type', self.type, False, False, True)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

