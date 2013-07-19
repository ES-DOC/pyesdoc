"""
.. module:: cim.v1.types.data.data_restriction.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.184983.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.license import License


class DataRestriction(object):
    """A concrete class within the cim v1 type system.

    An access or use restriction on some element of the DataObject's actual data.
    """

    def __init__(self):
        """Constructor"""
        super(DataRestriction, self).__init__()
        self.license = None                          # type = shared.License
        self.restriction = str()                     # type = str
        self.scope = str()                           # type = str


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
        append(d, 'license', self.license, False, False, False)
        append(d, 'restriction', self.restriction, False, True, False)
        append(d, 'scope', self.scope, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

