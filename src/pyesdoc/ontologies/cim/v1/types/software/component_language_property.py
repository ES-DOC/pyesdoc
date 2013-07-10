"""
.. module:: cim.v1.types.software.component_language_property.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.261963.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.property import Property


class ComponentLanguageProperty(Property):
    """A concrete class within the cim v1 type system.

    This provides a place to include language-specific information. Every property is basically a name/value pair, where the names are things like: moduleName, reservedUnits, reservedNames (these are all examples of Fortran-specific properties).
    """

    def __init__(self):
        """Constructor"""
        super(ComponentLanguageProperty, self).__init__()

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
        d = dict(super(ComponentLanguageProperty, self).as_dict())
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

