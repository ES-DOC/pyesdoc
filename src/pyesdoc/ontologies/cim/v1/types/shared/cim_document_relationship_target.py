"""
.. module:: cim.v1.types.shared.cim_document_relationship_target.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.248555.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.cim_document_type import CimDocumentType
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference


class CimDocumentRelationshipTarget(object):
    """A concrete class within the cim v1 type system.

    
    """

    def __init__(self):
        """Constructor"""
        super(CimDocumentRelationshipTarget, self).__init__()
        self.document = ''                           # type = shared.CimDocumentType
        self.reference = None                        # type = shared.CimReference


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
        append(d, 'document', self.document, False, False, True)
        append(d, 'reference', self.reference, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

