"""
.. module:: cim.v1.types.activity.simulation_run.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-21 14:34:23.254243.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.activity.simulation import Simulation
from pyesdoc.ontologies.cim.v1.types.shared.cim_info import CimInfo
from pyesdoc.ontologies.cim.v1.types.shared.date_range import DateRange
from pyesdoc.ontologies.cim.v1.types.software.model_component import ModelComponent
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference


class SimulationRun(Simulation):
    """A concrete class within the cim v1 type system.

    A SimulationRun is, as the name implies, one single model run. A SimulationRun is a Simulation. There is a one to one association between SimulationRun and (a top-level) SoftwarePackage::ModelComponent.
    """

    def __init__(self):
        """Constructor"""
        super(SimulationRun, self).__init__()
        self.cim_info = None                         # type = shared.CimInfo
        self.date_range = None                       # type = shared.DateRange
        self.model = None                            # type = software.ModelComponent
        self.model_reference = None                  # type = shared.CimReference


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
        d = dict(super(SimulationRun, self).as_dict())
        append(d, 'cim_info', self.cim_info, False, False, False)
        append(d, 'date_range', self.date_range, False, False, False)
        append(d, 'model', self.model, False, False, False)
        append(d, 'model_reference', self.model_reference, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

