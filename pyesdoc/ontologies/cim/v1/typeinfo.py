
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeinfo.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from collections import defaultdict
import datetime
import uuid


import typeset_for_shared_package as shared
import typeset_for_software_package as software
import typeset_for_grids_package as grids
import typeset_for_quality_package as quality
import typeset_for_data_package as data
import typeset_for_activity_package as activity
import typeset_for_misc_package as misc



# Module exports.
__all__ = [
    'PACKAGES',
    'DOCUMENT_TYPES',
    'CLASSES',
    'CLASS_PROPERTIES',
    'CLASS_OWN_PROPERTIES',
    'BASE_CLASSES',
    'BASE_CLASSED',
    'SUB_CLASSED',
    'SUB_CLASSES',
    'ENUMS',
    'CONSTRAINTS'
    ]

# Supported packages.
PACKAGES = (
    shared,
    software,
    grids,
    quality,
    data,
    activity,
    misc,
)

# Supported classes.
CLASSES = (
    shared.MachineCompilerUnit,
    software.Coupling,
    activity.Experiment,
    shared.Change,
    software.Timing,
    data.DataRestriction,
    software.EntryPoint,
    activity.OutputRequirement,
    quality.CimQuality,
    shared.OpenDateRange,
    grids.GridProperty,
    shared.DateRange,
    grids.VerticalCoordinateList,
    shared.ChangeProperty,
    software.ProcessorComponent,
    shared.RealCalendar,
    activity.LateralBoundaryCondition,
    activity.InitialCondition,
    data.DataDistribution,
    grids.GridExtent,
    software.SpatialRegriddingUserMethod,
    quality.Evaluation,
    activity.ExperimentRelationship,
    data.DataExtentTemporal,
    software.ComponentLanguageProperty,
    activity.NumericalRequirement,
    software.SpatialRegriddingProperty,
    software.ComponentProperty,
    shared.ClosedDateRange,
    grids.GridSpec,
    activity.SimulationRelationshipTarget,
    software.Component,
    activity.EnsembleMember,
    software.SpatialRegridding,
    activity.SpatioTemporalConstraint,
    shared.PerpetualPeriod,
    grids.GridTileResolutionType,
    software.TimeLag,
    activity.BoundaryCondition,
    misc.DocumentSet,
    data.DataStorageIp,
    software.Parallelisation,
    activity.ExperimentRelationshipTarget,
    activity.NumericalActivity,
    software.ConnectionEndpoint,
    shared.Calendar,
    grids.GridMosaic,
    grids.CoordinateList,
    data.DataExtentTimeInterval,
    shared.StandardName,
    activity.Ensemble,
    activity.SimulationRun,
    shared.DocRelationship,
    data.DataExtent,
    shared.Compiler,
    shared.Platform,
    software.Rank,
    shared.Property,
    shared.DocRelationshipTarget,
    activity.PhysicalModification,
    software.Connection,
    grids.GridTile,
    shared.DocReference,
    shared.ResponsibleParty,
    data.DataTopic,
    shared.License,
    activity.Activity,
    data.DataObject,
    software.CouplingProperty,
    quality.Report,
    data.DataStorage,
    activity.SimulationRelationship,
    software.ComponentLanguage,
    software.ConnectionProperty,
    shared.Citation,
    activity.Simulation,
    data.DataExtentGeographical,
    activity.NumericalRequirementOption,
    shared.Machine,
    shared.DataSource,
    data.DataHierarchyLevel,
    software.StatisticalModelComponent,
    software.TimeTransformation,
    software.CouplingEndpoint,
    software.Deployment,
    shared.Standard,
    shared.DocGenealogy,
    software.ModelComponent,
    activity.NumericalExperiment,
    quality.Measure,
    data.DataProperty,
    activity.Conformance,
    data.DataStorageDb,
    activity.MeasurementCampaign,
    grids.SimpleGridGeometry,
    shared.Relationship,
    shared.DocMetaInfo,
    data.DataContent,
    shared.Daily360,
    activity.SimulationComposite,
    activity.DownscalingSimulation,
    data.DataStorageFile,
    software.Composition,
)

# Supported enums.
ENUMS = (
    quality.CimResultType,
    grids.FeatureTypeEnum,
    shared.DocRelationshipDirectionType,
    activity.FrequencyType,
    activity.ProjectType,
    shared.InterconnectType,
    activity.ResolutionType,
    shared.MachineType,
    quality.QualitySeverityType,
    activity.SimulationType,
    grids.VerticalCsEnum,
    software.ModelComponentType,
    shared.ChangePropertyType,
    software.SpatialRegriddingDimensionType,
    grids.GridNodePositionEnum,
    software.SpatialRegriddingStandardMethodType,
    grids.GridTypeEnum,
    quality.CimScopeCodeType,
    shared.DataPurpose,
    activity.SimulationRelationshipType,
    grids.DiscretizationEnum,
    shared.CompilerType,
    shared.ProcessorType,
    activity.ConformanceType,
    data.DataHierarchyType,
    grids.GeometryTypeEnum,
    data.DataStatusType,
    grids.ArcTypeEnum,
    grids.HorizontalCsEnum,
    quality.CimFeatureType,
    shared.OperatingSystemType,
    shared.DocRelationshipType,
    software.CouplingFrameworkType,
    software.StatisticalModelComponentType,
    quality.QualityStatusType,
    software.TimingUnits,
    activity.EnsembleType,
    activity.DownscalingType,
    activity.ExperimentRelationshipType,
    shared.DocStatusType,
    software.ConnectionType,
    quality.QualityIssueType,
    shared.UnitType,
    shared.MachineVendorType,
    grids.RefinementTypeEnum,
    shared.DocType,
    software.ComponentPropertyIntentType,
    software.TimeMappingType,
)

# Set of supported types.
TYPES = CLASSES + ENUMS

# Total enum members across all enums.
TOTAL_ENUM_MEMBERS = sum(len(e.members) for e in ENUMS)

# Supported document types.
DOCUMENT_TYPES = (
    shared.Platform,
    software.ModelComponent,
    software.ProcessorComponent,
    software.StatisticalModelComponent,
    grids.GridSpec,
    quality.CimQuality,
    data.DataObject,
    activity.SimulationComposite,
    activity.Ensemble,
    activity.NumericalExperiment,
    activity.SimulationRun,
    activity.DownscalingSimulation,
    misc.DocumentSet,
)

