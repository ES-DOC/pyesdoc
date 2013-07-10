"""
.. module:: cim.v1.types.activity.ensemble.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.217223.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.activity.numerical_activity import NumericalActivity
from pyesdoc.ontologies.cim.v1.types.shared.cim_info import CimInfo
from pyesdoc.ontologies.cim.v1.types.shared.data_source import DataSource
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference
from pyesdoc.ontologies.cim.v1.types.activity.ensemble_type import EnsembleType


class Ensemble(NumericalActivity):
    """A concrete class within the cim v1 type system.

    An ensemble is made up of two or more simulations which are to be compared against each other to create ensemble statistics. Ensemble members can differ in terms of initial conditions, physical parameterisation and the model used. An ensemble bundles together sets of ensembleMembers, all of which reference the same Simulation(Run) and include one or more changes.
    """

    def __init__(self):
        """Constructor"""
        super(Ensemble, self).__init__()
        self.cim_info = None                         # type = shared.CimInfo
        self.members = []                            # type = activity.EnsembleMember
        self.outputs = []                            # type = shared.DataSource
        self.outputs_references = []                 # type = shared.CimReference
        self.types = []                              # type = activity.EnsembleType


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
        d = dict(super(Ensemble, self).as_dict())
        append(d, 'cim_info', self.cim_info, False, False, False)
        append(d, 'members', self.members, True, False, False)
        append(d, 'outputs', self.outputs, True, False, False)
        append(d, 'outputs_references', self.outputs_references, True, False, False)
        append(d, 'types', self.types, True, False, True)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm
from pyesdoc.ontologies.cim.v1.types.activity.ensemble_member import EnsembleMember

