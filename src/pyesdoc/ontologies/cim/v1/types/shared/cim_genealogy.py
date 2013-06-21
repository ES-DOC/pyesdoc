"""
.. module:: cim.v1.types.shared.cim_genealogy.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-21 14:34:23.273093.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.cim_relationship import CimRelationship


class CimGenealogy(object):
    """A concrete class within the cim v1 type system.

    A record of a document's history. A genealogy element contains a textual description and a set of relationships. Each relationship has a type and a reference to some target. There are different relationships for different document types.
    """

    def __init__(self):
        """Constructor"""
        super(CimGenealogy, self).__init__()
        self.relationships = []                      # type = shared.CimRelationship


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
        append(d, 'relationships', self.relationships, True, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

