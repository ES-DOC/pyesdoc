"""
.. module:: cim.v1.types.activity.downscaling_simulation.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.168284.

"""

# Module imports.
import abc
from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.activity.numerical_activity import NumericalActivity
from pyesdoc.ontologies.cim.v1.types.shared.calendar import Calendar
from pyesdoc.ontologies.cim.v1.types.shared.cim_info import CimInfo
from pyesdoc.ontologies.cim.v1.types.shared.data_source import DataSource
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference
from pyesdoc.ontologies.cim.v1.types.activity.downscaling_type import DownscalingType
from pyesdoc.ontologies.cim.v1.types.software.coupling import Coupling
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference
from pyesdoc.ontologies.cim.v1.types.data.data_object import DataObject




class DownscalingSimulation(NumericalActivity):
    """An abstract class within the cim v1 type system.

    A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.
    """
    # Abstract Base Class module.
    # N.B. - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(DownscalingSimulation, self).__init__()
        self.calendar = None                         # type = shared.Calendar
        self.cim_info = None                         # type = shared.CimInfo
        self.downscaled_from = None                  # type = shared.DataSource
        self.downscaled_from_reference = None        # type = shared.CimReference
        self.downscaling_id = str()                  # type = str
        self.downscaling_type = ''                   # type = activity.DownscalingType
        self.inputs = []                             # type = software.Coupling
        self.output_references = []                  # type = shared.CimReference
        self.outputs = []                            # type = data.DataObject


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
        d = dict(super(DownscalingSimulation, self).as_dict())
        append(d, 'calendar', self.calendar, False, False, False)
        append(d, 'cim_info', self.cim_info, False, False, False)
        append(d, 'downscaled_from', self.downscaled_from, False, False, False)
        append(d, 'downscaled_from_reference', self.downscaled_from_reference, False, False, False)
        append(d, 'downscaling_id', self.downscaling_id, False, True, False)
        append(d, 'downscaling_type', self.downscaling_type, False, False, True)
        append(d, 'inputs', self.inputs, True, False, False)
        append(d, 'output_references', self.output_references, True, False, False)
        append(d, 'outputs', self.outputs, True, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

