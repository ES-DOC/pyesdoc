"""
.. module:: cim.v1.types.activity.simulation_composite.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:08.039598.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.activity.simulation import Simulation
from pyesdoc.ontologies.cim.v1.types.shared.cim_info import CimInfo
from pyesdoc.ontologies.cim.v1.types.shared.date_range import DateRange


class SimulationComposite(Simulation):
    """A concrete class within the cim v1 type system.

    A SimulationComposite is an aggregation of Simulations. With the aggreation connector between Simulation and SimulationComposite(SC) the SC can be made up of both SimulationRuns and SCs. The SimulationComposite is the new name for the concept of SimulationCollection: A simulation can be made up of "child" simulations aggregated together to form a "simulation composite".  The "parent" simulation can be made up of whole or partial child simulations and the SimulationComposite attributes need to be able to capture this.
    """

    def __init__(self):
        """Constructor"""
        super(SimulationComposite, self).__init__()
        self.child = []                              # type = activity.Simulation
        self.cim_info = None                         # type = shared.CimInfo
        self.date_range = None                       # type = shared.DateRange
        self.rank = int()                            # type = int


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
        d = dict(super(SimulationComposite, self).as_dict())
        append(d, 'child', self.child, True, False, False)
        append(d, 'cim_info', self.cim_info, False, False, False)
        append(d, 'date_range', self.date_range, False, False, False)
        append(d, 'rank', self.rank, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

