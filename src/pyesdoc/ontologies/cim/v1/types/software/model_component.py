"""
.. module:: cim.v1.types.software.model_component.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.269216.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.software.component import Component
from pyesdoc.ontologies.cim.v1.types.activity.activity import Activity
from pyesdoc.ontologies.cim.v1.types.shared.cim_info import CimInfo
from pyesdoc.ontologies.cim.v1.types.software.timing import Timing
from pyesdoc.ontologies.cim.v1.types.software.model_component_type import ModelComponentType


class ModelComponent(Component):
    """A concrete class within the cim v1 type system.

    A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.
    """

    def __init__(self):
        """Constructor"""
        super(ModelComponent, self).__init__()
        self.activity = None                         # type = activity.Activity
        self.cim_info = None                         # type = shared.CimInfo
        self.timing = None                           # type = software.Timing
        self.type = ''                               # type = software.ModelComponentType
        self.types = []                              # type = software.ModelComponentType


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
        d = dict(super(ModelComponent, self).as_dict())
        append(d, 'activity', self.activity, False, False, False)
        append(d, 'cim_info', self.cim_info, False, False, False)
        append(d, 'timing', self.timing, False, False, False)
        append(d, 'type', self.type, False, False, True)
        append(d, 'types', self.types, True, False, True)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

