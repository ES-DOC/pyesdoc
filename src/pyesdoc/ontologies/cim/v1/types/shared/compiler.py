"""
.. module:: cim.v1.types.shared.compiler.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-21 14:34:23.276464.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.compiler_type import CompilerType


class Compiler(object):
    """A concrete class within the cim v1 type system.

    A description of a compiler used on a particular platform.
    """

    def __init__(self):
        """Constructor"""
        super(Compiler, self).__init__()
        self.environment_variables = str()           # type = str
        self.language = str()                        # type = str
        self.name = str()                            # type = str
        self.options = str()                         # type = str
        self.type = ''                               # type = shared.CompilerType
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
        append(d, 'environment_variables', self.environment_variables, False, True, False)
        append(d, 'language', self.language, False, True, False)
        append(d, 'name', self.name, False, True, False)
        append(d, 'options', self.options, False, True, False)
        append(d, 'type', self.type, False, False, True)
        append(d, 'version', self.version, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

