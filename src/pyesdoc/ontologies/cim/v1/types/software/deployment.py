"""
.. module:: cim.v1.types.software.deployment.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:08.095919.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.software.parallelisation import Parallelisation
from pyesdoc.ontologies.cim.v1.types.shared.platform import Platform
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference


class Deployment(object):
    """A concrete class within the cim v1 type system.

    Gives information about the technical properties of a component: what machine it was run on, which compilers were used, how it was parallised, etc. A deployment basically associates a deploymentDate with a Platform. A deployment only exists if something has been deployed. A platform, in contrast, can exist independently, waiting to be used in deployments.
    """

    def __init__(self):
        """Constructor"""
        super(Deployment, self).__init__()
        self.deployment_date = datetime.datetime.now()# type = datetime.datetime
        self.description = str()                     # type = str
        self.executable_arguments = []               # type = str
        self.executable_name = str()                 # type = str
        self.parallelisation = None                  # type = software.Parallelisation
        self.platform = None                         # type = shared.Platform
        self.platform_reference = None               # type = shared.CimReference


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
        append(d, 'deployment_date', self.deployment_date, False, True, False)
        append(d, 'description', self.description, False, True, False)
        append(d, 'executable_arguments', self.executable_arguments, True, True, False)
        append(d, 'executable_name', self.executable_name, False, True, False)
        append(d, 'parallelisation', self.parallelisation, False, False, False)
        append(d, 'platform', self.platform, False, False, False)
        append(d, 'platform_reference', self.platform_reference, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

