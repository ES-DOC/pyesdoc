"""
.. module:: cim.v1.types.shared.citation.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:08.073529.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference


class Citation(object):
    """A concrete class within the cim v1 type system.

    An academic reference to published work.
    """

    def __init__(self):
        """Constructor"""
        super(Citation, self).__init__()
        self.alternative_title = str()               # type = str
        self.collective_title = str()                # type = str
        self.date = datetime.datetime.now()          # type = datetime.datetime
        self.date_type = str()                       # type = str
        self.location = str()                        # type = str
        self.organisation = str()                    # type = str
        self.reference = None                        # type = shared.CimReference
        self.role = str()                            # type = str
        self.title = str()                           # type = str
        self.type = str()                            # type = str


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
        append(d, 'alternative_title', self.alternative_title, False, True, False)
        append(d, 'collective_title', self.collective_title, False, True, False)
        append(d, 'date', self.date, False, True, False)
        append(d, 'date_type', self.date_type, False, True, False)
        append(d, 'location', self.location, False, True, False)
        append(d, 'organisation', self.organisation, False, True, False)
        append(d, 'reference', self.reference, False, False, False)
        append(d, 'role', self.role, False, True, False)
        append(d, 'title', self.title, False, True, False)
        append(d, 'type', self.type, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

