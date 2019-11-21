
"""
.. module:: cim.v1.type_info.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
from collections import defaultdict
import datetime
import uuid


import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_grids_package as grids
import typeset_for_misc_package as misc
import typeset_for_quality_package as quality
import typeset_for_shared_package as shared
import typeset_for_software_package as software



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
    'CONSTRAINTS',
    'KEYS',
    'DOC_STRINGS'
    ]

# Supported packages.
PACKAGES = (
    activity,
    data,
    grids,
    misc,
    quality,
    shared,
    software,
)

# ------------------------------------------------
# Classes.
# ------------------------------------------------

# Supported classes.
CLASSES = (
    activity.Activity,
    activity.BoundaryCondition,
    activity.Conformance,
    activity.DownscalingSimulation,
    activity.Ensemble,
    activity.EnsembleMember,
    activity.Experiment,
    activity.ExperimentRelationship,
    activity.ExperimentRelationshipTarget,
    activity.InitialCondition,
    activity.LateralBoundaryCondition,
    activity.MeasurementCampaign,
    activity.NumericalActivity,
    activity.NumericalExperiment,
    activity.NumericalRequirement,
    activity.NumericalRequirementOption,
    activity.OutputRequirement,
    activity.PhysicalModification,
    activity.Simulation,
    activity.SimulationComposite,
    activity.SimulationRelationship,
    activity.SimulationRelationshipTarget,
    activity.SimulationRun,
    activity.SpatioTemporalConstraint,
    data.DataContent,
    data.DataDistribution,
    data.DataExtent,
    data.DataExtentGeographical,
    data.DataExtentTemporal,
    data.DataExtentTimeInterval,
    data.DataHierarchyLevel,
    data.DataObject,
    data.DataProperty,
    data.DataRestriction,
    data.DataStorage,
    data.DataStorageDb,
    data.DataStorageFile,
    data.DataStorageIp,
    data.DataTopic,
    grids.CoordinateList,
    grids.GridExtent,
    grids.GridMosaic,
    grids.GridProperty,
    grids.GridSpec,
    grids.GridTile,
    grids.GridTileResolutionType,
    grids.SimpleGridGeometry,
    grids.VerticalCoordinateList,
    misc.DocumentSet,
    quality.CimQuality,
    quality.Evaluation,
    quality.Measure,
    quality.Report,
    shared.Calendar,
    shared.Change,
    shared.ChangeProperty,
    shared.Citation,
    shared.ClosedDateRange,
    shared.Compiler,
    shared.Daily360,
    shared.DataSource,
    shared.DateRange,
    shared.DocMetaInfo,
    shared.DocReference,
    shared.License,
    shared.Machine,
    shared.MachineCompilerUnit,
    shared.OpenDateRange,
    shared.PerpetualPeriod,
    shared.Platform,
    shared.Property,
    shared.RealCalendar,
    shared.Relationship,
    shared.ResponsibleParty,
    shared.Standard,
    shared.StandardName,
    software.Component,
    software.ComponentLanguage,
    software.ComponentLanguageProperty,
    software.ComponentProperty,
    software.Composition,
    software.Connection,
    software.ConnectionEndpoint,
    software.ConnectionProperty,
    software.Coupling,
    software.CouplingEndpoint,
    software.CouplingProperty,
    software.Deployment,
    software.EntryPoint,
    software.ModelComponent,
    software.Parallelisation,
    software.ProcessorComponent,
    software.Rank,
    software.SpatialRegridding,
    software.SpatialRegriddingProperty,
    software.SpatialRegriddingUserMethod,
    software.StatisticalModelComponent,
    software.TimeLag,
    software.TimeTransformation,
    software.Timing,
)

# Supported class properties.
CLASS_PROPERTIES = { 
    activity.Activity: (
        'funding_sources',
        'projects',
        'rationales',
        'responsible_parties',
    ),
    activity.BoundaryCondition: (
        'description',
        'id',
        'name',
        'options',
        'requirement_type',
        'source',
    ),
    activity.Conformance: (
        'description',
        'frequency',
        'is_conformant',
        'requirements',
        'sources',
        'type',
    ),
    activity.DownscalingSimulation: (
        'calendar',
        'downscaled_from',
        'downscaling_id',
        'downscaling_type',
        'inputs',
        'meta',
        'outputs',
        'description',
        'long_name',
        'short_name',
        'supports',
        'funding_sources',
        'projects',
        'rationales',
        'responsible_parties',
    ),
    activity.Ensemble: (
        'members',
        'meta',
        'outputs',
        'types',
        'description',
        'long_name',
        'short_name',
        'supports',
        'funding_sources',
        'projects',
        'rationales',
        'responsible_parties',
    ),
    activity.EnsembleMember: (
        'ensemble',
        'ensemble_ids',
        'simulation',
        'description',
        'long_name',
        'short_name',
        'supports',
        'funding_sources',
        'projects',
        'rationales',
        'responsible_parties',
    ),
    activity.Experiment: (
        'generates',
        'measurement_campaigns',
        'requires',
        'supports',
        'funding_sources',
        'projects',
        'rationales',
        'responsible_parties',
    ),
    activity.ExperimentRelationship: (
        'target',
        'type',
        'description',
    ),
    activity.ExperimentRelationshipTarget: (
        'numerical_experiment',
    ),
    activity.InitialCondition: (
        'description',
        'id',
        'name',
        'options',
        'requirement_type',
        'source',
    ),
    activity.LateralBoundaryCondition: (
        'description',
        'id',
        'name',
        'options',
        'requirement_type',
        'source',
    ),
    activity.MeasurementCampaign: (
        'duration',
        'funding_sources',
        'projects',
        'rationales',
        'responsible_parties',
    ),
    activity.NumericalActivity: (
        'description',
        'long_name',
        'short_name',
        'supports',
        'funding_sources',
        'projects',
        'rationales',
        'responsible_parties',
    ),
    activity.NumericalExperiment: (
        'description',
        'experiment_id',
        'long_name',
        'meta',
        'requirements',
        'short_name',
        'generates',
        'measurement_campaigns',
        'requires',
        'supports',
        'funding_sources',
        'projects',
        'rationales',
        'responsible_parties',
    ),
    activity.NumericalRequirement: (
        'description',
        'id',
        'name',
        'options',
        'requirement_type',
        'source',
    ),
    activity.NumericalRequirementOption: (
        'description',
        'id',
        'name',
        'relationship',
        'sub_options',
    ),
    activity.OutputRequirement: (
        'description',
        'id',
        'name',
        'options',
        'requirement_type',
        'source',
    ),
    activity.PhysicalModification: (
        'description',
        'frequency',
        'is_conformant',
        'requirements',
        'sources',
        'type',
    ),
    activity.Simulation: (
        'authors',
        'calendar',
        'conformances',
        'control_simulation',
        'deployments',
        'inputs',
        'outputs',
        'restarts',
        'simulation_id',
        'spinup_date_range',
        'spinup_simulation',
        'description',
        'long_name',
        'short_name',
        'supports',
        'funding_sources',
        'projects',
        'rationales',
        'responsible_parties',
    ),
    activity.SimulationComposite: (
        'child',
        'date_range',
        'meta',
        'rank',
        'authors',
        'calendar',
        'conformances',
        'control_simulation',
        'deployments',
        'inputs',
        'outputs',
        'restarts',
        'simulation_id',
        'spinup_date_range',
        'spinup_simulation',
        'description',
        'long_name',
        'short_name',
        'supports',
        'funding_sources',
        'projects',
        'rationales',
        'responsible_parties',
    ),
    activity.SimulationRelationship: (
        'target',
        'type',
        'description',
    ),
    activity.SimulationRelationshipTarget: (
        'simulation',
        'target',
    ),
    activity.SimulationRun: (
        'date_range',
        'meta',
        'model',
        'authors',
        'calendar',
        'conformances',
        'control_simulation',
        'deployments',
        'inputs',
        'outputs',
        'restarts',
        'simulation_id',
        'spinup_date_range',
        'spinup_simulation',
        'description',
        'long_name',
        'short_name',
        'supports',
        'funding_sources',
        'projects',
        'rationales',
        'responsible_parties',
    ),
    activity.SpatioTemporalConstraint: (
        'date_range',
        'spatial_resolution',
        'description',
        'id',
        'name',
        'options',
        'requirement_type',
        'source',
    ),
    data.DataContent: (
        'aggregation',
        'frequency',
        'topic',
        'purpose',
    ),
    data.DataDistribution: (
        'access',
        'fee',
        'format',
        'responsible_party',
    ),
    data.DataExtent: (
        'geographical',
        'temporal',
    ),
    data.DataExtentGeographical: (
        'east',
        'north',
        'south',
        'west',
    ),
    data.DataExtentTemporal: (
        'begin',
        'end',
        'time_interval',
    ),
    data.DataExtentTimeInterval: (
        'factor',
        'radix',
        'unit',
    ),
    data.DataHierarchyLevel: (
        'is_open',
        'name',
        'value',
    ),
    data.DataObject: (
        'acronym',
        'child_object',
        'citations',
        'content',
        'data_status',
        'description',
        'distribution',
        'extent',
        'geometry_model',
        'hierarchy_level',
        'keyword',
        'meta',
        'parent_object',
        'properties',
        'purpose',
        'restriction',
        'source_simulation',
        'storage',
        'purpose',
    ),
    data.DataProperty: (
        'description',
        'name',
        'value',
    ),
    data.DataRestriction: (
        'license',
        'restriction',
        'scope',
    ),
    data.DataStorage: (
        'format',
        'location',
        'modification_date',
        'size',
    ),
    data.DataStorageDb: (
        'access_string',
        'name',
        'owner',
        'table',
        'format',
        'location',
        'modification_date',
        'size',
    ),
    data.DataStorageFile: (
        'file_name',
        'file_system',
        'path',
        'format',
        'location',
        'modification_date',
        'size',
    ),
    data.DataStorageIp: (
        'file_name',
        'host',
        'path',
        'protocol',
        'format',
        'location',
        'modification_date',
        'size',
    ),
    data.DataTopic: (
        'description',
        'name',
        'unit',
    ),
    grids.CoordinateList: (
        'has_constant_offset',
        'length',
        'uom',
    ),
    grids.GridExtent: (
        'maximum_latitude',
        'maximum_longitude',
        'minimum_latitude',
        'minimum_longitude',
        'units',
    ),
    grids.GridMosaic: (
        'citations',
        'description',
        'extent',
        'has_congruent_tiles',
        'id',
        'is_leaf',
        'long_name',
        'mnemonic',
        'mosaic_count',
        'mosaics',
        'short_name',
        'tile_count',
        'tiles',
        'type',
    ),
    grids.GridProperty: (
        'name',
        'value',
    ),
    grids.GridSpec: (
        'esm_exchange_grids',
        'esm_model_grids',
        'meta',
    ),
    grids.GridTile: (
        'area',
        'cell_array',
        'cell_ref_array',
        'coord_file',
        'coordinate_pole',
        'description',
        'discretization_type',
        'extent',
        'geometry_type',
        'grid_north_pole',
        'horizontal_crs',
        'horizontal_resolution',
        'id',
        'is_conformal',
        'is_regular',
        'is_terrain_following',
        'is_uniform',
        'long_name',
        'mnemonic',
        'nx',
        'ny',
        'nz',
        'refinement_scheme',
        'short_name',
        'simple_grid_geom',
        'vertical_crs',
        'vertical_resolution',
        'zcoords',
    ),
    grids.GridTileResolutionType: (
        'description',
        'properties',
    ),
    grids.SimpleGridGeometry: (
        'dim_order',
        'is_mesh',
        'num_dims',
        'xcoords',
        'ycoords',
        'zcoords',
    ),
    grids.VerticalCoordinateList: (
        'form',
        'properties',
        'type',
        'has_constant_offset',
        'length',
        'uom',
    ),
    misc.DocumentSet: (
        'data',
        'ensembles',
        'experiment',
        'grids',
        'meta',
        'model',
        'platform',
        'simulation',
    ),
    quality.CimQuality: (
        'meta',
        'reports',
    ),
    quality.Evaluation: (
        'date',
        'description',
        'did_pass',
        'explanation',
        'specification',
        'specification_hyperlink',
        'title',
        'type',
        'type_hyperlink',
    ),
    quality.Measure: (
        'description',
        'identification',
        'name',
    ),
    quality.Report: (
        'date',
        'evaluation',
        'evaluator',
        'measure',
    ),
    shared.Calendar: (
        'description',
        'length',
        'range',
    ),
    shared.Change: (
        'author',
        'date',
        'description',
        'details',
        'name',
        'type',
    ),
    shared.ChangeProperty: (
        'description',
        'id',
        'name',
        'value',
    ),
    shared.Citation: (
        'alternative_title',
        'collective_title',
        'date',
        'date_type',
        'location',
        'organisation',
        'role',
        'title',
        'type',
    ),
    shared.ClosedDateRange: (
        'end',
        'start',
        'duration',
    ),
    shared.Compiler: (
        'environment_variables',
        'language',
        'name',
        'options',
        'type',
        'version',
    ),
    shared.Daily360: (
        'description',
        'length',
        'range',
    ),
    shared.DataSource: (
        'purpose',
    ),
    shared.DateRange: (
        'duration',
    ),
    shared.DocMetaInfo: (
        'author',
        'create_date',
        'drs_keys',
        'drs_path',
        'external_ids',
        'id',
        'institute',
        'project',
        'sort_key',
        'source',
        'source_key',
        'sub_projects',
        'type',
        'type_display_name',
        'type_sort_key',
        'update_date',
        'version',
    ),
    shared.DocReference: (
        'canonical_name',
        'changes',
        'constraint_vocabulary',
        'context',
        'description',
        'external_id',
        'id',
        'institute',
        'linkage',
        'name',
        'protocol',
        'relationship',
        'type',
        'url',
        'version',
    ),
    shared.License: (
        'contact',
        'description',
        'is_unrestricted',
        'name',
    ),
    shared.Machine: (
        'cores_per_processor',
        'description',
        'interconnect',
        'libraries',
        'location',
        'maximum_processors',
        'name',
        'operating_system',
        'processor_type',
        'system',
        'type',
        'vendor',
    ),
    shared.MachineCompilerUnit: (
        'compilers',
        'machine',
    ),
    shared.OpenDateRange: (
        'end',
        'start',
        'duration',
    ),
    shared.PerpetualPeriod: (
        'description',
        'length',
        'range',
    ),
    shared.Platform: (
        'contacts',
        'description',
        'long_name',
        'meta',
        'short_name',
        'units',
    ),
    shared.Property: (
        'name',
        'value',
    ),
    shared.RealCalendar: (
        'description',
        'length',
        'range',
    ),
    shared.Relationship: (
        'description',
    ),
    shared.ResponsibleParty: (
        'abbreviation',
        'address',
        'email',
        'individual_name',
        'organisation_name',
        'role',
        'url',
    ),
    shared.Standard: (
        'description',
        'name',
        'version',
    ),
    shared.StandardName: (
        'is_open',
        'standards',
        'value',
    ),
    software.Component: (
        'citations',
        'code_access',
        'composition',
        'coupling_framework',
        'dependencies',
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
        'previous_version',
        'properties',
        'release_date',
        'responsible_parties',
        'short_name',
        'sub_components',
        'version',
        'purpose',
    ),
    software.ComponentLanguage: (
        'name',
        'properties',
    ),
    software.ComponentLanguageProperty: (
        'name',
        'value',
    ),
    software.ComponentProperty: (
        'citations',
        'description',
        'grid',
        'intent',
        'is_represented',
        'long_name',
        'short_name',
        'standard_names',
        'sub_properties',
        'units',
        'values',
        'purpose',
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
    software.Connection: (
        'description',
        'priming',
        'properties',
        'sources',
        'spatial_regridding',
        'target',
        'time_lag',
        'time_profile',
        'time_transformation',
        'transformers',
        'type',
    ),
    software.ConnectionEndpoint: (
        'data_source',
        'instance_id',
        'properties',
    ),
    software.ConnectionProperty: (
        'name',
        'value',
    ),
    software.Coupling: (
        'connections',
        'description',
        'is_fully_specified',
        'priming',
        'properties',
        'purpose',
        'sources',
        'spatial_regriddings',
        'target',
        'time_lag',
        'time_profile',
        'time_transformation',
        'transformers',
        'type',
    ),
    software.CouplingEndpoint: (
        'data_source',
        'instance_id',
        'properties',
    ),
    software.CouplingProperty: (
        'name',
        'value',
    ),
    software.Deployment: (
        'deployment_date',
        'description',
        'executable_arguments',
        'executable_name',
        'parallelisation',
        'platform',
    ),
    software.EntryPoint: (
        'name',
    ),
    software.ModelComponent: (
        'activity',
        'meta',
        'timing',
        'type',
        'types',
        'citations',
        'code_access',
        'composition',
        'coupling_framework',
        'dependencies',
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
        'previous_version',
        'properties',
        'release_date',
        'responsible_parties',
        'short_name',
        'sub_components',
        'version',
        'purpose',
    ),
    software.Parallelisation: (
        'processes',
        'ranks',
    ),
    software.ProcessorComponent: (
        'meta',
        'citations',
        'code_access',
        'composition',
        'coupling_framework',
        'dependencies',
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
        'previous_version',
        'properties',
        'release_date',
        'responsible_parties',
        'short_name',
        'sub_components',
        'version',
        'purpose',
    ),
    software.Rank: (
        'increment',
        'max',
        'min',
        'value',
    ),
    software.SpatialRegridding: (
        'dimension',
        'properties',
        'standard_method',
        'user_method',
    ),
    software.SpatialRegriddingProperty: (
        'name',
        'value',
    ),
    software.SpatialRegriddingUserMethod: (
        'file',
        'name',
    ),
    software.StatisticalModelComponent: (
        'meta',
        'timing',
        'type',
        'types',
        'citations',
        'code_access',
        'composition',
        'coupling_framework',
        'dependencies',
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
        'previous_version',
        'properties',
        'release_date',
        'responsible_parties',
        'short_name',
        'sub_components',
        'version',
        'purpose',
    ),
    software.TimeLag: (
        'units',
        'value',
    ),
    software.TimeTransformation: (
        'description',
        'mapping_type',
    ),
    software.Timing: (
        'end',
        'is_variable_rate',
        'rate',
        'start',
        'units',
    ),
}

# Supported class own properties.
CLASS_OWN_PROPERTIES = { 
    activity.Activity: (
        'funding_sources',
        'projects',
        'rationales',
        'responsible_parties',
    ),
    activity.BoundaryCondition: (
    ),
    activity.Conformance: (
        'description',
        'frequency',
        'is_conformant',
        'requirements',
        'sources',
        'type',
    ),
    activity.DownscalingSimulation: (
        'calendar',
        'downscaled_from',
        'downscaling_id',
        'downscaling_type',
        'inputs',
        'meta',
        'outputs',
    ),
    activity.Ensemble: (
        'members',
        'meta',
        'outputs',
        'types',
    ),
    activity.EnsembleMember: (
        'ensemble',
        'ensemble_ids',
        'simulation',
    ),
    activity.Experiment: (
        'generates',
        'measurement_campaigns',
        'requires',
        'supports',
    ),
    activity.ExperimentRelationship: (
        'target',
        'type',
    ),
    activity.ExperimentRelationshipTarget: (
        'numerical_experiment',
    ),
    activity.InitialCondition: (
    ),
    activity.LateralBoundaryCondition: (
    ),
    activity.MeasurementCampaign: (
        'duration',
    ),
    activity.NumericalActivity: (
        'description',
        'long_name',
        'short_name',
        'supports',
    ),
    activity.NumericalExperiment: (
        'description',
        'experiment_id',
        'long_name',
        'meta',
        'requirements',
        'short_name',
    ),
    activity.NumericalRequirement: (
        'description',
        'id',
        'name',
        'options',
        'requirement_type',
        'source',
    ),
    activity.NumericalRequirementOption: (
        'description',
        'id',
        'name',
        'relationship',
        'sub_options',
    ),
    activity.OutputRequirement: (
    ),
    activity.PhysicalModification: (
    ),
    activity.Simulation: (
        'authors',
        'calendar',
        'conformances',
        'control_simulation',
        'deployments',
        'inputs',
        'outputs',
        'restarts',
        'simulation_id',
        'spinup_date_range',
        'spinup_simulation',
    ),
    activity.SimulationComposite: (
        'child',
        'date_range',
        'meta',
        'rank',
    ),
    activity.SimulationRelationship: (
        'target',
        'type',
    ),
    activity.SimulationRelationshipTarget: (
        'simulation',
        'target',
    ),
    activity.SimulationRun: (
        'date_range',
        'meta',
        'model',
    ),
    activity.SpatioTemporalConstraint: (
        'date_range',
        'spatial_resolution',
    ),
    data.DataContent: (
        'aggregation',
        'frequency',
        'topic',
    ),
    data.DataDistribution: (
        'access',
        'fee',
        'format',
        'responsible_party',
    ),
    data.DataExtent: (
        'geographical',
        'temporal',
    ),
    data.DataExtentGeographical: (
        'east',
        'north',
        'south',
        'west',
    ),
    data.DataExtentTemporal: (
        'begin',
        'end',
        'time_interval',
    ),
    data.DataExtentTimeInterval: (
        'factor',
        'radix',
        'unit',
    ),
    data.DataHierarchyLevel: (
        'is_open',
        'name',
        'value',
    ),
    data.DataObject: (
        'acronym',
        'child_object',
        'citations',
        'content',
        'data_status',
        'description',
        'distribution',
        'extent',
        'geometry_model',
        'hierarchy_level',
        'keyword',
        'meta',
        'parent_object',
        'properties',
        'purpose',
        'restriction',
        'source_simulation',
        'storage',
    ),
    data.DataProperty: (
        'description',
    ),
    data.DataRestriction: (
        'license',
        'restriction',
        'scope',
    ),
    data.DataStorage: (
        'format',
        'location',
        'modification_date',
        'size',
    ),
    data.DataStorageDb: (
        'access_string',
        'name',
        'owner',
        'table',
    ),
    data.DataStorageFile: (
        'file_name',
        'file_system',
        'path',
    ),
    data.DataStorageIp: (
        'file_name',
        'host',
        'path',
        'protocol',
    ),
    data.DataTopic: (
        'description',
        'name',
        'unit',
    ),
    grids.CoordinateList: (
        'has_constant_offset',
        'length',
        'uom',
    ),
    grids.GridExtent: (
        'maximum_latitude',
        'maximum_longitude',
        'minimum_latitude',
        'minimum_longitude',
        'units',
    ),
    grids.GridMosaic: (
        'citations',
        'description',
        'extent',
        'has_congruent_tiles',
        'id',
        'is_leaf',
        'long_name',
        'mnemonic',
        'mosaic_count',
        'mosaics',
        'short_name',
        'tile_count',
        'tiles',
        'type',
    ),
    grids.GridProperty: (
    ),
    grids.GridSpec: (
        'esm_exchange_grids',
        'esm_model_grids',
        'meta',
    ),
    grids.GridTile: (
        'area',
        'cell_array',
        'cell_ref_array',
        'coord_file',
        'coordinate_pole',
        'description',
        'discretization_type',
        'extent',
        'geometry_type',
        'grid_north_pole',
        'horizontal_crs',
        'horizontal_resolution',
        'id',
        'is_conformal',
        'is_regular',
        'is_terrain_following',
        'is_uniform',
        'long_name',
        'mnemonic',
        'nx',
        'ny',
        'nz',
        'refinement_scheme',
        'short_name',
        'simple_grid_geom',
        'vertical_crs',
        'vertical_resolution',
        'zcoords',
    ),
    grids.GridTileResolutionType: (
        'description',
        'properties',
    ),
    grids.SimpleGridGeometry: (
        'dim_order',
        'is_mesh',
        'num_dims',
        'xcoords',
        'ycoords',
        'zcoords',
    ),
    grids.VerticalCoordinateList: (
        'form',
        'properties',
        'type',
    ),
    misc.DocumentSet: (
        'data',
        'ensembles',
        'experiment',
        'grids',
        'meta',
        'model',
        'platform',
        'simulation',
    ),
    quality.CimQuality: (
        'meta',
        'reports',
    ),
    quality.Evaluation: (
        'date',
        'description',
        'did_pass',
        'explanation',
        'specification',
        'specification_hyperlink',
        'title',
        'type',
        'type_hyperlink',
    ),
    quality.Measure: (
        'description',
        'identification',
        'name',
    ),
    quality.Report: (
        'date',
        'evaluation',
        'evaluator',
        'measure',
    ),
    shared.Calendar: (
        'description',
        'length',
        'range',
    ),
    shared.Change: (
        'author',
        'date',
        'description',
        'details',
        'name',
        'type',
    ),
    shared.ChangeProperty: (
        'description',
        'id',
    ),
    shared.Citation: (
        'alternative_title',
        'collective_title',
        'date',
        'date_type',
        'location',
        'organisation',
        'role',
        'title',
        'type',
    ),
    shared.ClosedDateRange: (
        'end',
        'start',
    ),
    shared.Compiler: (
        'environment_variables',
        'language',
        'name',
        'options',
        'type',
        'version',
    ),
    shared.Daily360: (
    ),
    shared.DataSource: (
        'purpose',
    ),
    shared.DateRange: (
        'duration',
    ),
    shared.DocMetaInfo: (
        'author',
        'create_date',
        'drs_keys',
        'drs_path',
        'external_ids',
        'id',
        'institute',
        'project',
        'sort_key',
        'source',
        'source_key',
        'sub_projects',
        'type',
        'type_display_name',
        'type_sort_key',
        'update_date',
        'version',
    ),
    shared.DocReference: (
        'canonical_name',
        'changes',
        'constraint_vocabulary',
        'context',
        'description',
        'external_id',
        'id',
        'institute',
        'linkage',
        'name',
        'protocol',
        'relationship',
        'type',
        'url',
        'version',
    ),
    shared.License: (
        'contact',
        'description',
        'is_unrestricted',
        'name',
    ),
    shared.Machine: (
        'cores_per_processor',
        'description',
        'interconnect',
        'libraries',
        'location',
        'maximum_processors',
        'name',
        'operating_system',
        'processor_type',
        'system',
        'type',
        'vendor',
    ),
    shared.MachineCompilerUnit: (
        'compilers',
        'machine',
    ),
    shared.OpenDateRange: (
        'end',
        'start',
    ),
    shared.PerpetualPeriod: (
    ),
    shared.Platform: (
        'contacts',
        'description',
        'long_name',
        'meta',
        'short_name',
        'units',
    ),
    shared.Property: (
        'name',
        'value',
    ),
    shared.RealCalendar: (
    ),
    shared.Relationship: (
        'description',
    ),
    shared.ResponsibleParty: (
        'abbreviation',
        'address',
        'email',
        'individual_name',
        'organisation_name',
        'role',
        'url',
    ),
    shared.Standard: (
        'description',
        'name',
        'version',
    ),
    shared.StandardName: (
        'is_open',
        'standards',
        'value',
    ),
    software.Component: (
        'citations',
        'code_access',
        'composition',
        'coupling_framework',
        'dependencies',
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
        'previous_version',
        'properties',
        'release_date',
        'responsible_parties',
        'short_name',
        'sub_components',
        'version',
    ),
    software.ComponentLanguage: (
        'name',
        'properties',
    ),
    software.ComponentLanguageProperty: (
    ),
    software.ComponentProperty: (
        'citations',
        'description',
        'grid',
        'intent',
        'is_represented',
        'long_name',
        'short_name',
        'standard_names',
        'sub_properties',
        'units',
        'values',
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
    software.Connection: (
        'description',
        'priming',
        'properties',
        'sources',
        'spatial_regridding',
        'target',
        'time_lag',
        'time_profile',
        'time_transformation',
        'transformers',
        'type',
    ),
    software.ConnectionEndpoint: (
        'data_source',
        'instance_id',
        'properties',
    ),
    software.ConnectionProperty: (
    ),
    software.Coupling: (
        'connections',
        'description',
        'is_fully_specified',
        'priming',
        'properties',
        'purpose',
        'sources',
        'spatial_regriddings',
        'target',
        'time_lag',
        'time_profile',
        'time_transformation',
        'transformers',
        'type',
    ),
    software.CouplingEndpoint: (
        'data_source',
        'instance_id',
        'properties',
    ),
    software.CouplingProperty: (
    ),
    software.Deployment: (
        'deployment_date',
        'description',
        'executable_arguments',
        'executable_name',
        'parallelisation',
        'platform',
    ),
    software.EntryPoint: (
        'name',
    ),
    software.ModelComponent: (
        'activity',
        'meta',
        'timing',
        'type',
        'types',
    ),
    software.Parallelisation: (
        'processes',
        'ranks',
    ),
    software.ProcessorComponent: (
        'meta',
    ),
    software.Rank: (
        'increment',
        'max',
        'min',
        'value',
    ),
    software.SpatialRegridding: (
        'dimension',
        'properties',
        'standard_method',
        'user_method',
    ),
    software.SpatialRegriddingProperty: (
    ),
    software.SpatialRegriddingUserMethod: (
        'file',
        'name',
    ),
    software.StatisticalModelComponent: (
        'meta',
        'timing',
        'type',
        'types',
    ),
    software.TimeLag: (
        'units',
        'value',
    ),
    software.TimeTransformation: (
        'description',
        'mapping_type',
    ),
    software.Timing: (
        'end',
        'is_variable_rate',
        'rate',
        'start',
        'units',
    ),
}

# Total class properties.
TOTAL_CLASS_PROPERTIES = sum(len(i) for i in CLASS_OWN_PROPERTIES.values())

# ------------------------------------------------
# Enum.
# ------------------------------------------------

# Supported enums.
ENUMS = (
    activity.ConformanceType,
    activity.DownscalingType,
    activity.EnsembleType,
    activity.ExperimentRelationshipType,
    activity.FrequencyType,
    activity.ProjectType,
    activity.ResolutionType,
    activity.SimulationRelationshipType,
    activity.SimulationType,
    data.DataHierarchyType,
    data.DataStatusType,
    grids.ArcTypeEnum,
    grids.DiscretizationEnum,
    grids.FeatureTypeEnum,
    grids.GeometryTypeEnum,
    grids.GridNodePositionEnum,
    grids.GridTypeEnum,
    grids.HorizontalCsEnum,
    grids.RefinementTypeEnum,
    grids.VerticalCsEnum,
    quality.CimFeatureType,
    quality.CimResultType,
    quality.CimScopeCodeType,
    quality.QualityIssueType,
    quality.QualitySeverityType,
    quality.QualityStatusType,
    shared.ChangePropertyType,
    shared.CompilerType,
    shared.DataPurpose,
    shared.InterconnectType,
    shared.MachineType,
    shared.MachineVendorType,
    shared.OperatingSystemType,
    shared.ProcessorType,
    shared.UnitType,
    software.ComponentPropertyIntentType,
    software.ConnectionType,
    software.CouplingFrameworkType,
    software.ModelComponentType,
    software.SpatialRegriddingDimensionType,
    software.SpatialRegriddingStandardMethodType,
    software.StatisticalModelComponentType,
    software.TimeMappingType,
    software.TimingUnits,
)

# Total enum members across all enums.
TOTAL_ENUM_MEMBERS = sum(len(e.members) for e in ENUMS)

# ------------------------------------------------
# Type hierarchies.
# ------------------------------------------------

# Set of supported types.
TYPES = CLASSES + ENUMS

# Supported document types.
DOCUMENT_TYPES = (
    activity.DownscalingSimulation,
    activity.Ensemble,
    activity.NumericalExperiment,
    activity.SimulationComposite,
    activity.SimulationRun,
    data.DataObject,
    grids.GridSpec,
    misc.DocumentSet,
    quality.CimQuality,
    shared.Platform,
    software.ModelComponent,
    software.ProcessorComponent,
    software.StatisticalModelComponent,
)

# Base classes.
BASE_CLASSES = defaultdict(tuple)
BASE_CLASSES[activity.BoundaryCondition] = (activity.NumericalRequirement, )
BASE_CLASSES[activity.DownscalingSimulation] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[activity.Ensemble] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[activity.EnsembleMember] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[activity.Experiment] = (activity.Activity, )
BASE_CLASSES[activity.ExperimentRelationship] = (shared.Relationship, )
BASE_CLASSES[activity.InitialCondition] = (activity.NumericalRequirement, )
BASE_CLASSES[activity.LateralBoundaryCondition] = (activity.NumericalRequirement, )
BASE_CLASSES[activity.MeasurementCampaign] = (activity.Activity, )
BASE_CLASSES[activity.NumericalActivity] = (activity.Activity, )
BASE_CLASSES[activity.NumericalExperiment] = (activity.Experiment, activity.Activity, )
BASE_CLASSES[activity.OutputRequirement] = (activity.NumericalRequirement, )
BASE_CLASSES[activity.PhysicalModification] = (activity.Conformance, )
BASE_CLASSES[activity.Simulation] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[activity.SimulationComposite] = (activity.Simulation, activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[activity.SimulationRelationship] = (shared.Relationship, )
BASE_CLASSES[activity.SimulationRun] = (activity.Simulation, activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[activity.SpatioTemporalConstraint] = (activity.NumericalRequirement, )
BASE_CLASSES[data.DataContent] = (shared.DataSource, )
BASE_CLASSES[data.DataObject] = (shared.DataSource, )
BASE_CLASSES[data.DataProperty] = (shared.Property, )
BASE_CLASSES[data.DataStorageDb] = (data.DataStorage, )
BASE_CLASSES[data.DataStorageFile] = (data.DataStorage, )
BASE_CLASSES[data.DataStorageIp] = (data.DataStorage, )
BASE_CLASSES[grids.GridProperty] = (shared.Property, )
BASE_CLASSES[grids.VerticalCoordinateList] = (grids.CoordinateList, )
BASE_CLASSES[shared.ChangeProperty] = (shared.Property, )
BASE_CLASSES[shared.ClosedDateRange] = (shared.DateRange, )
BASE_CLASSES[shared.Daily360] = (shared.Calendar, )
BASE_CLASSES[shared.OpenDateRange] = (shared.DateRange, )
BASE_CLASSES[shared.PerpetualPeriod] = (shared.Calendar, )
BASE_CLASSES[shared.RealCalendar] = (shared.Calendar, )
BASE_CLASSES[software.Component] = (shared.DataSource, )
BASE_CLASSES[software.ComponentLanguageProperty] = (shared.Property, )
BASE_CLASSES[software.ComponentProperty] = (shared.DataSource, )
BASE_CLASSES[software.ConnectionProperty] = (shared.Property, )
BASE_CLASSES[software.CouplingProperty] = (shared.Property, )
BASE_CLASSES[software.ModelComponent] = (software.Component, shared.DataSource, )
BASE_CLASSES[software.ProcessorComponent] = (software.Component, shared.DataSource, )
BASE_CLASSES[software.SpatialRegriddingProperty] = (shared.Property, )
BASE_CLASSES[software.StatisticalModelComponent] = (software.Component, shared.DataSource, )

# Classes with base classes.
BASE_CLASSED = tuple(BASE_CLASSES.keys())

# Sub classes.
SUB_CLASSES = defaultdict(tuple)
SUB_CLASSES[activity.Activity] = (
    activity.Experiment,
    activity.MeasurementCampaign,
    activity.NumericalActivity,
    activity.DownscalingSimulation,
    activity.Ensemble,
    activity.EnsembleMember,
    activity.NumericalExperiment,
    activity.Simulation,
    activity.SimulationComposite,
    activity.SimulationRun,
    )
SUB_CLASSES[activity.Conformance] = (
    activity.PhysicalModification,
    )
SUB_CLASSES[activity.Experiment] = (
    activity.NumericalExperiment,
    )
SUB_CLASSES[activity.NumericalActivity] = (
    activity.DownscalingSimulation,
    activity.Ensemble,
    activity.EnsembleMember,
    activity.Simulation,
    activity.SimulationComposite,
    activity.SimulationRun,
    )
SUB_CLASSES[activity.NumericalRequirement] = (
    activity.BoundaryCondition,
    activity.InitialCondition,
    activity.LateralBoundaryCondition,
    activity.OutputRequirement,
    activity.SpatioTemporalConstraint,
    )
SUB_CLASSES[activity.Simulation] = (
    activity.SimulationComposite,
    activity.SimulationRun,
    )
SUB_CLASSES[data.DataStorage] = (
    data.DataStorageDb,
    data.DataStorageFile,
    data.DataStorageIp,
    )
SUB_CLASSES[grids.CoordinateList] = (
    grids.VerticalCoordinateList,
    )
SUB_CLASSES[shared.Calendar] = (
    shared.Daily360,
    shared.PerpetualPeriod,
    shared.RealCalendar,
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
SUB_CLASSES[shared.DateRange] = (
    shared.ClosedDateRange,
    shared.OpenDateRange,
    )
SUB_CLASSES[shared.Property] = (
    data.DataProperty,
    grids.GridProperty,
    shared.ChangeProperty,
    software.ComponentLanguageProperty,
    software.ConnectionProperty,
    software.CouplingProperty,
    software.SpatialRegriddingProperty,
    )
SUB_CLASSES[shared.Relationship] = (
    activity.ExperimentRelationship,
    activity.SimulationRelationship,
    )
SUB_CLASSES[software.Component] = (
    software.ModelComponent,
    software.ProcessorComponent,
    software.StatisticalModelComponent,
    )

# Classes that have been sub classed.
SUB_CLASSED = tuple(SUB_CLASSES.keys())

# Maximum class depth in hierarchy.
CLASS_HIERACHY_DEPTH = max(len(v) for v in BASE_CLASSES.values())

# ------------------------------------------------
# Type constraints.
# ------------------------------------------------

# Map of ontology types to constraints.
CONSTRAINTS = {
    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    activity.Activity: (

        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('projects', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),

    ),
    activity.BoundaryCondition: (

        ('description', 'type', unicode),
        ('id', 'type', unicode),
        ('source', 'type', shared.DataSource),
        ('requirement_type', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('source', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('options', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

        ('requirement_type', 'constant', "boundaryCondition"),
    ),
    activity.Conformance: (

        ('requirements', 'type', activity.NumericalRequirement),
        ('description', 'type', unicode),
        ('sources', 'type', shared.DataSource),
        ('frequency', 'type', unicode),
        ('is_conformant', 'type', bool),
        ('type', 'type', unicode),

        ('requirements', 'cardinality', "1.N"),
        ('description', 'cardinality', "0.1"),
        ('sources', 'cardinality', "0.N"),
        ('frequency', 'cardinality', "0.1"),
        ('is_conformant', 'cardinality', "1.1"),
        ('type', 'cardinality', "0.1"),

    ),
    activity.DownscalingSimulation: (

        ('inputs', 'type', software.Coupling),
        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('outputs', 'type', data.DataObject),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('long_name', 'type', unicode),
        ('downscaled_from', 'type', shared.DataSource),
        ('downscaling_id', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('downscaling_type', 'type', unicode),
        ('calendar', 'type', shared.Calendar),
        ('supports', 'type', activity.Experiment),
        ('projects', 'type', unicode),

        ('inputs', 'cardinality', "0.N"),
        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('outputs', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('downscaled_from', 'cardinality', "1.1"),
        ('downscaling_id', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('downscaling_type', 'cardinality', "0.1"),
        ('calendar', 'cardinality', "1.1"),
        ('supports', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),

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
    activity.Experiment: (

        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('generates', 'type', unicode),
        ('supports', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('measurement_campaigns', 'type', activity.MeasurementCampaign),
        ('requires', 'type', activity.NumericalActivity),
        ('projects', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('generates', 'cardinality', "0.N"),
        ('supports', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('measurement_campaigns', 'cardinality', "0.N"),
        ('requires', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),

    ),
    activity.ExperimentRelationship: (

        ('type', 'type', unicode),
        ('description', 'type', unicode),
        ('target', 'type', activity.ExperimentRelationshipTarget),

        ('type', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('target', 'cardinality', "1.1"),

    ),
    activity.ExperimentRelationshipTarget: (

        ('numerical_experiment', 'type', activity.NumericalExperiment),

        ('numerical_experiment', 'cardinality', "0.1"),

    ),
    activity.InitialCondition: (

        ('description', 'type', unicode),
        ('id', 'type', unicode),
        ('source', 'type', shared.DataSource),
        ('requirement_type', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('source', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('options', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

        ('requirement_type', 'constant', "initialCondition"),
    ),
    activity.LateralBoundaryCondition: (

        ('description', 'type', unicode),
        ('id', 'type', unicode),
        ('source', 'type', shared.DataSource),
        ('requirement_type', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('source', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('options', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

        ('requirement_type', 'constant', "lateralBoundaryCondition"),
    ),
    activity.MeasurementCampaign: (

        ('duration', 'type', int),
        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('projects', 'type', unicode),
        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('duration', 'cardinality', "1.1"),
        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),

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
    activity.NumericalExperiment: (

        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('generates', 'type', unicode),
        ('short_name', 'type', unicode),
        ('long_name', 'type', unicode),
        ('requires', 'type', activity.NumericalActivity),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('measurement_campaigns', 'type', activity.MeasurementCampaign),
        ('meta', 'type', shared.DocMetaInfo),
        ('experiment_id', 'type', unicode),
        ('requirements', 'type', activity.NumericalRequirement),
        ('supports', 'type', unicode),
        ('projects', 'type', unicode),
        ('description', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('generates', 'cardinality', "0.N"),
        ('short_name', 'cardinality', "1.1"),
        ('long_name', 'cardinality', "0.1"),
        ('requires', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('measurement_campaigns', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('experiment_id', 'cardinality', "0.1"),
        ('requirements', 'cardinality', "0.N"),
        ('supports', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),

    ),
    activity.NumericalRequirement: (

        ('description', 'type', unicode),
        ('id', 'type', unicode),
        ('source', 'type', shared.DataSource),
        ('requirement_type', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('source', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('options', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    activity.NumericalRequirementOption: (

        ('sub_options', 'type', activity.NumericalRequirementOption),
        ('relationship', 'type', unicode),
        ('description', 'type', unicode),
        ('name', 'type', unicode),
        ('id', 'type', unicode),

        ('sub_options', 'cardinality', "0.N"),
        ('relationship', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('id', 'cardinality', "0.1"),

    ),
    activity.OutputRequirement: (

        ('description', 'type', unicode),
        ('id', 'type', unicode),
        ('source', 'type', shared.DataSource),
        ('requirement_type', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('source', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('options', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

        ('requirement_type', 'constant', "outputRequirement"),
    ),
    activity.PhysicalModification: (

        ('requirements', 'type', activity.NumericalRequirement),
        ('description', 'type', unicode),
        ('sources', 'type', shared.DataSource),
        ('frequency', 'type', unicode),
        ('is_conformant', 'type', bool),
        ('type', 'type', unicode),

        ('requirements', 'cardinality', "1.N"),
        ('description', 'cardinality', "0.1"),
        ('sources', 'cardinality', "0.N"),
        ('frequency', 'cardinality', "0.1"),
        ('is_conformant', 'cardinality', "1.1"),
        ('type', 'cardinality', "0.1"),

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
    activity.SimulationRelationship: (

        ('type', 'type', unicode),
        ('description', 'type', unicode),
        ('target', 'type', activity.SimulationRelationshipTarget),

        ('type', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('target', 'cardinality', "1.1"),

    ),
    activity.SimulationRelationshipTarget: (

        ('target', 'type', unicode),
        ('simulation', 'type', shared.DocReference),

        ('target', 'cardinality', "0.1"),
        ('simulation', 'cardinality', "0.1"),

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
    activity.SpatioTemporalConstraint: (

        ('description', 'type', unicode),
        ('id', 'type', unicode),
        ('date_range', 'type', shared.DateRange),
        ('source', 'type', shared.DataSource),
        ('spatial_resolution', 'type', unicode),
        ('requirement_type', 'type', unicode),
        ('options', 'type', activity.NumericalRequirementOption),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('date_range', 'cardinality', "0.1"),
        ('source', 'cardinality', "0.1"),
        ('spatial_resolution', 'cardinality', "0.1"),
        ('requirement_type', 'cardinality', "1.1"),
        ('options', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

        ('requirement_type', 'constant', "spatioTemporalConstraint"),
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
    data.DataExtent: (

        ('temporal', 'type', data.DataExtentTemporal),
        ('geographical', 'type', data.DataExtentGeographical),

        ('temporal', 'cardinality', "1.1"),
        ('geographical', 'cardinality', "1.1"),

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
    data.DataExtentTemporal: (

        ('time_interval', 'type', data.DataExtentTimeInterval),
        ('begin', 'type', datetime.date),
        ('end', 'type', datetime.date),

        ('time_interval', 'cardinality', "0.1"),
        ('begin', 'cardinality', "0.1"),
        ('end', 'cardinality', "0.1"),

    ),
    data.DataExtentTimeInterval: (

        ('radix', 'type', int),
        ('unit', 'type', unicode),
        ('factor', 'type', int),

        ('radix', 'cardinality', "0.1"),
        ('unit', 'cardinality', "0.1"),
        ('factor', 'cardinality', "0.1"),

    ),
    data.DataHierarchyLevel: (

        ('is_open', 'type', bool),
        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('is_open', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    data.DataObject: (

        ('hierarchy_level', 'type', data.DataHierarchyLevel),
        ('source_simulation', 'type', unicode),
        ('description', 'type', unicode),
        ('keyword', 'type', unicode),
        ('restriction', 'type', data.DataRestriction),
        ('acronym', 'type', unicode),
        ('storage', 'type', data.DataStorage),
        ('child_object', 'type', data.DataObject),
        ('content', 'type', data.DataContent),
        ('geometry_model', 'type', unicode),
        ('citations', 'type', shared.Citation),
        ('meta', 'type', shared.DocMetaInfo),
        ('purpose', 'type', unicode),
        ('extent', 'type', data.DataExtent),
        ('distribution', 'type', data.DataDistribution),
        ('parent_object', 'type', data.DataObject),
        ('properties', 'type', data.DataProperty),
        ('data_status', 'type', unicode),

        ('hierarchy_level', 'cardinality', "0.1"),
        ('source_simulation', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('keyword', 'cardinality', "0.1"),
        ('restriction', 'cardinality', "0.N"),
        ('acronym', 'cardinality', "0.1"),
        ('storage', 'cardinality', "0.N"),
        ('child_object', 'cardinality', "0.N"),
        ('content', 'cardinality', "0.N"),
        ('geometry_model', 'cardinality', "0.1"),
        ('citations', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('purpose', 'cardinality', "0.1"),
        ('extent', 'cardinality', "0.1"),
        ('distribution', 'cardinality', "0.1"),
        ('parent_object', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('data_status', 'cardinality', "0.1"),

    ),
    data.DataProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),
        ('description', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    data.DataRestriction: (

        ('restriction', 'type', unicode),
        ('license', 'type', shared.License),
        ('scope', 'type', unicode),

        ('restriction', 'cardinality', "0.1"),
        ('license', 'cardinality', "0.1"),
        ('scope', 'cardinality', "0.1"),

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
    data.DataTopic: (

        ('description', 'type', unicode),
        ('unit', 'type', unicode),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('unit', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),

    ),
    grids.CoordinateList: (

        ('has_constant_offset', 'type', bool),
        ('length', 'type', int),
        ('uom', 'type', unicode),

        ('has_constant_offset', 'cardinality', "0.1"),
        ('length', 'cardinality', "0.1"),
        ('uom', 'cardinality', "0.1"),

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
    grids.GridMosaic: (

        ('is_leaf', 'type', bool),
        ('mnemonic', 'type', unicode),
        ('tiles', 'type', grids.GridTile),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('mosaic_count', 'type', int),
        ('type', 'type', unicode),
        ('long_name', 'type', unicode),
        ('tile_count', 'type', int),
        ('citations', 'type', shared.Citation),
        ('extent', 'type', grids.GridExtent),
        ('has_congruent_tiles', 'type', bool),
        ('mosaics', 'type', grids.GridMosaic),
        ('id', 'type', unicode),

        ('is_leaf', 'cardinality', "1.1"),
        ('mnemonic', 'cardinality', "0.1"),
        ('tiles', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('mosaic_count', 'cardinality', "0.1"),
        ('type', 'cardinality', "1.1"),
        ('long_name', 'cardinality', "0.1"),
        ('tile_count', 'cardinality', "0.1"),
        ('citations', 'cardinality', "0.N"),
        ('extent', 'cardinality', "0.1"),
        ('has_congruent_tiles', 'cardinality', "0.1"),
        ('mosaics', 'cardinality', "0.N"),
        ('id', 'cardinality', "1.1"),

    ),
    grids.GridProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    grids.GridSpec: (

        ('esm_exchange_grids', 'type', grids.GridMosaic),
        ('meta', 'type', shared.DocMetaInfo),
        ('esm_model_grids', 'type', grids.GridMosaic),

        ('esm_exchange_grids', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('esm_model_grids', 'cardinality', "0.N"),

    ),
    grids.GridTile: (

        ('mnemonic', 'type', unicode),
        ('refinement_scheme', 'type', unicode),
        ('is_regular', 'type', bool),
        ('vertical_crs', 'type', unicode),
        ('long_name', 'type', unicode),
        ('horizontal_crs', 'type', unicode),
        ('cell_array', 'type', unicode),
        ('id', 'type', unicode),
        ('cell_ref_array', 'type', unicode),
        ('area', 'type', unicode),
        ('simple_grid_geom', 'type', grids.SimpleGridGeometry),
        ('grid_north_pole', 'type', unicode),
        ('nx', 'type', int),
        ('ny', 'type', int),
        ('nz', 'type', int),
        ('vertical_resolution', 'type', grids.GridTileResolutionType),
        ('discretization_type', 'type', unicode),
        ('coordinate_pole', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('extent', 'type', grids.GridExtent),
        ('zcoords', 'type', grids.VerticalCoordinateList),
        ('is_conformal', 'type', bool),
        ('is_uniform', 'type', bool),
        ('coord_file', 'type', unicode),
        ('geometry_type', 'type', unicode),
        ('horizontal_resolution', 'type', grids.GridTileResolutionType),
        ('is_terrain_following', 'type', bool),

        ('mnemonic', 'cardinality', "0.1"),
        ('refinement_scheme', 'cardinality', "0.1"),
        ('is_regular', 'cardinality', "0.1"),
        ('vertical_crs', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('horizontal_crs', 'cardinality', "0.1"),
        ('cell_array', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('cell_ref_array', 'cardinality', "0.1"),
        ('area', 'cardinality', "0.1"),
        ('simple_grid_geom', 'cardinality', "0.1"),
        ('grid_north_pole', 'cardinality', "0.1"),
        ('nx', 'cardinality', "0.1"),
        ('ny', 'cardinality', "0.1"),
        ('nz', 'cardinality', "0.1"),
        ('vertical_resolution', 'cardinality', "0.1"),
        ('discretization_type', 'cardinality', "0.1"),
        ('coordinate_pole', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "0.1"),
        ('extent', 'cardinality', "0.1"),
        ('zcoords', 'cardinality', "0.1"),
        ('is_conformal', 'cardinality', "0.1"),
        ('is_uniform', 'cardinality', "0.1"),
        ('coord_file', 'cardinality', "0.1"),
        ('geometry_type', 'cardinality', "0.1"),
        ('horizontal_resolution', 'cardinality', "0.1"),
        ('is_terrain_following', 'cardinality', "0.1"),

    ),
    grids.GridTileResolutionType: (

        ('description', 'type', unicode),
        ('properties', 'type', grids.GridProperty),

        ('description', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),

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
    misc.DocumentSet: (

        ('experiment', 'type', activity.NumericalExperiment),
        ('grids', 'type', grids.GridSpec),
        ('simulation', 'type', activity.SimulationRun),
        ('platform', 'type', shared.Platform),
        ('meta', 'type', shared.DocMetaInfo),
        ('model', 'type', software.ModelComponent),
        ('data', 'type', data.DataObject),
        ('ensembles', 'type', activity.Ensemble),

        ('experiment', 'cardinality', "0.1"),
        ('grids', 'cardinality', "0.N"),
        ('simulation', 'cardinality', "0.1"),
        ('platform', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('model', 'cardinality', "0.1"),
        ('data', 'cardinality', "0.N"),
        ('ensembles', 'cardinality', "0.N"),

    ),
    quality.CimQuality: (

        ('meta', 'type', shared.DocMetaInfo),
        ('reports', 'type', quality.Report),

        ('meta', 'cardinality', "1.1"),
        ('reports', 'cardinality', "0.N"),

    ),
    quality.Evaluation: (

        ('description', 'type', unicode),
        ('specification_hyperlink', 'type', unicode),
        ('explanation', 'type', unicode),
        ('title', 'type', unicode),
        ('did_pass', 'type', bool),
        ('type_hyperlink', 'type', unicode),
        ('date', 'type', datetime.datetime),
        ('type', 'type', unicode),
        ('specification', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('specification_hyperlink', 'cardinality', "0.1"),
        ('explanation', 'cardinality', "0.1"),
        ('title', 'cardinality', "0.1"),
        ('did_pass', 'cardinality', "0.1"),
        ('type_hyperlink', 'cardinality', "0.1"),
        ('date', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('specification', 'cardinality', "0.1"),

    ),
    quality.Measure: (

        ('identification', 'type', unicode),
        ('description', 'type', unicode),
        ('name', 'type', unicode),

        ('identification', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),

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
    shared.Calendar: (

        ('range', 'type', shared.DateRange),
        ('length', 'type', int),
        ('description', 'type', unicode),

        ('range', 'cardinality', "0.1"),
        ('length', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    shared.Change: (

        ('description', 'type', unicode),
        ('author', 'type', shared.ResponsibleParty),
        ('details', 'type', shared.ChangeProperty),
        ('date', 'type', datetime.datetime),
        ('type', 'type', unicode),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('author', 'cardinality', "0.1"),
        ('details', 'cardinality', "1.N"),
        ('date', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),

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
    shared.Citation: (

        ('alternative_title', 'type', unicode),
        ('date_type', 'type', unicode),
        ('collective_title', 'type', unicode),
        ('role', 'type', unicode),
        ('location', 'type', unicode),
        ('date', 'type', datetime.datetime),
        ('title', 'type', unicode),
        ('type', 'type', unicode),
        ('organisation', 'type', unicode),

        ('alternative_title', 'cardinality', "0.1"),
        ('date_type', 'cardinality', "0.1"),
        ('collective_title', 'cardinality', "0.1"),
        ('role', 'cardinality', "0.1"),
        ('location', 'cardinality', "0.1"),
        ('date', 'cardinality', "0.1"),
        ('title', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('organisation', 'cardinality', "0.1"),

    ),
    shared.ClosedDateRange: (

        ('duration', 'type', unicode),
        ('start', 'type', datetime.datetime),
        ('end', 'type', datetime.datetime),

        ('duration', 'cardinality', "0.1"),
        ('start', 'cardinality', "1.1"),
        ('end', 'cardinality', "0.1"),

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
    shared.Daily360: (

        ('range', 'type', shared.DateRange),
        ('length', 'type', int),
        ('description', 'type', unicode),

        ('range', 'cardinality', "0.1"),
        ('length', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    shared.DataSource: (

        ('purpose', 'type', unicode),

        ('purpose', 'cardinality', "0.1"),

    ),
    shared.DateRange: (

        ('duration', 'type', unicode),

        ('duration', 'cardinality', "0.1"),

    ),
    shared.DocMetaInfo: (

        ('drs_keys', 'type', unicode),
        ('drs_path', 'type', unicode),
        ('create_date', 'type', datetime.datetime),
        ('author', 'type', shared.ResponsibleParty),
        ('institute', 'type', unicode),
        ('source_key', 'type', unicode),
        ('project', 'type', unicode),
        ('sort_key', 'type', unicode),
        ('version', 'type', int),
        ('source', 'type', unicode),
        ('type_sort_key', 'type', unicode),
        ('update_date', 'type', datetime.datetime),
        ('external_ids', 'type', unicode),
        ('sub_projects', 'type', unicode),
        ('type', 'type', unicode),
        ('id', 'type', unicode),
        ('type_display_name', 'type', unicode),

        ('drs_keys', 'cardinality', "0.N"),
        ('drs_path', 'cardinality', "0.1"),
        ('create_date', 'cardinality', "1.1"),
        ('author', 'cardinality', "0.1"),
        ('institute', 'cardinality', "0.1"),
        ('source_key', 'cardinality', "0.1"),
        ('project', 'cardinality', "0.1"),
        ('sort_key', 'cardinality', "0.1"),
        ('version', 'cardinality', "1.1"),
        ('source', 'cardinality', "1.1"),
        ('type_sort_key', 'cardinality', "0.1"),
        ('update_date', 'cardinality', "0.1"),
        ('external_ids', 'cardinality', "0.N"),
        ('sub_projects', 'cardinality', "0.N"),
        ('type', 'cardinality', "1.1"),
        ('id', 'cardinality', "1.1"),
        ('type_display_name', 'cardinality', "0.1"),

    ),
    shared.DocReference: (

        ('constraint_vocabulary', 'type', unicode),
        ('protocol', 'type', unicode),
        ('description', 'type', unicode),
        ('relationship', 'type', unicode),
        ('institute', 'type', unicode),
        ('external_id', 'type', unicode),
        ('url', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('version', 'type', int),
        ('context', 'type', unicode),
        ('type', 'type', unicode),
        ('changes', 'type', shared.Change),
        ('id', 'type', unicode),
        ('linkage', 'type', unicode),
        ('name', 'type', unicode),

        ('constraint_vocabulary', 'cardinality', "0.1"),
        ('protocol', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('relationship', 'cardinality', "0.1"),
        ('institute', 'cardinality', "0.1"),
        ('external_id', 'cardinality', "0.1"),
        ('url', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('version', 'cardinality', "0.1"),
        ('context', 'cardinality', "0.1"),
        ('type', 'cardinality', "1.1"),
        ('changes', 'cardinality', "0.N"),
        ('id', 'cardinality', "0.1"),
        ('linkage', 'cardinality', "1.1"),
        ('name', 'cardinality', "1.1"),

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
    shared.Machine: (

        ('operating_system', 'type', unicode),
        ('maximum_processors', 'type', int),
        ('description', 'type', unicode),
        ('cores_per_processor', 'type', int),
        ('processor_type', 'type', unicode),
        ('system', 'type', unicode),
        ('vendor', 'type', unicode),
        ('libraries', 'type', unicode),
        ('location', 'type', unicode),
        ('interconnect', 'type', unicode),
        ('type', 'type', unicode),
        ('name', 'type', unicode),

        ('operating_system', 'cardinality', "0.1"),
        ('maximum_processors', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('cores_per_processor', 'cardinality', "0.1"),
        ('processor_type', 'cardinality', "0.1"),
        ('system', 'cardinality', "0.1"),
        ('vendor', 'cardinality', "0.1"),
        ('libraries', 'cardinality', "0.N"),
        ('location', 'cardinality', "0.1"),
        ('interconnect', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    shared.MachineCompilerUnit: (

        ('machine', 'type', shared.Machine),
        ('compilers', 'type', shared.Compiler),

        ('machine', 'cardinality', "1.1"),
        ('compilers', 'cardinality', "0.N"),

    ),
    shared.OpenDateRange: (

        ('duration', 'type', unicode),
        ('start', 'type', datetime.datetime),
        ('end', 'type', datetime.datetime),

        ('duration', 'cardinality', "0.1"),
        ('start', 'cardinality', "0.1"),
        ('end', 'cardinality', "0.1"),

    ),
    shared.PerpetualPeriod: (

        ('range', 'type', shared.DateRange),
        ('length', 'type', int),
        ('description', 'type', unicode),

        ('range', 'cardinality', "0.1"),
        ('length', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

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
    shared.Property: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    shared.RealCalendar: (

        ('range', 'type', shared.DateRange),
        ('length', 'type', int),
        ('description', 'type', unicode),

        ('range', 'cardinality', "0.1"),
        ('length', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    shared.Relationship: (

        ('description', 'type', unicode),

        ('description', 'cardinality', "0.1"),

    ),
    shared.ResponsibleParty: (

        ('url', 'type', unicode),
        ('email', 'type', unicode),
        ('abbreviation', 'type', unicode),
        ('individual_name', 'type', unicode),
        ('role', 'type', unicode),
        ('address', 'type', unicode),
        ('organisation_name', 'type', unicode),

        ('url', 'cardinality', "0.1"),
        ('email', 'cardinality', "0.1"),
        ('abbreviation', 'cardinality', "0.1"),
        ('individual_name', 'cardinality', "0.1"),
        ('role', 'cardinality', "0.1"),
        ('address', 'cardinality', "0.1"),
        ('organisation_name', 'cardinality', "0.1"),

    ),
    shared.Standard: (

        ('version', 'type', unicode),
        ('description', 'type', unicode),
        ('name', 'type', unicode),

        ('version', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    shared.StandardName: (

        ('is_open', 'type', bool),
        ('value', 'type', unicode),
        ('standards', 'type', shared.Standard),

        ('is_open', 'cardinality', "1.1"),
        ('value', 'cardinality', "1.1"),
        ('standards', 'cardinality', "0.N"),

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
    software.ComponentLanguage: (

        ('name', 'type', unicode),
        ('properties', 'type', software.ComponentLanguageProperty),

        ('name', 'cardinality', "1.1"),
        ('properties', 'cardinality', "0.N"),

    ),
    software.ComponentLanguageProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    software.ComponentProperty: (

        ('standard_names', 'type', unicode),
        ('sub_properties', 'type', software.ComponentProperty),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('values', 'type', unicode),
        ('is_represented', 'type', bool),
        ('long_name', 'type', unicode),
        ('citations', 'type', shared.Citation),
        ('intent', 'type', unicode),
        ('purpose', 'type', unicode),
        ('units', 'type', unicode),
        ('grid', 'type', unicode),

        ('standard_names', 'cardinality', "0.N"),
        ('sub_properties', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('values', 'cardinality', "0.N"),
        ('is_represented', 'cardinality', "1.1"),
        ('long_name', 'cardinality', "0.1"),
        ('citations', 'cardinality', "0.N"),
        ('intent', 'cardinality', "0.1"),
        ('purpose', 'cardinality', "0.1"),
        ('units', 'cardinality', "0.1"),
        ('grid', 'cardinality', "0.1"),

    ),
    software.Composition: (

        ('couplings', 'type', unicode),
        ('description', 'type', unicode),

        ('couplings', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),

    ),
    software.Connection: (

        ('transformers', 'type', software.ProcessorComponent),
        ('target', 'type', software.ConnectionEndpoint),
        ('time_transformation', 'type', software.TimeTransformation),
        ('spatial_regridding', 'type', software.SpatialRegridding),
        ('sources', 'type', software.ConnectionEndpoint),
        ('time_profile', 'type', software.Timing),
        ('priming', 'type', shared.DataSource),
        ('type', 'type', unicode),
        ('properties', 'type', software.ConnectionProperty),
        ('time_lag', 'type', unicode),
        ('description', 'type', unicode),

        ('transformers', 'cardinality', "0.N"),
        ('target', 'cardinality', "0.1"),
        ('time_transformation', 'cardinality', "0.1"),
        ('spatial_regridding', 'cardinality', "0.N"),
        ('sources', 'cardinality', "0.N"),
        ('time_profile', 'cardinality', "0.1"),
        ('priming', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('time_lag', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    software.ConnectionEndpoint: (

        ('instance_id', 'type', unicode),
        ('data_source', 'type', shared.DataSource),
        ('properties', 'type', software.ConnectionProperty),

        ('instance_id', 'cardinality', "0.1"),
        ('data_source', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),

    ),
    software.ConnectionProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

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
    software.CouplingEndpoint: (

        ('instance_id', 'type', unicode),
        ('data_source', 'type', shared.DataSource),
        ('properties', 'type', software.CouplingProperty),

        ('instance_id', 'cardinality', "0.1"),
        ('data_source', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),

    ),
    software.CouplingProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

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
    software.EntryPoint: (

        ('name', 'type', unicode),

        ('name', 'cardinality', "0.1"),

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
    software.Parallelisation: (

        ('ranks', 'type', software.Rank),
        ('processes', 'type', int),

        ('ranks', 'cardinality', "0.N"),
        ('processes', 'cardinality', "1.1"),

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
    software.Rank: (

        ('max', 'type', int),
        ('value', 'type', int),
        ('increment', 'type', int),
        ('min', 'type', int),

        ('max', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),
        ('increment', 'cardinality', "0.1"),
        ('min', 'cardinality', "0.1"),

    ),
    software.SpatialRegridding: (

        ('user_method', 'type', software.SpatialRegriddingUserMethod),
        ('dimension', 'type', unicode),
        ('standard_method', 'type', unicode),
        ('properties', 'type', software.SpatialRegriddingProperty),

        ('user_method', 'cardinality', "0.1"),
        ('dimension', 'cardinality', "0.1"),
        ('standard_method', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),

    ),
    software.SpatialRegriddingProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    software.SpatialRegriddingUserMethod: (

        ('name', 'type', unicode),
        ('file', 'type', data.DataObject),

        ('name', 'cardinality', "1.1"),
        ('file', 'cardinality', "0.1"),

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
    software.TimeLag: (

        ('units', 'type', unicode),
        ('value', 'type', int),

        ('units', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    software.TimeTransformation: (

        ('description', 'type', unicode),
        ('mapping_type', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('mapping_type', 'cardinality', "1.1"),

    ),
    software.Timing: (

        ('units', 'type', unicode),
        ('is_variable_rate', 'type', bool),
        ('rate', 'type', int),
        ('end', 'type', datetime.datetime),
        ('start', 'type', datetime.datetime),

        ('units', 'cardinality', "0.1"),
        ('is_variable_rate', 'cardinality', "0.1"),
        ('rate', 'cardinality', "0.1"),
        ('end', 'cardinality', "0.1"),
        ('start', 'cardinality', "0.1"),

    ),
    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------


    (activity.Activity, 'funding_sources'): (

        ('type', unicode),

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
    (activity.Activity, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

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
    (activity.BoundaryCondition, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "boundaryCondition"),
    ),
    (activity.BoundaryCondition, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),

    (activity.Conformance, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'frequency'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'is_conformant'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (activity.Conformance, 'requirements'): (

        ('type', activity.NumericalRequirement),

        ('cardinality', "1.N"),

    ),
    (activity.Conformance, 'sources'): (

        ('type', shared.DataSource),

        ('cardinality', "0.N"),

    ),
    (activity.Conformance, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.DownscalingSimulation, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "1.1"),

    ),
    (activity.DownscalingSimulation, 'downscaled_from'): (

        ('type', shared.DataSource),

        ('cardinality', "1.1"),

    ),
    (activity.DownscalingSimulation, 'downscaling_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.DownscalingSimulation, 'downscaling_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.DownscalingSimulation, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.DownscalingSimulation, 'outputs'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.DownscalingSimulation, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.DownscalingSimulation, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.DownscalingSimulation, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (activity.Ensemble, 'members'): (

        ('type', activity.EnsembleMember),

        ('cardinality', "1.N"),

    ),
    (activity.Ensemble, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.Ensemble, 'outputs'): (

        ('type', shared.DataSource),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'types'): (

        ('type', unicode),

        ('cardinality', "1.N"),

    ),
    (activity.Ensemble, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.Ensemble, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (activity.EnsembleMember, 'ensemble'): (

        ('type', activity.Ensemble),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'ensemble_ids'): (

        ('type', shared.StandardName),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.EnsembleMember, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (activity.Experiment, 'generates'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'measurement_campaigns'): (

        ('type', activity.MeasurementCampaign),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'requires'): (

        ('type', activity.NumericalActivity),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'supports'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (activity.ExperimentRelationship, 'target'): (

        ('type', activity.ExperimentRelationshipTarget),

        ('cardinality', "1.1"),

    ),
    (activity.ExperimentRelationship, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.ExperimentRelationship, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.ExperimentRelationshipTarget, 'numerical_experiment'): (

        ('type', activity.NumericalExperiment),

        ('cardinality', "0.1"),

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
    (activity.InitialCondition, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "initialCondition"),
    ),
    (activity.InitialCondition, 'source'): (

        ('type', shared.DataSource),

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
    (activity.LateralBoundaryCondition, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "lateralBoundaryCondition"),
    ),
    (activity.LateralBoundaryCondition, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),

    (activity.MeasurementCampaign, 'duration'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (activity.MeasurementCampaign, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.MeasurementCampaign, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.MeasurementCampaign, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.MeasurementCampaign, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (activity.NumericalActivity, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalActivity, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalActivity, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalActivity, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (activity.NumericalExperiment, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalExperiment, 'experiment_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalExperiment, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalExperiment, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalExperiment, 'requirements'): (

        ('type', activity.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalExperiment, 'generates'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'measurement_campaigns'): (

        ('type', activity.MeasurementCampaign),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'requires'): (

        ('type', activity.NumericalActivity),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'supports'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (activity.NumericalRequirement, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirement, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirement, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalRequirement, 'options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalRequirement, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalRequirement, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),

    (activity.NumericalRequirementOption, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirementOption, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirementOption, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalRequirementOption, 'relationship'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirementOption, 'sub_options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

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
    (activity.OutputRequirement, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "outputRequirement"),
    ),
    (activity.OutputRequirement, 'source'): (

        ('type', shared.DataSource),

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
    (activity.PhysicalModification, 'is_conformant'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (activity.PhysicalModification, 'requirements'): (

        ('type', activity.NumericalRequirement),

        ('cardinality', "1.N"),

    ),
    (activity.PhysicalModification, 'sources'): (

        ('type', shared.DataSource),

        ('cardinality', "0.N"),

    ),
    (activity.PhysicalModification, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.Simulation, 'authors'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "1.1"),

    ),
    (activity.Simulation, 'conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'control_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'outputs'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'restarts'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'simulation_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'spinup_date_range'): (

        ('type', shared.ClosedDateRange),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'spinup_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.Simulation, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (activity.SimulationComposite, 'child'): (

        ('type', activity.Simulation),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'date_range'): (

        ('type', shared.DateRange),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'rank'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'authors'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'control_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'outputs'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'restarts'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'simulation_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'spinup_date_range'): (

        ('type', shared.ClosedDateRange),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'spinup_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (activity.SimulationRelationship, 'target'): (

        ('type', activity.SimulationRelationshipTarget),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRelationship, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRelationship, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.SimulationRelationshipTarget, 'simulation'): (

        ('type', shared.DocReference),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRelationshipTarget, 'target'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.SimulationRun, 'date_range'): (

        ('type', shared.DateRange),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRun, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRun, 'model'): (

        ('type', software.ModelComponent),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'authors'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRun, 'conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'control_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'outputs'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'restarts'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'simulation_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'spinup_date_range'): (

        ('type', shared.ClosedDateRange),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'spinup_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRun, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (activity.SpatioTemporalConstraint, 'date_range'): (

        ('type', shared.DateRange),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'spatial_resolution'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.SpatioTemporalConstraint, 'options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.SpatioTemporalConstraint, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "spatioTemporalConstraint"),
    ),
    (activity.SpatioTemporalConstraint, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),

    (data.DataContent, 'aggregation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataContent, 'frequency'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataContent, 'topic'): (

        ('type', data.DataTopic),

        ('cardinality', "1.1"),

    ),
    (data.DataContent, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

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

    (data.DataExtent, 'geographical'): (

        ('type', data.DataExtentGeographical),

        ('cardinality', "1.1"),

    ),
    (data.DataExtent, 'temporal'): (

        ('type', data.DataExtentTemporal),

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
    (data.DataExtentGeographical, 'south'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentGeographical, 'west'): (

        ('type', float),

        ('cardinality', "0.1"),

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

    (data.DataExtentTimeInterval, 'factor'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentTimeInterval, 'radix'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.DataExtentTimeInterval, 'unit'): (

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

    (data.DataObject, 'acronym'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'child_object'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'content'): (

        ('type', data.DataContent),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'data_status'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'distribution'): (

        ('type', data.DataDistribution),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'extent'): (

        ('type', data.DataExtent),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'geometry_model'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'hierarchy_level'): (

        ('type', data.DataHierarchyLevel),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'keyword'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (data.DataObject, 'parent_object'): (

        ('type', data.DataObject),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'properties'): (

        ('type', data.DataProperty),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'restriction'): (

        ('type', data.DataRestriction),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'source_simulation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'storage'): (

        ('type', data.DataStorage),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (data.DataProperty, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (data.DataRestriction, 'license'): (

        ('type', shared.License),

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

    (data.DataStorage, 'format'): (

        ('type', unicode),

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
    (data.DataStorage, 'size'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (data.DataStorageDb, 'access_string'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'owner'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'table'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'modification_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'size'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (data.DataStorageFile, 'file_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'file_system'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'path'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'modification_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'size'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (data.DataStorageIp, 'file_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'host'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'path'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'protocol'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'modification_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'size'): (

        ('type', int),

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

    (grids.CoordinateList, 'has_constant_offset'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.CoordinateList, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.CoordinateList, 'uom'): (

        ('type', unicode),

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
    (grids.GridExtent, 'minimum_longitude'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridExtent, 'units'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (grids.GridMosaic, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (grids.GridMosaic, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'extent'): (

        ('type', grids.GridExtent),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'has_congruent_tiles'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridMosaic, 'is_leaf'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (grids.GridMosaic, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'mnemonic'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'mosaic_count'): (

        ('type', int),

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
    (grids.GridMosaic, 'tile_count'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'tiles'): (

        ('type', grids.GridTile),

        ('cardinality', "0.N"),

    ),
    (grids.GridMosaic, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (grids.GridProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

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

    (grids.GridTile, 'area'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'cell_array'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'cell_ref_array'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'coord_file'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'coordinate_pole'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'discretization_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'extent'): (

        ('type', grids.GridExtent),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'geometry_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'grid_north_pole'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'horizontal_crs'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'horizontal_resolution'): (

        ('type', grids.GridTileResolutionType),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'is_conformal'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'is_regular'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'is_terrain_following'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'is_uniform'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'mnemonic'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'nx'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'ny'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'nz'): (

        ('type', int),

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
    (grids.GridTile, 'simple_grid_geom'): (

        ('type', grids.SimpleGridGeometry),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'vertical_crs'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'vertical_resolution'): (

        ('type', grids.GridTileResolutionType),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'zcoords'): (

        ('type', grids.VerticalCoordinateList),

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

    (grids.SimpleGridGeometry, 'dim_order'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.SimpleGridGeometry, 'is_mesh'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.SimpleGridGeometry, 'num_dims'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (grids.SimpleGridGeometry, 'xcoords'): (

        ('type', grids.CoordinateList),

        ('cardinality', "1.1"),

    ),
    (grids.SimpleGridGeometry, 'ycoords'): (

        ('type', grids.CoordinateList),

        ('cardinality', "1.1"),

    ),
    (grids.SimpleGridGeometry, 'zcoords'): (

        ('type', grids.CoordinateList),

        ('cardinality', "0.1"),

    ),

    (grids.VerticalCoordinateList, 'form'): (

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
    (grids.VerticalCoordinateList, 'has_constant_offset'): (

        ('type', bool),

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

    (misc.DocumentSet, 'data'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (misc.DocumentSet, 'ensembles'): (

        ('type', activity.Ensemble),

        ('cardinality', "0.N"),

    ),
    (misc.DocumentSet, 'experiment'): (

        ('type', activity.NumericalExperiment),

        ('cardinality', "0.1"),

    ),
    (misc.DocumentSet, 'grids'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.N"),

    ),
    (misc.DocumentSet, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (misc.DocumentSet, 'model'): (

        ('type', software.ModelComponent),

        ('cardinality', "0.1"),

    ),
    (misc.DocumentSet, 'platform'): (

        ('type', shared.Platform),

        ('cardinality', "0.1"),

    ),
    (misc.DocumentSet, 'simulation'): (

        ('type', activity.SimulationRun),

        ('cardinality', "0.1"),

    ),

    (quality.CimQuality, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (quality.CimQuality, 'reports'): (

        ('type', quality.Report),

        ('cardinality', "0.N"),

    ),

    (quality.Evaluation, 'date'): (

        ('type', datetime.datetime),

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
    (quality.Evaluation, 'explanation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'specification'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'specification_hyperlink'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'type_hyperlink'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (quality.Measure, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Measure, 'identification'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Measure, 'name'): (

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

    (shared.Change, 'author'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.1"),

    ),
    (shared.Change, 'date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.Change, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Change, 'details'): (

        ('type', shared.ChangeProperty),

        ('cardinality', "1.N"),

    ),
    (shared.Change, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Change, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.ChangeProperty, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ChangeProperty, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ChangeProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ChangeProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Citation, 'alternative_title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'collective_title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'date_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'organisation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'role'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'type'): (

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
    (shared.ClosedDateRange, 'duration'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Compiler, 'environment_variables'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Compiler, 'language'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Compiler, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Compiler, 'options'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Compiler, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Compiler, 'version'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.Daily360, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Daily360, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.Daily360, 'range'): (

        ('type', shared.DateRange),

        ('cardinality', "0.1"),

    ),

    (shared.DataSource, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.DateRange, 'duration'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.DocMetaInfo, 'author'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'create_date'): (

        ('type', datetime.datetime),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'drs_keys'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (shared.DocMetaInfo, 'drs_path'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'external_ids'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (shared.DocMetaInfo, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'institute'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'project'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'sort_key'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'source'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'source_key'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'sub_projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (shared.DocMetaInfo, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'type_display_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'type_sort_key'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'update_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'version'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),

    (shared.DocReference, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'changes'): (

        ('type', shared.Change),

        ('cardinality', "0.N"),

    ),
    (shared.DocReference, 'constraint_vocabulary'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'context'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'external_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'institute'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'linkage'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocReference, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocReference, 'protocol'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'relationship'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocReference, 'url'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'version'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (shared.License, 'contact'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.License, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.License, 'is_unrestricted'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (shared.License, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Machine, 'cores_per_processor'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'interconnect'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'libraries'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (shared.Machine, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'maximum_processors'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Machine, 'operating_system'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'processor_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'system'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'vendor'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.MachineCompilerUnit, 'compilers'): (

        ('type', shared.Compiler),

        ('cardinality', "0.N"),

    ),
    (shared.MachineCompilerUnit, 'machine'): (

        ('type', shared.Machine),

        ('cardinality', "1.1"),

    ),

    (shared.OpenDateRange, 'end'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.OpenDateRange, 'start'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.OpenDateRange, 'duration'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.PerpetualPeriod, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.PerpetualPeriod, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.PerpetualPeriod, 'range'): (

        ('type', shared.DateRange),

        ('cardinality', "0.1"),

    ),

    (shared.Platform, 'contacts'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (shared.Platform, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Platform, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Platform, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (shared.Platform, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Platform, 'units'): (

        ('type', shared.MachineCompilerUnit),

        ('cardinality', "1.N"),

    ),

    (shared.Property, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Property, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.RealCalendar, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.RealCalendar, 'length'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.RealCalendar, 'range'): (

        ('type', shared.DateRange),

        ('cardinality', "0.1"),

    ),

    (shared.Relationship, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.ResponsibleParty, 'abbreviation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'address'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'email'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'individual_name'): (

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
    (shared.ResponsibleParty, 'url'): (

        ('type', unicode),

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

    (shared.StandardName, 'is_open'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (shared.StandardName, 'standards'): (

        ('type', shared.Standard),

        ('cardinality', "0.N"),

    ),
    (shared.StandardName, 'value'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (software.Component, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.Component, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.ComponentLanguage, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.ComponentLanguage, 'properties'): (

        ('type', software.ComponentLanguageProperty),

        ('cardinality', "0.N"),

    ),

    (software.ComponentLanguageProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentLanguageProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.ComponentProperty, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'description'): (

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
    (software.ComponentProperty, 'is_represented'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (software.ComponentProperty, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.ComponentProperty, 'standard_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'sub_properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'units'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'values'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'purpose'): (

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

    (software.Connection, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'priming'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'properties'): (

        ('type', software.ConnectionProperty),

        ('cardinality', "0.N"),

    ),
    (software.Connection, 'sources'): (

        ('type', software.ConnectionEndpoint),

        ('cardinality', "0.N"),

    ),
    (software.Connection, 'spatial_regridding'): (

        ('type', software.SpatialRegridding),

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
    (software.Connection, 'time_profile'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'time_transformation'): (

        ('type', software.TimeTransformation),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'transformers'): (

        ('type', software.ProcessorComponent),

        ('cardinality', "0.N"),

    ),
    (software.Connection, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.ConnectionEndpoint, 'data_source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (software.ConnectionEndpoint, 'instance_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ConnectionEndpoint, 'properties'): (

        ('type', software.ConnectionProperty),

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

    (software.Coupling, 'connections'): (

        ('type', software.Connection),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'is_fully_specified'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (software.Coupling, 'priming'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'properties'): (

        ('type', software.CouplingProperty),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'purpose'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.Coupling, 'sources'): (

        ('type', software.CouplingEndpoint),

        ('cardinality', "1.N"),

    ),
    (software.Coupling, 'spatial_regriddings'): (

        ('type', software.SpatialRegridding),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'target'): (

        ('type', software.CouplingEndpoint),

        ('cardinality', "1.1"),

    ),
    (software.Coupling, 'time_lag'): (

        ('type', software.TimeLag),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'time_profile'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'time_transformation'): (

        ('type', software.TimeTransformation),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'transformers'): (

        ('type', software.ProcessorComponent),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

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

    (software.CouplingProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.CouplingProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.Deployment, 'deployment_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.Deployment, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Deployment, 'executable_arguments'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.Deployment, 'executable_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Deployment, 'parallelisation'): (

        ('type', software.Parallelisation),

        ('cardinality', "0.1"),

    ),
    (software.Deployment, 'platform'): (

        ('type', shared.Platform),

        ('cardinality', "0.1"),

    ),

    (software.EntryPoint, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.ModelComponent, 'activity'): (

        ('type', activity.Activity),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (software.ModelComponent, 'timing'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'types'): (

        ('type', unicode),

        ('cardinality', "1.N"),

    ),
    (software.ModelComponent, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.ModelComponent, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'purpose'): (

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

    (software.ProcessorComponent, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (software.ProcessorComponent, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.ProcessorComponent, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.Rank, 'increment'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (software.Rank, 'max'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (software.Rank, 'min'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (software.Rank, 'value'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (software.SpatialRegridding, 'dimension'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SpatialRegridding, 'properties'): (

        ('type', software.SpatialRegriddingProperty),

        ('cardinality', "0.N"),

    ),
    (software.SpatialRegridding, 'standard_method'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SpatialRegridding, 'user_method'): (

        ('type', software.SpatialRegriddingUserMethod),

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

    (software.SpatialRegriddingUserMethod, 'file'): (

        ('type', data.DataObject),

        ('cardinality', "0.1"),

    ),
    (software.SpatialRegriddingUserMethod, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (software.StatisticalModelComponent, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (software.StatisticalModelComponent, 'timing'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'types'): (

        ('type', unicode),

        ('cardinality', "1.N"),

    ),
    (software.StatisticalModelComponent, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.StatisticalModelComponent, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.TimeLag, 'units'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.TimeLag, 'value'): (

        ('type', int),

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

    (software.Timing, 'end'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.Timing, 'is_variable_rate'): (

        ('type', bool),

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
    (software.Timing, 'units'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
}

# Count of class constraints.
TOTAL_CONSTRAINTS = sum(len(CONSTRAINTS[c]) for c in CLASSES)

# ------------------------------------------------
# Type documentation strings.
# ------------------------------------------------
DOC_STRINGS = {
    # ------------------------------------------------
    # Packages.
    # ------------------------------------------------

    activity: "Types that describe context against which climate models are run.",
    data: "Types that describe output that climate models emit.",
    grids: "Types that describe the grids that climate models plot.",
    misc: "Miscellaneous types.",
    quality: "Types that describe the quailty of output that climate models emit.",
    shared: "Shared types that might be imported from other packages within the ontology.",
    software: "Types that describe the climate models software.",

    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    activity.Activity: """
        An abstract class used as the parent of MeasurementCampaigns, Projects, Experiments, and NumericalActivities.

    """,
    activity.BoundaryCondition: """
        A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).

    """,
    activity.Conformance: """
        A conformance class maps how a configured model component met a specific numerical requirement.  For example, for a double CO2 boundary condition, a model component might read a CO2 dataset in which CO2 has been doubled, or it might modify a parameterisation (presumably with a factor of two somewhere).  So, the conformance links a requirement to a DataSource (which can be either an actual DataObject or a property of a model component).  In some cases a model/simulation may _naturally_ conform to a requirement.  In this case there would be no reference to a DataSource but the conformant attribute would be true.  If something is purpopsefully non-conformant then the conformant attribute would be false.

    """,
    activity.DownscalingSimulation: """
        A simulation is the implementation of a numerical experiment.  A simulation can be made up of 'child' simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

    """,
    activity.Ensemble: """
        An ensemble is made up of two or more simulations which are to be compared against each other to create ensemble statistics. Ensemble members can differ in terms of initial conditions, physical parameterisation and the model used. An ensemble bundles together sets of ensembleMembers, all of which reference the same Simulation(Run) and include one or more changes.

    """,
    activity.EnsembleMember: """
        A simulation is the implementation of a numerical experiment.  A simulation can be made up of 'child' simulations aggregated together to form a 'simulation composite'.  The 'parent' simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

    """,
    activity.Experiment: """
        An experiment might be an activity which is both observational and numerical in focus, for example, a measurement campaign and numerical experiments for an alpine experiment.  It is a place for the scientific description of the reason why an experiment was made.

    """,
    activity.ExperimentRelationship: """
        Contains a set of relationship types specific to a experiment document that can be used to describe its genealogy.

    """,
    activity.ExperimentRelationshipTarget: """
        Creates and returns instance of experiment_relationship_target class.

    """,
    activity.InitialCondition: """
        An initial condition is a numerical requirement on a model prognostic variable value at time zero.

    """,
    activity.LateralBoundaryCondition: """
        A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).

    """,
    activity.MeasurementCampaign: """
        Creates and returns instance of measurement_campaign class.

    """,
    activity.NumericalActivity: """
        Creates and returns instance of numerical_activity class.

    """,
    activity.NumericalExperiment: """
        A numerical experiment may be generated by an experiment, in which case it is inSupportOf the experiment. But a numerical experiment may also exist as an activity in its own right (as it might be if it were needed for a MIP). Examples: AR4 individual experiments, AR5 individual experiments, RAPID THC experiments etc.

    """,
    activity.NumericalRequirement: """
        A description of the requirements of particular experiments.  Numerical Requirements can be initial conditions, boundary conditions, or physical modificiations.

    """,
    activity.NumericalRequirementOption: """
        A NumericalRequirement that is being used as a set of related requirements; For example if a requirement is to use 1 of 3 boundary conditions, then that 'parent' requirement would have three 'child' RequirmentOptions (each of one with the XOR optionRelationship).

    """,
    activity.OutputRequirement: """
        Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

    """,
    activity.PhysicalModification: """
        Physical modification is the implementation of a boundary condition numerical requirement that is achieved within the model code rather than from some external source file. It  might include, for example,  a specific rate constant within a chemical reaction, or coefficient value(s) in a parameterisation.  For example, one might require a numerical experiment where specific chemical reactions were turned off - e.g. no heterogeneous chemistry.

    """,
    activity.Simulation: """
        A simulation is the implementation of a numerical experiment.  A simulation can be made up of 'child' simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

    """,
    activity.SimulationComposite: """
        A SimulationComposite is an aggregation of Simulations. With the aggreation connector between Simulation and SimulationComposite(SC) the SC can be made up of both SimulationRuns and SCs. The SimulationComposite is the new name for the concept of SimulationCollection: A simulation can be made up of 'child' simulations aggregated together to form a 'simulation composite'.  The 'parent' simulation can be made up of whole or partial child simulations and the SimulationComposite attributes need to be able to capture this.

    """,
    activity.SimulationRelationship: """
        Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

    """,
    activity.SimulationRelationshipTarget: """
        Creates and returns instance of simulation_relationship_target class.

    """,
    activity.SimulationRun: """
        A SimulationRun is, as the name implies, one single model run. A SimulationRun is a Simulation. There is a one to one association between SimulationRun and (a top-level) SoftwarePackage::ModelComponent.

    """,
    activity.SpatioTemporalConstraint: """
        Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

    """,
    data.DataContent: """
        The contents of the data object; like ISO: MD_ContentInformation.

    """,
    data.DataDistribution: """
        Describes how a DataObject is distributed.

    """,
    data.DataExtent: """
        A data object extent represents the geographical and temporal coverage associated with a data object.

    """,
    data.DataExtentGeographical: """
        A data object geographical extent represents the geographical coverage associated with a data object.

    """,
    data.DataExtentTemporal: """
        A data object temporal extent represents the temporal coverage associated with a data object.

    """,
    data.DataExtentTimeInterval: """
        A data object temporal extent represents the temporal coverage associated with a data object.

    """,
    data.DataHierarchyLevel: """
        The type of data object that is grouped together into a particular hierarchy.  Currently, this is made up of terms describing how the Met Office splits up archived data and how THREDDS categorises variables.

    """,
    data.DataObject: """
        A DataObject describes a unit of data.  DataObjects can be grouped hierarchically.  The attributes hierarchyLevelName and hierarchyLevelValue describe how objects are grouped.

    """,
    data.DataProperty: """
        A property of a DataObject. Currently this is intended to be used to record CF specific information (like packing, scaling, etc.) for OASIS4.

    """,
    data.DataRestriction: """
        An access or use restriction on some element of the DataObject actual data.

    """,
    data.DataStorage: """
        Describes the method that the DataObject is stored. An abstract class with specific child classes for each supported method.

    """,
    data.DataStorageDb: """
        Contains attributes to describe a DataObject stored as a database file.

    """,
    data.DataStorageFile: """
        Contains attributes to describe a DataObject stored as a single file.

    """,
    data.DataStorageIp: """
        Contains attributes to describe a DataObject stored as a database file.

    """,
    data.DataTopic: """
        Describes the content of a data object: the variable name, units, etc.

    """,
    grids.CoordinateList: """
        The CoordList type may be used to specify a list of coordinates, typically for the purpose of defining coordinates along the X, Y or Z axes. The length of the coordinate list is given by the attribute of that name. This may be used by software to allocate memory in advance of storing the coordinate values. The hasConstantOffset attribute may be used to indicate that the coordinate list consists of values with constant offset (spacing). In this case only the first coordinate value and the offset (spacing) value need to be specified; however, the length attribute must still define the final as-built size of the coordinate list.

    """,
    grids.GridExtent: """
        DataType for recording the geographic extent of a gridMosaic or gridTile.

    """,
    grids.GridMosaic: """
        The GridMosaic class is used to define the geometry properties of an earth system model grid or an exchange grid. Such a grid definition may then be referenced by any number of earth system models. A GridMosaic object consists either of 1 or more child GridMosaics, or one or more child GridTiles, but not both. In the latter case the isLeaf property should be set to true, indicating that the mosaic is a leaf mosaic.

    """,
    grids.GridProperty: """
        Creates and returns instance of grid_property class.

    """,
    grids.GridSpec: """
        This is a container class for GridSpec objects. A GridSpec object can contain one or more esmModelGrid objects, and one or more esmExchangeGrid objects. These objects may be serialised to one or possibly several files according to taste. Since GridSpec is sub-typed from GML's AbstractGeometryType it can, and should, be identified using a gml:id attribute.

    """,
    grids.GridTile: """
        The GridTile class is used to model an individual grid tile contained within a grid mosaic. A GridTile consists of an array of grid cells which may be defined in one of four ways: 1) for simple grids, by use of the SimpleGridGeometry data type; 2) by defining an array of GridCell objects; 3) by specifying an array of references to externally defined GridCell objects; or 4) by specifying a URI to a remote data file containing the grid cell definitions.  For all but the simplest grid tiles, it is envisaged that method 4 above will be the most frequently used option. However, it should be remembered that the CIM is primarily concerned with encoding climate model metadata. Specifying the coordinates of individual grid tiles and cells will most likely not be required as part of such metadata descriptions.  A GridTile object is associated with a geodetic or projected CRS via the horizontalCRS property, and with a vertical CRS via the verticalCRS property.

    """,
    grids.GridTileResolutionType: """
        Provides a description and set of named properties for the horizontal or vertical resolution.

    """,
    grids.SimpleGridGeometry: """
        SimpleGridGeometry:This property may be used to define the coordinates of the nodes or cells making up a simple (i.e. uniform or regular) grid tile. More details are provided in the description of the SimpleGridGeometry data type.

    """,
    grids.VerticalCoordinateList: """
        There are some specific attributes that are associated with vertical coordinates.

    """,
    misc.DocumentSet: """
        Represents a bundled set of documents.

    """,
    quality.CimQuality: """
        The starting point for a quality record.  It can contain any number of issues and reports.  An issue is an open-ended description of some issue about a CIM instance.  A record is a prescribed description of some specific quantitative measure that has been applied to a CIM instance.

    """,
    quality.Evaluation: """
        Creates and returns instance of evaluation class.

    """,
    quality.Measure: """
        Creates and returns instance of measure class.

    """,
    quality.Report: """
        Creates and returns instance of report class.

    """,
    shared.Calendar: """
        Describes a method of calculating a span of dates.

    """,
    shared.Change: """
        A description of [a set of] changes applied at a particular time, by a particular party, to a particular unit of metadata.

    """,
    shared.ChangeProperty: """
        A description of a single change applied to a single target.  Every ChangeProperty has a description, and may also have a name from a controlled vocabulary and a value.

    """,
    shared.Citation: """
        An academic reference to published work.

    """,
    shared.ClosedDateRange: """
        A date range with specified start and end points.

    """,
    shared.Compiler: """
        A description of a compiler used on a particular platform.

    """,
    shared.Daily360: """
        Creates and returns instance of daily_360 class.

    """,
    shared.DataSource: """
        A DataSource can be realised by either a DataObject (file), a DataContent (variable), a Component (model), or a ComponentProperty (variable); all of those can supply data.

    """,
    shared.DateRange: """
        Creates and returns instance of date_range class.

    """,
    shared.DocMetaInfo: """
        Encapsulates document meta information used by es-doc machinery. Will not normally be
    populated by humans. May duplicate information held in 'visible' metadata.

    """,
    shared.DocReference: """
        A reference to another cim entity.

    """,
    shared.License: """
        A description of a license restricting access to a unit of data or software.

    """,
    shared.Machine: """
        A description of a machine used by a particular platform.

    """,
    shared.MachineCompilerUnit: """
        Associates a machine with a [set of] compilers.  This is a separate class in case a platform needs to specify more than one machine/compiler pair.

    """,
    shared.OpenDateRange: """
        A date range without a specified start and/or end point.

    """,
    shared.PerpetualPeriod: """
        Creates and returns instance of perpetual_period class.

    """,
    shared.Platform: """
        A platform is a description of resources used to deploy a component/simulation.  A platform pairs a machine with a (set of) compilers.  There is also a point of contact for the platform.

    """,
    shared.Property: """
        A simple name/value pair representing a property of some entity or other.

    """,
    shared.RealCalendar: """
        Creates and returns instance of real_calendar class.

    """,
    shared.Relationship: """
        A record of a relationship between one document and another. This class is abstract; specific document types must specialise this class for their relationshipTypes to be included in a document's genealogy.

    """,
    shared.ResponsibleParty: """
        A person/organsiation responsible for some aspect of a climate science artefact.

    """,
    shared.Standard: """
        Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

    """,
    shared.StandardName: """
        Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

    """,
    software.Component: """
        A SofwareComponent is an abstract component from which all other components derive. It represents an element that takes input data and generates output data. A SoftwareCompnent can include nested 'child' components. Every component can have 'componentProperties' which describe the scientific properties that a component simulates (for example, temperature, pressure, etc.) and the numerical properties that influence how a component performs its simulation (for example, the force of gravity). A SoftwareComponent can also have a Deployment, which describes how software is deployed onto computing resources. And a SoftwareComponent can have a composition, which describes how ComponentProperties are coupled together either to/from other SoftwareComponents or external data files. The properties specified by a component's composition must be owned by that component or a child of that component; child components cannot couple together their parents' properties.

    """,
    software.ComponentLanguage: """
        Details of the programming language a component is written in. There is an assumption that all EntryPoints use the same ComponentLanguage.

    """,
    software.ComponentLanguageProperty: """
        This provides a place to include language-specific information. Every property is basically a name/value pair, where the names are things like: moduleName, reservedUnits, reservedNames (these are all examples of Fortran-specific properties).

    """,
    software.ComponentProperty: """
        ComponentProperties include things that a component simulates (ie: pressure, humidity) and things that prescribe that simulation (ie: gravity, choice of advection scheme). Note that this is a specialisation of shared::DataSource. data::DataObject is also a specialisation of shared::DataSource. This allows software::Connections and/or activity::Conformance to refer to either ComponentProperties or DataObjects.

    """,
    software.Composition: """
        The set of Couplings used by a Component. Couplings can only occur between child components. That is, a composition must belong to an ancestor component of the components whose fields are being connected.

    """,
    software.Connection: """
        A Connection represents a link from a source DataSource to a target DataSource.  These can either be ComponentProperties (ie: the values come from an internal component) or DataObjects (ie: the values come from an external file).   It can be associated with another software component (a transformer).  If present, the rate, lag, timeTransformation, and spatialRegridding override that of the parent coupling.  Note that there is the potential for multiple connectionSource & connectionTarget and multiple couplingSources & couplingTargets.  This may lead users to wonder how to match up a connection source (a ComponentProperty) with its coupling source (a SoftwareComponent). Clever logic is not required though; because the sources and targets are listed by reference, they can be found in a CIM document and the parent can be navigated to from there - there is no need to consult the source or target of the coupling.

    """,
    software.ConnectionEndpoint: """
        The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).

    """,
    software.ConnectionProperty: """
        A ConnectionProperty is a name/value pair used to specify OASIS-specific properties.

    """,
    software.Coupling: """
        A coupling represents a set of Connections between a source and target component. Couplings can be complete or incomplete. If they are complete then they must include all Connections between model properties. If they are incomplete then the connections can be underspecified or not listed at all.

    """,
    software.CouplingEndpoint: """
        The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).

    """,
    software.CouplingProperty: """
        A CouplingProperty is a name/value pair used to specify OASIS-specific properties.

    """,
    software.Deployment: """
        Gives information about the technical properties of a component: what machine it was run on, which compilers were used, how it was parallised, etc. A deployment basically associates a deploymentDate with a Platform. A deployment only exists if something has been deployed. A platform, in contrast, can exist independently, waiting to be used in deployments.

    """,
    software.EntryPoint: """
        Describes a function or subroutine of a SoftwareComponent. BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model. Currently, a very basic schedule can be approximated by using the 'proceeds' and 'follows' attributes, however a more complete system is required for full BFG compatibility. Every EntryPoint can have a set of arguments associated with it. These reference (previously defined) ComponentProperties.

    """,
    software.ModelComponent: """
        A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.

    """,
    software.Parallelisation: """
        Describes how a deployment has been parallelised across a computing platform.

    """,
    software.ProcessorComponent: """
        A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.

    """,
    software.Rank: """
        Creates and returns instance of rank class.

    """,
    software.SpatialRegridding: """
        Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.

    """,
    software.SpatialRegriddingProperty: """
        Used for OASIS-specific regridding information (ie: masked, order, normalisation, etc.)

    """,
    software.SpatialRegriddingUserMethod: """
        Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.

    """,
    software.StatisticalModelComponent: """
        Creates and returns instance of statistical_model_component class.

    """,
    software.TimeLag: """
        The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.

    """,
    software.TimeTransformation: """
        The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.

    """,
    software.Timing: """
        Provides information about the rate of couplings and connections and/or the timing characteristics of individual components - for example, the start and stop times that the component was run for or the units of time that a component is able to model (in a single timestep).

    """,

    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------

    (activity.Activity, 'funding_sources'):
        "The entities that funded this activity.",
    (activity.Activity, 'projects'):
        "The project(s) that this activity is associated with (ie: CMIP5, AMIP, etc).",
    (activity.Activity, 'rationales'):
        "For what purpose is this activity being performed?",
    (activity.Activity, 'responsible_parties'):
        "The point of contact(s) for this activity.This includes, among others, the principle investigator.",
    (activity.Conformance, 'description'):
        None,
    (activity.Conformance, 'frequency'):
        None,
    (activity.Conformance, 'is_conformant'):
        "Records whether or not this conformance satisfies the requirement.  A simulation should have at least one conformance mapping to every experimental requirement.  If a simulation satisfies the requirement - the usual case - then conformant should have a value of true.  If conformant is true but there is no reference to a source for the conformance, then we can assume that the simulation conforms to the requirement _naturally_, that is without having to modify code or inputs. If a simulation does not conform to a requirement then conformant should be set to false.",
    (activity.Conformance, 'requirements'):
        "Points to the NumericalRequirement that the simulation in question is conforming to.",
    (activity.Conformance, 'sources'):
        "Points to the DataSource used to conform to a particular Requirement.   This may be part of an activity::simulation or a software::component.  It can be either a DataObject or a SoftwareComponent or a ComponentProperty.  It could also be by using particular attributes of, say, a SoftwareComponent, but in that case the recommended practise is to reference the component and add appropriate text in the conformance description attribute.",
    (activity.Conformance, 'type'):
        "Describes the method that this simulation conforms to an experimental requirement (in case it is not specified by the change property of the reference to the source of this conformance)",
    (activity.DownscalingSimulation, 'calendar'):
        None,
    (activity.DownscalingSimulation, 'downscaled_from'):
        None,
    (activity.DownscalingSimulation, 'downscaling_id'):
        None,
    (activity.DownscalingSimulation, 'downscaling_type'):
        None,
    (activity.DownscalingSimulation, 'inputs'):
        "Implemented as a mapping from a source to target; can be a forcing file, a boundary condition, etc.",
    (activity.DownscalingSimulation, 'meta'):
        "Injected document metadata.",
    (activity.DownscalingSimulation, 'outputs'):
        None,
    (activity.Ensemble, 'members'):
        None,
    (activity.Ensemble, 'meta'):
        "Injected document metadata.",
    (activity.Ensemble, 'outputs'):
        "Points to the DataSource used to conform to a particular Requirement.   This may be part of an activity::simulation or a software::component.  It can be either a DataObject or a SoftwareComponent or a ComponentProperty.  It could also be by using particular attributes of, say, a SoftwareComponent, but in that case the recommended practise is to reference the component and add appropriate text in the conformance description attribute.",
    (activity.Ensemble, 'types'):
        None,
    (activity.EnsembleMember, 'ensemble'):
        None,
    (activity.EnsembleMember, 'ensemble_ids'):
        None,
    (activity.EnsembleMember, 'simulation'):
        None,
    (activity.Experiment, 'generates'):
        None,
    (activity.Experiment, 'measurement_campaigns'):
        None,
    (activity.Experiment, 'requires'):
        None,
    (activity.Experiment, 'supports'):
        None,
    (activity.ExperimentRelationship, 'target'):
        None,
    (activity.ExperimentRelationship, 'type'):
        None,
    (activity.ExperimentRelationshipTarget, 'numerical_experiment'):
        None,
    (activity.MeasurementCampaign, 'duration'):
        None,
    (activity.NumericalActivity, 'description'):
        "A free-text description of the experiment.",
    (activity.NumericalActivity, 'long_name'):
        "The name of the experiment (that is recognized externally).",
    (activity.NumericalActivity, 'short_name'):
        "The name of the experiment (that is used internally).",
    (activity.NumericalActivity, 'supports'):
        None,
    (activity.NumericalExperiment, 'description'):
        "A free-text description of the experiment.",
    (activity.NumericalExperiment, 'experiment_id'):
        "An experiment ID takes the form <number>.<number>[-<letter>].",
    (activity.NumericalExperiment, 'long_name'):
        "The name of the experiment (that is recognized externally).",
    (activity.NumericalExperiment, 'meta'):
        "Injected document metadata.",
    (activity.NumericalExperiment, 'requirements'):
        "The name of the experiment (that is used internally).",
    (activity.NumericalExperiment, 'short_name'):
        "The name of the experiment (that is used internally).",
    (activity.NumericalRequirement, 'description'):
        None,
    (activity.NumericalRequirement, 'id'):
        None,
    (activity.NumericalRequirement, 'name'):
        None,
    (activity.NumericalRequirement, 'options'):
        None,
    (activity.NumericalRequirement, 'requirement_type'):
        "Type of reqirement to which the experiment must conform.",
    (activity.NumericalRequirement, 'source'):
        None,
    (activity.NumericalRequirementOption, 'description'):
        None,
    (activity.NumericalRequirementOption, 'id'):
        None,
    (activity.NumericalRequirementOption, 'name'):
        None,
    (activity.NumericalRequirementOption, 'relationship'):
        "Describes how this optional (child) requirement is related to its sibling requirements.  For example, a NumericalRequirement could consist of a set of optional requirements each with an 'OR' relationship meaning use this boundary condition _or_ that one.",
    (activity.NumericalRequirementOption, 'sub_options'):
        None,
    (activity.Simulation, 'authors'):
        "List of associated authors.",
    (activity.Simulation, 'calendar'):
        None,
    (activity.Simulation, 'conformances'):
        None,
    (activity.Simulation, 'control_simulation'):
        "Points to a simulation being used as the basis (control) run.  Note that only 'derived' simulations can describe something as being control; a simulation should not know if it is being used itself as the control of some other run.",
    (activity.Simulation, 'deployments'):
        None,
    (activity.Simulation, 'inputs'):
        "Implemented as a mapping from a source to target; can be a forcing file, a boundary condition, etc.",
    (activity.Simulation, 'outputs'):
        None,
    (activity.Simulation, 'restarts'):
        None,
    (activity.Simulation, 'simulation_id'):
        None,
    (activity.Simulation, 'spinup_date_range'):
        "The date range that a simulation is engaged in spinup.",
    (activity.Simulation, 'spinup_simulation'):
        "The (external) simulation used during 'spinup.'  Note that this element can be used in conjuntion with spinupDateRange.  If a simulation has the latter but not the former, then one can assume that the simulation is performing its own spinup.",
    (activity.SimulationComposite, 'child'):
        None,
    (activity.SimulationComposite, 'date_range'):
        None,
    (activity.SimulationComposite, 'meta'):
        "Injected document metadata.",
    (activity.SimulationComposite, 'rank'):
        "Position of a simulation in the SimulationComposite timeline. eg:  Is this the first (rank = 1) or second (rank = 2) simulation",
    (activity.SimulationRelationship, 'target'):
        None,
    (activity.SimulationRelationship, 'type'):
        None,
    (activity.SimulationRelationshipTarget, 'simulation'):
        None,
    (activity.SimulationRelationshipTarget, 'target'):
        None,
    (activity.SimulationRun, 'date_range'):
        None,
    (activity.SimulationRun, 'meta'):
        "Injected document metadata.",
    (activity.SimulationRun, 'model'):
        None,
    (activity.SpatioTemporalConstraint, 'date_range'):
        None,
    (activity.SpatioTemporalConstraint, 'spatial_resolution'):
        None,
    (data.DataContent, 'aggregation'):
        "Describes how the content has been aggregated together: sum, min, mean, max, ...",
    (data.DataContent, 'frequency'):
        "Describes the frequency of the data content: daily, hourly, ...",
    (data.DataContent, 'topic'):
        None,
    (data.DataDistribution, 'access'):
        None,
    (data.DataDistribution, 'fee'):
        None,
    (data.DataDistribution, 'format'):
        None,
    (data.DataDistribution, 'responsible_party'):
        None,
    (data.DataExtent, 'geographical'):
        None,
    (data.DataExtent, 'temporal'):
        None,
    (data.DataExtentGeographical, 'east'):
        None,
    (data.DataExtentGeographical, 'north'):
        None,
    (data.DataExtentGeographical, 'south'):
        None,
    (data.DataExtentGeographical, 'west'):
        None,
    (data.DataExtentTemporal, 'begin'):
        None,
    (data.DataExtentTemporal, 'end'):
        None,
    (data.DataExtentTemporal, 'time_interval'):
        None,
    (data.DataExtentTimeInterval, 'factor'):
        None,
    (data.DataExtentTimeInterval, 'radix'):
        None,
    (data.DataExtentTimeInterval, 'unit'):
        None,
    (data.DataHierarchyLevel, 'is_open'):
        None,
    (data.DataHierarchyLevel, 'name'):
        "What level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.",
    (data.DataHierarchyLevel, 'value'):
        "What is the name of the specific HierarchyLevel this DataObject is being organised at (ie: if the HierarchyLevel is 'run' then the name might be the runid).",
    (data.DataObject, 'acronym'):
        None,
    (data.DataObject, 'child_object'):
        None,
    (data.DataObject, 'citations'):
        None,
    (data.DataObject, 'content'):
        "The content of a DataObject corresponds to a variable (in THREDDS, ...etc.)",
    (data.DataObject, 'data_status'):
        None,
    (data.DataObject, 'description'):
        None,
    (data.DataObject, 'distribution'):
        None,
    (data.DataObject, 'extent'):
        None,
    (data.DataObject, 'geometry_model'):
        None,
    (data.DataObject, 'hierarchy_level'):
        None,
    (data.DataObject, 'keyword'):
        None,
    (data.DataObject, 'meta'):
        "Injected document metadata.",
    (data.DataObject, 'parent_object'):
        None,
    (data.DataObject, 'properties'):
        None,
    (data.DataObject, 'purpose'):
        None,
    (data.DataObject, 'restriction'):
        None,
    (data.DataObject, 'source_simulation'):
        None,
    (data.DataObject, 'storage'):
        None,
    (data.DataProperty, 'description'):
        None,
    (data.DataRestriction, 'license'):
        "The thing (data or metadata, access or use) that this restriction is applied to.",
    (data.DataRestriction, 'restriction'):
        "The thing (data or metadata, access or use) that this restriction is applied to.",
    (data.DataRestriction, 'scope'):
        "The thing (data or metadata, access or use) that this restriction is applied to.",
    (data.DataStorage, 'format'):
        None,
    (data.DataStorage, 'location'):
        None,
    (data.DataStorage, 'modification_date'):
        None,
    (data.DataStorage, 'size'):
        None,
    (data.DataStorageDb, 'access_string'):
        None,
    (data.DataStorageDb, 'name'):
        None,
    (data.DataStorageDb, 'owner'):
        None,
    (data.DataStorageDb, 'table'):
        None,
    (data.DataStorageFile, 'file_name'):
        None,
    (data.DataStorageFile, 'file_system'):
        None,
    (data.DataStorageFile, 'path'):
        None,
    (data.DataStorageIp, 'file_name'):
        None,
    (data.DataStorageIp, 'host'):
        None,
    (data.DataStorageIp, 'path'):
        None,
    (data.DataStorageIp, 'protocol'):
        None,
    (data.DataTopic, 'description'):
        None,
    (data.DataTopic, 'name'):
        None,
    (data.DataTopic, 'unit'):
        None,
    (grids.CoordinateList, 'has_constant_offset'):
        "Set to true if coordinates in the built array have constant offset.",
    (grids.CoordinateList, 'length'):
        "Specifies the length of the coordinate array. This should always be the final, as-built length of the array if the hasConstantOffset property is set to true and the compact notation (start coordinate plus offset) is used.",
    (grids.CoordinateList, 'uom'):
        "Units of measure used by the coordinates.",
    (grids.GridExtent, 'maximum_latitude'):
        None,
    (grids.GridExtent, 'maximum_longitude'):
        None,
    (grids.GridExtent, 'minimum_latitude'):
        None,
    (grids.GridExtent, 'minimum_longitude'):
        None,
    (grids.GridExtent, 'units'):
        None,
    (grids.GridMosaic, 'citations'):
        "Optional container element for specifying a list of references that describe the grid.",
    (grids.GridMosaic, 'description'):
        "A free-text description of a grid mosaic.",
    (grids.GridMosaic, 'extent'):
        None,
    (grids.GridMosaic, 'has_congruent_tiles'):
        "Indicates whether or not all the tiles contained within a grid mosaic are congruent, that is, of the same size and shape.",
    (grids.GridMosaic, 'id'):
        "Specifies a globally unique identifier for a grid mosaic instance. By globally we mean across all GridSpec instances/records within a given modelling activity (such as CMIP5).",
    (grids.GridMosaic, 'is_leaf'):
        "Indicates whether or not a grid mosaic is a leaf mosaic, that is, it only contains child grid tiles not further mosaics.",
    (grids.GridMosaic, 'long_name'):
        "Specifies the long name associated with a grid mosaic. The long name will typically be a human-readable string, with acronyms expanded, used for labelling purposes.",
    (grids.GridMosaic, 'mnemonic'):
        None,
    (grids.GridMosaic, 'mosaic_count'):
        "Specifies the number of mosaics associated with a non-leaf grid mosaic. Set to zero if the grid mosaic is a leaf mosaic, i.e. it contains child grid tiles not mosaics.",
    (grids.GridMosaic, 'mosaics'):
        None,
    (grids.GridMosaic, 'short_name'):
        "Specifies the short name associated with a grid mosaic. The short name will typically be a convenient abbreviation used to refer to a grid mosaic, e.g. 'UM ATM N96'.",
    (grids.GridMosaic, 'tile_count'):
        "Specifies the number of tiles associated with a leaf grid mosaic. Set to zero if the grid mosaic is not a leaf mosaic, i.e. it contains child grid mosaics rather than tiles. (Added to align with equivalent ESG/Curator property.)",
    (grids.GridMosaic, 'tiles'):
        None,
    (grids.GridMosaic, 'type'):
        "Specifies the type of all the grid tiles contained in a grid mosaic. It is assumed that all of the tiles comprising a given grid mosaic are of the same type. The value domain is as per the specified enumeration list.",
    (grids.GridSpec, 'esm_exchange_grids'):
        None,
    (grids.GridSpec, 'esm_model_grids'):
        None,
    (grids.GridSpec, 'meta'):
        "Injected document metadata.",
    (grids.GridTile, 'area'):
        "gml:MeasureType:Specifies the area of the grid tile in the units defined by the uom attribute that is attached to the GML MeasureType data type.",
    (grids.GridTile, 'cell_array'):
        "GridCellArray:This property may be used to specify an array of grid cell definitions which together define the coordinate geometry of a grid tile. Depending on context, any of the existing sub-types of GridCell may be used. Mixing types is, however, not currently permitted.",
    (grids.GridTile, 'cell_ref_array'):
        "GridCellArray:This property may be used to define the coordinate geometry of a grid tile by specifying an array of references to remotely defined grid cells. Depending on context, any of the existing sub-types of GridCell may be referenced.",
    (grids.GridTile, 'coord_file'):
        "This property may be used to specify the URI of a file containing grid coordinates that define the geometry of a a grid tile. It is envisaged that this will be the preferred mechanism for specifying the geometry of complex grids.",
    (grids.GridTile, 'coordinate_pole'):
        "gml:PointType:The coordinatePole property may be used to specify the lat-long position of any coordinate poles (in the mathematical sense) that form part of the definition of a grid tile. Not to be confused with the gridNorthPole property.  If required, two or more coordinate pole definitions may be distinguished by setting the gml:id attribute to appropriate values, such as spole, npole, etc.",
    (grids.GridTile, 'description'):
        "A free-text description of a grid tile.",
    (grids.GridTile, 'discretization_type'):
        "Indicates the type of discretization applied to the grid tile, e.g. 'logically_rectangular'.",
    (grids.GridTile, 'extent'):
        None,
    (grids.GridTile, 'geometry_type'):
        "Indicates the geometric figure used to approximate the figure of the Earth, e.g. 'sphere'.",
    (grids.GridTile, 'grid_north_pole'):
        "gml:PointType:If required, defines the lat-long position of the north pole used by the grid tile in the case of rotated/displaced pole grids. Not to be confused with the coordinatePole property.",
    (grids.GridTile, 'horizontal_crs'):
        "gml:CRSPropertyType:Specifies the horizontal coordinate reference system used in the definition of the grid tile coordinates. This property should normally be an xlink reference to an external horizontal CRS definition (e.g. in a separate CRS dictionary). If required, however, the property may be defined in situ within a CIM document.",
    (grids.GridTile, 'horizontal_resolution'):
        "Provides an indication of the approximate spatial sampling size of the grid tile, i.e. the size of the underlying grid cells. (Note: the maximum spatial resolution of the grid is twice the sampling size (e.g. 2 km for a 1 km x 1 km grid pitch).",
    (grids.GridTile, 'id'):
        "Specifies an identifer for a grid tile that is unique within its parent grid mosaic. It is not required for this identifier to be unique either across all mosaics in a GridSpec or across all GridSpecs, though if that were the case it would not be detrimental.",
    (grids.GridTile, 'is_conformal'):
        "This property is used to indicate if the grid tile is conformal, i.e. angle-preserving. If so, angles measured on the grid are equal to the equivalent angles on the Earth.",
    (grids.GridTile, 'is_regular'):
        "If true, indicates that the horizontal coordinates of the grid can be defined using 1D arrays (vectors). This means that grid node locations are defined by the cartesian product of the X/Lon and Y/Lat coordinate vectors. It also means that grid cells are logically rectangular (they may also be physically rectangular in the case of projected coordinates).",
    (grids.GridTile, 'is_terrain_following'):
        "Set to true if the vertical coordinate system is terrain-following even if, as is often the case, this only applies to the lower levels of the grid.",
    (grids.GridTile, 'is_uniform'):
        "If true, indicates that horizontal coordinates have fixed offsets in the X and Y directions. If the offset is the same in both directions then the grids are logically square, otherwise they are logically rectangular. The offsets can be specified by two scalar values (or three values in the case of 3D grids).",
    (grids.GridTile, 'long_name'):
        None,
    (grids.GridTile, 'mnemonic'):
        None,
    (grids.GridTile, 'nx'):
        "Specifies the length of the X, or longitude, dimension of the grid tile.",
    (grids.GridTile, 'ny'):
        "Specifies the length of the Y, or latitude, dimension of the grid tile.",
    (grids.GridTile, 'nz'):
        "Specifies the length of the Z, or height/level, dimension of the grid tile. The zcoords coordinate list property, if specified, should have this length.",
    (grids.GridTile, 'refinement_scheme'):
        None,
    (grids.GridTile, 'short_name'):
        None,
    (grids.GridTile, 'simple_grid_geom'):
        "SimpleGridGeometry:This property may be used to define the coordinates of the nodes or cells making up a simple (i.e. uniform or regular) grid tile. More details are provided in the description of the SimpleGridGeometry data type.",
    (grids.GridTile, 'vertical_crs'):
        "gml:CRSPropertyType:Specifies the vertical coordinate reference system used in the definition of the grid tile coordinates. This property should normally be an xlink reference to an external vertical CRS definition (e.g. in a separate CRS dictionary). If required, however, the property may be defined in situ within a CIM document.",
    (grids.GridTile, 'vertical_resolution'):
        "Provides an indication of the approximate resolution of the grid tile in the vertical dimension. (Added to align with corresponding ESG/Curator and DIF property).",
    (grids.GridTile, 'zcoords'):
        "This optional property may be used to specify the vertical coordinates (e.g. heights or model levels) at which a grid tile is utilised or realised. In the case of simple grid tiles the equivalent zcoords property on the SimpleGridGeometry data type would be used instead. The current property is intended to be used when the horizontal grid coordinates are defined by one of the other methods.",
    (grids.GridTileResolutionType, 'description'):
        "A description of the resolution.",
    (grids.GridTileResolutionType, 'properties'):
        None,
    (grids.SimpleGridGeometry, 'dim_order'):
        None,
    (grids.SimpleGridGeometry, 'is_mesh'):
        None,
    (grids.SimpleGridGeometry, 'num_dims'):
        None,
    (grids.SimpleGridGeometry, 'xcoords'):
        "X-Co-ordinates",
    (grids.SimpleGridGeometry, 'ycoords'):
        "Y-Co-ordinates",
    (grids.SimpleGridGeometry, 'zcoords'):
        "Z-Co-ordinates",
    (grids.VerticalCoordinateList, 'form'):
        "Units of measure used by the coordinates.",
    (grids.VerticalCoordinateList, 'properties'):
        None,
    (grids.VerticalCoordinateList, 'type'):
        "Specifies the length of the coordinate array. This should always be the final, as-built length of the array if the hasConstantOffset property is set to true and the compact notation (start coordinate plus offset) is used.",
    (misc.DocumentSet, 'data'):
        "Associated input/output data.",
    (misc.DocumentSet, 'ensembles'):
        "Associated ensemble runs.",
    (misc.DocumentSet, 'experiment'):
        "Associated numerical experiment.",
    (misc.DocumentSet, 'grids'):
        "Associated grid-spec.",
    (misc.DocumentSet, 'meta'):
        "Injected document metadata.",
    (misc.DocumentSet, 'model'):
        "Associated model component.",
    (misc.DocumentSet, 'platform'):
        "Associated simulation execution platform.",
    (misc.DocumentSet, 'simulation'):
        "Associated simulation run.",
    (quality.CimQuality, 'meta'):
        "Injected document metadata.",
    (quality.CimQuality, 'reports'):
        None,
    (quality.Evaluation, 'date'):
        None,
    (quality.Evaluation, 'description'):
        None,
    (quality.Evaluation, 'did_pass'):
        None,
    (quality.Evaluation, 'explanation'):
        None,
    (quality.Evaluation, 'specification'):
        None,
    (quality.Evaluation, 'specification_hyperlink'):
        None,
    (quality.Evaluation, 'title'):
        None,
    (quality.Evaluation, 'type'):
        None,
    (quality.Evaluation, 'type_hyperlink'):
        None,
    (quality.Measure, 'description'):
        None,
    (quality.Measure, 'identification'):
        None,
    (quality.Measure, 'name'):
        None,
    (quality.Report, 'date'):
        None,
    (quality.Report, 'evaluation'):
        None,
    (quality.Report, 'evaluator'):
        None,
    (quality.Report, 'measure'):
        None,
    (shared.Calendar, 'description'):
        "Describes the finer details of the calendar, in case they are not-obvious.  For example, if an experiment has changing conditions within it (ie: 1% CO2 increase until 2100, then hold fixed for the remaining period of the  experment)",
    (shared.Calendar, 'length'):
        None,
    (shared.Calendar, 'range'):
        None,
    (shared.Change, 'author'):
        "The person that made the change.",
    (shared.Change, 'date'):
        "The date the change was implemented.",
    (shared.Change, 'description'):
        None,
    (shared.Change, 'details'):
        None,
    (shared.Change, 'name'):
        "A mnemonic for describing a particular change.",
    (shared.Change, 'type'):
        None,
    (shared.ChangeProperty, 'description'):
        "A text description of the change.  May be used in addition to, or instead of, the more formal description provided by the 'value' attribute.",
    (shared.ChangeProperty, 'id'):
        None,
    (shared.Citation, 'alternative_title'):
        None,
    (shared.Citation, 'collective_title'):
        None,
    (shared.Citation, 'date'):
        None,
    (shared.Citation, 'date_type'):
        None,
    (shared.Citation, 'location'):
        None,
    (shared.Citation, 'organisation'):
        None,
    (shared.Citation, 'role'):
        None,
    (shared.Citation, 'title'):
        None,
    (shared.Citation, 'type'):
        None,
    (shared.ClosedDateRange, 'end'):
        "End date is optional becuase the length of a ClosedDateRange can be calculated from the StartDate plus the Duration element.",
    (shared.ClosedDateRange, 'start'):
        None,
    (shared.Compiler, 'environment_variables'):
        "The set of environment_variables used during compilation (recorded here as a single string rather than separate elements)",
    (shared.Compiler, 'language'):
        None,
    (shared.Compiler, 'name'):
        None,
    (shared.Compiler, 'options'):
        "The set of options used during compilation (recorded here as a single string rather than separate elements)",
    (shared.Compiler, 'type'):
        None,
    (shared.Compiler, 'version'):
        None,
    (shared.DataSource, 'purpose'):
        None,
    (shared.DateRange, 'duration'):
        None,
    (shared.DocMetaInfo, 'author'):
        "Author of the metadata in the parent document.",
    (shared.DocMetaInfo, 'create_date'):
        "Date upon which the instance was created.",
    (shared.DocMetaInfo, 'drs_keys'):
        "DRS related keys to support correlation of documents with datasets.",
    (shared.DocMetaInfo, 'drs_path'):
        "DRS related path to support documents with datasets.",
    (shared.DocMetaInfo, 'external_ids'):
        "Set of identifiers used to reference the document by external parties.",
    (shared.DocMetaInfo, 'id'):
        "Universal document identifier (must be a valid UUID).",
    (shared.DocMetaInfo, 'institute'):
        "Name of institute with which instance is associated.",
    (shared.DocMetaInfo, 'project'):
        "Name of project with which instance is associated.",
    (shared.DocMetaInfo, 'sort_key'):
        "Document sort key.",
    (shared.DocMetaInfo, 'source'):
        "Name of application that created the instance.",
    (shared.DocMetaInfo, 'source_key'):
        "Key of application that created the instance.",
    (shared.DocMetaInfo, 'sub_projects'):
        "Set of sub-projects with which instance is associated.",
    (shared.DocMetaInfo, 'type'):
        "Document ontology type key.",
    (shared.DocMetaInfo, 'type_display_name'):
        "Document type display name.",
    (shared.DocMetaInfo, 'type_sort_key'):
        "Document type sort key.",
    (shared.DocMetaInfo, 'update_date'):
        "Date upon which the instance was last updated.",
    (shared.DocMetaInfo, 'version'):
        "Document version identifier.",
    (shared.DocReference, 'canonical_name'):
        "Canonical name given to document.",
    (shared.DocReference, 'changes'):
        "An optional description of how the item being referenced has been modified.  This is particularly useful for dealing with Ensembles (a set of simulations where something about each simulation has changed) or Conformances.",
    (shared.DocReference, 'constraint_vocabulary'):
        "A constraint vocabulary for the relationship.",
    (shared.DocReference, 'context'):
        "Information about remote record in context of reference.",
    (shared.DocReference, 'description'):
        "Detail of how to access the resource.",
    (shared.DocReference, 'external_id'):
        "External identifier of remote resource, if known.",
    (shared.DocReference, 'id'):
        "Identifier of remote resource, if known.",
    (shared.DocReference, 'institute'):
        "Canonical institute name of referenced document.",
    (shared.DocReference, 'linkage'):
        "A URL.",
    (shared.DocReference, 'name'):
        "A user friendly name given to document.",
    (shared.DocReference, 'protocol'):
        "Protocol to use at the linkage.",
    (shared.DocReference, 'relationship'):
        "Predicate - relationship of the object target as seen from the subject resource.",
    (shared.DocReference, 'type'):
        "The type of remote document.",
    (shared.DocReference, 'url'):
        "The URL of the remote document.",
    (shared.DocReference, 'version'):
        "The version of the remote document.",
    (shared.License, 'contact'):
        "The point of contact for access to this artifact; may be either a person or an institution.",
    (shared.License, 'description'):
        "A textual description of the license; might be the full text of the license, more likely to be a brief summary",
    (shared.License, 'is_unrestricted'):
        "If unrestricted='true' then the artifact can be downloaded with no restrictions (ie: there are no administrative steps for the user to deal with; code or data can be downloaded and used directly).",
    (shared.License, 'name'):
        "The name that the license goes by (ie: 'GPL')",
    (shared.Machine, 'cores_per_processor'):
        None,
    (shared.Machine, 'description'):
        None,
    (shared.Machine, 'interconnect'):
        None,
    (shared.Machine, 'libraries'):
        "The libraries residing on this machine.",
    (shared.Machine, 'location'):
        None,
    (shared.Machine, 'maximum_processors'):
        None,
    (shared.Machine, 'name'):
        None,
    (shared.Machine, 'operating_system'):
        None,
    (shared.Machine, 'processor_type'):
        None,
    (shared.Machine, 'system'):
        None,
    (shared.Machine, 'type'):
        None,
    (shared.Machine, 'vendor'):
        None,
    (shared.MachineCompilerUnit, 'compilers'):
        None,
    (shared.MachineCompilerUnit, 'machine'):
        None,
    (shared.OpenDateRange, 'end'):
        None,
    (shared.OpenDateRange, 'start'):
        None,
    (shared.Platform, 'contacts'):
        None,
    (shared.Platform, 'description'):
        None,
    (shared.Platform, 'long_name'):
        None,
    (shared.Platform, 'meta'):
        "Injected document metadata.",
    (shared.Platform, 'short_name'):
        None,
    (shared.Platform, 'units'):
        None,
    (shared.Property, 'name'):
        None,
    (shared.Property, 'value'):
        None,
    (shared.Relationship, 'description'):
        None,
    (shared.ResponsibleParty, 'abbreviation'):
        None,
    (shared.ResponsibleParty, 'address'):
        None,
    (shared.ResponsibleParty, 'email'):
        None,
    (shared.ResponsibleParty, 'individual_name'):
        None,
    (shared.ResponsibleParty, 'organisation_name'):
        None,
    (shared.ResponsibleParty, 'role'):
        None,
    (shared.ResponsibleParty, 'url'):
        None,
    (shared.Standard, 'description'):
        "The version of the standard",
    (shared.Standard, 'name'):
        "The name of the standard",
    (shared.Standard, 'version'):
        "The version of the standard",
    (shared.StandardName, 'is_open'):
        None,
    (shared.StandardName, 'standards'):
        "Details of the standard being used.",
    (shared.StandardName, 'value'):
        None,
    (software.Component, 'citations'):
        None,
    (software.Component, 'code_access'):
        "Instructions on how to access the source code for this component.",
    (software.Component, 'composition'):
        None,
    (software.Component, 'coupling_framework'):
        "The coupling framework that this entire component conforms to.",
    (software.Component, 'dependencies'):
        None,
    (software.Component, 'deployments'):
        None,
    (software.Component, 'description'):
        "A free-text description of the component.",
    (software.Component, 'funding_sources'):
        "The entities that funded this software component.",
    (software.Component, 'grid'):
        "A reference to the grid that is used by this component.",
    (software.Component, 'is_embedded'):
        "An embedded component cannot exist on its own as an atomic piece of software; instead it is embedded within another (parent) component. When embedded equals 'true', the SoftwareComponent has a corresponding piece of software (otherwise it is acting as a 'virtual' component which may be inexorably nested within a piece of software along with several other virtual components).",
    (software.Component, 'language'):
        None,
    (software.Component, 'license'):
        "The license held by this piece of software.",
    (software.Component, 'long_name'):
        "The name of the model (that is recognized externally).",
    (software.Component, 'online_resource'):
        "Provides a URL location for this model.",
    (software.Component, 'parent'):
        None,
    (software.Component, 'previous_version'):
        None,
    (software.Component, 'properties'):
        "The properties that this model simulates and/or couples.",
    (software.Component, 'release_date'):
        "The date of publication of the software component code (as opposed to the date of publication of the metadata document, or the date of deployment of the model)",
    (software.Component, 'responsible_parties'):
        None,
    (software.Component, 'short_name'):
        "The name of the model (that is used internally).",
    (software.Component, 'sub_components'):
        None,
    (software.Component, 'version'):
        "A free text description of the component version #.",
    (software.ComponentLanguage, 'name'):
        "The name of the language.",
    (software.ComponentLanguage, 'properties'):
        None,
    (software.ComponentProperty, 'citations'):
        None,
    (software.ComponentProperty, 'description'):
        None,
    (software.ComponentProperty, 'grid'):
        "A reference to the grid that is used by this component.",
    (software.ComponentProperty, 'intent'):
        "The direction that this property is intended to be coupled: in, out, or inout.",
    (software.ComponentProperty, 'is_represented'):
        "When set to false, means that this property is not used by the component. Covers the case when, for instance, a modeler chooses not to represent some property in their model. (But still allows meaningful comparisons between components which _do_ model this property.)",
    (software.ComponentProperty, 'long_name'):
        None,
    (software.ComponentProperty, 'short_name'):
        None,
    (software.ComponentProperty, 'standard_names'):
        None,
    (software.ComponentProperty, 'sub_properties'):
        None,
    (software.ComponentProperty, 'units'):
        "The standard name that this property is known as (for example, its CF name).",
    (software.ComponentProperty, 'values'):
        "The value of the property (not applicable to fields).",
    (software.Composition, 'couplings'):
        None,
    (software.Composition, 'description'):
        None,
    (software.Connection, 'description'):
        None,
    (software.Connection, 'priming'):
        "A priming source is one that is active on the first available timestep only (before 'proper' coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created.",
    (software.Connection, 'properties'):
        None,
    (software.Connection, 'sources'):
        "The source property being connected.  (note that there can be multiple sources)  This is optional; the file/component source may have already been specified by the couplingSource.",
    (software.Connection, 'spatial_regridding'):
        "Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid)",
    (software.Connection, 'target'):
        "The target property being connected.  This is optional to support the way that input is handled in the CMIP5 questionnaire.",
    (software.Connection, 'time_lag'):
        "The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time.",
    (software.Connection, 'time_profile'):
        "All information having to do with the rate of this connection; the times that it is active.  This overrides any rate of a Coupling.",
    (software.Connection, 'time_transformation'):
        "Temporal transformation performed on the coupling field before or after regridding onto the target grid.",
    (software.Connection, 'transformers'):
        "An 'in-line' transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here.",
    (software.Connection, 'type'):
        "The type of Connection",
    (software.ConnectionEndpoint, 'data_source'):
        None,
    (software.ConnectionEndpoint, 'instance_id'):
        "If the same datasource is used more than once in a coupled model then a method for identifying which particular instance is being referenced is needed (for BFG).",
    (software.ConnectionEndpoint, 'properties'):
        "The place to describe features specific to the source/target of a connection.",
    (software.Coupling, 'connections'):
        None,
    (software.Coupling, 'description'):
        "A free-text description of the coupling.",
    (software.Coupling, 'is_fully_specified'):
        "If true then the coupling is fully-specified.  If false then not every Connection has been described within the coupling.",
    (software.Coupling, 'priming'):
        "A priming source is one that is active on the first available timestep only (before 'proper' coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created.",
    (software.Coupling, 'properties'):
        None,
    (software.Coupling, 'purpose'):
        None,
    (software.Coupling, 'sources'):
        "The source component of the coupling. (note that there can be multiple sources).",
    (software.Coupling, 'spatial_regriddings'):
        "Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).",
    (software.Coupling, 'target'):
        "The target component of the coupling.",
    (software.Coupling, 'time_lag'):
        "The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time.",
    (software.Coupling, 'time_profile'):
        "Describes how often the coupling takes place.",
    (software.Coupling, 'time_transformation'):
        "Temporal transformation performed on the coupling field before or after regridding onto the target grid.",
    (software.Coupling, 'transformers'):
        "An 'in-line' transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here.",
    (software.Coupling, 'type'):
        "Describes the method of coupling.",
    (software.CouplingEndpoint, 'data_source'):
        None,
    (software.CouplingEndpoint, 'instance_id'):
        "If the same datasource is used more than once in a coupled model then a method for identifying which particular instance is being referenced is needed (for BFG).",
    (software.CouplingEndpoint, 'properties'):
        "A place to describe features specific to the source/target of a coupling",
    (software.Deployment, 'deployment_date'):
        None,
    (software.Deployment, 'description'):
        None,
    (software.Deployment, 'executable_arguments'):
        None,
    (software.Deployment, 'executable_name'):
        None,
    (software.Deployment, 'parallelisation'):
        None,
    (software.Deployment, 'platform'):
        "The platform that this deployment has been run on. It is optional to allow for 'unconfigured' models, that nonetheless specify their parallelisation constraints (a feature needed by OASIS).",
    (software.EntryPoint, 'name'):
        None,
    (software.ModelComponent, 'activity'):
        None,
    (software.ModelComponent, 'meta'):
        "Injected document metadata.",
    (software.ModelComponent, 'timing'):
        "Describes information about how this component simulates time.",
    (software.ModelComponent, 'type'):
        "Describes the type of component. There can be multiple types.",
    (software.ModelComponent, 'types'):
        "Describes the type of component. There can be multiple types.",
    (software.Parallelisation, 'processes'):
        None,
    (software.Parallelisation, 'ranks'):
        None,
    (software.ProcessorComponent, 'meta'):
        "Injected document metadata.",
    (software.Rank, 'increment'):
        None,
    (software.Rank, 'max'):
        None,
    (software.Rank, 'min'):
        None,
    (software.Rank, 'value'):
        None,
    (software.SpatialRegridding, 'dimension'):
        None,
    (software.SpatialRegridding, 'properties'):
        None,
    (software.SpatialRegridding, 'standard_method'):
        None,
    (software.SpatialRegridding, 'user_method'):
        None,
    (software.SpatialRegriddingUserMethod, 'file'):
        None,
    (software.SpatialRegriddingUserMethod, 'name'):
        None,
    (software.StatisticalModelComponent, 'meta'):
        "Injected document metadata.",
    (software.StatisticalModelComponent, 'timing'):
        "Describes information about how this component simulates time.",
    (software.StatisticalModelComponent, 'type'):
        "Describes the type of component. There can be multiple types.",
    (software.StatisticalModelComponent, 'types'):
        "Describes the type of component. There can be multiple types.",
    (software.TimeLag, 'units'):
        None,
    (software.TimeLag, 'value'):
        None,
    (software.TimeTransformation, 'description'):
        None,
    (software.TimeTransformation, 'mapping_type'):
        None,
    (software.Timing, 'end'):
        None,
    (software.Timing, 'is_variable_rate'):
        "Describes whether or not the model supports a variable timestep. If set to true, then rate should not be specified.",
    (software.Timing, 'rate'):
        None,
    (software.Timing, 'start'):
        None,
    (software.Timing, 'units'):
        None,

    # ------------------------------------------------
    # Enums.
    # ------------------------------------------------

    activity.ConformanceType: """
        Creates and returns instance of conformance_type enum.

    """,
    activity.DownscalingType: """
        Creates and returns instance of downscaling_type enum.

    """,
    activity.EnsembleType: """
        Creates and returns instance of ensemble_type enum.

    """,
    activity.ExperimentRelationshipType: """
        Creates and returns instance of experiment_relationship_type enum.

    """,
    activity.FrequencyType: """
        Creates and returns instance of frequency_type enum.

    """,
    activity.ProjectType: """
        Creates and returns instance of project_type enum.

    """,
    activity.ResolutionType: """
        Creates and returns instance of resolution_type enum.

    """,
    activity.SimulationRelationshipType: """
        Creates and returns instance of simulation_relationship_type enum.

    """,
    activity.SimulationType: """
        Creates and returns instance of simulation_type enum.

    """,
    data.DataHierarchyType: """
        Enumerates the level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.

    """,
    data.DataStatusType: """
        Enumerates status of a data object.

    """,
    grids.ArcTypeEnum: """
        Creates and returns instance of arc_type_enum enum.

    """,
    grids.DiscretizationEnum: """
        Creates and returns instance of discretization_enum enum.

    """,
    grids.FeatureTypeEnum: """
        Creates and returns instance of feature_type_enum enum.

    """,
    grids.GeometryTypeEnum: """
        Creates and returns instance of geometry_type_enum enum.

    """,
    grids.GridNodePositionEnum: """
        Creates and returns instance of grid_node_position_enum enum.

    """,
    grids.GridTypeEnum: """
        Creates and returns instance of grid_type_enum enum.

    """,
    grids.HorizontalCsEnum: """
        Creates and returns instance of horizontal_cs_enum enum.

    """,
    grids.RefinementTypeEnum: """
        Creates and returns instance of refinement_type_enum enum.

    """,
    grids.VerticalCsEnum: """
        Creates and returns instance of vertical_cs_enum enum.

    """,
    quality.CimFeatureType: """
        Creates and returns instance of cim_feature_type enum.

    """,
    quality.CimResultType: """
        Creates and returns instance of cim_result_type enum.

    """,
    quality.CimScopeCodeType: """
        This would cover quality issues with the CIM itself.

    """,
    quality.QualityIssueType: """
        Creates and returns instance of quality_issue_type enum.

    """,
    quality.QualitySeverityType: """
        Creates and returns instance of quality_severity_type enum.

    """,
    quality.QualityStatusType: """
        Creates and returns instance of quality_status_type enum.

    """,
    shared.ChangePropertyType: """
        Creates and returns instance of change_property_type enum.

    """,
    shared.CompilerType: """
        Creates and returns instance of compiler_type enum.

    """,
    shared.DataPurpose: """
        Purpose of the data - i.e. ancillaryFile, boundaryCondition or initialCondition.

    """,
    shared.InterconnectType: """
        A list of connectors between machines.

    """,
    shared.MachineType: """
        A list of known machines.

    """,
    shared.MachineVendorType: """
        A list of organisations that create machines.

    """,
    shared.OperatingSystemType: """
        A list of common operating systems.

    """,
    shared.ProcessorType: """
        A list of known cpu's.

    """,
    shared.UnitType: """
        A list of scientific units.

    """,
    software.ComponentPropertyIntentType: """
        The direction that the associated component property is intended to be coupled: in, out, or inout.

    """,
    software.ConnectionType: """
        The ConnectionType enumeration describes the mechanism of transport for a connection.

    """,
    software.CouplingFrameworkType: """
        Creates and returns instance of coupling_framework_type enum.

    """,
    software.ModelComponentType: """
        An enumeration of types of ModelComponent. This includes things like atmosphere & ocean models, radiation schemes, etc. CIM best-practice is to describe every component for which there is a named ComponentType as a separate component, even if it is not a separate unit of software (ie: even if it is embedded), instead of as a (set of) ModelParameters. This codelist is synonomous with 'realm' for the purposes of CMIP5.

    """,
    software.SpatialRegriddingDimensionType: """
        Creates and returns instance of spatial_regridding_dimension_type enum.

    """,
    software.SpatialRegriddingStandardMethodType: """
        Creates and returns instance of spatial_regridding_standard_method_type enum.

    """,
    software.StatisticalModelComponentType: """
        An enumeration of types of ProcessorComponent.  This includes things like transformers and post-processors.

    """,
    software.TimeMappingType: """
        Enumerates the different ways that time can be mapped when transforming from one field to another.

    """,
    software.TimingUnits: """
        Creates and returns instance of timing_units enum.

    """,

    # ------------------------------------------------
    # Enum members.
    # ------------------------------------------------

    (activity.ConformanceType, 'not-xxx'):
        None,
    (activity.ConformanceType, 'not conformant'):
        "Describes a simulation that is purpefully non-conformant to an experimental requirement.",
    (activity.ConformanceType, 'standard config'):
        "Describes a simulation that is naturally conformant to an experimental requirement.",
    (activity.ConformanceType, 'via inputs'):
        "Describes a simulation that conforms to an experimental requirement by using particular inputs.",
    (activity.ConformanceType, 'via model mods'):
        "Describes a simulation that conforms to an experimental requirement by changing the configuration of the software model implementing that simulation.",
    (activity.ConformanceType, 'combination'):
        "Describes a simulation that conforms to an experimental requirement by using more than one method.",
    (activity.DownscalingType, 'statistical'):
        None,
    (activity.DownscalingType, 'dynamic'):
        None,
    (activity.ExperimentRelationshipType, 'previousRealisation'):
        None,
    (activity.ExperimentRelationshipType, 'continuationOf'):
        None,
    (activity.ExperimentRelationshipType, 'controlExperiment'):
        None,
    (activity.ExperimentRelationshipType, 'higherResolutionVersionOf'):
        None,
    (activity.ExperimentRelationshipType, 'lowerResolutionVersionOf'):
        None,
    (activity.ExperimentRelationshipType, 'increaseEnsembleOf'):
        None,
    (activity.ExperimentRelationshipType, 'modifiedInputMethodOf'):
        None,
    (activity.ExperimentRelationshipType, 'shorterVersionOf'):
        None,
    (activity.ExperimentRelationshipType, 'extensionOf'):
        None,
    (activity.SimulationRelationshipType, 'extensionOf'):
        None,
    (activity.SimulationRelationshipType, 'responseTo'):
        None,
    (activity.SimulationRelationshipType, 'continuationOf'):
        None,
    (activity.SimulationRelationshipType, 'previousSimulation'):
        None,
    (activity.SimulationRelationshipType, 'higherResolutionVersionOf'):
        None,
    (activity.SimulationRelationshipType, 'lowerResolutionVersionOf'):
        None,
    (activity.SimulationRelationshipType, 'fixedVersionOf'):
        None,
    (activity.SimulationRelationshipType, 'followingSimulation'):
        None,
    (activity.SimulationType, 'simulationRun'):
        None,
    (activity.SimulationType, 'assimilation'):
        None,
    (activity.SimulationType, 'simulationComposite'):
        None,
    (data.DataStatusType, 'complete'):
        "This DataObject is complete.",
    (data.DataStatusType, 'metadataOnly'):
        "This DataObject is incomplete - it is described in metadata but the actual data has not yet been linked to it.",
    (data.DataStatusType, 'continuouslySupplemented'):
        "This DataObject's actual data is continuously updated.",
    (grids.ArcTypeEnum, 'geodesic'):
        None,
    (grids.ArcTypeEnum, 'great_circle'):
        None,
    (grids.ArcTypeEnum, 'small_circle'):
        None,
    (grids.ArcTypeEnum, 'complex'):
        None,
    (grids.DiscretizationEnum, 'logically_rectangular'):
        None,
    (grids.DiscretizationEnum, 'structured_triangular'):
        None,
    (grids.DiscretizationEnum, 'unstructured_triangular'):
        None,
    (grids.DiscretizationEnum, 'pixel-based_catchment'):
        None,
    (grids.DiscretizationEnum, 'unstructured_polygonal'):
        None,
    (grids.DiscretizationEnum, 'spherical_harmonics'):
        None,
    (grids.DiscretizationEnum, 'other'):
        None,
    (grids.FeatureTypeEnum, 'point'):
        None,
    (grids.FeatureTypeEnum, 'edge'):
        None,
    (grids.GeometryTypeEnum, 'ellipsoid'):
        None,
    (grids.GeometryTypeEnum, 'plane'):
        None,
    (grids.GeometryTypeEnum, 'sphere'):
        None,
    (grids.GridNodePositionEnum, 'centre'):
        None,
    (grids.GridNodePositionEnum, 'plane'):
        None,
    (grids.GridNodePositionEnum, 'sphere'):
        None,
    (grids.GridTypeEnum, 'cubed_sphere'):
        None,
    (grids.GridTypeEnum, 'displaced_pole'):
        None,
    (grids.GridTypeEnum, 'icosahedral_geodesic'):
        None,
    (grids.GridTypeEnum, 'reduced_gaussian'):
        None,
    (grids.GridTypeEnum, 'regular_lat_lon'):
        None,
    (grids.GridTypeEnum, 'spectral_gaussian'):
        None,
    (grids.GridTypeEnum, 'tripolar'):
        None,
    (grids.GridTypeEnum, 'yin_yang'):
        None,
    (grids.GridTypeEnum, 'composite'):
        None,
    (grids.GridTypeEnum, 'other'):
        None,
    (grids.HorizontalCsEnum, 'cartesian'):
        None,
    (grids.HorizontalCsEnum, 'ellipsoidal'):
        None,
    (grids.HorizontalCsEnum, 'polar'):
        None,
    (grids.HorizontalCsEnum, 'spherical'):
        None,
    (grids.RefinementTypeEnum, 'none'):
        "Tile boundaries have no refinement when the grid lines meeting at the tile boundary are continuous.",
    (grids.RefinementTypeEnum, 'integer'):
        "The refinement is integer when grid lines from the coarser grid are continuous on the finer grid, but not vice versa.",
    (grids.RefinementTypeEnum, 'rational'):
        "The refinement is rational when the adjacent or overlapping grid tiles have grid line counts that are coprime (i.e. no common factor other than 1).",
    (grids.VerticalCsEnum, 'mass-based'):
        None,
    (grids.VerticalCsEnum, 'space-based'):
        None,
    (quality.CimFeatureType, 'file'):
        None,
    (quality.CimFeatureType, 'diagnostic'):
        None,
    (quality.CimResultType, 'plot'):
        None,
    (quality.CimResultType, 'document'):
        None,
    (quality.CimResultType, 'logfile'):
        None,
    (quality.CimScopeCodeType, 'dataset'):
        None,
    (quality.CimScopeCodeType, 'software'):
        None,
    (quality.CimScopeCodeType, 'service'):
        None,
    (quality.CimScopeCodeType, 'model'):
        None,
    (quality.CimScopeCodeType, 'modelComponent'):
        None,
    (quality.CimScopeCodeType, 'simulation'):
        None,
    (quality.CimScopeCodeType, 'experiment'):
        None,
    (quality.CimScopeCodeType, 'numericalRequirement'):
        None,
    (quality.CimScopeCodeType, 'ensemble'):
        None,
    (quality.CimScopeCodeType, 'file'):
        None,
    (quality.QualityIssueType, 'metadata'):
        None,
    (quality.QualityIssueType, 'data_format'):
        None,
    (quality.QualityIssueType, 'data_content'):
        None,
    (quality.QualityIssueType, 'data_indexing'):
        None,
    (quality.QualityIssueType, 'science'):
        None,
    (quality.QualitySeverityType, 'cosmetic'):
        None,
    (quality.QualitySeverityType, 'minor'):
        None,
    (quality.QualitySeverityType, 'major'):
        None,
    (quality.QualityStatusType, 'reported'):
        None,
    (quality.QualityStatusType, 'confirmed'):
        None,
    (quality.QualityStatusType, 'partially_resolved'):
        None,
    (quality.QualityStatusType, 'resolved'):
        None,
    (shared.ChangePropertyType, 'InputMod'):
        None,
    (shared.ChangePropertyType, 'ModelMod'):
        None,
    (shared.ChangePropertyType, 'Decrement'):
        None,
    (shared.ChangePropertyType, 'Increment'):
        None,
    (shared.ChangePropertyType, 'Redistribution'):
        None,
    (shared.ChangePropertyType, 'Replacement'):
        None,
    (shared.ChangePropertyType, 'ParameterChange'):
        "A specific type of ModelMod",
    (shared.ChangePropertyType, 'CodeChange'):
        "A specific type of ModelMod",
    (shared.ChangePropertyType, 'AncillaryFile'):
        "A specific type of ModelMod",
    (shared.ChangePropertyType, 'BoundaryCondition'):
        "A specific type of ModelMod",
    (shared.ChangePropertyType, 'InitialCondition'):
        "A specific type of ModelMod",
    (shared.ChangePropertyType, 'Unused'):
        None,
    (shared.DataPurpose, 'ancillaryFile'):
        None,
    (shared.DataPurpose, 'boundaryCondition'):
        None,
    (shared.DataPurpose, 'initialCondition'):
        None,
    (shared.MachineType, 'Parallel'):
        None,
    (shared.MachineType, 'Vector'):
        None,
    (shared.MachineType, 'Beowulf'):
        None,
    (software.ComponentPropertyIntentType, 'in'):
        None,
    (software.ComponentPropertyIntentType, 'out'):
        None,
    (software.ComponentPropertyIntentType, 'inout'):
        None,
    (software.CouplingFrameworkType, 'BFG'):
        None,
    (software.CouplingFrameworkType, 'ESMF'):
        None,
    (software.CouplingFrameworkType, 'OASIS'):
        None,
    (software.SpatialRegriddingDimensionType, '1D'):
        None,
    (software.SpatialRegriddingDimensionType, '2D'):
        None,
    (software.SpatialRegriddingDimensionType, '3D'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'linear'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'near-neighbour'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'cubic'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'conservative-first-order'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'conservative-second-order'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'conservative'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'non-conservative'):
        None,
    (software.TimingUnits, 'seconds'):
        None,
    (software.TimingUnits, 'minutes'):
        None,
    (software.TimingUnits, 'hours'):
        None,
    (software.TimingUnits, 'days'):
        None,
    (software.TimingUnits, 'months'):
        None,
    (software.TimingUnits, 'years'):
        None,
    (software.TimingUnits, 'decades'):
        None,
    (software.TimingUnits, 'centuries'):
        None,
}

# ------------------------------------------------
# Type keys.
# ------------------------------------------------

# Map of ontology types to type keys.
KEYS = {
    # ------------------------------------------------
    # Packages.
    # ------------------------------------------------

    activity: "cim.1.activity",
    data: "cim.1.data",
    grids: "cim.1.grids",
    misc: "cim.1.misc",
    quality: "cim.1.quality",
    shared: "cim.1.shared",
    software: "cim.1.software",

    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    activity.Activity: "cim.1.activity.Activity",
    activity.BoundaryCondition: "cim.1.activity.BoundaryCondition",
    activity.Conformance: "cim.1.activity.Conformance",
    activity.DownscalingSimulation: "cim.1.activity.DownscalingSimulation",
    activity.Ensemble: "cim.1.activity.Ensemble",
    activity.EnsembleMember: "cim.1.activity.EnsembleMember",
    activity.Experiment: "cim.1.activity.Experiment",
    activity.ExperimentRelationship: "cim.1.activity.ExperimentRelationship",
    activity.ExperimentRelationshipTarget: "cim.1.activity.ExperimentRelationshipTarget",
    activity.InitialCondition: "cim.1.activity.InitialCondition",
    activity.LateralBoundaryCondition: "cim.1.activity.LateralBoundaryCondition",
    activity.MeasurementCampaign: "cim.1.activity.MeasurementCampaign",
    activity.NumericalActivity: "cim.1.activity.NumericalActivity",
    activity.NumericalExperiment: "cim.1.activity.NumericalExperiment",
    activity.NumericalRequirement: "cim.1.activity.NumericalRequirement",
    activity.NumericalRequirementOption: "cim.1.activity.NumericalRequirementOption",
    activity.OutputRequirement: "cim.1.activity.OutputRequirement",
    activity.PhysicalModification: "cim.1.activity.PhysicalModification",
    activity.Simulation: "cim.1.activity.Simulation",
    activity.SimulationComposite: "cim.1.activity.SimulationComposite",
    activity.SimulationRelationship: "cim.1.activity.SimulationRelationship",
    activity.SimulationRelationshipTarget: "cim.1.activity.SimulationRelationshipTarget",
    activity.SimulationRun: "cim.1.activity.SimulationRun",
    activity.SpatioTemporalConstraint: "cim.1.activity.SpatioTemporalConstraint",
    data.DataContent: "cim.1.data.DataContent",
    data.DataDistribution: "cim.1.data.DataDistribution",
    data.DataExtent: "cim.1.data.DataExtent",
    data.DataExtentGeographical: "cim.1.data.DataExtentGeographical",
    data.DataExtentTemporal: "cim.1.data.DataExtentTemporal",
    data.DataExtentTimeInterval: "cim.1.data.DataExtentTimeInterval",
    data.DataHierarchyLevel: "cim.1.data.DataHierarchyLevel",
    data.DataObject: "cim.1.data.DataObject",
    data.DataProperty: "cim.1.data.DataProperty",
    data.DataRestriction: "cim.1.data.DataRestriction",
    data.DataStorage: "cim.1.data.DataStorage",
    data.DataStorageDb: "cim.1.data.DataStorageDb",
    data.DataStorageFile: "cim.1.data.DataStorageFile",
    data.DataStorageIp: "cim.1.data.DataStorageIp",
    data.DataTopic: "cim.1.data.DataTopic",
    grids.CoordinateList: "cim.1.grids.CoordinateList",
    grids.GridExtent: "cim.1.grids.GridExtent",
    grids.GridMosaic: "cim.1.grids.GridMosaic",
    grids.GridProperty: "cim.1.grids.GridProperty",
    grids.GridSpec: "cim.1.grids.GridSpec",
    grids.GridTile: "cim.1.grids.GridTile",
    grids.GridTileResolutionType: "cim.1.grids.GridTileResolutionType",
    grids.SimpleGridGeometry: "cim.1.grids.SimpleGridGeometry",
    grids.VerticalCoordinateList: "cim.1.grids.VerticalCoordinateList",
    misc.DocumentSet: "cim.1.misc.DocumentSet",
    quality.CimQuality: "cim.1.quality.CimQuality",
    quality.Evaluation: "cim.1.quality.Evaluation",
    quality.Measure: "cim.1.quality.Measure",
    quality.Report: "cim.1.quality.Report",
    shared.Calendar: "cim.1.shared.Calendar",
    shared.Change: "cim.1.shared.Change",
    shared.ChangeProperty: "cim.1.shared.ChangeProperty",
    shared.Citation: "cim.1.shared.Citation",
    shared.ClosedDateRange: "cim.1.shared.ClosedDateRange",
    shared.Compiler: "cim.1.shared.Compiler",
    shared.Daily360: "cim.1.shared.Daily360",
    shared.DataSource: "cim.1.shared.DataSource",
    shared.DateRange: "cim.1.shared.DateRange",
    shared.DocMetaInfo: "cim.1.shared.DocMetaInfo",
    shared.DocReference: "cim.1.shared.DocReference",
    shared.License: "cim.1.shared.License",
    shared.Machine: "cim.1.shared.Machine",
    shared.MachineCompilerUnit: "cim.1.shared.MachineCompilerUnit",
    shared.OpenDateRange: "cim.1.shared.OpenDateRange",
    shared.PerpetualPeriod: "cim.1.shared.PerpetualPeriod",
    shared.Platform: "cim.1.shared.Platform",
    shared.Property: "cim.1.shared.Property",
    shared.RealCalendar: "cim.1.shared.RealCalendar",
    shared.Relationship: "cim.1.shared.Relationship",
    shared.ResponsibleParty: "cim.1.shared.ResponsibleParty",
    shared.Standard: "cim.1.shared.Standard",
    shared.StandardName: "cim.1.shared.StandardName",
    software.Component: "cim.1.software.Component",
    software.ComponentLanguage: "cim.1.software.ComponentLanguage",
    software.ComponentLanguageProperty: "cim.1.software.ComponentLanguageProperty",
    software.ComponentProperty: "cim.1.software.ComponentProperty",
    software.Composition: "cim.1.software.Composition",
    software.Connection: "cim.1.software.Connection",
    software.ConnectionEndpoint: "cim.1.software.ConnectionEndpoint",
    software.ConnectionProperty: "cim.1.software.ConnectionProperty",
    software.Coupling: "cim.1.software.Coupling",
    software.CouplingEndpoint: "cim.1.software.CouplingEndpoint",
    software.CouplingProperty: "cim.1.software.CouplingProperty",
    software.Deployment: "cim.1.software.Deployment",
    software.EntryPoint: "cim.1.software.EntryPoint",
    software.ModelComponent: "cim.1.software.ModelComponent",
    software.Parallelisation: "cim.1.software.Parallelisation",
    software.ProcessorComponent: "cim.1.software.ProcessorComponent",
    software.Rank: "cim.1.software.Rank",
    software.SpatialRegridding: "cim.1.software.SpatialRegridding",
    software.SpatialRegriddingProperty: "cim.1.software.SpatialRegriddingProperty",
    software.SpatialRegriddingUserMethod: "cim.1.software.SpatialRegriddingUserMethod",
    software.StatisticalModelComponent: "cim.1.software.StatisticalModelComponent",
    software.TimeLag: "cim.1.software.TimeLag",
    software.TimeTransformation: "cim.1.software.TimeTransformation",
    software.Timing: "cim.1.software.Timing",

    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------

    (activity.Activity, 'funding_sources'): "cim.1.activity.Activity.funding_sources",
    (activity.Activity, 'projects'): "cim.1.activity.Activity.projects",
    (activity.Activity, 'rationales'): "cim.1.activity.Activity.rationales",
    (activity.Activity, 'responsible_parties'): "cim.1.activity.Activity.responsible_parties",
    (activity.Conformance, 'description'): "cim.1.activity.Conformance.description",
    (activity.Conformance, 'frequency'): "cim.1.activity.Conformance.frequency",
    (activity.Conformance, 'is_conformant'): "cim.1.activity.Conformance.is_conformant",
    (activity.Conformance, 'requirements'): "cim.1.activity.Conformance.requirements",
    (activity.Conformance, 'sources'): "cim.1.activity.Conformance.sources",
    (activity.Conformance, 'type'): "cim.1.activity.Conformance.type",
    (activity.DownscalingSimulation, 'calendar'): "cim.1.activity.DownscalingSimulation.calendar",
    (activity.DownscalingSimulation, 'downscaled_from'): "cim.1.activity.DownscalingSimulation.downscaled_from",
    (activity.DownscalingSimulation, 'downscaling_id'): "cim.1.activity.DownscalingSimulation.downscaling_id",
    (activity.DownscalingSimulation, 'downscaling_type'): "cim.1.activity.DownscalingSimulation.downscaling_type",
    (activity.DownscalingSimulation, 'inputs'): "cim.1.activity.DownscalingSimulation.inputs",
    (activity.DownscalingSimulation, 'meta'): "cim.1.activity.DownscalingSimulation.meta",
    (activity.DownscalingSimulation, 'outputs'): "cim.1.activity.DownscalingSimulation.outputs",
    (activity.Ensemble, 'members'): "cim.1.activity.Ensemble.members",
    (activity.Ensemble, 'meta'): "cim.1.activity.Ensemble.meta",
    (activity.Ensemble, 'outputs'): "cim.1.activity.Ensemble.outputs",
    (activity.Ensemble, 'types'): "cim.1.activity.Ensemble.types",
    (activity.EnsembleMember, 'ensemble'): "cim.1.activity.EnsembleMember.ensemble",
    (activity.EnsembleMember, 'ensemble_ids'): "cim.1.activity.EnsembleMember.ensemble_ids",
    (activity.EnsembleMember, 'simulation'): "cim.1.activity.EnsembleMember.simulation",
    (activity.Experiment, 'generates'): "cim.1.activity.Experiment.generates",
    (activity.Experiment, 'measurement_campaigns'): "cim.1.activity.Experiment.measurement_campaigns",
    (activity.Experiment, 'requires'): "cim.1.activity.Experiment.requires",
    (activity.Experiment, 'supports'): "cim.1.activity.Experiment.supports",
    (activity.ExperimentRelationship, 'target'): "cim.1.activity.ExperimentRelationship.target",
    (activity.ExperimentRelationship, 'type'): "cim.1.activity.ExperimentRelationship.type",
    (activity.ExperimentRelationshipTarget, 'numerical_experiment'): "cim.1.activity.ExperimentRelationshipTarget.numerical_experiment",
    (activity.MeasurementCampaign, 'duration'): "cim.1.activity.MeasurementCampaign.duration",
    (activity.NumericalActivity, 'description'): "cim.1.activity.NumericalActivity.description",
    (activity.NumericalActivity, 'long_name'): "cim.1.activity.NumericalActivity.long_name",
    (activity.NumericalActivity, 'short_name'): "cim.1.activity.NumericalActivity.short_name",
    (activity.NumericalActivity, 'supports'): "cim.1.activity.NumericalActivity.supports",
    (activity.NumericalExperiment, 'description'): "cim.1.activity.NumericalExperiment.description",
    (activity.NumericalExperiment, 'experiment_id'): "cim.1.activity.NumericalExperiment.experiment_id",
    (activity.NumericalExperiment, 'long_name'): "cim.1.activity.NumericalExperiment.long_name",
    (activity.NumericalExperiment, 'meta'): "cim.1.activity.NumericalExperiment.meta",
    (activity.NumericalExperiment, 'requirements'): "cim.1.activity.NumericalExperiment.requirements",
    (activity.NumericalExperiment, 'short_name'): "cim.1.activity.NumericalExperiment.short_name",
    (activity.NumericalRequirement, 'description'): "cim.1.activity.NumericalRequirement.description",
    (activity.NumericalRequirement, 'id'): "cim.1.activity.NumericalRequirement.id",
    (activity.NumericalRequirement, 'name'): "cim.1.activity.NumericalRequirement.name",
    (activity.NumericalRequirement, 'options'): "cim.1.activity.NumericalRequirement.options",
    (activity.NumericalRequirement, 'requirement_type'): "cim.1.activity.NumericalRequirement.requirement_type",
    (activity.NumericalRequirement, 'source'): "cim.1.activity.NumericalRequirement.source",
    (activity.NumericalRequirementOption, 'description'): "cim.1.activity.NumericalRequirementOption.description",
    (activity.NumericalRequirementOption, 'id'): "cim.1.activity.NumericalRequirementOption.id",
    (activity.NumericalRequirementOption, 'name'): "cim.1.activity.NumericalRequirementOption.name",
    (activity.NumericalRequirementOption, 'relationship'): "cim.1.activity.NumericalRequirementOption.relationship",
    (activity.NumericalRequirementOption, 'sub_options'): "cim.1.activity.NumericalRequirementOption.sub_options",
    (activity.Simulation, 'authors'): "cim.1.activity.Simulation.authors",
    (activity.Simulation, 'calendar'): "cim.1.activity.Simulation.calendar",
    (activity.Simulation, 'conformances'): "cim.1.activity.Simulation.conformances",
    (activity.Simulation, 'control_simulation'): "cim.1.activity.Simulation.control_simulation",
    (activity.Simulation, 'deployments'): "cim.1.activity.Simulation.deployments",
    (activity.Simulation, 'inputs'): "cim.1.activity.Simulation.inputs",
    (activity.Simulation, 'outputs'): "cim.1.activity.Simulation.outputs",
    (activity.Simulation, 'restarts'): "cim.1.activity.Simulation.restarts",
    (activity.Simulation, 'simulation_id'): "cim.1.activity.Simulation.simulation_id",
    (activity.Simulation, 'spinup_date_range'): "cim.1.activity.Simulation.spinup_date_range",
    (activity.Simulation, 'spinup_simulation'): "cim.1.activity.Simulation.spinup_simulation",
    (activity.SimulationComposite, 'child'): "cim.1.activity.SimulationComposite.child",
    (activity.SimulationComposite, 'date_range'): "cim.1.activity.SimulationComposite.date_range",
    (activity.SimulationComposite, 'meta'): "cim.1.activity.SimulationComposite.meta",
    (activity.SimulationComposite, 'rank'): "cim.1.activity.SimulationComposite.rank",
    (activity.SimulationRelationship, 'target'): "cim.1.activity.SimulationRelationship.target",
    (activity.SimulationRelationship, 'type'): "cim.1.activity.SimulationRelationship.type",
    (activity.SimulationRelationshipTarget, 'simulation'): "cim.1.activity.SimulationRelationshipTarget.simulation",
    (activity.SimulationRelationshipTarget, 'target'): "cim.1.activity.SimulationRelationshipTarget.target",
    (activity.SimulationRun, 'date_range'): "cim.1.activity.SimulationRun.date_range",
    (activity.SimulationRun, 'meta'): "cim.1.activity.SimulationRun.meta",
    (activity.SimulationRun, 'model'): "cim.1.activity.SimulationRun.model",
    (activity.SpatioTemporalConstraint, 'date_range'): "cim.1.activity.SpatioTemporalConstraint.date_range",
    (activity.SpatioTemporalConstraint, 'spatial_resolution'): "cim.1.activity.SpatioTemporalConstraint.spatial_resolution",
    (data.DataContent, 'aggregation'): "cim.1.data.DataContent.aggregation",
    (data.DataContent, 'frequency'): "cim.1.data.DataContent.frequency",
    (data.DataContent, 'topic'): "cim.1.data.DataContent.topic",
    (data.DataDistribution, 'access'): "cim.1.data.DataDistribution.access",
    (data.DataDistribution, 'fee'): "cim.1.data.DataDistribution.fee",
    (data.DataDistribution, 'format'): "cim.1.data.DataDistribution.format",
    (data.DataDistribution, 'responsible_party'): "cim.1.data.DataDistribution.responsible_party",
    (data.DataExtent, 'geographical'): "cim.1.data.DataExtent.geographical",
    (data.DataExtent, 'temporal'): "cim.1.data.DataExtent.temporal",
    (data.DataExtentGeographical, 'east'): "cim.1.data.DataExtentGeographical.east",
    (data.DataExtentGeographical, 'north'): "cim.1.data.DataExtentGeographical.north",
    (data.DataExtentGeographical, 'south'): "cim.1.data.DataExtentGeographical.south",
    (data.DataExtentGeographical, 'west'): "cim.1.data.DataExtentGeographical.west",
    (data.DataExtentTemporal, 'begin'): "cim.1.data.DataExtentTemporal.begin",
    (data.DataExtentTemporal, 'end'): "cim.1.data.DataExtentTemporal.end",
    (data.DataExtentTemporal, 'time_interval'): "cim.1.data.DataExtentTemporal.time_interval",
    (data.DataExtentTimeInterval, 'factor'): "cim.1.data.DataExtentTimeInterval.factor",
    (data.DataExtentTimeInterval, 'radix'): "cim.1.data.DataExtentTimeInterval.radix",
    (data.DataExtentTimeInterval, 'unit'): "cim.1.data.DataExtentTimeInterval.unit",
    (data.DataHierarchyLevel, 'is_open'): "cim.1.data.DataHierarchyLevel.is_open",
    (data.DataHierarchyLevel, 'name'): "cim.1.data.DataHierarchyLevel.name",
    (data.DataHierarchyLevel, 'value'): "cim.1.data.DataHierarchyLevel.value",
    (data.DataObject, 'acronym'): "cim.1.data.DataObject.acronym",
    (data.DataObject, 'child_object'): "cim.1.data.DataObject.child_object",
    (data.DataObject, 'citations'): "cim.1.data.DataObject.citations",
    (data.DataObject, 'content'): "cim.1.data.DataObject.content",
    (data.DataObject, 'data_status'): "cim.1.data.DataObject.data_status",
    (data.DataObject, 'description'): "cim.1.data.DataObject.description",
    (data.DataObject, 'distribution'): "cim.1.data.DataObject.distribution",
    (data.DataObject, 'extent'): "cim.1.data.DataObject.extent",
    (data.DataObject, 'geometry_model'): "cim.1.data.DataObject.geometry_model",
    (data.DataObject, 'hierarchy_level'): "cim.1.data.DataObject.hierarchy_level",
    (data.DataObject, 'keyword'): "cim.1.data.DataObject.keyword",
    (data.DataObject, 'meta'): "cim.1.data.DataObject.meta",
    (data.DataObject, 'parent_object'): "cim.1.data.DataObject.parent_object",
    (data.DataObject, 'properties'): "cim.1.data.DataObject.properties",
    (data.DataObject, 'purpose'): "cim.1.data.DataObject.purpose",
    (data.DataObject, 'restriction'): "cim.1.data.DataObject.restriction",
    (data.DataObject, 'source_simulation'): "cim.1.data.DataObject.source_simulation",
    (data.DataObject, 'storage'): "cim.1.data.DataObject.storage",
    (data.DataProperty, 'description'): "cim.1.data.DataProperty.description",
    (data.DataRestriction, 'license'): "cim.1.data.DataRestriction.license",
    (data.DataRestriction, 'restriction'): "cim.1.data.DataRestriction.restriction",
    (data.DataRestriction, 'scope'): "cim.1.data.DataRestriction.scope",
    (data.DataStorage, 'format'): "cim.1.data.DataStorage.format",
    (data.DataStorage, 'location'): "cim.1.data.DataStorage.location",
    (data.DataStorage, 'modification_date'): "cim.1.data.DataStorage.modification_date",
    (data.DataStorage, 'size'): "cim.1.data.DataStorage.size",
    (data.DataStorageDb, 'access_string'): "cim.1.data.DataStorageDb.access_string",
    (data.DataStorageDb, 'name'): "cim.1.data.DataStorageDb.name",
    (data.DataStorageDb, 'owner'): "cim.1.data.DataStorageDb.owner",
    (data.DataStorageDb, 'table'): "cim.1.data.DataStorageDb.table",
    (data.DataStorageFile, 'file_name'): "cim.1.data.DataStorageFile.file_name",
    (data.DataStorageFile, 'file_system'): "cim.1.data.DataStorageFile.file_system",
    (data.DataStorageFile, 'path'): "cim.1.data.DataStorageFile.path",
    (data.DataStorageIp, 'file_name'): "cim.1.data.DataStorageIp.file_name",
    (data.DataStorageIp, 'host'): "cim.1.data.DataStorageIp.host",
    (data.DataStorageIp, 'path'): "cim.1.data.DataStorageIp.path",
    (data.DataStorageIp, 'protocol'): "cim.1.data.DataStorageIp.protocol",
    (data.DataTopic, 'description'): "cim.1.data.DataTopic.description",
    (data.DataTopic, 'name'): "cim.1.data.DataTopic.name",
    (data.DataTopic, 'unit'): "cim.1.data.DataTopic.unit",
    (grids.CoordinateList, 'has_constant_offset'): "cim.1.grids.CoordinateList.has_constant_offset",
    (grids.CoordinateList, 'length'): "cim.1.grids.CoordinateList.length",
    (grids.CoordinateList, 'uom'): "cim.1.grids.CoordinateList.uom",
    (grids.GridExtent, 'maximum_latitude'): "cim.1.grids.GridExtent.maximum_latitude",
    (grids.GridExtent, 'maximum_longitude'): "cim.1.grids.GridExtent.maximum_longitude",
    (grids.GridExtent, 'minimum_latitude'): "cim.1.grids.GridExtent.minimum_latitude",
    (grids.GridExtent, 'minimum_longitude'): "cim.1.grids.GridExtent.minimum_longitude",
    (grids.GridExtent, 'units'): "cim.1.grids.GridExtent.units",
    (grids.GridMosaic, 'citations'): "cim.1.grids.GridMosaic.citations",
    (grids.GridMosaic, 'description'): "cim.1.grids.GridMosaic.description",
    (grids.GridMosaic, 'extent'): "cim.1.grids.GridMosaic.extent",
    (grids.GridMosaic, 'has_congruent_tiles'): "cim.1.grids.GridMosaic.has_congruent_tiles",
    (grids.GridMosaic, 'id'): "cim.1.grids.GridMosaic.id",
    (grids.GridMosaic, 'is_leaf'): "cim.1.grids.GridMosaic.is_leaf",
    (grids.GridMosaic, 'long_name'): "cim.1.grids.GridMosaic.long_name",
    (grids.GridMosaic, 'mnemonic'): "cim.1.grids.GridMosaic.mnemonic",
    (grids.GridMosaic, 'mosaic_count'): "cim.1.grids.GridMosaic.mosaic_count",
    (grids.GridMosaic, 'mosaics'): "cim.1.grids.GridMosaic.mosaics",
    (grids.GridMosaic, 'short_name'): "cim.1.grids.GridMosaic.short_name",
    (grids.GridMosaic, 'tile_count'): "cim.1.grids.GridMosaic.tile_count",
    (grids.GridMosaic, 'tiles'): "cim.1.grids.GridMosaic.tiles",
    (grids.GridMosaic, 'type'): "cim.1.grids.GridMosaic.type",
    (grids.GridSpec, 'esm_exchange_grids'): "cim.1.grids.GridSpec.esm_exchange_grids",
    (grids.GridSpec, 'esm_model_grids'): "cim.1.grids.GridSpec.esm_model_grids",
    (grids.GridSpec, 'meta'): "cim.1.grids.GridSpec.meta",
    (grids.GridTile, 'area'): "cim.1.grids.GridTile.area",
    (grids.GridTile, 'cell_array'): "cim.1.grids.GridTile.cell_array",
    (grids.GridTile, 'cell_ref_array'): "cim.1.grids.GridTile.cell_ref_array",
    (grids.GridTile, 'coord_file'): "cim.1.grids.GridTile.coord_file",
    (grids.GridTile, 'coordinate_pole'): "cim.1.grids.GridTile.coordinate_pole",
    (grids.GridTile, 'description'): "cim.1.grids.GridTile.description",
    (grids.GridTile, 'discretization_type'): "cim.1.grids.GridTile.discretization_type",
    (grids.GridTile, 'extent'): "cim.1.grids.GridTile.extent",
    (grids.GridTile, 'geometry_type'): "cim.1.grids.GridTile.geometry_type",
    (grids.GridTile, 'grid_north_pole'): "cim.1.grids.GridTile.grid_north_pole",
    (grids.GridTile, 'horizontal_crs'): "cim.1.grids.GridTile.horizontal_crs",
    (grids.GridTile, 'horizontal_resolution'): "cim.1.grids.GridTile.horizontal_resolution",
    (grids.GridTile, 'id'): "cim.1.grids.GridTile.id",
    (grids.GridTile, 'is_conformal'): "cim.1.grids.GridTile.is_conformal",
    (grids.GridTile, 'is_regular'): "cim.1.grids.GridTile.is_regular",
    (grids.GridTile, 'is_terrain_following'): "cim.1.grids.GridTile.is_terrain_following",
    (grids.GridTile, 'is_uniform'): "cim.1.grids.GridTile.is_uniform",
    (grids.GridTile, 'long_name'): "cim.1.grids.GridTile.long_name",
    (grids.GridTile, 'mnemonic'): "cim.1.grids.GridTile.mnemonic",
    (grids.GridTile, 'nx'): "cim.1.grids.GridTile.nx",
    (grids.GridTile, 'ny'): "cim.1.grids.GridTile.ny",
    (grids.GridTile, 'nz'): "cim.1.grids.GridTile.nz",
    (grids.GridTile, 'refinement_scheme'): "cim.1.grids.GridTile.refinement_scheme",
    (grids.GridTile, 'short_name'): "cim.1.grids.GridTile.short_name",
    (grids.GridTile, 'simple_grid_geom'): "cim.1.grids.GridTile.simple_grid_geom",
    (grids.GridTile, 'vertical_crs'): "cim.1.grids.GridTile.vertical_crs",
    (grids.GridTile, 'vertical_resolution'): "cim.1.grids.GridTile.vertical_resolution",
    (grids.GridTile, 'zcoords'): "cim.1.grids.GridTile.zcoords",
    (grids.GridTileResolutionType, 'description'): "cim.1.grids.GridTileResolutionType.description",
    (grids.GridTileResolutionType, 'properties'): "cim.1.grids.GridTileResolutionType.properties",
    (grids.SimpleGridGeometry, 'dim_order'): "cim.1.grids.SimpleGridGeometry.dim_order",
    (grids.SimpleGridGeometry, 'is_mesh'): "cim.1.grids.SimpleGridGeometry.is_mesh",
    (grids.SimpleGridGeometry, 'num_dims'): "cim.1.grids.SimpleGridGeometry.num_dims",
    (grids.SimpleGridGeometry, 'xcoords'): "cim.1.grids.SimpleGridGeometry.xcoords",
    (grids.SimpleGridGeometry, 'ycoords'): "cim.1.grids.SimpleGridGeometry.ycoords",
    (grids.SimpleGridGeometry, 'zcoords'): "cim.1.grids.SimpleGridGeometry.zcoords",
    (grids.VerticalCoordinateList, 'form'): "cim.1.grids.VerticalCoordinateList.form",
    (grids.VerticalCoordinateList, 'properties'): "cim.1.grids.VerticalCoordinateList.properties",
    (grids.VerticalCoordinateList, 'type'): "cim.1.grids.VerticalCoordinateList.type",
    (misc.DocumentSet, 'data'): "cim.1.misc.DocumentSet.data",
    (misc.DocumentSet, 'ensembles'): "cim.1.misc.DocumentSet.ensembles",
    (misc.DocumentSet, 'experiment'): "cim.1.misc.DocumentSet.experiment",
    (misc.DocumentSet, 'grids'): "cim.1.misc.DocumentSet.grids",
    (misc.DocumentSet, 'meta'): "cim.1.misc.DocumentSet.meta",
    (misc.DocumentSet, 'model'): "cim.1.misc.DocumentSet.model",
    (misc.DocumentSet, 'platform'): "cim.1.misc.DocumentSet.platform",
    (misc.DocumentSet, 'simulation'): "cim.1.misc.DocumentSet.simulation",
    (quality.CimQuality, 'meta'): "cim.1.quality.CimQuality.meta",
    (quality.CimQuality, 'reports'): "cim.1.quality.CimQuality.reports",
    (quality.Evaluation, 'date'): "cim.1.quality.Evaluation.date",
    (quality.Evaluation, 'description'): "cim.1.quality.Evaluation.description",
    (quality.Evaluation, 'did_pass'): "cim.1.quality.Evaluation.did_pass",
    (quality.Evaluation, 'explanation'): "cim.1.quality.Evaluation.explanation",
    (quality.Evaluation, 'specification'): "cim.1.quality.Evaluation.specification",
    (quality.Evaluation, 'specification_hyperlink'): "cim.1.quality.Evaluation.specification_hyperlink",
    (quality.Evaluation, 'title'): "cim.1.quality.Evaluation.title",
    (quality.Evaluation, 'type'): "cim.1.quality.Evaluation.type",
    (quality.Evaluation, 'type_hyperlink'): "cim.1.quality.Evaluation.type_hyperlink",
    (quality.Measure, 'description'): "cim.1.quality.Measure.description",
    (quality.Measure, 'identification'): "cim.1.quality.Measure.identification",
    (quality.Measure, 'name'): "cim.1.quality.Measure.name",
    (quality.Report, 'date'): "cim.1.quality.Report.date",
    (quality.Report, 'evaluation'): "cim.1.quality.Report.evaluation",
    (quality.Report, 'evaluator'): "cim.1.quality.Report.evaluator",
    (quality.Report, 'measure'): "cim.1.quality.Report.measure",
    (shared.Calendar, 'description'): "cim.1.shared.Calendar.description",
    (shared.Calendar, 'length'): "cim.1.shared.Calendar.length",
    (shared.Calendar, 'range'): "cim.1.shared.Calendar.range",
    (shared.Change, 'author'): "cim.1.shared.Change.author",
    (shared.Change, 'date'): "cim.1.shared.Change.date",
    (shared.Change, 'description'): "cim.1.shared.Change.description",
    (shared.Change, 'details'): "cim.1.shared.Change.details",
    (shared.Change, 'name'): "cim.1.shared.Change.name",
    (shared.Change, 'type'): "cim.1.shared.Change.type",
    (shared.ChangeProperty, 'description'): "cim.1.shared.ChangeProperty.description",
    (shared.ChangeProperty, 'id'): "cim.1.shared.ChangeProperty.id",
    (shared.Citation, 'alternative_title'): "cim.1.shared.Citation.alternative_title",
    (shared.Citation, 'collective_title'): "cim.1.shared.Citation.collective_title",
    (shared.Citation, 'date'): "cim.1.shared.Citation.date",
    (shared.Citation, 'date_type'): "cim.1.shared.Citation.date_type",
    (shared.Citation, 'location'): "cim.1.shared.Citation.location",
    (shared.Citation, 'organisation'): "cim.1.shared.Citation.organisation",
    (shared.Citation, 'role'): "cim.1.shared.Citation.role",
    (shared.Citation, 'title'): "cim.1.shared.Citation.title",
    (shared.Citation, 'type'): "cim.1.shared.Citation.type",
    (shared.ClosedDateRange, 'end'): "cim.1.shared.ClosedDateRange.end",
    (shared.ClosedDateRange, 'start'): "cim.1.shared.ClosedDateRange.start",
    (shared.Compiler, 'environment_variables'): "cim.1.shared.Compiler.environment_variables",
    (shared.Compiler, 'language'): "cim.1.shared.Compiler.language",
    (shared.Compiler, 'name'): "cim.1.shared.Compiler.name",
    (shared.Compiler, 'options'): "cim.1.shared.Compiler.options",
    (shared.Compiler, 'type'): "cim.1.shared.Compiler.type",
    (shared.Compiler, 'version'): "cim.1.shared.Compiler.version",
    (shared.DataSource, 'purpose'): "cim.1.shared.DataSource.purpose",
    (shared.DateRange, 'duration'): "cim.1.shared.DateRange.duration",
    (shared.DocMetaInfo, 'author'): "cim.1.shared.DocMetaInfo.author",
    (shared.DocMetaInfo, 'create_date'): "cim.1.shared.DocMetaInfo.create_date",
    (shared.DocMetaInfo, 'drs_keys'): "cim.1.shared.DocMetaInfo.drs_keys",
    (shared.DocMetaInfo, 'drs_path'): "cim.1.shared.DocMetaInfo.drs_path",
    (shared.DocMetaInfo, 'external_ids'): "cim.1.shared.DocMetaInfo.external_ids",
    (shared.DocMetaInfo, 'id'): "cim.1.shared.DocMetaInfo.id",
    (shared.DocMetaInfo, 'institute'): "cim.1.shared.DocMetaInfo.institute",
    (shared.DocMetaInfo, 'project'): "cim.1.shared.DocMetaInfo.project",
    (shared.DocMetaInfo, 'sort_key'): "cim.1.shared.DocMetaInfo.sort_key",
    (shared.DocMetaInfo, 'source'): "cim.1.shared.DocMetaInfo.source",
    (shared.DocMetaInfo, 'source_key'): "cim.1.shared.DocMetaInfo.source_key",
    (shared.DocMetaInfo, 'sub_projects'): "cim.1.shared.DocMetaInfo.sub_projects",
    (shared.DocMetaInfo, 'type'): "cim.1.shared.DocMetaInfo.type",
    (shared.DocMetaInfo, 'type_display_name'): "cim.1.shared.DocMetaInfo.type_display_name",
    (shared.DocMetaInfo, 'type_sort_key'): "cim.1.shared.DocMetaInfo.type_sort_key",
    (shared.DocMetaInfo, 'update_date'): "cim.1.shared.DocMetaInfo.update_date",
    (shared.DocMetaInfo, 'version'): "cim.1.shared.DocMetaInfo.version",
    (shared.DocReference, 'canonical_name'): "cim.1.shared.DocReference.canonical_name",
    (shared.DocReference, 'changes'): "cim.1.shared.DocReference.changes",
    (shared.DocReference, 'constraint_vocabulary'): "cim.1.shared.DocReference.constraint_vocabulary",
    (shared.DocReference, 'context'): "cim.1.shared.DocReference.context",
    (shared.DocReference, 'description'): "cim.1.shared.DocReference.description",
    (shared.DocReference, 'external_id'): "cim.1.shared.DocReference.external_id",
    (shared.DocReference, 'id'): "cim.1.shared.DocReference.id",
    (shared.DocReference, 'institute'): "cim.1.shared.DocReference.institute",
    (shared.DocReference, 'linkage'): "cim.1.shared.DocReference.linkage",
    (shared.DocReference, 'name'): "cim.1.shared.DocReference.name",
    (shared.DocReference, 'protocol'): "cim.1.shared.DocReference.protocol",
    (shared.DocReference, 'relationship'): "cim.1.shared.DocReference.relationship",
    (shared.DocReference, 'type'): "cim.1.shared.DocReference.type",
    (shared.DocReference, 'url'): "cim.1.shared.DocReference.url",
    (shared.DocReference, 'version'): "cim.1.shared.DocReference.version",
    (shared.License, 'contact'): "cim.1.shared.License.contact",
    (shared.License, 'description'): "cim.1.shared.License.description",
    (shared.License, 'is_unrestricted'): "cim.1.shared.License.is_unrestricted",
    (shared.License, 'name'): "cim.1.shared.License.name",
    (shared.Machine, 'cores_per_processor'): "cim.1.shared.Machine.cores_per_processor",
    (shared.Machine, 'description'): "cim.1.shared.Machine.description",
    (shared.Machine, 'interconnect'): "cim.1.shared.Machine.interconnect",
    (shared.Machine, 'libraries'): "cim.1.shared.Machine.libraries",
    (shared.Machine, 'location'): "cim.1.shared.Machine.location",
    (shared.Machine, 'maximum_processors'): "cim.1.shared.Machine.maximum_processors",
    (shared.Machine, 'name'): "cim.1.shared.Machine.name",
    (shared.Machine, 'operating_system'): "cim.1.shared.Machine.operating_system",
    (shared.Machine, 'processor_type'): "cim.1.shared.Machine.processor_type",
    (shared.Machine, 'system'): "cim.1.shared.Machine.system",
    (shared.Machine, 'type'): "cim.1.shared.Machine.type",
    (shared.Machine, 'vendor'): "cim.1.shared.Machine.vendor",
    (shared.MachineCompilerUnit, 'compilers'): "cim.1.shared.MachineCompilerUnit.compilers",
    (shared.MachineCompilerUnit, 'machine'): "cim.1.shared.MachineCompilerUnit.machine",
    (shared.OpenDateRange, 'end'): "cim.1.shared.OpenDateRange.end",
    (shared.OpenDateRange, 'start'): "cim.1.shared.OpenDateRange.start",
    (shared.Platform, 'contacts'): "cim.1.shared.Platform.contacts",
    (shared.Platform, 'description'): "cim.1.shared.Platform.description",
    (shared.Platform, 'long_name'): "cim.1.shared.Platform.long_name",
    (shared.Platform, 'meta'): "cim.1.shared.Platform.meta",
    (shared.Platform, 'short_name'): "cim.1.shared.Platform.short_name",
    (shared.Platform, 'units'): "cim.1.shared.Platform.units",
    (shared.Property, 'name'): "cim.1.shared.Property.name",
    (shared.Property, 'value'): "cim.1.shared.Property.value",
    (shared.Relationship, 'description'): "cim.1.shared.Relationship.description",
    (shared.ResponsibleParty, 'abbreviation'): "cim.1.shared.ResponsibleParty.abbreviation",
    (shared.ResponsibleParty, 'address'): "cim.1.shared.ResponsibleParty.address",
    (shared.ResponsibleParty, 'email'): "cim.1.shared.ResponsibleParty.email",
    (shared.ResponsibleParty, 'individual_name'): "cim.1.shared.ResponsibleParty.individual_name",
    (shared.ResponsibleParty, 'organisation_name'): "cim.1.shared.ResponsibleParty.organisation_name",
    (shared.ResponsibleParty, 'role'): "cim.1.shared.ResponsibleParty.role",
    (shared.ResponsibleParty, 'url'): "cim.1.shared.ResponsibleParty.url",
    (shared.Standard, 'description'): "cim.1.shared.Standard.description",
    (shared.Standard, 'name'): "cim.1.shared.Standard.name",
    (shared.Standard, 'version'): "cim.1.shared.Standard.version",
    (shared.StandardName, 'is_open'): "cim.1.shared.StandardName.is_open",
    (shared.StandardName, 'standards'): "cim.1.shared.StandardName.standards",
    (shared.StandardName, 'value'): "cim.1.shared.StandardName.value",
    (software.Component, 'citations'): "cim.1.software.Component.citations",
    (software.Component, 'code_access'): "cim.1.software.Component.code_access",
    (software.Component, 'composition'): "cim.1.software.Component.composition",
    (software.Component, 'coupling_framework'): "cim.1.software.Component.coupling_framework",
    (software.Component, 'dependencies'): "cim.1.software.Component.dependencies",
    (software.Component, 'deployments'): "cim.1.software.Component.deployments",
    (software.Component, 'description'): "cim.1.software.Component.description",
    (software.Component, 'funding_sources'): "cim.1.software.Component.funding_sources",
    (software.Component, 'grid'): "cim.1.software.Component.grid",
    (software.Component, 'is_embedded'): "cim.1.software.Component.is_embedded",
    (software.Component, 'language'): "cim.1.software.Component.language",
    (software.Component, 'license'): "cim.1.software.Component.license",
    (software.Component, 'long_name'): "cim.1.software.Component.long_name",
    (software.Component, 'online_resource'): "cim.1.software.Component.online_resource",
    (software.Component, 'parent'): "cim.1.software.Component.parent",
    (software.Component, 'previous_version'): "cim.1.software.Component.previous_version",
    (software.Component, 'properties'): "cim.1.software.Component.properties",
    (software.Component, 'release_date'): "cim.1.software.Component.release_date",
    (software.Component, 'responsible_parties'): "cim.1.software.Component.responsible_parties",
    (software.Component, 'short_name'): "cim.1.software.Component.short_name",
    (software.Component, 'sub_components'): "cim.1.software.Component.sub_components",
    (software.Component, 'version'): "cim.1.software.Component.version",
    (software.ComponentLanguage, 'name'): "cim.1.software.ComponentLanguage.name",
    (software.ComponentLanguage, 'properties'): "cim.1.software.ComponentLanguage.properties",
    (software.ComponentProperty, 'citations'): "cim.1.software.ComponentProperty.citations",
    (software.ComponentProperty, 'description'): "cim.1.software.ComponentProperty.description",
    (software.ComponentProperty, 'grid'): "cim.1.software.ComponentProperty.grid",
    (software.ComponentProperty, 'intent'): "cim.1.software.ComponentProperty.intent",
    (software.ComponentProperty, 'is_represented'): "cim.1.software.ComponentProperty.is_represented",
    (software.ComponentProperty, 'long_name'): "cim.1.software.ComponentProperty.long_name",
    (software.ComponentProperty, 'short_name'): "cim.1.software.ComponentProperty.short_name",
    (software.ComponentProperty, 'standard_names'): "cim.1.software.ComponentProperty.standard_names",
    (software.ComponentProperty, 'sub_properties'): "cim.1.software.ComponentProperty.sub_properties",
    (software.ComponentProperty, 'units'): "cim.1.software.ComponentProperty.units",
    (software.ComponentProperty, 'values'): "cim.1.software.ComponentProperty.values",
    (software.Composition, 'couplings'): "cim.1.software.Composition.couplings",
    (software.Composition, 'description'): "cim.1.software.Composition.description",
    (software.Connection, 'description'): "cim.1.software.Connection.description",
    (software.Connection, 'priming'): "cim.1.software.Connection.priming",
    (software.Connection, 'properties'): "cim.1.software.Connection.properties",
    (software.Connection, 'sources'): "cim.1.software.Connection.sources",
    (software.Connection, 'spatial_regridding'): "cim.1.software.Connection.spatial_regridding",
    (software.Connection, 'target'): "cim.1.software.Connection.target",
    (software.Connection, 'time_lag'): "cim.1.software.Connection.time_lag",
    (software.Connection, 'time_profile'): "cim.1.software.Connection.time_profile",
    (software.Connection, 'time_transformation'): "cim.1.software.Connection.time_transformation",
    (software.Connection, 'transformers'): "cim.1.software.Connection.transformers",
    (software.Connection, 'type'): "cim.1.software.Connection.type",
    (software.ConnectionEndpoint, 'data_source'): "cim.1.software.ConnectionEndpoint.data_source",
    (software.ConnectionEndpoint, 'instance_id'): "cim.1.software.ConnectionEndpoint.instance_id",
    (software.ConnectionEndpoint, 'properties'): "cim.1.software.ConnectionEndpoint.properties",
    (software.Coupling, 'connections'): "cim.1.software.Coupling.connections",
    (software.Coupling, 'description'): "cim.1.software.Coupling.description",
    (software.Coupling, 'is_fully_specified'): "cim.1.software.Coupling.is_fully_specified",
    (software.Coupling, 'priming'): "cim.1.software.Coupling.priming",
    (software.Coupling, 'properties'): "cim.1.software.Coupling.properties",
    (software.Coupling, 'purpose'): "cim.1.software.Coupling.purpose",
    (software.Coupling, 'sources'): "cim.1.software.Coupling.sources",
    (software.Coupling, 'spatial_regriddings'): "cim.1.software.Coupling.spatial_regriddings",
    (software.Coupling, 'target'): "cim.1.software.Coupling.target",
    (software.Coupling, 'time_lag'): "cim.1.software.Coupling.time_lag",
    (software.Coupling, 'time_profile'): "cim.1.software.Coupling.time_profile",
    (software.Coupling, 'time_transformation'): "cim.1.software.Coupling.time_transformation",
    (software.Coupling, 'transformers'): "cim.1.software.Coupling.transformers",
    (software.Coupling, 'type'): "cim.1.software.Coupling.type",
    (software.CouplingEndpoint, 'data_source'): "cim.1.software.CouplingEndpoint.data_source",
    (software.CouplingEndpoint, 'instance_id'): "cim.1.software.CouplingEndpoint.instance_id",
    (software.CouplingEndpoint, 'properties'): "cim.1.software.CouplingEndpoint.properties",
    (software.Deployment, 'deployment_date'): "cim.1.software.Deployment.deployment_date",
    (software.Deployment, 'description'): "cim.1.software.Deployment.description",
    (software.Deployment, 'executable_arguments'): "cim.1.software.Deployment.executable_arguments",
    (software.Deployment, 'executable_name'): "cim.1.software.Deployment.executable_name",
    (software.Deployment, 'parallelisation'): "cim.1.software.Deployment.parallelisation",
    (software.Deployment, 'platform'): "cim.1.software.Deployment.platform",
    (software.EntryPoint, 'name'): "cim.1.software.EntryPoint.name",
    (software.ModelComponent, 'activity'): "cim.1.software.ModelComponent.activity",
    (software.ModelComponent, 'meta'): "cim.1.software.ModelComponent.meta",
    (software.ModelComponent, 'timing'): "cim.1.software.ModelComponent.timing",
    (software.ModelComponent, 'type'): "cim.1.software.ModelComponent.type",
    (software.ModelComponent, 'types'): "cim.1.software.ModelComponent.types",
    (software.Parallelisation, 'processes'): "cim.1.software.Parallelisation.processes",
    (software.Parallelisation, 'ranks'): "cim.1.software.Parallelisation.ranks",
    (software.ProcessorComponent, 'meta'): "cim.1.software.ProcessorComponent.meta",
    (software.Rank, 'increment'): "cim.1.software.Rank.increment",
    (software.Rank, 'max'): "cim.1.software.Rank.max",
    (software.Rank, 'min'): "cim.1.software.Rank.min",
    (software.Rank, 'value'): "cim.1.software.Rank.value",
    (software.SpatialRegridding, 'dimension'): "cim.1.software.SpatialRegridding.dimension",
    (software.SpatialRegridding, 'properties'): "cim.1.software.SpatialRegridding.properties",
    (software.SpatialRegridding, 'standard_method'): "cim.1.software.SpatialRegridding.standard_method",
    (software.SpatialRegridding, 'user_method'): "cim.1.software.SpatialRegridding.user_method",
    (software.SpatialRegriddingUserMethod, 'file'): "cim.1.software.SpatialRegriddingUserMethod.file",
    (software.SpatialRegriddingUserMethod, 'name'): "cim.1.software.SpatialRegriddingUserMethod.name",
    (software.StatisticalModelComponent, 'meta'): "cim.1.software.StatisticalModelComponent.meta",
    (software.StatisticalModelComponent, 'timing'): "cim.1.software.StatisticalModelComponent.timing",
    (software.StatisticalModelComponent, 'type'): "cim.1.software.StatisticalModelComponent.type",
    (software.StatisticalModelComponent, 'types'): "cim.1.software.StatisticalModelComponent.types",
    (software.TimeLag, 'units'): "cim.1.software.TimeLag.units",
    (software.TimeLag, 'value'): "cim.1.software.TimeLag.value",
    (software.TimeTransformation, 'description'): "cim.1.software.TimeTransformation.description",
    (software.TimeTransformation, 'mapping_type'): "cim.1.software.TimeTransformation.mapping_type",
    (software.Timing, 'end'): "cim.1.software.Timing.end",
    (software.Timing, 'is_variable_rate'): "cim.1.software.Timing.is_variable_rate",
    (software.Timing, 'rate'): "cim.1.software.Timing.rate",
    (software.Timing, 'start'): "cim.1.software.Timing.start",
    (software.Timing, 'units'): "cim.1.software.Timing.units",

    # ------------------------------------------------
    # Enums.
    # ------------------------------------------------

    activity.ConformanceType: "cim.1.activity.ConformanceType",
    activity.DownscalingType: "cim.1.activity.DownscalingType",
    activity.EnsembleType: "cim.1.activity.EnsembleType",
    activity.ExperimentRelationshipType: "cim.1.activity.ExperimentRelationshipType",
    activity.FrequencyType: "cim.1.activity.FrequencyType",
    activity.ProjectType: "cim.1.activity.ProjectType",
    activity.ResolutionType: "cim.1.activity.ResolutionType",
    activity.SimulationRelationshipType: "cim.1.activity.SimulationRelationshipType",
    activity.SimulationType: "cim.1.activity.SimulationType",
    data.DataHierarchyType: "cim.1.data.DataHierarchyType",
    data.DataStatusType: "cim.1.data.DataStatusType",
    grids.ArcTypeEnum: "cim.1.grids.ArcTypeEnum",
    grids.DiscretizationEnum: "cim.1.grids.DiscretizationEnum",
    grids.FeatureTypeEnum: "cim.1.grids.FeatureTypeEnum",
    grids.GeometryTypeEnum: "cim.1.grids.GeometryTypeEnum",
    grids.GridNodePositionEnum: "cim.1.grids.GridNodePositionEnum",
    grids.GridTypeEnum: "cim.1.grids.GridTypeEnum",
    grids.HorizontalCsEnum: "cim.1.grids.HorizontalCsEnum",
    grids.RefinementTypeEnum: "cim.1.grids.RefinementTypeEnum",
    grids.VerticalCsEnum: "cim.1.grids.VerticalCsEnum",
    quality.CimFeatureType: "cim.1.quality.CimFeatureType",
    quality.CimResultType: "cim.1.quality.CimResultType",
    quality.CimScopeCodeType: "cim.1.quality.CimScopeCodeType",
    quality.QualityIssueType: "cim.1.quality.QualityIssueType",
    quality.QualitySeverityType: "cim.1.quality.QualitySeverityType",
    quality.QualityStatusType: "cim.1.quality.QualityStatusType",
    shared.ChangePropertyType: "cim.1.shared.ChangePropertyType",
    shared.CompilerType: "cim.1.shared.CompilerType",
    shared.DataPurpose: "cim.1.shared.DataPurpose",
    shared.InterconnectType: "cim.1.shared.InterconnectType",
    shared.MachineType: "cim.1.shared.MachineType",
    shared.MachineVendorType: "cim.1.shared.MachineVendorType",
    shared.OperatingSystemType: "cim.1.shared.OperatingSystemType",
    shared.ProcessorType: "cim.1.shared.ProcessorType",
    shared.UnitType: "cim.1.shared.UnitType",
    software.ComponentPropertyIntentType: "cim.1.software.ComponentPropertyIntentType",
    software.ConnectionType: "cim.1.software.ConnectionType",
    software.CouplingFrameworkType: "cim.1.software.CouplingFrameworkType",
    software.ModelComponentType: "cim.1.software.ModelComponentType",
    software.SpatialRegriddingDimensionType: "cim.1.software.SpatialRegriddingDimensionType",
    software.SpatialRegriddingStandardMethodType: "cim.1.software.SpatialRegriddingStandardMethodType",
    software.StatisticalModelComponentType: "cim.1.software.StatisticalModelComponentType",
    software.TimeMappingType: "cim.1.software.TimeMappingType",
    software.TimingUnits: "cim.1.software.TimingUnits",

    # ------------------------------------------------
    # Enum members.
    # ------------------------------------------------

    (activity.ConformanceType, 'not-xxx'): "cim.1.activity.ConformanceType.not-xxx",
    (activity.ConformanceType, 'not conformant'): "cim.1.activity.ConformanceType.not-conformant",
    (activity.ConformanceType, 'standard config'): "cim.1.activity.ConformanceType.standard-config",
    (activity.ConformanceType, 'via inputs'): "cim.1.activity.ConformanceType.via-inputs",
    (activity.ConformanceType, 'via model mods'): "cim.1.activity.ConformanceType.via-model-mods",
    (activity.ConformanceType, 'combination'): "cim.1.activity.ConformanceType.combination",
    (activity.DownscalingType, 'statistical'): "cim.1.activity.DownscalingType.statistical",
    (activity.DownscalingType, 'dynamic'): "cim.1.activity.DownscalingType.dynamic",
    (activity.ExperimentRelationshipType, 'previousRealisation'): "cim.1.activity.ExperimentRelationshipType.previousRealisation",
    (activity.ExperimentRelationshipType, 'continuationOf'): "cim.1.activity.ExperimentRelationshipType.continuationOf",
    (activity.ExperimentRelationshipType, 'controlExperiment'): "cim.1.activity.ExperimentRelationshipType.controlExperiment",
    (activity.ExperimentRelationshipType, 'higherResolutionVersionOf'): "cim.1.activity.ExperimentRelationshipType.higherResolutionVersionOf",
    (activity.ExperimentRelationshipType, 'lowerResolutionVersionOf'): "cim.1.activity.ExperimentRelationshipType.lowerResolutionVersionOf",
    (activity.ExperimentRelationshipType, 'increaseEnsembleOf'): "cim.1.activity.ExperimentRelationshipType.increaseEnsembleOf",
    (activity.ExperimentRelationshipType, 'modifiedInputMethodOf'): "cim.1.activity.ExperimentRelationshipType.modifiedInputMethodOf",
    (activity.ExperimentRelationshipType, 'shorterVersionOf'): "cim.1.activity.ExperimentRelationshipType.shorterVersionOf",
    (activity.ExperimentRelationshipType, 'extensionOf'): "cim.1.activity.ExperimentRelationshipType.extensionOf",
    (activity.SimulationRelationshipType, 'extensionOf'): "cim.1.activity.SimulationRelationshipType.extensionOf",
    (activity.SimulationRelationshipType, 'responseTo'): "cim.1.activity.SimulationRelationshipType.responseTo",
    (activity.SimulationRelationshipType, 'continuationOf'): "cim.1.activity.SimulationRelationshipType.continuationOf",
    (activity.SimulationRelationshipType, 'previousSimulation'): "cim.1.activity.SimulationRelationshipType.previousSimulation",
    (activity.SimulationRelationshipType, 'higherResolutionVersionOf'): "cim.1.activity.SimulationRelationshipType.higherResolutionVersionOf",
    (activity.SimulationRelationshipType, 'lowerResolutionVersionOf'): "cim.1.activity.SimulationRelationshipType.lowerResolutionVersionOf",
    (activity.SimulationRelationshipType, 'fixedVersionOf'): "cim.1.activity.SimulationRelationshipType.fixedVersionOf",
    (activity.SimulationRelationshipType, 'followingSimulation'): "cim.1.activity.SimulationRelationshipType.followingSimulation",
    (activity.SimulationType, 'simulationRun'): "cim.1.activity.SimulationType.simulationRun",
    (activity.SimulationType, 'assimilation'): "cim.1.activity.SimulationType.assimilation",
    (activity.SimulationType, 'simulationComposite'): "cim.1.activity.SimulationType.simulationComposite",
    (data.DataStatusType, 'complete'): "cim.1.data.DataStatusType.complete",
    (data.DataStatusType, 'metadataOnly'): "cim.1.data.DataStatusType.metadataOnly",
    (data.DataStatusType, 'continuouslySupplemented'): "cim.1.data.DataStatusType.continuouslySupplemented",
    (grids.ArcTypeEnum, 'geodesic'): "cim.1.grids.ArcTypeEnum.geodesic",
    (grids.ArcTypeEnum, 'great_circle'): "cim.1.grids.ArcTypeEnum.great_circle",
    (grids.ArcTypeEnum, 'small_circle'): "cim.1.grids.ArcTypeEnum.small_circle",
    (grids.ArcTypeEnum, 'complex'): "cim.1.grids.ArcTypeEnum.complex",
    (grids.DiscretizationEnum, 'logically_rectangular'): "cim.1.grids.DiscretizationEnum.logically_rectangular",
    (grids.DiscretizationEnum, 'structured_triangular'): "cim.1.grids.DiscretizationEnum.structured_triangular",
    (grids.DiscretizationEnum, 'unstructured_triangular'): "cim.1.grids.DiscretizationEnum.unstructured_triangular",
    (grids.DiscretizationEnum, 'pixel-based_catchment'): "cim.1.grids.DiscretizationEnum.pixel-based_catchment",
    (grids.DiscretizationEnum, 'unstructured_polygonal'): "cim.1.grids.DiscretizationEnum.unstructured_polygonal",
    (grids.DiscretizationEnum, 'spherical_harmonics'): "cim.1.grids.DiscretizationEnum.spherical_harmonics",
    (grids.DiscretizationEnum, 'other'): "cim.1.grids.DiscretizationEnum.other",
    (grids.FeatureTypeEnum, 'point'): "cim.1.grids.FeatureTypeEnum.point",
    (grids.FeatureTypeEnum, 'edge'): "cim.1.grids.FeatureTypeEnum.edge",
    (grids.GeometryTypeEnum, 'ellipsoid'): "cim.1.grids.GeometryTypeEnum.ellipsoid",
    (grids.GeometryTypeEnum, 'plane'): "cim.1.grids.GeometryTypeEnum.plane",
    (grids.GeometryTypeEnum, 'sphere'): "cim.1.grids.GeometryTypeEnum.sphere",
    (grids.GridNodePositionEnum, 'centre'): "cim.1.grids.GridNodePositionEnum.centre",
    (grids.GridNodePositionEnum, 'plane'): "cim.1.grids.GridNodePositionEnum.plane",
    (grids.GridNodePositionEnum, 'sphere'): "cim.1.grids.GridNodePositionEnum.sphere",
    (grids.GridTypeEnum, 'cubed_sphere'): "cim.1.grids.GridTypeEnum.cubed_sphere",
    (grids.GridTypeEnum, 'displaced_pole'): "cim.1.grids.GridTypeEnum.displaced_pole",
    (grids.GridTypeEnum, 'icosahedral_geodesic'): "cim.1.grids.GridTypeEnum.icosahedral_geodesic",
    (grids.GridTypeEnum, 'reduced_gaussian'): "cim.1.grids.GridTypeEnum.reduced_gaussian",
    (grids.GridTypeEnum, 'regular_lat_lon'): "cim.1.grids.GridTypeEnum.regular_lat_lon",
    (grids.GridTypeEnum, 'spectral_gaussian'): "cim.1.grids.GridTypeEnum.spectral_gaussian",
    (grids.GridTypeEnum, 'tripolar'): "cim.1.grids.GridTypeEnum.tripolar",
    (grids.GridTypeEnum, 'yin_yang'): "cim.1.grids.GridTypeEnum.yin_yang",
    (grids.GridTypeEnum, 'composite'): "cim.1.grids.GridTypeEnum.composite",
    (grids.GridTypeEnum, 'other'): "cim.1.grids.GridTypeEnum.other",
    (grids.HorizontalCsEnum, 'cartesian'): "cim.1.grids.HorizontalCsEnum.cartesian",
    (grids.HorizontalCsEnum, 'ellipsoidal'): "cim.1.grids.HorizontalCsEnum.ellipsoidal",
    (grids.HorizontalCsEnum, 'polar'): "cim.1.grids.HorizontalCsEnum.polar",
    (grids.HorizontalCsEnum, 'spherical'): "cim.1.grids.HorizontalCsEnum.spherical",
    (grids.RefinementTypeEnum, 'none'): "cim.1.grids.RefinementTypeEnum.none",
    (grids.RefinementTypeEnum, 'integer'): "cim.1.grids.RefinementTypeEnum.integer",
    (grids.RefinementTypeEnum, 'rational'): "cim.1.grids.RefinementTypeEnum.rational",
    (grids.VerticalCsEnum, 'mass-based'): "cim.1.grids.VerticalCsEnum.mass-based",
    (grids.VerticalCsEnum, 'space-based'): "cim.1.grids.VerticalCsEnum.space-based",
    (quality.CimFeatureType, 'file'): "cim.1.quality.CimFeatureType.file",
    (quality.CimFeatureType, 'diagnostic'): "cim.1.quality.CimFeatureType.diagnostic",
    (quality.CimResultType, 'plot'): "cim.1.quality.CimResultType.plot",
    (quality.CimResultType, 'document'): "cim.1.quality.CimResultType.document",
    (quality.CimResultType, 'logfile'): "cim.1.quality.CimResultType.logfile",
    (quality.CimScopeCodeType, 'dataset'): "cim.1.quality.CimScopeCodeType.dataset",
    (quality.CimScopeCodeType, 'software'): "cim.1.quality.CimScopeCodeType.software",
    (quality.CimScopeCodeType, 'service'): "cim.1.quality.CimScopeCodeType.service",
    (quality.CimScopeCodeType, 'model'): "cim.1.quality.CimScopeCodeType.model",
    (quality.CimScopeCodeType, 'modelComponent'): "cim.1.quality.CimScopeCodeType.modelComponent",
    (quality.CimScopeCodeType, 'simulation'): "cim.1.quality.CimScopeCodeType.simulation",
    (quality.CimScopeCodeType, 'experiment'): "cim.1.quality.CimScopeCodeType.experiment",
    (quality.CimScopeCodeType, 'numericalRequirement'): "cim.1.quality.CimScopeCodeType.numericalRequirement",
    (quality.CimScopeCodeType, 'ensemble'): "cim.1.quality.CimScopeCodeType.ensemble",
    (quality.CimScopeCodeType, 'file'): "cim.1.quality.CimScopeCodeType.file",
    (quality.QualityIssueType, 'metadata'): "cim.1.quality.QualityIssueType.metadata",
    (quality.QualityIssueType, 'data_format'): "cim.1.quality.QualityIssueType.data_format",
    (quality.QualityIssueType, 'data_content'): "cim.1.quality.QualityIssueType.data_content",
    (quality.QualityIssueType, 'data_indexing'): "cim.1.quality.QualityIssueType.data_indexing",
    (quality.QualityIssueType, 'science'): "cim.1.quality.QualityIssueType.science",
    (quality.QualitySeverityType, 'cosmetic'): "cim.1.quality.QualitySeverityType.cosmetic",
    (quality.QualitySeverityType, 'minor'): "cim.1.quality.QualitySeverityType.minor",
    (quality.QualitySeverityType, 'major'): "cim.1.quality.QualitySeverityType.major",
    (quality.QualityStatusType, 'reported'): "cim.1.quality.QualityStatusType.reported",
    (quality.QualityStatusType, 'confirmed'): "cim.1.quality.QualityStatusType.confirmed",
    (quality.QualityStatusType, 'partially_resolved'): "cim.1.quality.QualityStatusType.partially_resolved",
    (quality.QualityStatusType, 'resolved'): "cim.1.quality.QualityStatusType.resolved",
    (shared.ChangePropertyType, 'InputMod'): "cim.1.shared.ChangePropertyType.InputMod",
    (shared.ChangePropertyType, 'ModelMod'): "cim.1.shared.ChangePropertyType.ModelMod",
    (shared.ChangePropertyType, 'Decrement'): "cim.1.shared.ChangePropertyType.Decrement",
    (shared.ChangePropertyType, 'Increment'): "cim.1.shared.ChangePropertyType.Increment",
    (shared.ChangePropertyType, 'Redistribution'): "cim.1.shared.ChangePropertyType.Redistribution",
    (shared.ChangePropertyType, 'Replacement'): "cim.1.shared.ChangePropertyType.Replacement",
    (shared.ChangePropertyType, 'ParameterChange'): "cim.1.shared.ChangePropertyType.ParameterChange",
    (shared.ChangePropertyType, 'CodeChange'): "cim.1.shared.ChangePropertyType.CodeChange",
    (shared.ChangePropertyType, 'AncillaryFile'): "cim.1.shared.ChangePropertyType.AncillaryFile",
    (shared.ChangePropertyType, 'BoundaryCondition'): "cim.1.shared.ChangePropertyType.BoundaryCondition",
    (shared.ChangePropertyType, 'InitialCondition'): "cim.1.shared.ChangePropertyType.InitialCondition",
    (shared.ChangePropertyType, 'Unused'): "cim.1.shared.ChangePropertyType.Unused",
    (shared.DataPurpose, 'ancillaryFile'): "cim.1.shared.DataPurpose.ancillaryFile",
    (shared.DataPurpose, 'boundaryCondition'): "cim.1.shared.DataPurpose.boundaryCondition",
    (shared.DataPurpose, 'initialCondition'): "cim.1.shared.DataPurpose.initialCondition",
    (shared.MachineType, 'Parallel'): "cim.1.shared.MachineType.Parallel",
    (shared.MachineType, 'Vector'): "cim.1.shared.MachineType.Vector",
    (shared.MachineType, 'Beowulf'): "cim.1.shared.MachineType.Beowulf",
    (software.ComponentPropertyIntentType, 'in'): "cim.1.software.ComponentPropertyIntentType.in",
    (software.ComponentPropertyIntentType, 'out'): "cim.1.software.ComponentPropertyIntentType.out",
    (software.ComponentPropertyIntentType, 'inout'): "cim.1.software.ComponentPropertyIntentType.inout",
    (software.CouplingFrameworkType, 'BFG'): "cim.1.software.CouplingFrameworkType.BFG",
    (software.CouplingFrameworkType, 'ESMF'): "cim.1.software.CouplingFrameworkType.ESMF",
    (software.CouplingFrameworkType, 'OASIS'): "cim.1.software.CouplingFrameworkType.OASIS",
    (software.SpatialRegriddingDimensionType, '1D'): "cim.1.software.SpatialRegriddingDimensionType.1D",
    (software.SpatialRegriddingDimensionType, '2D'): "cim.1.software.SpatialRegriddingDimensionType.2D",
    (software.SpatialRegriddingDimensionType, '3D'): "cim.1.software.SpatialRegriddingDimensionType.3D",
    (software.SpatialRegriddingStandardMethodType, 'linear'): "cim.1.software.SpatialRegriddingStandardMethodType.linear",
    (software.SpatialRegriddingStandardMethodType, 'near-neighbour'): "cim.1.software.SpatialRegriddingStandardMethodType.near-neighbour",
    (software.SpatialRegriddingStandardMethodType, 'cubic'): "cim.1.software.SpatialRegriddingStandardMethodType.cubic",
    (software.SpatialRegriddingStandardMethodType, 'conservative-first-order'): "cim.1.software.SpatialRegriddingStandardMethodType.conservative-first-order",
    (software.SpatialRegriddingStandardMethodType, 'conservative-second-order'): "cim.1.software.SpatialRegriddingStandardMethodType.conservative-second-order",
    (software.SpatialRegriddingStandardMethodType, 'conservative'): "cim.1.software.SpatialRegriddingStandardMethodType.conservative",
    (software.SpatialRegriddingStandardMethodType, 'non-conservative'): "cim.1.software.SpatialRegriddingStandardMethodType.non-conservative",
    (software.TimingUnits, 'seconds'): "cim.1.software.TimingUnits.seconds",
    (software.TimingUnits, 'minutes'): "cim.1.software.TimingUnits.minutes",
    (software.TimingUnits, 'hours'): "cim.1.software.TimingUnits.hours",
    (software.TimingUnits, 'days'): "cim.1.software.TimingUnits.days",
    (software.TimingUnits, 'months'): "cim.1.software.TimingUnits.months",
    (software.TimingUnits, 'years'): "cim.1.software.TimingUnits.years",
    (software.TimingUnits, 'decades'): "cim.1.software.TimingUnits.decades",
    (software.TimingUnits, 'centuries'): "cim.1.software.TimingUnits.centuries",
}

# Set inline type keys.
activity.Activity.type_key = KEYS[activity.Activity]
activity.BoundaryCondition.type_key = KEYS[activity.BoundaryCondition]
activity.Conformance.type_key = KEYS[activity.Conformance]
activity.ConformanceType.type_key = KEYS[activity.ConformanceType]
activity.DownscalingSimulation.type_key = KEYS[activity.DownscalingSimulation]
activity.DownscalingType.type_key = KEYS[activity.DownscalingType]
activity.Ensemble.type_key = KEYS[activity.Ensemble]
activity.EnsembleMember.type_key = KEYS[activity.EnsembleMember]
activity.EnsembleType.type_key = KEYS[activity.EnsembleType]
activity.Experiment.type_key = KEYS[activity.Experiment]
activity.ExperimentRelationship.type_key = KEYS[activity.ExperimentRelationship]
activity.ExperimentRelationshipTarget.type_key = KEYS[activity.ExperimentRelationshipTarget]
activity.ExperimentRelationshipType.type_key = KEYS[activity.ExperimentRelationshipType]
activity.FrequencyType.type_key = KEYS[activity.FrequencyType]
activity.InitialCondition.type_key = KEYS[activity.InitialCondition]
activity.LateralBoundaryCondition.type_key = KEYS[activity.LateralBoundaryCondition]
activity.MeasurementCampaign.type_key = KEYS[activity.MeasurementCampaign]
activity.NumericalActivity.type_key = KEYS[activity.NumericalActivity]
activity.NumericalExperiment.type_key = KEYS[activity.NumericalExperiment]
activity.NumericalRequirement.type_key = KEYS[activity.NumericalRequirement]
activity.NumericalRequirementOption.type_key = KEYS[activity.NumericalRequirementOption]
activity.OutputRequirement.type_key = KEYS[activity.OutputRequirement]
activity.PhysicalModification.type_key = KEYS[activity.PhysicalModification]
activity.ProjectType.type_key = KEYS[activity.ProjectType]
activity.ResolutionType.type_key = KEYS[activity.ResolutionType]
activity.Simulation.type_key = KEYS[activity.Simulation]
activity.SimulationComposite.type_key = KEYS[activity.SimulationComposite]
activity.SimulationRelationship.type_key = KEYS[activity.SimulationRelationship]
activity.SimulationRelationshipTarget.type_key = KEYS[activity.SimulationRelationshipTarget]
activity.SimulationRelationshipType.type_key = KEYS[activity.SimulationRelationshipType]
activity.SimulationRun.type_key = KEYS[activity.SimulationRun]
activity.SimulationType.type_key = KEYS[activity.SimulationType]
activity.SpatioTemporalConstraint.type_key = KEYS[activity.SpatioTemporalConstraint]
data.DataContent.type_key = KEYS[data.DataContent]
data.DataDistribution.type_key = KEYS[data.DataDistribution]
data.DataExtent.type_key = KEYS[data.DataExtent]
data.DataExtentGeographical.type_key = KEYS[data.DataExtentGeographical]
data.DataExtentTemporal.type_key = KEYS[data.DataExtentTemporal]
data.DataExtentTimeInterval.type_key = KEYS[data.DataExtentTimeInterval]
data.DataHierarchyLevel.type_key = KEYS[data.DataHierarchyLevel]
data.DataHierarchyType.type_key = KEYS[data.DataHierarchyType]
data.DataObject.type_key = KEYS[data.DataObject]
data.DataProperty.type_key = KEYS[data.DataProperty]
data.DataRestriction.type_key = KEYS[data.DataRestriction]
data.DataStatusType.type_key = KEYS[data.DataStatusType]
data.DataStorage.type_key = KEYS[data.DataStorage]
data.DataStorageDb.type_key = KEYS[data.DataStorageDb]
data.DataStorageFile.type_key = KEYS[data.DataStorageFile]
data.DataStorageIp.type_key = KEYS[data.DataStorageIp]
data.DataTopic.type_key = KEYS[data.DataTopic]
grids.ArcTypeEnum.type_key = KEYS[grids.ArcTypeEnum]
grids.CoordinateList.type_key = KEYS[grids.CoordinateList]
grids.DiscretizationEnum.type_key = KEYS[grids.DiscretizationEnum]
grids.FeatureTypeEnum.type_key = KEYS[grids.FeatureTypeEnum]
grids.GeometryTypeEnum.type_key = KEYS[grids.GeometryTypeEnum]
grids.GridExtent.type_key = KEYS[grids.GridExtent]
grids.GridMosaic.type_key = KEYS[grids.GridMosaic]
grids.GridNodePositionEnum.type_key = KEYS[grids.GridNodePositionEnum]
grids.GridProperty.type_key = KEYS[grids.GridProperty]
grids.GridSpec.type_key = KEYS[grids.GridSpec]
grids.GridTile.type_key = KEYS[grids.GridTile]
grids.GridTileResolutionType.type_key = KEYS[grids.GridTileResolutionType]
grids.GridTypeEnum.type_key = KEYS[grids.GridTypeEnum]
grids.HorizontalCsEnum.type_key = KEYS[grids.HorizontalCsEnum]
grids.RefinementTypeEnum.type_key = KEYS[grids.RefinementTypeEnum]
grids.SimpleGridGeometry.type_key = KEYS[grids.SimpleGridGeometry]
grids.VerticalCoordinateList.type_key = KEYS[grids.VerticalCoordinateList]
grids.VerticalCsEnum.type_key = KEYS[grids.VerticalCsEnum]
misc.DocumentSet.type_key = KEYS[misc.DocumentSet]
quality.CimFeatureType.type_key = KEYS[quality.CimFeatureType]
quality.CimQuality.type_key = KEYS[quality.CimQuality]
quality.CimResultType.type_key = KEYS[quality.CimResultType]
quality.CimScopeCodeType.type_key = KEYS[quality.CimScopeCodeType]
quality.Evaluation.type_key = KEYS[quality.Evaluation]
quality.Measure.type_key = KEYS[quality.Measure]
quality.QualityIssueType.type_key = KEYS[quality.QualityIssueType]
quality.QualitySeverityType.type_key = KEYS[quality.QualitySeverityType]
quality.QualityStatusType.type_key = KEYS[quality.QualityStatusType]
quality.Report.type_key = KEYS[quality.Report]
shared.Calendar.type_key = KEYS[shared.Calendar]
shared.Change.type_key = KEYS[shared.Change]
shared.ChangeProperty.type_key = KEYS[shared.ChangeProperty]
shared.ChangePropertyType.type_key = KEYS[shared.ChangePropertyType]
shared.Citation.type_key = KEYS[shared.Citation]
shared.ClosedDateRange.type_key = KEYS[shared.ClosedDateRange]
shared.Compiler.type_key = KEYS[shared.Compiler]
shared.CompilerType.type_key = KEYS[shared.CompilerType]
shared.Daily360.type_key = KEYS[shared.Daily360]
shared.DataPurpose.type_key = KEYS[shared.DataPurpose]
shared.DataSource.type_key = KEYS[shared.DataSource]
shared.DateRange.type_key = KEYS[shared.DateRange]
shared.DocMetaInfo.type_key = KEYS[shared.DocMetaInfo]
shared.DocReference.type_key = KEYS[shared.DocReference]
shared.InterconnectType.type_key = KEYS[shared.InterconnectType]
shared.License.type_key = KEYS[shared.License]
shared.Machine.type_key = KEYS[shared.Machine]
shared.MachineCompilerUnit.type_key = KEYS[shared.MachineCompilerUnit]
shared.MachineType.type_key = KEYS[shared.MachineType]
shared.MachineVendorType.type_key = KEYS[shared.MachineVendorType]
shared.OpenDateRange.type_key = KEYS[shared.OpenDateRange]
shared.OperatingSystemType.type_key = KEYS[shared.OperatingSystemType]
shared.PerpetualPeriod.type_key = KEYS[shared.PerpetualPeriod]
shared.Platform.type_key = KEYS[shared.Platform]
shared.ProcessorType.type_key = KEYS[shared.ProcessorType]
shared.Property.type_key = KEYS[shared.Property]
shared.RealCalendar.type_key = KEYS[shared.RealCalendar]
shared.Relationship.type_key = KEYS[shared.Relationship]
shared.ResponsibleParty.type_key = KEYS[shared.ResponsibleParty]
shared.Standard.type_key = KEYS[shared.Standard]
shared.StandardName.type_key = KEYS[shared.StandardName]
shared.UnitType.type_key = KEYS[shared.UnitType]
software.Component.type_key = KEYS[software.Component]
software.ComponentLanguage.type_key = KEYS[software.ComponentLanguage]
software.ComponentLanguageProperty.type_key = KEYS[software.ComponentLanguageProperty]
software.ComponentProperty.type_key = KEYS[software.ComponentProperty]
software.ComponentPropertyIntentType.type_key = KEYS[software.ComponentPropertyIntentType]
software.Composition.type_key = KEYS[software.Composition]
software.Connection.type_key = KEYS[software.Connection]
software.ConnectionEndpoint.type_key = KEYS[software.ConnectionEndpoint]
software.ConnectionProperty.type_key = KEYS[software.ConnectionProperty]
software.ConnectionType.type_key = KEYS[software.ConnectionType]
software.Coupling.type_key = KEYS[software.Coupling]
software.CouplingEndpoint.type_key = KEYS[software.CouplingEndpoint]
software.CouplingFrameworkType.type_key = KEYS[software.CouplingFrameworkType]
software.CouplingProperty.type_key = KEYS[software.CouplingProperty]
software.Deployment.type_key = KEYS[software.Deployment]
software.EntryPoint.type_key = KEYS[software.EntryPoint]
software.ModelComponent.type_key = KEYS[software.ModelComponent]
software.ModelComponentType.type_key = KEYS[software.ModelComponentType]
software.Parallelisation.type_key = KEYS[software.Parallelisation]
software.ProcessorComponent.type_key = KEYS[software.ProcessorComponent]
software.Rank.type_key = KEYS[software.Rank]
software.SpatialRegridding.type_key = KEYS[software.SpatialRegridding]
software.SpatialRegriddingDimensionType.type_key = KEYS[software.SpatialRegriddingDimensionType]
software.SpatialRegriddingProperty.type_key = KEYS[software.SpatialRegriddingProperty]
software.SpatialRegriddingStandardMethodType.type_key = KEYS[software.SpatialRegriddingStandardMethodType]
software.SpatialRegriddingUserMethod.type_key = KEYS[software.SpatialRegriddingUserMethod]
software.StatisticalModelComponent.type_key = KEYS[software.StatisticalModelComponent]
software.StatisticalModelComponentType.type_key = KEYS[software.StatisticalModelComponentType]
software.TimeLag.type_key = KEYS[software.TimeLag]
software.TimeMappingType.type_key = KEYS[software.TimeMappingType]
software.TimeTransformation.type_key = KEYS[software.TimeTransformation]
software.Timing.type_key = KEYS[software.Timing]
software.TimingUnits.type_key = KEYS[software.TimingUnits]



# Remove import dross.
del defaultdict
del datetime
del uuid
del activity
del data
del grids
del misc
del quality
del shared
del software

