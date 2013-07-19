"""
.. module:: cim.v1.types.software.component_language.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.207661.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.software.component_language_property import ComponentLanguageProperty


class ComponentLanguage(object):
    """A concrete class within the cim v1 type system.

    Details of the programming language a component is written in. There is an assumption that all EntryPoints use the same ComponentLanguage.
    """

    def __init__(self):
        """Constructor"""
        super(ComponentLanguage, self).__init__()
        self.name = str()                            # type = str
        self.properties = []                         # type = software.ComponentLanguageProperty


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
        append(d, 'name', self.name, False, True, False)
        append(d, 'properties', self.properties, True, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

