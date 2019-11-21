"""
.. module:: cim.v1.typeset_for_software_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.software package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class Component(shared.DataSource):
    """A concrete class within the cim v1 type system.

    A SofwareComponent is an abstract component from which all other components derive. It represents an element that takes input data and generates output data. A SoftwareCompnent can include nested "child" components. Every component can have "componentProperties" which describe the scientific properties that a component simulates (for example, temperature, pressure, etc.) and the numerical properties that influence how a component performs its simulation (for example, the force of gravity). A SoftwareComponent can also have a Deployment, which describes how software is deployed onto computing resources. And a SoftwareComponent can have a composition, which describes how ComponentProperties are coupled together either to/from other SoftwareComponents or external data files. The properties specified by a component's composition must be owned by that component or a child of that component; child components cannot couple together their parents' properties.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Component, self).__init__()

        self.citations = []                               # shared.Citation (0.N)
        self.code_access = None                           # unicode (0.1)
        self.composition = None                           # software.Composition (0.1)
        self.coupling_framework = None                    # software.CouplingFrameworkType (0.1)
        self.dependencies = []                            # software.EntryPoint (0.N)
        self.deployments = []                             # software.Deployment (0.N)
        self.description = None                           # unicode (0.1)
        self.funding_sources = []                         # unicode (0.N)
        self.grid = None                                  # grids.GridSpec (0.1)
        self.is_embedded = None                           # bool (0.1)
        self.language = None                              # software.ComponentLanguage (0.1)
        self.license = None                               # shared.License (0.1)
        self.long_name = None                             # unicode (0.1)
        self.online_resource = None                       # unicode (0.1)
        self.parent = None                                # software.Component (0.1)
        self.previous_version = None                      # unicode (0.1)
        self.properties = []                              # software.ComponentProperty (0.N)
        self.release_date = None                          # datetime.datetime (0.1)
        self.responsible_parties = []                     # shared.ResponsibleParty (0.N)
        self.short_name = None                            # unicode (1.1)
        self.sub_components = []                          # software.Component (0.N)
        self.version = None                               # unicode (0.1)


class ComponentLanguage(object):
    """A concrete class within the cim v1 type system.

    Details of the programming language a component is written in. There is an assumption that all EntryPoints use the same ComponentLanguage.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ComponentLanguage, self).__init__()

        self.name = None                                  # unicode (1.1)
        self.properties = []                              # software.ComponentLanguageProperty (0.N)


class ComponentLanguageProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    This provides a place to include language-specific information. Every property is basically a name/value pair, where the names are things like: moduleName, reservedUnits, reservedNames (these are all examples of Fortran-specific properties).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ComponentLanguageProperty, self).__init__()



class ComponentProperty(shared.DataSource):
    """A concrete class within the cim v1 type system.

    ComponentProperties include things that a component simulates (ie: pressure, humidity) and things that prescribe that simulation (ie: gravity, choice of advection scheme). Note that this is a specialisation of shared::DataSource. data::DataObject is also a specialisation of shared::DataSource. This allows software::Connections and/or activity::Conformance to refer to either ComponentProperties or DataObjects.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ComponentProperty, self).__init__()

        self.citations = []                               # shared.Citation (0.N)
        self.description = None                           # unicode (0.1)
        self.grid = None                                  # unicode (0.1)
        self.intent = None                                # software.ComponentPropertyIntentType (0.1)
        self.is_represented = None                        # bool (1.1)
        self.long_name = None                             # unicode (0.1)
        self.short_name = None                            # unicode (1.1)
        self.standard_names = []                          # unicode (0.N)
        self.sub_properties = []                          # software.ComponentProperty (0.N)
        self.units = None                                 # shared.UnitType (0.1)
        self.values = []                                  # unicode (0.N)


class Composition(object):
    """A concrete class within the cim v1 type system.

    The set of Couplings used by a Component. Couplings can only occur between child components. That is, a composition must belong to an ancestor component of the components whose fields are being connected.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Composition, self).__init__()

        self.couplings = []                               # unicode (0.N)
        self.description = None                           # unicode (0.1)


class Connection(object):
    """A concrete class within the cim v1 type system.

    A Connection represents a link from a source DataSource to a target DataSource.  These can either be ComponentProperties (ie: the values come from an internal component) or DataObjects (ie: the values come from an external file).   It can be associated with another software component (a transformer).  If present, the rate, lag, timeTransformation, and spatialRegridding override that of the parent coupling.  Note that there is the potential for multiple connectionSource & connectionTarget and multiple couplingSources & couplingTargets.  This may lead users to wonder how to match up a connection source (a ComponentProperty) with its coupling source (a SoftwareComponent). Clever logic is not required though; because the sources and targets are listed by reference, they can be found in a CIM document and the parent can be navigated to from there - there is no need to consult the source or target of the coupling.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Connection, self).__init__()

        self.description = None                           # unicode (0.1)
        self.priming = None                               # shared.DataSource (0.1)
        self.properties = []                              # software.ConnectionProperty (0.N)
        self.sources = []                                 # software.ConnectionEndpoint (0.N)
        self.spatial_regridding = []                      # software.SpatialRegridding (0.N)
        self.target = None                                # software.ConnectionEndpoint (0.1)
        self.time_lag = None                              # unicode (0.1)
        self.time_profile = None                          # software.Timing (0.1)
        self.time_transformation = None                   # software.TimeTransformation (0.1)
        self.transformers = []                            # software.ProcessorComponent (0.N)
        self.type = None                                  # software.ConnectionType (0.1)


