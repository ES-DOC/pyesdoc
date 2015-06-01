# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_for_software_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.software package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-01 16:50:10.368351.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class Component(shared.DataSource):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of _component class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Component, self).__init__()

        self.citations = []                               # shared.Citation
        self.code_access = None                           # str
        self.composition = None                           # software.Composition
        self.coupling_framework = None                    # software.CouplingFrameworkType
        self.dependencies = []                            # software.EntryPoint
        self.deployments = []                             # software.Deployment
        self.description = None                           # str
        self.funding_sources = []                         # str
        self.grid = None                                  # grids.GridSpec
        self.is_embedded = None                           # bool
        self.language = None                              # software.ComponentLanguage
        self.license = None                               # shared.License
        self.long_name = None                             # str
        self.online_resource = None                       # str
        self.parent = None                                # software.Component
        self.previous_version = None                      # str
        self.properties = []                              # software.ComponentProperty
        self.release_date = None                          # datetime.datetime
        self.responsible_parties = []                     # shared.ResponsibleParty
        self.short_name = None                            # str
        self.sub_components = []                          # software.Component
        self.version = None                               # str


class ComponentLanguage(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of component_language class.

    """
    def __init__(self):
        """Constructor.

        """
        super(ComponentLanguage, self).__init__()

        self.name = None                                  # str
        self.properties = []                              # software.ComponentLanguageProperty


class ComponentLanguageProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of component_language_property class.

    """
    def __init__(self):
        """Constructor.

        """
        super(ComponentLanguageProperty, self).__init__()



class ComponentProperty(shared.DataSource):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of _component_property class.

    """
    def __init__(self):
        """Constructor.

        """
        super(ComponentProperty, self).__init__()

        self.citations = []                               # shared.Citation
        self.description = None                           # str
        self.grid = None                                  # str
        self.intent = None                                # software.ComponentPropertyIntentType
        self.is_represented = None                        # bool
        self.long_name = None                             # str
        self.short_name = None                            # str
        self.standard_names = []                          # str
        self.sub_properties = []                          # software.ComponentProperty
        self.units = None                                 # shared.UnitType
        self.values = []                                  # str


class Composition(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of composition class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Composition, self).__init__()

        self.couplings = []                               # str
        self.description = None                           # str


class Connection(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of connection class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Connection, self).__init__()

        self.description = None                           # str
        self.priming = None                               # shared.DataSource
        self.priming_reference = None                     # shared.DocReference
        self.properties = []                              # software.ConnectionProperty
        self.sources = []                                 # software.ConnectionEndpoint
        self.spatial_regridding = []                      # software.SpatialRegridding
        self.target = None                                # software.ConnectionEndpoint
        self.time_lag = None                              # str
        self.time_profile = None                          # software.Timing
        self.time_transformation = None                   # software.TimeTransformation
        self.transformers = []                            # software.ProcessorComponent
        self.transformers_references = []                 # shared.DocReference
        self.type = None                                  # software.ConnectionType


class ConnectionEndpoint(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of connection_endpoint class.

    """
    def __init__(self):
        """Constructor.

        """
        super(ConnectionEndpoint, self).__init__()

        self.data_source = None                           # shared.DataSource
        self.data_source_reference = None                 # shared.DocReference
        self.instance_id = None                           # str
        self.properties = []                              # software.ConnectionProperty


class ConnectionProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of connection_property class.

    """
    def __init__(self):
        """Constructor.

        """
        super(ConnectionProperty, self).__init__()



class Coupling(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of coupling class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Coupling, self).__init__()

        self.connections = []                             # software.Connection
        self.description = None                           # str
        self.is_fully_specified = None                    # bool
        self.priming = None                               # shared.DataSource
        self.priming_reference = None                     # shared.DocReference
        self.properties = []                              # software.CouplingProperty
        self.purpose = None                               # shared.DataPurpose
        self.sources = []                                 # software.CouplingEndpoint
        self.spatial_regriddings = []                     # software.SpatialRegridding
        self.target = None                                # software.CouplingEndpoint
        self.time_lag = None                              # software.TimeLag
        self.time_profile = None                          # software.Timing
        self.time_transformation = None                   # software.TimeTransformation
        self.transformers = []                            # software.ProcessorComponent
        self.transformers_references = []                 # shared.DocReference
        self.type = None                                  # software.ConnectionType


class CouplingEndpoint(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of coupling_endpoint class.

    """
    def __init__(self):
        """Constructor.

        """
        super(CouplingEndpoint, self).__init__()

        self.data_source = None                           # shared.DataSource
        self.data_source_reference = None                 # shared.DocReference
        self.instance_id = None                           # str
        self.properties = []                              # software.CouplingProperty


class CouplingProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of coupling_property class.

    """
    def __init__(self):
        """Constructor.

        """
        super(CouplingProperty, self).__init__()



class Deployment(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of deployment class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Deployment, self).__init__()

        self.deployment_date = None                       # datetime.datetime
        self.description = None                           # str
        self.executable_arguments = []                    # str
        self.executable_name = None                       # str
        self.parallelisation = None                       # software.Parallelisation
        self.platform = None                              # shared.Platform
        self.platform_reference = None                    # shared.DocReference


class EntryPoint(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of entry_point class.

    """
    def __init__(self):
        """Constructor.

        """
        super(EntryPoint, self).__init__()

        self.name = None                                  # str


class Parallelisation(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of parallelisation class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Parallelisation, self).__init__()

        self.processes = None                             # int
        self.ranks = []                                   # software.Rank


class Rank(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of rank class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Rank, self).__init__()

        self.increment = None                             # int
        self.max = None                                   # int
        self.min = None                                   # int
        self.value = None                                 # int


class SpatialRegridding(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of spatial_regridding class.

    """
    def __init__(self):
        """Constructor.

        """
        super(SpatialRegridding, self).__init__()

        self.dimension = None                             # software.SpatialRegriddingDimensionType
        self.properties = []                              # software.SpatialRegriddingProperty
        self.standard_method = None                       # software.SpatialRegriddingStandardMethodType
        self.user_method = None                           # software.SpatialRegriddingUserMethod


class SpatialRegriddingProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of spatial_regridding_property class.

    """
    def __init__(self):
        """Constructor.

        """
        super(SpatialRegriddingProperty, self).__init__()



class SpatialRegriddingUserMethod(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of spatial_regridding_user_method class.

    """
    def __init__(self):
        """Constructor.

        """
        super(SpatialRegriddingUserMethod, self).__init__()

        self.file = None                                  # data.DataObject
        self.file_reference = None                        # shared.DocReference
        self.name = None                                  # str


class TimeLag(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of time_lag class.

    """
    def __init__(self):
        """Constructor.

        """
        super(TimeLag, self).__init__()

        self.units = None                                 # software.TimingUnits
        self.value = None                                 # int


class TimeTransformation(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of time_transformation class.

    """
    def __init__(self):
        """Constructor.

        """
        super(TimeTransformation, self).__init__()

        self.description = None                           # str
        self.mapping_type = None                          # software.TimeMappingType


class Timing(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of timing class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Timing, self).__init__()

        self.end = None                                   # datetime.datetime
        self.is_variable_rate = None                      # bool
        self.rate = None                                  # int
        self.start = None                                 # datetime.datetime
        self.units = None                                 # software.TimingUnits


class ModelComponent(Component):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of model_component class.

    """
    def __init__(self):
        """Constructor.

        """
        super(ModelComponent, self).__init__()

        self.activity = None                              # activity.Activity
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.timing = None                                # software.Timing
        self.type = None                                  # software.ModelComponentType
        self.types = []                                   # software.ModelComponentType


class ProcessorComponent(Component):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of processor_component class.

    """
    def __init__(self):
        """Constructor.

        """
        super(ProcessorComponent, self).__init__()

        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo


class StatisticalModelComponent(Component):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of statistical_model_component class.

    """
    def __init__(self):
        """Constructor.

        """
        super(StatisticalModelComponent, self).__init__()

        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.timing = None                                # software.Timing
        self.type = None                                  # software.StatisticalModelComponentType
        self.types = []                                   # software.StatisticalModelComponentType


class ComponentPropertyIntentType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of component_property_intent_type enum.
    """

    pass


class ConnectionType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of connection_type enum.
    """

    pass


class CouplingFrameworkType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of coupling_framework_type enum.
    """

    pass


class ModelComponentType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of model_component_type enum.
    """

    pass


class SpatialRegriddingDimensionType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of spatial_regridding_dimension_type enum.
    """

    pass


class SpatialRegriddingStandardMethodType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of spatial_regridding_standard_method_type enum.
    """

    pass


class StatisticalModelComponentType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of statistical_model_component_type enum.
    """

    pass


class TimeMappingType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of time_mapping_type enum.
    """

    pass


class TimingUnits(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of timing_units enum.
    """

    pass


