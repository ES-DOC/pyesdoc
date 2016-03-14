
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.type_keys.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The ontology map of types to keys.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import typeset_for_shared_package as shared
import typeset_for_software_package as software
import typeset_for_grids_package as grids
import typeset_for_quality_package as quality
import typeset_for_data_package as data
import typeset_for_activity_package as activity
import typeset_for_misc_package as misc




# Map of ontology types to type keys.
KEYS = {
    # ------------------------------------------------
    # Packages.
    # ------------------------------------------------

    shared: "cim.1.shared",
    software: "cim.1.software",
    grids: "cim.1.grids",
    quality: "cim.1.quality",
    data: "cim.1.data",
    activity: "cim.1.activity",
    misc: "cim.1.misc",

    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    shared.StandardName: "cim.1.shared.StandardName",

    shared.Change: "cim.1.shared.Change",

    shared.ChangeProperty: "cim.1.shared.ChangeProperty",

    shared.DataSource: "cim.1.shared.DataSource",

    shared.Daily360: "cim.1.shared.Daily360",

    shared.ResponsibleParty: "cim.1.shared.ResponsibleParty",

    shared.DocGenealogy: "cim.1.shared.DocGenealogy",

    shared.MachineCompilerUnit: "cim.1.shared.MachineCompilerUnit",

    shared.DateRange: "cim.1.shared.DateRange",

    shared.Compiler: "cim.1.shared.Compiler",

    shared.License: "cim.1.shared.License",

    shared.DocReference: "cim.1.shared.DocReference",

    shared.DocMetaInfo: "cim.1.shared.DocMetaInfo",

    shared.Standard: "cim.1.shared.Standard",

    shared.Calendar: "cim.1.shared.Calendar",

    shared.Citation: "cim.1.shared.Citation",

    shared.DocRelationshipTarget: "cim.1.shared.DocRelationshipTarget",

    shared.OpenDateRange: "cim.1.shared.OpenDateRange",

    shared.PerpetualPeriod: "cim.1.shared.PerpetualPeriod",

    shared.Platform: "cim.1.shared.Platform",

    shared.DocRelationship: "cim.1.shared.DocRelationship",

    shared.Property: "cim.1.shared.Property",

    shared.Relationship: "cim.1.shared.Relationship",

    shared.ClosedDateRange: "cim.1.shared.ClosedDateRange",

    shared.RealCalendar: "cim.1.shared.RealCalendar",

    shared.Machine: "cim.1.shared.Machine",

    software.Connection: "cim.1.software.Connection",

    software.ConnectionEndpoint: "cim.1.software.ConnectionEndpoint",

    software.SpatialRegriddingUserMethod: "cim.1.software.SpatialRegriddingUserMethod",

    software.EntryPoint: "cim.1.software.EntryPoint",

    software.ConnectionProperty: "cim.1.software.ConnectionProperty",

    software.Timing: "cim.1.software.Timing",

    software.ComponentLanguageProperty: "cim.1.software.ComponentLanguageProperty",

    software.SpatialRegriddingProperty: "cim.1.software.SpatialRegriddingProperty",

    software.Parallelisation: "cim.1.software.Parallelisation",

    software.CouplingEndpoint: "cim.1.software.CouplingEndpoint",

    software.ComponentLanguage: "cim.1.software.ComponentLanguage",

    software.CouplingProperty: "cim.1.software.CouplingProperty",

    software.Component: "cim.1.software.Component",

    software.StatisticalModelComponent: "cim.1.software.StatisticalModelComponent",

    software.TimeTransformation: "cim.1.software.TimeTransformation",

    software.ProcessorComponent: "cim.1.software.ProcessorComponent",

    software.SpatialRegridding: "cim.1.software.SpatialRegridding",

    software.TimeLag: "cim.1.software.TimeLag",

    software.ComponentProperty: "cim.1.software.ComponentProperty",

    software.Coupling: "cim.1.software.Coupling",

    software.Deployment: "cim.1.software.Deployment",

    software.Composition: "cim.1.software.Composition",

    software.Rank: "cim.1.software.Rank",

    software.ModelComponent: "cim.1.software.ModelComponent",

    grids.GridTileResolutionType: "cim.1.grids.GridTileResolutionType",

    grids.GridMosaic: "cim.1.grids.GridMosaic",

    grids.VerticalCoordinateList: "cim.1.grids.VerticalCoordinateList",

    grids.GridSpec: "cim.1.grids.GridSpec",

    grids.GridExtent: "cim.1.grids.GridExtent",

    grids.CoordinateList: "cim.1.grids.CoordinateList",

    grids.GridTile: "cim.1.grids.GridTile",

    grids.GridProperty: "cim.1.grids.GridProperty",

    grids.SimpleGridGeometry: "cim.1.grids.SimpleGridGeometry",

    quality.CimQuality: "cim.1.quality.CimQuality",

    quality.Report: "cim.1.quality.Report",

    quality.Evaluation: "cim.1.quality.Evaluation",

    quality.Measure: "cim.1.quality.Measure",

    data.DataTopic: "cim.1.data.DataTopic",

    data.DataExtent: "cim.1.data.DataExtent",

    data.DataObject: "cim.1.data.DataObject",

    data.DataHierarchyLevel: "cim.1.data.DataHierarchyLevel",

    data.DataStorage: "cim.1.data.DataStorage",

    data.DataExtentGeographical: "cim.1.data.DataExtentGeographical",

    data.DataProperty: "cim.1.data.DataProperty",

    data.DataStorageFile: "cim.1.data.DataStorageFile",

    data.DataContent: "cim.1.data.DataContent",

    data.DataDistribution: "cim.1.data.DataDistribution",

    data.DataRestriction: "cim.1.data.DataRestriction",

    data.DataExtentTimeInterval: "cim.1.data.DataExtentTimeInterval",

    data.DataStorageIp: "cim.1.data.DataStorageIp",

    data.DataExtentTemporal: "cim.1.data.DataExtentTemporal",

    data.DataStorageDb: "cim.1.data.DataStorageDb",

    activity.Simulation: "cim.1.activity.Simulation",

    activity.Activity: "cim.1.activity.Activity",

    activity.NumericalRequirementOption: "cim.1.activity.NumericalRequirementOption",

    activity.SimulationRun: "cim.1.activity.SimulationRun",

    activity.SimulationRelationshipTarget: "cim.1.activity.SimulationRelationshipTarget",

    activity.ExperimentRelationship: "cim.1.activity.ExperimentRelationship",

    activity.SimulationComposite: "cim.1.activity.SimulationComposite",

    activity.BoundaryCondition: "cim.1.activity.BoundaryCondition",

    activity.NumericalActivity: "cim.1.activity.NumericalActivity",

    activity.ExperimentRelationshipTarget: "cim.1.activity.ExperimentRelationshipTarget",

    activity.EnsembleMember: "cim.1.activity.EnsembleMember",

    activity.DownscalingSimulation: "cim.1.activity.DownscalingSimulation",

    activity.NumericalExperiment: "cim.1.activity.NumericalExperiment",

    activity.Experiment: "cim.1.activity.Experiment",

    activity.SpatioTemporalConstraint: "cim.1.activity.SpatioTemporalConstraint",

    activity.OutputRequirement: "cim.1.activity.OutputRequirement",

    activity.Conformance: "cim.1.activity.Conformance",

    activity.MeasurementCampaign: "cim.1.activity.MeasurementCampaign",

    activity.Ensemble: "cim.1.activity.Ensemble",

    activity.PhysicalModification: "cim.1.activity.PhysicalModification",

    activity.InitialCondition: "cim.1.activity.InitialCondition",

    activity.SimulationRelationship: "cim.1.activity.SimulationRelationship",

    activity.NumericalRequirement: "cim.1.activity.NumericalRequirement",

    activity.LateralBoundaryCondition: "cim.1.activity.LateralBoundaryCondition",

    misc.DocumentSet: "cim.1.misc.DocumentSet",

    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------

    (shared.StandardName, 'is_open'): "cim.1.shared.StandardName.is_open",

    (shared.StandardName, 'value'): "cim.1.shared.StandardName.value",

    (shared.StandardName, 'standards'): "cim.1.shared.StandardName.standards",

    (shared.Change, 'details'): "cim.1.shared.Change.details",

    (shared.Change, 'name'): "cim.1.shared.Change.name",

    (shared.Change, 'author'): "cim.1.shared.Change.author",

    (shared.Change, 'type'): "cim.1.shared.Change.type",

    (shared.Change, 'description'): "cim.1.shared.Change.description",

    (shared.Change, 'date'): "cim.1.shared.Change.date",

    (shared.ChangeProperty, 'description'): "cim.1.shared.ChangeProperty.description",

    (shared.ChangeProperty, 'id'): "cim.1.shared.ChangeProperty.id",

    (shared.DataSource, 'purpose'): "cim.1.shared.DataSource.purpose",

    (shared.ResponsibleParty, 'role'): "cim.1.shared.ResponsibleParty.role",

    (shared.ResponsibleParty, 'url'): "cim.1.shared.ResponsibleParty.url",

    (shared.ResponsibleParty, 'email'): "cim.1.shared.ResponsibleParty.email",

    (shared.ResponsibleParty, 'abbreviation'): "cim.1.shared.ResponsibleParty.abbreviation",

    (shared.ResponsibleParty, 'individual_name'): "cim.1.shared.ResponsibleParty.individual_name",

    (shared.ResponsibleParty, 'organisation_name'): "cim.1.shared.ResponsibleParty.organisation_name",

    (shared.ResponsibleParty, 'address'): "cim.1.shared.ResponsibleParty.address",

    (shared.DocGenealogy, 'relationships'): "cim.1.shared.DocGenealogy.relationships",

    (shared.MachineCompilerUnit, 'compilers'): "cim.1.shared.MachineCompilerUnit.compilers",

    (shared.MachineCompilerUnit, 'machine'): "cim.1.shared.MachineCompilerUnit.machine",

    (shared.DateRange, 'duration'): "cim.1.shared.DateRange.duration",

    (shared.Compiler, 'name'): "cim.1.shared.Compiler.name",

    (shared.Compiler, 'type'): "cim.1.shared.Compiler.type",

    (shared.Compiler, 'options'): "cim.1.shared.Compiler.options",

    (shared.Compiler, 'environment_variables'): "cim.1.shared.Compiler.environment_variables",

    (shared.Compiler, 'language'): "cim.1.shared.Compiler.language",

    (shared.Compiler, 'version'): "cim.1.shared.Compiler.version",

    (shared.License, 'contact'): "cim.1.shared.License.contact",

    (shared.License, 'name'): "cim.1.shared.License.name",

    (shared.License, 'is_unrestricted'): "cim.1.shared.License.is_unrestricted",

    (shared.License, 'description'): "cim.1.shared.License.description",

    (shared.DocReference, 'url'): "cim.1.shared.DocReference.url",

    (shared.DocReference, 'id'): "cim.1.shared.DocReference.id",

    (shared.DocReference, 'version'): "cim.1.shared.DocReference.version",

    (shared.DocReference, 'name'): "cim.1.shared.DocReference.name",

    (shared.DocReference, 'changes'): "cim.1.shared.DocReference.changes",

    (shared.DocReference, 'type'): "cim.1.shared.DocReference.type",

    (shared.DocReference, 'external_id'): "cim.1.shared.DocReference.external_id",

    (shared.DocReference, 'description'): "cim.1.shared.DocReference.description",

    (shared.DocMetaInfo, 'source_key'): "cim.1.shared.DocMetaInfo.source_key",

    (shared.DocMetaInfo, 'id'): "cim.1.shared.DocMetaInfo.id",

    (shared.DocMetaInfo, 'genealogy'): "cim.1.shared.DocMetaInfo.genealogy",

    (shared.DocMetaInfo, 'update_date'): "cim.1.shared.DocMetaInfo.update_date",

    (shared.DocMetaInfo, 'type'): "cim.1.shared.DocMetaInfo.type",

    (shared.DocMetaInfo, 'project'): "cim.1.shared.DocMetaInfo.project",

    (shared.DocMetaInfo, 'drs_path'): "cim.1.shared.DocMetaInfo.drs_path",

    (shared.DocMetaInfo, 'language'): "cim.1.shared.DocMetaInfo.language",

    (shared.DocMetaInfo, 'author'): "cim.1.shared.DocMetaInfo.author",

    (shared.DocMetaInfo, 'version'): "cim.1.shared.DocMetaInfo.version",

    (shared.DocMetaInfo, 'sort_key'): "cim.1.shared.DocMetaInfo.sort_key",

    (shared.DocMetaInfo, 'institute'): "cim.1.shared.DocMetaInfo.institute",

    (shared.DocMetaInfo, 'drs_keys'): "cim.1.shared.DocMetaInfo.drs_keys",

    (shared.DocMetaInfo, 'type_sort_key'): "cim.1.shared.DocMetaInfo.type_sort_key",

    (shared.DocMetaInfo, 'status'): "cim.1.shared.DocMetaInfo.status",

    (shared.DocMetaInfo, 'source'): "cim.1.shared.DocMetaInfo.source",

    (shared.DocMetaInfo, 'type_display_name'): "cim.1.shared.DocMetaInfo.type_display_name",

    (shared.DocMetaInfo, 'external_ids'): "cim.1.shared.DocMetaInfo.external_ids",

    (shared.DocMetaInfo, 'create_date'): "cim.1.shared.DocMetaInfo.create_date",

    (shared.Standard, 'description'): "cim.1.shared.Standard.description",

    (shared.Standard, 'version'): "cim.1.shared.Standard.version",

    (shared.Standard, 'name'): "cim.1.shared.Standard.name",

    (shared.Calendar, 'range'): "cim.1.shared.Calendar.range",

    (shared.Calendar, 'description'): "cim.1.shared.Calendar.description",

    (shared.Calendar, 'length'): "cim.1.shared.Calendar.length",

    (shared.Citation, 'location'): "cim.1.shared.Citation.location",

    (shared.Citation, 'role'): "cim.1.shared.Citation.role",

    (shared.Citation, 'type'): "cim.1.shared.Citation.type",

    (shared.Citation, 'date'): "cim.1.shared.Citation.date",

    (shared.Citation, 'collective_title'): "cim.1.shared.Citation.collective_title",

    (shared.Citation, 'date_type'): "cim.1.shared.Citation.date_type",

    (shared.Citation, 'title'): "cim.1.shared.Citation.title",

    (shared.Citation, 'organisation'): "cim.1.shared.Citation.organisation",

    (shared.Citation, 'alternative_title'): "cim.1.shared.Citation.alternative_title",

    (shared.DocRelationshipTarget, 'reference'): "cim.1.shared.DocRelationshipTarget.reference",

    (shared.OpenDateRange, 'end'): "cim.1.shared.OpenDateRange.end",

    (shared.OpenDateRange, 'start'): "cim.1.shared.OpenDateRange.start",

    (shared.Platform, 'meta'): "cim.1.shared.Platform.meta",

    (shared.Platform, 'short_name'): "cim.1.shared.Platform.short_name",

    (shared.Platform, 'contacts'): "cim.1.shared.Platform.contacts",

    (shared.Platform, 'description'): "cim.1.shared.Platform.description",

    (shared.Platform, 'units'): "cim.1.shared.Platform.units",

    (shared.Platform, 'long_name'): "cim.1.shared.Platform.long_name",

    (shared.DocRelationship, 'target'): "cim.1.shared.DocRelationship.target",

    (shared.DocRelationship, 'type'): "cim.1.shared.DocRelationship.type",

    (shared.Property, 'name'): "cim.1.shared.Property.name",

    (shared.Property, 'value'): "cim.1.shared.Property.value",

    (shared.Relationship, 'description'): "cim.1.shared.Relationship.description",

    (shared.Relationship, 'direction'): "cim.1.shared.Relationship.direction",

    (shared.ClosedDateRange, 'end'): "cim.1.shared.ClosedDateRange.end",

    (shared.ClosedDateRange, 'start'): "cim.1.shared.ClosedDateRange.start",

    (shared.Machine, 'processor_type'): "cim.1.shared.Machine.processor_type",

    (shared.Machine, 'cores_per_processor'): "cim.1.shared.Machine.cores_per_processor",

    (shared.Machine, 'libraries'): "cim.1.shared.Machine.libraries",

    (shared.Machine, 'system'): "cim.1.shared.Machine.system",

    (shared.Machine, 'location'): "cim.1.shared.Machine.location",

    (shared.Machine, 'description'): "cim.1.shared.Machine.description",

    (shared.Machine, 'type'): "cim.1.shared.Machine.type",

    (shared.Machine, 'maximum_processors'): "cim.1.shared.Machine.maximum_processors",

    (shared.Machine, 'operating_system'): "cim.1.shared.Machine.operating_system",

    (shared.Machine, 'vendor'): "cim.1.shared.Machine.vendor",

    (shared.Machine, 'name'): "cim.1.shared.Machine.name",

    (shared.Machine, 'interconnect'): "cim.1.shared.Machine.interconnect",

    (software.Connection, 'time_profile'): "cim.1.software.Connection.time_profile",

    (software.Connection, 'transformers'): "cim.1.software.Connection.transformers",

    (software.Connection, 'properties'): "cim.1.software.Connection.properties",

    (software.Connection, 'spatial_regridding'): "cim.1.software.Connection.spatial_regridding",

    (software.Connection, 'sources'): "cim.1.software.Connection.sources",

    (software.Connection, 'time_lag'): "cim.1.software.Connection.time_lag",

    (software.Connection, 'time_transformation'): "cim.1.software.Connection.time_transformation",

    (software.Connection, 'target'): "cim.1.software.Connection.target",

    (software.Connection, 'type'): "cim.1.software.Connection.type",

    (software.Connection, 'description'): "cim.1.software.Connection.description",

    (software.Connection, 'priming'): "cim.1.software.Connection.priming",

    (software.ConnectionEndpoint, 'properties'): "cim.1.software.ConnectionEndpoint.properties",

    (software.ConnectionEndpoint, 'data_source'): "cim.1.software.ConnectionEndpoint.data_source",

    (software.ConnectionEndpoint, 'instance_id'): "cim.1.software.ConnectionEndpoint.instance_id",

    (software.SpatialRegriddingUserMethod, 'file'): "cim.1.software.SpatialRegriddingUserMethod.file",

    (software.SpatialRegriddingUserMethod, 'name'): "cim.1.software.SpatialRegriddingUserMethod.name",

    (software.EntryPoint, 'name'): "cim.1.software.EntryPoint.name",

    (software.Timing, 'end'): "cim.1.software.Timing.end",

    (software.Timing, 'units'): "cim.1.software.Timing.units",

    (software.Timing, 'start'): "cim.1.software.Timing.start",

    (software.Timing, 'rate'): "cim.1.software.Timing.rate",

    (software.Timing, 'is_variable_rate'): "cim.1.software.Timing.is_variable_rate",

    (software.Parallelisation, 'processes'): "cim.1.software.Parallelisation.processes",

    (software.Parallelisation, 'ranks'): "cim.1.software.Parallelisation.ranks",

    (software.CouplingEndpoint, 'properties'): "cim.1.software.CouplingEndpoint.properties",

    (software.CouplingEndpoint, 'data_source'): "cim.1.software.CouplingEndpoint.data_source",

    (software.CouplingEndpoint, 'instance_id'): "cim.1.software.CouplingEndpoint.instance_id",

    (software.ComponentLanguage, 'name'): "cim.1.software.ComponentLanguage.name",

    (software.ComponentLanguage, 'properties'): "cim.1.software.ComponentLanguage.properties",

    (software.Component, 'grid'): "cim.1.software.Component.grid",

    (software.Component, 'is_embedded'): "cim.1.software.Component.is_embedded",

    (software.Component, 'language'): "cim.1.software.Component.language",

    (software.Component, 'license'): "cim.1.software.Component.license",

    (software.Component, 'long_name'): "cim.1.software.Component.long_name",

    (software.Component, 'online_resource'): "cim.1.software.Component.online_resource",

    (software.Component, 'parent'): "cim.1.software.Component.parent",

    (software.Component, 'sub_components'): "cim.1.software.Component.sub_components",

    (software.Component, 'previous_version'): "cim.1.software.Component.previous_version",

    (software.Component, 'citations'): "cim.1.software.Component.citations",

    (software.Component, 'properties'): "cim.1.software.Component.properties",

    (software.Component, 'code_access'): "cim.1.software.Component.code_access",

    (software.Component, 'release_date'): "cim.1.software.Component.release_date",

    (software.Component, 'composition'): "cim.1.software.Component.composition",

    (software.Component, 'responsible_parties'): "cim.1.software.Component.responsible_parties",

    (software.Component, 'coupling_framework'): "cim.1.software.Component.coupling_framework",

    (software.Component, 'short_name'): "cim.1.software.Component.short_name",

    (software.Component, 'version'): "cim.1.software.Component.version",

    (software.Component, 'dependencies'): "cim.1.software.Component.dependencies",

    (software.Component, 'deployments'): "cim.1.software.Component.deployments",

    (software.Component, 'description'): "cim.1.software.Component.description",

    (software.Component, 'funding_sources'): "cim.1.software.Component.funding_sources",

    (software.StatisticalModelComponent, 'types'): "cim.1.software.StatisticalModelComponent.types",

    (software.StatisticalModelComponent, 'meta'): "cim.1.software.StatisticalModelComponent.meta",

    (software.StatisticalModelComponent, 'type'): "cim.1.software.StatisticalModelComponent.type",

    (software.StatisticalModelComponent, 'timing'): "cim.1.software.StatisticalModelComponent.timing",

    (software.TimeTransformation, 'description'): "cim.1.software.TimeTransformation.description",

    (software.TimeTransformation, 'mapping_type'): "cim.1.software.TimeTransformation.mapping_type",

    (software.ProcessorComponent, 'meta'): "cim.1.software.ProcessorComponent.meta",

    (software.SpatialRegridding, 'user_method'): "cim.1.software.SpatialRegridding.user_method",

    (software.SpatialRegridding, 'dimension'): "cim.1.software.SpatialRegridding.dimension",

    (software.SpatialRegridding, 'standard_method'): "cim.1.software.SpatialRegridding.standard_method",

    (software.SpatialRegridding, 'properties'): "cim.1.software.SpatialRegridding.properties",

    (software.TimeLag, 'units'): "cim.1.software.TimeLag.units",

    (software.TimeLag, 'value'): "cim.1.software.TimeLag.value",

    (software.ComponentProperty, 'intent'): "cim.1.software.ComponentProperty.intent",

    (software.ComponentProperty, 'standard_names'): "cim.1.software.ComponentProperty.standard_names",

    (software.ComponentProperty, 'description'): "cim.1.software.ComponentProperty.description",

    (software.ComponentProperty, 'citations'): "cim.1.software.ComponentProperty.citations",

    (software.ComponentProperty, 'short_name'): "cim.1.software.ComponentProperty.short_name",

    (software.ComponentProperty, 'long_name'): "cim.1.software.ComponentProperty.long_name",

    (software.ComponentProperty, 'units'): "cim.1.software.ComponentProperty.units",

    (software.ComponentProperty, 'is_represented'): "cim.1.software.ComponentProperty.is_represented",

    (software.ComponentProperty, 'grid'): "cim.1.software.ComponentProperty.grid",

    (software.ComponentProperty, 'values'): "cim.1.software.ComponentProperty.values",

    (software.ComponentProperty, 'sub_properties'): "cim.1.software.ComponentProperty.sub_properties",

    (software.Coupling, 'priming'): "cim.1.software.Coupling.priming",

    (software.Coupling, 'connections'): "cim.1.software.Coupling.connections",

    (software.Coupling, 'time_profile'): "cim.1.software.Coupling.time_profile",

    (software.Coupling, 'description'): "cim.1.software.Coupling.description",

    (software.Coupling, 'type'): "cim.1.software.Coupling.type",

    (software.Coupling, 'time_lag'): "cim.1.software.Coupling.time_lag",

    (software.Coupling, 'properties'): "cim.1.software.Coupling.properties",

    (software.Coupling, 'time_transformation'): "cim.1.software.Coupling.time_transformation",

    (software.Coupling, 'is_fully_specified'): "cim.1.software.Coupling.is_fully_specified",

    (software.Coupling, 'sources'): "cim.1.software.Coupling.sources",

    (software.Coupling, 'spatial_regriddings'): "cim.1.software.Coupling.spatial_regriddings",

    (software.Coupling, 'purpose'): "cim.1.software.Coupling.purpose",

    (software.Coupling, 'target'): "cim.1.software.Coupling.target",

    (software.Coupling, 'transformers'): "cim.1.software.Coupling.transformers",

    (software.Deployment, 'platform'): "cim.1.software.Deployment.platform",

    (software.Deployment, 'deployment_date'): "cim.1.software.Deployment.deployment_date",

    (software.Deployment, 'executable_name'): "cim.1.software.Deployment.executable_name",

    (software.Deployment, 'description'): "cim.1.software.Deployment.description",

    (software.Deployment, 'executable_arguments'): "cim.1.software.Deployment.executable_arguments",

    (software.Deployment, 'parallelisation'): "cim.1.software.Deployment.parallelisation",

    (software.Composition, 'couplings'): "cim.1.software.Composition.couplings",

    (software.Composition, 'description'): "cim.1.software.Composition.description",

    (software.Rank, 'min'): "cim.1.software.Rank.min",

    (software.Rank, 'value'): "cim.1.software.Rank.value",

    (software.Rank, 'increment'): "cim.1.software.Rank.increment",

    (software.Rank, 'max'): "cim.1.software.Rank.max",

    (software.ModelComponent, 'meta'): "cim.1.software.ModelComponent.meta",

    (software.ModelComponent, 'type'): "cim.1.software.ModelComponent.type",

    (software.ModelComponent, 'activity'): "cim.1.software.ModelComponent.activity",

    (software.ModelComponent, 'types'): "cim.1.software.ModelComponent.types",

    (software.ModelComponent, 'timing'): "cim.1.software.ModelComponent.timing",

    (grids.GridTileResolutionType, 'description'): "cim.1.grids.GridTileResolutionType.description",

    (grids.GridTileResolutionType, 'properties'): "cim.1.grids.GridTileResolutionType.properties",

    (grids.GridMosaic, 'mosaic_count'): "cim.1.grids.GridMosaic.mosaic_count",

    (grids.GridMosaic, 'citations'): "cim.1.grids.GridMosaic.citations",

    (grids.GridMosaic, 'id'): "cim.1.grids.GridMosaic.id",

    (grids.GridMosaic, 'type'): "cim.1.grids.GridMosaic.type",

    (grids.GridMosaic, 'is_leaf'): "cim.1.grids.GridMosaic.is_leaf",

    (grids.GridMosaic, 'short_name'): "cim.1.grids.GridMosaic.short_name",

    (grids.GridMosaic, 'mnemonic'): "cim.1.grids.GridMosaic.mnemonic",

    (grids.GridMosaic, 'mosaics'): "cim.1.grids.GridMosaic.mosaics",

    (grids.GridMosaic, 'extent'): "cim.1.grids.GridMosaic.extent",

    (grids.GridMosaic, 'description'): "cim.1.grids.GridMosaic.description",

    (grids.GridMosaic, 'tiles'): "cim.1.grids.GridMosaic.tiles",

    (grids.GridMosaic, 'has_congruent_tiles'): "cim.1.grids.GridMosaic.has_congruent_tiles",

    (grids.GridMosaic, 'tile_count'): "cim.1.grids.GridMosaic.tile_count",

    (grids.GridMosaic, 'long_name'): "cim.1.grids.GridMosaic.long_name",

    (grids.VerticalCoordinateList, 'form'): "cim.1.grids.VerticalCoordinateList.form",

    (grids.VerticalCoordinateList, 'type'): "cim.1.grids.VerticalCoordinateList.type",

    (grids.VerticalCoordinateList, 'properties'): "cim.1.grids.VerticalCoordinateList.properties",

    (grids.GridSpec, 'esm_exchange_grids'): "cim.1.grids.GridSpec.esm_exchange_grids",

    (grids.GridSpec, 'meta'): "cim.1.grids.GridSpec.meta",

    (grids.GridSpec, 'esm_model_grids'): "cim.1.grids.GridSpec.esm_model_grids",

    (grids.GridExtent, 'maximum_latitude'): "cim.1.grids.GridExtent.maximum_latitude",

    (grids.GridExtent, 'minimum_longitude'): "cim.1.grids.GridExtent.minimum_longitude",

    (grids.GridExtent, 'minimum_latitude'): "cim.1.grids.GridExtent.minimum_latitude",

    (grids.GridExtent, 'units'): "cim.1.grids.GridExtent.units",

    (grids.GridExtent, 'maximum_longitude'): "cim.1.grids.GridExtent.maximum_longitude",

    (grids.CoordinateList, 'uom'): "cim.1.grids.CoordinateList.uom",

    (grids.CoordinateList, 'has_constant_offset'): "cim.1.grids.CoordinateList.has_constant_offset",

    (grids.CoordinateList, 'length'): "cim.1.grids.CoordinateList.length",

    (grids.GridTile, 'zcoords'): "cim.1.grids.GridTile.zcoords",

    (grids.GridTile, 'horizontal_resolution'): "cim.1.grids.GridTile.horizontal_resolution",

    (grids.GridTile, 'id'): "cim.1.grids.GridTile.id",

    (grids.GridTile, 'area'): "cim.1.grids.GridTile.area",

    (grids.GridTile, 'is_conformal'): "cim.1.grids.GridTile.is_conformal",

    (grids.GridTile, 'cell_array'): "cim.1.grids.GridTile.cell_array",

    (grids.GridTile, 'is_regular'): "cim.1.grids.GridTile.is_regular",

    (grids.GridTile, 'cell_ref_array'): "cim.1.grids.GridTile.cell_ref_array",

    (grids.GridTile, 'is_terrain_following'): "cim.1.grids.GridTile.is_terrain_following",

    (grids.GridTile, 'vertical_crs'): "cim.1.grids.GridTile.vertical_crs",

    (grids.GridTile, 'coord_file'): "cim.1.grids.GridTile.coord_file",

    (grids.GridTile, 'is_uniform'): "cim.1.grids.GridTile.is_uniform",

    (grids.GridTile, 'coordinate_pole'): "cim.1.grids.GridTile.coordinate_pole",

    (grids.GridTile, 'long_name'): "cim.1.grids.GridTile.long_name",

    (grids.GridTile, 'horizontal_crs'): "cim.1.grids.GridTile.horizontal_crs",

    (grids.GridTile, 'mnemonic'): "cim.1.grids.GridTile.mnemonic",

    (grids.GridTile, 'grid_north_pole'): "cim.1.grids.GridTile.grid_north_pole",

    (grids.GridTile, 'nx'): "cim.1.grids.GridTile.nx",

    (grids.GridTile, 'simple_grid_geom'): "cim.1.grids.GridTile.simple_grid_geom",

    (grids.GridTile, 'ny'): "cim.1.grids.GridTile.ny",

    (grids.GridTile, 'nz'): "cim.1.grids.GridTile.nz",

    (grids.GridTile, 'refinement_scheme'): "cim.1.grids.GridTile.refinement_scheme",

    (grids.GridTile, 'description'): "cim.1.grids.GridTile.description",

    (grids.GridTile, 'discretization_type'): "cim.1.grids.GridTile.discretization_type",

    (grids.GridTile, 'short_name'): "cim.1.grids.GridTile.short_name",

    (grids.GridTile, 'extent'): "cim.1.grids.GridTile.extent",

    (grids.GridTile, 'vertical_resolution'): "cim.1.grids.GridTile.vertical_resolution",

    (grids.GridTile, 'geometry_type'): "cim.1.grids.GridTile.geometry_type",

    (grids.SimpleGridGeometry, 'xcoords'): "cim.1.grids.SimpleGridGeometry.xcoords",

    (grids.SimpleGridGeometry, 'dim_order'): "cim.1.grids.SimpleGridGeometry.dim_order",

    (grids.SimpleGridGeometry, 'ycoords'): "cim.1.grids.SimpleGridGeometry.ycoords",

    (grids.SimpleGridGeometry, 'is_mesh'): "cim.1.grids.SimpleGridGeometry.is_mesh",

    (grids.SimpleGridGeometry, 'zcoords'): "cim.1.grids.SimpleGridGeometry.zcoords",

    (grids.SimpleGridGeometry, 'num_dims'): "cim.1.grids.SimpleGridGeometry.num_dims",

    (quality.CimQuality, 'meta'): "cim.1.quality.CimQuality.meta",

    (quality.CimQuality, 'reports'): "cim.1.quality.CimQuality.reports",

    (quality.Report, 'date'): "cim.1.quality.Report.date",

    (quality.Report, 'measure'): "cim.1.quality.Report.measure",

    (quality.Report, 'evaluator'): "cim.1.quality.Report.evaluator",

    (quality.Report, 'evaluation'): "cim.1.quality.Report.evaluation",

    (quality.Evaluation, 'specification_hyperlink'): "cim.1.quality.Evaluation.specification_hyperlink",

    (quality.Evaluation, 'description'): "cim.1.quality.Evaluation.description",

    (quality.Evaluation, 'did_pass'): "cim.1.quality.Evaluation.did_pass",

    (quality.Evaluation, 'type'): "cim.1.quality.Evaluation.type",

    (quality.Evaluation, 'type_hyperlink'): "cim.1.quality.Evaluation.type_hyperlink",

    (quality.Evaluation, 'explanation'): "cim.1.quality.Evaluation.explanation",

    (quality.Evaluation, 'specification'): "cim.1.quality.Evaluation.specification",

    (quality.Evaluation, 'date'): "cim.1.quality.Evaluation.date",

    (quality.Evaluation, 'title'): "cim.1.quality.Evaluation.title",

    (quality.Measure, 'name'): "cim.1.quality.Measure.name",

    (quality.Measure, 'description'): "cim.1.quality.Measure.description",

    (quality.Measure, 'identification'): "cim.1.quality.Measure.identification",

    (data.DataTopic, 'description'): "cim.1.data.DataTopic.description",

    (data.DataTopic, 'unit'): "cim.1.data.DataTopic.unit",

    (data.DataTopic, 'name'): "cim.1.data.DataTopic.name",

    (data.DataExtent, 'geographical'): "cim.1.data.DataExtent.geographical",

    (data.DataExtent, 'temporal'): "cim.1.data.DataExtent.temporal",

    (data.DataObject, 'geometry_model'): "cim.1.data.DataObject.geometry_model",

    (data.DataObject, 'properties'): "cim.1.data.DataObject.properties",

    (data.DataObject, 'description'): "cim.1.data.DataObject.description",

    (data.DataObject, 'hierarchy_level'): "cim.1.data.DataObject.hierarchy_level",

    (data.DataObject, 'keyword'): "cim.1.data.DataObject.keyword",

    (data.DataObject, 'purpose'): "cim.1.data.DataObject.purpose",

    (data.DataObject, 'restriction'): "cim.1.data.DataObject.restriction",

    (data.DataObject, 'citations'): "cim.1.data.DataObject.citations",

    (data.DataObject, 'distribution'): "cim.1.data.DataObject.distribution",

    (data.DataObject, 'storage'): "cim.1.data.DataObject.storage",

    (data.DataObject, 'extent'): "cim.1.data.DataObject.extent",

    (data.DataObject, 'source_simulation'): "cim.1.data.DataObject.source_simulation",

    (data.DataObject, 'content'): "cim.1.data.DataObject.content",

    (data.DataObject, 'parent_object'): "cim.1.data.DataObject.parent_object",

    (data.DataObject, 'acronym'): "cim.1.data.DataObject.acronym",

    (data.DataObject, 'meta'): "cim.1.data.DataObject.meta",

    (data.DataObject, 'data_status'): "cim.1.data.DataObject.data_status",

    (data.DataObject, 'child_object'): "cim.1.data.DataObject.child_object",

    (data.DataHierarchyLevel, 'is_open'): "cim.1.data.DataHierarchyLevel.is_open",

    (data.DataHierarchyLevel, 'value'): "cim.1.data.DataHierarchyLevel.value",

    (data.DataHierarchyLevel, 'name'): "cim.1.data.DataHierarchyLevel.name",

    (data.DataStorage, 'format'): "cim.1.data.DataStorage.format",

    (data.DataStorage, 'size'): "cim.1.data.DataStorage.size",

    (data.DataStorage, 'modification_date'): "cim.1.data.DataStorage.modification_date",

    (data.DataStorage, 'location'): "cim.1.data.DataStorage.location",

    (data.DataExtentGeographical, 'west'): "cim.1.data.DataExtentGeographical.west",

    (data.DataExtentGeographical, 'south'): "cim.1.data.DataExtentGeographical.south",

    (data.DataExtentGeographical, 'east'): "cim.1.data.DataExtentGeographical.east",

    (data.DataExtentGeographical, 'north'): "cim.1.data.DataExtentGeographical.north",

    (data.DataProperty, 'description'): "cim.1.data.DataProperty.description",

    (data.DataStorageFile, 'path'): "cim.1.data.DataStorageFile.path",

    (data.DataStorageFile, 'file_name'): "cim.1.data.DataStorageFile.file_name",

    (data.DataStorageFile, 'file_system'): "cim.1.data.DataStorageFile.file_system",

    (data.DataContent, 'aggregation'): "cim.1.data.DataContent.aggregation",

    (data.DataContent, 'topic'): "cim.1.data.DataContent.topic",

    (data.DataContent, 'frequency'): "cim.1.data.DataContent.frequency",

    (data.DataDistribution, 'access'): "cim.1.data.DataDistribution.access",

    (data.DataDistribution, 'responsible_party'): "cim.1.data.DataDistribution.responsible_party",

    (data.DataDistribution, 'format'): "cim.1.data.DataDistribution.format",

    (data.DataDistribution, 'fee'): "cim.1.data.DataDistribution.fee",

    (data.DataRestriction, 'scope'): "cim.1.data.DataRestriction.scope",

    (data.DataRestriction, 'license'): "cim.1.data.DataRestriction.license",

    (data.DataRestriction, 'restriction'): "cim.1.data.DataRestriction.restriction",

    (data.DataExtentTimeInterval, 'factor'): "cim.1.data.DataExtentTimeInterval.factor",

    (data.DataExtentTimeInterval, 'unit'): "cim.1.data.DataExtentTimeInterval.unit",

    (data.DataExtentTimeInterval, 'radix'): "cim.1.data.DataExtentTimeInterval.radix",

    (data.DataStorageIp, 'protocol'): "cim.1.data.DataStorageIp.protocol",

    (data.DataStorageIp, 'file_name'): "cim.1.data.DataStorageIp.file_name",

    (data.DataStorageIp, 'path'): "cim.1.data.DataStorageIp.path",

    (data.DataStorageIp, 'host'): "cim.1.data.DataStorageIp.host",

    (data.DataExtentTemporal, 'begin'): "cim.1.data.DataExtentTemporal.begin",

    (data.DataExtentTemporal, 'time_interval'): "cim.1.data.DataExtentTemporal.time_interval",

    (data.DataExtentTemporal, 'end'): "cim.1.data.DataExtentTemporal.end",

    (data.DataStorageDb, 'access_string'): "cim.1.data.DataStorageDb.access_string",

    (data.DataStorageDb, 'table'): "cim.1.data.DataStorageDb.table",

    (data.DataStorageDb, 'owner'): "cim.1.data.DataStorageDb.owner",

    (data.DataStorageDb, 'name'): "cim.1.data.DataStorageDb.name",

    (activity.Simulation, 'inputs'): "cim.1.activity.Simulation.inputs",

    (activity.Simulation, 'spinup_date_range'): "cim.1.activity.Simulation.spinup_date_range",

    (activity.Simulation, 'calendar'): "cim.1.activity.Simulation.calendar",

    (activity.Simulation, 'control_simulation'): "cim.1.activity.Simulation.control_simulation",

    (activity.Simulation, 'restarts'): "cim.1.activity.Simulation.restarts",

    (activity.Simulation, 'spinup_simulation'): "cim.1.activity.Simulation.spinup_simulation",

    (activity.Simulation, 'conformances'): "cim.1.activity.Simulation.conformances",

    (activity.Simulation, 'deployments'): "cim.1.activity.Simulation.deployments",

    (activity.Simulation, 'authors'): "cim.1.activity.Simulation.authors",

    (activity.Simulation, 'simulation_id'): "cim.1.activity.Simulation.simulation_id",

    (activity.Simulation, 'outputs'): "cim.1.activity.Simulation.outputs",

    (activity.Activity, 'funding_sources'): "cim.1.activity.Activity.funding_sources",

    (activity.Activity, 'rationales'): "cim.1.activity.Activity.rationales",

    (activity.Activity, 'responsible_parties'): "cim.1.activity.Activity.responsible_parties",

    (activity.Activity, 'projects'): "cim.1.activity.Activity.projects",

    (activity.NumericalRequirementOption, 'name'): "cim.1.activity.NumericalRequirementOption.name",

    (activity.NumericalRequirementOption, 'relationship'): "cim.1.activity.NumericalRequirementOption.relationship",

    (activity.NumericalRequirementOption, 'sub_options'): "cim.1.activity.NumericalRequirementOption.sub_options",

    (activity.NumericalRequirementOption, 'description'): "cim.1.activity.NumericalRequirementOption.description",

    (activity.NumericalRequirementOption, 'id'): "cim.1.activity.NumericalRequirementOption.id",

    (activity.SimulationRun, 'date_range'): "cim.1.activity.SimulationRun.date_range",

    (activity.SimulationRun, 'model'): "cim.1.activity.SimulationRun.model",

    (activity.SimulationRun, 'meta'): "cim.1.activity.SimulationRun.meta",

    (activity.SimulationRelationshipTarget, 'simulation'): "cim.1.activity.SimulationRelationshipTarget.simulation",

    (activity.SimulationRelationshipTarget, 'target'): "cim.1.activity.SimulationRelationshipTarget.target",

    (activity.ExperimentRelationship, 'target'): "cim.1.activity.ExperimentRelationship.target",

    (activity.ExperimentRelationship, 'type'): "cim.1.activity.ExperimentRelationship.type",

    (activity.SimulationComposite, 'date_range'): "cim.1.activity.SimulationComposite.date_range",

    (activity.SimulationComposite, 'rank'): "cim.1.activity.SimulationComposite.rank",

    (activity.SimulationComposite, 'child'): "cim.1.activity.SimulationComposite.child",

    (activity.SimulationComposite, 'meta'): "cim.1.activity.SimulationComposite.meta",

    (activity.NumericalActivity, 'supports'): "cim.1.activity.NumericalActivity.supports",

    (activity.NumericalActivity, 'description'): "cim.1.activity.NumericalActivity.description",

    (activity.NumericalActivity, 'short_name'): "cim.1.activity.NumericalActivity.short_name",

    (activity.NumericalActivity, 'long_name'): "cim.1.activity.NumericalActivity.long_name",

    (activity.ExperimentRelationshipTarget, 'numerical_experiment'): "cim.1.activity.ExperimentRelationshipTarget.numerical_experiment",

    (activity.EnsembleMember, 'simulation'): "cim.1.activity.EnsembleMember.simulation",

    (activity.EnsembleMember, 'ensemble'): "cim.1.activity.EnsembleMember.ensemble",

    (activity.EnsembleMember, 'ensemble_ids'): "cim.1.activity.EnsembleMember.ensemble_ids",

    (activity.DownscalingSimulation, 'calendar'): "cim.1.activity.DownscalingSimulation.calendar",

    (activity.DownscalingSimulation, 'downscaling_type'): "cim.1.activity.DownscalingSimulation.downscaling_type",

    (activity.DownscalingSimulation, 'downscaled_from'): "cim.1.activity.DownscalingSimulation.downscaled_from",

    (activity.DownscalingSimulation, 'inputs'): "cim.1.activity.DownscalingSimulation.inputs",

    (activity.DownscalingSimulation, 'outputs'): "cim.1.activity.DownscalingSimulation.outputs",

    (activity.DownscalingSimulation, 'meta'): "cim.1.activity.DownscalingSimulation.meta",

    (activity.DownscalingSimulation, 'downscaling_id'): "cim.1.activity.DownscalingSimulation.downscaling_id",

    (activity.NumericalExperiment, 'long_name'): "cim.1.activity.NumericalExperiment.long_name",

    (activity.NumericalExperiment, 'requirements'): "cim.1.activity.NumericalExperiment.requirements",

    (activity.NumericalExperiment, 'description'): "cim.1.activity.NumericalExperiment.description",

    (activity.NumericalExperiment, 'short_name'): "cim.1.activity.NumericalExperiment.short_name",

    (activity.NumericalExperiment, 'meta'): "cim.1.activity.NumericalExperiment.meta",

    (activity.NumericalExperiment, 'experiment_id'): "cim.1.activity.NumericalExperiment.experiment_id",

    (activity.Experiment, 'supports'): "cim.1.activity.Experiment.supports",

    (activity.Experiment, 'measurement_campaigns'): "cim.1.activity.Experiment.measurement_campaigns",

    (activity.Experiment, 'generates'): "cim.1.activity.Experiment.generates",

    (activity.Experiment, 'requires'): "cim.1.activity.Experiment.requires",

    (activity.SpatioTemporalConstraint, 'date_range'): "cim.1.activity.SpatioTemporalConstraint.date_range",

    (activity.SpatioTemporalConstraint, 'spatial_resolution'): "cim.1.activity.SpatioTemporalConstraint.spatial_resolution",

    (activity.Conformance, 'description'): "cim.1.activity.Conformance.description",

    (activity.Conformance, 'sources'): "cim.1.activity.Conformance.sources",

    (activity.Conformance, 'frequency'): "cim.1.activity.Conformance.frequency",

    (activity.Conformance, 'type'): "cim.1.activity.Conformance.type",

    (activity.Conformance, 'is_conformant'): "cim.1.activity.Conformance.is_conformant",

    (activity.Conformance, 'requirements'): "cim.1.activity.Conformance.requirements",

    (activity.MeasurementCampaign, 'duration'): "cim.1.activity.MeasurementCampaign.duration",

    (activity.Ensemble, 'outputs'): "cim.1.activity.Ensemble.outputs",

    (activity.Ensemble, 'members'): "cim.1.activity.Ensemble.members",

    (activity.Ensemble, 'types'): "cim.1.activity.Ensemble.types",

    (activity.Ensemble, 'meta'): "cim.1.activity.Ensemble.meta",

    (activity.SimulationRelationship, 'target'): "cim.1.activity.SimulationRelationship.target",

    (activity.SimulationRelationship, 'type'): "cim.1.activity.SimulationRelationship.type",

    (activity.NumericalRequirement, 'options'): "cim.1.activity.NumericalRequirement.options",

    (activity.NumericalRequirement, 'description'): "cim.1.activity.NumericalRequirement.description",

    (activity.NumericalRequirement, 'requirement_type'): "cim.1.activity.NumericalRequirement.requirement_type",

    (activity.NumericalRequirement, 'id'): "cim.1.activity.NumericalRequirement.id",

    (activity.NumericalRequirement, 'source'): "cim.1.activity.NumericalRequirement.source",

    (activity.NumericalRequirement, 'name'): "cim.1.activity.NumericalRequirement.name",

    (misc.DocumentSet, 'model'): "cim.1.misc.DocumentSet.model",

    (misc.DocumentSet, 'experiment'): "cim.1.misc.DocumentSet.experiment",

    (misc.DocumentSet, 'meta'): "cim.1.misc.DocumentSet.meta",

    (misc.DocumentSet, 'platform'): "cim.1.misc.DocumentSet.platform",

    (misc.DocumentSet, 'data'): "cim.1.misc.DocumentSet.data",

    (misc.DocumentSet, 'ensembles'): "cim.1.misc.DocumentSet.ensembles",

    (misc.DocumentSet, 'simulation'): "cim.1.misc.DocumentSet.simulation",

    (misc.DocumentSet, 'grids'): "cim.1.misc.DocumentSet.grids",

    # ------------------------------------------------
    # Enums.
    # ------------------------------------------------

    shared.DocRelationshipDirectionType: "cim.1.shared.DocRelationshipDirectionType",

    shared.DocStatusType: "cim.1.shared.DocStatusType",

    shared.MachineType: "cim.1.shared.MachineType",

    shared.CompilerType: "cim.1.shared.CompilerType",

    shared.OperatingSystemType: "cim.1.shared.OperatingSystemType",

    shared.DocRelationshipType: "cim.1.shared.DocRelationshipType",

    shared.DataPurpose: "cim.1.shared.DataPurpose",

    shared.MachineVendorType: "cim.1.shared.MachineVendorType",

    shared.ChangePropertyType: "cim.1.shared.ChangePropertyType",

    shared.ProcessorType: "cim.1.shared.ProcessorType",

    shared.UnitType: "cim.1.shared.UnitType",

    shared.InterconnectType: "cim.1.shared.InterconnectType",

    shared.DocType: "cim.1.shared.DocType",

    software.SpatialRegriddingDimensionType: "cim.1.software.SpatialRegriddingDimensionType",

    software.SpatialRegriddingStandardMethodType: "cim.1.software.SpatialRegriddingStandardMethodType",

    software.CouplingFrameworkType: "cim.1.software.CouplingFrameworkType",

    software.ComponentPropertyIntentType: "cim.1.software.ComponentPropertyIntentType",

    software.ConnectionType: "cim.1.software.ConnectionType",

    software.StatisticalModelComponentType: "cim.1.software.StatisticalModelComponentType",

    software.TimeMappingType: "cim.1.software.TimeMappingType",

    software.TimingUnits: "cim.1.software.TimingUnits",

    software.ModelComponentType: "cim.1.software.ModelComponentType",

    grids.HorizontalCsEnum: "cim.1.grids.HorizontalCsEnum",

    grids.GridTypeEnum: "cim.1.grids.GridTypeEnum",

    grids.DiscretizationEnum: "cim.1.grids.DiscretizationEnum",

    grids.RefinementTypeEnum: "cim.1.grids.RefinementTypeEnum",

    grids.FeatureTypeEnum: "cim.1.grids.FeatureTypeEnum",

    grids.ArcTypeEnum: "cim.1.grids.ArcTypeEnum",

    grids.GeometryTypeEnum: "cim.1.grids.GeometryTypeEnum",

    grids.VerticalCsEnum: "cim.1.grids.VerticalCsEnum",

    grids.GridNodePositionEnum: "cim.1.grids.GridNodePositionEnum",

    quality.CimResultType: "cim.1.quality.CimResultType",

    quality.CimFeatureType: "cim.1.quality.CimFeatureType",

    quality.QualitySeverityType: "cim.1.quality.QualitySeverityType",

    quality.QualityStatusType: "cim.1.quality.QualityStatusType",

    quality.QualityIssueType: "cim.1.quality.QualityIssueType",

    quality.CimScopeCodeType: "cim.1.quality.CimScopeCodeType",

    data.DataStatusType: "cim.1.data.DataStatusType",

    data.DataHierarchyType: "cim.1.data.DataHierarchyType",

    activity.ConformanceType: "cim.1.activity.ConformanceType",

    activity.FrequencyType: "cim.1.activity.FrequencyType",

    activity.ProjectType: "cim.1.activity.ProjectType",

    activity.SimulationRelationshipType: "cim.1.activity.SimulationRelationshipType",

    activity.DownscalingType: "cim.1.activity.DownscalingType",

    activity.ResolutionType: "cim.1.activity.ResolutionType",

    activity.ExperimentRelationshipType: "cim.1.activity.ExperimentRelationshipType",

    activity.EnsembleType: "cim.1.activity.EnsembleType",

    activity.SimulationType: "cim.1.activity.SimulationType",

    # ------------------------------------------------
    # Enum members.
    # ------------------------------------------------

    (shared.DocRelationshipDirectionType, 'fromTarget'): "cim.1.shared.DocRelationshipDirectionType.fromTarget",

    (shared.DocRelationshipDirectionType, 'toTarget'): "cim.1.shared.DocRelationshipDirectionType.toTarget",

    (shared.DocStatusType, 'complete'): "cim.1.shared.DocStatusType.complete",

    (shared.DocStatusType, 'incomplete'): "cim.1.shared.DocStatusType.incomplete",

    (shared.DocStatusType, 'in-progress'): "cim.1.shared.DocStatusType.in-progress",

    (shared.MachineType, 'Vector'): "cim.1.shared.MachineType.Vector",

    (shared.MachineType, 'Beowulf'): "cim.1.shared.MachineType.Beowulf",

    (shared.MachineType, 'Parallel'): "cim.1.shared.MachineType.Parallel",

    (shared.DocRelationshipType, 'similarTo'): "cim.1.shared.DocRelationshipType.similarTo",

    (shared.DocRelationshipType, 'fixedVersionOf'): "cim.1.shared.DocRelationshipType.fixedVersionOf",

    (shared.DocRelationshipType, 'previousVersionOf'): "cim.1.shared.DocRelationshipType.previousVersionOf",

    (shared.DocRelationshipType, 'other'): "cim.1.shared.DocRelationshipType.other",

    (shared.DocRelationshipType, 'laterVersionOf'): "cim.1.shared.DocRelationshipType.laterVersionOf",

    (shared.DataPurpose, 'ancillaryFile'): "cim.1.shared.DataPurpose.ancillaryFile",

    (shared.DataPurpose, 'boundaryCondition'): "cim.1.shared.DataPurpose.boundaryCondition",

    (shared.DataPurpose, 'initialCondition'): "cim.1.shared.DataPurpose.initialCondition",

    (shared.ChangePropertyType, 'Decrement'): "cim.1.shared.ChangePropertyType.Decrement",

    (shared.ChangePropertyType, 'Increment'): "cim.1.shared.ChangePropertyType.Increment",

    (shared.ChangePropertyType, 'InitialCondition'): "cim.1.shared.ChangePropertyType.InitialCondition",

    (shared.ChangePropertyType, 'Redistribution'): "cim.1.shared.ChangePropertyType.Redistribution",

    (shared.ChangePropertyType, 'Replacement'): "cim.1.shared.ChangePropertyType.Replacement",

    (shared.ChangePropertyType, 'ModelMod'): "cim.1.shared.ChangePropertyType.ModelMod",

    (shared.ChangePropertyType, 'ParameterChange'): "cim.1.shared.ChangePropertyType.ParameterChange",

    (shared.ChangePropertyType, 'CodeChange'): "cim.1.shared.ChangePropertyType.CodeChange",

    (shared.ChangePropertyType, 'InputMod'): "cim.1.shared.ChangePropertyType.InputMod",

    (shared.ChangePropertyType, 'AncillaryFile'): "cim.1.shared.ChangePropertyType.AncillaryFile",

    (shared.ChangePropertyType, 'BoundaryCondition'): "cim.1.shared.ChangePropertyType.BoundaryCondition",

    (shared.ChangePropertyType, 'Unused'): "cim.1.shared.ChangePropertyType.Unused",

    (shared.DocType, 'gridSpec'): "cim.1.shared.DocType.gridSpec",

    (shared.DocType, 'cimQuality'): "cim.1.shared.DocType.cimQuality",

    (shared.DocType, 'numericalExperiment'): "cim.1.shared.DocType.numericalExperiment",

    (shared.DocType, 'platform'): "cim.1.shared.DocType.platform",

    (shared.DocType, 'assimilation'): "cim.1.shared.DocType.assimilation",

    (shared.DocType, 'processorComponent'): "cim.1.shared.DocType.processorComponent",

    (shared.DocType, 'simulationComposite'): "cim.1.shared.DocType.simulationComposite",

    (shared.DocType, 'modelComponent'): "cim.1.shared.DocType.modelComponent",

    (shared.DocType, 'statisticalModelComponent'): "cim.1.shared.DocType.statisticalModelComponent",

    (shared.DocType, 'dataProcessing'): "cim.1.shared.DocType.dataProcessing",

    (shared.DocType, 'downscalingSimulation'): "cim.1.shared.DocType.downscalingSimulation",

    (shared.DocType, 'ensemble'): "cim.1.shared.DocType.ensemble",

    (shared.DocType, 'dataObject'): "cim.1.shared.DocType.dataObject",

    (shared.DocType, 'simulationRun'): "cim.1.shared.DocType.simulationRun",

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

    (software.CouplingFrameworkType, 'BFG'): "cim.1.software.CouplingFrameworkType.BFG",

    (software.CouplingFrameworkType, 'ESMF'): "cim.1.software.CouplingFrameworkType.ESMF",

    (software.CouplingFrameworkType, 'OASIS'): "cim.1.software.CouplingFrameworkType.OASIS",

    (software.ComponentPropertyIntentType, 'out'): "cim.1.software.ComponentPropertyIntentType.out",

    (software.ComponentPropertyIntentType, 'in'): "cim.1.software.ComponentPropertyIntentType.in",

    (software.ComponentPropertyIntentType, 'inout'): "cim.1.software.ComponentPropertyIntentType.inout",

    (software.TimingUnits, 'minutes'): "cim.1.software.TimingUnits.minutes",

    (software.TimingUnits, 'hours'): "cim.1.software.TimingUnits.hours",

    (software.TimingUnits, 'days'): "cim.1.software.TimingUnits.days",

    (software.TimingUnits, 'months'): "cim.1.software.TimingUnits.months",

    (software.TimingUnits, 'years'): "cim.1.software.TimingUnits.years",

    (software.TimingUnits, 'decades'): "cim.1.software.TimingUnits.decades",

    (software.TimingUnits, 'centuries'): "cim.1.software.TimingUnits.centuries",

    (software.TimingUnits, 'seconds'): "cim.1.software.TimingUnits.seconds",

    (grids.HorizontalCsEnum, 'spherical'): "cim.1.grids.HorizontalCsEnum.spherical",

    (grids.HorizontalCsEnum, 'ellipsoidal'): "cim.1.grids.HorizontalCsEnum.ellipsoidal",

    (grids.HorizontalCsEnum, 'cartesian'): "cim.1.grids.HorizontalCsEnum.cartesian",

    (grids.HorizontalCsEnum, 'polar'): "cim.1.grids.HorizontalCsEnum.polar",

    (grids.GridTypeEnum, 'tripolar'): "cim.1.grids.GridTypeEnum.tripolar",

    (grids.GridTypeEnum, 'other'): "cim.1.grids.GridTypeEnum.other",

    (grids.GridTypeEnum, 'cubed_sphere'): "cim.1.grids.GridTypeEnum.cubed_sphere",

    (grids.GridTypeEnum, 'composite'): "cim.1.grids.GridTypeEnum.composite",

    (grids.GridTypeEnum, 'displaced_pole'): "cim.1.grids.GridTypeEnum.displaced_pole",

    (grids.GridTypeEnum, 'icosahedral_geodesic'): "cim.1.grids.GridTypeEnum.icosahedral_geodesic",

    (grids.GridTypeEnum, 'reduced_gaussian'): "cim.1.grids.GridTypeEnum.reduced_gaussian",

    (grids.GridTypeEnum, 'yin_yang'): "cim.1.grids.GridTypeEnum.yin_yang",

    (grids.GridTypeEnum, 'regular_lat_lon'): "cim.1.grids.GridTypeEnum.regular_lat_lon",

    (grids.GridTypeEnum, 'spectral_gaussian'): "cim.1.grids.GridTypeEnum.spectral_gaussian",

    (grids.DiscretizationEnum, 'unstructured_triangular'): "cim.1.grids.DiscretizationEnum.unstructured_triangular",

    (grids.DiscretizationEnum, 'pixel-based_catchment'): "cim.1.grids.DiscretizationEnum.pixel-based_catchment",

    (grids.DiscretizationEnum, 'unstructured_polygonal'): "cim.1.grids.DiscretizationEnum.unstructured_polygonal",

    (grids.DiscretizationEnum, 'spherical_harmonics'): "cim.1.grids.DiscretizationEnum.spherical_harmonics",

    (grids.DiscretizationEnum, 'other'): "cim.1.grids.DiscretizationEnum.other",

    (grids.DiscretizationEnum, 'logically_rectangular'): "cim.1.grids.DiscretizationEnum.logically_rectangular",

    (grids.DiscretizationEnum, 'structured_triangular'): "cim.1.grids.DiscretizationEnum.structured_triangular",

    (grids.RefinementTypeEnum, 'none'): "cim.1.grids.RefinementTypeEnum.none",

    (grids.RefinementTypeEnum, 'integer'): "cim.1.grids.RefinementTypeEnum.integer",

    (grids.RefinementTypeEnum, 'rational'): "cim.1.grids.RefinementTypeEnum.rational",

    (grids.FeatureTypeEnum, 'point'): "cim.1.grids.FeatureTypeEnum.point",

    (grids.FeatureTypeEnum, 'edge'): "cim.1.grids.FeatureTypeEnum.edge",

    (grids.ArcTypeEnum, 'geodesic'): "cim.1.grids.ArcTypeEnum.geodesic",

    (grids.ArcTypeEnum, 'complex'): "cim.1.grids.ArcTypeEnum.complex",

    (grids.ArcTypeEnum, 'small_circle'): "cim.1.grids.ArcTypeEnum.small_circle",

    (grids.ArcTypeEnum, 'great_circle'): "cim.1.grids.ArcTypeEnum.great_circle",

    (grids.GeometryTypeEnum, 'ellipsoid'): "cim.1.grids.GeometryTypeEnum.ellipsoid",

    (grids.GeometryTypeEnum, 'plane'): "cim.1.grids.GeometryTypeEnum.plane",

    (grids.GeometryTypeEnum, 'sphere'): "cim.1.grids.GeometryTypeEnum.sphere",

    (grids.VerticalCsEnum, 'space-based'): "cim.1.grids.VerticalCsEnum.space-based",

    (grids.VerticalCsEnum, 'mass-based'): "cim.1.grids.VerticalCsEnum.mass-based",

    (grids.GridNodePositionEnum, 'centre'): "cim.1.grids.GridNodePositionEnum.centre",

    (grids.GridNodePositionEnum, 'plane'): "cim.1.grids.GridNodePositionEnum.plane",

    (grids.GridNodePositionEnum, 'sphere'): "cim.1.grids.GridNodePositionEnum.sphere",

    (quality.CimResultType, 'document'): "cim.1.quality.CimResultType.document",

    (quality.CimResultType, 'logfile'): "cim.1.quality.CimResultType.logfile",

    (quality.CimResultType, 'plot'): "cim.1.quality.CimResultType.plot",

    (quality.CimFeatureType, 'diagnostic'): "cim.1.quality.CimFeatureType.diagnostic",

    (quality.CimFeatureType, 'file'): "cim.1.quality.CimFeatureType.file",

    (quality.QualitySeverityType, 'cosmetic'): "cim.1.quality.QualitySeverityType.cosmetic",

    (quality.QualitySeverityType, 'minor'): "cim.1.quality.QualitySeverityType.minor",

    (quality.QualitySeverityType, 'major'): "cim.1.quality.QualitySeverityType.major",

    (quality.QualityStatusType, 'partially_resolved'): "cim.1.quality.QualityStatusType.partially_resolved",

    (quality.QualityStatusType, 'resolved'): "cim.1.quality.QualityStatusType.resolved",

    (quality.QualityStatusType, 'confirmed'): "cim.1.quality.QualityStatusType.confirmed",

    (quality.QualityStatusType, 'reported'): "cim.1.quality.QualityStatusType.reported",

    (quality.QualityIssueType, 'data_format'): "cim.1.quality.QualityIssueType.data_format",

    (quality.QualityIssueType, 'metadata'): "cim.1.quality.QualityIssueType.metadata",

    (quality.QualityIssueType, 'data_content'): "cim.1.quality.QualityIssueType.data_content",

    (quality.QualityIssueType, 'science'): "cim.1.quality.QualityIssueType.science",

    (quality.QualityIssueType, 'data_indexing'): "cim.1.quality.QualityIssueType.data_indexing",

    (quality.CimScopeCodeType, 'dataset'): "cim.1.quality.CimScopeCodeType.dataset",

    (quality.CimScopeCodeType, 'file'): "cim.1.quality.CimScopeCodeType.file",

    (quality.CimScopeCodeType, 'ensemble'): "cim.1.quality.CimScopeCodeType.ensemble",

    (quality.CimScopeCodeType, 'service'): "cim.1.quality.CimScopeCodeType.service",

    (quality.CimScopeCodeType, 'model'): "cim.1.quality.CimScopeCodeType.model",

    (quality.CimScopeCodeType, 'modelComponent'): "cim.1.quality.CimScopeCodeType.modelComponent",

    (quality.CimScopeCodeType, 'simulation'): "cim.1.quality.CimScopeCodeType.simulation",

    (quality.CimScopeCodeType, 'experiment'): "cim.1.quality.CimScopeCodeType.experiment",

    (quality.CimScopeCodeType, 'numericalRequirement'): "cim.1.quality.CimScopeCodeType.numericalRequirement",

    (quality.CimScopeCodeType, 'software'): "cim.1.quality.CimScopeCodeType.software",

    (data.DataStatusType, 'metadataOnly'): "cim.1.data.DataStatusType.metadataOnly",

    (data.DataStatusType, 'complete'): "cim.1.data.DataStatusType.complete",

    (data.DataStatusType, 'continuouslySupplemented'): "cim.1.data.DataStatusType.continuouslySupplemented",

    (activity.ConformanceType, 'not-xxx'): "cim.1.activity.ConformanceType.not-xxx",

    (activity.ConformanceType, 'not conformant'): "cim.1.activity.ConformanceType.not-conformant",

    (activity.ConformanceType, 'standard config'): "cim.1.activity.ConformanceType.standard-config",

    (activity.ConformanceType, 'via inputs'): "cim.1.activity.ConformanceType.via-inputs",

    (activity.ConformanceType, 'via model mods'): "cim.1.activity.ConformanceType.via-model-mods",

    (activity.ConformanceType, 'combination'): "cim.1.activity.ConformanceType.combination",

    (activity.SimulationRelationshipType, 'higherResolutionVersionOf'): "cim.1.activity.SimulationRelationshipType.higherResolutionVersionOf",

    (activity.SimulationRelationshipType, 'lowerResolutionVersionOf'): "cim.1.activity.SimulationRelationshipType.lowerResolutionVersionOf",

    (activity.SimulationRelationshipType, 'fixedVersionOf'): "cim.1.activity.SimulationRelationshipType.fixedVersionOf",

    (activity.SimulationRelationshipType, 'followingSimulation'): "cim.1.activity.SimulationRelationshipType.followingSimulation",

    (activity.SimulationRelationshipType, 'extensionOf'): "cim.1.activity.SimulationRelationshipType.extensionOf",

    (activity.SimulationRelationshipType, 'responseTo'): "cim.1.activity.SimulationRelationshipType.responseTo",

    (activity.SimulationRelationshipType, 'continuationOf'): "cim.1.activity.SimulationRelationshipType.continuationOf",

    (activity.SimulationRelationshipType, 'previousSimulation'): "cim.1.activity.SimulationRelationshipType.previousSimulation",

    (activity.DownscalingType, 'statistical'): "cim.1.activity.DownscalingType.statistical",

    (activity.DownscalingType, 'dynamic'): "cim.1.activity.DownscalingType.dynamic",

    (activity.ExperimentRelationshipType, 'extensionOf'): "cim.1.activity.ExperimentRelationshipType.extensionOf",

    (activity.ExperimentRelationshipType, 'continuationOf'): "cim.1.activity.ExperimentRelationshipType.continuationOf",

    (activity.ExperimentRelationshipType, 'previousRealisation'): "cim.1.activity.ExperimentRelationshipType.previousRealisation",

    (activity.ExperimentRelationshipType, 'controlExperiment'): "cim.1.activity.ExperimentRelationshipType.controlExperiment",

    (activity.ExperimentRelationshipType, 'higherResolutionVersionOf'): "cim.1.activity.ExperimentRelationshipType.higherResolutionVersionOf",

    (activity.ExperimentRelationshipType, 'lowerResolutionVersionOf'): "cim.1.activity.ExperimentRelationshipType.lowerResolutionVersionOf",

    (activity.ExperimentRelationshipType, 'increaseEnsembleOf'): "cim.1.activity.ExperimentRelationshipType.increaseEnsembleOf",

    (activity.ExperimentRelationshipType, 'modifiedInputMethodOf'): "cim.1.activity.ExperimentRelationshipType.modifiedInputMethodOf",

    (activity.ExperimentRelationshipType, 'shorterVersionOf'): "cim.1.activity.ExperimentRelationshipType.shorterVersionOf",

    (activity.SimulationType, 'simulationComposite'): "cim.1.activity.SimulationType.simulationComposite",

    (activity.SimulationType, 'assimilation'): "cim.1.activity.SimulationType.assimilation",

    (activity.SimulationType, 'simulationRun'): "cim.1.activity.SimulationType.simulationRun",

}