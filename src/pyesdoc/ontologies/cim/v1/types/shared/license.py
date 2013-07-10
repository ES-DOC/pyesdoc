"""
.. module:: cim.v1.types.shared.license.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.254469.

"""

# Module imports.
import datetime
import types
import uuid



class License(object):
    """A concrete class within the cim v1 type system.

    A description of a license restricting access to a unit of data or software
    """

    def __init__(self):
        """Constructor"""
        super(License, self).__init__()
        self.contact = str()                         # type = str
        self.description = str()                     # type = str
        self.is_unrestricted = str()                 # type = str
        self.name = str()                            # type = str


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
        append(d, 'contact', self.contact, False, True, False)
        append(d, 'description', self.description, False, True, False)
        append(d, 'is_unrestricted', self.is_unrestricted, False, True, False)
        append(d, 'name', self.name, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

