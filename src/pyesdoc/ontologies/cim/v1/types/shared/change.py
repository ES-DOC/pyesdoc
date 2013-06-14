"""
.. module:: cim.v1.types.shared.change.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:08.066984.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.responsible_party import ResponsibleParty
from pyesdoc.ontologies.cim.v1.types.shared.change_property import ChangeProperty
from pyesdoc.ontologies.cim.v1.types.shared.change_property_type import ChangePropertyType


class Change(object):
    """A concrete class within the cim v1 type system.

    A description of [a set of] changes applied at a particular time, by a particular party, to a particular unit of metadata.
    """

    def __init__(self):
        """Constructor"""
        super(Change, self).__init__()
        self.author = None                           # type = shared.ResponsibleParty
        self.date = datetime.datetime.now()          # type = datetime.datetime
        self.description = str()                     # type = str
        self.details = []                            # type = shared.ChangeProperty
        self.name = str()                            # type = str
        self.type = ''                               # type = shared.ChangePropertyType


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
        append(d, 'author', self.author, False, False, False)
        append(d, 'date', self.date, False, True, False)
        append(d, 'description', self.description, False, True, False)
        append(d, 'details', self.details, True, False, False)
        append(d, 'name', self.name, False, True, False)
        append(d, 'type', self.type, False, False, True)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

