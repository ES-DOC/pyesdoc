"""
.. module:: cim.v1.types.software.coupling.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.266244.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.software.connection import Connection
from pyesdoc.ontologies.cim.v1.types.shared.data_source import DataSource
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference
from pyesdoc.ontologies.cim.v1.types.software.coupling_property import CouplingProperty
from pyesdoc.ontologies.cim.v1.types.shared.data_purpose import DataPurpose
from pyesdoc.ontologies.cim.v1.types.software.coupling_endpoint import CouplingEndpoint
from pyesdoc.ontologies.cim.v1.types.software.spatial_regridding import SpatialRegridding
from pyesdoc.ontologies.cim.v1.types.software.time_lag import TimeLag
from pyesdoc.ontologies.cim.v1.types.software.timing import Timing
from pyesdoc.ontologies.cim.v1.types.software.time_transformation import TimeTransformation
from pyesdoc.ontologies.cim.v1.types.software.processor_component import ProcessorComponent
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference
from pyesdoc.ontologies.cim.v1.types.software.connection_type import ConnectionType


class Coupling(object):
    """A concrete class within the cim v1 type system.

    A coupling represents a set of Connections between a source and target component. Couplings can be complete or incomplete. If they are complete then they must include all Connections between model properties. If they are incomplete then the connections can be underspecified or not listed at all.
    """

    def __init__(self):
        """Constructor"""
        super(Coupling, self).__init__()
        self.connections = []                        # type = software.Connection
        self.description = str()                     # type = str
        self.is_fully_specified = bool()             # type = bool
        self.priming = None                          # type = shared.DataSource
        self.priming_reference = None                # type = shared.CimReference
        self.properties = []                         # type = software.CouplingProperty
        self.purpose = ''                            # type = shared.DataPurpose
        self.sources = []                            # type = software.CouplingEndpoint
        self.spatial_regriddings = []                # type = software.SpatialRegridding
        self.target = None                           # type = software.CouplingEndpoint
        self.time_lag = None                         # type = software.TimeLag
        self.time_profile = None                     # type = software.Timing
        self.time_transformation = None              # type = software.TimeTransformation
        self.transformers = []                       # type = software.ProcessorComponent
        self.transformers_references = []            # type = shared.CimReference
        self.type = ''                               # type = software.ConnectionType


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
        append(d, 'connections', self.connections, True, False, False)
        append(d, 'description', self.description, False, True, False)
        append(d, 'is_fully_specified', self.is_fully_specified, False, True, False)
        append(d, 'priming', self.priming, False, False, False)
        append(d, 'priming_reference', self.priming_reference, False, False, False)
        append(d, 'properties', self.properties, True, False, False)
        append(d, 'purpose', self.purpose, False, False, True)
        append(d, 'sources', self.sources, True, False, False)
        append(d, 'spatial_regriddings', self.spatial_regriddings, True, False, False)
        append(d, 'target', self.target, False, False, False)
        append(d, 'time_lag', self.time_lag, False, False, False)
        append(d, 'time_profile', self.time_profile, False, False, False)
        append(d, 'time_transformation', self.time_transformation, False, False, False)
        append(d, 'transformers', self.transformers, True, False, False)
        append(d, 'transformers_references', self.transformers_references, True, False, False)
        append(d, 'type', self.type, False, False, True)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

