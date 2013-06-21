"""
.. module:: cim.v1.types.activity.simulation.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-21 14:34:23.252267.

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
from pyesdoc.ontologies.cim.v1.types.activity.conformance import Conformance
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference
from pyesdoc.ontologies.cim.v1.types.software.deployment import Deployment
from pyesdoc.ontologies.cim.v1.types.software.coupling import Coupling
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference
from pyesdoc.ontologies.cim.v1.types.data.data_object import DataObject
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference
from pyesdoc.ontologies.cim.v1.types.data.data_object import DataObject
from pyesdoc.ontologies.cim.v1.types.shared.closed_date_range import ClosedDateRange
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference




class Simulation(NumericalActivity):
    """An abstract class within the cim v1 type system.

    A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.
    """
    # Abstract Base Class module.
    # N.B. - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(Simulation, self).__init__()
        self.authors = str()                         # type = str
        self.calendar = None                         # type = shared.Calendar
        self.conformances = []                       # type = activity.Conformance
        self.control_simulation = None               # type = activity.Simulation
        self.control_simulation_reference = None     # type = shared.CimReference
        self.deployments = []                        # type = software.Deployment
        self.inputs = []                             # type = software.Coupling
        self.output_references = []                  # type = shared.CimReference
        self.outputs = []                            # type = data.DataObject
        self.restart_references = []                 # type = shared.CimReference
        self.restarts = []                           # type = data.DataObject
        self.simulation_id = str()                   # type = str
        self.spinup_date_range = None                # type = shared.ClosedDateRange
        self.spinup_simulation = None                # type = activity.Simulation
        self.spinup_simulation_reference = None      # type = shared.CimReference


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
        d = dict(super(Simulation, self).as_dict())
        append(d, 'authors', self.authors, False, True, False)
        append(d, 'calendar', self.calendar, False, False, False)
        append(d, 'conformances', self.conformances, True, False, False)
        append(d, 'control_simulation', self.control_simulation, False, False, False)
        append(d, 'control_simulation_reference', self.control_simulation_reference, False, False, False)
        append(d, 'deployments', self.deployments, True, False, False)
        append(d, 'inputs', self.inputs, True, False, False)
        append(d, 'output_references', self.output_references, True, False, False)
        append(d, 'outputs', self.outputs, True, False, False)
        append(d, 'restart_references', self.restart_references, True, False, False)
        append(d, 'restarts', self.restarts, True, False, False)
        append(d, 'simulation_id', self.simulation_id, False, True, False)
        append(d, 'spinup_date_range', self.spinup_date_range, False, False, False)
        append(d, 'spinup_simulation', self.spinup_simulation, False, False, False)
        append(d, 'spinup_simulation_reference', self.spinup_simulation_reference, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

