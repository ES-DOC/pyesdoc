"""
.. module:: cim.v1.types.shared.cim_document_relationship.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.195423.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.cim_relationship import CimRelationship
from pyesdoc.ontologies.cim.v1.types.shared.cim_document_relationship_target import CimDocumentRelationshipTarget
from pyesdoc.ontologies.cim.v1.types.shared.cim_document_relationship_type import CimDocumentRelationshipType


class CimDocumentRelationship(CimRelationship):
    """A concrete class within the cim v1 type system.

    Contains the set of relationships supported by a Document.
    """

    def __init__(self):
        """Constructor"""
        super(CimDocumentRelationship, self).__init__()
        self.target = None                           # type = shared.CimDocumentRelationshipTarget
        self.type = ''                               # type = shared.CimDocumentRelationshipType


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
        d = dict(super(CimDocumentRelationship, self).as_dict())
        append(d, 'target', self.target, False, False, False)
        append(d, 'type', self.type, False, False, True)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

