"""
.. module:: cim.v1.typeset_for_software_package.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.software package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-09-06 15:59:51.502320.

"""
# Module imports.
import abc
import datetime
import uuid

import typeset_for_shared_package as shared




class Component(shared.DataSource):
    """A concrete class within the cim v1 type system.

    A SofwareComponent is an abstract component from which all other components derive. It represents an element that takes input data and generates output data. A SoftwareCompnent can include nested "child" components. Every component can have "componentProperties" which describe the scientific properties that a component simulates (for example, temperature, pressure, etc.) and the numerical properties that influence how a component performs its simulation (for example, the force of gravity). A SoftwareComponent can also have a Deployment, which describes how software is deployed onto computing resources. And a SoftwareComponent can have a composition, which describes how ComponentProperties are coupled together either to/from other SoftwareComponents or external data files. The properties specified by a component's composition must be owned by that component or a child of that component; child components cannot couple together their parents' properties.
    """
    def __init__(self):
        """Constructor.

        """
        super(Component, self).__init__()

        self.children = []                           # type = software.Component
        self.citation_list = []                      # type = shared.Citation
        self.citations = []                          # type = shared.Citation
        self.composition = None                      # type = software.Composition
        self.coupling_framework = ''                 # type = software.CouplingFrameworkType
        self.dependencies = []                       # type = software.EntryPoint
        self.deployments = []                        # type = software.Deployment
        self.description = str()                     # type = str
        self.funding_sources = []                    # type = str
        self.grid = None                             # type = grids.GridSpec
        self.is_embedded = bool()                    # type = bool
        self.language = None                         # type = software.ComponentLanguage
        self.license = None                          # type = shared.License
        self.long_name = str()                       # type = str
        self.online_resource = str()                 # type = str
        self.parent = None                           # type = software.Component
        self.previous_version = str()                # type = str
        self.properties = []                         # type = software.ComponentProperty
        self.property_tree = []                      # type = software.ComponentProperty
        self.release_date = datetime.datetime.now()  # type = datetime.datetime
        self.responsible_parties = []                # type = shared.ResponsibleParty
        self.responsible_party_list = []             # type = shared.ResponsibleParty
        self.short_name = str()                      # type = str


class ComponentLanguage(object):
    """A concrete class within the cim v1 type system.

    Details of the programming language a component is written in. There is an assumption that all EntryPoints use the same ComponentLanguage.
    """
    def __init__(self):
        """Constructor.

        """
        super(ComponentLanguage, self).__init__()

        self.name = str()                            # type = str
        self.properties = []                         # type = software.ComponentLanguageProperty


class ComponentLanguageProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    This provides a place to include language-specific information. Every property is basically a name/value pair, where the names are things like: moduleName, reservedUnits, reservedNames (these are all examples of Fortran-specific properties).
    """
    def __init__(self):
        """Constructor.

        """
        super(ComponentLanguageProperty, self).__init__()



class ComponentProperty(shared.DataSource):
    """A concrete class within the cim v1 type system.

    ComponentProperties include things that a component simulates (ie: pressure, humidity) and things that prescribe that simulation (ie: gravity, choice of advection scheme). Note that this is a specialisation of shared::DataSource. data::DataObject is also a specialisation of shared::DataSource. This allows software::Connections and/or activity::Conformance to refer to either ComponentProperties or DataObjects.
    """
    def __init__(self):
        """Constructor.

        """
        super(ComponentProperty, self).__init__()

        self.children = []                           # type = software.ComponentProperty
        self.citations = []                          # type = shared.Citation
        self.description = str()                     # type = str
        self.grid = str()                            # type = str
        self.intent = ''                             # type = software.ComponentPropertyIntentType
        self.is_represented = bool()                 # type = bool
        self.long_name = str()                       # type = str
        self.short_name = str()                      # type = str
        self.standard_names = []                     # type = str
        self.units = ''                              # type = shared.UnitType
        self.values = []                             # type = str


class Composition(object):
    """A concrete class within the cim v1 type system.

    The set of Couplings used by a Component. Couplings can only occur between child components. That is, a composition must belong to an ancestor component of the components whose fields are being connected.
    """
    def __init__(self):
        """Constructor.

        """
        super(Composition, self).__init__()

        self.couplings = []                          # type = str
        self.description = str()                     # type = str


class Connection(object):
    """A concrete class within the cim v1 type system.

    A Connection represents a link from a source DataSource to a target DataSource.  These can either be ComponentProperties (ie: the values come from an internal component) or DataObjects (ie: the values come from an external file).   It can be associated with another software component (a transformer).  If present, the rate, lag, timeTransformation, and spatialRegridding override that of the parent coupling.  Note that there is the potential for multiple connectionSource & connectionTarget and multiple couplingSources & couplingTargets.  This may lead users to wonder how to match up a connection source (a ComponentProperty) with its coupling source (a SoftwareComponent). Clever logic is not required though; because the sources and targets are listed by reference, they can be found in a CIM document and the parent can be navigated to from there - there is no need to consult the source or target of the coupling.
    """
    def __init__(self):
        """Constructor.

        """
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


class ConnectionEndpoint(object):
    """A concrete class within the cim v1 type system.

    The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).
    """
    def __init__(self):
        """Constructor.

        """
        super(ConnectionEndpoint, self).__init__()

        self.data_source = None                      # type = shared.DataSource
        self.data_source_reference = None            # type = shared.CimReference
        self.instance_id = str()                     # type = str
        self.properties = []                         # type = software.ConnectionProperty


class ConnectionProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    A ConnectionProperty is a name/value pair used to specify OASIS-specific properties.
    """
    def __init__(self):
        """Constructor.

        """
        super(ConnectionProperty, self).__init__()



