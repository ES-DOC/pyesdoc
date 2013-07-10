"""
.. module:: cim.v1.types.shared.platform.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.257207.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.cim_info import CimInfo
from pyesdoc.ontologies.cim.v1.types.shared.responsible_party import ResponsibleParty
from pyesdoc.ontologies.cim.v1.types.shared.machine_compiler_unit import MachineCompilerUnit


class Platform(object):
    """A concrete class within the cim v1 type system.

    A platform is a description of resources used to deploy a component/simulation.  A platform pairs a machine with a (set of) compilers.  There is also a point of contact for the platform.
    """

    def __init__(self):
        """Constructor"""
        super(Platform, self).__init__()
        self.cim_info = None                         # type = shared.CimInfo
        self.contacts = []                           # type = shared.ResponsibleParty
        self.description = str()                     # type = str
        self.long_name = str()                       # type = str
        self.short_name = str()                      # type = str
        self.units = []                              # type = shared.MachineCompilerUnit


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
        append(d, 'cim_info', self.cim_info, False, False, False)
        append(d, 'contacts', self.contacts, True, False, False)
        append(d, 'description', self.description, False, True, False)
        append(d, 'long_name', self.long_name, False, True, False)
        append(d, 'short_name', self.short_name, False, True, False)
        append(d, 'units', self.units, True, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