# Supported class properties.
CLASS_PROPERTIES = { 
    shared.MachineCompilerUnit: (
        'compilers',
        'machine',
    ),
    software.Coupling: (
        'priming',
        'connections',
        'description',
        'transformers',
        'spatial_regriddings',
        'is_fully_specified',
        'time_profile',
        'properties',
        'target',
        'type',
        'sources',
        'time_lag',
        'purpose',
        'time_transformation',
    ),
    activity.Experiment: (
        'supports',
        'measurement_campaigns',
        'projects',
        'responsible_parties',
        'funding_sources',
        'requires',
        'rationales',
        'generates',
    ),
    shared.Change: (
        'details',
        'date',
        'description',
        'name',
        'type',
        'author',
    ),
    software.Timing: (
        'rate',
        'start',
        'is_variable_rate',
        'units',
        'end',
    ),
    data.DataRestriction: (
        'restriction',
        'scope',
        'license',
    ),
    software.EntryPoint: (
        'name',
    ),
    activity.OutputRequirement: (
        'description',
        'id',
        'name',
        'options',
        'source',
        'requirement_type',
    ),
    quality.CimQuality: (
        'meta',
        'reports',
    ),
    shared.OpenDateRange: (
        'end',
        'duration',
        'start',
    ),
    grids.GridProperty: (
        'name',
        'value',
    ),
    shared.DateRange: (
        'duration',
    ),
    grids.VerticalCoordinateList: (
        'has_constant_offset',
        'form',
        'length',
        'uom',
        'properties',
        'type',
    ),
    shared.ChangeProperty: (
        'name',
        'description',
        'value',
        'id',
    ),
    software.ProcessorComponent: (
        'dependencies',
        'version',
        'long_name',
        'deployments',
        'responsible_parties',
        'description',
        'sub_components',
        'code_access',
        'previous_version',
        'funding_sources',
        'citations',
        'purpose',
        'grid',
        'meta',
        'parent',
        'release_date',
        'properties',
        'composition',
        'language',
        'coupling_framework',
        'online_resource',
        'is_embedded',
        'license',
        'short_name',
    ),
    shared.RealCalendar: (
        'description',
        'range',
        'length',
    ),
    activity.LateralBoundaryCondition: (
        'description',
        'id',
        'name',
        'options',
        'source',
        'requirement_type',
    ),
    activity.InitialCondition: (
        'description',
        'id',
        'name',
        'options',
        'source',
        'requirement_type',
    ),
    data.DataDistribution: (
        'access',
        'fee',
        'format',
        'responsible_party',
    ),
    grids.GridExtent: (
        'maximum_latitude',
        'maximum_longitude',
        'minimum_latitude',
        'units',
        'minimum_longitude',
    ),
    software.SpatialRegriddingUserMethod: (
        'file',
        'name',
    ),
    quality.Evaluation: (
        'specification_hyperlink',
        'explanation',
        'description',
        'did_pass',
        'type_hyperlink',
        'date',
        'type',
        'specification',
        'title',
    ),
    activity.ExperimentRelationship: (
        'direction',
        'description',
        'target',
        'type',
    ),
    data.DataExtentTemporal: (
        'begin',
        'end',
        'time_interval',
    ),
    software.ComponentLanguageProperty: (
        'name',
        'value',
    ),
    activity.NumericalRequirement: (
        'description',
        'requirement_type',
        'options',
        'name',
        'source',
        'id',
    ),
    software.SpatialRegriddingProperty: (
        'name',
        'value',
    ),
    software.ComponentProperty: (
        'short_name',
        'purpose',
        'grid',
        'intent',
        'values',
        'sub_properties',
        'standard_names',
        'units',
        'long_name',
        'description',
        'citations',
        'is_represented',
    ),
    shared.ClosedDateRange: (
        'duration',
        'end',
        'start',
    ),
    grids.GridSpec: (
        'esm_exchange_grids',
        'esm_model_grids',
        'meta',
    ),
    activity.SimulationRelationshipTarget: (
        'simulation',
        'target',
    ),
    software.Component: (
        'dependencies',
        'version',
        'long_name',
        'deployments',
        'description',
        'sub_components',
        'funding_sources',
        'previous_version',
        'online_resource',
        'citations',
        'purpose',
        'grid',
        'code_access',
        'parent',
        'language',
        'release_date',
        'properties',
        'composition',
        'responsible_parties',
        'coupling_framework',
        'is_embedded',
        'license',
        'short_name',
    ),
    activity.EnsembleMember: (
        'responsible_parties',
        'simulation',
        'projects',
        'funding_sources',
        'supports',
        'ensemble',
        'description',
        'rationales',
        'ensemble_ids',
        'long_name',
        'short_name',
    ),
    software.SpatialRegridding: (
        'properties',
        'dimension',
        'user_method',
        'standard_method',
    ),
    activity.SpatioTemporalConstraint: (
        'spatial_resolution',
        'id',
        'source',
        'requirement_type',
        'options',
        'name',
        'date_range',
        'description',
    ),
    shared.PerpetualPeriod: (
        'description',
        'range',
        'length',
    ),
    grids.GridTileResolutionType: (
        'description',
        'properties',
    ),
    software.TimeLag: (
        'units',
        'value',
    ),
    activity.BoundaryCondition: (
        'description',
        'id',
        'name',
        'options',
        'source',
        'requirement_type',
    ),
    misc.DocumentSet: (
        'model',
        'ensembles',
        'meta',
        'platform',
        'grids',
        'experiment',
        'simulation',
        'data',
    ),
    data.DataStorageIp: (
        'size',
        'file_name',
        'format',
        'protocol',
        'modification_date',
        'host',
        'location',
        'path',
    ),
    software.Parallelisation: (
        'processes',
        'ranks',
    ),
    activity.ExperimentRelationshipTarget: (
        'numerical_experiment',
    ),
    activity.NumericalActivity: (
        'responsible_parties',
        'short_name',
        'funding_sources',
        'supports',
        'projects',
        'description',
        'rationales',
        'long_name',
    ),
    software.ConnectionEndpoint: (
        'instance_id',
        'data_source',
        'properties',
    ),
    shared.Calendar: (
        'description',
        'length',
        'range',
    ),
    grids.GridMosaic: (
        'mosaic_count',
        'long_name',
        'citations',
        'type',
        'description',
        'mosaics',
        'short_name',
        'has_congruent_tiles',
        'is_leaf',
        'tiles',
        'mnemonic',
        'tile_count',
        'extent',
        'id',
    ),
    grids.CoordinateList: (
        'length',
        'uom',
        'has_constant_offset',
    ),
    data.DataExtentTimeInterval: (
        'radix',
        'factor',
        'unit',
    ),
    shared.StandardName: (
        'standards',
        'is_open',
        'value',
    ),
    activity.Ensemble: (
        'responsible_parties',
        'description',
        'outputs',
        'funding_sources',
        'meta',
        'supports',
        'projects',
        'long_name',
        'members',
        'rationales',
        'types',
        'short_name',
    ),
    activity.SimulationRun: (
        'calendar',
        'date_range',
        'responsible_parties',
        'control_simulation',
        'model',
        'supports',
        'spinup_simulation',
        'projects',
        'deployments',
        'rationales',
        'short_name',
        'spinup_date_range',
        'inputs',
        'conformances',
        'outputs',
        'long_name',
        'restarts',
        'description',
        'funding_sources',
        'authors',
        'simulation_id',
        'meta',
    ),
    shared.DocRelationship: (
        'target',
        'direction',
        'type',
        'description',
    ),
    data.DataExtent: (
        'geographical',
        'temporal',
    ),
    shared.Compiler: (
        'language',
        'version',
        'options',
        'name',
        'environment_variables',
        'type',
    ),
    shared.Platform: (
        'description',
        'meta',
        'long_name',
        'short_name',
        'units',
        'contacts',
    ),
    software.Rank: (
        'max',
        'value',
        'min',
        'increment',
    ),
    shared.Property: (
        'name',
        'value',
    ),
    shared.DocRelationshipTarget: (
        'reference',
    ),
    activity.PhysicalModification: (
        'description',
        'frequency',
        'sources',
        'is_conformant',
        'requirements',
        'type',
    ),
    software.Connection: (
        'priming',
        'description',
        'sources',
        'time_transformation',
        'type',
        'spatial_regridding',
        'time_profile',
        'transformers',
        'target',
        'time_lag',
        'properties',
    ),
    grids.GridTile: (
        'horizontal_crs',
        'zcoords',
        'horizontal_resolution',
        'extent',
        'nx',
        'discretization_type',
        'simple_grid_geom',
        'id',
        'vertical_resolution',
        'area',
        'is_conformal',
        'mnemonic',
        'cell_array',
        'is_regular',
        'refinement_scheme',
        'short_name',
        'cell_ref_array',
        'description',
        'is_terrain_following',
        'nz',
        'vertical_crs',
        'coord_file',
        'is_uniform',
        'grid_north_pole',
        'coordinate_pole',
        'geometry_type',
        'long_name',
        'ny',
    ),
    shared.DocReference: (
        'id',
        'name',
        'type',
        'description',
        'changes',
        'url',
        'version',
        'external_id',
    ),
    shared.ResponsibleParty: (
        'address',
        'individual_name',
        'email',
        'abbreviation',
        'url',
        'organisation_name',
        'role',
    ),
    data.DataTopic: (
        'description',
        'name',
        'unit',
    ),
    shared.License: (
        'description',
        'name',
        'is_unrestricted',
        'contact',
    ),
    activity.Activity: (
        'responsible_parties',
        'projects',
        'rationales',
        'funding_sources',
    ),
    data.DataObject: (
        'storage',
        'hierarchy_level',
        'citations',
        'keyword',
        'purpose',
        'content',
        'source_simulation',
        'parent_object',
        'data_status',
        'child_object',
        'properties',
        'description',
        'restriction',
        'purpose',
        'distribution',
        'meta',
        'extent',
        'acronym',
        'geometry_model',
    ),
    software.CouplingProperty: (
        'name',
        'value',
    ),
    quality.Report: (
        'date',
        'evaluation',
        'evaluator',
        'measure',
    ),
    data.DataStorage: (
        'format',
        'size',
        'location',
        'modification_date',
    ),
    activity.SimulationRelationship: (
        'direction',
        'description',
        'target',
        'type',
    ),
    software.ComponentLanguage: (
        'name',
        'properties',
    ),
    software.ConnectionProperty: (
        'name',
        'value',
    ),
    shared.Citation: (
        'type',
        'collective_title',
        'organisation',
        'location',
        'date_type',
        'role',
        'date',
        'title',
        'alternative_title',
    ),
    activity.Simulation: (
        'inputs',
        'rationales',
        'spinup_date_range',
        'projects',
        'calendar',
        'control_simulation',
        'restarts',
        'spinup_simulation',
        'supports',
        'conformances',
        'description',
        'funding_sources',
        'deployments',
        'responsible_parties',
        'authors',
        'simulation_id',
        'outputs',
        'long_name',
        'short_name',
    ),
    data.DataExtentGeographical: (
        'east',
        'north',
        'west',
        'south',
    ),
    activity.NumericalRequirementOption: (
        'id',
        'sub_options',
        'name',
        'relationship',
        'description',
    ),
    shared.Machine: (
        'system',
        'location',
        'libraries',
        'type',
        'interconnect',
        'maximum_processors',
        'vendor',
        'name',
        'description',
        'processor_type',
        'cores_per_processor',
        'operating_system',
    ),
    shared.DataSource: (
        'purpose',
    ),
    data.DataHierarchyLevel: (
        'is_open',
        'name',
        'value',
    ),
    software.StatisticalModelComponent: (
        'dependencies',
        'version',
        'long_name',
        'deployments',
        'responsible_parties',
        'composition',
        'description',
        'sub_components',
        'code_access',
        'previous_version',
        'funding_sources',
        'citations',
        'purpose',
        'grid',
        'meta',
        'parent',
        'release_date',
        'properties',
        'type',
        'language',
        'types',
        'online_resource',
        'is_embedded',
        'license',
        'short_name',
        'timing',
        'coupling_framework',
    ),
    software.TimeTransformation: (
        'description',
        'mapping_type',
    ),
    software.CouplingEndpoint: (
        'data_source',
        'instance_id',
        'properties',
    ),
    software.Deployment: (
        'parallelisation',
        'deployment_date',
        'executable_arguments',
        'description',
        'executable_name',
        'platform',
    ),
    shared.Standard: (
        'description',
        'name',
        'version',
    ),
    shared.DocGenealogy: (
        'relationships',
    ),
    software.ModelComponent: (
        'dependencies',
        'activity',
        'long_name',
        'deployments',
        'responsible_parties',
        'composition',
        'description',
        'purpose',
        'sub_components',
        'funding_sources',
        'license',
        'meta',
        'release_date',
        'citations',
        'version',
        'type',
        'code_access',
        'parent',
        'grid',
        'properties',
        'types',
        'language',
        'coupling_framework',
        'online_resource',
        'is_embedded',
        'timing',
        'previous_version',
        'short_name',
    ),
    activity.NumericalExperiment: (
        'supports',
        'description',
        'responsible_parties',
        'generates',
        'short_name',
        'experiment_id',
        'meta',
        'projects',
        'long_name',
        'funding_sources',
        'requires',
        'rationales',
        'requirements',
        'measurement_campaigns',
    ),
    quality.Measure: (
        'identification',
        'name',
        'description',
    ),
    data.DataProperty: (
        'description',
        'value',
        'name',
    ),
    activity.Conformance: (
        'description',
        'requirements',
        'sources',
        'is_conformant',
        'frequency',
        'type',
    ),
    data.DataStorageDb: (
        'table',
        'size',
        'access_string',
        'location',
        'name',
        'format',
        'owner',
        'modification_date',
    ),
    activity.MeasurementCampaign: (
        'responsible_parties',
        'funding_sources',
        'duration',
        'rationales',
        'projects',
    ),
    grids.SimpleGridGeometry: (
        'is_mesh',
        'xcoords',
        'num_dims',
        'dim_order',
        'ycoords',
        'zcoords',
    ),
    shared.Relationship: (
        'description',
        'direction',
    ),
    shared.DocMetaInfo: (
        'version',
        'sort_key',
        'drs_keys',
        'institute',
        'external_ids',
        'update_date',
        'status',
        'type',
        'id',
        'type_sort_key',
        'type_display_name',
        'genealogy',
        'author',
        'language',
        'create_date',
        'source',
        'project',
        'drs_path',
        'source_key',
    ),
    data.DataContent: (
        'aggregation',
        'purpose',
        'topic',
        'frequency',
    ),
    shared.Daily360: (
        'description',
        'range',
        'length',
    ),
    activity.SimulationComposite: (
        'calendar',
        'spinup_date_range',
        'responsible_parties',
        'date_range',
        'conformances',
        'spinup_simulation',
        'supports',
        'rank',
        'funding_sources',
        'deployments',
        'rationales',
        'short_name',
        'inputs',
        'projects',
        'outputs',
        'long_name',
        'restarts',
        'meta',
        'control_simulation',
        'authors',
        'simulation_id',
        'child',
        'description',
    ),
    activity.DownscalingSimulation: (
        'meta',
        'description',
        'outputs',
        'responsible_parties',
        'funding_sources',
        'downscaling_id',
        'supports',
        'downscaling_type',
        'projects',
        'long_name',
        'downscaled_from',
        'rationales',
        'inputs',
        'short_name',
        'calendar',
    ),
    data.DataStorageFile: (
        'size',
        'modification_date',
        'file_name',
        'location',
        'format',
        'path',
        'file_system',
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
}

# Supported class own properties.
CLASS_OWN_PROPERTIES = { 
    shared.MachineCompilerUnit: (
        'compilers',
        'machine',
    ),
    software.Coupling: (
        'priming',
        'time_lag',
        'sources',
        'spatial_regriddings',
        'is_fully_specified',
        'connections',
        'transformers',
        'properties',
        'type',
        'target',
        'time_profile',
        'description',
        'purpose',
        'time_transformation',
    ),
    activity.Experiment: (
        'generates',
        'supports',
        'measurement_campaigns',
        'requires',
    ),
    shared.Change: (
        'details',
        'name',
        'author',
        'type',
        'description',
        'date',
    ),
    software.Timing: (
        'start',
        'end',
        'units',
        'rate',
        'is_variable_rate',
    ),
    data.DataRestriction: (
        'scope',
        'license',
        'restriction',
    ),
    software.EntryPoint: (
        'name',
    ),
    activity.OutputRequirement: (
    ),
    quality.CimQuality: (
        'meta',
        'reports',
    ),
    shared.OpenDateRange: (
        'end',
        'start',
    ),
    grids.GridProperty: (
    ),
    shared.DateRange: (
        'duration',
    ),
    grids.VerticalCoordinateList: (
        'form',
        'type',
        'properties',
    ),
    shared.ChangeProperty: (
        'description',
        'id',
    ),
    software.ProcessorComponent: (
        'meta',
    ),
    shared.RealCalendar: (
    ),
    activity.LateralBoundaryCondition: (
    ),
    activity.InitialCondition: (
    ),
    data.DataDistribution: (
        'access',
        'responsible_party',
        'format',
        'fee',
    ),
    grids.GridExtent: (
        'maximum_latitude',
        'minimum_longitude',
        'minimum_latitude',
        'units',
        'maximum_longitude',
    ),
    software.SpatialRegriddingUserMethod: (
        'file',
        'name',
    ),
    quality.Evaluation: (
        'specification_hyperlink',
        'description',
        'did_pass',
        'type',
        'type_hyperlink',
        'explanation',
        'specification',
        'date',
        'title',
    ),
    activity.ExperimentRelationship: (
        'target',
        'type',
    ),
    data.DataExtentTemporal: (
        'begin',
        'time_interval',
        'end',
    ),
    software.ComponentLanguageProperty: (
    ),
    activity.NumericalRequirement: (
        'requirement_type',
        'source',
        'id',
        'name',
        'options',
        'description',
    ),
    software.SpatialRegriddingProperty: (
    ),
    software.ComponentProperty: (
        'short_name',
        'grid',
        'is_represented',
        'intent',
        'values',
        'sub_properties',
        'standard_names',
        'citations',
        'description',
        'long_name',
        'units',
    ),
    shared.ClosedDateRange: (
        'end',
        'start',
    ),
    grids.GridSpec: (
        'esm_exchange_grids',
        'meta',
        'esm_model_grids',
    ),
    activity.SimulationRelationshipTarget: (
        'simulation',
        'target',
    ),
    software.Component: (
        'dependencies',
        'version',
        'deployments',
        'description',
        'funding_sources',
        'grid',
        'is_embedded',
        'language',
        'license',
        'long_name',
        'online_resource',
        'parent',
        'sub_components',
        'previous_version',
        'citations',
        'properties',
        'code_access',
        'release_date',
        'composition',
        'responsible_parties',
        'coupling_framework',
        'short_name',
    ),
    activity.EnsembleMember: (
        'ensemble',
        'simulation',
        'ensemble_ids',
    ),
    software.SpatialRegridding: (
        'user_method',
        'dimension',
        'standard_method',
        'properties',
    ),
    activity.SpatioTemporalConstraint: (
        'date_range',
        'spatial_resolution',
    ),
    shared.PerpetualPeriod: (
    ),
    grids.GridTileResolutionType: (
        'description',
        'properties',
    ),
    software.TimeLag: (
        'units',
        'value',
    ),
    activity.BoundaryCondition: (
    ),
    misc.DocumentSet: (
        'model',
        'experiment',
        'meta',
        'platform',
        'data',
        'ensembles',
        'simulation',
        'grids',
    ),
    data.DataStorageIp: (
        'protocol',
        'file_name',
        'path',
        'host',
    ),
    software.Parallelisation: (
        'processes',
        'ranks',
    ),
    activity.ExperimentRelationshipTarget: (
        'numerical_experiment',
    ),
    activity.NumericalActivity: (
        'supports',
        'description',
        'short_name',
        'long_name',
    ),
    software.ConnectionEndpoint: (
        'data_source',
        'properties',
        'instance_id',
    ),
    shared.Calendar: (
        'description',
        'range',
        'length',
    ),
    grids.GridMosaic: (
        'mosaic_count',
        'citations',
        'id',
        'type',
        'is_leaf',
        'short_name',
        'mnemonic',
        'mosaics',
        'extent',
        'description',
        'tiles',
        'has_congruent_tiles',
        'tile_count',
        'long_name',
    ),
    grids.CoordinateList: (
        'uom',
        'has_constant_offset',
        'length',
    ),
    data.DataExtentTimeInterval: (
        'factor',
        'unit',
        'radix',
    ),
    shared.StandardName: (
        'is_open',
        'value',
        'standards',
    ),
    activity.Ensemble: (
        'outputs',
        'members',
        'types',
        'meta',
    ),
    activity.SimulationRun: (
        'model',
        'date_range',
        'meta',
    ),
    shared.DocRelationship: (
        'target',
        'type',
    ),
    data.DataExtent: (
        'geographical',
        'temporal',
    ),
    shared.Compiler: (
        'language',
        'version',
        'name',
        'options',
        'type',
        'environment_variables',
    ),
    shared.Platform: (
        'meta',
        'short_name',
        'contacts',
        'description',
        'units',
        'long_name',
    ),
    software.Rank: (
        'value',
        'increment',
        'min',
        'max',
    ),
    shared.Property: (
        'name',
        'value',
    ),
    shared.DocRelationshipTarget: (
        'reference',
    ),
    activity.PhysicalModification: (
    ),
    software.Connection: (
        'time_lag',
        'time_transformation',
        'type',
        'description',
        'properties',
        'priming',
        'time_profile',
        'transformers',
        'spatial_regridding',
        'target',
        'sources',
    ),
    grids.GridTile: (
        'zcoords',
        'horizontal_resolution',
        'id',
        'area',
        'is_conformal',
        'cell_array',
        'is_regular',
        'cell_ref_array',
        'is_terrain_following',
        'vertical_crs',
        'coord_file',
        'is_uniform',
        'coordinate_pole',
        'long_name',
        'horizontal_crs',
        'mnemonic',
        'grid_north_pole',
        'nx',
        'simple_grid_geom',
        'ny',
        'nz',
        'refinement_scheme',
        'description',
        'discretization_type',
        'short_name',
        'extent',
        'vertical_resolution',
        'geometry_type',
    ),
    shared.DocReference: (
        'version',
        'name',
        'type',
        'description',
        'url',
        'external_id',
        'id',
        'changes',
    ),
    shared.ResponsibleParty: (
        'individual_name',
        'abbreviation',
        'organisation_name',
        'address',
        'role',
        'email',
        'url',
    ),
    data.DataTopic: (
        'description',
        'unit',
        'name',
    ),
    shared.License: (
        'name',
        'contact',
        'is_unrestricted',
        'description',
    ),
    activity.Activity: (
        'responsible_parties',
        'funding_sources',
        'rationales',
        'projects',
    ),
    data.DataObject: (
        'geometry_model',
        'properties',
        'description',
        'hierarchy_level',
        'keyword',
        'purpose',
        'citations',
        'distribution',
        'storage',
        'extent',
        'restriction',
        'content',
        'parent_object',
        'source_simulation',
        'acronym',
        'meta',
        'data_status',
        'child_object',
    ),
    software.CouplingProperty: (
    ),
    quality.Report: (
        'date',
        'measure',
        'evaluator',
        'evaluation',
    ),
    data.DataStorage: (
        'format',
        'modification_date',
        'size',
        'location',
    ),
    activity.SimulationRelationship: (
        'target',
        'type',
    ),
    software.ComponentLanguage: (
        'name',
        'properties',
    ),
    software.ConnectionProperty: (
    ),
    shared.Citation: (
        'type',
        'collective_title',
        'organisation',
        'location',
        'alternative_title',
        'role',
        'date',
        'title',
        'date_type',
    ),
    activity.Simulation: (
        'inputs',
        'spinup_date_range',
        'calendar',
        'control_simulation',
        'restarts',
        'spinup_simulation',
        'conformances',
        'deployments',
        'authors',
        'simulation_id',
        'outputs',
    ),
    data.DataExtentGeographical: (
        'west',
        'south',
        'east',
        'north',
    ),
    activity.NumericalRequirementOption: (
        'sub_options',
        'description',
        'name',
        'relationship',
        'id',
    ),
    shared.Machine: (
        'system',
        'location',
        'interconnect',
        'type',
        'maximum_processors',
        'cores_per_processor',
        'vendor',
        'name',
        'operating_system',
        'processor_type',
        'libraries',
        'description',
    ),
    shared.DataSource: (
        'purpose',
    ),
    data.DataHierarchyLevel: (
        'is_open',
        'value',
        'name',
    ),
    software.StatisticalModelComponent: (
        'type',
        'types',
        'meta',
        'timing',
    ),
    software.TimeTransformation: (
        'description',
        'mapping_type',
    ),
    software.CouplingEndpoint: (
        'data_source',
        'properties',
        'instance_id',
    ),
    software.Deployment: (
        'parallelisation',
        'executable_name',
        'platform',
        'deployment_date',
        'description',
        'executable_arguments',
    ),
    shared.Standard: (
        'description',
        'version',
        'name',
    ),
    shared.DocGenealogy: (
        'relationships',
    ),
    software.ModelComponent: (
        'meta',
        'type',
        'types',
        'activity',
        'timing',
    ),
    activity.NumericalExperiment: (
        'description',
        'short_name',
        'experiment_id',
        'requirements',
        'long_name',
        'meta',
    ),
    quality.Measure: (
        'name',
        'description',
        'identification',
    ),
    data.DataProperty: (
        'description',
    ),
    activity.Conformance: (
        'description',
        'sources',
        'frequency',
        'type',
        'is_conformant',
        'requirements',
    ),
    data.DataStorageDb: (
        'access_string',
        'table',
        'owner',
        'name',
    ),
    activity.MeasurementCampaign: (
        'duration',
    ),
    grids.SimpleGridGeometry: (
        'xcoords',
        'dim_order',
        'ycoords',
        'is_mesh',
        'zcoords',
        'num_dims',
    ),
    shared.Relationship: (
        'description',
        'direction',
    ),
    shared.DocMetaInfo: (
        'version',
        'id',
        'project',
        'update_date',
        'language',
        'status',
        'drs_keys',
        'type_sort_key',
        'author',
        'source',
        'type_display_name',
        'external_ids',
        'create_date',
        'institute',
        'source_key',
        'genealogy',
        'drs_path',
        'sort_key',
        'type',
    ),
    data.DataContent: (
        'aggregation',
        'topic',
        'frequency',
    ),
    shared.Daily360: (
    ),
    activity.SimulationComposite: (
        'date_range',
        'rank',
        'child',
        'meta',
    ),
    activity.DownscalingSimulation: (
        'downscaling_type',
        'outputs',
        'downscaling_id',
        'meta',
        'calendar',
        'inputs',
        'downscaled_from',
    ),
    data.DataStorageFile: (
        'path',
        'file_name',
        'file_system',
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
}

# Total class properties.
TOTAL_CLASS_PROPERTIES = sum(len(i) for i in CLASS_OWN_PROPERTIES.values())

# Base classes.
BASE_CLASSES = defaultdict(tuple)
BASE_CLASSES[activity.Experiment] = (activity.Activity, )
BASE_CLASSES[activity.OutputRequirement] = (activity.NumericalRequirement, )
BASE_CLASSES[shared.OpenDateRange] = (shared.DateRange, )
BASE_CLASSES[grids.GridProperty] = (shared.Property, )
BASE_CLASSES[grids.VerticalCoordinateList] = (grids.CoordinateList, )
BASE_CLASSES[shared.ChangeProperty] = (shared.Property, )
BASE_CLASSES[software.ProcessorComponent] = (software.Component, shared.DataSource, )
BASE_CLASSES[shared.RealCalendar] = (shared.Calendar, )
BASE_CLASSES[activity.LateralBoundaryCondition] = (activity.NumericalRequirement, )
BASE_CLASSES[activity.InitialCondition] = (activity.NumericalRequirement, )
BASE_CLASSES[activity.ExperimentRelationship] = (shared.Relationship, )
BASE_CLASSES[software.ComponentLanguageProperty] = (shared.Property, )
BASE_CLASSES[software.SpatialRegriddingProperty] = (shared.Property, )
BASE_CLASSES[software.ComponentProperty] = (shared.DataSource, )
BASE_CLASSES[shared.ClosedDateRange] = (shared.DateRange, )
BASE_CLASSES[software.Component] = (shared.DataSource, )
BASE_CLASSES[activity.EnsembleMember] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[activity.SpatioTemporalConstraint] = (activity.NumericalRequirement, )
BASE_CLASSES[shared.PerpetualPeriod] = (shared.Calendar, )
BASE_CLASSES[activity.BoundaryCondition] = (activity.NumericalRequirement, )
BASE_CLASSES[data.DataStorageIp] = (data.DataStorage, )
BASE_CLASSES[activity.NumericalActivity] = (activity.Activity, )
BASE_CLASSES[activity.Ensemble] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[activity.SimulationRun] = (activity.Simulation, activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[shared.DocRelationship] = (shared.Relationship, )
BASE_CLASSES[activity.PhysicalModification] = (activity.Conformance, )
BASE_CLASSES[data.DataObject] = (shared.DataSource, )
BASE_CLASSES[software.CouplingProperty] = (shared.Property, )
BASE_CLASSES[activity.SimulationRelationship] = (shared.Relationship, )
BASE_CLASSES[software.ConnectionProperty] = (shared.Property, )
BASE_CLASSES[activity.Simulation] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[software.StatisticalModelComponent] = (software.Component, shared.DataSource, )
BASE_CLASSES[software.ModelComponent] = (software.Component, shared.DataSource, )
BASE_CLASSES[activity.NumericalExperiment] = (activity.Experiment, activity.Activity, )
BASE_CLASSES[data.DataProperty] = (shared.Property, )
BASE_CLASSES[data.DataStorageDb] = (data.DataStorage, )
BASE_CLASSES[activity.MeasurementCampaign] = (activity.Activity, )
BASE_CLASSES[data.DataContent] = (shared.DataSource, )
BASE_CLASSES[shared.Daily360] = (shared.Calendar, )
BASE_CLASSES[activity.SimulationComposite] = (activity.Simulation, activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[activity.DownscalingSimulation] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[data.DataStorageFile] = (data.DataStorage, )

# Classes with base classes.
BASE_CLASSED = tuple(BASE_CLASSES.keys())

# Sub classes.
SUB_CLASSES = defaultdict(tuple)
SUB_CLASSES[activity.Experiment] = (
    activity.NumericalExperiment,
    )
SUB_CLASSES[shared.Relationship] = (
    activity.SimulationRelationship,
    activity.ExperimentRelationship,
    shared.DocRelationship,
    )
SUB_CLASSES[shared.DateRange] = (
    shared.ClosedDateRange,
    shared.OpenDateRange,
    )
SUB_CLASSES[activity.NumericalActivity] = (
    activity.Ensemble,
    activity.Simulation,
    activity.EnsembleMember,
    activity.DownscalingSimulation,
    activity.SimulationComposite,
    activity.SimulationRun,
    )
SUB_CLASSES[shared.Property] = (
    data.DataProperty,
    software.ConnectionProperty,
    software.ComponentLanguageProperty,
    software.SpatialRegriddingProperty,
    software.CouplingProperty,
    grids.GridProperty,
    shared.ChangeProperty,
    )
SUB_CLASSES[shared.Calendar] = (
    shared.PerpetualPeriod,
    shared.RealCalendar,
    shared.Daily360,
    )
SUB_CLASSES[data.DataStorage] = (
    data.DataStorageDb,
    data.DataStorageFile,
    data.DataStorageIp,
    )
SUB_CLASSES[software.Component] = (
    software.ModelComponent,
    software.ProcessorComponent,
    software.StatisticalModelComponent,
    )
SUB_CLASSES[activity.Simulation] = (
    activity.SimulationComposite,
    activity.SimulationRun,
    )
SUB_CLASSES[grids.CoordinateList] = (
    grids.VerticalCoordinateList,
    )
SUB_CLASSES[shared.DataSource] = (
    data.DataContent,
    data.DataObject,
    software.Component,
    software.ComponentProperty,
    software.ModelComponent,
    software.ProcessorComponent,
    software.StatisticalModelComponent,
    )
SUB_CLASSES[activity.Conformance] = (
    activity.PhysicalModification,
    )
SUB_CLASSES[activity.NumericalRequirement] = (
    activity.OutputRequirement,
    activity.BoundaryCondition,
    activity.InitialCondition,
    activity.LateralBoundaryCondition,
    activity.SpatioTemporalConstraint,
    )
SUB_CLASSES[activity.Activity] = (
    activity.MeasurementCampaign,
    activity.NumericalActivity,
    activity.Experiment,
    activity.Ensemble,
    activity.Simulation,
    activity.NumericalExperiment,
    activity.EnsembleMember,
    activity.DownscalingSimulation,
    activity.SimulationComposite,
    activity.SimulationRun,
    )

# Classes that have been sub classed.
SUB_CLASSED = tuple(SUB_CLASSES.keys())

# Maximum class depth in hierarchy.
CLASS_HIERACHY_DEPTH = max(len(v) for v in BASE_CLASSES.values())

# Map of ontology types to constraints.
CONSTRAINTS = {
    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    shared.MachineCompilerUnit: (

        ('machine', 'type', shared.Machine),
        ('compilers', 'type', shared.Compiler),

        ('machine', 'cardinality', "1.1"),
        ('compilers', 'cardinality', "0.N"),

    ),
    software.Coupling: (

        ('transformers', 'type', software.ProcessorComponent),
        ('description', 'type', unicode),
        ('type', 'type', unicode),
        ('time_transformation', 'type', software.TimeTransformation),
        ('connections', 'type', software.Connection),
        ('sources', 'type', software.CouplingEndpoint),
        ('spatial_regriddings', 'type', software.SpatialRegridding),
        ('purpose', 'type', unicode),
        ('target', 'type', software.CouplingEndpoint),
        ('time_profile', 'type', software.Timing),
        ('is_fully_specified', 'type', bool),
        ('properties', 'type', software.CouplingProperty),
        ('time_lag', 'type', software.TimeLag),
        ('priming', 'type', shared.DataSource),

        ('transformers', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('time_transformation', 'cardinality', "0.1"),
        ('connections', 'cardinality', "0.N"),
        ('sources', 'cardinality', "1.N"),
        ('spatial_regriddings', 'cardinality', "0.N"),
        ('purpose', 'cardinality', "1.1"),
        ('target', 'cardinality', "1.1"),
        ('time_profile', 'cardinality', "0.1"),
        ('is_fully_specified', 'cardinality', "1.1"),
        ('properties', 'cardinality', "0.N"),
        ('time_lag', 'cardinality', "0.1"),
        ('priming', 'cardinality', "0.1"),

    ),
    activity.Experiment: (

        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('generates', 'type', unicode),
        ('requires', 'type', activity.NumericalActivity),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('measurement_campaigns', 'type', activity.MeasurementCampaign),
        ('supports', 'type', unicode),
        ('projects', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('generates', 'cardinality', "0.N"),
        ('requires', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('measurement_campaigns', 'cardinality', "0.N"),
        ('supports', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),

    ),
    shared.Change: (

        ('name', 'type', unicode),
        ('author', 'type', shared.ResponsibleParty),
        ('details', 'type', shared.ChangeProperty),
        ('date', 'type', datetime.datetime),
        ('type', 'type', unicode),
        ('description', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('author', 'cardinality', "0.1"),
        ('details', 'cardinality', "1.N"),
        ('date', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    software.Timing: (

        ('units', 'type', unicode),
        ('start', 'type', datetime.datetime),
        ('rate', 'type', int),
        ('end', 'type', datetime.datetime),
        ('is_variable_rate', 'type', bool),

        ('units', 'cardinality', "0.1"),
        ('start', 'cardinality', "0.1"),
        ('rate', 'cardinality', "0.1"),
        ('end', 'cardinality', "0.1"),
        ('is_variable_rate', 'cardinality', "0.1"),

    ),
    data.DataRestriction: (

        ('restriction', 'type', unicode),
        ('license', 'type', shared.License),
        ('scope', 'type', unicode),

        ('restriction', 'cardinality', "0.1"),
        ('license', 'cardinality', "0.1"),
        ('scope', 'cardinality', "0.1"),

    ),
    software.EntryPoint: (

        ('name', 'type', unicode),

        ('name', 'cardinality', "0.1"),

    ),
    activity.OutputRequirement: (

        ('description', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('source', 'type', shared.DataSource),
        ('requirement_type', 'type', unicode),
        ('id', 'type', unicode),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('options', 'cardinality', "0.N"),
        ('source', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('id', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

        ('requirement_type', 'constant', "outputRequirement"),
    ),
    quality.CimQuality: (

        ('meta', 'type', shared.DocMetaInfo),
        ('reports', 'type', quality.Report),

        ('meta', 'cardinality', "1.1"),
        ('reports', 'cardinality', "0.N"),

    ),
    shared.OpenDateRange: (

        ('duration', 'type', unicode),
        ('start', 'type', datetime.datetime),
        ('end', 'type', datetime.datetime),

        ('duration', 'cardinality', "0.1"),
        ('start', 'cardinality', "0.1"),
        ('end', 'cardinality', "0.1"),

    ),
    grids.GridProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    shared.DateRange: (

        ('duration', 'type', unicode),

        ('duration', 'cardinality', "0.1"),

    ),
    grids.VerticalCoordinateList: (

        ('has_constant_offset', 'type', bool),
        ('form', 'type', unicode),
        ('length', 'type', int),
        ('type', 'type', unicode),
        ('properties', 'type', grids.GridProperty),
        ('uom', 'type', unicode),

        ('has_constant_offset', 'cardinality', "0.1"),
        ('form', 'cardinality', "0.1"),
        ('length', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('uom', 'cardinality', "0.1"),

    ),
    shared.ChangeProperty: (

        ('id', 'type', unicode),
        ('name', 'type', unicode),
        ('value', 'type', unicode),
        ('description', 'type', unicode),

        ('id', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    software.ProcessorComponent: (

        ('funding_sources', 'type', unicode),
        ('version', 'type', unicode),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('is_embedded', 'type', bool),
        ('short_name', 'type', unicode),
        ('previous_version', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('deployments', 'type', software.Deployment),
        ('citations', 'type', shared.Citation),
        ('composition', 'type', software.Composition),
        ('coupling_framework', 'type', unicode),
        ('description', 'type', unicode),
        ('parent', 'type', software.Component),
        ('sub_components', 'type', software.Component),
        ('dependencies', 'type', software.EntryPoint),
        ('grid', 'type', grids.GridSpec),
        ('purpose', 'type', unicode),
        ('online_resource', 'type', unicode),
        ('properties', 'type', software.ComponentProperty),
        ('language', 'type', software.ComponentLanguage),
        ('license', 'type', shared.License),
        ('release_date', 'type', datetime.datetime),
        ('code_access', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('version', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('is_embedded', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('previous_version', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('deployments', 'cardinality', "0.N"),
        ('citations', 'cardinality', "0.N"),
        ('composition', 'cardinality', "0.1"),
        ('coupling_framework', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('parent', 'cardinality', "0.1"),
        ('sub_components', 'cardinality', "0.N"),
        ('dependencies', 'cardinality', "0.N"),
        ('grid', 'cardinality', "0.1"),
        ('purpose', 'cardinality', "0.1"),
        ('online_resource', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('language', 'cardinality', "0.1"),
        ('license', 'cardinality', "0.1"),
        ('release_date', 'cardinality', "0.1"),
        ('code_access', 'cardinality', "0.1"),

    ),
    shared.RealCalendar: (

        ('range', 'type', shared.DateRange),
        ('length', 'type', int),
        ('description', 'type', unicode),

        ('range', 'cardinality', "0.1"),
        ('length', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    activity.LateralBoundaryCondition: (

        ('description', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('source', 'type', shared.DataSource),
        ('requirement_type', 'type', unicode),
        ('id', 'type', unicode),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('options', 'cardinality', "0.N"),
        ('source', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('id', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

        ('requirement_type', 'constant', "lateralBoundaryCondition"),
    ),
    activity.InitialCondition: (

        ('description', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('source', 'type', shared.DataSource),
        ('requirement_type', 'type', unicode),
        ('id', 'type', unicode),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('options', 'cardinality', "0.N"),
        ('source', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('id', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

        ('requirement_type', 'constant', "initialCondition"),
    ),
    data.DataDistribution: (

        ('access', 'type', unicode),
        ('fee', 'type', unicode),
        ('responsible_party', 'type', shared.ResponsibleParty),
        ('format', 'type', unicode),

        ('access', 'cardinality', "0.1"),
        ('fee', 'cardinality', "0.1"),
        ('responsible_party', 'cardinality', "0.1"),
        ('format', 'cardinality', "0.1"),

    ),
    grids.GridExtent: (

        ('units', 'type', unicode),
        ('maximum_latitude', 'type', unicode),
        ('minimum_latitude', 'type', unicode),
        ('maximum_longitude', 'type', unicode),
        ('minimum_longitude', 'type', unicode),

        ('units', 'cardinality', "0.1"),
        ('maximum_latitude', 'cardinality', "1.1"),
        ('minimum_latitude', 'cardinality', "1.1"),
        ('maximum_longitude', 'cardinality', "1.1"),
        ('minimum_longitude', 'cardinality', "1.1"),

    ),
    software.SpatialRegriddingUserMethod: (

        ('name', 'type', unicode),
        ('file', 'type', data.DataObject),

        ('name', 'cardinality', "1.1"),
        ('file', 'cardinality', "0.1"),

    ),
    quality.Evaluation: (

        ('description', 'type', unicode),
        ('type_hyperlink', 'type', unicode),
        ('explanation', 'type', unicode),
        ('specification_hyperlink', 'type', unicode),
        ('did_pass', 'type', bool),
        ('date', 'type', datetime.datetime),
        ('title', 'type', unicode),
        ('type', 'type', unicode),
        ('specification', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('type_hyperlink', 'cardinality', "0.1"),
        ('explanation', 'cardinality', "0.1"),
        ('specification_hyperlink', 'cardinality', "0.1"),
        ('did_pass', 'cardinality', "0.1"),
        ('date', 'cardinality', "0.1"),
        ('title', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('specification', 'cardinality', "0.1"),

    ),
    activity.ExperimentRelationship: (

        ('direction', 'type', unicode),
        ('type', 'type', unicode),
        ('description', 'type', unicode),
        ('target', 'type', activity.ExperimentRelationshipTarget),

        ('direction', 'cardinality', "1.1"),
        ('type', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('target', 'cardinality', "1.1"),

    ),
    data.DataExtentTemporal: (

        ('time_interval', 'type', data.DataExtentTimeInterval),
        ('begin', 'type', datetime.date),
        ('end', 'type', datetime.date),

        ('time_interval', 'cardinality', "0.1"),
        ('begin', 'cardinality', "0.1"),
        ('end', 'cardinality', "0.1"),

    ),
    software.ComponentLanguageProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    activity.NumericalRequirement: (

        ('description', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('source', 'type', shared.DataSource),
        ('requirement_type', 'type', unicode),
        ('id', 'type', unicode),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('options', 'cardinality', "0.N"),
        ('source', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('id', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    software.SpatialRegriddingProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    software.ComponentProperty: (

        ('standard_names', 'type', unicode),
        ('is_represented', 'type', bool),
        ('sub_properties', 'type', software.ComponentProperty),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('grid', 'type', unicode),
        ('long_name', 'type', unicode),
        ('citations', 'type', shared.Citation),
        ('values', 'type', unicode),
        ('purpose', 'type', unicode),
        ('units', 'type', unicode),
        ('intent', 'type', unicode),

        ('standard_names', 'cardinality', "0.N"),
        ('is_represented', 'cardinality', "1.1"),
        ('sub_properties', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('grid', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('citations', 'cardinality', "0.N"),
        ('values', 'cardinality', "0.N"),
        ('purpose', 'cardinality', "0.1"),
        ('units', 'cardinality', "0.1"),
        ('intent', 'cardinality', "0.1"),

    ),
    shared.ClosedDateRange: (

        ('duration', 'type', unicode),
        ('start', 'type', datetime.datetime),
        ('end', 'type', datetime.datetime),

        ('duration', 'cardinality', "0.1"),
        ('start', 'cardinality', "1.1"),
        ('end', 'cardinality', "0.1"),

    ),
    grids.GridSpec: (

        ('esm_exchange_grids', 'type', grids.GridMosaic),
        ('meta', 'type', shared.DocMetaInfo),
        ('esm_model_grids', 'type', grids.GridMosaic),

        ('esm_exchange_grids', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('esm_model_grids', 'cardinality', "0.N"),

    ),
    activity.SimulationRelationshipTarget: (

        ('target', 'type', unicode),
        ('simulation', 'type', shared.DocReference),

        ('target', 'cardinality', "0.1"),
        ('simulation', 'cardinality', "0.1"),

    ),
    software.Component: (

        ('funding_sources', 'type', unicode),
        ('version', 'type', unicode),
        ('long_name', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('short_name', 'type', unicode),
        ('previous_version', 'type', unicode),
        ('is_embedded', 'type', bool),
        ('deployments', 'type', software.Deployment),
        ('citations', 'type', shared.Citation),
        ('composition', 'type', software.Composition),
        ('coupling_framework', 'type', unicode),
        ('description', 'type', unicode),
        ('parent', 'type', software.Component),
        ('sub_components', 'type', software.Component),
        ('dependencies', 'type', software.EntryPoint),
        ('grid', 'type', grids.GridSpec),
        ('purpose', 'type', unicode),
        ('online_resource', 'type', unicode),
        ('properties', 'type', software.ComponentProperty),
        ('language', 'type', software.ComponentLanguage),
        ('license', 'type', shared.License),
        ('release_date', 'type', datetime.datetime),
        ('code_access', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('version', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('short_name', 'cardinality', "1.1"),
        ('previous_version', 'cardinality', "0.1"),
        ('is_embedded', 'cardinality', "0.1"),
        ('deployments', 'cardinality', "0.N"),
        ('citations', 'cardinality', "0.N"),
        ('composition', 'cardinality', "0.1"),
        ('coupling_framework', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('parent', 'cardinality', "0.1"),
        ('sub_components', 'cardinality', "0.N"),
        ('dependencies', 'cardinality', "0.N"),
        ('grid', 'cardinality', "0.1"),
        ('purpose', 'cardinality', "0.1"),
        ('online_resource', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('language', 'cardinality', "0.1"),
        ('license', 'cardinality', "0.1"),
        ('release_date', 'cardinality', "0.1"),
        ('code_access', 'cardinality', "0.1"),

    ),
    activity.EnsembleMember: (

        ('ensemble_ids', 'type', shared.StandardName),
        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('simulation', 'type', activity.Simulation),
        ('long_name', 'type', unicode),
        ('supports', 'type', activity.Experiment),
        ('ensemble', 'type', activity.Ensemble),
        ('projects', 'type', unicode),

        ('ensemble_ids', 'cardinality', "0.N"),
        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('simulation', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('supports', 'cardinality', "0.N"),
        ('ensemble', 'cardinality', "0.1"),
        ('projects', 'cardinality', "0.N"),

    ),
    software.SpatialRegridding: (

        ('user_method', 'type', software.SpatialRegriddingUserMethod),
        ('properties', 'type', software.SpatialRegriddingProperty),
        ('standard_method', 'type', unicode),
        ('dimension', 'type', unicode),

        ('user_method', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('standard_method', 'cardinality', "0.1"),
        ('dimension', 'cardinality', "0.1"),

    ),
    activity.SpatioTemporalConstraint: (

        ('description', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('date_range', 'type', shared.DateRange),
        ('source', 'type', shared.DataSource),
        ('spatial_resolution', 'type', unicode),
        ('requirement_type', 'type', unicode),
        ('id', 'type', unicode),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('options', 'cardinality', "0.N"),
        ('date_range', 'cardinality', "0.1"),
        ('source', 'cardinality', "0.1"),
        ('spatial_resolution', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('id', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

        ('requirement_type', 'constant', "spatioTemporalConstraint"),
    ),
    shared.PerpetualPeriod: (

        ('range', 'type', shared.DateRange),
        ('length', 'type', int),
        ('description', 'type', unicode),

        ('range', 'cardinality', "0.1"),
        ('length', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    grids.GridTileResolutionType: (

        ('description', 'type', unicode),
        ('properties', 'type', grids.GridProperty),

        ('description', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),

    ),
    software.TimeLag: (

        ('units', 'type', unicode),
        ('value', 'type', int),

        ('units', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    activity.BoundaryCondition: (

        ('description', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('source', 'type', shared.DataSource),
        ('requirement_type', 'type', unicode),
        ('id', 'type', unicode),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('options', 'cardinality', "0.N"),
        ('source', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('id', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

        ('requirement_type', 'constant', "boundaryCondition"),
    ),
    misc.DocumentSet: (

        ('ensembles', 'type', activity.Ensemble),
        ('grids', 'type', grids.GridSpec),
        ('simulation', 'type', activity.SimulationRun),
        ('platform', 'type', shared.Platform),
        ('experiment', 'type', activity.NumericalExperiment),
        ('meta', 'type', shared.DocMetaInfo),
        ('model', 'type', software.ModelComponent),
        ('data', 'type', data.DataObject),

        ('ensembles', 'cardinality', "0.N"),
        ('grids', 'cardinality', "0.N"),
        ('simulation', 'cardinality', "0.1"),
        ('platform', 'cardinality', "0.1"),
        ('experiment', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('model', 'cardinality', "0.1"),
        ('data', 'cardinality', "0.N"),

    ),
    data.DataStorageIp: (

        ('protocol', 'type', unicode),
        ('modification_date', 'type', datetime.datetime),
        ('format', 'type', unicode),
        ('file_name', 'type', unicode),
        ('host', 'type', unicode),
        ('location', 'type', unicode),
        ('path', 'type', unicode),
        ('size', 'type', int),

        ('protocol', 'cardinality', "0.1"),
        ('modification_date', 'cardinality', "0.1"),
        ('format', 'cardinality', "0.1"),
        ('file_name', 'cardinality', "0.1"),
        ('host', 'cardinality', "0.1"),
        ('location', 'cardinality', "0.1"),
        ('path', 'cardinality', "0.1"),
        ('size', 'cardinality', "0.1"),

    ),
    software.Parallelisation: (

        ('ranks', 'type', software.Rank),
        ('processes', 'type', int),

        ('ranks', 'cardinality', "0.N"),
        ('processes', 'cardinality', "1.1"),

    ),
    activity.ExperimentRelationshipTarget: (

        ('numerical_experiment', 'type', activity.NumericalExperiment),

        ('numerical_experiment', 'cardinality', "0.1"),

    ),
    activity.NumericalActivity: (

        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('long_name', 'type', unicode),
        ('supports', 'type', activity.Experiment),
        ('projects', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('supports', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),

    ),
    software.ConnectionEndpoint: (

        ('instance_id', 'type', unicode),
        ('data_source', 'type', shared.DataSource),
        ('properties', 'type', software.ConnectionProperty),

        ('instance_id', 'cardinality', "0.1"),
        ('data_source', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),

    ),
    shared.Calendar: (

        ('range', 'type', shared.DateRange),
        ('length', 'type', int),
        ('description', 'type', unicode),

        ('range', 'cardinality', "0.1"),
        ('length', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    grids.GridMosaic: (

        ('mosaic_count', 'type', int),
        ('is_leaf', 'type', bool),
        ('tiles', 'type', grids.GridTile),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('mosaics', 'type', grids.GridMosaic),
        ('tile_count', 'type', int),
        ('long_name', 'type', unicode),
        ('mnemonic', 'type', unicode),
        ('citations', 'type', shared.Citation),
        ('extent', 'type', grids.GridExtent),
        ('has_congruent_tiles', 'type', bool),
        ('type', 'type', unicode),
        ('id', 'type', unicode),

        ('mosaic_count', 'cardinality', "0.1"),
        ('is_leaf', 'cardinality', "1.1"),
        ('tiles', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('mosaics', 'cardinality', "0.N"),
        ('tile_count', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('mnemonic', 'cardinality', "0.1"),
        ('citations', 'cardinality', "0.N"),
        ('extent', 'cardinality', "0.1"),
        ('has_congruent_tiles', 'cardinality', "0.1"),
        ('type', 'cardinality', "1.1"),
        ('id', 'cardinality', "1.1"),

    ),
    grids.CoordinateList: (

        ('has_constant_offset', 'type', bool),
        ('length', 'type', int),
        ('uom', 'type', unicode),

        ('has_constant_offset', 'cardinality', "0.1"),
        ('length', 'cardinality', "0.1"),
        ('uom', 'cardinality', "0.1"),

    ),
    data.DataExtentTimeInterval: (

        ('radix', 'type', int),
        ('unit', 'type', unicode),
        ('factor', 'type', int),

        ('radix', 'cardinality', "0.1"),
        ('unit', 'cardinality', "0.1"),
        ('factor', 'cardinality', "0.1"),

    ),
    shared.StandardName: (

        ('is_open', 'type', bool),
        ('value', 'type', unicode),
        ('standards', 'type', shared.Standard),

        ('is_open', 'cardinality', "1.1"),
        ('value', 'cardinality', "1.1"),
        ('standards', 'cardinality', "0.N"),

    ),
    activity.Ensemble: (

        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('outputs', 'type', shared.DataSource),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('types', 'type', unicode),
        ('members', 'type', activity.EnsembleMember),
        ('supports', 'type', activity.Experiment),
        ('projects', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('outputs', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('types', 'cardinality', "1.N"),
        ('members', 'cardinality', "1.N"),
        ('supports', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),

    ),
    activity.SimulationRun: (

        ('funding_sources', 'type', unicode),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('calendar', 'type', shared.Calendar),
        ('conformances', 'type', activity.Conformance),
        ('rationales', 'type', unicode),
        ('control_simulation', 'type', activity.Simulation),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('deployments', 'type', software.Deployment),
        ('restarts', 'type', data.DataObject),
        ('supports', 'type', activity.Experiment),
        ('inputs', 'type', software.Coupling),
        ('simulation_id', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('outputs', 'type', data.DataObject),
        ('spinup_date_range', 'type', shared.ClosedDateRange),
        ('date_range', 'type', shared.DateRange),
        ('authors', 'type', unicode),
        ('projects', 'type', unicode),
        ('spinup_simulation', 'type', activity.Simulation),
        ('model', 'type', software.ModelComponent),

        ('funding_sources', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('calendar', 'cardinality', "1.1"),
        ('conformances', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('control_simulation', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('deployments', 'cardinality', "0.N"),
        ('restarts', 'cardinality', "0.N"),
        ('supports', 'cardinality', "0.N"),
        ('inputs', 'cardinality', "0.N"),
        ('simulation_id', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('outputs', 'cardinality', "0.N"),
        ('spinup_date_range', 'cardinality', "0.1"),
        ('date_range', 'cardinality', "1.1"),
        ('authors', 'cardinality', "0.1"),
        ('projects', 'cardinality', "0.N"),
        ('spinup_simulation', 'cardinality', "0.1"),
        ('model', 'cardinality', "0.1"),

    ),
    shared.DocRelationship: (

        ('direction', 'type', unicode),
        ('type', 'type', unicode),
        ('description', 'type', unicode),
        ('target', 'type', shared.DocRelationshipTarget),

        ('direction', 'cardinality', "1.1"),
        ('type', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('target', 'cardinality', "1.1"),

    ),
    data.DataExtent: (

        ('temporal', 'type', data.DataExtentTemporal),
        ('geographical', 'type', data.DataExtentGeographical),

        ('temporal', 'cardinality', "1.1"),
        ('geographical', 'cardinality', "1.1"),

    ),
    shared.Compiler: (

        ('name', 'type', unicode),
        ('language', 'type', unicode),
        ('version', 'type', unicode),
        ('environment_variables', 'type', unicode),
        ('type', 'type', unicode),
        ('options', 'type', unicode),

        ('name', 'cardinality', "1.1"),
        ('language', 'cardinality', "0.1"),
        ('version', 'cardinality', "1.1"),
        ('environment_variables', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('options', 'cardinality', "0.1"),

    ),
    shared.Platform: (

        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('contacts', 'type', shared.ResponsibleParty),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('units', 'type', shared.MachineCompilerUnit),

        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('contacts', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('units', 'cardinality', "1.N"),

    ),
    software.Rank: (

        ('max', 'type', int),
        ('increment', 'type', int),
        ('value', 'type', int),
        ('min', 'type', int),

        ('max', 'cardinality', "0.1"),
        ('increment', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),
        ('min', 'cardinality', "0.1"),

    ),
    shared.Property: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    shared.DocRelationshipTarget: (

        ('reference', 'type', shared.DocReference),

        ('reference', 'cardinality', "0.1"),

    ),
    activity.PhysicalModification: (

        ('requirements', 'type', activity.NumericalRequirement),
        ('description', 'type', unicode),
        ('sources', 'type', shared.DataSource),
        ('frequency', 'type', unicode),
        ('is_conformant', 'type', bool),
        ('type', 'type', unicode),

        ('requirements', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('sources', 'cardinality', "0.N"),
        ('frequency', 'cardinality', "0.1"),
        ('is_conformant', 'cardinality', "1.1"),
        ('type', 'cardinality', "0.1"),

    ),
    software.Connection: (

        ('transformers', 'type', software.ProcessorComponent),
        ('description', 'type', unicode),
        ('time_transformation', 'type', software.TimeTransformation),
        ('spatial_regridding', 'type', software.SpatialRegridding),
        ('sources', 'type', software.ConnectionEndpoint),
        ('target', 'type', software.ConnectionEndpoint),
        ('time_profile', 'type', software.Timing),
        ('type', 'type', unicode),
        ('properties', 'type', software.ConnectionProperty),
        ('time_lag', 'type', unicode),
        ('priming', 'type', shared.DataSource),

        ('transformers', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('time_transformation', 'cardinality', "0.1"),
        ('spatial_regridding', 'cardinality', "0.N"),
        ('sources', 'cardinality', "0.N"),
        ('target', 'cardinality', "0.1"),
        ('time_profile', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('time_lag', 'cardinality', "0.1"),
        ('priming', 'cardinality', "0.1"),

    ),
    grids.GridTile: (

        ('mnemonic', 'type', unicode),
        ('refinement_scheme', 'type', unicode),
        ('is_regular', 'type', bool),
        ('coordinate_pole', 'type', unicode),
        ('horizontal_crs', 'type', unicode),
        ('cell_array', 'type', unicode),
        ('id', 'type', unicode),
        ('cell_ref_array', 'type', unicode),
        ('area', 'type', unicode),
        ('simple_grid_geom', 'type', grids.SimpleGridGeometry),
        ('vertical_crs', 'type', unicode),
        ('nx', 'type', int),
        ('ny', 'type', int),
        ('nz', 'type', int),
        ('vertical_resolution', 'type', grids.GridTileResolutionType),
        ('discretization_type', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('extent', 'type', grids.GridExtent),
        ('zcoords', 'type', grids.VerticalCoordinateList),
        ('is_conformal', 'type', bool),
        ('is_uniform', 'type', bool),
        ('coord_file', 'type', unicode),
        ('geometry_type', 'type', unicode),
        ('long_name', 'type', unicode),
        ('is_terrain_following', 'type', bool),
        ('horizontal_resolution', 'type', grids.GridTileResolutionType),
        ('grid_north_pole', 'type', unicode),

        ('mnemonic', 'cardinality', "0.1"),
        ('refinement_scheme', 'cardinality', "0.1"),
        ('is_regular', 'cardinality', "0.1"),
        ('coordinate_pole', 'cardinality', "0.1"),
        ('horizontal_crs', 'cardinality', "0.1"),
        ('cell_array', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('cell_ref_array', 'cardinality', "0.1"),
        ('area', 'cardinality', "0.1"),
        ('simple_grid_geom', 'cardinality', "0.1"),
        ('vertical_crs', 'cardinality', "0.1"),
        ('nx', 'cardinality', "0.1"),
        ('ny', 'cardinality', "0.1"),
        ('nz', 'cardinality', "0.1"),
        ('vertical_resolution', 'cardinality', "0.1"),
        ('discretization_type', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "0.1"),
        ('extent', 'cardinality', "0.1"),
        ('zcoords', 'cardinality', "0.1"),
        ('is_conformal', 'cardinality', "0.1"),
        ('is_uniform', 'cardinality', "0.1"),
        ('coord_file', 'cardinality', "0.1"),
        ('geometry_type', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('is_terrain_following', 'cardinality', "0.1"),
        ('horizontal_resolution', 'cardinality', "0.1"),
        ('grid_north_pole', 'cardinality', "0.1"),

    ),
    shared.DocReference: (

        ('description', 'type', unicode),
        ('url', 'type', unicode),
        ('type', 'type', unicode),
        ('external_id', 'type', unicode),
        ('version', 'type', int),
        ('changes', 'type', shared.Change),
        ('id', 'type', uuid.UUID),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('url', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('external_id', 'cardinality', "0.1"),
        ('version', 'cardinality', "0.1"),
        ('changes', 'cardinality', "0.N"),
        ('id', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),

    ),
    shared.ResponsibleParty: (

        ('url', 'type', unicode),
        ('organisation_name', 'type', unicode),
        ('abbreviation', 'type', unicode),
        ('individual_name', 'type', unicode),
        ('role', 'type', unicode),
        ('address', 'type', unicode),
        ('email', 'type', unicode),

        ('url', 'cardinality', "0.1"),
        ('organisation_name', 'cardinality', "0.1"),
        ('abbreviation', 'cardinality', "0.1"),
        ('individual_name', 'cardinality', "0.1"),
        ('role', 'cardinality', "0.1"),
        ('address', 'cardinality', "0.1"),
        ('email', 'cardinality', "0.1"),

    ),
    data.DataTopic: (

        ('description', 'type', unicode),
        ('unit', 'type', unicode),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('unit', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),

    ),
    shared.License: (

        ('contact', 'type', unicode),
        ('description', 'type', unicode),
        ('is_unrestricted', 'type', bool),
        ('name', 'type', unicode),

        ('contact', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('is_unrestricted', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),

    ),
    activity.Activity: (

        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('projects', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),

    ),
    data.DataObject: (

        ('hierarchy_level', 'type', data.DataHierarchyLevel),
        ('description', 'type', unicode),
        ('keyword', 'type', unicode),
        ('restriction', 'type', data.DataRestriction),
        ('acronym', 'type', unicode),
        ('child_object', 'type', data.DataObject),
        ('storage', 'type', data.DataStorage),
        ('distribution', 'type', data.DataDistribution),
        ('content', 'type', data.DataContent),
        ('geometry_model', 'type', unicode),
        ('citations', 'type', shared.Citation),
        ('meta', 'type', shared.DocMetaInfo),
        ('purpose', 'type', unicode),
        ('extent', 'type', data.DataExtent),
        ('source_simulation', 'type', unicode),
        ('parent_object', 'type', data.DataObject),
        ('properties', 'type', data.DataProperty),
        ('data_status', 'type', unicode),

        ('hierarchy_level', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('keyword', 'cardinality', "0.1"),
        ('restriction', 'cardinality', "0.N"),
        ('acronym', 'cardinality', "0.1"),
        ('child_object', 'cardinality', "0.N"),
        ('storage', 'cardinality', "0.N"),
        ('distribution', 'cardinality', "0.1"),
        ('content', 'cardinality', "0.N"),
        ('geometry_model', 'cardinality', "0.1"),
        ('citations', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('purpose', 'cardinality', "0.1"),
        ('extent', 'cardinality', "0.1"),
        ('source_simulation', 'cardinality', "0.1"),
        ('parent_object', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('data_status', 'cardinality', "0.1"),

    ),
    software.CouplingProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    quality.Report: (

        ('date', 'type', datetime.datetime),
        ('evaluator', 'type', shared.ResponsibleParty),
        ('evaluation', 'type', quality.Evaluation),
        ('measure', 'type', quality.Measure),

        ('date', 'cardinality', "0.1"),
        ('evaluator', 'cardinality', "0.1"),
        ('evaluation', 'cardinality', "1.1"),
        ('measure', 'cardinality', "1.1"),

    ),
    data.DataStorage: (

        ('size', 'type', int),
        ('location', 'type', unicode),
        ('modification_date', 'type', datetime.datetime),
        ('format', 'type', unicode),

        ('size', 'cardinality', "0.1"),
        ('location', 'cardinality', "0.1"),
        ('modification_date', 'cardinality', "0.1"),
        ('format', 'cardinality', "0.1"),

    ),
    activity.SimulationRelationship: (

        ('direction', 'type', unicode),
        ('type', 'type', unicode),
        ('description', 'type', unicode),
        ('target', 'type', activity.SimulationRelationshipTarget),

        ('direction', 'cardinality', "1.1"),
        ('type', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('target', 'cardinality', "1.1"),

    ),
    software.ComponentLanguage: (

        ('name', 'type', unicode),
        ('properties', 'type', software.ComponentLanguageProperty),

        ('name', 'cardinality', "1.1"),
        ('properties', 'cardinality', "0.N"),

    ),
    software.ConnectionProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    shared.Citation: (

        ('title', 'type', unicode),
        ('organisation', 'type', unicode),
        ('collective_title', 'type', unicode),
        ('role', 'type', unicode),
        ('location', 'type', unicode),
        ('date', 'type', datetime.datetime),
        ('type', 'type', unicode),
        ('date_type', 'type', unicode),
        ('alternative_title', 'type', unicode),

        ('title', 'cardinality', "0.1"),
        ('organisation', 'cardinality', "0.1"),
        ('collective_title', 'cardinality', "0.1"),
        ('role', 'cardinality', "0.1"),
        ('location', 'cardinality', "0.1"),
        ('date', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('date_type', 'cardinality', "0.1"),
        ('alternative_title', 'cardinality', "0.1"),

    ),
    activity.Simulation: (

        ('inputs', 'type', software.Coupling),
        ('simulation_id', 'type', unicode),
        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('control_simulation', 'type', activity.Simulation),
        ('spinup_simulation', 'type', activity.Simulation),
        ('spinup_date_range', 'type', shared.ClosedDateRange),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('deployments', 'type', software.Deployment),
        ('restarts', 'type', data.DataObject),
        ('long_name', 'type', unicode),
        ('outputs', 'type', data.DataObject),
        ('authors', 'type', unicode),
        ('calendar', 'type', shared.Calendar),
        ('supports', 'type', activity.Experiment),
        ('conformances', 'type', activity.Conformance),
        ('projects', 'type', unicode),

        ('inputs', 'cardinality', "0.N"),
        ('simulation_id', 'cardinality', "0.1"),
        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('control_simulation', 'cardinality', "0.1"),
        ('spinup_simulation', 'cardinality', "0.1"),
        ('spinup_date_range', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('deployments', 'cardinality', "0.N"),
        ('restarts', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('outputs', 'cardinality', "0.N"),
        ('authors', 'cardinality', "0.1"),
        ('calendar', 'cardinality', "1.1"),
        ('supports', 'cardinality', "0.N"),
        ('conformances', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),

    ),
    data.DataExtentGeographical: (

        ('west', 'type', float),
        ('east', 'type', float),
        ('north', 'type', float),
        ('south', 'type', float),

        ('west', 'cardinality', "0.1"),
        ('east', 'cardinality', "0.1"),
        ('north', 'cardinality', "0.1"),
        ('south', 'cardinality', "0.1"),

    ),
    activity.NumericalRequirementOption: (

        ('sub_options', 'type', activity.NumericalRequirementOption),
        ('description', 'type', unicode),
        ('id', 'type', unicode),
        ('relationship', 'type', unicode),
        ('name', 'type', unicode),

        ('sub_options', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('relationship', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    shared.Machine: (

        ('processor_type', 'type', unicode),
        ('interconnect', 'type', unicode),
        ('name', 'type', unicode),
        ('cores_per_processor', 'type', int),
        ('system', 'type', unicode),
        ('vendor', 'type', unicode),
        ('libraries', 'type', unicode),
        ('operating_system', 'type', unicode),
        ('location', 'type', unicode),
        ('maximum_processors', 'type', int),
        ('type', 'type', unicode),
        ('description', 'type', unicode),

        ('processor_type', 'cardinality', "0.1"),
        ('interconnect', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('cores_per_processor', 'cardinality', "0.1"),
        ('system', 'cardinality', "0.1"),
        ('vendor', 'cardinality', "0.1"),
        ('libraries', 'cardinality', "0.N"),
        ('operating_system', 'cardinality', "0.1"),
        ('location', 'cardinality', "0.1"),
        ('maximum_processors', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    shared.DataSource: (

        ('purpose', 'type', unicode),

        ('purpose', 'cardinality', "0.1"),

    ),
    data.DataHierarchyLevel: (

        ('is_open', 'type', bool),
        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('is_open', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    software.StatisticalModelComponent: (

        ('funding_sources', 'type', unicode),
        ('version', 'type', unicode),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('is_embedded', 'type', bool),
        ('short_name', 'type', unicode),
        ('previous_version', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('deployments', 'type', software.Deployment),
        ('citations', 'type', shared.Citation),
        ('type', 'type', unicode),
        ('composition', 'type', software.Composition),
        ('coupling_framework', 'type', unicode),
        ('description', 'type', unicode),
        ('parent', 'type', software.Component),
        ('sub_components', 'type', software.Component),
        ('dependencies', 'type', software.EntryPoint),
        ('grid', 'type', grids.GridSpec),
        ('purpose', 'type', unicode),
        ('online_resource', 'type', unicode),
        ('timing', 'type', software.Timing),
        ('properties', 'type', software.ComponentProperty),
        ('types', 'type', unicode),
        ('language', 'type', software.ComponentLanguage),
        ('license', 'type', shared.License),
        ('release_date', 'type', datetime.datetime),
        ('code_access', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('version', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('is_embedded', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('previous_version', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('deployments', 'cardinality', "0.N"),
        ('citations', 'cardinality', "0.N"),
        ('type', 'cardinality', "0.1"),
        ('composition', 'cardinality', "0.1"),
        ('coupling_framework', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('parent', 'cardinality', "0.1"),
        ('sub_components', 'cardinality', "0.N"),
        ('dependencies', 'cardinality', "0.N"),
        ('grid', 'cardinality', "0.1"),
        ('purpose', 'cardinality', "0.1"),
        ('online_resource', 'cardinality', "0.1"),
        ('timing', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('types', 'cardinality', "1.N"),
        ('language', 'cardinality', "0.1"),
        ('license', 'cardinality', "0.1"),
        ('release_date', 'cardinality', "0.1"),
        ('code_access', 'cardinality', "0.1"),

    ),
    software.TimeTransformation: (

        ('description', 'type', unicode),
        ('mapping_type', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('mapping_type', 'cardinality', "1.1"),

    ),
    software.CouplingEndpoint: (

        ('instance_id', 'type', unicode),
        ('data_source', 'type', shared.DataSource),
        ('properties', 'type', software.CouplingProperty),

        ('instance_id', 'cardinality', "0.1"),
        ('data_source', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),

    ),
    software.Deployment: (

        ('executable_arguments', 'type', unicode),
        ('description', 'type', unicode),
        ('parallelisation', 'type', software.Parallelisation),
        ('deployment_date', 'type', datetime.datetime),
        ('platform', 'type', shared.Platform),
        ('executable_name', 'type', unicode),

        ('executable_arguments', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('parallelisation', 'cardinality', "0.1"),
        ('deployment_date', 'cardinality', "0.1"),
        ('platform', 'cardinality', "0.1"),
        ('executable_name', 'cardinality', "0.1"),

    ),
    shared.Standard: (

        ('version', 'type', unicode),
        ('description', 'type', unicode),
        ('name', 'type', unicode),

        ('version', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    shared.DocGenealogy: (

        ('relationships', 'type', shared.DocRelationship),

        ('relationships', 'cardinality', "0.N"),

    ),
    software.ModelComponent: (

        ('funding_sources', 'type', unicode),
        ('version', 'type', unicode),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('is_embedded', 'type', bool),
        ('short_name', 'type', unicode),
        ('previous_version', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('deployments', 'type', software.Deployment),
        ('citations', 'type', shared.Citation),
        ('type', 'type', unicode),
        ('composition', 'type', software.Composition),
        ('coupling_framework', 'type', unicode),
        ('description', 'type', unicode),
        ('parent', 'type', software.Component),
        ('sub_components', 'type', software.Component),
        ('dependencies', 'type', software.EntryPoint),
        ('grid', 'type', grids.GridSpec),
        ('purpose', 'type', unicode),
        ('online_resource', 'type', unicode),
        ('timing', 'type', software.Timing),
        ('properties', 'type', software.ComponentProperty),
        ('types', 'type', unicode),
        ('language', 'type', software.ComponentLanguage),
        ('license', 'type', shared.License),
        ('release_date', 'type', datetime.datetime),
        ('code_access', 'type', unicode),
        ('activity', 'type', activity.Activity),

        ('funding_sources', 'cardinality', "0.N"),
        ('version', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('is_embedded', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('previous_version', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('deployments', 'cardinality', "0.N"),
        ('citations', 'cardinality', "0.N"),
        ('type', 'cardinality', "0.1"),
        ('composition', 'cardinality', "0.1"),
        ('coupling_framework', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('parent', 'cardinality', "0.1"),
        ('sub_components', 'cardinality', "0.N"),
        ('dependencies', 'cardinality', "0.N"),
        ('grid', 'cardinality', "0.1"),
        ('purpose', 'cardinality', "0.1"),
        ('online_resource', 'cardinality', "0.1"),
        ('timing', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('types', 'cardinality', "1.N"),
        ('language', 'cardinality', "0.1"),
        ('license', 'cardinality', "0.1"),
        ('release_date', 'cardinality', "0.1"),
        ('code_access', 'cardinality', "0.1"),
        ('activity', 'cardinality', "0.1"),

    ),
    activity.NumericalExperiment: (

        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('generates', 'type', unicode),
        ('short_name', 'type', unicode),
        ('long_name', 'type', unicode),
        ('supports', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('measurement_campaigns', 'type', activity.MeasurementCampaign),
        ('meta', 'type', shared.DocMetaInfo),
        ('experiment_id', 'type', unicode),
        ('requirements', 'type', activity.NumericalRequirement),
        ('requires', 'type', activity.NumericalActivity),
        ('projects', 'type', unicode),
        ('description', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('generates', 'cardinality', "0.N"),
        ('short_name', 'cardinality', "1.1"),
        ('long_name', 'cardinality', "0.1"),
        ('supports', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('measurement_campaigns', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('experiment_id', 'cardinality', "0.1"),
        ('requirements', 'cardinality', "0.N"),
        ('requires', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),

    ),
    quality.Measure: (

        ('identification', 'type', unicode),
        ('name', 'type', unicode),
        ('description', 'type', unicode),

        ('identification', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    data.DataProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),
        ('description', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    activity.Conformance: (

        ('requirements', 'type', activity.NumericalRequirement),
        ('description', 'type', unicode),
        ('sources', 'type', shared.DataSource),
        ('frequency', 'type', unicode),
        ('is_conformant', 'type', bool),
        ('type', 'type', unicode),

        ('requirements', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('sources', 'cardinality', "0.N"),
        ('frequency', 'cardinality', "0.1"),
        ('is_conformant', 'cardinality', "1.1"),
        ('type', 'cardinality', "0.1"),

    ),
    data.DataStorageDb: (

        ('name', 'type', unicode),
        ('modification_date', 'type', datetime.datetime),
        ('format', 'type', unicode),
        ('location', 'type', unicode),
        ('owner', 'type', unicode),
        ('table', 'type', unicode),
        ('access_string', 'type', unicode),
        ('size', 'type', int),

        ('name', 'cardinality', "0.1"),
        ('modification_date', 'cardinality', "0.1"),
        ('format', 'cardinality', "0.1"),
        ('location', 'cardinality', "0.1"),
        ('owner', 'cardinality', "0.1"),
        ('table', 'cardinality', "0.1"),
        ('access_string', 'cardinality', "0.1"),
        ('size', 'cardinality', "0.1"),

    ),
    activity.MeasurementCampaign: (

        ('duration', 'type', int),
        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('projects', 'type', unicode),

        ('duration', 'cardinality', "1.1"),
        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),

    ),
    grids.SimpleGridGeometry: (

        ('dim_order', 'type', unicode),
        ('num_dims', 'type', int),
        ('xcoords', 'type', grids.CoordinateList),
        ('is_mesh', 'type', bool),
        ('ycoords', 'type', grids.CoordinateList),
        ('zcoords', 'type', grids.CoordinateList),

        ('dim_order', 'cardinality', "0.1"),
        ('num_dims', 'cardinality', "1.1"),
        ('xcoords', 'cardinality', "1.1"),
        ('is_mesh', 'cardinality', "0.1"),
        ('ycoords', 'cardinality', "1.1"),
        ('zcoords', 'cardinality', "0.1"),

    ),
    shared.Relationship: (

        ('direction', 'type', unicode),
        ('description', 'type', unicode),

        ('direction', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),

    ),
    shared.DocMetaInfo: (

        ('drs_keys', 'type', unicode),
        ('update_date', 'type', datetime.datetime),
        ('create_date', 'type', datetime.datetime),
        ('language', 'type', unicode),
        ('genealogy', 'type', shared.DocGenealogy),
        ('author', 'type', shared.ResponsibleParty),
        ('sort_key', 'type', unicode),
        ('drs_path', 'type', unicode),
        ('source_key', 'type', unicode),
        ('project', 'type', unicode),
        ('institute', 'type', unicode),
        ('version', 'type', int),
        ('status', 'type', unicode),
        ('source', 'type', unicode),
        ('type_sort_key', 'type', unicode),
        ('external_ids', 'type', shared.StandardName),
        ('type', 'type', unicode),
        ('id', 'type', uuid.UUID),
        ('type_display_name', 'type', unicode),

        ('drs_keys', 'cardinality', "0.N"),
        ('update_date', 'cardinality', "1.1"),
        ('create_date', 'cardinality', "1.1"),
        ('language', 'cardinality', "1.1"),
        ('genealogy', 'cardinality', "0.1"),
        ('author', 'cardinality', "0.1"),
        ('sort_key', 'cardinality', "0.1"),
        ('drs_path', 'cardinality', "0.1"),
        ('source_key', 'cardinality', "0.1"),
        ('project', 'cardinality', "1.1"),
        ('institute', 'cardinality', "0.1"),
        ('version', 'cardinality', "1.1"),
        ('status', 'cardinality', "0.1"),
        ('source', 'cardinality', "1.1"),
        ('type_sort_key', 'cardinality', "0.1"),
        ('external_ids', 'cardinality', "0.N"),
        ('type', 'cardinality', "1.1"),
        ('id', 'cardinality', "1.1"),
        ('type_display_name', 'cardinality', "0.1"),

        ('source', 'constant', "scripts"),
    ),
    data.DataContent: (

        ('topic', 'type', data.DataTopic),
        ('frequency', 'type', unicode),
        ('purpose', 'type', unicode),
        ('aggregation', 'type', unicode),

        ('topic', 'cardinality', "1.1"),
        ('frequency', 'cardinality', "0.1"),
        ('purpose', 'cardinality', "0.1"),
        ('aggregation', 'cardinality', "0.1"),

    ),
    shared.Daily360: (

        ('range', 'type', shared.DateRange),
        ('length', 'type', int),
        ('description', 'type', unicode),

        ('range', 'cardinality', "0.1"),
        ('length', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    activity.SimulationComposite: (

        ('funding_sources', 'type', unicode),
        ('child', 'type', activity.Simulation),
        ('rank', 'type', int),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('calendar', 'type', shared.Calendar),
        ('conformances', 'type', activity.Conformance),
        ('rationales', 'type', unicode),
        ('control_simulation', 'type', activity.Simulation),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('deployments', 'type', software.Deployment),
        ('restarts', 'type', data.DataObject),
        ('supports', 'type', activity.Experiment),
        ('inputs', 'type', software.Coupling),
        ('simulation_id', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('outputs', 'type', data.DataObject),
        ('spinup_date_range', 'type', shared.ClosedDateRange),
        ('date_range', 'type', shared.DateRange),
        ('authors', 'type', unicode),
        ('projects', 'type', unicode),
        ('spinup_simulation', 'type', activity.Simulation),

        ('funding_sources', 'cardinality', "0.N"),
        ('child', 'cardinality', "0.N"),
        ('rank', 'cardinality', "1.1"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('calendar', 'cardinality', "1.1"),
        ('conformances', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('control_simulation', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('deployments', 'cardinality', "0.N"),
        ('restarts', 'cardinality', "0.N"),
        ('supports', 'cardinality', "0.N"),
        ('inputs', 'cardinality', "0.N"),
        ('simulation_id', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('outputs', 'cardinality', "0.N"),
        ('spinup_date_range', 'cardinality', "0.1"),
        ('date_range', 'cardinality', "1.1"),
        ('authors', 'cardinality', "0.1"),
        ('projects', 'cardinality', "0.N"),
        ('spinup_simulation', 'cardinality', "0.1"),

    ),
    activity.DownscalingSimulation: (

        ('inputs', 'type', software.Coupling),
        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('outputs', 'type', data.DataObject),
        ('downscaling_type', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('long_name', 'type', unicode),
        ('downscaled_from', 'type', shared.DataSource),
        ('meta', 'type', shared.DocMetaInfo),
        ('downscaling_id', 'type', unicode),
        ('calendar', 'type', shared.Calendar),
        ('supports', 'type', activity.Experiment),
        ('projects', 'type', unicode),

        ('inputs', 'cardinality', "0.N"),
        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('outputs', 'cardinality', "0.N"),
        ('downscaling_type', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('downscaled_from', 'cardinality', "1.1"),
        ('meta', 'cardinality', "1.1"),
        ('downscaling_id', 'cardinality', "0.1"),
        ('calendar', 'cardinality', "1.1"),
        ('supports', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),

    ),
    data.DataStorageFile: (

        ('modification_date', 'type', datetime.datetime),
        ('format', 'type', unicode),
        ('file_name', 'type', unicode),
        ('location', 'type', unicode),
        ('path', 'type', unicode),
        ('file_system', 'type', unicode),
        ('size', 'type', int),

        ('modification_date', 'cardinality', "0.1"),
        ('format', 'cardinality', "0.1"),
        ('file_name', 'cardinality', "0.1"),
        ('location', 'cardinality', "0.1"),
        ('path', 'cardinality', "0.1"),
        ('file_system', 'cardinality', "0.1"),
        ('size', 'cardinality', "0.1"),

    ),
    software.Composition: (

        ('couplings', 'type', unicode),
        ('description', 'type', unicode),

        ('couplings', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),

    ),
    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------


    (shared.MachineCompilerUnit, 'compilers'): (

        ('type', shared.Compiler),

        ('cardinality', "0.N"),

    ),
    (shared.MachineCompilerUnit, 'machine'): (

        ('type', shared.Machine),

        ('cardinality', "1.1"),

    ),

    (software.Coupling, 'priming'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'connections'): (

        ('type', software.Connection),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'transformers'): (

        ('type', software.ProcessorComponent),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'spatial_regriddings'): (

        ('type', software.SpatialRegridding),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'is_fully_specified'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (software.Coupling, 'time_profile'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'properties'): (

        ('type', software.CouplingProperty),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'target'): (

        ('type', software.CouplingEndpoint),

        ('cardinality', "1.1"),

    ),
    (software.Coupling, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'sources'): (

        ('type', software.CouplingEndpoint),

        ('cardinality', "1.N"),

    ),
    (software.Coupling, 'time_lag'): (

        ('type', software.TimeLag),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'purpose'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.Coupling, 'time_transformation'): (

        ('type', software.TimeTransformation),

        ('cardinality', "0.1"),

    ),

    (activity.Experiment, 'supports'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'measurement_campaigns'): (

        ('type', activity.MeasurementCampaign),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'requires'): (

        ('type', activity.NumericalActivity),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'generates'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),

    (shared.Change, 'details'): (

        ('type', shared.ChangeProperty),

        ('cardinality', "1.N"),

    ),
    (shared.Change, 'date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.Change, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Change, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Change, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Change, 'author'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.1"),

    ),

    (software.Timing, 'rate'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (software.Timing, 'start'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.Timing, 'is_variable_rate'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.Timing, 'units'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Timing, 'end'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),

    (data.DataRestriction, 'restriction'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataRestriction, 'scope'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataRestriction, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),

    (software.EntryPoint, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.OutputRequirement, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.OutputRequirement, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.OutputRequirement, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.OutputRequirement, 'options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.OutputRequirement, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (activity.OutputRequirement, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "outputRequirement"),
    ),

    (quality.CimQuality, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (quality.CimQuality, 'reports'): (

        ('type', quality.Report),

        ('cardinality', "0.N"),

    ),

    (shared.OpenDateRange, 'end'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.OpenDateRange, 'duration'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.OpenDateRange, 'start'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),

    (grids.GridProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.DateRange, 'duration'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (grids.VerticalCoordinateList, 'has_constant_offset'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.VerticalCoordinateList, 'form'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.VerticalCoordinateList, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.VerticalCoordinateList, 'uom'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.VerticalCoordinateList, 'properties'): (

        ('type', grids.GridProperty),

        ('cardinality', "0.N"),

    ),
    (grids.VerticalCoordinateList, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.ChangeProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ChangeProperty, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ChangeProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ChangeProperty, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.ProcessorComponent, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (software.ProcessorComponent, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.RealCalendar, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.RealCalendar, 'range'): (

        ('type', shared.DateRange),

        ('cardinality', "0.1"),

    ),
    (shared.RealCalendar, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (activity.LateralBoundaryCondition, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.LateralBoundaryCondition, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.LateralBoundaryCondition, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.LateralBoundaryCondition, 'options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.LateralBoundaryCondition, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (activity.LateralBoundaryCondition, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "lateralBoundaryCondition"),
    ),

    (activity.InitialCondition, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.InitialCondition, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.InitialCondition, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.InitialCondition, 'options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.InitialCondition, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (activity.InitialCondition, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "initialCondition"),
    ),

    (data.DataDistribution, 'access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataDistribution, 'fee'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataDistribution, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataDistribution, 'responsible_party'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.1"),

    ),

    (grids.GridExtent, 'maximum_latitude'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridExtent, 'maximum_longitude'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridExtent, 'minimum_latitude'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridExtent, 'units'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridExtent, 'minimum_longitude'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (software.SpatialRegriddingUserMethod, 'file'): (

        ('type', data.DataObject),

        ('cardinality', "0.1"),

    ),
    (software.SpatialRegriddingUserMethod, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (quality.Evaluation, 'specification_hyperlink'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'explanation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'did_pass'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'type_hyperlink'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'specification'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.ExperimentRelationship, 'direction'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.ExperimentRelationship, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.ExperimentRelationship, 'target'): (

        ('type', activity.ExperimentRelationshipTarget),

        ('cardinality', "1.1"),

    ),
    (activity.ExperimentRelationship, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (data.DataExtentTemporal, 'begin'): (

        ('type', datetime.date),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentTemporal, 'end'): (

        ('type', datetime.date),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentTemporal, 'time_interval'): (

        ('type', data.DataExtentTimeInterval),

        ('cardinality', "0.1"),

    ),

    (software.ComponentLanguageProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentLanguageProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.NumericalRequirement, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirement, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalRequirement, 'options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalRequirement, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalRequirement, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirement, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.SpatialRegriddingProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SpatialRegriddingProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.ComponentProperty, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.ComponentProperty, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'grid'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'intent'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'values'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'sub_properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'standard_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'units'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'is_represented'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),

    (shared.ClosedDateRange, 'duration'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ClosedDateRange, 'end'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.ClosedDateRange, 'start'): (

        ('type', datetime.datetime),

        ('cardinality', "1.1"),

    ),

    (grids.GridSpec, 'esm_exchange_grids'): (

        ('type', grids.GridMosaic),

        ('cardinality', "0.N"),

    ),
    (grids.GridSpec, 'esm_model_grids'): (

        ('type', grids.GridMosaic),

        ('cardinality', "0.N"),

    ),
    (grids.GridSpec, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),

    (activity.SimulationRelationshipTarget, 'simulation'): (

        ('type', shared.DocReference),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRelationshipTarget, 'target'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.Component, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (activity.EnsembleMember, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'ensemble'): (

        ('type', activity.Ensemble),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'ensemble_ids'): (

        ('type', shared.StandardName),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (software.SpatialRegridding, 'properties'): (

        ('type', software.SpatialRegriddingProperty),

        ('cardinality', "0.N"),

    ),
    (software.SpatialRegridding, 'dimension'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SpatialRegridding, 'user_method'): (

        ('type', software.SpatialRegriddingUserMethod),

        ('cardinality', "0.1"),

    ),
    (software.SpatialRegridding, 'standard_method'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.SpatioTemporalConstraint, 'spatial_resolution'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "spatioTemporalConstraint"),
    ),
    (activity.SpatioTemporalConstraint, 'options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.SpatioTemporalConstraint, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.SpatioTemporalConstraint, 'date_range'): (

        ('type', shared.DateRange),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.PerpetualPeriod, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.PerpetualPeriod, 'range'): (

        ('type', shared.DateRange),

        ('cardinality', "0.1"),

    ),
    (shared.PerpetualPeriod, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (grids.GridTileResolutionType, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTileResolutionType, 'properties'): (

        ('type', grids.GridProperty),

        ('cardinality', "0.N"),

    ),

    (software.TimeLag, 'units'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.TimeLag, 'value'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (activity.BoundaryCondition, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.BoundaryCondition, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.BoundaryCondition, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.BoundaryCondition, 'options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.BoundaryCondition, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (activity.BoundaryCondition, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "boundaryCondition"),
    ),

    (misc.DocumentSet, 'model'): (

        ('type', software.ModelComponent),

        ('cardinality', "0.1"),

    ),
    (misc.DocumentSet, 'ensembles'): (

        ('type', activity.Ensemble),

        ('cardinality', "0.N"),

    ),
    (misc.DocumentSet, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (misc.DocumentSet, 'platform'): (

        ('type', shared.Platform),

        ('cardinality', "0.1"),

    ),
    (misc.DocumentSet, 'grids'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.N"),

    ),
    (misc.DocumentSet, 'experiment'): (

        ('type', activity.NumericalExperiment),

        ('cardinality', "0.1"),

    ),
    (misc.DocumentSet, 'simulation'): (

        ('type', activity.SimulationRun),

        ('cardinality', "0.1"),

    ),
    (misc.DocumentSet, 'data'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),

    (data.DataStorageIp, 'size'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'file_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'protocol'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'modification_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'host'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'path'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.Parallelisation, 'processes'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (software.Parallelisation, 'ranks'): (

        ('type', software.Rank),

        ('cardinality', "0.N"),

    ),

    (activity.ExperimentRelationshipTarget, 'numerical_experiment'): (

        ('type', activity.NumericalExperiment),

        ('cardinality', "0.1"),

    ),

    (activity.NumericalActivity, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalActivity, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalActivity, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.ConnectionEndpoint, 'instance_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ConnectionEndpoint, 'data_source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (software.ConnectionEndpoint, 'properties'): (

        ('type', software.ConnectionProperty),

        ('cardinality', "0.N"),

    ),

    (shared.Calendar, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Calendar, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.Calendar, 'range'): (

        ('type', shared.DateRange),

        ('cardinality', "0.1"),

    ),

    (grids.GridMosaic, 'mosaic_count'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (grids.GridMosaic, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridMosaic, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'mosaics'): (

        ('type', grids.GridMosaic),

        ('cardinality', "0.N"),

    ),
    (grids.GridMosaic, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridMosaic, 'has_congruent_tiles'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'is_leaf'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (grids.GridMosaic, 'tiles'): (

        ('type', grids.GridTile),

        ('cardinality', "0.N"),

    ),
    (grids.GridMosaic, 'mnemonic'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'tile_count'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'extent'): (

        ('type', grids.GridExtent),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (grids.CoordinateList, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.CoordinateList, 'uom'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.CoordinateList, 'has_constant_offset'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),

    (data.DataExtentTimeInterval, 'radix'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentTimeInterval, 'factor'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentTimeInterval, 'unit'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.StandardName, 'standards'): (

        ('type', shared.Standard),

        ('cardinality', "0.N"),

    ),
    (shared.StandardName, 'is_open'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (shared.StandardName, 'value'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (activity.Ensemble, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'outputs'): (

        ('type', shared.DataSource),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.Ensemble, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'members'): (

        ('type', activity.EnsembleMember),

        ('cardinality', "1.N"),

    ),
    (activity.Ensemble, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'types'): (

        ('type', unicode),

        ('cardinality', "1.N"),

    ),
    (activity.Ensemble, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (activity.SimulationRun, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRun, 'date_range'): (

        ('type', shared.DateRange),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRun, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'control_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'model'): (

        ('type', software.ModelComponent),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'spinup_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRun, 'spinup_date_range'): (

        ('type', shared.ClosedDateRange),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'outputs'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'restarts'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'authors'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'simulation_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),

    (shared.DocRelationship, 'target'): (

        ('type', shared.DocRelationshipTarget),

        ('cardinality', "1.1"),

    ),
    (shared.DocRelationship, 'direction'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocRelationship, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocRelationship, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (data.DataExtent, 'geographical'): (

        ('type', data.DataExtentGeographical),

        ('cardinality', "1.1"),

    ),
    (data.DataExtent, 'temporal'): (

        ('type', data.DataExtentTemporal),

        ('cardinality', "1.1"),

    ),

    (shared.Compiler, 'language'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Compiler, 'version'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Compiler, 'options'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Compiler, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Compiler, 'environment_variables'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Compiler, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Platform, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Platform, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (shared.Platform, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Platform, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Platform, 'units'): (

        ('type', shared.MachineCompilerUnit),

        ('cardinality', "1.N"),

    ),
    (shared.Platform, 'contacts'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (software.Rank, 'max'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (software.Rank, 'value'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (software.Rank, 'min'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (software.Rank, 'increment'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (shared.Property, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Property, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.DocRelationshipTarget, 'reference'): (

        ('type', shared.DocReference),

        ('cardinality', "0.1"),

    ),

    (activity.PhysicalModification, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.PhysicalModification, 'frequency'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.PhysicalModification, 'sources'): (

        ('type', shared.DataSource),

        ('cardinality', "0.N"),

    ),
    (activity.PhysicalModification, 'is_conformant'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (activity.PhysicalModification, 'requirements'): (

        ('type', activity.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (activity.PhysicalModification, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.Connection, 'priming'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'sources'): (

        ('type', software.ConnectionEndpoint),

        ('cardinality', "0.N"),

    ),
    (software.Connection, 'time_transformation'): (

        ('type', software.TimeTransformation),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'spatial_regridding'): (

        ('type', software.SpatialRegridding),

        ('cardinality', "0.N"),

    ),
    (software.Connection, 'time_profile'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'transformers'): (

        ('type', software.ProcessorComponent),

        ('cardinality', "0.N"),

    ),
    (software.Connection, 'target'): (

        ('type', software.ConnectionEndpoint),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'time_lag'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'properties'): (

        ('type', software.ConnectionProperty),

        ('cardinality', "0.N"),

    ),

    (grids.GridTile, 'horizontal_crs'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'zcoords'): (

        ('type', grids.VerticalCoordinateList),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'horizontal_resolution'): (

        ('type', grids.GridTileResolutionType),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'extent'): (

        ('type', grids.GridExtent),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'nx'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'discretization_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'simple_grid_geom'): (

        ('type', grids.SimpleGridGeometry),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'vertical_resolution'): (

        ('type', grids.GridTileResolutionType),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'area'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'is_conformal'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'mnemonic'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'cell_array'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'is_regular'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'refinement_scheme'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'short_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'cell_ref_array'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'is_terrain_following'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'nz'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'vertical_crs'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'coord_file'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'is_uniform'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'grid_north_pole'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'coordinate_pole'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'geometry_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'ny'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (shared.DocReference, 'id'): (

        ('type', uuid.UUID),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'changes'): (

        ('type', shared.Change),

        ('cardinality', "0.N"),

    ),
    (shared.DocReference, 'url'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'version'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'external_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.ResponsibleParty, 'address'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'individual_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'email'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'abbreviation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'url'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'organisation_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'role'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (data.DataTopic, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataTopic, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataTopic, 'unit'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.License, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.License, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.License, 'is_unrestricted'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (shared.License, 'contact'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.Activity, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.Activity, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Activity, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Activity, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),

    (data.DataObject, 'storage'): (

        ('type', data.DataStorage),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'hierarchy_level'): (

        ('type', data.DataHierarchyLevel),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'keyword'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'content'): (

        ('type', data.DataContent),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'source_simulation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'parent_object'): (

        ('type', data.DataObject),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'data_status'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'child_object'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'properties'): (

        ('type', data.DataProperty),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'restriction'): (

        ('type', data.DataRestriction),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'distribution'): (

        ('type', data.DataDistribution),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (data.DataObject, 'extent'): (

        ('type', data.DataExtent),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'acronym'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'geometry_model'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.CouplingProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.CouplingProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (quality.Report, 'date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (quality.Report, 'evaluation'): (

        ('type', quality.Evaluation),

        ('cardinality', "1.1"),

    ),
    (quality.Report, 'evaluator'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.1"),

    ),
    (quality.Report, 'measure'): (

        ('type', quality.Measure),

        ('cardinality', "1.1"),

    ),

    (data.DataStorage, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorage, 'size'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.DataStorage, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorage, 'modification_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),

    (activity.SimulationRelationship, 'direction'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRelationship, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRelationship, 'target'): (

        ('type', activity.SimulationRelationshipTarget),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRelationship, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (software.ComponentLanguage, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.ComponentLanguage, 'properties'): (

        ('type', software.ComponentLanguageProperty),

        ('cardinality', "0.N"),

    ),

    (software.ConnectionProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ConnectionProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Citation, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'collective_title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'organisation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'date_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'role'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'alternative_title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.Simulation, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'spinup_date_range'): (

        ('type', shared.ClosedDateRange),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "1.1"),

    ),
    (activity.Simulation, 'control_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'restarts'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'spinup_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'authors'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'simulation_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'outputs'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (data.DataExtentGeographical, 'east'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentGeographical, 'north'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentGeographical, 'west'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentGeographical, 'south'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),

    (activity.NumericalRequirementOption, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirementOption, 'sub_options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalRequirementOption, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalRequirementOption, 'relationship'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirementOption, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Machine, 'system'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'libraries'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (shared.Machine, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'interconnect'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'maximum_processors'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'vendor'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Machine, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'processor_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'cores_per_processor'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'operating_system'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.DataSource, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (data.DataHierarchyLevel, 'is_open'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (data.DataHierarchyLevel, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataHierarchyLevel, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.StatisticalModelComponent, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (software.StatisticalModelComponent, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'types'): (

        ('type', unicode),

        ('cardinality', "1.N"),

    ),
    (software.StatisticalModelComponent, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.StatisticalModelComponent, 'timing'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.TimeTransformation, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.TimeTransformation, 'mapping_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (software.CouplingEndpoint, 'data_source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (software.CouplingEndpoint, 'instance_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.CouplingEndpoint, 'properties'): (

        ('type', software.CouplingProperty),

        ('cardinality', "0.N"),

    ),

    (software.Deployment, 'parallelisation'): (

        ('type', software.Parallelisation),

        ('cardinality', "0.1"),

    ),
    (software.Deployment, 'deployment_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.Deployment, 'executable_arguments'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.Deployment, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Deployment, 'executable_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Deployment, 'platform'): (

        ('type', shared.Platform),

        ('cardinality', "0.1"),

    ),

    (shared.Standard, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Standard, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Standard, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.DocGenealogy, 'relationships'): (

        ('type', shared.DocRelationship),

        ('cardinality', "0.N"),

    ),

    (software.ModelComponent, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'activity'): (

        ('type', activity.Activity),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (software.ModelComponent, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'types'): (

        ('type', unicode),

        ('cardinality', "1.N"),

    ),
    (software.ModelComponent, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'timing'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (activity.NumericalExperiment, 'supports'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalExperiment, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'generates'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalExperiment, 'experiment_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalExperiment, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalExperiment, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalExperiment, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'requires'): (

        ('type', activity.NumericalActivity),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'requirements'): (

        ('type', activity.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'measurement_campaigns'): (

        ('type', activity.MeasurementCampaign),

        ('cardinality', "0.N"),

    ),

    (quality.Measure, 'identification'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Measure, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Measure, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (data.DataProperty, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.Conformance, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'requirements'): (

        ('type', activity.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (activity.Conformance, 'sources'): (

        ('type', shared.DataSource),

        ('cardinality', "0.N"),

    ),
    (activity.Conformance, 'is_conformant'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (activity.Conformance, 'frequency'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (data.DataStorageDb, 'table'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'size'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'access_string'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'owner'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'modification_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),

    (activity.MeasurementCampaign, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.MeasurementCampaign, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.MeasurementCampaign, 'duration'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (activity.MeasurementCampaign, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.MeasurementCampaign, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),

    (grids.SimpleGridGeometry, 'is_mesh'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.SimpleGridGeometry, 'xcoords'): (

        ('type', grids.CoordinateList),

        ('cardinality', "1.1"),

    ),
    (grids.SimpleGridGeometry, 'num_dims'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (grids.SimpleGridGeometry, 'dim_order'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.SimpleGridGeometry, 'ycoords'): (

        ('type', grids.CoordinateList),

        ('cardinality', "1.1"),

    ),
    (grids.SimpleGridGeometry, 'zcoords'): (

        ('type', grids.CoordinateList),

        ('cardinality', "0.1"),

    ),

    (shared.Relationship, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Relationship, 'direction'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.DocMetaInfo, 'version'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'sort_key'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'drs_keys'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (shared.DocMetaInfo, 'institute'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'external_ids'): (

        ('type', shared.StandardName),

        ('cardinality', "0.N"),

    ),
    (shared.DocMetaInfo, 'update_date'): (

        ('type', datetime.datetime),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'status'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'id'): (

        ('type', uuid.UUID),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'type_sort_key'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'type_display_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'genealogy'): (

        ('type', shared.DocGenealogy),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'author'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'language'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'create_date'): (

        ('type', datetime.datetime),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'source'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "scripts"),
    ),
    (shared.DocMetaInfo, 'project'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'drs_path'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'source_key'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (data.DataContent, 'aggregation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataContent, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataContent, 'topic'): (

        ('type', data.DataTopic),

        ('cardinality', "1.1"),

    ),
    (data.DataContent, 'frequency'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Daily360, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Daily360, 'range'): (

        ('type', shared.DateRange),

        ('cardinality', "0.1"),

    ),
    (shared.Daily360, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (activity.SimulationComposite, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'spinup_date_range'): (

        ('type', shared.ClosedDateRange),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'date_range'): (

        ('type', shared.DateRange),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'spinup_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'rank'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'outputs'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'restarts'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'control_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'authors'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'simulation_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'child'): (

        ('type', activity.Simulation),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.DownscalingSimulation, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.DownscalingSimulation, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.DownscalingSimulation, 'outputs'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'downscaling_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.DownscalingSimulation, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'downscaling_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.DownscalingSimulation, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.DownscalingSimulation, 'downscaled_from'): (

        ('type', shared.DataSource),

        ('cardinality', "1.1"),

    ),
    (activity.DownscalingSimulation, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.DownscalingSimulation, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "1.1"),

    ),

    (data.DataStorageFile, 'size'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'modification_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'file_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'path'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'file_system'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.Composition, 'couplings'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.Composition, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
}

# Count of class constraints.
TOTAL_CONSTRAINTS = sum(len(CONSTRAINTS[c]) for c in CLASSES)