class ConnectionEndpoint(object):
    """A concrete class within the cim v1 type system.

    The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ConnectionEndpoint, self).__init__()

        self.data_source = None                           # shared.DataSource (0.1)
        self.instance_id = None                           # unicode (0.1)
        self.properties = []                              # software.ConnectionProperty (0.N)


class ConnectionProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    A ConnectionProperty is a name/value pair used to specify OASIS-specific properties.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ConnectionProperty, self).__init__()



class Coupling(object):
    """A concrete class within the cim v1 type system.

    A coupling represents a set of Connections between a source and target component. Couplings can be complete or incomplete. If they are complete then they must include all Connections between model properties. If they are incomplete then the connections can be underspecified or not listed at all.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Coupling, self).__init__()

        self.connections = []                             # software.Connection (0.N)
        self.description = None                           # unicode (0.1)
        self.is_fully_specified = None                    # bool (1.1)
        self.priming = None                               # shared.DataSource (0.1)
        self.properties = []                              # software.CouplingProperty (0.N)
        self.purpose = None                               # shared.DataPurpose (1.1)
        self.sources = []                                 # software.CouplingEndpoint (1.N)
        self.spatial_regriddings = []                     # software.SpatialRegridding (0.N)
        self.target = None                                # software.CouplingEndpoint (1.1)
        self.time_lag = None                              # software.TimeLag (0.1)
        self.time_profile = None                          # software.Timing (0.1)
        self.time_transformation = None                   # software.TimeTransformation (0.1)
        self.transformers = []                            # software.ProcessorComponent (0.N)
        self.type = None                                  # software.ConnectionType (0.1)


class CouplingEndpoint(object):
    """A concrete class within the cim v1 type system.

    The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(CouplingEndpoint, self).__init__()

        self.data_source = None                           # shared.DataSource (0.1)
        self.instance_id = None                           # unicode (0.1)
        self.properties = []                              # software.CouplingProperty (0.N)


class CouplingProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    A CouplingProperty is a name/value pair used to specify OASIS-specific properties.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(CouplingProperty, self).__init__()



class Deployment(object):
    """A concrete class within the cim v1 type system.

    Gives information about the technical properties of a component: what machine it was run on, which compilers were used, how it was parallised, etc. A deployment basically associates a deploymentDate with a Platform. A deployment only exists if something has been deployed. A platform, in contrast, can exist independently, waiting to be used in deployments.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Deployment, self).__init__()

        self.deployment_date = None                       # datetime.datetime (0.1)
        self.description = None                           # unicode (0.1)
        self.executable_arguments = []                    # unicode (0.N)
        self.executable_name = None                       # unicode (0.1)
        self.parallelisation = None                       # software.Parallelisation (0.1)
        self.platform = None                              # shared.Platform (0.1)


class EntryPoint(object):
    """A concrete class within the cim v1 type system.

    Describes a function or subroutine of a SoftwareComponent. BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model. Currently, a very basic schedule can be approximated by using the "proceeds" and "follows" attributes, however a more complete system is required for full BFG compatibility. Every EntryPoint can have a set of arguments associated with it. These reference (previously defined) ComponentProperties.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(EntryPoint, self).__init__()

        self.name = None                                  # unicode (0.1)


class Parallelisation(object):
    """A concrete class within the cim v1 type system.

    Describes how a deployment has been parallelised across a computing platform.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Parallelisation, self).__init__()

        self.processes = None                             # int (1.1)
        self.ranks = []                                   # software.Rank (0.N)


class Rank(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of rank class.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Rank, self).__init__()

        self.increment = None                             # int (0.1)
        self.max = None                                   # int (0.1)
        self.min = None                                   # int (0.1)
        self.value = None                                 # int (0.1)


class SpatialRegridding(object):
    """A concrete class within the cim v1 type system.

    Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(SpatialRegridding, self).__init__()

        self.dimension = None                             # software.SpatialRegriddingDimensionType (0.1)
        self.properties = []                              # software.SpatialRegriddingProperty (0.N)
        self.standard_method = None                       # software.SpatialRegriddingStandardMethodType (0.1)
        self.user_method = None                           # software.SpatialRegriddingUserMethod (0.1)


class SpatialRegriddingProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    Used for OASIS-specific regridding information (ie: masked, order, normalisation, etc.)

    """
    def __init__(self):
        """Instance constructor.

        """
        super(SpatialRegriddingProperty, self).__init__()



