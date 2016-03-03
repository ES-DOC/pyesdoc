
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.keys.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The ontology map of types to keys.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import typeset_for_data_package as data
import typeset_for_software_package as software
import typeset_for_shared_package as shared
import typeset_for_grids_package as grids
import typeset_for_quality_package as quality
import typeset_for_misc_package as misc
import typeset_for_activity_package as activity




# Map of ontology types to type keys.
KEYS = {
    # ------------------------------------------------
    # Packages.
    # ------------------------------------------------

    data: "cim.1.data",

    software: "cim.1.software",

    shared: "cim.1.shared",

    grids: "cim.1.grids",

    quality: "cim.1.quality",

    misc: "cim.1.misc",

    activity: "cim.1.activity",

    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------


    data.DataStorage: "cim.1.data.DataStorage",

    data.DataStorageDb: "cim.1.data.DataStorageDb",

    data.DataExtentTemporal: "cim.1.data.DataExtentTemporal",

    data.DataExtent: "cim.1.data.DataExtent",

    data.DataStorageIp: "cim.1.data.DataStorageIp",

    data.DataExtentTimeInterval: "cim.1.data.DataExtentTimeInterval",

    data.DataContent: "cim.1.data.DataContent",

    data.DataRestriction: "cim.1.data.DataRestriction",

    data.DataDistribution: "cim.1.data.DataDistribution",

    data.DataStorageFile: "cim.1.data.DataStorageFile",

    data.DataProperty: "cim.1.data.DataProperty",

    data.DataObject: "cim.1.data.DataObject",

    data.DataExtentGeographical: "cim.1.data.DataExtentGeographical",

    data.DataTopic: "cim.1.data.DataTopic",

    data.DataHierarchyLevel: "cim.1.data.DataHierarchyLevel",



    software.ComponentLanguageProperty: "cim.1.software.ComponentLanguageProperty",

    software.Composition: "cim.1.software.Composition",

    software.Parallelisation: "cim.1.software.Parallelisation",

    software.ModelComponent: "cim.1.software.ModelComponent",

    software.ProcessorComponent: "cim.1.software.ProcessorComponent",

    software.StatisticalModelComponent: "cim.1.software.StatisticalModelComponent",

    software.ComponentLanguage: "cim.1.software.ComponentLanguage",

    software.CouplingProperty: "cim.1.software.CouplingProperty",

    software.SpatialRegridding: "cim.1.software.SpatialRegridding",

    software.TimeTransformation: "cim.1.software.TimeTransformation",

    software.Connection: "cim.1.software.Connection",

    software.Component: "cim.1.software.Component",

    software.TimeLag: "cim.1.software.TimeLag",

    software.EntryPoint: "cim.1.software.EntryPoint",

    software.SpatialRegriddingProperty: "cim.1.software.SpatialRegriddingProperty",

    software.ConnectionEndpoint: "cim.1.software.ConnectionEndpoint",

    software.CouplingEndpoint: "cim.1.software.CouplingEndpoint",

    software.Timing: "cim.1.software.Timing",

    software.Rank: "cim.1.software.Rank",

    software.SpatialRegriddingUserMethod: "cim.1.software.SpatialRegriddingUserMethod",

    software.ComponentProperty: "cim.1.software.ComponentProperty",

    software.ConnectionProperty: "cim.1.software.ConnectionProperty",

    software.Coupling: "cim.1.software.Coupling",

    software.Deployment: "cim.1.software.Deployment",



    shared.PerpetualPeriod: "cim.1.shared.PerpetualPeriod",

    shared.OpenDateRange: "cim.1.shared.OpenDateRange",

    shared.Relationship: "cim.1.shared.Relationship",

    shared.ChangeProperty: "cim.1.shared.ChangeProperty",

    shared.ClosedDateRange: "cim.1.shared.ClosedDateRange",

    shared.DocReference: "cim.1.shared.DocReference",

    shared.Change: "cim.1.shared.Change",

    shared.Standard: "cim.1.shared.Standard",

    shared.DocMetaInfo: "cim.1.shared.DocMetaInfo",

    shared.Citation: "cim.1.shared.Citation",

    shared.Platform: "cim.1.shared.Platform",

    shared.Calendar: "cim.1.shared.Calendar",

    shared.DocGenealogy: "cim.1.shared.DocGenealogy",

    shared.DocRelationship: "cim.1.shared.DocRelationship",

    shared.RealCalendar: "cim.1.shared.RealCalendar",

    shared.DataSource: "cim.1.shared.DataSource",

    shared.Machine: "cim.1.shared.Machine",

    shared.StandardName: "cim.1.shared.StandardName",

    shared.DocRelationshipTarget: "cim.1.shared.DocRelationshipTarget",

    shared.MachineCompilerUnit: "cim.1.shared.MachineCompilerUnit",

    shared.Property: "cim.1.shared.Property",

    shared.ResponsibleParty: "cim.1.shared.ResponsibleParty",

    shared.Daily360: "cim.1.shared.Daily360",

    shared.License: "cim.1.shared.License",

    shared.Compiler: "cim.1.shared.Compiler",

    shared.DateRange: "cim.1.shared.DateRange",



    grids.GridSpec: "cim.1.grids.GridSpec",

    grids.SimpleGridGeometry: "cim.1.grids.SimpleGridGeometry",

    grids.CoordinateList: "cim.1.grids.CoordinateList",

    grids.GridTileResolutionType: "cim.1.grids.GridTileResolutionType",

    grids.GridTile: "cim.1.grids.GridTile",

    grids.GridMosaic: "cim.1.grids.GridMosaic",

    grids.VerticalCoordinateList: "cim.1.grids.VerticalCoordinateList",

    grids.GridProperty: "cim.1.grids.GridProperty",

    grids.GridExtent: "cim.1.grids.GridExtent",



    quality.CimQuality: "cim.1.quality.CimQuality",

    quality.Measure: "cim.1.quality.Measure",

    quality.Report: "cim.1.quality.Report",

    quality.Evaluation: "cim.1.quality.Evaluation",



    misc.DocumentSet: "cim.1.misc.DocumentSet",



    activity.Simulation: "cim.1.activity.Simulation",

    activity.SimulationRun: "cim.1.activity.SimulationRun",

    activity.InitialCondition: "cim.1.activity.InitialCondition",

    activity.Experiment: "cim.1.activity.Experiment",

    activity.Activity: "cim.1.activity.Activity",

    activity.Conformance: "cim.1.activity.Conformance",

    activity.NumericalRequirementOption: "cim.1.activity.NumericalRequirementOption",

    activity.OutputRequirement: "cim.1.activity.OutputRequirement",

    activity.NumericalActivity: "cim.1.activity.NumericalActivity",

    activity.SimulationRelationship: "cim.1.activity.SimulationRelationship",

    activity.PhysicalModification: "cim.1.activity.PhysicalModification",

    activity.ExperimentRelationship: "cim.1.activity.ExperimentRelationship",

    activity.EnsembleMember: "cim.1.activity.EnsembleMember",

    activity.MeasurementCampaign: "cim.1.activity.MeasurementCampaign",

    activity.DownscalingSimulation: "cim.1.activity.DownscalingSimulation",

    activity.NumericalExperiment: "cim.1.activity.NumericalExperiment",

    activity.BoundaryCondition: "cim.1.activity.BoundaryCondition",

    activity.SimulationRelationshipTarget: "cim.1.activity.SimulationRelationshipTarget",

    activity.Ensemble: "cim.1.activity.Ensemble",

    activity.ExperimentRelationshipTarget: "cim.1.activity.ExperimentRelationshipTarget",

    activity.NumericalRequirement: "cim.1.activity.NumericalRequirement",

    activity.SpatioTemporalConstraint: "cim.1.activity.SpatioTemporalConstraint",

    activity.LateralBoundaryCondition: "cim.1.activity.LateralBoundaryCondition",

    activity.SimulationComposite: "cim.1.activity.SimulationComposite",


    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------



    (data.DataStorage, 'size'): "cim.1.data.DataStorage.size",

    (data.DataStorage, 'format'): "cim.1.data.DataStorage.format",

    (data.DataStorage, 'modification_date'): "cim.1.data.DataStorage.modification_date",

    (data.DataStorage, 'location'): "cim.1.data.DataStorage.location",



    (data.DataStorageDb, 'access_string'): "cim.1.data.DataStorageDb.access_string",

    (data.DataStorageDb, 'table'): "cim.1.data.DataStorageDb.table",

    (data.DataStorageDb, 'owner'): "cim.1.data.DataStorageDb.owner",

    (data.DataStorageDb, 'name'): "cim.1.data.DataStorageDb.name",



    (data.DataExtentTemporal, 'begin'): "cim.1.data.DataExtentTemporal.begin",

    (data.DataExtentTemporal, 'time_interval'): "cim.1.data.DataExtentTemporal.time_interval",

    (data.DataExtentTemporal, 'end'): "cim.1.data.DataExtentTemporal.end",



    (data.DataExtent, 'geographical'): "cim.1.data.DataExtent.geographical",

    (data.DataExtent, 'temporal'): "cim.1.data.DataExtent.temporal",



    (data.DataStorageIp, 'path'): "cim.1.data.DataStorageIp.path",

    (data.DataStorageIp, 'protocol'): "cim.1.data.DataStorageIp.protocol",

    (data.DataStorageIp, 'file_name'): "cim.1.data.DataStorageIp.file_name",

    (data.DataStorageIp, 'host'): "cim.1.data.DataStorageIp.host",



    (data.DataExtentTimeInterval, 'unit'): "cim.1.data.DataExtentTimeInterval.unit",

    (data.DataExtentTimeInterval, 'factor'): "cim.1.data.DataExtentTimeInterval.factor",

    (data.DataExtentTimeInterval, 'radix'): "cim.1.data.DataExtentTimeInterval.radix",



    (data.DataContent, 'aggregation'): "cim.1.data.DataContent.aggregation",

    (data.DataContent, 'topic'): "cim.1.data.DataContent.topic",

    (data.DataContent, 'frequency'): "cim.1.data.DataContent.frequency",



    (data.DataRestriction, 'license'): "cim.1.data.DataRestriction.license",

    (data.DataRestriction, 'scope'): "cim.1.data.DataRestriction.scope",

    (data.DataRestriction, 'restriction'): "cim.1.data.DataRestriction.restriction",



    (data.DataDistribution, 'responsible_party'): "cim.1.data.DataDistribution.responsible_party",

    (data.DataDistribution, 'format'): "cim.1.data.DataDistribution.format",

    (data.DataDistribution, 'access'): "cim.1.data.DataDistribution.access",

    (data.DataDistribution, 'fee'): "cim.1.data.DataDistribution.fee",



    (data.DataStorageFile, 'file_system'): "cim.1.data.DataStorageFile.file_system",

    (data.DataStorageFile, 'file_name'): "cim.1.data.DataStorageFile.file_name",

    (data.DataStorageFile, 'path'): "cim.1.data.DataStorageFile.path",



    (data.DataProperty, 'description'): "cim.1.data.DataProperty.description",



    (data.DataObject, 'hierarchy_level'): "cim.1.data.DataObject.hierarchy_level",

    (data.DataObject, 'citations'): "cim.1.data.DataObject.citations",

    (data.DataObject, 'keyword'): "cim.1.data.DataObject.keyword",

    (data.DataObject, 'distribution'): "cim.1.data.DataObject.distribution",

    (data.DataObject, 'purpose'): "cim.1.data.DataObject.purpose",

    (data.DataObject, 'content'): "cim.1.data.DataObject.content",

    (data.DataObject, 'properties'): "cim.1.data.DataObject.properties",

    (data.DataObject, 'child_object'): "cim.1.data.DataObject.child_object",

    (data.DataObject, 'extent'): "cim.1.data.DataObject.extent",

    (data.DataObject, 'meta'): "cim.1.data.DataObject.meta",

    (data.DataObject, 'data_status'): "cim.1.data.DataObject.data_status",

    (data.DataObject, 'parent_object'): "cim.1.data.DataObject.parent_object",

    (data.DataObject, 'geometry_model'): "cim.1.data.DataObject.geometry_model",

    (data.DataObject, 'source_simulation'): "cim.1.data.DataObject.source_simulation",

    (data.DataObject, 'storage'): "cim.1.data.DataObject.storage",

    (data.DataObject, 'description'): "cim.1.data.DataObject.description",

    (data.DataObject, 'restriction'): "cim.1.data.DataObject.restriction",

    (data.DataObject, 'acronym'): "cim.1.data.DataObject.acronym",



    (data.DataExtentGeographical, 'south'): "cim.1.data.DataExtentGeographical.south",

    (data.DataExtentGeographical, 'west'): "cim.1.data.DataExtentGeographical.west",

    (data.DataExtentGeographical, 'east'): "cim.1.data.DataExtentGeographical.east",

    (data.DataExtentGeographical, 'north'): "cim.1.data.DataExtentGeographical.north",



    (data.DataTopic, 'unit'): "cim.1.data.DataTopic.unit",

    (data.DataTopic, 'description'): "cim.1.data.DataTopic.description",

    (data.DataTopic, 'name'): "cim.1.data.DataTopic.name",



    (data.DataHierarchyLevel, 'is_open'): "cim.1.data.DataHierarchyLevel.is_open",

    (data.DataHierarchyLevel, 'value'): "cim.1.data.DataHierarchyLevel.value",

    (data.DataHierarchyLevel, 'name'): "cim.1.data.DataHierarchyLevel.name",







    (software.Composition, 'couplings'): "cim.1.software.Composition.couplings",

    (software.Composition, 'description'): "cim.1.software.Composition.description",



    (software.Parallelisation, 'processes'): "cim.1.software.Parallelisation.processes",

    (software.Parallelisation, 'ranks'): "cim.1.software.Parallelisation.ranks",



    (software.ModelComponent, 'activity'): "cim.1.software.ModelComponent.activity",

    (software.ModelComponent, 'type'): "cim.1.software.ModelComponent.type",

    (software.ModelComponent, 'meta'): "cim.1.software.ModelComponent.meta",

    (software.ModelComponent, 'types'): "cim.1.software.ModelComponent.types",

    (software.ModelComponent, 'timing'): "cim.1.software.ModelComponent.timing",



    (software.ProcessorComponent, 'meta'): "cim.1.software.ProcessorComponent.meta",



    (software.StatisticalModelComponent, 'type'): "cim.1.software.StatisticalModelComponent.type",

    (software.StatisticalModelComponent, 'meta'): "cim.1.software.StatisticalModelComponent.meta",

    (software.StatisticalModelComponent, 'types'): "cim.1.software.StatisticalModelComponent.types",

    (software.StatisticalModelComponent, 'timing'): "cim.1.software.StatisticalModelComponent.timing",



    (software.ComponentLanguage, 'name'): "cim.1.software.ComponentLanguage.name",

    (software.ComponentLanguage, 'properties'): "cim.1.software.ComponentLanguage.properties",





    (software.SpatialRegridding, 'standard_method'): "cim.1.software.SpatialRegridding.standard_method",

    (software.SpatialRegridding, 'dimension'): "cim.1.software.SpatialRegridding.dimension",

    (software.SpatialRegridding, 'user_method'): "cim.1.software.SpatialRegridding.user_method",

    (software.SpatialRegridding, 'properties'): "cim.1.software.SpatialRegridding.properties",



    (software.TimeTransformation, 'description'): "cim.1.software.TimeTransformation.description",

    (software.TimeTransformation, 'mapping_type'): "cim.1.software.TimeTransformation.mapping_type",



    (software.Connection, 'properties'): "cim.1.software.Connection.properties",

    (software.Connection, 'time_transformation'): "cim.1.software.Connection.time_transformation",

    (software.Connection, 'priming'): "cim.1.software.Connection.priming",

    (software.Connection, 'spatial_regridding'): "cim.1.software.Connection.spatial_regridding",

    (software.Connection, 'time_lag'): "cim.1.software.Connection.time_lag",

    (software.Connection, 'transformers'): "cim.1.software.Connection.transformers",

    (software.Connection, 'target'): "cim.1.software.Connection.target",

    (software.Connection, 'type'): "cim.1.software.Connection.type",

    (software.Connection, 'sources'): "cim.1.software.Connection.sources",

    (software.Connection, 'description'): "cim.1.software.Connection.description",

    (software.Connection, 'time_profile'): "cim.1.software.Connection.time_profile",



    (software.Component, 'description'): "cim.1.software.Component.description",

    (software.Component, 'funding_sources'): "cim.1.software.Component.funding_sources",

    (software.Component, 'code_access'): "cim.1.software.Component.code_access",

    (software.Component, 'grid'): "cim.1.software.Component.grid",

    (software.Component, 'is_embedded'): "cim.1.software.Component.is_embedded",

    (software.Component, 'language'): "cim.1.software.Component.language",

    (software.Component, 'license'): "cim.1.software.Component.license",

    (software.Component, 'sub_components'): "cim.1.software.Component.sub_components",

    (software.Component, 'long_name'): "cim.1.software.Component.long_name",

    (software.Component, 'online_resource'): "cim.1.software.Component.online_resource",

    (software.Component, 'release_date'): "cim.1.software.Component.release_date",

    (software.Component, 'parent'): "cim.1.software.Component.parent",

    (software.Component, 'previous_version'): "cim.1.software.Component.previous_version",

    (software.Component, 'properties'): "cim.1.software.Component.properties",

    (software.Component, 'composition'): "cim.1.software.Component.composition",

    (software.Component, 'citations'): "cim.1.software.Component.citations",

    (software.Component, 'coupling_framework'): "cim.1.software.Component.coupling_framework",

    (software.Component, 'short_name'): "cim.1.software.Component.short_name",

    (software.Component, 'dependencies'): "cim.1.software.Component.dependencies",

    (software.Component, 'responsible_parties'): "cim.1.software.Component.responsible_parties",

    (software.Component, 'version'): "cim.1.software.Component.version",

    (software.Component, 'deployments'): "cim.1.software.Component.deployments",



    (software.TimeLag, 'units'): "cim.1.software.TimeLag.units",

    (software.TimeLag, 'value'): "cim.1.software.TimeLag.value",



    (software.EntryPoint, 'name'): "cim.1.software.EntryPoint.name",





    (software.ConnectionEndpoint, 'data_source'): "cim.1.software.ConnectionEndpoint.data_source",

    (software.ConnectionEndpoint, 'properties'): "cim.1.software.ConnectionEndpoint.properties",

    (software.ConnectionEndpoint, 'instance_id'): "cim.1.software.ConnectionEndpoint.instance_id",



    (software.CouplingEndpoint, 'properties'): "cim.1.software.CouplingEndpoint.properties",

    (software.CouplingEndpoint, 'data_source'): "cim.1.software.CouplingEndpoint.data_source",

    (software.CouplingEndpoint, 'instance_id'): "cim.1.software.CouplingEndpoint.instance_id",



    (software.Timing, 'start'): "cim.1.software.Timing.start",

    (software.Timing, 'end'): "cim.1.software.Timing.end",

    (software.Timing, 'units'): "cim.1.software.Timing.units",

    (software.Timing, 'rate'): "cim.1.software.Timing.rate",

    (software.Timing, 'is_variable_rate'): "cim.1.software.Timing.is_variable_rate",



    (software.Rank, 'increment'): "cim.1.software.Rank.increment",

    (software.Rank, 'value'): "cim.1.software.Rank.value",

    (software.Rank, 'max'): "cim.1.software.Rank.max",

    (software.Rank, 'min'): "cim.1.software.Rank.min",



    (software.SpatialRegriddingUserMethod, 'file'): "cim.1.software.SpatialRegriddingUserMethod.file",

    (software.SpatialRegriddingUserMethod, 'name'): "cim.1.software.SpatialRegriddingUserMethod.name",



    (software.ComponentProperty, 'is_represented'): "cim.1.software.ComponentProperty.is_represented",

    (software.ComponentProperty, 'units'): "cim.1.software.ComponentProperty.units",

    (software.ComponentProperty, 'short_name'): "cim.1.software.ComponentProperty.short_name",

    (software.ComponentProperty, 'description'): "cim.1.software.ComponentProperty.description",

    (software.ComponentProperty, 'grid'): "cim.1.software.ComponentProperty.grid",

    (software.ComponentProperty, 'standard_names'): "cim.1.software.ComponentProperty.standard_names",

    (software.ComponentProperty, 'values'): "cim.1.software.ComponentProperty.values",

    (software.ComponentProperty, 'long_name'): "cim.1.software.ComponentProperty.long_name",

    (software.ComponentProperty, 'intent'): "cim.1.software.ComponentProperty.intent",

    (software.ComponentProperty, 'citations'): "cim.1.software.ComponentProperty.citations",

    (software.ComponentProperty, 'sub_properties'): "cim.1.software.ComponentProperty.sub_properties",





    (software.Coupling, 'description'): "cim.1.software.Coupling.description",

    (software.Coupling, 'time_transformation'): "cim.1.software.Coupling.time_transformation",

    (software.Coupling, 'transformers'): "cim.1.software.Coupling.transformers",

    (software.Coupling, 'spatial_regriddings'): "cim.1.software.Coupling.spatial_regriddings",

    (software.Coupling, 'sources'): "cim.1.software.Coupling.sources",

    (software.Coupling, 'properties'): "cim.1.software.Coupling.properties",

    (software.Coupling, 'purpose'): "cim.1.software.Coupling.purpose",

    (software.Coupling, 'time_lag'): "cim.1.software.Coupling.time_lag",

    (software.Coupling, 'type'): "cim.1.software.Coupling.type",

    (software.Coupling, 'target'): "cim.1.software.Coupling.target",

    (software.Coupling, 'time_profile'): "cim.1.software.Coupling.time_profile",

    (software.Coupling, 'is_fully_specified'): "cim.1.software.Coupling.is_fully_specified",

    (software.Coupling, 'priming'): "cim.1.software.Coupling.priming",

    (software.Coupling, 'connections'): "cim.1.software.Coupling.connections",



    (software.Deployment, 'deployment_date'): "cim.1.software.Deployment.deployment_date",

    (software.Deployment, 'executable_name'): "cim.1.software.Deployment.executable_name",

    (software.Deployment, 'executable_arguments'): "cim.1.software.Deployment.executable_arguments",

    (software.Deployment, 'parallelisation'): "cim.1.software.Deployment.parallelisation",

    (software.Deployment, 'description'): "cim.1.software.Deployment.description",

    (software.Deployment, 'platform'): "cim.1.software.Deployment.platform",







    (shared.OpenDateRange, 'end'): "cim.1.shared.OpenDateRange.end",

    (shared.OpenDateRange, 'start'): "cim.1.shared.OpenDateRange.start",



    (shared.Relationship, 'description'): "cim.1.shared.Relationship.description",

    (shared.Relationship, 'direction'): "cim.1.shared.Relationship.direction",



    (shared.ChangeProperty, 'description'): "cim.1.shared.ChangeProperty.description",

    (shared.ChangeProperty, 'id'): "cim.1.shared.ChangeProperty.id",



    (shared.ClosedDateRange, 'end'): "cim.1.shared.ClosedDateRange.end",

    (shared.ClosedDateRange, 'start'): "cim.1.shared.ClosedDateRange.start",



    (shared.DocReference, 'type'): "cim.1.shared.DocReference.type",

    (shared.DocReference, 'version'): "cim.1.shared.DocReference.version",

    (shared.DocReference, 'external_id'): "cim.1.shared.DocReference.external_id",

    (shared.DocReference, 'changes'): "cim.1.shared.DocReference.changes",

    (shared.DocReference, 'id'): "cim.1.shared.DocReference.id",

    (shared.DocReference, 'url'): "cim.1.shared.DocReference.url",

    (shared.DocReference, 'name'): "cim.1.shared.DocReference.name",

    (shared.DocReference, 'description'): "cim.1.shared.DocReference.description",



    (shared.Change, 'details'): "cim.1.shared.Change.details",

    (shared.Change, 'name'): "cim.1.shared.Change.name",

    (shared.Change, 'author'): "cim.1.shared.Change.author",

    (shared.Change, 'type'): "cim.1.shared.Change.type",

    (shared.Change, 'description'): "cim.1.shared.Change.description",

    (shared.Change, 'date'): "cim.1.shared.Change.date",



    (shared.Standard, 'version'): "cim.1.shared.Standard.version",

    (shared.Standard, 'description'): "cim.1.shared.Standard.description",

    (shared.Standard, 'name'): "cim.1.shared.Standard.name",



    (shared.DocMetaInfo, 'drs_keys'): "cim.1.shared.DocMetaInfo.drs_keys",

    (shared.DocMetaInfo, 'project'): "cim.1.shared.DocMetaInfo.project",

    (shared.DocMetaInfo, 'type_sort_key'): "cim.1.shared.DocMetaInfo.type_sort_key",

    (shared.DocMetaInfo, 'version'): "cim.1.shared.DocMetaInfo.version",

    (shared.DocMetaInfo, 'id'): "cim.1.shared.DocMetaInfo.id",

    (shared.DocMetaInfo, 'create_date'): "cim.1.shared.DocMetaInfo.create_date",

    (shared.DocMetaInfo, 'source_key'): "cim.1.shared.DocMetaInfo.source_key",

    (shared.DocMetaInfo, 'author'): "cim.1.shared.DocMetaInfo.author",

    (shared.DocMetaInfo, 'institute'): "cim.1.shared.DocMetaInfo.institute",

    (shared.DocMetaInfo, 'status'): "cim.1.shared.DocMetaInfo.status",

    (shared.DocMetaInfo, 'genealogy'): "cim.1.shared.DocMetaInfo.genealogy",

    (shared.DocMetaInfo, 'sort_key'): "cim.1.shared.DocMetaInfo.sort_key",

    (shared.DocMetaInfo, 'type_display_name'): "cim.1.shared.DocMetaInfo.type_display_name",

    (shared.DocMetaInfo, 'update_date'): "cim.1.shared.DocMetaInfo.update_date",

    (shared.DocMetaInfo, 'external_ids'): "cim.1.shared.DocMetaInfo.external_ids",

    (shared.DocMetaInfo, 'source'): "cim.1.shared.DocMetaInfo.source",

    (shared.DocMetaInfo, 'drs_path'): "cim.1.shared.DocMetaInfo.drs_path",

    (shared.DocMetaInfo, 'language'): "cim.1.shared.DocMetaInfo.language",

    (shared.DocMetaInfo, 'type'): "cim.1.shared.DocMetaInfo.type",



    (shared.Citation, 'location'): "cim.1.shared.Citation.location",

    (shared.Citation, 'date_type'): "cim.1.shared.Citation.date_type",

    (shared.Citation, 'date'): "cim.1.shared.Citation.date",

    (shared.Citation, 'title'): "cim.1.shared.Citation.title",

    (shared.Citation, 'type'): "cim.1.shared.Citation.type",

    (shared.Citation, 'alternative_title'): "cim.1.shared.Citation.alternative_title",

    (shared.Citation, 'collective_title'): "cim.1.shared.Citation.collective_title",

    (shared.Citation, 'organisation'): "cim.1.shared.Citation.organisation",

    (shared.Citation, 'role'): "cim.1.shared.Citation.role",



    (shared.Platform, 'contacts'): "cim.1.shared.Platform.contacts",

    (shared.Platform, 'units'): "cim.1.shared.Platform.units",

    (shared.Platform, 'description'): "cim.1.shared.Platform.description",

    (shared.Platform, 'long_name'): "cim.1.shared.Platform.long_name",

    (shared.Platform, 'short_name'): "cim.1.shared.Platform.short_name",

    (shared.Platform, 'meta'): "cim.1.shared.Platform.meta",



    (shared.Calendar, 'range'): "cim.1.shared.Calendar.range",

    (shared.Calendar, 'description'): "cim.1.shared.Calendar.description",

    (shared.Calendar, 'length'): "cim.1.shared.Calendar.length",



    (shared.DocGenealogy, 'relationships'): "cim.1.shared.DocGenealogy.relationships",



    (shared.DocRelationship, 'target'): "cim.1.shared.DocRelationship.target",

    (shared.DocRelationship, 'type'): "cim.1.shared.DocRelationship.type",





    (shared.DataSource, 'purpose'): "cim.1.shared.DataSource.purpose",



    (shared.Machine, 'operating_system'): "cim.1.shared.Machine.operating_system",

    (shared.Machine, 'location'): "cim.1.shared.Machine.location",

    (shared.Machine, 'type'): "cim.1.shared.Machine.type",

    (shared.Machine, 'description'): "cim.1.shared.Machine.description",

    (shared.Machine, 'maximum_processors'): "cim.1.shared.Machine.maximum_processors",

    (shared.Machine, 'vendor'): "cim.1.shared.Machine.vendor",

    (shared.Machine, 'interconnect'): "cim.1.shared.Machine.interconnect",

    (shared.Machine, 'name'): "cim.1.shared.Machine.name",

    (shared.Machine, 'processor_type'): "cim.1.shared.Machine.processor_type",

    (shared.Machine, 'libraries'): "cim.1.shared.Machine.libraries",

    (shared.Machine, 'cores_per_processor'): "cim.1.shared.Machine.cores_per_processor",

    (shared.Machine, 'system'): "cim.1.shared.Machine.system",



    (shared.StandardName, 'is_open'): "cim.1.shared.StandardName.is_open",

    (shared.StandardName, 'value'): "cim.1.shared.StandardName.value",

    (shared.StandardName, 'standards'): "cim.1.shared.StandardName.standards",



    (shared.DocRelationshipTarget, 'reference'): "cim.1.shared.DocRelationshipTarget.reference",



    (shared.MachineCompilerUnit, 'compilers'): "cim.1.shared.MachineCompilerUnit.compilers",

    (shared.MachineCompilerUnit, 'machine'): "cim.1.shared.MachineCompilerUnit.machine",



    (shared.Property, 'name'): "cim.1.shared.Property.name",

    (shared.Property, 'value'): "cim.1.shared.Property.value",



    (shared.ResponsibleParty, 'email'): "cim.1.shared.ResponsibleParty.email",

    (shared.ResponsibleParty, 'individual_name'): "cim.1.shared.ResponsibleParty.individual_name",

    (shared.ResponsibleParty, 'abbreviation'): "cim.1.shared.ResponsibleParty.abbreviation",

    (shared.ResponsibleParty, 'organisation_name'): "cim.1.shared.ResponsibleParty.organisation_name",

    (shared.ResponsibleParty, 'address'): "cim.1.shared.ResponsibleParty.address",

    (shared.ResponsibleParty, 'role'): "cim.1.shared.ResponsibleParty.role",

    (shared.ResponsibleParty, 'url'): "cim.1.shared.ResponsibleParty.url",





    (shared.License, 'is_unrestricted'): "cim.1.shared.License.is_unrestricted",

    (shared.License, 'contact'): "cim.1.shared.License.contact",

    (shared.License, 'name'): "cim.1.shared.License.name",

    (shared.License, 'description'): "cim.1.shared.License.description",



    (shared.Compiler, 'type'): "cim.1.shared.Compiler.type",

    (shared.Compiler, 'language'): "cim.1.shared.Compiler.language",

    (shared.Compiler, 'name'): "cim.1.shared.Compiler.name",

    (shared.Compiler, 'version'): "cim.1.shared.Compiler.version",

    (shared.Compiler, 'options'): "cim.1.shared.Compiler.options",

    (shared.Compiler, 'environment_variables'): "cim.1.shared.Compiler.environment_variables",



    (shared.DateRange, 'duration'): "cim.1.shared.DateRange.duration",





    (grids.GridSpec, 'meta'): "cim.1.grids.GridSpec.meta",

    (grids.GridSpec, 'esm_exchange_grids'): "cim.1.grids.GridSpec.esm_exchange_grids",

    (grids.GridSpec, 'esm_model_grids'): "cim.1.grids.GridSpec.esm_model_grids",



    (grids.SimpleGridGeometry, 'xcoords'): "cim.1.grids.SimpleGridGeometry.xcoords",

    (grids.SimpleGridGeometry, 'is_mesh'): "cim.1.grids.SimpleGridGeometry.is_mesh",

    (grids.SimpleGridGeometry, 'dim_order'): "cim.1.grids.SimpleGridGeometry.dim_order",

    (grids.SimpleGridGeometry, 'zcoords'): "cim.1.grids.SimpleGridGeometry.zcoords",

    (grids.SimpleGridGeometry, 'ycoords'): "cim.1.grids.SimpleGridGeometry.ycoords",

    (grids.SimpleGridGeometry, 'num_dims'): "cim.1.grids.SimpleGridGeometry.num_dims",



    (grids.CoordinateList, 'uom'): "cim.1.grids.CoordinateList.uom",

    (grids.CoordinateList, 'has_constant_offset'): "cim.1.grids.CoordinateList.has_constant_offset",

    (grids.CoordinateList, 'length'): "cim.1.grids.CoordinateList.length",



    (grids.GridTileResolutionType, 'description'): "cim.1.grids.GridTileResolutionType.description",

    (grids.GridTileResolutionType, 'properties'): "cim.1.grids.GridTileResolutionType.properties",



    (grids.GridTile, 'horizontal_resolution'): "cim.1.grids.GridTile.horizontal_resolution",

    (grids.GridTile, 'mnemonic'): "cim.1.grids.GridTile.mnemonic",

    (grids.GridTile, 'short_name'): "cim.1.grids.GridTile.short_name",

    (grids.GridTile, 'id'): "cim.1.grids.GridTile.id",

    (grids.GridTile, 'area'): "cim.1.grids.GridTile.area",

    (grids.GridTile, 'is_conformal'): "cim.1.grids.GridTile.is_conformal",

    (grids.GridTile, 'zcoords'): "cim.1.grids.GridTile.zcoords",

    (grids.GridTile, 'cell_array'): "cim.1.grids.GridTile.cell_array",

    (grids.GridTile, 'is_uniform'): "cim.1.grids.GridTile.is_uniform",

    (grids.GridTile, 'is_terrain_following'): "cim.1.grids.GridTile.is_terrain_following",

    (grids.GridTile, 'coord_file'): "cim.1.grids.GridTile.coord_file",

    (grids.GridTile, 'grid_north_pole'): "cim.1.grids.GridTile.grid_north_pole",

    (grids.GridTile, 'long_name'): "cim.1.grids.GridTile.long_name",

    (grids.GridTile, 'vertical_resolution'): "cim.1.grids.GridTile.vertical_resolution",

    (grids.GridTile, 'horizontal_crs'): "cim.1.grids.GridTile.horizontal_crs",

    (grids.GridTile, 'is_regular'): "cim.1.grids.GridTile.is_regular",

    (grids.GridTile, 'nx'): "cim.1.grids.GridTile.nx",

    (grids.GridTile, 'ny'): "cim.1.grids.GridTile.ny",

    (grids.GridTile, 'coordinate_pole'): "cim.1.grids.GridTile.coordinate_pole",

    (grids.GridTile, 'nz'): "cim.1.grids.GridTile.nz",

    (grids.GridTile, 'vertical_crs'): "cim.1.grids.GridTile.vertical_crs",

    (grids.GridTile, 'refinement_scheme'): "cim.1.grids.GridTile.refinement_scheme",

    (grids.GridTile, 'description'): "cim.1.grids.GridTile.description",

    (grids.GridTile, 'simple_grid_geom'): "cim.1.grids.GridTile.simple_grid_geom",

    (grids.GridTile, 'discretization_type'): "cim.1.grids.GridTile.discretization_type",

    (grids.GridTile, 'extent'): "cim.1.grids.GridTile.extent",

    (grids.GridTile, 'cell_ref_array'): "cim.1.grids.GridTile.cell_ref_array",

    (grids.GridTile, 'geometry_type'): "cim.1.grids.GridTile.geometry_type",



    (grids.GridMosaic, 'tiles'): "cim.1.grids.GridMosaic.tiles",

    (grids.GridMosaic, 'mosaic_count'): "cim.1.grids.GridMosaic.mosaic_count",

    (grids.GridMosaic, 'mnemonic'): "cim.1.grids.GridMosaic.mnemonic",

    (grids.GridMosaic, 'is_leaf'): "cim.1.grids.GridMosaic.is_leaf",

    (grids.GridMosaic, 'mosaics'): "cim.1.grids.GridMosaic.mosaics",

    (grids.GridMosaic, 'extent'): "cim.1.grids.GridMosaic.extent",

    (grids.GridMosaic, 'citations'): "cim.1.grids.GridMosaic.citations",

    (grids.GridMosaic, 'short_name'): "cim.1.grids.GridMosaic.short_name",

    (grids.GridMosaic, 'long_name'): "cim.1.grids.GridMosaic.long_name",

    (grids.GridMosaic, 'has_congruent_tiles'): "cim.1.grids.GridMosaic.has_congruent_tiles",

    (grids.GridMosaic, 'type'): "cim.1.grids.GridMosaic.type",

    (grids.GridMosaic, 'tile_count'): "cim.1.grids.GridMosaic.tile_count",

    (grids.GridMosaic, 'id'): "cim.1.grids.GridMosaic.id",

    (grids.GridMosaic, 'description'): "cim.1.grids.GridMosaic.description",



    (grids.VerticalCoordinateList, 'type'): "cim.1.grids.VerticalCoordinateList.type",

    (grids.VerticalCoordinateList, 'form'): "cim.1.grids.VerticalCoordinateList.form",

    (grids.VerticalCoordinateList, 'properties'): "cim.1.grids.VerticalCoordinateList.properties",





    (grids.GridExtent, 'units'): "cim.1.grids.GridExtent.units",

    (grids.GridExtent, 'maximum_latitude'): "cim.1.grids.GridExtent.maximum_latitude",

    (grids.GridExtent, 'minimum_longitude'): "cim.1.grids.GridExtent.minimum_longitude",

    (grids.GridExtent, 'minimum_latitude'): "cim.1.grids.GridExtent.minimum_latitude",

    (grids.GridExtent, 'maximum_longitude'): "cim.1.grids.GridExtent.maximum_longitude",





    (quality.CimQuality, 'meta'): "cim.1.quality.CimQuality.meta",

    (quality.CimQuality, 'reports'): "cim.1.quality.CimQuality.reports",



    (quality.Measure, 'name'): "cim.1.quality.Measure.name",

    (quality.Measure, 'description'): "cim.1.quality.Measure.description",

    (quality.Measure, 'identification'): "cim.1.quality.Measure.identification",



    (quality.Report, 'date'): "cim.1.quality.Report.date",

    (quality.Report, 'measure'): "cim.1.quality.Report.measure",

    (quality.Report, 'evaluator'): "cim.1.quality.Report.evaluator",

    (quality.Report, 'evaluation'): "cim.1.quality.Report.evaluation",



    (quality.Evaluation, 'did_pass'): "cim.1.quality.Evaluation.did_pass",

    (quality.Evaluation, 'type_hyperlink'): "cim.1.quality.Evaluation.type_hyperlink",

    (quality.Evaluation, 'explanation'): "cim.1.quality.Evaluation.explanation",

    (quality.Evaluation, 'description'): "cim.1.quality.Evaluation.description",

    (quality.Evaluation, 'type'): "cim.1.quality.Evaluation.type",

    (quality.Evaluation, 'specification'): "cim.1.quality.Evaluation.specification",

    (quality.Evaluation, 'title'): "cim.1.quality.Evaluation.title",

    (quality.Evaluation, 'specification_hyperlink'): "cim.1.quality.Evaluation.specification_hyperlink",

    (quality.Evaluation, 'date'): "cim.1.quality.Evaluation.date",





    (misc.DocumentSet, 'meta'): "cim.1.misc.DocumentSet.meta",

    (misc.DocumentSet, 'grids'): "cim.1.misc.DocumentSet.grids",

    (misc.DocumentSet, 'data'): "cim.1.misc.DocumentSet.data",

    (misc.DocumentSet, 'model'): "cim.1.misc.DocumentSet.model",

    (misc.DocumentSet, 'ensembles'): "cim.1.misc.DocumentSet.ensembles",

    (misc.DocumentSet, 'platform'): "cim.1.misc.DocumentSet.platform",

    (misc.DocumentSet, 'experiment'): "cim.1.misc.DocumentSet.experiment",

    (misc.DocumentSet, 'simulation'): "cim.1.misc.DocumentSet.simulation",





    (activity.Simulation, 'deployments'): "cim.1.activity.Simulation.deployments",

    (activity.Simulation, 'outputs'): "cim.1.activity.Simulation.outputs",

    (activity.Simulation, 'simulation_id'): "cim.1.activity.Simulation.simulation_id",

    (activity.Simulation, 'inputs'): "cim.1.activity.Simulation.inputs",

    (activity.Simulation, 'calendar'): "cim.1.activity.Simulation.calendar",

    (activity.Simulation, 'spinup_simulation'): "cim.1.activity.Simulation.spinup_simulation",

    (activity.Simulation, 'control_simulation'): "cim.1.activity.Simulation.control_simulation",

    (activity.Simulation, 'restarts'): "cim.1.activity.Simulation.restarts",

    (activity.Simulation, 'spinup_date_range'): "cim.1.activity.Simulation.spinup_date_range",

    (activity.Simulation, 'conformances'): "cim.1.activity.Simulation.conformances",

    (activity.Simulation, 'authors'): "cim.1.activity.Simulation.authors",



    (activity.SimulationRun, 'date_range'): "cim.1.activity.SimulationRun.date_range",

    (activity.SimulationRun, 'model'): "cim.1.activity.SimulationRun.model",

    (activity.SimulationRun, 'meta'): "cim.1.activity.SimulationRun.meta",





    (activity.Experiment, 'measurement_campaigns'): "cim.1.activity.Experiment.measurement_campaigns",

    (activity.Experiment, 'generates'): "cim.1.activity.Experiment.generates",

    (activity.Experiment, 'supports'): "cim.1.activity.Experiment.supports",

    (activity.Experiment, 'requires'): "cim.1.activity.Experiment.requires",



    (activity.Activity, 'responsible_parties'): "cim.1.activity.Activity.responsible_parties",

    (activity.Activity, 'rationales'): "cim.1.activity.Activity.rationales",

    (activity.Activity, 'funding_sources'): "cim.1.activity.Activity.funding_sources",

    (activity.Activity, 'projects'): "cim.1.activity.Activity.projects",



    (activity.Conformance, 'sources'): "cim.1.activity.Conformance.sources",

    (activity.Conformance, 'frequency'): "cim.1.activity.Conformance.frequency",

    (activity.Conformance, 'type'): "cim.1.activity.Conformance.type",

    (activity.Conformance, 'is_conformant'): "cim.1.activity.Conformance.is_conformant",

    (activity.Conformance, 'requirements'): "cim.1.activity.Conformance.requirements",

    (activity.Conformance, 'description'): "cim.1.activity.Conformance.description",



    (activity.NumericalRequirementOption, 'sub_options'): "cim.1.activity.NumericalRequirementOption.sub_options",

    (activity.NumericalRequirementOption, 'description'): "cim.1.activity.NumericalRequirementOption.description",

    (activity.NumericalRequirementOption, 'name'): "cim.1.activity.NumericalRequirementOption.name",

    (activity.NumericalRequirementOption, 'relationship'): "cim.1.activity.NumericalRequirementOption.relationship",

    (activity.NumericalRequirementOption, 'id'): "cim.1.activity.NumericalRequirementOption.id",





    (activity.NumericalActivity, 'short_name'): "cim.1.activity.NumericalActivity.short_name",

    (activity.NumericalActivity, 'description'): "cim.1.activity.NumericalActivity.description",

    (activity.NumericalActivity, 'supports'): "cim.1.activity.NumericalActivity.supports",

    (activity.NumericalActivity, 'long_name'): "cim.1.activity.NumericalActivity.long_name",



    (activity.SimulationRelationship, 'target'): "cim.1.activity.SimulationRelationship.target",

    (activity.SimulationRelationship, 'type'): "cim.1.activity.SimulationRelationship.type",





    (activity.ExperimentRelationship, 'target'): "cim.1.activity.ExperimentRelationship.target",

    (activity.ExperimentRelationship, 'type'): "cim.1.activity.ExperimentRelationship.type",



    (activity.EnsembleMember, 'ensemble'): "cim.1.activity.EnsembleMember.ensemble",

    (activity.EnsembleMember, 'simulation'): "cim.1.activity.EnsembleMember.simulation",

    (activity.EnsembleMember, 'ensemble_ids'): "cim.1.activity.EnsembleMember.ensemble_ids",



    (activity.MeasurementCampaign, 'duration'): "cim.1.activity.MeasurementCampaign.duration",



    (activity.DownscalingSimulation, 'downscaling_id'): "cim.1.activity.DownscalingSimulation.downscaling_id",

    (activity.DownscalingSimulation, 'inputs'): "cim.1.activity.DownscalingSimulation.inputs",

    (activity.DownscalingSimulation, 'calendar'): "cim.1.activity.DownscalingSimulation.calendar",

    (activity.DownscalingSimulation, 'downscaling_type'): "cim.1.activity.DownscalingSimulation.downscaling_type",

    (activity.DownscalingSimulation, 'downscaled_from'): "cim.1.activity.DownscalingSimulation.downscaled_from",

    (activity.DownscalingSimulation, 'outputs'): "cim.1.activity.DownscalingSimulation.outputs",

    (activity.DownscalingSimulation, 'meta'): "cim.1.activity.DownscalingSimulation.meta",



    (activity.NumericalExperiment, 'experiment_id'): "cim.1.activity.NumericalExperiment.experiment_id",

    (activity.NumericalExperiment, 'meta'): "cim.1.activity.NumericalExperiment.meta",

    (activity.NumericalExperiment, 'long_name'): "cim.1.activity.NumericalExperiment.long_name",

    (activity.NumericalExperiment, 'requirements'): "cim.1.activity.NumericalExperiment.requirements",

    (activity.NumericalExperiment, 'description'): "cim.1.activity.NumericalExperiment.description",

    (activity.NumericalExperiment, 'short_name'): "cim.1.activity.NumericalExperiment.short_name",





    (activity.SimulationRelationshipTarget, 'simulation'): "cim.1.activity.SimulationRelationshipTarget.simulation",

    (activity.SimulationRelationshipTarget, 'target'): "cim.1.activity.SimulationRelationshipTarget.target",



    (activity.Ensemble, 'types'): "cim.1.activity.Ensemble.types",

    (activity.Ensemble, 'outputs'): "cim.1.activity.Ensemble.outputs",

    (activity.Ensemble, 'members'): "cim.1.activity.Ensemble.members",

    (activity.Ensemble, 'meta'): "cim.1.activity.Ensemble.meta",



    (activity.ExperimentRelationshipTarget, 'numerical_experiment'): "cim.1.activity.ExperimentRelationshipTarget.numerical_experiment",



    (activity.NumericalRequirement, 'requirement_type'): "cim.1.activity.NumericalRequirement.requirement_type",

    (activity.NumericalRequirement, 'source'): "cim.1.activity.NumericalRequirement.source",

    (activity.NumericalRequirement, 'id'): "cim.1.activity.NumericalRequirement.id",

    (activity.NumericalRequirement, 'name'): "cim.1.activity.NumericalRequirement.name",

    (activity.NumericalRequirement, 'options'): "cim.1.activity.NumericalRequirement.options",

    (activity.NumericalRequirement, 'description'): "cim.1.activity.NumericalRequirement.description",



    (activity.SpatioTemporalConstraint, 'date_range'): "cim.1.activity.SpatioTemporalConstraint.date_range",

    (activity.SpatioTemporalConstraint, 'spatial_resolution'): "cim.1.activity.SpatioTemporalConstraint.spatial_resolution",





    (activity.SimulationComposite, 'rank'): "cim.1.activity.SimulationComposite.rank",

    (activity.SimulationComposite, 'child'): "cim.1.activity.SimulationComposite.child",

    (activity.SimulationComposite, 'meta'): "cim.1.activity.SimulationComposite.meta",

    (activity.SimulationComposite, 'date_range'): "cim.1.activity.SimulationComposite.date_range",



    # ------------------------------------------------
    # Enums.
    # ------------------------------------------------


    data.DataHierarchyType: "cim.1.data.DataHierarchyType",

    data.DataStatusType: "cim.1.data.DataStatusType",



    software.ModelComponentType: "cim.1.software.ModelComponentType",

    software.CouplingFrameworkType: "cim.1.software.CouplingFrameworkType",

    software.SpatialRegriddingDimensionType: "cim.1.software.SpatialRegriddingDimensionType",

    software.ConnectionType: "cim.1.software.ConnectionType",

    software.SpatialRegriddingStandardMethodType: "cim.1.software.SpatialRegriddingStandardMethodType",

    software.TimeMappingType: "cim.1.software.TimeMappingType",

    software.TimingUnits: "cim.1.software.TimingUnits",

    software.StatisticalModelComponentType: "cim.1.software.StatisticalModelComponentType",

    software.ComponentPropertyIntentType: "cim.1.software.ComponentPropertyIntentType",



    shared.DataPurpose: "cim.1.shared.DataPurpose",

    shared.ProcessorType: "cim.1.shared.ProcessorType",

    shared.CompilerType: "cim.1.shared.CompilerType",

    shared.InterconnectType: "cim.1.shared.InterconnectType",

    shared.DocRelationshipType: "cim.1.shared.DocRelationshipType",

    shared.UnitType: "cim.1.shared.UnitType",

    shared.MachineVendorType: "cim.1.shared.MachineVendorType",

    shared.ChangePropertyType: "cim.1.shared.ChangePropertyType",

    shared.DocStatusType: "cim.1.shared.DocStatusType",

    shared.OperatingSystemType: "cim.1.shared.OperatingSystemType",

    shared.DocType: "cim.1.shared.DocType",

    shared.DocRelationshipDirectionType: "cim.1.shared.DocRelationshipDirectionType",

    shared.MachineType: "cim.1.shared.MachineType",



    grids.RefinementTypeEnum: "cim.1.grids.RefinementTypeEnum",

    grids.FeatureTypeEnum: "cim.1.grids.FeatureTypeEnum",

    grids.GridNodePositionEnum: "cim.1.grids.GridNodePositionEnum",

    grids.ArcTypeEnum: "cim.1.grids.ArcTypeEnum",

    grids.VerticalCsEnum: "cim.1.grids.VerticalCsEnum",

    grids.HorizontalCsEnum: "cim.1.grids.HorizontalCsEnum",

    grids.DiscretizationEnum: "cim.1.grids.DiscretizationEnum",

    grids.GridTypeEnum: "cim.1.grids.GridTypeEnum",

    grids.GeometryTypeEnum: "cim.1.grids.GeometryTypeEnum",



    quality.QualityStatusType: "cim.1.quality.QualityStatusType",

    quality.CimScopeCodeType: "cim.1.quality.CimScopeCodeType",

    quality.QualityIssueType: "cim.1.quality.QualityIssueType",

    quality.CimResultType: "cim.1.quality.CimResultType",

    quality.QualitySeverityType: "cim.1.quality.QualitySeverityType",

    quality.CimFeatureType: "cim.1.quality.CimFeatureType",





    activity.ProjectType: "cim.1.activity.ProjectType",

    activity.EnsembleType: "cim.1.activity.EnsembleType",

    activity.ExperimentRelationshipType: "cim.1.activity.ExperimentRelationshipType",

    activity.SimulationType: "cim.1.activity.SimulationType",

    activity.FrequencyType: "cim.1.activity.FrequencyType",

    activity.SimulationRelationshipType: "cim.1.activity.SimulationRelationshipType",

    activity.DownscalingType: "cim.1.activity.DownscalingType",

    activity.ConformanceType: "cim.1.activity.ConformanceType",

    activity.ResolutionType: "cim.1.activity.ResolutionType",


    # ------------------------------------------------
    # Enum members.
    # ------------------------------------------------





    (data.DataStatusType, 'complete'): "cim.1.data.DataStatusType.complete",

    (data.DataStatusType, 'metadataOnly'): "cim.1.data.DataStatusType.metadataOnly",

    (data.DataStatusType, 'continuouslySupplemented'): "cim.1.data.DataStatusType.continuouslySupplemented",







    (software.CouplingFrameworkType, 'ESMF'): "cim.1.software.CouplingFrameworkType.ESMF",

    (software.CouplingFrameworkType, 'BFG'): "cim.1.software.CouplingFrameworkType.BFG",

    (software.CouplingFrameworkType, 'OASIS'): "cim.1.software.CouplingFrameworkType.OASIS",



    (software.SpatialRegriddingDimensionType, '2D'): "cim.1.software.SpatialRegriddingDimensionType.2D",

    (software.SpatialRegriddingDimensionType, '1D'): "cim.1.software.SpatialRegriddingDimensionType.1D",

    (software.SpatialRegriddingDimensionType, '3D'): "cim.1.software.SpatialRegriddingDimensionType.3D",





    (software.SpatialRegriddingStandardMethodType, 'conservative-first-order'): "cim.1.software.SpatialRegriddingStandardMethodType.conservative-first-order",

    (software.SpatialRegriddingStandardMethodType, 'conservative-second-order'): "cim.1.software.SpatialRegriddingStandardMethodType.conservative-second-order",

    (software.SpatialRegriddingStandardMethodType, 'conservative'): "cim.1.software.SpatialRegriddingStandardMethodType.conservative",

    (software.SpatialRegriddingStandardMethodType, 'non-conservative'): "cim.1.software.SpatialRegriddingStandardMethodType.non-conservative",

    (software.SpatialRegriddingStandardMethodType, 'linear'): "cim.1.software.SpatialRegriddingStandardMethodType.linear",

    (software.SpatialRegriddingStandardMethodType, 'near-neighbour'): "cim.1.software.SpatialRegriddingStandardMethodType.near-neighbour",

    (software.SpatialRegriddingStandardMethodType, 'cubic'): "cim.1.software.SpatialRegriddingStandardMethodType.cubic",





    (software.TimingUnits, 'minutes'): "cim.1.software.TimingUnits.minutes",

    (software.TimingUnits, 'hours'): "cim.1.software.TimingUnits.hours",

    (software.TimingUnits, 'days'): "cim.1.software.TimingUnits.days",

    (software.TimingUnits, 'months'): "cim.1.software.TimingUnits.months",

    (software.TimingUnits, 'years'): "cim.1.software.TimingUnits.years",

    (software.TimingUnits, 'decades'): "cim.1.software.TimingUnits.decades",

    (software.TimingUnits, 'centuries'): "cim.1.software.TimingUnits.centuries",

    (software.TimingUnits, 'seconds'): "cim.1.software.TimingUnits.seconds",





    (software.ComponentPropertyIntentType, 'in'): "cim.1.software.ComponentPropertyIntentType.in",

    (software.ComponentPropertyIntentType, 'out'): "cim.1.software.ComponentPropertyIntentType.out",

    (software.ComponentPropertyIntentType, 'inout'): "cim.1.software.ComponentPropertyIntentType.inout",





    (shared.DataPurpose, 'boundaryCondition'): "cim.1.shared.DataPurpose.boundaryCondition",

    (shared.DataPurpose, 'ancillaryFile'): "cim.1.shared.DataPurpose.ancillaryFile",

    (shared.DataPurpose, 'initialCondition'): "cim.1.shared.DataPurpose.initialCondition",









    (shared.DocRelationshipType, 'previousVersionOf'): "cim.1.shared.DocRelationshipType.previousVersionOf",

    (shared.DocRelationshipType, 'other'): "cim.1.shared.DocRelationshipType.other",

    (shared.DocRelationshipType, 'fixedVersionOf'): "cim.1.shared.DocRelationshipType.fixedVersionOf",

    (shared.DocRelationshipType, 'similarTo'): "cim.1.shared.DocRelationshipType.similarTo",

    (shared.DocRelationshipType, 'laterVersionOf'): "cim.1.shared.DocRelationshipType.laterVersionOf",







    (shared.ChangePropertyType, 'Unused'): "cim.1.shared.ChangePropertyType.Unused",

    (shared.ChangePropertyType, 'Redistribution'): "cim.1.shared.ChangePropertyType.Redistribution",

    (shared.ChangePropertyType, 'InputMod'): "cim.1.shared.ChangePropertyType.InputMod",

    (shared.ChangePropertyType, 'Replacement'): "cim.1.shared.ChangePropertyType.Replacement",

    (shared.ChangePropertyType, 'ParameterChange'): "cim.1.shared.ChangePropertyType.ParameterChange",

    (shared.ChangePropertyType, 'Increment'): "cim.1.shared.ChangePropertyType.Increment",

    (shared.ChangePropertyType, 'CodeChange'): "cim.1.shared.ChangePropertyType.CodeChange",

    (shared.ChangePropertyType, 'AncillaryFile'): "cim.1.shared.ChangePropertyType.AncillaryFile",

    (shared.ChangePropertyType, 'Decrement'): "cim.1.shared.ChangePropertyType.Decrement",

    (shared.ChangePropertyType, 'BoundaryCondition'): "cim.1.shared.ChangePropertyType.BoundaryCondition",

    (shared.ChangePropertyType, 'InitialCondition'): "cim.1.shared.ChangePropertyType.InitialCondition",

    (shared.ChangePropertyType, 'ModelMod'): "cim.1.shared.ChangePropertyType.ModelMod",



    (shared.DocStatusType, 'incomplete'): "cim.1.shared.DocStatusType.incomplete",

    (shared.DocStatusType, 'complete'): "cim.1.shared.DocStatusType.complete",

    (shared.DocStatusType, 'in-progress'): "cim.1.shared.DocStatusType.in-progress",





    (shared.DocType, 'modelComponent'): "cim.1.shared.DocType.modelComponent",

    (shared.DocType, 'dataProcessing'): "cim.1.shared.DocType.dataProcessing",

    (shared.DocType, 'numericalExperiment'): "cim.1.shared.DocType.numericalExperiment",

    (shared.DocType, 'ensemble'): "cim.1.shared.DocType.ensemble",

    (shared.DocType, 'downscalingSimulation'): "cim.1.shared.DocType.downscalingSimulation",

    (shared.DocType, 'dataObject'): "cim.1.shared.DocType.dataObject",

    (shared.DocType, 'gridSpec'): "cim.1.shared.DocType.gridSpec",

    (shared.DocType, 'statisticalModelComponent'): "cim.1.shared.DocType.statisticalModelComponent",

    (shared.DocType, 'cimQuality'): "cim.1.shared.DocType.cimQuality",

    (shared.DocType, 'platform'): "cim.1.shared.DocType.platform",

    (shared.DocType, 'assimilation'): "cim.1.shared.DocType.assimilation",

    (shared.DocType, 'simulationComposite'): "cim.1.shared.DocType.simulationComposite",

    (shared.DocType, 'processorComponent'): "cim.1.shared.DocType.processorComponent",

    (shared.DocType, 'simulationRun'): "cim.1.shared.DocType.simulationRun",



    (shared.DocRelationshipDirectionType, 'fromTarget'): "cim.1.shared.DocRelationshipDirectionType.fromTarget",

    (shared.DocRelationshipDirectionType, 'toTarget'): "cim.1.shared.DocRelationshipDirectionType.toTarget",



    (shared.MachineType, 'Beowulf'): "cim.1.shared.MachineType.Beowulf",

    (shared.MachineType, 'Vector'): "cim.1.shared.MachineType.Vector",

    (shared.MachineType, 'Parallel'): "cim.1.shared.MachineType.Parallel",





    (grids.RefinementTypeEnum, 'none'): "cim.1.grids.RefinementTypeEnum.none",

    (grids.RefinementTypeEnum, 'integer'): "cim.1.grids.RefinementTypeEnum.integer",

    (grids.RefinementTypeEnum, 'rational'): "cim.1.grids.RefinementTypeEnum.rational",



    (grids.FeatureTypeEnum, 'edge'): "cim.1.grids.FeatureTypeEnum.edge",

    (grids.FeatureTypeEnum, 'point'): "cim.1.grids.FeatureTypeEnum.point",



    (grids.GridNodePositionEnum, 'centre'): "cim.1.grids.GridNodePositionEnum.centre",

    (grids.GridNodePositionEnum, 'plane'): "cim.1.grids.GridNodePositionEnum.plane",

    (grids.GridNodePositionEnum, 'sphere'): "cim.1.grids.GridNodePositionEnum.sphere",



    (grids.ArcTypeEnum, 'geodesic'): "cim.1.grids.ArcTypeEnum.geodesic",

    (grids.ArcTypeEnum, 'small_circle'): "cim.1.grids.ArcTypeEnum.small_circle",

    (grids.ArcTypeEnum, 'complex'): "cim.1.grids.ArcTypeEnum.complex",

    (grids.ArcTypeEnum, 'great_circle'): "cim.1.grids.ArcTypeEnum.great_circle",



    (grids.VerticalCsEnum, 'space-based'): "cim.1.grids.VerticalCsEnum.space-based",

    (grids.VerticalCsEnum, 'mass-based'): "cim.1.grids.VerticalCsEnum.mass-based",



    (grids.HorizontalCsEnum, 'cartesian'): "cim.1.grids.HorizontalCsEnum.cartesian",

    (grids.HorizontalCsEnum, 'spherical'): "cim.1.grids.HorizontalCsEnum.spherical",

    (grids.HorizontalCsEnum, 'ellipsoidal'): "cim.1.grids.HorizontalCsEnum.ellipsoidal",

    (grids.HorizontalCsEnum, 'polar'): "cim.1.grids.HorizontalCsEnum.polar",



    (grids.DiscretizationEnum, 'unstructured_polygonal'): "cim.1.grids.DiscretizationEnum.unstructured_polygonal",

    (grids.DiscretizationEnum, 'spherical_harmonics'): "cim.1.grids.DiscretizationEnum.spherical_harmonics",

    (grids.DiscretizationEnum, 'other'): "cim.1.grids.DiscretizationEnum.other",

    (grids.DiscretizationEnum, 'logically_rectangular'): "cim.1.grids.DiscretizationEnum.logically_rectangular",

    (grids.DiscretizationEnum, 'structured_triangular'): "cim.1.grids.DiscretizationEnum.structured_triangular",

    (grids.DiscretizationEnum, 'unstructured_triangular'): "cim.1.grids.DiscretizationEnum.unstructured_triangular",

    (grids.DiscretizationEnum, 'pixel-based_catchment'): "cim.1.grids.DiscretizationEnum.pixel-based_catchment",



    (grids.GridTypeEnum, 'cubed_sphere'): "cim.1.grids.GridTypeEnum.cubed_sphere",

    (grids.GridTypeEnum, 'composite'): "cim.1.grids.GridTypeEnum.composite",

    (grids.GridTypeEnum, 'icosahedral_geodesic'): "cim.1.grids.GridTypeEnum.icosahedral_geodesic",

    (grids.GridTypeEnum, 'reduced_gaussian'): "cim.1.grids.GridTypeEnum.reduced_gaussian",

    (grids.GridTypeEnum, 'regular_lat_lon'): "cim.1.grids.GridTypeEnum.regular_lat_lon",

    (grids.GridTypeEnum, 'spectral_gaussian'): "cim.1.grids.GridTypeEnum.spectral_gaussian",

    (grids.GridTypeEnum, 'other'): "cim.1.grids.GridTypeEnum.other",

    (grids.GridTypeEnum, 'tripolar'): "cim.1.grids.GridTypeEnum.tripolar",

    (grids.GridTypeEnum, 'yin_yang'): "cim.1.grids.GridTypeEnum.yin_yang",

    (grids.GridTypeEnum, 'displaced_pole'): "cim.1.grids.GridTypeEnum.displaced_pole",



    (grids.GeometryTypeEnum, 'ellipsoid'): "cim.1.grids.GeometryTypeEnum.ellipsoid",

    (grids.GeometryTypeEnum, 'plane'): "cim.1.grids.GeometryTypeEnum.plane",

    (grids.GeometryTypeEnum, 'sphere'): "cim.1.grids.GeometryTypeEnum.sphere",





    (quality.QualityStatusType, 'partially_resolved'): "cim.1.quality.QualityStatusType.partially_resolved",

    (quality.QualityStatusType, 'confirmed'): "cim.1.quality.QualityStatusType.confirmed",

    (quality.QualityStatusType, 'resolved'): "cim.1.quality.QualityStatusType.resolved",

    (quality.QualityStatusType, 'reported'): "cim.1.quality.QualityStatusType.reported",



    (quality.CimScopeCodeType, 'simulation'): "cim.1.quality.CimScopeCodeType.simulation",

    (quality.CimScopeCodeType, 'experiment'): "cim.1.quality.CimScopeCodeType.experiment",

    (quality.CimScopeCodeType, 'software'): "cim.1.quality.CimScopeCodeType.software",

    (quality.CimScopeCodeType, 'numericalRequirement'): "cim.1.quality.CimScopeCodeType.numericalRequirement",

    (quality.CimScopeCodeType, 'dataset'): "cim.1.quality.CimScopeCodeType.dataset",

    (quality.CimScopeCodeType, 'ensemble'): "cim.1.quality.CimScopeCodeType.ensemble",

    (quality.CimScopeCodeType, 'file'): "cim.1.quality.CimScopeCodeType.file",

    (quality.CimScopeCodeType, 'service'): "cim.1.quality.CimScopeCodeType.service",

    (quality.CimScopeCodeType, 'model'): "cim.1.quality.CimScopeCodeType.model",

    (quality.CimScopeCodeType, 'modelComponent'): "cim.1.quality.CimScopeCodeType.modelComponent",



    (quality.QualityIssueType, 'data_format'): "cim.1.quality.QualityIssueType.data_format",

    (quality.QualityIssueType, 'science'): "cim.1.quality.QualityIssueType.science",

    (quality.QualityIssueType, 'metadata'): "cim.1.quality.QualityIssueType.metadata",

    (quality.QualityIssueType, 'data_content'): "cim.1.quality.QualityIssueType.data_content",

    (quality.QualityIssueType, 'data_indexing'): "cim.1.quality.QualityIssueType.data_indexing",



    (quality.CimResultType, 'document'): "cim.1.quality.CimResultType.document",

    (quality.CimResultType, 'logfile'): "cim.1.quality.CimResultType.logfile",

    (quality.CimResultType, 'plot'): "cim.1.quality.CimResultType.plot",



    (quality.QualitySeverityType, 'minor'): "cim.1.quality.QualitySeverityType.minor",

    (quality.QualitySeverityType, 'cosmetic'): "cim.1.quality.QualitySeverityType.cosmetic",

    (quality.QualitySeverityType, 'major'): "cim.1.quality.QualitySeverityType.major",



    (quality.CimFeatureType, 'diagnostic'): "cim.1.quality.CimFeatureType.diagnostic",

    (quality.CimFeatureType, 'file'): "cim.1.quality.CimFeatureType.file",











    (activity.ExperimentRelationshipType, 'increaseEnsembleOf'): "cim.1.activity.ExperimentRelationshipType.increaseEnsembleOf",

    (activity.ExperimentRelationshipType, 'modifiedInputMethodOf'): "cim.1.activity.ExperimentRelationshipType.modifiedInputMethodOf",

    (activity.ExperimentRelationshipType, 'shorterVersionOf'): "cim.1.activity.ExperimentRelationshipType.shorterVersionOf",

    (activity.ExperimentRelationshipType, 'extensionOf'): "cim.1.activity.ExperimentRelationshipType.extensionOf",

    (activity.ExperimentRelationshipType, 'previousRealisation'): "cim.1.activity.ExperimentRelationshipType.previousRealisation",

    (activity.ExperimentRelationshipType, 'continuationOf'): "cim.1.activity.ExperimentRelationshipType.continuationOf",

    (activity.ExperimentRelationshipType, 'controlExperiment'): "cim.1.activity.ExperimentRelationshipType.controlExperiment",

    (activity.ExperimentRelationshipType, 'higherResolutionVersionOf'): "cim.1.activity.ExperimentRelationshipType.higherResolutionVersionOf",

    (activity.ExperimentRelationshipType, 'lowerResolutionVersionOf'): "cim.1.activity.ExperimentRelationshipType.lowerResolutionVersionOf",



    (activity.SimulationType, 'simulationComposite'): "cim.1.activity.SimulationType.simulationComposite",

    (activity.SimulationType, 'assimilation'): "cim.1.activity.SimulationType.assimilation",

    (activity.SimulationType, 'simulationRun'): "cim.1.activity.SimulationType.simulationRun",





    (activity.SimulationRelationshipType, 'lowerResolutionVersionOf'): "cim.1.activity.SimulationRelationshipType.lowerResolutionVersionOf",

    (activity.SimulationRelationshipType, 'fixedVersionOf'): "cim.1.activity.SimulationRelationshipType.fixedVersionOf",

    (activity.SimulationRelationshipType, 'followingSimulation'): "cim.1.activity.SimulationRelationshipType.followingSimulation",

    (activity.SimulationRelationshipType, 'extensionOf'): "cim.1.activity.SimulationRelationshipType.extensionOf",

    (activity.SimulationRelationshipType, 'responseTo'): "cim.1.activity.SimulationRelationshipType.responseTo",

    (activity.SimulationRelationshipType, 'continuationOf'): "cim.1.activity.SimulationRelationshipType.continuationOf",

    (activity.SimulationRelationshipType, 'previousSimulation'): "cim.1.activity.SimulationRelationshipType.previousSimulation",

    (activity.SimulationRelationshipType, 'higherResolutionVersionOf'): "cim.1.activity.SimulationRelationshipType.higherResolutionVersionOf",



    (activity.DownscalingType, 'dynamic'): "cim.1.activity.DownscalingType.dynamic",

    (activity.DownscalingType, 'statistical'): "cim.1.activity.DownscalingType.statistical",



    (activity.ConformanceType, 'not-xxx'): "cim.1.activity.ConformanceType.not-xxx",

    (activity.ConformanceType, 'not conformant'): "cim.1.activity.ConformanceType.not-conformant",

    (activity.ConformanceType, 'standard config'): "cim.1.activity.ConformanceType.standard-config",

    (activity.ConformanceType, 'via inputs'): "cim.1.activity.ConformanceType.via-inputs",

    (activity.ConformanceType, 'via model mods'): "cim.1.activity.ConformanceType.via-model-mods",

    (activity.ConformanceType, 'combination'): "cim.1.activity.ConformanceType.combination",





}