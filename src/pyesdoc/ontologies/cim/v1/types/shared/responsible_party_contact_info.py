"""
.. module:: cim.v1.types.shared.responsible_party_contact_info.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.205262.

"""

# Module imports.
import datetime
import types
import uuid



class ResponsiblePartyContactInfo(object):
    """A concrete class within the cim v1 type system.

    Maps gmd:contactInfo element.
    """

    def __init__(self):
        """Constructor"""
        super(ResponsiblePartyContactInfo, self).__init__()
        self.address = str()                         # type = str
        self.email = str()                           # type = str
        self.url = str()                             # type = str


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
        append(d, 'address', self.address, False, True, False)
        append(d, 'email', self.email, False, True, False)
        append(d, 'url', self.url, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

