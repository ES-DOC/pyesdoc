"""
.. module:: cim.v1.types.activity.ensemble_member.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:08.027174.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.activity.numerical_activity import NumericalActivity
from pyesdoc.ontologies.cim.v1.types.shared.standard_name import StandardName
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference
from pyesdoc.ontologies.cim.v1.types.activity.simulation import Simulation
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference


class EnsembleMember(NumericalActivity):
    """A concrete class within the cim v1 type system.

    A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a "simulation composite".  The "parent" simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.
    """

    def __init__(self):
        """Constructor"""
        super(EnsembleMember, self).__init__()
        self.ensemble = None                         # type = activity.Ensemble
        self.ensemble_ids = []                       # type = shared.StandardName
        self.ensemble_reference = None               # type = shared.CimReference
        self.simulation = None                       # type = activity.Simulation
        self.simulation_reference = None             # type = shared.CimReference


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
        d = dict(super(EnsembleMember, self).as_dict())
        append(d, 'ensemble', self.ensemble, False, False, False)
        append(d, 'ensemble_ids', self.ensemble_ids, True, False, False)
        append(d, 'ensemble_reference', self.ensemble_reference, False, False, False)
        append(d, 'simulation', self.simulation, False, False, False)
        append(d, 'simulation_reference', self.simulation_reference, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm
from pyesdoc.ontologies.cim.v1.types.activity.ensemble import Ensemble