class Coupling(object):
    """A concrete class within the cim v1 type system.

    A coupling represents a set of Connections between a source and target component. Couplings can be complete or incomplete. If they are complete then they must include all Connections between model properties. If they are incomplete then the connections can be underspecified or not listed at all.
    """
    def __init__(self):
        """Constructor.

        """
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


class CouplingEndpoint(object):
    """A concrete class within the cim v1 type system.

    The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).
    """
    def __init__(self):
        """Constructor.

        """
        super(CouplingEndpoint, self).__init__()

        self.data_source = None                      # type = shared.DataSource
        self.data_source_reference = None            # type = shared.CimReference
        self.instance_id = str()                     # type = str
        self.properties = []                         # type = software.CouplingProperty


class CouplingProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    A CouplingProperty is a name/value pair used to specify OASIS-specific properties.
    """
    def __init__(self):
        """Constructor.

        """
        super(CouplingProperty, self).__init__()



class Deployment(object):
    """A concrete class within the cim v1 type system.

    Gives information about the technical properties of a component: what machine it was run on, which compilers were used, how it was parallised, etc. A deployment basically associates a deploymentDate with a Platform. A deployment only exists if something has been deployed. A platform, in contrast, can exist independently, waiting to be used in deployments.
    """
    def __init__(self):
        """Constructor.

        """
        super(Deployment, self).__init__()

        self.deployment_date = datetime.datetime.now()# type = datetime.datetime
        self.description = str()                     # type = str
        self.executable_arguments = []               # type = str
        self.executable_name = str()                 # type = str
        self.parallelisation = None                  # type = software.Parallelisation
        self.platform = None                         # type = shared.Platform
        self.platform_reference = None               # type = shared.CimReference


class EntryPoint(object):
    """A concrete class within the cim v1 type system.

    Describes a function or subroutine of a SoftwareComponent. BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model. Currently, a very basic schedule can be approximated by using the "proceeds" and "follows" attributes, however a more complete system is required for full BFG compatibility. Every EntryPoint can have a set of arguments associated with it. These reference (previously defined) ComponentProperties.
    """
    def __init__(self):
        """Constructor.

        """
        super(EntryPoint, self).__init__()

        self.name = str()                            # type = str


class Parallelisation(object):
    """A concrete class within the cim v1 type system.

    Describes how a deployment has been parallelised across a computing platform.
    """
    def __init__(self):
        """Constructor.

        """
        super(Parallelisation, self).__init__()

        self.processes = int()                       # type = int
        self.ranks = []                              # type = software.Rank


class Rank(object):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(Rank, self).__init__()

        self.increment = int()                       # type = int
        self.max = int()                             # type = int
        self.min = int()                             # type = int
        self.value = int()                           # type = int


class SpatialRegridding(object):
    """A concrete class within the cim v1 type system.

    Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.
    """
    def __init__(self):
        """Constructor.

        """
        super(SpatialRegridding, self).__init__()

        self.dimension = ''                          # type = software.SpatialRegriddingDimensionType
        self.properties = []                         # type = software.SpatialRegriddingProperty
        self.standard_method = ''                    # type = software.SpatialRegriddingStandardMethodType
        self.user_method = None                      # type = software.SpatialRegriddingUserMethod


class SpatialRegriddingProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    Used for OASIS-specific regridding information (ie: masked, order, normalisation, etc.)
    """
    def __init__(self):
        """Constructor.

        """
        super(SpatialRegriddingProperty, self).__init__()



