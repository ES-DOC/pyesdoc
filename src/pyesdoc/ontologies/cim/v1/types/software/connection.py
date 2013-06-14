"""
.. module:: cim.v1.types.software.connection.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:08.090621.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.data_source import DataSource
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference
from pyesdoc.ontologies.cim.v1.types.software.connection_property import ConnectionProperty
from pyesdoc.ontologies.cim.v1.types.software.connection_endpoint import ConnectionEndpoint
from pyesdoc.ontologies.cim.v1.types.software.spatial_regridding import SpatialRegridding
from pyesdoc.ontologies.cim.v1.types.software.timing import Timing
from pyesdoc.ontologies.cim.v1.types.software.time_transformation import TimeTransformation
from pyesdoc.ontologies.cim.v1.types.software.processor_component import ProcessorComponent
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference
from pyesdoc.ontologies.cim.v1.types.software.connection_type import ConnectionType


class Connection(object):
    """A concrete class within the cim v1 type system.

    A Connection represents a link from a source DataSource to a target DataSource.  These can either be ComponentProperties (ie: the values come from an internal component) or DataObjects (ie: the values come from an external file).   It can be associated with another software component (a transformer).  If present, the rate, lag, timeTransformation, and spatialRegridding override that of the parent coupling.  Note that there is the potential for multiple connectionSource & connectionTarget and multiple couplingSources & couplingTargets.  This may lead users to wonder how to match up a connection source (a ComponentProperty) with its coupling source (a SoftwareComponent). Clever logic is not required though; because the sources and targets are listed by reference, they can be found in a CIM document and the parent can be navigated to from there - there is no need to consult the source or target of the coupling.
    """

    def __init__(self):
        """Constructor"""
        super(Connection, self).__init__()
        self.description = str()                     # type = str
        self.priming = None                          # type = shared.DataSource
        self.priming_reference = None                # type = shared.CimReference
        self.properties = []                         # type = software.ConnectionProperty
        self.sources = []                            # type = software.ConnectionEndpoint
        self.spatial_regridding = []                 # type = software.SpatialRegridding
        self.target = None                           # type = software.ConnectionEndpoint
        self.time_lag = str()                        # type = str
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
        append(d, 'description', self.description, False, True, False)
        append(d, 'priming', self.priming, False, False, False)
        append(d, 'priming_reference', self.priming_reference, False, False, False)
        append(d, 'properties', self.properties, True, False, False)
        append(d, 'sources', self.sources, True, False, False)
        append(d, 'spatial_regridding', self.spatial_regridding, True, False, False)
        append(d, 'target', self.target, False, False, False)
        append(d, 'time_lag', self.time_lag, False, True, False)
        append(d, 'time_profile', self.time_profile, False, False, False)
        append(d, 'time_transformation', self.time_transformation, False, False, False)
        append(d, 'transformers', self.transformers, True, False, False)
        append(d, 'transformers_references', self.transformers_references, True, False, False)
        append(d, 'type', self.type, False, False, True)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

