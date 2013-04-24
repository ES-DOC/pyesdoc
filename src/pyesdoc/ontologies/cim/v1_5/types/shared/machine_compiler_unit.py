"""
.. module:: cim.v1_5.types.shared.machine_compiler_unit.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1.5 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-04-17 17:20:28.700310.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1_5.types.shared.compiler import Compiler
from pyesdoc.ontologies.cim.v1_5.types.shared.machine import Machine


class MachineCompilerUnit(object):
    """A concrete class within the cim v1.5 type system.

    Associates a machine with a [set of] compilers.  This is a separate class in case a platform needs to specify more than one machine/compiler pair.
    """

    def __init__(self):
        """Constructor"""
        super(MachineCompilerUnit, self).__init__()
        self.compilers = []                          # type = shared.Compiler
        self.machine = None                          # type = shared.Machine


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
        append(d, 'compilers', self.compilers, True, False, False)
        append(d, 'machine', self.machine, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