class SpatialRegriddingUserMethod(object):
    """A concrete class within the cim v1 type system.

    Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(SpatialRegriddingUserMethod, self).__init__()

        self.file = None                                  # data.DataObject (0.1)
        self.name = None                                  # unicode (1.1)


class TimeLag(object):
    """A concrete class within the cim v1 type system.

    The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(TimeLag, self).__init__()

        self.units = None                                 # software.TimingUnits (0.1)
        self.value = None                                 # int (0.1)


class TimeTransformation(object):
    """A concrete class within the cim v1 type system.

    The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(TimeTransformation, self).__init__()

        self.description = None                           # unicode (0.1)
        self.mapping_type = None                          # software.TimeMappingType (1.1)


class Timing(object):
    """A concrete class within the cim v1 type system.

    Provides information about the rate of couplings and connections and/or the timing characteristics of individual components - for example, the start and stop times that the component was run for or the units of time that a component is able to model (in a single timestep).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Timing, self).__init__()

        self.end = None                                   # datetime.datetime (0.1)
        self.is_variable_rate = None                      # bool (0.1)
        self.rate = None                                  # int (0.1)
        self.start = None                                 # datetime.datetime (0.1)
        self.units = None                                 # software.TimingUnits (0.1)


class ModelComponent(Component):
    """A concrete class within the cim v1 type system.

    A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ModelComponent, self).__init__()

        self.activity = None                              # activity.Activity (0.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.timing = None                                # software.Timing (0.1)
        self.type = None                                  # software.ModelComponentType (0.1)
        self.types = []                                   # software.ModelComponentType (1.N)


class ProcessorComponent(Component):
    """A concrete class within the cim v1 type system.

    A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ProcessorComponent, self).__init__()

        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)


class StatisticalModelComponent(Component):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of statistical_model_component class.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(StatisticalModelComponent, self).__init__()

        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.timing = None                                # software.Timing (0.1)
        self.type = None                                  # software.StatisticalModelComponentType (0.1)
        self.types = []                                   # software.StatisticalModelComponentType (1.N)


class ComponentPropertyIntentType(object):
    """An enumeration within the cim v1 type system.

    The direction that the associated component property is intended to be coupled: in, out, or inout.
    """
    is_open = False
    members = [
        "in",
        "out",
        "inout"
        ]
    descriptions = [
        "None",
        "None",
        "None"
        ]


class ConnectionType(object):
    """An enumeration within the cim v1 type system.

    The ConnectionType enumeration describes the mechanism of transport for a connection.
    """
    is_open = True
    members = []
    descriptions = []


class CouplingFrameworkType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of coupling_framework_type enum.
    """
    is_open = False
    members = [
        "BFG",
        "ESMF",
        "OASIS"
        ]
    descriptions = [
        "None",
        "None",
        "None"
        ]


class ModelComponentType(object):
    """An enumeration within the cim v1 type system.

    An enumeration of types of ModelComponent. This includes things like atmosphere & ocean models, radiation schemes, etc. CIM best-practice is to describe every component for which there is a named ComponentType as a separate component, even if it is not a separate unit of software (ie: even if it is embedded), instead of as a (set of) ModelParameters. This codelist is synonomous with "realm" for the purposes of CMIP5.
    """
    is_open = True
    members = []
    descriptions = []


class SpatialRegriddingDimensionType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of spatial_regridding_dimension_type enum.
    """
    is_open = False
    members = [
        "1D",
        "2D",
        "3D"
        ]
    descriptions = [
        "None",
        "None",
        "None"
        ]


class SpatialRegriddingStandardMethodType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of spatial_regridding_standard_method_type enum.
    """
    is_open = False
    members = [
        "linear",
        "near-neighbour",
        "cubic",
        "conservative-first-order",
        "conservative-second-order",
        "conservative",
        "non-conservative"
        ]
    descriptions = [
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None"
        ]


class StatisticalModelComponentType(object):
    """An enumeration within the cim v1 type system.

    An enumeration of types of ProcessorComponent.  This includes things like transformers and post-processors.
    """
    is_open = True
    members = []
    descriptions = []


class TimeMappingType(object):
    """An enumeration within the cim v1 type system.

    Enumerates the different ways that time can be mapped when transforming from one field to another.
    """
    is_open = True
    members = []
    descriptions = []


class TimingUnits(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of timing_units enum.
    """
    is_open = False
    members = [
        "seconds",
        "minutes",
        "hours",
        "days",
        "months",
        "years",
        "decades",
        "centuries"
        ]
    descriptions = [
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None"
        ]


