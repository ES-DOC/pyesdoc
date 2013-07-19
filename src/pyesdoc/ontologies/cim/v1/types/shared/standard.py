"""
.. module:: cim.v1.types.shared.standard.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.205610.

"""

# Module imports.
import datetime
import types
import uuid



class Standard(object):
    """A concrete class within the cim v1 type system.

    Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.
    """

    def __init__(self):
        """Constructor"""
        super(Standard, self).__init__()
        self.description = str()                     # type = str
        self.name = str()                            # type = str
        self.version = str()                         # type = str


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
        append(d, 'description', self.description, False, True, False)
        append(d, 'name', self.name, False, True, False)
        append(d, 'version', self.version, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

