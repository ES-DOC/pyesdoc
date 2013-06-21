"""
.. module:: cim.v1.types.shared.responsible_party.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-21 14:34:23.284891.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.responsible_party_contact_info import ResponsiblePartyContactInfo


class ResponsibleParty(object):
    """A concrete class within the cim v1 type system.

    A person/organsiation responsible for some aspect of a climate science artefact
    """

    def __init__(self):
        """Constructor"""
        super(ResponsibleParty, self).__init__()
        self.abbreviation = str()                    # type = str
        self.contact_info = None                     # type = shared.ResponsiblePartyContactInfo
        self.individual_name = str()                 # type = str
        self.organisation_name = str()               # type = str
        self.role = str()                            # type = str


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
        append(d, 'abbreviation', self.abbreviation, False, True, False)
        append(d, 'contact_info', self.contact_info, False, False, False)
        append(d, 'individual_name', self.individual_name, False, True, False)
        append(d, 'organisation_name', self.organisation_name, False, True, False)
        append(d, 'role', self.role, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