class SpatialRegriddingUserMethod(object):
    """A concrete class within the cim v1 type system.

    Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.
    """
    def __init__(self):
        """Constructor.

        """
        super(SpatialRegriddingUserMethod, self).__init__()

        self.file = None                             # type = data.DataObject
        self.file_reference = None                   # type = shared.CimReference
        self.name = str()                            # type = str


class TimeLag(object):
    """A concrete class within the cim v1 type system.

    The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.
    """
    def __init__(self):
        """Constructor.

        """
        super(TimeLag, self).__init__()

        self.units = ''                              # type = software.TimingUnits
        self.value = int()                           # type = int


class TimeTransformation(object):
    """A concrete class within the cim v1 type system.

    The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.
    """
    def __init__(self):
        """Constructor.

        """
        super(TimeTransformation, self).__init__()

        self.description = str()                     # type = str
        self.mapping_type = ''                       # type = software.TimeMappingType


class Timing(object):
    """A concrete class within the cim v1 type system.

    Provides information about the rate of couplings and connections and/or the timing characteristics of individual components - for example, the start and stop times that the component was run for or the units of time that a component is able to model (in a single timestep).
    """
    def __init__(self):
        """Constructor.

        """
        super(Timing, self).__init__()

        self.end = datetime.datetime.now()           # type = datetime.datetime
        self.is_variable_rate = bool()               # type = bool
        self.rate = int()                            # type = int
        self.start = datetime.datetime.now()         # type = datetime.datetime
        self.units = ''                              # type = software.TimingUnits


class ModelComponent(Component):
    """A concrete class within the cim v1 type system.

    A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.
    """
    def __init__(self):
        """Constructor.

        """
        super(ModelComponent, self).__init__()

        self.activity = None                         # type = activity.Activity
        self.cim_info = None                         # type = shared.CimInfo
        self.timing = None                           # type = software.Timing
        self.type = ''                               # type = software.ModelComponentType
        self.types = []                              # type = software.ModelComponentType


class ProcessorComponent(Component):
    """A concrete class within the cim v1 type system.

    A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.
    """
    def __init__(self):
        """Constructor.

        """
        super(ProcessorComponent, self).__init__()

        self.cim_info = None                         # type = shared.CimInfo


class StatisticalModelComponent(Component):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(StatisticalModelComponent, self).__init__()

        self.cim_info = None                         # type = shared.CimInfo
        self.timing = None                           # type = software.Timing
        self.type = ''                               # type = software.StatisticalModelComponentType
        self.types = []                              # type = software.StatisticalModelComponentType


class ComponentPropertyIntentType(object):
    """An enumeration within the cim v1 type system.

    The direction that the associated component property is intended to be coupled: in, out, or inout..
    """

    pass


class ConnectionType(object):
    """An enumeration within the cim v1 type system.

    The ConnectionType enumeration describes the mechanism of transport for a connection.
    """

    pass


class CouplingFrameworkType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class ModelComponentType(object):
    """An enumeration within the cim v1 type system.

    An enumeration of types of ModelComponent. This includes things like atmosphere & ocean models, radiation schemes, etc. CIM best-practice is to describe every component for which there is a named ComponentType as a separate component, even if it is not a separate unit of software (ie: even if it is embedded), instead of as a (set of) ModelParameters. This codelist is synonomous with "realm" for the purposes of CMIP5.
    """

    pass


class SpatialRegriddingDimensionType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class SpatialRegriddingStandardMethodType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class StatisticalModelComponentType(object):
    """An enumeration within the cim v1 type system.

    An enumeration of types of ProcessorComponent.  This includes things like transformers and post-processors.
    """

    pass


class TimeMappingType(object):
    """An enumeration within the cim v1 type system.

    Enumerates the different ways that time can be mapped when transforming from one field to another.
    """

    pass


class TimingUnits(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


