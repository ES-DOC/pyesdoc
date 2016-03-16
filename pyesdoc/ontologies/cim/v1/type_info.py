
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.type_info.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from collections import defaultdict
import datetime
import uuid


import typeset_for_misc_package as misc
import typeset_for_quality_package as quality
import typeset_for_activity_package as activity
import typeset_for_software_package as software
import typeset_for_data_package as data
import typeset_for_shared_package as shared
import typeset_for_grids_package as grids



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
    misc,
    quality,
    activity,
    software,
    data,
    shared,
    grids,
)

# ------------------------------------------------
# Classes.
# ------------------------------------------------

# Supported classes.
CLASSES = (
    data.DataDistribution,
    software.Timing,
    activity.Simulation,
    quality.Report,
    quality.CimQuality,
    activity.NumericalRequirementOption,
    shared.DateRange,
    shared.DocGenealogy,
    shared.DataSource,
    software.ComponentLanguage,
    activity.LateralBoundaryCondition,
    software.TimeTransformation,
    data.DataRestriction,
    software.CouplingEndpoint,
    shared.Platform,
    activity.NumericalActivity,
    shared.Relationship,
    shared.ResponsibleParty,
    data.DataProperty,
    shared.DocMetaInfo,
    software.ProcessorComponent,
    activity.OutputRequirement,
    data.DataTopic,
    software.Connection,
    grids.SimpleGridGeometry,
    grids.GridExtent,
    activity.NumericalRequirement,
    shared.StandardName,
    activity.PhysicalModification,
    activity.SimulationComposite,
    activity.ExperimentRelationship,
    shared.Compiler,
    shared.MachineCompilerUnit,
    activity.MeasurementCampaign,
    software.Coupling,
    shared.ChangeProperty,
    shared.Property,
    data.DataStorage,
    software.CouplingProperty,
    software.Parallelisation,
    software.Component,
    data.DataContent,
    shared.OpenDateRange,
    shared.DocRelationshipTarget,
    quality.Evaluation,
    activity.ExperimentRelationshipTarget,
    grids.GridProperty,
    grids.GridTileResolutionType,
    software.EntryPoint,
    shared.Citation,
    shared.RealCalendar,
    activity.InitialCondition,
    data.DataHierarchyLevel,
    software.ComponentProperty,
    software.ConnectionEndpoint,
    activity.SpatioTemporalConstraint,
    data.DataStorageIp,
    shared.License,
    activity.NumericalExperiment,
    grids.GridSpec,
    shared.Change,
    activity.Experiment,
    shared.DocRelationship,
    software.SpatialRegriddingUserMethod,
    software.TimeLag,
    software.ConnectionProperty,
    software.SpatialRegridding,
    shared.PerpetualPeriod,
    grids.VerticalCoordinateList,
    activity.Conformance,
    activity.BoundaryCondition,
    misc.DocumentSet,
    shared.Standard,
    shared.ClosedDateRange,
    activity.Ensemble,
    software.StatisticalModelComponent,
    grids.GridMosaic,
    data.DataExtentGeographical,
    grids.CoordinateList,
    activity.SimulationRelationshipTarget,
    activity.SimulationRelationship,
    activity.SimulationRun,
    data.DataStorageDb,
    shared.Machine,
    shared.DocReference,
    data.DataExtentTimeInterval,
    shared.Calendar,
    quality.Measure,
    software.Deployment,
    data.DataExtent,
    software.ModelComponent,
    grids.GridTile,
    activity.Activity,
    data.DataExtentTemporal,
    software.SpatialRegriddingProperty,
    data.DataObject,
    data.DataStorageFile,
    software.Rank,
    software.Composition,
    software.ComponentLanguageProperty,
    activity.EnsembleMember,
    activity.DownscalingSimulation,
    shared.Daily360,
)

# Supported class properties.
CLASS_PROPERTIES = { 
    data.DataDistribution: (
        'access',
        'fee',
        'responsible_party',
        'format',
    ),
    software.Timing: (
        'start',
        'end',
        'rate',
        'is_variable_rate',
        'units',
    ),
    activity.Simulation: (
        'description',
        'control_simulation',
        'supports',
        'rationales',
        'deployments',
        'outputs',
        'simulation_id',
        'conformances',
        'short_name',
        'projects',
        'long_name',
        'authors',
        'spinup_simulation',
        'responsible_parties',
        'calendar',
        'restarts',
        'spinup_date_range',
        'inputs',
        'funding_sources',
    ),
    quality.Report: (
        'date',
        'evaluation',
        'evaluator',
        'measure',
    ),
    quality.CimQuality: (
        'meta',
        'reports',
    ),
    activity.NumericalRequirementOption: (
        'description',
        'sub_options',
        'name',
        'id',
        'relationship',
    ),
    shared.DateRange: (
        'duration',
    ),
    shared.DocGenealogy: (
        'relationships',
    ),
    shared.DataSource: (
        'purpose',
    ),
    software.ComponentLanguage: (
        'name',
        'properties',
    ),
    activity.LateralBoundaryCondition: (
        'id',
        'description',
        'name',
        'source',
        'options',
        'requirement_type',
    ),
    software.TimeTransformation: (
        'description',
        'mapping_type',
    ),
    data.DataRestriction: (
        'license',
        'restriction',
        'scope',
    ),
    software.CouplingEndpoint: (
        'data_source',
        'instance_id',
        'properties',
    ),
    shared.Platform: (
        'units',
        'meta',
        'short_name',
        'description',
        'long_name',
        'contacts',
    ),
    activity.NumericalActivity: (
        'supports',
        'rationales',
        'funding_sources',
        'description',
        'long_name',
        'responsible_parties',
        'projects',
        'short_name',
    ),
    shared.Relationship: (
        'description',
        'direction',
    ),
    shared.ResponsibleParty: (
        'individual_name',
        'abbreviation',
        'organisation_name',
        'role',
        'address',
        'email',
        'url',
    ),
    data.DataProperty: (
        'description',
        'value',
        'name',
    ),
    shared.DocMetaInfo: (
        'type_sort_key',
        'drs_path',
        'sort_key',
        'create_date',
        'update_date',
        'version',
        'project',
        'status',
        'source',
        'language',
        'external_ids',
        'author',
        'source_key',
        'genealogy',
        'type_display_name',
        'id',
        'drs_keys',
        'institute',
        'type',
    ),
    software.ProcessorComponent: (
        'long_name',
        'version',
        'online_resource',
        'language',
        'parent',
        'sub_components',
        'funding_sources',
        'previous_version',
        'release_date',
        'citations',
        'properties',
        'code_access',
        'description',
        'is_embedded',
        'composition',
        'dependencies',
        'grid',
        'responsible_parties',
        'purpose',
        'coupling_framework',
        'deployments',
        'meta',
        'short_name',
        'license',
    ),
    activity.OutputRequirement: (
        'id',
        'description',
        'name',
        'source',
        'options',
        'requirement_type',
    ),
    data.DataTopic: (
        'description',
        'name',
        'unit',
    ),
    software.Connection: (
        'properties',
        'description',
        'time_transformation',
        'priming',
        'spatial_regridding',
        'transformers',
        'target',
        'time_lag',
        'type',
        'sources',
        'time_profile',
    ),
    grids.SimpleGridGeometry: (
        'dim_order',
        'is_mesh',
        'num_dims',
        'ycoords',
        'zcoords',
        'xcoords',
    ),
    grids.GridExtent: (
        'maximum_latitude',
        'maximum_longitude',
        'minimum_latitude',
        'minimum_longitude',
        'units',
    ),
    activity.NumericalRequirement: (
        'description',
        'requirement_type',
        'name',
        'source',
        'options',
        'id',
    ),
    shared.StandardName: (
        'standards',
        'value',
        'is_open',
    ),
    activity.PhysicalModification: (
        'type',
        'is_conformant',
        'description',
        'sources',
        'frequency',
        'requirements',
    ),
    activity.SimulationComposite: (
        'outputs',
        'authors',
        'supports',
        'description',
        'meta',
        'long_name',
        'simulation_id',
        'spinup_simulation',
        'child',
        'restarts',
        'calendar',
        'short_name',
        'date_range',
        'control_simulation',
        'funding_sources',
        'rank',
        'deployments',
        'conformances',
        'rationales',
        'inputs',
        'spinup_date_range',
        'projects',
        'responsible_parties',
    ),
    activity.ExperimentRelationship: (
        'target',
        'direction',
        'description',
        'type',
    ),
    shared.Compiler: (
        'name',
        'type',
        'options',
        'language',
        'environment_variables',
        'version',
    ),
    shared.MachineCompilerUnit: (
        'compilers',
        'machine',
    ),
    activity.MeasurementCampaign: (
        'funding_sources',
        'responsible_parties',
        'rationales',
        'duration',
        'projects',
    ),
    software.Coupling: (
        'properties',
        'is_fully_specified',
        'connections',
        'description',
        'purpose',
        'time_lag',
        'sources',
        'spatial_regriddings',
        'time_transformation',
        'target',
        'time_profile',
        'type',
        'transformers',
        'priming',
    ),
    shared.ChangeProperty: (
        'description',
        'value',
        'name',
        'id',
    ),
    shared.Property: (
        'name',
        'value',
    ),
    data.DataStorage: (
        'location',
        'size',
        'modification_date',
        'format',
    ),
    software.CouplingProperty: (
        'name',
        'value',
    ),
    software.Parallelisation: (
        'processes',
        'ranks',
    ),
    software.Component: (
        'long_name',
        'version',
        'online_resource',
        'responsible_parties',
        'parent',
        'sub_components',
        'previous_version',
        'funding_sources',
        'citations',
        'deployments',
        'properties',
        'code_access',
        'description',
        'is_embedded',
        'composition',
        'dependencies',
        'grid',
        'language',
        'purpose',
        'coupling_framework',
        'release_date',
        'short_name',
        'license',
    ),
    data.DataContent: (
        'aggregation',
        'purpose',
        'frequency',
        'topic',
    ),
    shared.OpenDateRange: (
        'end',
        'duration',
        'start',
    ),
    shared.DocRelationshipTarget: (
        'reference',
    ),
    quality.Evaluation: (
        'specification_hyperlink',
        'did_pass',
        'title',
        'explanation',
        'date',
        'specification',
        'type',
        'description',
        'type_hyperlink',
    ),
    activity.ExperimentRelationshipTarget: (
        'numerical_experiment',
    ),
    grids.GridProperty: (
        'name',
        'value',
    ),
    grids.GridTileResolutionType: (
        'description',
        'properties',
    ),
    software.EntryPoint: (
        'name',
    ),
    shared.Citation: (
        'location',
        'title',
        'organisation',
        'date',
        'alternative_title',
        'date_type',
        'role',
        'collective_title',
        'type',
    ),
    shared.RealCalendar: (
        'description',
        'length',
        'range',
    ),
    activity.InitialCondition: (
        'id',
        'description',
        'name',
        'source',
        'options',
        'requirement_type',
    ),
    data.DataHierarchyLevel: (
        'name',
        'value',
        'is_open',
    ),
    software.ComponentProperty: (
        'grid',
        'intent',
        'is_represented',
        'sub_properties',
        'values',
        'long_name',
        'citations',
        'units',
        'standard_names',
        'description',
        'short_name',
        'purpose',
    ),
    software.ConnectionEndpoint: (
        'instance_id',
        'properties',
        'data_source',
    ),
    activity.SpatioTemporalConstraint: (
        'description',
        'source',
        'id',
        'date_range',
        'name',
        'spatial_resolution',
        'options',
        'requirement_type',
    ),
    data.DataStorageIp: (
        'size',
        'path',
        'format',
        'file_name',
        'modification_date',
        'protocol',
        'location',
        'host',
    ),
    shared.License: (
        'description',
        'name',
        'is_unrestricted',
        'contact',
    ),
    activity.NumericalExperiment: (
        'requires',
        'supports',
        'description',
        'funding_sources',
        'short_name',
        'experiment_id',
        'meta',
        'generates',
        'rationales',
        'long_name',
        'projects',
        'responsible_parties',
        'requirements',
        'measurement_campaigns',
    ),
    grids.GridSpec: (
        'esm_exchange_grids',
        'esm_model_grids',
        'meta',
    ),
    shared.Change: (
        'author',
        'description',
        'details',
        'name',
        'date',
        'type',
    ),
    activity.Experiment: (
        'supports',
        'rationales',
        'measurement_campaigns',
        'funding_sources',
        'projects',
        'requires',
        'responsible_parties',
        'generates',
    ),
    shared.DocRelationship: (
        'type',
        'direction',
        'target',
        'description',
    ),
    software.SpatialRegriddingUserMethod: (
        'file',
        'name',
    ),
    software.TimeLag: (
        'units',
        'value',
    ),
    software.ConnectionProperty: (
        'name',
        'value',
    ),
    software.SpatialRegridding: (
        'standard_method',
        'properties',
        'dimension',
        'user_method',
    ),
    shared.PerpetualPeriod: (
        'description',
        'length',
        'range',
    ),
    grids.VerticalCoordinateList: (
        'properties',
        'uom',
        'type',
        'form',
        'has_constant_offset',
        'length',
    ),
    activity.Conformance: (
        'type',
        'is_conformant',
        'frequency',
        'sources',
        'requirements',
        'description',
    ),
    activity.BoundaryCondition: (
        'id',
        'description',
        'name',
        'source',
        'options',
        'requirement_type',
    ),
    misc.DocumentSet: (
        'ensembles',
        'experiment',
        'grids',
        'data',
        'platform',
        'meta',
        'model',
        'simulation',
    ),
    shared.Standard: (
        'description',
        'name',
        'version',
    ),
    shared.ClosedDateRange: (
        'end',
        'duration',
        'start',
    ),
    activity.Ensemble: (
        'short_name',
        'meta',
        'rationales',
        'supports',
        'members',
        'projects',
        'long_name',
        'types',
        'responsible_parties',
        'description',
        'outputs',
        'funding_sources',
    ),
    software.StatisticalModelComponent: (
        'type',
        'long_name',
        'types',
        'description',
        'language',
        'timing',
        'sub_components',
        'funding_sources',
        'previous_version',
        'release_date',
        'citations',
        'deployments',
        'properties',
        'code_access',
        'parent',
        'is_embedded',
        'composition',
        'dependencies',
        'grid',
        'responsible_parties',
        'version',
        'purpose',
        'coupling_framework',
        'online_resource',
        'meta',
        'short_name',
        'license',
    ),
    grids.GridMosaic: (
        'extent',
        'description',
        'has_congruent_tiles',
        'mosaics',
        'mnemonic',
        'tile_count',
        'is_leaf',
        'mosaic_count',
        'tiles',
        'id',
        'long_name',
        'short_name',
        'type',
        'citations',
    ),
    data.DataExtentGeographical: (
        'east',
        'north',
        'south',
        'west',
    ),
    grids.CoordinateList: (
        'has_constant_offset',
        'length',
        'uom',
    ),
    activity.SimulationRelationshipTarget: (
        'simulation',
        'target',
    ),
    activity.SimulationRelationship: (
        'direction',
        'description',
        'target',
        'type',
    ),
    activity.SimulationRun: (
        'outputs',
        'authors',
        'deployments',
        'simulation_id',
        'control_simulation',
        'description',
        'long_name',
        'meta',
        'spinup_simulation',
        'restarts',
        'short_name',
        'date_range',
        'model',
        'funding_sources',
        'rationales',
        'conformances',
        'supports',
        'calendar',
        'inputs',
        'spinup_date_range',
        'projects',
        'responsible_parties',
    ),
    data.DataStorageDb: (
        'owner',
        'size',
        'table',
        'modification_date',
        'access_string',
        'location',
        'name',
        'format',
    ),
    shared.Machine: (
        'maximum_processors',
        'vendor',
        'interconnect',
        'operating_system',
        'processor_type',
        'cores_per_processor',
        'libraries',
        'system',
        'name',
        'description',
        'type',
        'location',
    ),
    shared.DocReference: (
        'description',
        'type',
        'external_id',
        'url',
        'id',
        'version',
        'changes',
        'name',
    ),
    data.DataExtentTimeInterval: (
        'radix',
        'unit',
        'factor',
    ),
    shared.Calendar: (
        'length',
        'range',
        'description',
    ),
    quality.Measure: (
        'description',
        'identification',
        'name',
    ),
    software.Deployment: (
        'platform',
        'description',
        'deployment_date',
        'parallelisation',
        'executable_arguments',
        'executable_name',
    ),
    data.DataExtent: (
        'geographical',
        'temporal',
    ),
    software.ModelComponent: (
        'long_name',
        'types',
        'version',
        'online_resource',
        'description',
        'language',
        'parent',
        'timing',
        'sub_components',
        'previous_version',
        'activity',
        'release_date',
        'citations',
        'properties',
        'code_access',
        'responsible_parties',
        'is_embedded',
        'composition',
        'dependencies',
        'grid',
        'meta',
        'purpose',
        'coupling_framework',
        'deployments',
        'type',
        'short_name',
        'funding_sources',
        'license',
    ),
    grids.GridTile: (
        'is_terrain_following',
        'short_name',
        'nx',
        'id',
        'coord_file',
        'zcoords',
        'extent',
        'vertical_resolution',
        'long_name',
        'geometry_type',
        'mnemonic',
        'horizontal_crs',
        'horizontal_resolution',
        'discretization_type',
        'grid_north_pole',
        'simple_grid_geom',
        'coordinate_pole',
        'is_regular',
        'ny',
        'area',
        'cell_ref_array',
        'nz',
        'vertical_crs',
        'is_uniform',
        'is_conformal',
        'refinement_scheme',
        'description',
        'cell_array',
    ),
    activity.Activity: (
        'funding_sources',
        'projects',
        'rationales',
        'responsible_parties',
    ),
    data.DataExtentTemporal: (
        'begin',
        'end',
        'time_interval',
    ),
    software.SpatialRegriddingProperty: (
        'name',
        'value',
    ),
    data.DataObject: (
        'geometry_model',
        'storage',
        'hierarchy_level',
        'citations',
        'keyword',
        'content',
        'parent_object',
        'data_status',
        'properties',
        'description',
        'purpose',
        'source_simulation',
        'distribution',
        'purpose',
        'restriction',
        'child_object',
        'extent',
        'acronym',
        'meta',
    ),
    data.DataStorageFile: (
        'size',
        'path',
        'location',
        'file_system',
        'format',
        'file_name',
        'modification_date',
    ),
    software.Rank: (
        'max',
        'min',
        'value',
        'increment',
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
    software.ComponentLanguageProperty: (
        'name',
        'value',
    ),
    activity.EnsembleMember: (
        'short_name',
        'supports',
        'simulation',
        'funding_sources',
        'description',
        'long_name',
        'rationales',
        'ensemble',
        'projects',
        'responsible_parties',
        'ensemble_ids',
    ),
    activity.DownscalingSimulation: (
        'short_name',
        'supports',
        'downscaling_id',
        'funding_sources',
        'description',
        'calendar',
        'downscaled_from',
        'long_name',
        'rationales',
        'downscaling_type',
        'projects',
        'responsible_parties',
        'meta',
        'outputs',
        'inputs',
    ),
    shared.Daily360: (
        'description',
        'length',
        'range',
    ),
}

# Supported class own properties.
CLASS_OWN_PROPERTIES = { 
    data.DataDistribution: (
        'access',
        'format',
        'responsible_party',
        'fee',
    ),
    software.Timing: (
        'rate',
        'units',
        'start',
        'end',
        'is_variable_rate',
    ),
    activity.Simulation: (
        'control_simulation',
        'outputs',
        'deployments',
        'conformances',
        'simulation_id',
        'authors',
        'spinup_simulation',
        'restarts',
        'calendar',
        'inputs',
        'spinup_date_range',
    ),
    quality.Report: (
        'date',
        'measure',
        'evaluator',
        'evaluation',
    ),
    quality.CimQuality: (
        'meta',
        'reports',
    ),
    activity.NumericalRequirementOption: (
        'description',
        'relationship',
        'name',
        'sub_options',
        'id',
    ),
    shared.DateRange: (
        'duration',
    ),
    shared.DocGenealogy: (
        'relationships',
    ),
    shared.DataSource: (
        'purpose',
    ),
    software.ComponentLanguage: (
        'name',
        'properties',
    ),
    activity.LateralBoundaryCondition: (
    ),
    software.TimeTransformation: (
        'description',
        'mapping_type',
    ),
    data.DataRestriction: (
        'license',
        'scope',
        'restriction',
    ),
    software.CouplingEndpoint: (
        'data_source',
        'properties',
        'instance_id',
    ),
    shared.Platform: (
        'description',
        'long_name',
        'contacts',
        'short_name',
        'units',
        'meta',
    ),
    activity.NumericalActivity: (
        'short_name',
        'description',
        'supports',
        'long_name',
    ),
    shared.Relationship: (
        'description',
        'direction',
    ),
    shared.ResponsibleParty: (
        'abbreviation',
        'organisation_name',
        'role',
        'url',
        'email',
        'address',
        'individual_name',
    ),
    data.DataProperty: (
        'description',
    ),
    shared.DocMetaInfo: (
        'source',
        'type_sort_key',
        'external_ids',
        'id',
        'language',
        'source_key',
        'type',
        'genealogy',
        'version',
        'create_date',
        'sort_key',
        'update_date',
        'drs_path',
        'institute',
        'project',
        'status',
        'type_display_name',
        'drs_keys',
        'author',
    ),
    software.ProcessorComponent: (
        'meta',
    ),
    activity.OutputRequirement: (
    ),
    data.DataTopic: (
        'description',
        'unit',
        'name',
    ),
    software.Connection: (
        'properties',
        'time_profile',
        'time_transformation',
        'priming',
        'spatial_regridding',
        'transformers',
        'target',
        'time_lag',
        'type',
        'sources',
        'description',
    ),
    grids.SimpleGridGeometry: (
        'dim_order',
        'ycoords',
        'zcoords',
        'num_dims',
        'is_mesh',
        'xcoords',
    ),
    grids.GridExtent: (
        'maximum_latitude',
        'units',
        'minimum_latitude',
        'minimum_longitude',
        'maximum_longitude',
    ),
    activity.NumericalRequirement: (
        'requirement_type',
        'source',
        'id',
        'name',
        'options',
        'description',
    ),
    shared.StandardName: (
        'value',
        'is_open',
        'standards',
    ),
    activity.PhysicalModification: (
    ),
    activity.SimulationComposite: (
        'rank',
        'child',
        'meta',
        'date_range',
    ),
    activity.ExperimentRelationship: (
        'target',
        'type',
    ),
    shared.Compiler: (
        'name',
        'type',
        'options',
        'environment_variables',
        'language',
        'version',
    ),
    shared.MachineCompilerUnit: (
        'compilers',
        'machine',
    ),
    activity.MeasurementCampaign: (
        'duration',
    ),
    software.Coupling: (
        'transformers',
        'is_fully_specified',
        'sources',
        'spatial_regriddings',
        'time_lag',
        'purpose',
        'description',
        'time_transformation',
        'priming',
        'target',
        'time_profile',
        'type',
        'connections',
        'properties',
    ),
    shared.ChangeProperty: (
        'description',
        'id',
    ),
    shared.Property: (
        'name',
        'value',
    ),
    data.DataStorage: (
        'size',
        'format',
        'modification_date',
        'location',
    ),
    software.CouplingProperty: (
    ),
    software.Parallelisation: (
        'processes',
        'ranks',
    ),
    software.Component: (
        'long_name',
        'version',
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
        'dependencies',
        'deployments',
        'description',
        'funding_sources',
        'grid',
        'is_embedded',
        'language',
        'license',
    ),
    data.DataContent: (
        'topic',
        'aggregation',
        'frequency',
    ),
    shared.OpenDateRange: (
        'end',
        'start',
    ),
    shared.DocRelationshipTarget: (
        'reference',
    ),
    quality.Evaluation: (
        'did_pass',
        'specification',
        'explanation',
        'title',
        'date',
        'type',
        'description',
        'specification_hyperlink',
        'type_hyperlink',
    ),
    activity.ExperimentRelationshipTarget: (
        'numerical_experiment',
    ),
    grids.GridProperty: (
    ),
    grids.GridTileResolutionType: (
        'description',
        'properties',
    ),
    software.EntryPoint: (
        'name',
    ),
    shared.Citation: (
        'location',
        'title',
        'date',
        'collective_title',
        'date_type',
        'type',
        'role',
        'organisation',
        'alternative_title',
    ),
    shared.RealCalendar: (
    ),
    activity.InitialCondition: (
    ),
    data.DataHierarchyLevel: (
        'value',
        'is_open',
        'name',
    ),
    software.ComponentProperty: (
        'grid',
        'values',
        'is_represented',
        'sub_properties',
        'intent',
        'standard_names',
        'citations',
        'units',
        'description',
        'long_name',
        'short_name',
    ),
    software.ConnectionEndpoint: (
        'properties',
        'data_source',
        'instance_id',
    ),
    activity.SpatioTemporalConstraint: (
        'date_range',
        'spatial_resolution',
    ),
    data.DataStorageIp: (
        'protocol',
        'path',
        'file_name',
        'host',
    ),
    shared.License: (
        'name',
        'contact',
        'is_unrestricted',
        'description',
    ),
    activity.NumericalExperiment: (
        'description',
        'short_name',
        'experiment_id',
        'requirements',
        'long_name',
        'meta',
    ),
    grids.GridSpec: (
        'esm_exchange_grids',
        'meta',
        'esm_model_grids',
    ),
    shared.Change: (
        'author',
        'name',
        'type',
        'description',
        'date',
        'details',
    ),
    activity.Experiment: (
        'generates',
        'supports',
        'measurement_campaigns',
        'requires',
    ),
    shared.DocRelationship: (
        'type',
        'target',
    ),
    software.SpatialRegriddingUserMethod: (
        'file',
        'name',
    ),
    software.TimeLag: (
        'units',
        'value',
    ),
    software.ConnectionProperty: (
    ),
    software.SpatialRegridding: (
        'standard_method',
        'user_method',
        'dimension',
        'properties',
    ),
    shared.PerpetualPeriod: (
    ),
    grids.VerticalCoordinateList: (
        'type',
        'form',
        'properties',
    ),
    activity.Conformance: (
        'type',
        'is_conformant',
        'requirements',
        'description',
        'sources',
        'frequency',
    ),
    activity.BoundaryCondition: (
    ),
    misc.DocumentSet: (
        'ensembles',
        'experiment',
        'platform',
        'data',
        'grids',
        'model',
        'meta',
        'simulation',
    ),
    shared.Standard: (
        'description',
        'version',
        'name',
    ),
    shared.ClosedDateRange: (
        'end',
        'start',
    ),
    activity.Ensemble: (
        'members',
        'outputs',
        'types',
        'meta',
    ),
    software.StatisticalModelComponent: (
        'type',
        'meta',
        'types',
        'timing',
    ),
    grids.GridMosaic: (
        'extent',
        'mosaic_count',
        'mnemonic',
        'tile_count',
        'type',
        'has_congruent_tiles',
        'description',
        'citations',
        'mosaics',
        'long_name',
        'short_name',
        'tiles',
        'is_leaf',
        'id',
    ),
    data.DataExtentGeographical: (
        'south',
        'west',
        'east',
        'north',
    ),
    grids.CoordinateList: (
        'has_constant_offset',
        'uom',
        'length',
    ),
    activity.SimulationRelationshipTarget: (
        'simulation',
        'target',
    ),
    activity.SimulationRelationship: (
        'target',
        'type',
    ),
    activity.SimulationRun: (
        'date_range',
        'model',
        'meta',
    ),
    data.DataStorageDb: (
        'table',
        'access_string',
        'owner',
        'name',
    ),
    shared.Machine: (
        'maximum_processors',
        'operating_system',
        'vendor',
        'libraries',
        'name',
        'processor_type',
        'interconnect',
        'cores_per_processor',
        'system',
        'description',
        'location',
        'type',
    ),
    shared.DocReference: (
        'description',
        'type',
        'external_id',
        'url',
        'id',
        'version',
        'name',
        'changes',
    ),
    data.DataExtentTimeInterval: (
        'unit',
        'factor',
        'radix',
    ),
    shared.Calendar: (
        'range',
        'description',
        'length',
    ),
    quality.Measure: (
        'description',
        'name',
        'identification',
    ),
    software.Deployment: (
        'platform',
        'description',
        'deployment_date',
        'executable_arguments',
        'executable_name',
        'parallelisation',
    ),
    data.DataExtent: (
        'geographical',
        'temporal',
    ),
    software.ModelComponent: (
        'activity',
        'types',
        'type',
        'timing',
        'meta',
    ),
    grids.GridTile: (
        'is_terrain_following',
        'coord_file',
        'long_name',
        'horizontal_crs',
        'mnemonic',
        'short_name',
        'grid_north_pole',
        'ny',
        'nz',
        'vertical_crs',
        'is_uniform',
        'refinement_scheme',
        'description',
        'discretization_type',
        'nx',
        'extent',
        'vertical_resolution',
        'geometry_type',
        'zcoords',
        'horizontal_resolution',
        'coordinate_pole',
        'id',
        'area',
        'is_conformal',
        'cell_array',
        'simple_grid_geom',
        'is_regular',
        'cell_ref_array',
    ),
    activity.Activity: (
        'funding_sources',
        'responsible_parties',
        'rationales',
        'projects',
    ),
    data.DataExtentTemporal: (
        'begin',
        'time_interval',
        'end',
    ),
    software.SpatialRegriddingProperty: (
    ),
    data.DataObject: (
        'data_status',
        'restriction',
        'extent',
        'hierarchy_level',
        'distribution',
        'description',
        'source_simulation',
        'purpose',
        'parent_object',
        'storage',
        'citations',
        'keyword',
        'geometry_model',
        'child_object',
        'content',
        'properties',
        'acronym',
        'meta',
    ),
    data.DataStorageFile: (
        'file_system',
        'file_name',
        'path',
    ),
    software.Rank: (
        'min',
        'increment',
        'value',
        'max',
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
    software.ComponentLanguageProperty: (
    ),
    activity.EnsembleMember: (
        'simulation',
        'ensemble',
        'ensemble_ids',
    ),
    activity.DownscalingSimulation: (
        'meta',
        'outputs',
        'calendar',
        'downscaled_from',
        'downscaling_type',
        'downscaling_id',
        'inputs',
    ),
    shared.Daily360: (
    ),
}

# Total class properties.
TOTAL_CLASS_PROPERTIES = sum(len(i) for i in CLASS_OWN_PROPERTIES.values())

# ------------------------------------------------
# Enum.
# ------------------------------------------------

# Supported enums.
ENUMS = (
    grids.RefinementTypeEnum,
    activity.SimulationRelationshipType,
    grids.DiscretizationEnum,
    activity.ConformanceType,
    quality.CimResultType,
    data.DataHierarchyType,
    grids.ArcTypeEnum,
    data.DataStatusType,
    quality.CimScopeCodeType,
    shared.DocRelationshipType,
    software.TimingUnits,
    software.StatisticalModelComponentType,
    software.TimeMappingType,
    shared.CompilerType,
    activity.EnsembleType,
    shared.DocRelationshipDirectionType,
    activity.ExperimentRelationshipType,
    software.SpatialRegriddingStandardMethodType,
    shared.MachineType,
    grids.GridTypeEnum,
    software.SpatialRegriddingDimensionType,
    shared.InterconnectType,
    quality.QualitySeverityType,
    quality.QualityIssueType,
    shared.DocType,
    shared.OperatingSystemType,
    grids.GeometryTypeEnum,
    shared.ChangePropertyType,
    shared.MachineVendorType,
    software.ComponentPropertyIntentType,
    activity.DownscalingType,
    activity.FrequencyType,
    software.ConnectionType,
    software.CouplingFrameworkType,
    shared.DataPurpose,
    activity.ResolutionType,
    shared.ProcessorType,
    activity.SimulationType,
    activity.ProjectType,
    grids.VerticalCsEnum,
    shared.DocStatusType,
    quality.CimFeatureType,
    grids.HorizontalCsEnum,
    grids.FeatureTypeEnum,
    grids.GridNodePositionEnum,
    software.ModelComponentType,
    quality.QualityStatusType,
    shared.UnitType,
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
    misc.DocumentSet,
    quality.CimQuality,
    activity.SimulationComposite,
    activity.Ensemble,
    activity.NumericalExperiment,
    activity.SimulationRun,
    activity.DownscalingSimulation,
    software.ModelComponent,
    software.ProcessorComponent,
    software.StatisticalModelComponent,
    data.DataObject,
    shared.Platform,
    grids.GridSpec,
)

# Base classes.
BASE_CLASSES = defaultdict(tuple)
BASE_CLASSES[activity.Simulation] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[activity.LateralBoundaryCondition] = (activity.NumericalRequirement, )
BASE_CLASSES[activity.NumericalActivity] = (activity.Activity, )
BASE_CLASSES[data.DataProperty] = (shared.Property, )
BASE_CLASSES[software.ProcessorComponent] = (software.Component, shared.DataSource, )
BASE_CLASSES[activity.OutputRequirement] = (activity.NumericalRequirement, )
BASE_CLASSES[activity.PhysicalModification] = (activity.Conformance, )
BASE_CLASSES[activity.SimulationComposite] = (activity.Simulation, activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[activity.ExperimentRelationship] = (shared.Relationship, )
BASE_CLASSES[activity.MeasurementCampaign] = (activity.Activity, )
BASE_CLASSES[shared.ChangeProperty] = (shared.Property, )
BASE_CLASSES[software.CouplingProperty] = (shared.Property, )
BASE_CLASSES[software.Component] = (shared.DataSource, )
BASE_CLASSES[data.DataContent] = (shared.DataSource, )
BASE_CLASSES[shared.OpenDateRange] = (shared.DateRange, )
BASE_CLASSES[grids.GridProperty] = (shared.Property, )
BASE_CLASSES[shared.RealCalendar] = (shared.Calendar, )
BASE_CLASSES[activity.InitialCondition] = (activity.NumericalRequirement, )
BASE_CLASSES[software.ComponentProperty] = (shared.DataSource, )
BASE_CLASSES[activity.SpatioTemporalConstraint] = (activity.NumericalRequirement, )
BASE_CLASSES[data.DataStorageIp] = (data.DataStorage, )
BASE_CLASSES[activity.NumericalExperiment] = (activity.Experiment, activity.Activity, )
BASE_CLASSES[activity.Experiment] = (activity.Activity, )
BASE_CLASSES[shared.DocRelationship] = (shared.Relationship, )
BASE_CLASSES[software.ConnectionProperty] = (shared.Property, )
BASE_CLASSES[shared.PerpetualPeriod] = (shared.Calendar, )
BASE_CLASSES[grids.VerticalCoordinateList] = (grids.CoordinateList, )
BASE_CLASSES[activity.BoundaryCondition] = (activity.NumericalRequirement, )
BASE_CLASSES[shared.ClosedDateRange] = (shared.DateRange, )
BASE_CLASSES[activity.Ensemble] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[software.StatisticalModelComponent] = (software.Component, shared.DataSource, )
BASE_CLASSES[activity.SimulationRelationship] = (shared.Relationship, )
BASE_CLASSES[activity.SimulationRun] = (activity.Simulation, activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[data.DataStorageDb] = (data.DataStorage, )
BASE_CLASSES[software.ModelComponent] = (software.Component, shared.DataSource, )
BASE_CLASSES[software.SpatialRegriddingProperty] = (shared.Property, )
BASE_CLASSES[data.DataObject] = (shared.DataSource, )
BASE_CLASSES[data.DataStorageFile] = (data.DataStorage, )
BASE_CLASSES[software.ComponentLanguageProperty] = (shared.Property, )
BASE_CLASSES[activity.EnsembleMember] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[activity.DownscalingSimulation] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[shared.Daily360] = (shared.Calendar, )

# Classes with base classes.
BASE_CLASSED = tuple(BASE_CLASSES.keys())

# Sub classes.
SUB_CLASSES = defaultdict(tuple)
SUB_CLASSES[activity.NumericalRequirement] = (
    activity.OutputRequirement,
    activity.BoundaryCondition,
    activity.InitialCondition,
    activity.LateralBoundaryCondition,
    activity.SpatioTemporalConstraint,
    )
SUB_CLASSES[activity.Conformance] = (
    activity.PhysicalModification,
    )
SUB_CLASSES[grids.CoordinateList] = (
    grids.VerticalCoordinateList,
    )
SUB_CLASSES[activity.Experiment] = (
    activity.NumericalExperiment,
    )
SUB_CLASSES[activity.NumericalActivity] = (
    activity.Ensemble,
    activity.Simulation,
    activity.EnsembleMember,
    activity.DownscalingSimulation,
    activity.SimulationComposite,
    activity.SimulationRun,
    )
SUB_CLASSES[shared.Relationship] = (
    activity.SimulationRelationship,
    activity.ExperimentRelationship,
    shared.DocRelationship,
    )
SUB_CLASSES[activity.Simulation] = (
    activity.SimulationComposite,
    activity.SimulationRun,
    )
SUB_CLASSES[data.DataStorage] = (
    data.DataStorageIp,
    data.DataStorageDb,
    data.DataStorageFile,
    )
SUB_CLASSES[software.Component] = (
    software.ModelComponent,
    software.ProcessorComponent,
    software.StatisticalModelComponent,
    )
SUB_CLASSES[shared.DateRange] = (
    shared.ClosedDateRange,
    shared.OpenDateRange,
    )
SUB_CLASSES[shared.DataSource] = (
    data.DataContent,
    data.DataObject,
    software.ComponentProperty,
    software.Component,
    software.ModelComponent,
    software.ProcessorComponent,
    software.StatisticalModelComponent,
    )
SUB_CLASSES[shared.Calendar] = (
    shared.PerpetualPeriod,
    shared.RealCalendar,
    shared.Daily360,
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
SUB_CLASSES[shared.Property] = (
    data.DataProperty,
    software.ConnectionProperty,
    software.ComponentLanguageProperty,
    software.SpatialRegriddingProperty,
    software.CouplingProperty,
    grids.GridProperty,
    shared.ChangeProperty,
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
    activity.Simulation: (

        ('inputs', 'type', software.Coupling),
        ('simulation_id', 'type', unicode),
        ('funding_sources', 'type', unicode),
        ('rationales', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('control_simulation', 'type', activity.Simulation),
        ('spinup_simulation', 'type', activity.Simulation),
        ('authors', 'type', unicode),
        ('spinup_date_range', 'type', shared.ClosedDateRange),
        ('responsible_parties', 'type', shared.ResponsibleParty),
        ('deployments', 'type', software.Deployment),
        ('restarts', 'type', data.DataObject),
        ('long_name', 'type', unicode),
        ('outputs', 'type', data.DataObject),
        ('conformances', 'type', activity.Conformance),
        ('supports', 'type', activity.Experiment),
        ('calendar', 'type', shared.Calendar),
        ('projects', 'type', unicode),

        ('inputs', 'cardinality', "0.N"),
        ('simulation_id', 'cardinality', "0.1"),
        ('funding_sources', 'cardinality', "0.N"),
        ('rationales', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "1.1"),
        ('control_simulation', 'cardinality', "0.1"),
        ('spinup_simulation', 'cardinality', "0.1"),
        ('authors', 'cardinality', "0.1"),
        ('spinup_date_range', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('deployments', 'cardinality', "0.N"),
        ('restarts', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('outputs', 'cardinality', "0.N"),
        ('conformances', 'cardinality', "0.N"),
        ('supports', 'cardinality', "0.N"),
        ('calendar', 'cardinality', "1.1"),
        ('projects', 'cardinality', "0.N"),

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
    quality.CimQuality: (

        ('meta', 'type', shared.DocMetaInfo),
        ('reports', 'type', quality.Report),

        ('meta', 'cardinality', "1.1"),
        ('reports', 'cardinality', "0.N"),

    ),
    activity.NumericalRequirementOption: (

        ('id', 'type', unicode),
        ('sub_options', 'type', activity.NumericalRequirementOption),
        ('description', 'type', unicode),
        ('relationship', 'type', unicode),
        ('name', 'type', unicode),

        ('id', 'cardinality', "0.1"),
        ('sub_options', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('relationship', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    shared.DateRange: (

        ('duration', 'type', unicode),

        ('duration', 'cardinality', "0.1"),

    ),
    shared.DocGenealogy: (

        ('relationships', 'type', shared.DocRelationship),

        ('relationships', 'cardinality', "0.N"),

    ),
    shared.DataSource: (

        ('purpose', 'type', unicode),

        ('purpose', 'cardinality', "0.1"),

    ),
    software.ComponentLanguage: (

        ('name', 'type', unicode),
        ('properties', 'type', software.ComponentLanguageProperty),

        ('name', 'cardinality', "1.1"),
        ('properties', 'cardinality', "0.N"),

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
    software.TimeTransformation: (

        ('description', 'type', unicode),
        ('mapping_type', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('mapping_type', 'cardinality', "1.1"),

    ),
    data.DataRestriction: (

        ('restriction', 'type', unicode),
        ('license', 'type', shared.License),
        ('scope', 'type', unicode),

        ('restriction', 'cardinality', "0.1"),
        ('license', 'cardinality', "0.1"),
        ('scope', 'cardinality', "0.1"),

    ),
    software.CouplingEndpoint: (

        ('instance_id', 'type', unicode),
        ('data_source', 'type', shared.DataSource),
        ('properties', 'type', software.CouplingProperty),

        ('instance_id', 'cardinality', "0.1"),
        ('data_source', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),

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
    shared.Relationship: (

        ('direction', 'type', unicode),
        ('description', 'type', unicode),

        ('direction', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),

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
    data.DataProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),
        ('description', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    shared.DocMetaInfo: (

        ('status', 'type', unicode),
        ('drs_path', 'type', unicode),
        ('drs_keys', 'type', unicode),
        ('create_date', 'type', datetime.datetime),
        ('genealogy', 'type', shared.DocGenealogy),
        ('language', 'type', unicode),
        ('update_date', 'type', datetime.datetime),
        ('sort_key', 'type', unicode),
        ('author', 'type', shared.ResponsibleParty),
        ('source_key', 'type', unicode),
        ('project', 'type', unicode),
        ('source', 'type', unicode),
        ('version', 'type', int),
        ('type_sort_key', 'type', unicode),
        ('external_ids', 'type', shared.StandardName),
        ('type', 'type', unicode),
        ('id', 'type', uuid.UUID),
        ('type_display_name', 'type', unicode),
        ('institute', 'type', unicode),

        ('status', 'cardinality', "0.1"),
        ('drs_path', 'cardinality', "0.1"),
        ('drs_keys', 'cardinality', "0.N"),
        ('create_date', 'cardinality', "1.1"),
        ('genealogy', 'cardinality', "0.1"),
        ('language', 'cardinality', "1.1"),
        ('update_date', 'cardinality', "1.1"),
        ('sort_key', 'cardinality', "0.1"),
        ('author', 'cardinality', "0.1"),
        ('source_key', 'cardinality', "0.1"),
        ('project', 'cardinality', "1.1"),
        ('source', 'cardinality', "1.1"),
        ('version', 'cardinality', "1.1"),
        ('type_sort_key', 'cardinality', "0.1"),
        ('external_ids', 'cardinality', "0.N"),
        ('type', 'cardinality', "1.1"),
        ('id', 'cardinality', "1.1"),
        ('type_display_name', 'cardinality', "0.1"),
        ('institute', 'cardinality', "0.1"),

        ('source', 'constant', "scripts"),
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
    data.DataTopic: (

        ('description', 'type', unicode),
        ('unit', 'type', unicode),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('unit', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),

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
    shared.StandardName: (

        ('is_open', 'type', bool),
        ('value', 'type', unicode),
        ('standards', 'type', shared.Standard),

        ('is_open', 'cardinality', "1.1"),
        ('value', 'cardinality', "1.1"),
        ('standards', 'cardinality', "0.N"),

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
    activity.SimulationComposite: (

        ('funding_sources', 'type', unicode),
        ('authors', 'type', unicode),
        ('rank', 'type', int),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('conformances', 'type', activity.Conformance),
        ('calendar', 'type', shared.Calendar),
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
        ('child', 'type', activity.Simulation),
        ('projects', 'type', unicode),
        ('spinup_simulation', 'type', activity.Simulation),

        ('funding_sources', 'cardinality', "0.N"),
        ('authors', 'cardinality', "0.1"),
        ('rank', 'cardinality', "1.1"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('conformances', 'cardinality', "0.N"),
        ('calendar', 'cardinality', "1.1"),
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
        ('child', 'cardinality', "0.N"),
        ('projects', 'cardinality', "0.N"),
        ('spinup_simulation', 'cardinality', "0.1"),

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
    shared.MachineCompilerUnit: (

        ('machine', 'type', shared.Machine),
        ('compilers', 'type', shared.Compiler),

        ('machine', 'cardinality', "1.1"),
        ('compilers', 'cardinality', "0.N"),

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
    software.Coupling: (

        ('transformers', 'type', software.ProcessorComponent),
        ('description', 'type', unicode),
        ('type', 'type', unicode),
        ('time_transformation', 'type', software.TimeTransformation),
        ('connections', 'type', software.Connection),
        ('sources', 'type', software.CouplingEndpoint),
        ('spatial_regriddings', 'type', software.SpatialRegridding),
        ('purpose', 'type', unicode),
        ('time_profile', 'type', software.Timing),
        ('priming', 'type', shared.DataSource),
        ('is_fully_specified', 'type', bool),
        ('properties', 'type', software.CouplingProperty),
        ('time_lag', 'type', software.TimeLag),
        ('target', 'type', software.CouplingEndpoint),

        ('transformers', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('time_transformation', 'cardinality', "0.1"),
        ('connections', 'cardinality', "0.N"),
        ('sources', 'cardinality', "1.N"),
        ('spatial_regriddings', 'cardinality', "0.N"),
        ('purpose', 'cardinality', "1.1"),
        ('time_profile', 'cardinality', "0.1"),
        ('priming', 'cardinality', "0.1"),
        ('is_fully_specified', 'cardinality', "1.1"),
        ('properties', 'cardinality', "0.N"),
        ('time_lag', 'cardinality', "0.1"),
        ('target', 'cardinality', "1.1"),

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
    shared.Property: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    data.DataStorage: (

        ('format', 'type', unicode),
        ('location', 'type', unicode),
        ('modification_date', 'type', datetime.datetime),
        ('size', 'type', int),

        ('format', 'cardinality', "0.1"),
        ('location', 'cardinality', "0.1"),
        ('modification_date', 'cardinality', "0.1"),
        ('size', 'cardinality', "0.1"),

    ),
    software.CouplingProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    software.Parallelisation: (

        ('ranks', 'type', software.Rank),
        ('processes', 'type', int),

        ('ranks', 'cardinality', "0.N"),
        ('processes', 'cardinality', "1.1"),

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
        ('license', 'type', shared.License),
        ('language', 'type', software.ComponentLanguage),
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
        ('license', 'cardinality', "0.1"),
        ('language', 'cardinality', "0.1"),
        ('release_date', 'cardinality', "0.1"),
        ('code_access', 'cardinality', "0.1"),

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
    shared.OpenDateRange: (

        ('duration', 'type', unicode),
        ('start', 'type', datetime.datetime),
        ('end', 'type', datetime.datetime),

        ('duration', 'cardinality', "0.1"),
        ('start', 'cardinality', "0.1"),
        ('end', 'cardinality', "0.1"),

    ),
    shared.DocRelationshipTarget: (

        ('reference', 'type', shared.DocReference),

        ('reference', 'cardinality', "0.1"),

    ),
    quality.Evaluation: (

        ('description', 'type', unicode),
        ('title', 'type', unicode),
        ('explanation', 'type', unicode),
        ('specification_hyperlink', 'type', unicode),
        ('did_pass', 'type', bool),
        ('type_hyperlink', 'type', unicode),
        ('date', 'type', datetime.datetime),
        ('type', 'type', unicode),
        ('specification', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('title', 'cardinality', "0.1"),
        ('explanation', 'cardinality', "0.1"),
        ('specification_hyperlink', 'cardinality', "0.1"),
        ('did_pass', 'cardinality', "0.1"),
        ('type_hyperlink', 'cardinality', "0.1"),
        ('date', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('specification', 'cardinality', "0.1"),

    ),
    activity.ExperimentRelationshipTarget: (

        ('numerical_experiment', 'type', activity.NumericalExperiment),

        ('numerical_experiment', 'cardinality', "0.1"),

    ),
    grids.GridProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    grids.GridTileResolutionType: (

        ('description', 'type', unicode),
        ('properties', 'type', grids.GridProperty),

        ('description', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),

    ),
    software.EntryPoint: (

        ('name', 'type', unicode),

        ('name', 'cardinality', "0.1"),

    ),
    shared.Citation: (

        ('collective_title', 'type', unicode),
        ('alternative_title', 'type', unicode),
        ('organisation', 'type', unicode),
        ('title', 'type', unicode),
        ('role', 'type', unicode),
        ('location', 'type', unicode),
        ('date', 'type', datetime.datetime),
        ('type', 'type', unicode),
        ('date_type', 'type', unicode),

        ('collective_title', 'cardinality', "0.1"),
        ('alternative_title', 'cardinality', "0.1"),
        ('organisation', 'cardinality', "0.1"),
        ('title', 'cardinality', "0.1"),
        ('role', 'cardinality', "0.1"),
        ('location', 'cardinality', "0.1"),
        ('date', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('date_type', 'cardinality', "0.1"),

    ),
    shared.RealCalendar: (

        ('length', 'type', int),
        ('range', 'type', shared.DateRange),
        ('description', 'type', unicode),

        ('length', 'cardinality', "0.1"),
        ('range', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

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
    data.DataHierarchyLevel: (

        ('is_open', 'type', bool),
        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('is_open', 'cardinality', "0.1"),
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
    software.ConnectionEndpoint: (

        ('instance_id', 'type', unicode),
        ('data_source', 'type', shared.DataSource),
        ('properties', 'type', software.ConnectionProperty),

        ('instance_id', 'cardinality', "0.1"),
        ('data_source', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),

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
    grids.GridSpec: (

        ('esm_exchange_grids', 'type', grids.GridMosaic),
        ('meta', 'type', shared.DocMetaInfo),
        ('esm_model_grids', 'type', grids.GridMosaic),

        ('esm_exchange_grids', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('esm_model_grids', 'cardinality', "0.N"),

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
    software.SpatialRegriddingUserMethod: (

        ('name', 'type', unicode),
        ('file', 'type', data.DataObject),

        ('name', 'cardinality', "1.1"),
        ('file', 'cardinality', "0.1"),

    ),
    software.TimeLag: (

        ('units', 'type', unicode),
        ('value', 'type', int),

        ('units', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    software.ConnectionProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

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
    shared.PerpetualPeriod: (

        ('length', 'type', int),
        ('range', 'type', shared.DateRange),
        ('description', 'type', unicode),

        ('length', 'cardinality', "0.1"),
        ('range', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

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
    shared.Standard: (

        ('version', 'type', unicode),
        ('description', 'type', unicode),
        ('name', 'type', unicode),

        ('version', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    shared.ClosedDateRange: (

        ('duration', 'type', unicode),
        ('start', 'type', datetime.datetime),
        ('end', 'type', datetime.datetime),

        ('duration', 'cardinality', "0.1"),
        ('start', 'cardinality', "1.1"),
        ('end', 'cardinality', "0.1"),

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
    grids.GridMosaic: (

        ('mnemonic', 'type', unicode),
        ('is_leaf', 'type', bool),
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

        ('mnemonic', 'cardinality', "0.1"),
        ('is_leaf', 'cardinality', "1.1"),
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
    grids.CoordinateList: (

        ('has_constant_offset', 'type', bool),
        ('length', 'type', int),
        ('uom', 'type', unicode),

        ('has_constant_offset', 'cardinality', "0.1"),
        ('length', 'cardinality', "0.1"),
        ('uom', 'cardinality', "0.1"),

    ),
    activity.SimulationRelationshipTarget: (

        ('target', 'type', unicode),
        ('simulation', 'type', shared.DocReference),

        ('target', 'cardinality', "0.1"),
        ('simulation', 'cardinality', "0.1"),

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
    activity.SimulationRun: (

        ('funding_sources', 'type', unicode),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('conformances', 'type', activity.Conformance),
        ('calendar', 'type', shared.Calendar),
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
        ('conformances', 'cardinality', "0.N"),
        ('calendar', 'cardinality', "1.1"),
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
    shared.Machine: (

        ('operating_system', 'type', unicode),
        ('vendor', 'type', unicode),
        ('processor_type', 'type', unicode),
        ('cores_per_processor', 'type', int),
        ('type', 'type', unicode),
        ('description', 'type', unicode),
        ('system', 'type', unicode),
        ('libraries', 'type', unicode),
        ('location', 'type', unicode),
        ('interconnect', 'type', unicode),
        ('maximum_processors', 'type', int),
        ('name', 'type', unicode),

        ('operating_system', 'cardinality', "0.1"),
        ('vendor', 'cardinality', "0.1"),
        ('processor_type', 'cardinality', "0.1"),
        ('cores_per_processor', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('system', 'cardinality', "0.1"),
        ('libraries', 'cardinality', "0.N"),
        ('location', 'cardinality', "0.1"),
        ('interconnect', 'cardinality', "0.1"),
        ('maximum_processors', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    shared.DocReference: (

        ('description', 'type', unicode),
        ('url', 'type', unicode),
        ('type', 'type', unicode),
        ('version', 'type', int),
        ('changes', 'type', shared.Change),
        ('external_id', 'type', unicode),
        ('id', 'type', uuid.UUID),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('url', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('version', 'cardinality', "0.1"),
        ('changes', 'cardinality', "0.N"),
        ('external_id', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),

    ),
    data.DataExtentTimeInterval: (

        ('radix', 'type', int),
        ('unit', 'type', unicode),
        ('factor', 'type', int),

        ('radix', 'cardinality', "0.1"),
        ('unit', 'cardinality', "0.1"),
        ('factor', 'cardinality', "0.1"),

    ),
    shared.Calendar: (

        ('length', 'type', int),
        ('range', 'type', shared.DateRange),
        ('description', 'type', unicode),

        ('length', 'cardinality', "0.1"),
        ('range', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    quality.Measure: (

        ('identification', 'type', unicode),
        ('description', 'type', unicode),
        ('name', 'type', unicode),

        ('identification', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),

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
    data.DataExtent: (

        ('temporal', 'type', data.DataExtentTemporal),
        ('geographical', 'type', data.DataExtentGeographical),

        ('temporal', 'cardinality', "1.1"),
        ('geographical', 'cardinality', "1.1"),

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
    grids.GridTile: (

        ('mnemonic', 'type', unicode),
        ('refinement_scheme', 'type', unicode),
        ('is_regular', 'type', bool),
        ('vertical_crs', 'type', unicode),
        ('long_name', 'type', unicode),
        ('horizontal_crs', 'type', unicode),
        ('simple_grid_geom', 'type', grids.SimpleGridGeometry),
        ('id', 'type', unicode),
        ('is_conformal', 'type', bool),
        ('cell_ref_array', 'type', unicode),
        ('area', 'type', unicode),
        ('cell_array', 'type', unicode),
        ('grid_north_pole', 'type', unicode),
        ('nx', 'type', int),
        ('ny', 'type', int),
        ('nz', 'type', int),
        ('vertical_resolution', 'type', grids.GridTileResolutionType),
        ('discretization_type', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('extent', 'type', grids.GridExtent),
        ('zcoords', 'type', grids.VerticalCoordinateList),
        ('coordinate_pole', 'type', unicode),
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
        ('simple_grid_geom', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),
        ('is_conformal', 'cardinality', "0.1"),
        ('cell_ref_array', 'cardinality', "0.1"),
        ('area', 'cardinality', "0.1"),
        ('cell_array', 'cardinality', "0.1"),
        ('grid_north_pole', 'cardinality', "0.1"),
        ('nx', 'cardinality', "0.1"),
        ('ny', 'cardinality', "0.1"),
        ('nz', 'cardinality', "0.1"),
        ('vertical_resolution', 'cardinality', "0.1"),
        ('discretization_type', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('short_name', 'cardinality', "0.1"),
        ('extent', 'cardinality', "0.1"),
        ('zcoords', 'cardinality', "0.1"),
        ('coordinate_pole', 'cardinality', "0.1"),
        ('is_uniform', 'cardinality', "0.1"),
        ('coord_file', 'cardinality', "0.1"),
        ('geometry_type', 'cardinality', "0.1"),
        ('horizontal_resolution', 'cardinality', "0.1"),
        ('is_terrain_following', 'cardinality', "0.1"),

    ),
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
    data.DataExtentTemporal: (

        ('time_interval', 'type', data.DataExtentTimeInterval),
        ('begin', 'type', datetime.date),
        ('end', 'type', datetime.date),

        ('time_interval', 'cardinality', "0.1"),
        ('begin', 'cardinality', "0.1"),
        ('end', 'cardinality', "0.1"),

    ),
    software.SpatialRegriddingProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

    ),
    data.DataObject: (

        ('hierarchy_level', 'type', data.DataHierarchyLevel),
        ('description', 'type', unicode),
        ('keyword', 'type', unicode),
        ('restriction', 'type', data.DataRestriction),
        ('geometry_model', 'type', unicode),
        ('child_object', 'type', data.DataObject),
        ('storage', 'type', data.DataStorage),
        ('distribution', 'type', data.DataDistribution),
        ('content', 'type', data.DataContent),
        ('acronym', 'type', unicode),
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
        ('geometry_model', 'cardinality', "0.1"),
        ('child_object', 'cardinality', "0.N"),
        ('storage', 'cardinality', "0.N"),
        ('distribution', 'cardinality', "0.1"),
        ('content', 'cardinality', "0.N"),
        ('acronym', 'cardinality', "0.1"),
        ('citations', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('purpose', 'cardinality', "0.1"),
        ('extent', 'cardinality', "0.1"),
        ('source_simulation', 'cardinality', "0.1"),
        ('parent_object', 'cardinality', "0.1"),
        ('properties', 'cardinality', "0.N"),
        ('data_status', 'cardinality', "0.1"),

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
    software.Composition: (

        ('couplings', 'type', unicode),
        ('description', 'type', unicode),

        ('couplings', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),

    ),
    software.ComponentLanguageProperty: (

        ('name', 'type', unicode),
        ('value', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('value', 'cardinality', "0.1"),

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
    shared.Daily360: (

        ('length', 'type', int),
        ('range', 'type', shared.DateRange),
        ('description', 'type', unicode),

        ('length', 'cardinality', "0.1"),
        ('range', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------


    (data.DataDistribution, 'access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataDistribution, 'fee'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataDistribution, 'responsible_party'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.1"),

    ),
    (data.DataDistribution, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.Timing, 'start'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.Timing, 'end'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.Timing, 'rate'): (

        ('type', int),

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

    (activity.Simulation, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'control_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'outputs'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'simulation_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.Simulation, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'authors'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'spinup_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "1.1"),

    ),
    (activity.Simulation, 'restarts'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'spinup_date_range'): (

        ('type', shared.ClosedDateRange),

        ('cardinality', "0.1"),

    ),
    (activity.Simulation, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

    ),
    (activity.Simulation, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

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

    (quality.CimQuality, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (quality.CimQuality, 'reports'): (

        ('type', quality.Report),

        ('cardinality', "0.N"),

    ),

    (activity.NumericalRequirementOption, 'description'): (

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
    (activity.NumericalRequirementOption, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirementOption, 'relationship'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.DateRange, 'duration'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.DocGenealogy, 'relationships'): (

        ('type', shared.DocRelationship),

        ('cardinality', "0.N"),

    ),

    (shared.DataSource, 'purpose'): (

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

    (activity.LateralBoundaryCondition, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.LateralBoundaryCondition, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.LateralBoundaryCondition, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.LateralBoundaryCondition, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

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

    (software.TimeTransformation, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.TimeTransformation, 'mapping_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

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

    (shared.Platform, 'units'): (

        ('type', shared.MachineCompilerUnit),

        ('cardinality', "1.N"),

    ),
    (shared.Platform, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (shared.Platform, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Platform, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Platform, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Platform, 'contacts'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (activity.NumericalActivity, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'funding_sources'): (

        ('type', unicode),

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
    (activity.NumericalActivity, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalActivity, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.Relationship, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Relationship, 'direction'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.ResponsibleParty, 'individual_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'abbreviation'): (

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
    (shared.ResponsibleParty, 'address'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'email'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ResponsibleParty, 'url'): (

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

    (shared.DocMetaInfo, 'type_sort_key'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'drs_path'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'sort_key'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'create_date'): (

        ('type', datetime.datetime),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'update_date'): (

        ('type', datetime.datetime),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'version'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'project'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'status'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'source'): (

        ('type', unicode),

        ('cardinality', "1.1"),

        ('constant', "scripts"),
    ),
    (shared.DocMetaInfo, 'language'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'external_ids'): (

        ('type', shared.StandardName),

        ('cardinality', "0.N"),

    ),
    (shared.DocMetaInfo, 'author'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'source_key'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'genealogy'): (

        ('type', shared.DocGenealogy),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'type_display_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'id'): (

        ('type', uuid.UUID),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'drs_keys'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (shared.DocMetaInfo, 'institute'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (software.ProcessorComponent, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ProcessorComponent, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.ProcessorComponent, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (software.ProcessorComponent, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.ProcessorComponent, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),

    (activity.OutputRequirement, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.OutputRequirement, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.OutputRequirement, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.OutputRequirement, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

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

    (software.Connection, 'properties'): (

        ('type', software.ConnectionProperty),

        ('cardinality', "0.N"),

    ),
    (software.Connection, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'time_transformation'): (

        ('type', software.TimeTransformation),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'priming'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'spatial_regridding'): (

        ('type', software.SpatialRegridding),

        ('cardinality', "0.N"),

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
    (software.Connection, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Connection, 'sources'): (

        ('type', software.ConnectionEndpoint),

        ('cardinality', "0.N"),

    ),
    (software.Connection, 'time_profile'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

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
    (grids.SimpleGridGeometry, 'ycoords'): (

        ('type', grids.CoordinateList),

        ('cardinality', "1.1"),

    ),
    (grids.SimpleGridGeometry, 'zcoords'): (

        ('type', grids.CoordinateList),

        ('cardinality', "0.1"),

    ),
    (grids.SimpleGridGeometry, 'xcoords'): (

        ('type', grids.CoordinateList),

        ('cardinality', "1.1"),

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

    (activity.NumericalRequirement, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirement, 'requirement_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalRequirement, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.NumericalRequirement, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalRequirement, 'options'): (

        ('type', activity.NumericalRequirementOption),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalRequirement, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.StandardName, 'standards'): (

        ('type', shared.Standard),

        ('cardinality', "0.N"),

    ),
    (shared.StandardName, 'value'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.StandardName, 'is_open'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),

    (activity.PhysicalModification, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.PhysicalModification, 'is_conformant'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (activity.PhysicalModification, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.PhysicalModification, 'sources'): (

        ('type', shared.DataSource),

        ('cardinality', "0.N"),

    ),
    (activity.PhysicalModification, 'frequency'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.PhysicalModification, 'requirements'): (

        ('type', activity.NumericalRequirement),

        ('cardinality', "0.N"),

    ),

    (activity.SimulationComposite, 'outputs'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'authors'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'simulation_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'spinup_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'child'): (

        ('type', activity.Simulation),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'restarts'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'date_range'): (

        ('type', shared.DateRange),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'control_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'rank'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationComposite, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'spinup_date_range'): (

        ('type', shared.ClosedDateRange),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationComposite, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationComposite, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (activity.ExperimentRelationship, 'target'): (

        ('type', activity.ExperimentRelationshipTarget),

        ('cardinality', "1.1"),

    ),
    (activity.ExperimentRelationship, 'direction'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.ExperimentRelationship, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.ExperimentRelationship, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.Compiler, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Compiler, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Compiler, 'options'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Compiler, 'language'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Compiler, 'environment_variables'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Compiler, 'version'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.MachineCompilerUnit, 'compilers'): (

        ('type', shared.Compiler),

        ('cardinality', "0.N"),

    ),
    (shared.MachineCompilerUnit, 'machine'): (

        ('type', shared.Machine),

        ('cardinality', "1.1"),

    ),

    (activity.MeasurementCampaign, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.MeasurementCampaign, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.MeasurementCampaign, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.MeasurementCampaign, 'duration'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (activity.MeasurementCampaign, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),

    (software.Coupling, 'properties'): (

        ('type', software.CouplingProperty),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'is_fully_specified'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (software.Coupling, 'connections'): (

        ('type', software.Connection),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'purpose'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.Coupling, 'time_lag'): (

        ('type', software.TimeLag),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'sources'): (

        ('type', software.CouplingEndpoint),

        ('cardinality', "1.N"),

    ),
    (software.Coupling, 'spatial_regriddings'): (

        ('type', software.SpatialRegridding),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'time_transformation'): (

        ('type', software.TimeTransformation),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'target'): (

        ('type', software.CouplingEndpoint),

        ('cardinality', "1.1"),

    ),
    (software.Coupling, 'time_profile'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Coupling, 'transformers'): (

        ('type', software.ProcessorComponent),

        ('cardinality', "0.N"),

    ),
    (software.Coupling, 'priming'): (

        ('type', shared.DataSource),

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
    (shared.ChangeProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ChangeProperty, 'id'): (

        ('type', unicode),

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

    (data.DataStorage, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorage, 'size'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.DataStorage, 'modification_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (data.DataStorage, 'format'): (

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

    (software.Parallelisation, 'processes'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (software.Parallelisation, 'ranks'): (

        ('type', software.Rank),

        ('cardinality', "0.N"),

    ),

    (software.Component, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.Component, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.Component, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.Component, 'license'): (

        ('type', shared.License),

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
    (data.DataContent, 'frequency'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataContent, 'topic'): (

        ('type', data.DataTopic),

        ('cardinality', "1.1"),

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

    (shared.DocRelationshipTarget, 'reference'): (

        ('type', shared.DocReference),

        ('cardinality', "0.1"),

    ),

    (quality.Evaluation, 'specification_hyperlink'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'did_pass'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'explanation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'specification'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (quality.Evaluation, 'type_hyperlink'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.ExperimentRelationshipTarget, 'numerical_experiment'): (

        ('type', activity.NumericalExperiment),

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

    (grids.GridTileResolutionType, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTileResolutionType, 'properties'): (

        ('type', grids.GridProperty),

        ('cardinality', "0.N"),

    ),

    (software.EntryPoint, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Citation, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'organisation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'alternative_title'): (

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
    (shared.Citation, 'collective_title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'type'): (

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

    (activity.InitialCondition, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.InitialCondition, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.InitialCondition, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.InitialCondition, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

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

    (data.DataHierarchyLevel, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataHierarchyLevel, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataHierarchyLevel, 'is_open'): (

        ('type', bool),

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
    (software.ComponentProperty, 'sub_properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'values'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'units'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentProperty, 'standard_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ComponentProperty, 'description'): (

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

    (software.ConnectionEndpoint, 'instance_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ConnectionEndpoint, 'properties'): (

        ('type', software.ConnectionProperty),

        ('cardinality', "0.N"),

    ),
    (software.ConnectionEndpoint, 'data_source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),

    (activity.SpatioTemporalConstraint, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'date_range'): (

        ('type', shared.DateRange),

        ('cardinality', "0.1"),

    ),
    (activity.SpatioTemporalConstraint, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.SpatioTemporalConstraint, 'spatial_resolution'): (

        ('type', unicode),

        ('cardinality', "0.1"),

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

    (data.DataStorageIp, 'size'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'path'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'file_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'modification_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'protocol'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageIp, 'host'): (

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

    (activity.NumericalExperiment, 'requires'): (

        ('type', activity.NumericalActivity),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'supports'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalExperiment, 'funding_sources'): (

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
    (activity.NumericalExperiment, 'generates'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.NumericalExperiment, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.NumericalExperiment, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

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

    (shared.Change, 'author'): (

        ('type', shared.ResponsibleParty),

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
    (shared.Change, 'date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.Change, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.Experiment, 'supports'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'measurement_campaigns'): (

        ('type', activity.MeasurementCampaign),

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
    (activity.Experiment, 'requires'): (

        ('type', activity.NumericalActivity),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.Experiment, 'generates'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),

    (shared.DocRelationship, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocRelationship, 'direction'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocRelationship, 'target'): (

        ('type', shared.DocRelationshipTarget),

        ('cardinality', "1.1"),

    ),
    (shared.DocRelationship, 'description'): (

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

    (software.TimeLag, 'units'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.TimeLag, 'value'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (software.ConnectionProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ConnectionProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.SpatialRegridding, 'standard_method'): (

        ('type', unicode),

        ('cardinality', "0.1"),

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

    (grids.VerticalCoordinateList, 'properties'): (

        ('type', grids.GridProperty),

        ('cardinality', "0.N"),

    ),
    (grids.VerticalCoordinateList, 'uom'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.VerticalCoordinateList, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.VerticalCoordinateList, 'form'): (

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

    (activity.Conformance, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'is_conformant'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (activity.Conformance, 'frequency'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'sources'): (

        ('type', shared.DataSource),

        ('cardinality', "0.N"),

    ),
    (activity.Conformance, 'requirements'): (

        ('type', activity.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (activity.Conformance, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (activity.BoundaryCondition, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.BoundaryCondition, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.BoundaryCondition, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.BoundaryCondition, 'source'): (

        ('type', shared.DataSource),

        ('cardinality', "0.1"),

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
    (misc.DocumentSet, 'data'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (misc.DocumentSet, 'platform'): (

        ('type', shared.Platform),

        ('cardinality', "0.1"),

    ),
    (misc.DocumentSet, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (misc.DocumentSet, 'model'): (

        ('type', software.ModelComponent),

        ('cardinality', "0.1"),

    ),
    (misc.DocumentSet, 'simulation'): (

        ('type', activity.SimulationRun),

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

    (shared.ClosedDateRange, 'end'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (shared.ClosedDateRange, 'duration'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ClosedDateRange, 'start'): (

        ('type', datetime.datetime),

        ('cardinality', "1.1"),

    ),

    (activity.Ensemble, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.Ensemble, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.Ensemble, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'members'): (

        ('type', activity.EnsembleMember),

        ('cardinality', "1.N"),

    ),
    (activity.Ensemble, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'types'): (

        ('type', unicode),

        ('cardinality', "1.N"),

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

    (software.StatisticalModelComponent, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'types'): (

        ('type', unicode),

        ('cardinality', "1.N"),

    ),
    (software.StatisticalModelComponent, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'timing'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.StatisticalModelComponent, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

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
    (software.StatisticalModelComponent, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.StatisticalModelComponent, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (software.StatisticalModelComponent, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.StatisticalModelComponent, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),

    (grids.GridMosaic, 'extent'): (

        ('type', grids.GridExtent),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'has_congruent_tiles'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'mosaics'): (

        ('type', grids.GridMosaic),

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
    (grids.GridMosaic, 'is_leaf'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (grids.GridMosaic, 'mosaic_count'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'tiles'): (

        ('type', grids.GridTile),

        ('cardinality', "0.N"),

    ),
    (grids.GridMosaic, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridMosaic, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridMosaic, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridMosaic, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (grids.GridMosaic, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

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

    (activity.SimulationRelationshipTarget, 'simulation'): (

        ('type', shared.DocReference),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRelationshipTarget, 'target'): (

        ('type', unicode),

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

    (activity.SimulationRun, 'outputs'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'authors'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'simulation_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'control_simulation'): (

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
    (activity.SimulationRun, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRun, 'spinup_simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'restarts'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRun, 'date_range'): (

        ('type', shared.DateRange),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRun, 'model'): (

        ('type', software.ModelComponent),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "1.1"),

    ),
    (activity.SimulationRun, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'spinup_date_range'): (

        ('type', shared.ClosedDateRange),

        ('cardinality', "0.1"),

    ),
    (activity.SimulationRun, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.SimulationRun, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),

    (data.DataStorageDb, 'owner'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'size'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'table'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageDb, 'modification_date'): (

        ('type', datetime.datetime),

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

    (shared.Machine, 'maximum_processors'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'vendor'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'interconnect'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'operating_system'): (

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
    (shared.Machine, 'libraries'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (shared.Machine, 'system'): (

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
    (shared.Machine, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Machine, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.DocReference, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'external_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'url'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'id'): (

        ('type', uuid.UUID),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'version'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'changes'): (

        ('type', shared.Change),

        ('cardinality', "0.N"),

    ),
    (shared.DocReference, 'name'): (

        ('type', unicode),

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
    (data.DataExtentTimeInterval, 'factor'): (

        ('type', int),

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
    (shared.Calendar, 'description'): (

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

    (software.Deployment, 'platform'): (

        ('type', shared.Platform),

        ('cardinality', "0.1"),

    ),
    (software.Deployment, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Deployment, 'deployment_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.Deployment, 'parallelisation'): (

        ('type', software.Parallelisation),

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

    (data.DataExtent, 'geographical'): (

        ('type', data.DataExtentGeographical),

        ('cardinality', "1.1"),

    ),
    (data.DataExtent, 'temporal'): (

        ('type', data.DataExtentTemporal),

        ('cardinality', "1.1"),

    ),

    (software.ModelComponent, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'types'): (

        ('type', unicode),

        ('cardinality', "1.N"),

    ),
    (software.ModelComponent, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'online_resource'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'language'): (

        ('type', software.ComponentLanguage),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'parent'): (

        ('type', software.Component),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'timing'): (

        ('type', software.Timing),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'sub_components'): (

        ('type', software.Component),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'activity'): (

        ('type', activity.Activity),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'citations'): (

        ('type', shared.Citation),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'properties'): (

        ('type', software.ComponentProperty),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'code_access'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'is_embedded'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'grid'): (

        ('type', grids.GridSpec),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (software.ModelComponent, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'deployments'): (

        ('type', software.Deployment),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ModelComponent, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.ModelComponent, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.ModelComponent, 'license'): (

        ('type', shared.License),

        ('cardinality', "0.1"),

    ),

    (grids.GridTile, 'is_terrain_following'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'short_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'nx'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'coord_file'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'zcoords'): (

        ('type', grids.VerticalCoordinateList),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'extent'): (

        ('type', grids.GridExtent),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'vertical_resolution'): (

        ('type', grids.GridTileResolutionType),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'geometry_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'mnemonic'): (

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
    (grids.GridTile, 'discretization_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'grid_north_pole'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'simple_grid_geom'): (

        ('type', grids.SimpleGridGeometry),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'coordinate_pole'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'is_regular'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'ny'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'area'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'cell_ref_array'): (

        ('type', unicode),

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
    (grids.GridTile, 'is_uniform'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'is_conformal'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'refinement_scheme'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (grids.GridTile, 'cell_array'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

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

    (software.SpatialRegriddingProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SpatialRegriddingProperty, 'value'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (data.DataObject, 'geometry_model'): (

        ('type', unicode),

        ('cardinality', "0.1"),

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
    (data.DataObject, 'content'): (

        ('type', data.DataContent),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'parent_object'): (

        ('type', data.DataObject),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'data_status'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'properties'): (

        ('type', data.DataProperty),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'source_simulation'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'distribution'): (

        ('type', data.DataDistribution),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'purpose'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'restriction'): (

        ('type', data.DataRestriction),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'child_object'): (

        ('type', data.DataObject),

        ('cardinality', "0.N"),

    ),
    (data.DataObject, 'extent'): (

        ('type', data.DataExtent),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'acronym'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataObject, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),

    (data.DataStorageFile, 'size'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'path'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'location'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'file_system'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'format'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'file_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.DataStorageFile, 'modification_date'): (

        ('type', datetime.datetime),

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
    (software.Rank, 'increment'): (

        ('type', int),

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

    (software.ComponentLanguageProperty, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentLanguageProperty, 'value'): (

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
    (activity.EnsembleMember, 'simulation'): (

        ('type', activity.Simulation),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'rationales'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'ensemble'): (

        ('type', activity.Ensemble),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'projects'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

        ('cardinality', "0.N"),

    ),
    (activity.EnsembleMember, 'ensemble_ids'): (

        ('type', shared.StandardName),

        ('cardinality', "0.N"),

    ),

    (activity.DownscalingSimulation, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.DownscalingSimulation, 'supports'): (

        ('type', activity.Experiment),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'downscaling_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.DownscalingSimulation, 'funding_sources'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.DownscalingSimulation, 'description'): (

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
    (activity.DownscalingSimulation, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.DownscalingSimulation, 'rationales'): (

        ('type', unicode),

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
    (activity.DownscalingSimulation, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),

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
    (activity.DownscalingSimulation, 'inputs'): (

        ('type', software.Coupling),

        ('cardinality', "0.N"),

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

    misc: "Miscellaneous types.",
    quality: "Types that describe the quailty of output that climate models emit.",
    activity: "Types that describe context against which climate models are run.",
    software: "Types that describe the climate models software.",
    data: "Types that describe output that climate models emit.",
    shared: "Shared types that might be imported from other packages within the ontology.",
    grids: "Types that describe the grids that climate models plot.",

    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    misc.DocumentSet: """
        Represents a bundled set of documents.

    """,
    quality.CimQuality: """
        The starting point for a quality record.  It can contain any number of issues and reports.  An issue is an open-ended description of some issue about a CIM instance.  A record is a prescribed description of some specific quantitative measure that has been applied to a CIM instance.

    """,
    quality.Report: """
        Creates and returns instance of report class.

    """,
    quality.Evaluation: """
        Creates and returns instance of evaluation class.

    """,
    quality.Measure: """
        Creates and returns instance of measure class.

    """,
    activity.LateralBoundaryCondition: """
        A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).

    """,
    activity.Simulation: """
        A simulation is the implementation of a numerical experiment.  A simulation can be made up of 'child' simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

    """,
    activity.SpatioTemporalConstraint: """
        Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

    """,
    activity.EnsembleMember: """
        A simulation is the implementation of a numerical experiment.  A simulation can be made up of 'child' simulations aggregated together to form a 'simulation composite'.  The 'parent' simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

    """,
    activity.NumericalRequirementOption: """
        A NumericalRequirement that is being used as a set of related requirements; For example if a requirement is to use 1 of 3 boundary conditions, then that 'parent' requirement would have three 'child' RequirmentOptions (each of one with the XOR optionRelationship).

    """,
    activity.NumericalExperiment: """
        A numerical experiment may be generated by an experiment, in which case it is inSupportOf the experiment. But a numerical experiment may also exist as an activity in its own right (as it might be if it were needed for a MIP). Examples: AR4 individual experiments, AR5 individual experiments, RAPID THC experiments etc.

    """,
    activity.NumericalActivity: """
        Creates and returns instance of numerical_activity class.

    """,
    activity.Experiment: """
        An experiment might be an activity which is both observational and numerical in focus, for example, a measurement campaign and numerical experiments for an alpine experiment.  It is a place for the scientific description of the reason why an experiment was made.

    """,
    activity.Conformance: """
        A conformance class maps how a configured model component met a specific numerical requirement.  For example, for a double CO2 boundary condition, a model component might read a CO2 dataset in which CO2 has been doubled, or it might modify a parameterisation (presumably with a factor of two somewhere).  So, the conformance links a requirement to a DataSource (which can be either an actual DataObject or a property of a model component).  In some cases a model/simulation may _naturally_ conform to a requirement.  In this case there would be no reference to a DataSource but the conformant attribute would be true.  If something is purpopsefully non-conformant then the conformant attribute would be false.

    """,
    activity.OutputRequirement: """
        Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

    """,
    activity.BoundaryCondition: """
        A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).

    """,
    activity.SimulationRelationship: """
        Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

    """,
    activity.MeasurementCampaign: """
        Creates and returns instance of measurement_campaign class.

    """,
    activity.ExperimentRelationshipTarget: """
        Creates and returns instance of experiment_relationship_target class.

    """,
    activity.NumericalRequirement: """
        A description of the requirements of particular experiments.  Numerical Requirements can be initial conditions, boundary conditions, or physical modificiations.

    """,
    activity.PhysicalModification: """
        Physical modification is the implementation of a boundary condition numerical requirement that is achieved within the model code rather than from some external source file. It  might include, for example,  a specific rate constant within a chemical reaction, or coefficient value(s) in a parameterisation.  For example, one might require a numerical experiment where specific chemical reactions were turned off - e.g. no heterogeneous chemistry.

    """,
    activity.SimulationRelationshipTarget: """
        Creates and returns instance of simulation_relationship_target class.

    """,
    activity.SimulationComposite: """
        A SimulationComposite is an aggregation of Simulations. With the aggreation connector between Simulation and SimulationComposite(SC) the SC can be made up of both SimulationRuns and SCs. The SimulationComposite is the new name for the concept of SimulationCollection: A simulation can be made up of 'child' simulations aggregated together to form a 'simulation composite'.  The 'parent' simulation can be made up of whole or partial child simulations and the SimulationComposite attributes need to be able to capture this.

    """,
    activity.SimulationRun: """
        A SimulationRun is, as the name implies, one single model run. A SimulationRun is a Simulation. There is a one to one association between SimulationRun and (a top-level) SoftwarePackage::ModelComponent.

    """,
    activity.ExperimentRelationship: """
        Contains a set of relationship types specific to a experiment document that can be used to describe its genealogy.

    """,
    activity.Activity: """
        An abstract class used as the parent of MeasurementCampaigns, Projects, Experiments, and NumericalActivities.

    """,
    activity.Ensemble: """
        An ensemble is made up of two or more simulations which are to be compared against each other to create ensemble statistics. Ensemble members can differ in terms of initial conditions, physical parameterisation and the model used. An ensemble bundles together sets of ensembleMembers, all of which reference the same Simulation(Run) and include one or more changes.

    """,
    activity.DownscalingSimulation: """
        A simulation is the implementation of a numerical experiment.  A simulation can be made up of 'child' simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

    """,
    activity.InitialCondition: """
        An initial condition is a numerical requirement on a model prognostic variable value at time zero.

    """,
    software.Timing: """
        Provides information about the rate of couplings and connections and/or the timing characteristics of individual components - for example, the start and stop times that the component was run for or the units of time that a component is able to model (in a single timestep).

    """,
    software.SpatialRegriddingUserMethod: """
        Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.

    """,
    software.Component: """
        A SofwareComponent is an abstract component from which all other components derive. It represents an element that takes input data and generates output data. A SoftwareCompnent can include nested 'child' components. Every component can have 'componentProperties' which describe the scientific properties that a component simulates (for example, temperature, pressure, etc.) and the numerical properties that influence how a component performs its simulation (for example, the force of gravity). A SoftwareComponent can also have a Deployment, which describes how software is deployed onto computing resources. And a SoftwareComponent can have a composition, which describes how ComponentProperties are coupled together either to/from other SoftwareComponents or external data files. The properties specified by a component's composition must be owned by that component or a child of that component; child components cannot couple together their parents' properties.

    """,
    software.ComponentLanguage: """
        Details of the programming language a component is written in. There is an assumption that all EntryPoints use the same ComponentLanguage.

    """,
    software.Parallelisation: """
        Describes how a deployment has been parallelised across a computing platform.

    """,
    software.ComponentProperty: """
        ComponentProperties include things that a component simulates (ie: pressure, humidity) and things that prescribe that simulation (ie: gravity, choice of advection scheme). Note that this is a specialisation of shared::DataSource. data::DataObject is also a specialisation of shared::DataSource. This allows software::Connections and/or activity::Conformance to refer to either ComponentProperties or DataObjects.

    """,
    software.TimeTransformation: """
        The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.

    """,
    software.CouplingEndpoint: """
        The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).

    """,
    software.Composition: """
        The set of Couplings used by a Component. Couplings can only occur between child components. That is, a composition must belong to an ancestor component of the components whose fields are being connected.

    """,
    software.ModelComponent: """
        A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.

    """,
    software.TimeLag: """
        The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.

    """,
    software.Rank: """
        Creates and returns instance of rank class.

    """,
    software.ConnectionEndpoint: """
        The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).

    """,
    software.StatisticalModelComponent: """
        Creates and returns instance of statistical_model_component class.

    """,
    software.Coupling: """
        A coupling represents a set of Connections between a source and target component. Couplings can be complete or incomplete. If they are complete then they must include all Connections between model properties. If they are incomplete then the connections can be underspecified or not listed at all.

    """,
    software.Deployment: """
        Gives information about the technical properties of a component: what machine it was run on, which compilers were used, how it was parallised, etc. A deployment basically associates a deploymentDate with a Platform. A deployment only exists if something has been deployed. A platform, in contrast, can exist independently, waiting to be used in deployments.

    """,
    software.CouplingProperty: """
        A CouplingProperty is a name/value pair used to specify OASIS-specific properties.

    """,
    software.EntryPoint: """
        Describes a function or subroutine of a SoftwareComponent. BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model. Currently, a very basic schedule can be approximated by using the 'proceeds' and 'follows' attributes, however a more complete system is required for full BFG compatibility. Every EntryPoint can have a set of arguments associated with it. These reference (previously defined) ComponentProperties.

    """,
    software.Connection: """
        A Connection represents a link from a source DataSource to a target DataSource.  These can either be ComponentProperties (ie: the values come from an internal component) or DataObjects (ie: the values come from an external file).   It can be associated with another software component (a transformer).  If present, the rate, lag, timeTransformation, and spatialRegridding override that of the parent coupling.  Note that there is the potential for multiple connectionSource & connectionTarget and multiple couplingSources & couplingTargets.  This may lead users to wonder how to match up a connection source (a ComponentProperty) with its coupling source (a SoftwareComponent). Clever logic is not required though; because the sources and targets are listed by reference, they can be found in a CIM document and the parent can be navigated to from there - there is no need to consult the source or target of the coupling.

    """,
    software.ConnectionProperty: """
        A ConnectionProperty is a name/value pair used to specify OASIS-specific properties.

    """,
    software.ProcessorComponent: """
        A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.

    """,
    software.SpatialRegridding: """
        Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.

    """,
    software.ComponentLanguageProperty: """
        This provides a place to include language-specific information. Every property is basically a name/value pair, where the names are things like: moduleName, reservedUnits, reservedNames (these are all examples of Fortran-specific properties).

    """,
    software.SpatialRegriddingProperty: """
        Used for OASIS-specific regridding information (ie: masked, order, normalisation, etc.)

    """,
    data.DataExtentGeographical: """
        A data object geographical extent represents the geographical coverage associated with a data object.

    """,
    data.DataDistribution: """
        Describes how a DataObject is distributed.

    """,
    data.DataHierarchyLevel: """
        The type of data object that is grouped together into a particular hierarchy.  Currently, this is made up of terms describing how the Met Office splits up archived data and how THREDDS categorises variables.

    """,
    data.DataStorageIp: """
        Contains attributes to describe a DataObject stored as a database file.

    """,
    data.DataContent: """
        The contents of the data object; like ISO: MD_ContentInformation.

    """,
    data.DataProperty: """
        A property of a DataObject. Currently this is intended to be used to record CF specific information (like packing, scaling, etc.) for OASIS4.

    """,
    data.DataRestriction: """
        An access or use restriction on some element of the DataObject actual data.

    """,
    data.DataObject: """
        A DataObject describes a unit of data.  DataObjects can be grouped hierarchically.  The attributes hierarchyLevelName and hierarchyLevelValue describe how objects are grouped.

    """,
    data.DataStorageFile: """
        Contains attributes to describe a DataObject stored as a single file.

    """,
    data.DataStorage: """
        Describes the method that the DataObject is stored. An abstract class with specific child classes for each supported method.

    """,
    data.DataExtent: """
        A data object extent represents the geographical and temporal coverage associated with a data object.

    """,
    data.DataExtentTimeInterval: """
        A data object temporal extent represents the temporal coverage associated with a data object.

    """,
    data.DataStorageDb: """
        Contains attributes to describe a DataObject stored as a database file.

    """,
    data.DataExtentTemporal: """
        A data object temporal extent represents the temporal coverage associated with a data object.

    """,
    data.DataTopic: """
        Describes the content of a data object: the variable name, units, etc.

    """,
    shared.License: """
        A description of a license restricting access to a unit of data or software.

    """,
    shared.Machine: """
        A description of a machine used by a particular platform.

    """,
    shared.PerpetualPeriod: """
        Creates and returns instance of perpetual_period class.

    """,
    shared.DataSource: """
        A DataSource can be realised by either a DataObject (file), a DataContent (variable), a Component (model), or a ComponentProperty (variable); all of those can supply data.

    """,
    shared.Relationship: """
        A record of a relationship between one document and another. This class is abstract; specific document types must specialise this class for their relationshipTypes to be included in a document's genealogy.

    """,
    shared.Property: """
        A simple name/value pair representing a property of some entity or other.

    """,
    shared.DocGenealogy: """
        A record of a document's history. A genealogy element contains a textual description and a set of relationships. Each relationship has a type and a reference to some target. There are different relationships for different document types.

    """,
    shared.Standard: """
        Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

    """,
    shared.MachineCompilerUnit: """
        Associates a machine with a [set of] compilers.  This is a separate class in case a platform needs to specify more than one machine/compiler pair.

    """,
    shared.Platform: """
        A platform is a description of resources used to deploy a component/simulation.  A platform pairs a machine with a (set of) compilers.  There is also a point of contact for the platform.

    """,
    shared.Calendar: """
        Describes a method of calculating a span of dates.

    """,
    shared.Compiler: """
        A description of a compiler used on a particular platform.

    """,
    shared.Citation: """
        An academic reference to published work.

    """,
    shared.ClosedDateRange: """
        A date range with specified start and end points.

    """,
    shared.ResponsibleParty: """
        A person/organsiation responsible for some aspect of a climate science artefact.

    """,
    shared.DocMetaInfo: """
        Encapsulates document meta information.

    """,
    shared.ChangeProperty: """
        A description of a single change applied to a single target.  Every ChangeProperty has a description, and may also have a name from a controlled vocabulary and a value.

    """,
    shared.Daily360: """
        Creates and returns instance of daily_360 class.

    """,
    shared.DateRange: """
        Creates and returns instance of date_range class.

    """,
    shared.Change: """
        A description of [a set of] changes applied at a particular time, by a particular party, to a particular unit of metadata.

    """,
    shared.StandardName: """
        Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

    """,
    shared.DocRelationship: """
        Contains the set of relationships supported by a Document.

    """,
    shared.OpenDateRange: """
        A date range without a specified start and/or end point.

    """,
    shared.RealCalendar: """
        Creates and returns instance of real_calendar class.

    """,
    shared.DocRelationshipTarget: """
        Creates and returns instance of doc_relationship_target class.

    """,
    shared.DocReference: """
        A reference to another cim entity.

    """,
    grids.CoordinateList: """
        The CoordList type may be used to specify a list of coordinates, typically for the purpose of defining coordinates along the X, Y or Z axes. The length of the coordinate list is given by the attribute of that name. This may be used by software to allocate memory in advance of storing the coordinate values. The hasConstantOffset attribute may be used to indicate that the coordinate list consists of values with constant offset (spacing). In this case only the first coordinate value and the offset (spacing) value need to be specified; however, the length attribute must still define the final as-built size of the coordinate list.

    """,
    grids.GridProperty: """
        Creates and returns instance of grid_property class.

    """,
    grids.GridTile: """
        The GridTile class is used to model an individual grid tile contained within a grid mosaic. A GridTile consists of an array of grid cells which may be defined in one of four ways: 1) for simple grids, by use of the SimpleGridGeometry data type; 2) by defining an array of GridCell objects; 3) by specifying an array of references to externally defined GridCell objects; or 4) by specifying a URI to a remote data file containing the grid cell definitions.  For all but the simplest grid tiles, it is envisaged that method 4 above will be the most frequently used option. However, it should be remembered that the CIM is primarily concerned with encoding climate model metadata. Specifying the coordinates of individual grid tiles and cells will most likely not be required as part of such metadata descriptions.  A GridTile object is associated with a geodetic or projected CRS via the horizontalCRS property, and with a vertical CRS via the verticalCRS property.

    """,
    grids.SimpleGridGeometry: """
        SimpleGridGeometry:This property may be used to define the coordinates of the nodes or cells making up a simple (i.e. uniform or regular) grid tile. More details are provided in the description of the SimpleGridGeometry data type.

    """,
    grids.GridMosaic: """
        The GridMosaic class is used to define the geometry properties of an earth system model grid or an exchange grid. Such a grid definition may then be referenced by any number of earth system models. A GridMosaic object consists either of 1 or more child GridMosaics, or one or more child GridTiles, but not both. In the latter case the isLeaf property should be set to true, indicating that the mosaic is a leaf mosaic.

    """,
    grids.VerticalCoordinateList: """
        There are some specific attributes that are associated with vertical coordinates.

    """,
    grids.GridExtent: """
        DataType for recording the geographic extent of a gridMosaic or gridTile.

    """,
    grids.GridSpec: """
        This is a container class for GridSpec objects. A GridSpec object can contain one or more esmModelGrid objects, and one or more esmExchangeGrid objects. These objects may be serialised to one or possibly several files according to taste. Since GridSpec is sub-typed from GML's AbstractGeometryType it can, and should, be identified using a gml:id attribute.

    """,
    grids.GridTileResolutionType: """
        Provides a description and set of named properties for the horizontal or vertical resolution.

    """,

    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------

    (misc.DocumentSet, 'ensembles'):
        "Associated ensemble runs.",
    (misc.DocumentSet, 'experiment'):
        "Associated numerical experiment.",
    (misc.DocumentSet, 'platform'):
        "Associated simulation execution platform.",
    (misc.DocumentSet, 'data'):
        "Associated input/output data.",
    (misc.DocumentSet, 'grids'):
        "Associated grid-spec.",
    (misc.DocumentSet, 'model'):
        "Associated model component.",
    (misc.DocumentSet, 'meta'):
        None,
    (misc.DocumentSet, 'simulation'):
        "Associated simulation run.",
    (quality.CimQuality, 'meta'):
        None,
    (quality.CimQuality, 'reports'):
        None,
    (quality.Report, 'date'):
        None,
    (quality.Report, 'measure'):
        None,
    (quality.Report, 'evaluator'):
        None,
    (quality.Report, 'evaluation'):
        None,
    (quality.Evaluation, 'did_pass'):
        None,
    (quality.Evaluation, 'specification'):
        None,
    (quality.Evaluation, 'explanation'):
        None,
    (quality.Evaluation, 'title'):
        None,
    (quality.Evaluation, 'date'):
        None,
    (quality.Evaluation, 'type'):
        None,
    (quality.Evaluation, 'description'):
        None,
    (quality.Evaluation, 'specification_hyperlink'):
        None,
    (quality.Evaluation, 'type_hyperlink'):
        None,
    (quality.Measure, 'description'):
        None,
    (quality.Measure, 'name'):
        None,
    (quality.Measure, 'identification'):
        None,
    (activity.Simulation, 'control_simulation'):
        "Points to a simulation being used as the basis (control) run.  Note that only 'derived' simulations can describe something as being control; a simulation should not know if it is being used itself as the control of some other run.",
    (activity.Simulation, 'outputs'):
        None,
    (activity.Simulation, 'deployments'):
        None,
    (activity.Simulation, 'conformances'):
        None,
    (activity.Simulation, 'simulation_id'):
        None,
    (activity.Simulation, 'authors'):
        "List of associated authors.",
    (activity.Simulation, 'spinup_simulation'):
        "The (external) simulation used during 'spinup.'  Note that this element can be used in conjuntion with spinupDateRange.  If a simulation has the latter but not the former, then one can assume that the simulation is performing its own spinup.",
    (activity.Simulation, 'restarts'):
        None,
    (activity.Simulation, 'calendar'):
        None,
    (activity.Simulation, 'inputs'):
        "Implemented as a mapping from a source to target; can be a forcing file, a boundary condition, etc.",
    (activity.Simulation, 'spinup_date_range'):
        "The date range that a simulation is engaged in spinup.",
    (activity.SpatioTemporalConstraint, 'date_range'):
        None,
    (activity.SpatioTemporalConstraint, 'spatial_resolution'):
        None,
    (activity.EnsembleMember, 'simulation'):
        None,
    (activity.EnsembleMember, 'ensemble'):
        None,
    (activity.EnsembleMember, 'ensemble_ids'):
        None,
    (activity.NumericalRequirementOption, 'description'):
        None,
    (activity.NumericalRequirementOption, 'relationship'):
        "Describes how this optional (child) requirement is related to its sibling requirements.  For example, a NumericalRequirement could consist of a set of optional requirements each with an 'OR' relationship meaning use this boundary condition _or_ that one.",
    (activity.NumericalRequirementOption, 'name'):
        None,
    (activity.NumericalRequirementOption, 'sub_options'):
        None,
    (activity.NumericalRequirementOption, 'id'):
        None,
    (activity.NumericalExperiment, 'description'):
        "A free-text description of the experiment.",
    (activity.NumericalExperiment, 'short_name'):
        "The name of the experiment (that is used internally).",
    (activity.NumericalExperiment, 'experiment_id'):
        "An experiment ID takes the form <number>.<number>[-<letter>].",
    (activity.NumericalExperiment, 'requirements'):
        "The name of the experiment (that is used internally).",
    (activity.NumericalExperiment, 'long_name'):
        "The name of the experiment (that is recognized externally).",
    (activity.NumericalExperiment, 'meta'):
        None,
    (activity.NumericalActivity, 'short_name'):
        "The name of the experiment (that is used internally).",
    (activity.NumericalActivity, 'description'):
        "A free-text description of the experiment.",
    (activity.NumericalActivity, 'supports'):
        None,
    (activity.NumericalActivity, 'long_name'):
        "The name of the experiment (that is recognized externally).",
    (activity.Experiment, 'generates'):
        None,
    (activity.Experiment, 'supports'):
        None,
    (activity.Experiment, 'measurement_campaigns'):
        None,
    (activity.Experiment, 'requires'):
        None,
    (activity.Conformance, 'type'):
        "Describes the method that this simulation conforms to an experimental requirement (in case it is not specified by the change property of the reference to the source of this conformance)",
    (activity.Conformance, 'is_conformant'):
        "Records whether or not this conformance satisfies the requirement.  A simulation should have at least one conformance mapping to every experimental requirement.  If a simulation satisfies the requirement - the usual case - then conformant should have a value of true.  If conformant is true but there is no reference to a source for the conformance, then we can assume that the simulation conforms to the requirement _naturally_, that is without having to modify code or inputs. If a simulation does not conform to a requirement then conformant should be set to false.",
    (activity.Conformance, 'requirements'):
        "Points to the NumericalRequirement that the simulation in question is conforming to.",
    (activity.Conformance, 'description'):
        None,
    (activity.Conformance, 'sources'):
        "Points to the DataSource used to conform to a particular Requirement.   This may be part of an activity::simulation or a software::component.  It can be either a DataObject or a SoftwareComponent or a ComponentProperty.  It could also be by using particular attributes of, say, a SoftwareComponent, but in that case the recommended practise is to reference the component and add appropriate text in the conformance description attribute.",
    (activity.Conformance, 'frequency'):
        None,
    (activity.SimulationRelationship, 'target'):
        None,
    (activity.SimulationRelationship, 'type'):
        None,
    (activity.MeasurementCampaign, 'duration'):
        None,
    (activity.ExperimentRelationshipTarget, 'numerical_experiment'):
        None,
    (activity.NumericalRequirement, 'requirement_type'):
        "Type of reqirement to which the experiment must conform.",
    (activity.NumericalRequirement, 'source'):
        None,
    (activity.NumericalRequirement, 'id'):
        None,
    (activity.NumericalRequirement, 'name'):
        None,
    (activity.NumericalRequirement, 'options'):
        None,
    (activity.NumericalRequirement, 'description'):
        None,
    (activity.SimulationRelationshipTarget, 'simulation'):
        None,
    (activity.SimulationRelationshipTarget, 'target'):
        None,
    (activity.SimulationComposite, 'rank'):
        "Position of a simulation in the SimulationComposite timeline. eg:  Is this the first (rank = 1) or second (rank = 2) simulation",
    (activity.SimulationComposite, 'child'):
        None,
    (activity.SimulationComposite, 'meta'):
        None,
    (activity.SimulationComposite, 'date_range'):
        None,
    (activity.SimulationRun, 'date_range'):
        None,
    (activity.SimulationRun, 'model'):
        None,
    (activity.SimulationRun, 'meta'):
        None,
    (activity.ExperimentRelationship, 'target'):
        None,
    (activity.ExperimentRelationship, 'type'):
        None,
    (activity.Activity, 'funding_sources'):
        "The entities that funded this activity.",
    (activity.Activity, 'responsible_parties'):
        "The point of contact(s) for this activity.This includes, among others, the principle investigator.",
    (activity.Activity, 'rationales'):
        "For what purpose is this activity being performed?",
    (activity.Activity, 'projects'):
        "The project(s) that this activity is associated with (ie: CMIP5, AMIP, etc).",
    (activity.Ensemble, 'members'):
        None,
    (activity.Ensemble, 'outputs'):
        "Points to the DataSource used to conform to a particular Requirement.   This may be part of an activity::simulation or a software::component.  It can be either a DataObject or a SoftwareComponent or a ComponentProperty.  It could also be by using particular attributes of, say, a SoftwareComponent, but in that case the recommended practise is to reference the component and add appropriate text in the conformance description attribute.",
    (activity.Ensemble, 'types'):
        None,
    (activity.Ensemble, 'meta'):
        None,
    (activity.DownscalingSimulation, 'meta'):
        None,
    (activity.DownscalingSimulation, 'outputs'):
        None,
    (activity.DownscalingSimulation, 'calendar'):
        None,
    (activity.DownscalingSimulation, 'downscaled_from'):
        None,
    (activity.DownscalingSimulation, 'downscaling_type'):
        None,
    (activity.DownscalingSimulation, 'downscaling_id'):
        None,
    (activity.DownscalingSimulation, 'inputs'):
        "Implemented as a mapping from a source to target; can be a forcing file, a boundary condition, etc.",
    (software.Timing, 'rate'):
        None,
    (software.Timing, 'units'):
        None,
    (software.Timing, 'start'):
        None,
    (software.Timing, 'end'):
        None,
    (software.Timing, 'is_variable_rate'):
        "Describes whether or not the model supports a variable timestep. If set to true, then rate should not be specified.",
    (software.SpatialRegriddingUserMethod, 'file'):
        None,
    (software.SpatialRegriddingUserMethod, 'name'):
        None,
    (software.Component, 'long_name'):
        "The name of the model (that is recognized externally).",
    (software.Component, 'version'):
        "A free text description of the component version #.",
    (software.Component, 'online_resource'):
        "Provides a URL location for this model.",
    (software.Component, 'parent'):
        None,
    (software.Component, 'sub_components'):
        None,
    (software.Component, 'previous_version'):
        None,
    (software.Component, 'citations'):
        None,
    (software.Component, 'properties'):
        "The properties that this model simulates and/or couples.",
    (software.Component, 'code_access'):
        "Instructions on how to access the source code for this component.",
    (software.Component, 'release_date'):
        "The date of publication of the software component code (as opposed to the date of publication of the metadata document, or the date of deployment of the model)",
    (software.Component, 'composition'):
        None,
    (software.Component, 'responsible_parties'):
        None,
    (software.Component, 'coupling_framework'):
        "The coupling framework that this entire component conforms to.",
    (software.Component, 'short_name'):
        "The name of the model (that is used internally).",
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
    (software.ComponentLanguage, 'name'):
        "The name of the language.",
    (software.ComponentLanguage, 'properties'):
        None,
    (software.Parallelisation, 'processes'):
        None,
    (software.Parallelisation, 'ranks'):
        None,
    (software.ComponentProperty, 'grid'):
        "A reference to the grid that is used by this component.",
    (software.ComponentProperty, 'values'):
        "The value of the property (not applicable to fields).",
    (software.ComponentProperty, 'is_represented'):
        "When set to false, means that this property is not used by the component. Covers the case when, for instance, a modeler chooses not to represent some property in their model. (But still allows meaningful comparisons between components which _do_ model this property.)",
    (software.ComponentProperty, 'sub_properties'):
        None,
    (software.ComponentProperty, 'intent'):
        "The direction that this property is intended to be coupled: in, out, or inout.",
    (software.ComponentProperty, 'standard_names'):
        None,
    (software.ComponentProperty, 'citations'):
        None,
    (software.ComponentProperty, 'units'):
        "The standard name that this property is known as (for example, its CF name).",
    (software.ComponentProperty, 'description'):
        None,
    (software.ComponentProperty, 'long_name'):
        None,
    (software.ComponentProperty, 'short_name'):
        None,
    (software.TimeTransformation, 'description'):
        None,
    (software.TimeTransformation, 'mapping_type'):
        None,
    (software.CouplingEndpoint, 'data_source'):
        None,
    (software.CouplingEndpoint, 'properties'):
        "A place to describe features specific to the source/target of a coupling",
    (software.CouplingEndpoint, 'instance_id'):
        "If the same datasource is used more than once in a coupled model then a method for identifying which particular instance is being referenced is needed (for BFG).",
    (software.Composition, 'couplings'):
        None,
    (software.Composition, 'description'):
        None,
    (software.ModelComponent, 'activity'):
        None,
    (software.ModelComponent, 'types'):
        "Describes the type of component. There can be multiple types.",
    (software.ModelComponent, 'type'):
        "Describes the type of component. There can be multiple types.",
    (software.ModelComponent, 'timing'):
        "Describes information about how this component simulates time.",
    (software.ModelComponent, 'meta'):
        None,
    (software.TimeLag, 'units'):
        None,
    (software.TimeLag, 'value'):
        None,
    (software.Rank, 'min'):
        None,
    (software.Rank, 'increment'):
        None,
    (software.Rank, 'value'):
        None,
    (software.Rank, 'max'):
        None,
    (software.ConnectionEndpoint, 'properties'):
        "The place to describe features specific to the source/target of a connection.",
    (software.ConnectionEndpoint, 'data_source'):
        None,
    (software.ConnectionEndpoint, 'instance_id'):
        "If the same datasource is used more than once in a coupled model then a method for identifying which particular instance is being referenced is needed (for BFG).",
    (software.StatisticalModelComponent, 'type'):
        "Describes the type of component. There can be multiple types.",
    (software.StatisticalModelComponent, 'meta'):
        None,
    (software.StatisticalModelComponent, 'types'):
        "Describes the type of component. There can be multiple types.",
    (software.StatisticalModelComponent, 'timing'):
        "Describes information about how this component simulates time.",
    (software.Coupling, 'transformers'):
        "An 'in-line' transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here.",
    (software.Coupling, 'is_fully_specified'):
        "If true then the coupling is fully-specified.  If false then not every Connection has been described within the coupling.",
    (software.Coupling, 'sources'):
        "The source component of the coupling. (note that there can be multiple sources).",
    (software.Coupling, 'spatial_regriddings'):
        "Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).",
    (software.Coupling, 'time_lag'):
        "The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time.",
    (software.Coupling, 'purpose'):
        None,
    (software.Coupling, 'description'):
        "A free-text description of the coupling.",
    (software.Coupling, 'time_transformation'):
        "Temporal transformation performed on the coupling field before or after regridding onto the target grid.",
    (software.Coupling, 'priming'):
        "A priming source is one that is active on the first available timestep only (before 'proper' coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created.",
    (software.Coupling, 'target'):
        "The target component of the coupling.",
    (software.Coupling, 'time_profile'):
        "Describes how often the coupling takes place.",
    (software.Coupling, 'type'):
        "Describes the method of coupling.",
    (software.Coupling, 'connections'):
        None,
    (software.Coupling, 'properties'):
        None,
    (software.Deployment, 'platform'):
        "The platform that this deployment has been run on. It is optional to allow for 'unconfigured' models, that nonetheless specify their parallelisation constraints (a feature needed by OASIS).",
    (software.Deployment, 'description'):
        None,
    (software.Deployment, 'deployment_date'):
        None,
    (software.Deployment, 'executable_arguments'):
        None,
    (software.Deployment, 'executable_name'):
        None,
    (software.Deployment, 'parallelisation'):
        None,
    (software.EntryPoint, 'name'):
        None,
    (software.Connection, 'properties'):
        None,
    (software.Connection, 'time_profile'):
        "All information having to do with the rate of this connection; the times that it is active.  This overrides any rate of a Coupling.",
    (software.Connection, 'time_transformation'):
        "Temporal transformation performed on the coupling field before or after regridding onto the target grid.",
    (software.Connection, 'priming'):
        "A priming source is one that is active on the first available timestep only (before 'proper' coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created.",
    (software.Connection, 'spatial_regridding'):
        "Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid)",
    (software.Connection, 'transformers'):
        "An 'in-line' transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here.",
    (software.Connection, 'target'):
        "The target property being connected.  This is optional to support the way that input is handled in the CMIP5 questionnaire.",
    (software.Connection, 'time_lag'):
        "The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time.",
    (software.Connection, 'type'):
        "The type of Connection",
    (software.Connection, 'sources'):
        "The source property being connected.  (note that there can be multiple sources)  This is optional; the file/component source may have already been specified by the couplingSource.",
    (software.Connection, 'description'):
        None,
    (software.ProcessorComponent, 'meta'):
        None,
    (software.SpatialRegridding, 'standard_method'):
        None,
    (software.SpatialRegridding, 'user_method'):
        None,
    (software.SpatialRegridding, 'dimension'):
        None,
    (software.SpatialRegridding, 'properties'):
        None,
    (data.DataExtentGeographical, 'south'):
        None,
    (data.DataExtentGeographical, 'west'):
        None,
    (data.DataExtentGeographical, 'east'):
        None,
    (data.DataExtentGeographical, 'north'):
        None,
    (data.DataDistribution, 'access'):
        None,
    (data.DataDistribution, 'format'):
        None,
    (data.DataDistribution, 'responsible_party'):
        None,
    (data.DataDistribution, 'fee'):
        None,
    (data.DataHierarchyLevel, 'value'):
        "What is the name of the specific HierarchyLevel this DataObject is being organised at (ie: if the HierarchyLevel is 'run' then the name might be the runid).",
    (data.DataHierarchyLevel, 'is_open'):
        None,
    (data.DataHierarchyLevel, 'name'):
        "What level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.",
    (data.DataStorageIp, 'protocol'):
        None,
    (data.DataStorageIp, 'path'):
        None,
    (data.DataStorageIp, 'file_name'):
        None,
    (data.DataStorageIp, 'host'):
        None,
    (data.DataContent, 'topic'):
        None,
    (data.DataContent, 'aggregation'):
        "Describes how the content has been aggregated together: sum, min, mean, max, ...",
    (data.DataContent, 'frequency'):
        "Describes the frequency of the data content: daily, hourly, ...",
    (data.DataProperty, 'description'):
        None,
    (data.DataRestriction, 'license'):
        "The thing (data or metadata, access or use) that this restriction is applied to.",
    (data.DataRestriction, 'scope'):
        "The thing (data or metadata, access or use) that this restriction is applied to.",
    (data.DataRestriction, 'restriction'):
        "The thing (data or metadata, access or use) that this restriction is applied to.",
    (data.DataObject, 'data_status'):
        None,
    (data.DataObject, 'restriction'):
        None,
    (data.DataObject, 'extent'):
        None,
    (data.DataObject, 'hierarchy_level'):
        None,
    (data.DataObject, 'distribution'):
        None,
    (data.DataObject, 'description'):
        None,
    (data.DataObject, 'source_simulation'):
        None,
    (data.DataObject, 'purpose'):
        None,
    (data.DataObject, 'parent_object'):
        None,
    (data.DataObject, 'storage'):
        None,
    (data.DataObject, 'citations'):
        None,
    (data.DataObject, 'keyword'):
        None,
    (data.DataObject, 'geometry_model'):
        None,
    (data.DataObject, 'child_object'):
        None,
    (data.DataObject, 'content'):
        "The content of a DataObject corresponds to a variable (in THREDDS, ...etc.)",
    (data.DataObject, 'properties'):
        None,
    (data.DataObject, 'acronym'):
        None,
    (data.DataObject, 'meta'):
        None,
    (data.DataStorageFile, 'file_system'):
        None,
    (data.DataStorageFile, 'file_name'):
        None,
    (data.DataStorageFile, 'path'):
        None,
    (data.DataStorage, 'size'):
        None,
    (data.DataStorage, 'format'):
        None,
    (data.DataStorage, 'modification_date'):
        None,
    (data.DataStorage, 'location'):
        None,
    (data.DataExtent, 'geographical'):
        None,
    (data.DataExtent, 'temporal'):
        None,
    (data.DataExtentTimeInterval, 'unit'):
        None,
    (data.DataExtentTimeInterval, 'factor'):
        None,
    (data.DataExtentTimeInterval, 'radix'):
        None,
    (data.DataStorageDb, 'table'):
        None,
    (data.DataStorageDb, 'access_string'):
        None,
    (data.DataStorageDb, 'owner'):
        None,
    (data.DataStorageDb, 'name'):
        None,
    (data.DataExtentTemporal, 'begin'):
        None,
    (data.DataExtentTemporal, 'time_interval'):
        None,
    (data.DataExtentTemporal, 'end'):
        None,
    (data.DataTopic, 'description'):
        None,
    (data.DataTopic, 'unit'):
        None,
    (data.DataTopic, 'name'):
        None,
    (shared.License, 'name'):
        "The name that the license goes by (ie: 'GPL')",
    (shared.License, 'contact'):
        "The point of contact for access to this artifact; may be either a person or an institution.",
    (shared.License, 'is_unrestricted'):
        "If unrestricted='true' then the artifact can be downloaded with no restrictions (ie: there are no administrative steps for the user to deal with; code or data can be downloaded and used directly).",
    (shared.License, 'description'):
        "A textual description of the license; might be the full text of the license, more likely to be a brief summary",
    (shared.Machine, 'maximum_processors'):
        None,
    (shared.Machine, 'operating_system'):
        None,
    (shared.Machine, 'vendor'):
        None,
    (shared.Machine, 'libraries'):
        "The libraries residing on this machine.",
    (shared.Machine, 'name'):
        None,
    (shared.Machine, 'processor_type'):
        None,
    (shared.Machine, 'interconnect'):
        None,
    (shared.Machine, 'cores_per_processor'):
        None,
    (shared.Machine, 'system'):
        None,
    (shared.Machine, 'description'):
        None,
    (shared.Machine, 'location'):
        None,
    (shared.Machine, 'type'):
        None,
    (shared.DataSource, 'purpose'):
        None,
    (shared.Relationship, 'description'):
        None,
    (shared.Relationship, 'direction'):
        None,
    (shared.Property, 'name'):
        None,
    (shared.Property, 'value'):
        None,
    (shared.DocGenealogy, 'relationships'):
        None,
    (shared.Standard, 'description'):
        "The version of the standard",
    (shared.Standard, 'version'):
        "The version of the standard",
    (shared.Standard, 'name'):
        "The name of the standard",
    (shared.MachineCompilerUnit, 'compilers'):
        None,
    (shared.MachineCompilerUnit, 'machine'):
        None,
    (shared.Platform, 'description'):
        None,
    (shared.Platform, 'long_name'):
        None,
    (shared.Platform, 'contacts'):
        None,
    (shared.Platform, 'short_name'):
        None,
    (shared.Platform, 'units'):
        None,
    (shared.Platform, 'meta'):
        None,
    (shared.Calendar, 'range'):
        None,
    (shared.Calendar, 'description'):
        "Describes the finer details of the calendar, in case they are not-obvious.  For example, if an experiment has changing conditions within it (ie: 1% CO2 increase until 2100, then hold fixed for the remaining period of the  experment)",
    (shared.Calendar, 'length'):
        None,
    (shared.Compiler, 'name'):
        None,
    (shared.Compiler, 'type'):
        None,
    (shared.Compiler, 'options'):
        "The set of options used during compilation (recorded here as a single string rather than separate elements)",
    (shared.Compiler, 'environment_variables'):
        "The set of environment_variables used during compilation (recorded here as a single string rather than separate elements)",
    (shared.Compiler, 'language'):
        None,
    (shared.Compiler, 'version'):
        None,
    (shared.Citation, 'location'):
        None,
    (shared.Citation, 'title'):
        None,
    (shared.Citation, 'date'):
        None,
    (shared.Citation, 'collective_title'):
        None,
    (shared.Citation, 'date_type'):
        None,
    (shared.Citation, 'type'):
        None,
    (shared.Citation, 'role'):
        None,
    (shared.Citation, 'organisation'):
        None,
    (shared.Citation, 'alternative_title'):
        None,
    (shared.ClosedDateRange, 'end'):
        "End date is optional becuase the length of a ClosedDateRange can be calculated from the StartDate plus the Duration element.",
    (shared.ClosedDateRange, 'start'):
        None,
    (shared.ResponsibleParty, 'abbreviation'):
        None,
    (shared.ResponsibleParty, 'organisation_name'):
        None,
    (shared.ResponsibleParty, 'role'):
        None,
    (shared.ResponsibleParty, 'url'):
        None,
    (shared.ResponsibleParty, 'email'):
        None,
    (shared.ResponsibleParty, 'address'):
        None,
    (shared.ResponsibleParty, 'individual_name'):
        None,
    (shared.DocMetaInfo, 'source'):
        "Application that created the instance.",
    (shared.DocMetaInfo, 'type_sort_key'):
        "Document type sort key.",
    (shared.DocMetaInfo, 'external_ids'):
        "Set of identifiers used to reference the document by external parties.",
    (shared.DocMetaInfo, 'id'):
        "Universal document identifier.",
    (shared.DocMetaInfo, 'language'):
        "Language with which instance is associated with.",
    (shared.DocMetaInfo, 'source_key'):
        "Key of application that created the instance.",
    (shared.DocMetaInfo, 'type'):
        "Document ontology type.",
    (shared.DocMetaInfo, 'genealogy'):
        "Specifies the relationship of this document with another document. Various relationship types (depending on the type of document; ie: simulation, component, etc.) are supported.",
    (shared.DocMetaInfo, 'version'):
        "Document version identifier.",
    (shared.DocMetaInfo, 'create_date'):
        "Date upon which the instance was created",
    (shared.DocMetaInfo, 'sort_key'):
        "Document sort key.",
    (shared.DocMetaInfo, 'update_date'):
        "Date upon which the instance was last updated",
    (shared.DocMetaInfo, 'drs_path'):
        "DRS related path to support documents with datasets.",
    (shared.DocMetaInfo, 'institute'):
        "Name of institute with which instance is associated with.",
    (shared.DocMetaInfo, 'project'):
        "Name of project with which instance is associated with.",
    (shared.DocMetaInfo, 'status'):
        "Document status.",
    (shared.DocMetaInfo, 'type_display_name'):
        "Document type display name.",
    (shared.DocMetaInfo, 'drs_keys'):
        "DRS related keys to support correlation of documents with datasets.",
    (shared.DocMetaInfo, 'author'):
        "Associated document author.",
    (shared.ChangeProperty, 'description'):
        "A text description of the change.  May be used in addition to, or instead of, the more formal description provided by the 'value' attribute.",
    (shared.ChangeProperty, 'id'):
        None,
    (shared.DateRange, 'duration'):
        None,
    (shared.Change, 'author'):
        "The person that made the change.",
    (shared.Change, 'name'):
        "A mnemonic for describing a particular change.",
    (shared.Change, 'type'):
        None,
    (shared.Change, 'description'):
        None,
    (shared.Change, 'date'):
        "The date the change was implemented.",
    (shared.Change, 'details'):
        None,
    (shared.StandardName, 'value'):
        None,
    (shared.StandardName, 'is_open'):
        None,
    (shared.StandardName, 'standards'):
        "Details of the standard being used.",
    (shared.DocRelationship, 'type'):
        None,
    (shared.DocRelationship, 'target'):
        None,
    (shared.OpenDateRange, 'end'):
        None,
    (shared.OpenDateRange, 'start'):
        None,
    (shared.DocRelationshipTarget, 'reference'):
        None,
    (shared.DocReference, 'description'):
        "A description of the element being referenced, in the context of the current class.",
    (shared.DocReference, 'type'):
        "The type of the element being referenced.",
    (shared.DocReference, 'external_id'):
        "A non-CIM (non-GUID) id used to reference the element in question.",
    (shared.DocReference, 'url'):
        "A URL associated witht he document reference.",
    (shared.DocReference, 'id'):
        "The ID of the element being referenced.",
    (shared.DocReference, 'version'):
        "The version of the element being referenced.",
    (shared.DocReference, 'name'):
        "The name of the element being referenced.",
    (shared.DocReference, 'changes'):
        "An optional description of how the item being referenced has been modified.  This is particularly useful for dealing with Ensembles (a set of simulations where something about each simulation has changed) or Conformances.",
    (grids.CoordinateList, 'has_constant_offset'):
        "Set to true if coordinates in the built array have constant offset.",
    (grids.CoordinateList, 'uom'):
        "Units of measure used by the coordinates.",
    (grids.CoordinateList, 'length'):
        "Specifies the length of the coordinate array. This should always be the final, as-built length of the array if the hasConstantOffset property is set to true and the compact notation (start coordinate plus offset) is used.",
    (grids.GridTile, 'is_terrain_following'):
        "Set to true if the vertical coordinate system is terrain-following even if, as is often the case, this only applies to the lower levels of the grid.",
    (grids.GridTile, 'coord_file'):
        "This property may be used to specify the URI of a file containing grid coordinates that define the geometry of a a grid tile. It is envisaged that this will be the preferred mechanism for specifying the geometry of complex grids.",
    (grids.GridTile, 'long_name'):
        None,
    (grids.GridTile, 'horizontal_crs'):
        "gml:CRSPropertyType:Specifies the horizontal coordinate reference system used in the definition of the grid tile coordinates. This property should normally be an xlink reference to an external horizontal CRS definition (e.g. in a separate CRS dictionary). If required, however, the property may be defined in situ within a CIM document.",
    (grids.GridTile, 'mnemonic'):
        None,
    (grids.GridTile, 'short_name'):
        None,
    (grids.GridTile, 'grid_north_pole'):
        "gml:PointType:If required, defines the lat-long position of the north pole used by the grid tile in the case of rotated/displaced pole grids. Not to be confused with the coordinatePole property.",
    (grids.GridTile, 'ny'):
        "Specifies the length of the Y, or latitude, dimension of the grid tile.",
    (grids.GridTile, 'nz'):
        "Specifies the length of the Z, or height/level, dimension of the grid tile. The zcoords coordinate list property, if specified, should have this length.",
    (grids.GridTile, 'vertical_crs'):
        "gml:CRSPropertyType:Specifies the vertical coordinate reference system used in the definition of the grid tile coordinates. This property should normally be an xlink reference to an external vertical CRS definition (e.g. in a separate CRS dictionary). If required, however, the property may be defined in situ within a CIM document.",
    (grids.GridTile, 'is_uniform'):
        "If true, indicates that horizontal coordinates have fixed offsets in the X and Y directions. If the offset is the same in both directions then the grids are logically square, otherwise they are logically rectangular. The offsets can be specified by two scalar values (or three values in the case of 3D grids).",
    (grids.GridTile, 'refinement_scheme'):
        None,
    (grids.GridTile, 'description'):
        "A free-text description of a grid tile.",
    (grids.GridTile, 'discretization_type'):
        "Indicates the type of discretization applied to the grid tile, e.g. 'logically_rectangular'.",
    (grids.GridTile, 'nx'):
        "Specifies the length of the X, or longitude, dimension of the grid tile.",
    (grids.GridTile, 'extent'):
        None,
    (grids.GridTile, 'vertical_resolution'):
        "Provides an indication of the approximate resolution of the grid tile in the vertical dimension. (Added to align with corresponding ESG/Curator and DIF property).",
    (grids.GridTile, 'geometry_type'):
        "Indicates the geometric figure used to approximate the figure of the Earth, e.g. 'sphere'.",
    (grids.GridTile, 'zcoords'):
        "This optional property may be used to specify the vertical coordinates (e.g. heights or model levels) at which a grid tile is utilised or realised. In the case of simple grid tiles the equivalent zcoords property on the SimpleGridGeometry data type would be used instead. The current property is intended to be used when the horizontal grid coordinates are defined by one of the other methods.",
    (grids.GridTile, 'horizontal_resolution'):
        "Provides an indication of the approximate spatial sampling size of the grid tile, i.e. the size of the underlying grid cells. (Note: the maximum spatial resolution of the grid is twice the sampling size (e.g. 2 km for a 1 km x 1 km grid pitch).",
    (grids.GridTile, 'coordinate_pole'):
        "gml:PointType:The coordinatePole property may be used to specify the lat-long position of any coordinate poles (in the mathematical sense) that form part of the definition of a grid tile. Not to be confused with the gridNorthPole property.  If required, two or more coordinate pole definitions may be distinguished by setting the gml:id attribute to appropriate values, such as spole, npole, etc.",
    (grids.GridTile, 'id'):
        "Specifies an identifer for a grid tile that is unique within its parent grid mosaic. It is not required for this identifier to be unique either across all mosaics in a GridSpec or across all GridSpecs, though if that were the case it would not be detrimental.",
    (grids.GridTile, 'area'):
        "gml:MeasureType:Specifies the area of the grid tile in the units defined by the uom attribute that is attached to the GML MeasureType data type.",
    (grids.GridTile, 'is_conformal'):
        "This property is used to indicate if the grid tile is conformal, i.e. angle-preserving. If so, angles measured on the grid are equal to the equivalent angles on the Earth.",
    (grids.GridTile, 'cell_array'):
        "GridCellArray:This property may be used to specify an array of grid cell definitions which together define the coordinate geometry of a grid tile. Depending on context, any of the existing sub-types of GridCell may be used. Mixing types is, however, not currently permitted.",
    (grids.GridTile, 'simple_grid_geom'):
        "SimpleGridGeometry:This property may be used to define the coordinates of the nodes or cells making up a simple (i.e. uniform or regular) grid tile. More details are provided in the description of the SimpleGridGeometry data type.",
    (grids.GridTile, 'is_regular'):
        "If true, indicates that the horizontal coordinates of the grid can be defined using 1D arrays (vectors). This means that grid node locations are defined by the cartesian product of the X/Lon and Y/Lat coordinate vectors. It also means that grid cells are logically rectangular (they may also be physically rectangular in the case of projected coordinates).",
    (grids.GridTile, 'cell_ref_array'):
        "GridCellArray:This property may be used to define the coordinate geometry of a grid tile by specifying an array of references to remotely defined grid cells. Depending on context, any of the existing sub-types of GridCell may be referenced.",
    (grids.SimpleGridGeometry, 'dim_order'):
        None,
    (grids.SimpleGridGeometry, 'ycoords'):
        "Y-Co-ordinates",
    (grids.SimpleGridGeometry, 'zcoords'):
        "Z-Co-ordinates",
    (grids.SimpleGridGeometry, 'num_dims'):
        None,
    (grids.SimpleGridGeometry, 'is_mesh'):
        None,
    (grids.SimpleGridGeometry, 'xcoords'):
        "X-Co-ordinates",
    (grids.GridMosaic, 'extent'):
        None,
    (grids.GridMosaic, 'mosaic_count'):
        "Specifies the number of mosaics associated with a non-leaf grid mosaic. Set to zero if the grid mosaic is a leaf mosaic, i.e. it contains child grid tiles not mosaics.",
    (grids.GridMosaic, 'mnemonic'):
        None,
    (grids.GridMosaic, 'tile_count'):
        "Specifies the number of tiles associated with a leaf grid mosaic. Set to zero if the grid mosaic is not a leaf mosaic, i.e. it contains child grid mosaics rather than tiles. (Added to align with equivalent ESG/Curator property.)",
    (grids.GridMosaic, 'type'):
        "Specifies the type of all the grid tiles contained in a grid mosaic. It is assumed that all of the tiles comprising a given grid mosaic are of the same type. The value domain is as per the specified enumeration list.",
    (grids.GridMosaic, 'has_congruent_tiles'):
        "Indicates whether or not all the tiles contained within a grid mosaic are congruent, that is, of the same size and shape.",
    (grids.GridMosaic, 'description'):
        "A free-text description of a grid mosaic.",
    (grids.GridMosaic, 'citations'):
        "Optional container element for specifying a list of references that describe the grid.",
    (grids.GridMosaic, 'mosaics'):
        None,
    (grids.GridMosaic, 'long_name'):
        "Specifies the long name associated with a grid mosaic. The long name will typically be a human-readable string, with acronyms expanded, used for labelling purposes.",
    (grids.GridMosaic, 'short_name'):
        "Specifies the short name associated with a grid mosaic. The short name will typically be a convenient abbreviation used to refer to a grid mosaic, e.g. 'UM ATM N96'.",
    (grids.GridMosaic, 'tiles'):
        None,
    (grids.GridMosaic, 'is_leaf'):
        "Indicates whether or not a grid mosaic is a leaf mosaic, that is, it only contains child grid tiles not further mosaics.",
    (grids.GridMosaic, 'id'):
        "Specifies a globally unique identifier for a grid mosaic instance. By globally we mean across all GridSpec instances/records within a given modelling activity (such as CMIP5).",
    (grids.VerticalCoordinateList, 'type'):
        "Specifies the length of the coordinate array. This should always be the final, as-built length of the array if the hasConstantOffset property is set to true and the compact notation (start coordinate plus offset) is used.",
    (grids.VerticalCoordinateList, 'form'):
        "Units of measure used by the coordinates.",
    (grids.VerticalCoordinateList, 'properties'):
        None,
    (grids.GridExtent, 'maximum_latitude'):
        None,
    (grids.GridExtent, 'units'):
        None,
    (grids.GridExtent, 'minimum_latitude'):
        None,
    (grids.GridExtent, 'minimum_longitude'):
        None,
    (grids.GridExtent, 'maximum_longitude'):
        None,
    (grids.GridSpec, 'esm_exchange_grids'):
        None,
    (grids.GridSpec, 'meta'):
        None,
    (grids.GridSpec, 'esm_model_grids'):
        None,
    (grids.GridTileResolutionType, 'description'):
        "A description of the resolution.",
    (grids.GridTileResolutionType, 'properties'):
        None,

    # ------------------------------------------------
    # Enums.
    # ------------------------------------------------

    quality.CimScopeCodeType: """
        This would cover quality issues with the CIM itself.

    """,
    quality.QualitySeverityType: """
        Creates and returns instance of quality_severity_type enum.

    """,
    quality.QualityIssueType: """
        Creates and returns instance of quality_issue_type enum.

    """,
    quality.CimResultType: """
        Creates and returns instance of cim_result_type enum.

    """,
    quality.CimFeatureType: """
        Creates and returns instance of cim_feature_type enum.

    """,
    quality.QualityStatusType: """
        Creates and returns instance of quality_status_type enum.

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
    activity.ConformanceType: """
        Creates and returns instance of conformance_type enum.

    """,
    activity.EnsembleType: """
        Creates and returns instance of ensemble_type enum.

    """,
    activity.ExperimentRelationshipType: """
        Creates and returns instance of experiment_relationship_type enum.

    """,
    activity.SimulationType: """
        Creates and returns instance of simulation_type enum.

    """,
    activity.DownscalingType: """
        Creates and returns instance of downscaling_type enum.

    """,
    activity.FrequencyType: """
        Creates and returns instance of frequency_type enum.

    """,
    software.CouplingFrameworkType: """
        Creates and returns instance of coupling_framework_type enum.

    """,
    software.ConnectionType: """
        The ConnectionType enumeration describes the mechanism of transport for a connection.

    """,
    software.TimingUnits: """
        Creates and returns instance of timing_units enum.

    """,
    software.SpatialRegriddingStandardMethodType: """
        Creates and returns instance of spatial_regridding_standard_method_type enum.

    """,
    software.TimeMappingType: """
        Enumerates the different ways that time can be mapped when transforming from one field to another.

    """,
    software.ModelComponentType: """
        An enumeration of types of ModelComponent. This includes things like atmosphere & ocean models, radiation schemes, etc. CIM best-practice is to describe every component for which there is a named ComponentType as a separate component, even if it is not a separate unit of software (ie: even if it is embedded), instead of as a (set of) ModelParameters. This codelist is synonomous with 'realm' for the purposes of CMIP5.

    """,
    software.SpatialRegriddingDimensionType: """
        Creates and returns instance of spatial_regridding_dimension_type enum.

    """,
    software.StatisticalModelComponentType: """
        An enumeration of types of ProcessorComponent.  This includes things like transformers and post-processors.

    """,
    software.ComponentPropertyIntentType: """
        The direction that the associated component property is intended to be coupled: in, out, or inout.

    """,
    data.DataStatusType: """
        Enumerates status of a data object.

    """,
    data.DataHierarchyType: """
        Enumerates the level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.

    """,
    shared.DataPurpose: """
        Purpose of the data - i.e. ancillaryFile, boundaryCondition or initialCondition.

    """,
    shared.DocRelationshipType: """
        Creates and returns instance of document_relationship_type enum.

    """,
    shared.ProcessorType: """
        A list of known cpu's.

    """,
    shared.ChangePropertyType: """
        Creates and returns instance of change_property_type enum.

    """,
    shared.OperatingSystemType: """
        A list of common operating systems.

    """,
    shared.DocType: """
        Creates and returns instance of doc_type enum.

    """,
    shared.DocStatusType: """
        Status of cim document.

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
    shared.DocRelationshipDirectionType: """
        Creates and returns instance of relationship_direction_type enum.

    """,
    shared.CompilerType: """
        Creates and returns instance of compiler_type enum.

    """,
    shared.UnitType: """
        A list of scientific units.

    """,
    grids.VerticalCsEnum: """
        Creates and returns instance of vertical_cs_enum enum.

    """,
    grids.RefinementTypeEnum: """
        Creates and returns instance of refinement_type_enum enum.

    """,
    grids.GeometryTypeEnum: """
        Creates and returns instance of geometry_type_enum enum.

    """,
    grids.DiscretizationEnum: """
        Creates and returns instance of discretization_enum enum.

    """,
    grids.FeatureTypeEnum: """
        Creates and returns instance of feature_type_enum enum.

    """,
    grids.HorizontalCsEnum: """
        Creates and returns instance of horizontal_cs_enum enum.

    """,
    grids.GridNodePositionEnum: """
        Creates and returns instance of grid_node_position_enum enum.

    """,
    grids.ArcTypeEnum: """
        Creates and returns instance of arc_type_enum enum.

    """,
    grids.GridTypeEnum: """
        Creates and returns instance of grid_type_enum enum.

    """,

    # ------------------------------------------------
    # Enum members.
    # ------------------------------------------------

    (quality.CimScopeCodeType, 'numericalRequirement'):
        None,
    (quality.CimScopeCodeType, 'dataset'):
        None,
    (quality.CimScopeCodeType, 'file'):
        None,
    (quality.CimScopeCodeType, 'service'):
        None,
    (quality.CimScopeCodeType, 'model'):
        None,
    (quality.CimScopeCodeType, 'modelComponent'):
        None,
    (quality.CimScopeCodeType, 'software'):
        None,
    (quality.CimScopeCodeType, 'simulation'):
        None,
    (quality.CimScopeCodeType, 'experiment'):
        None,
    (quality.CimScopeCodeType, 'ensemble'):
        None,
    (quality.QualitySeverityType, 'minor'):
        None,
    (quality.QualitySeverityType, 'cosmetic'):
        None,
    (quality.QualitySeverityType, 'major'):
        None,
    (quality.QualityIssueType, 'data_content'):
        None,
    (quality.QualityIssueType, 'metadata'):
        None,
    (quality.QualityIssueType, 'science'):
        None,
    (quality.QualityIssueType, 'data_format'):
        None,
    (quality.QualityIssueType, 'data_indexing'):
        None,
    (quality.CimResultType, 'document'):
        None,
    (quality.CimResultType, 'logfile'):
        None,
    (quality.CimResultType, 'plot'):
        None,
    (quality.CimFeatureType, 'diagnostic'):
        None,
    (quality.CimFeatureType, 'file'):
        None,
    (quality.QualityStatusType, 'resolved'):
        None,
    (quality.QualityStatusType, 'partially_resolved'):
        None,
    (quality.QualityStatusType, 'confirmed'):
        None,
    (quality.QualityStatusType, 'reported'):
        None,
    (activity.SimulationRelationshipType, 'lowerResolutionVersionOf'):
        None,
    (activity.SimulationRelationshipType, 'fixedVersionOf'):
        None,
    (activity.SimulationRelationshipType, 'followingSimulation'):
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
    (activity.ConformanceType, 'via model mods'):
        "Describes a simulation that conforms to an experimental requirement by changing the configuration of the software model implementing that simulation.",
    (activity.ConformanceType, 'combination'):
        "Describes a simulation that conforms to an experimental requirement by using more than one method.",
    (activity.ConformanceType, 'not-xxx'):
        None,
    (activity.ConformanceType, 'not conformant'):
        "Describes a simulation that is purpefully non-conformant to an experimental requirement.",
    (activity.ConformanceType, 'standard config'):
        "Describes a simulation that is 'naturally' conformant to an experimental requirement.",
    (activity.ConformanceType, 'via inputs'):
        "Describes a simulation that conforms to an experimental requirement by using particular inputs.",
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
    (activity.ExperimentRelationshipType, 'previousRealisation'):
        None,
    (activity.ExperimentRelationshipType, 'extensionOf'):
        None,
    (activity.ExperimentRelationshipType, 'continuationOf'):
        None,
    (activity.SimulationType, 'assimilation'):
        None,
    (activity.SimulationType, 'simulationComposite'):
        None,
    (activity.SimulationType, 'simulationRun'):
        None,
    (activity.DownscalingType, 'dynamic'):
        None,
    (activity.DownscalingType, 'statistical'):
        None,
    (software.CouplingFrameworkType, 'ESMF'):
        None,
    (software.CouplingFrameworkType, 'BFG'):
        None,
    (software.CouplingFrameworkType, 'OASIS'):
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
    (software.TimingUnits, 'seconds'):
        None,
    (software.TimingUnits, 'minutes'):
        None,
    (software.TimingUnits, 'hours'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'conservative'):
        None,
    (software.SpatialRegriddingStandardMethodType, 'non-conservative'):
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
    (software.SpatialRegriddingDimensionType, '1D'):
        None,
    (software.SpatialRegriddingDimensionType, '2D'):
        None,
    (software.SpatialRegriddingDimensionType, '3D'):
        None,
    (software.ComponentPropertyIntentType, 'in'):
        None,
    (software.ComponentPropertyIntentType, 'out'):
        None,
    (software.ComponentPropertyIntentType, 'inout'):
        None,
    (data.DataStatusType, 'metadataOnly'):
        "This DataObject is incomplete - it is described in metadata but the actual data has not yet been linked to it.",
    (data.DataStatusType, 'complete'):
        "This DataObject is complete.",
    (data.DataStatusType, 'continuouslySupplemented'):
        "This DataObject's actual data is continuously updated.",
    (shared.DataPurpose, 'boundaryCondition'):
        None,
    (shared.DataPurpose, 'ancillaryFile'):
        None,
    (shared.DataPurpose, 'initialCondition'):
        None,
    (shared.DocRelationshipType, 'similarTo'):
        None,
    (shared.DocRelationshipType, 'fixedVersionOf'):
        None,
    (shared.DocRelationshipType, 'previousVersionOf'):
        None,
    (shared.DocRelationshipType, 'other'):
        None,
    (shared.DocRelationshipType, 'laterVersionOf'):
        None,
    (shared.ChangePropertyType, 'Replacement'):
        None,
    (shared.ChangePropertyType, 'ParameterChange'):
        "A specific type of ModelMod",
    (shared.ChangePropertyType, 'ModelMod'):
        None,
    (shared.ChangePropertyType, 'CodeChange'):
        "A specific type of ModelMod",
    (shared.ChangePropertyType, 'AncillaryFile'):
        "A specific type of ModelMod",
    (shared.ChangePropertyType, 'InputMod'):
        None,
    (shared.ChangePropertyType, 'BoundaryCondition'):
        "A specific type of ModelMod",
    (shared.ChangePropertyType, 'Decrement'):
        None,
    (shared.ChangePropertyType, 'Unused'):
        None,
    (shared.ChangePropertyType, 'Increment'):
        None,
    (shared.ChangePropertyType, 'Redistribution'):
        None,
    (shared.ChangePropertyType, 'InitialCondition'):
        "A specific type of ModelMod",
    (shared.DocType, 'processorComponent'):
        None,
    (shared.DocType, 'modelComponent'):
        None,
    (shared.DocType, 'simulationComposite'):
        None,
    (shared.DocType, 'dataObject'):
        None,
    (shared.DocType, 'dataProcessing'):
        None,
    (shared.DocType, 'ensemble'):
        None,
    (shared.DocType, 'platform'):
        None,
    (shared.DocType, 'downscalingSimulation'):
        None,
    (shared.DocType, 'gridSpec'):
        None,
    (shared.DocType, 'simulationRun'):
        None,
    (shared.DocType, 'cimQuality'):
        None,
    (shared.DocType, 'assimilation'):
        None,
    (shared.DocType, 'statisticalModelComponent'):
        None,
    (shared.DocType, 'numericalExperiment'):
        None,
    (shared.DocStatusType, 'complete'):
        None,
    (shared.DocStatusType, 'incomplete'):
        None,
    (shared.DocStatusType, 'in-progress'):
        None,
    (shared.MachineType, 'Parallel'):
        None,
    (shared.MachineType, 'Beowulf'):
        None,
    (shared.MachineType, 'Vector'):
        None,
    (shared.DocRelationshipDirectionType, 'fromTarget'):
        None,
    (shared.DocRelationshipDirectionType, 'toTarget'):
        None,
    (grids.VerticalCsEnum, 'mass-based'):
        None,
    (grids.VerticalCsEnum, 'space-based'):
        None,
    (grids.RefinementTypeEnum, 'none'):
        "Tile boundaries have no refinement when the grid lines meeting at the tile boundary are continuous.",
    (grids.RefinementTypeEnum, 'integer'):
        "The refinement is integer when grid lines from the coarser grid are continuous on the finer grid, but not vice versa.",
    (grids.RefinementTypeEnum, 'rational'):
        "The refinement is rational when the adjacent or overlapping grid tiles have grid line counts that are coprime (i.e. no common factor other than 1).",
    (grids.GeometryTypeEnum, 'plane'):
        None,
    (grids.GeometryTypeEnum, 'ellipsoid'):
        None,
    (grids.GeometryTypeEnum, 'sphere'):
        None,
    (grids.DiscretizationEnum, 'unstructured_polygonal'):
        None,
    (grids.DiscretizationEnum, 'spherical_harmonics'):
        None,
    (grids.DiscretizationEnum, 'other'):
        None,
    (grids.DiscretizationEnum, 'logically_rectangular'):
        None,
    (grids.DiscretizationEnum, 'structured_triangular'):
        None,
    (grids.DiscretizationEnum, 'unstructured_triangular'):
        None,
    (grids.DiscretizationEnum, 'pixel-based_catchment'):
        None,
    (grids.FeatureTypeEnum, 'edge'):
        None,
    (grids.FeatureTypeEnum, 'point'):
        None,
    (grids.HorizontalCsEnum, 'spherical'):
        None,
    (grids.HorizontalCsEnum, 'cartesian'):
        None,
    (grids.HorizontalCsEnum, 'ellipsoidal'):
        None,
    (grids.HorizontalCsEnum, 'polar'):
        None,
    (grids.GridNodePositionEnum, 'sphere'):
        None,
    (grids.GridNodePositionEnum, 'centre'):
        None,
    (grids.GridNodePositionEnum, 'plane'):
        None,
    (grids.ArcTypeEnum, 'complex'):
        None,
    (grids.ArcTypeEnum, 'small_circle'):
        None,
    (grids.ArcTypeEnum, 'geodesic'):
        None,
    (grids.ArcTypeEnum, 'great_circle'):
        None,
    (grids.GridTypeEnum, 'composite'):
        None,
    (grids.GridTypeEnum, 'other'):
        None,
    (grids.GridTypeEnum, 'cubed_sphere'):
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
    (grids.GridTypeEnum, 'displaced_pole'):
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

    misc: "cim.1.misc",
    quality: "cim.1.quality",
    activity: "cim.1.activity",
    software: "cim.1.software",
    data: "cim.1.data",
    shared: "cim.1.shared",
    grids: "cim.1.grids",

    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    misc.DocumentSet: "cim.1.misc.DocumentSet",
    quality.CimQuality: "cim.1.quality.CimQuality",
    quality.Report: "cim.1.quality.Report",
    quality.Evaluation: "cim.1.quality.Evaluation",
    quality.Measure: "cim.1.quality.Measure",
    activity.LateralBoundaryCondition: "cim.1.activity.LateralBoundaryCondition",
    activity.Simulation: "cim.1.activity.Simulation",
    activity.SpatioTemporalConstraint: "cim.1.activity.SpatioTemporalConstraint",
    activity.EnsembleMember: "cim.1.activity.EnsembleMember",
    activity.NumericalRequirementOption: "cim.1.activity.NumericalRequirementOption",
    activity.NumericalExperiment: "cim.1.activity.NumericalExperiment",
    activity.NumericalActivity: "cim.1.activity.NumericalActivity",
    activity.Experiment: "cim.1.activity.Experiment",
    activity.Conformance: "cim.1.activity.Conformance",
    activity.OutputRequirement: "cim.1.activity.OutputRequirement",
    activity.BoundaryCondition: "cim.1.activity.BoundaryCondition",
    activity.SimulationRelationship: "cim.1.activity.SimulationRelationship",
    activity.MeasurementCampaign: "cim.1.activity.MeasurementCampaign",
    activity.ExperimentRelationshipTarget: "cim.1.activity.ExperimentRelationshipTarget",
    activity.NumericalRequirement: "cim.1.activity.NumericalRequirement",
    activity.PhysicalModification: "cim.1.activity.PhysicalModification",
    activity.SimulationRelationshipTarget: "cim.1.activity.SimulationRelationshipTarget",
    activity.SimulationComposite: "cim.1.activity.SimulationComposite",
    activity.SimulationRun: "cim.1.activity.SimulationRun",
    activity.ExperimentRelationship: "cim.1.activity.ExperimentRelationship",
    activity.Activity: "cim.1.activity.Activity",
    activity.Ensemble: "cim.1.activity.Ensemble",
    activity.DownscalingSimulation: "cim.1.activity.DownscalingSimulation",
    activity.InitialCondition: "cim.1.activity.InitialCondition",
    software.Timing: "cim.1.software.Timing",
    software.SpatialRegriddingUserMethod: "cim.1.software.SpatialRegriddingUserMethod",
    software.Component: "cim.1.software.Component",
    software.ComponentLanguage: "cim.1.software.ComponentLanguage",
    software.Parallelisation: "cim.1.software.Parallelisation",
    software.ComponentProperty: "cim.1.software.ComponentProperty",
    software.TimeTransformation: "cim.1.software.TimeTransformation",
    software.CouplingEndpoint: "cim.1.software.CouplingEndpoint",
    software.Composition: "cim.1.software.Composition",
    software.ModelComponent: "cim.1.software.ModelComponent",
    software.TimeLag: "cim.1.software.TimeLag",
    software.Rank: "cim.1.software.Rank",
    software.ConnectionEndpoint: "cim.1.software.ConnectionEndpoint",
    software.StatisticalModelComponent: "cim.1.software.StatisticalModelComponent",
    software.Coupling: "cim.1.software.Coupling",
    software.Deployment: "cim.1.software.Deployment",
    software.CouplingProperty: "cim.1.software.CouplingProperty",
    software.EntryPoint: "cim.1.software.EntryPoint",
    software.Connection: "cim.1.software.Connection",
    software.ConnectionProperty: "cim.1.software.ConnectionProperty",
    software.ProcessorComponent: "cim.1.software.ProcessorComponent",
    software.SpatialRegridding: "cim.1.software.SpatialRegridding",
    software.ComponentLanguageProperty: "cim.1.software.ComponentLanguageProperty",
    software.SpatialRegriddingProperty: "cim.1.software.SpatialRegriddingProperty",
    data.DataExtentGeographical: "cim.1.data.DataExtentGeographical",
    data.DataDistribution: "cim.1.data.DataDistribution",
    data.DataHierarchyLevel: "cim.1.data.DataHierarchyLevel",
    data.DataStorageIp: "cim.1.data.DataStorageIp",
    data.DataContent: "cim.1.data.DataContent",
    data.DataProperty: "cim.1.data.DataProperty",
    data.DataRestriction: "cim.1.data.DataRestriction",
    data.DataObject: "cim.1.data.DataObject",
    data.DataStorageFile: "cim.1.data.DataStorageFile",
    data.DataStorage: "cim.1.data.DataStorage",
    data.DataExtent: "cim.1.data.DataExtent",
    data.DataExtentTimeInterval: "cim.1.data.DataExtentTimeInterval",
    data.DataStorageDb: "cim.1.data.DataStorageDb",
    data.DataExtentTemporal: "cim.1.data.DataExtentTemporal",
    data.DataTopic: "cim.1.data.DataTopic",
    shared.License: "cim.1.shared.License",
    shared.Machine: "cim.1.shared.Machine",
    shared.PerpetualPeriod: "cim.1.shared.PerpetualPeriod",
    shared.DataSource: "cim.1.shared.DataSource",
    shared.Relationship: "cim.1.shared.Relationship",
    shared.Property: "cim.1.shared.Property",
    shared.DocGenealogy: "cim.1.shared.DocGenealogy",
    shared.Standard: "cim.1.shared.Standard",
    shared.MachineCompilerUnit: "cim.1.shared.MachineCompilerUnit",
    shared.Platform: "cim.1.shared.Platform",
    shared.Calendar: "cim.1.shared.Calendar",
    shared.Compiler: "cim.1.shared.Compiler",
    shared.Citation: "cim.1.shared.Citation",
    shared.ClosedDateRange: "cim.1.shared.ClosedDateRange",
    shared.ResponsibleParty: "cim.1.shared.ResponsibleParty",
    shared.DocMetaInfo: "cim.1.shared.DocMetaInfo",
    shared.ChangeProperty: "cim.1.shared.ChangeProperty",
    shared.Daily360: "cim.1.shared.Daily360",
    shared.DateRange: "cim.1.shared.DateRange",
    shared.Change: "cim.1.shared.Change",
    shared.StandardName: "cim.1.shared.StandardName",
    shared.DocRelationship: "cim.1.shared.DocRelationship",
    shared.OpenDateRange: "cim.1.shared.OpenDateRange",
    shared.RealCalendar: "cim.1.shared.RealCalendar",
    shared.DocRelationshipTarget: "cim.1.shared.DocRelationshipTarget",
    shared.DocReference: "cim.1.shared.DocReference",
    grids.CoordinateList: "cim.1.grids.CoordinateList",
    grids.GridProperty: "cim.1.grids.GridProperty",
    grids.GridTile: "cim.1.grids.GridTile",
    grids.SimpleGridGeometry: "cim.1.grids.SimpleGridGeometry",
    grids.GridMosaic: "cim.1.grids.GridMosaic",
    grids.VerticalCoordinateList: "cim.1.grids.VerticalCoordinateList",
    grids.GridExtent: "cim.1.grids.GridExtent",
    grids.GridSpec: "cim.1.grids.GridSpec",
    grids.GridTileResolutionType: "cim.1.grids.GridTileResolutionType",

    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------

    (misc.DocumentSet, 'ensembles'): "cim.1.misc.DocumentSet.ensembles",
    (misc.DocumentSet, 'experiment'): "cim.1.misc.DocumentSet.experiment",
    (misc.DocumentSet, 'platform'): "cim.1.misc.DocumentSet.platform",
    (misc.DocumentSet, 'data'): "cim.1.misc.DocumentSet.data",
    (misc.DocumentSet, 'grids'): "cim.1.misc.DocumentSet.grids",
    (misc.DocumentSet, 'model'): "cim.1.misc.DocumentSet.model",
    (misc.DocumentSet, 'meta'): "cim.1.misc.DocumentSet.meta",
    (misc.DocumentSet, 'simulation'): "cim.1.misc.DocumentSet.simulation",
    (quality.CimQuality, 'meta'): "cim.1.quality.CimQuality.meta",
    (quality.CimQuality, 'reports'): "cim.1.quality.CimQuality.reports",
    (quality.Report, 'date'): "cim.1.quality.Report.date",
    (quality.Report, 'measure'): "cim.1.quality.Report.measure",
    (quality.Report, 'evaluator'): "cim.1.quality.Report.evaluator",
    (quality.Report, 'evaluation'): "cim.1.quality.Report.evaluation",
    (quality.Evaluation, 'did_pass'): "cim.1.quality.Evaluation.did_pass",
    (quality.Evaluation, 'specification'): "cim.1.quality.Evaluation.specification",
    (quality.Evaluation, 'explanation'): "cim.1.quality.Evaluation.explanation",
    (quality.Evaluation, 'title'): "cim.1.quality.Evaluation.title",
    (quality.Evaluation, 'date'): "cim.1.quality.Evaluation.date",
    (quality.Evaluation, 'type'): "cim.1.quality.Evaluation.type",
    (quality.Evaluation, 'description'): "cim.1.quality.Evaluation.description",
    (quality.Evaluation, 'specification_hyperlink'): "cim.1.quality.Evaluation.specification_hyperlink",
    (quality.Evaluation, 'type_hyperlink'): "cim.1.quality.Evaluation.type_hyperlink",
    (quality.Measure, 'description'): "cim.1.quality.Measure.description",
    (quality.Measure, 'name'): "cim.1.quality.Measure.name",
    (quality.Measure, 'identification'): "cim.1.quality.Measure.identification",
    (activity.Simulation, 'control_simulation'): "cim.1.activity.Simulation.control_simulation",
    (activity.Simulation, 'outputs'): "cim.1.activity.Simulation.outputs",
    (activity.Simulation, 'deployments'): "cim.1.activity.Simulation.deployments",
    (activity.Simulation, 'conformances'): "cim.1.activity.Simulation.conformances",
    (activity.Simulation, 'simulation_id'): "cim.1.activity.Simulation.simulation_id",
    (activity.Simulation, 'authors'): "cim.1.activity.Simulation.authors",
    (activity.Simulation, 'spinup_simulation'): "cim.1.activity.Simulation.spinup_simulation",
    (activity.Simulation, 'restarts'): "cim.1.activity.Simulation.restarts",
    (activity.Simulation, 'calendar'): "cim.1.activity.Simulation.calendar",
    (activity.Simulation, 'inputs'): "cim.1.activity.Simulation.inputs",
    (activity.Simulation, 'spinup_date_range'): "cim.1.activity.Simulation.spinup_date_range",
    (activity.SpatioTemporalConstraint, 'date_range'): "cim.1.activity.SpatioTemporalConstraint.date_range",
    (activity.SpatioTemporalConstraint, 'spatial_resolution'): "cim.1.activity.SpatioTemporalConstraint.spatial_resolution",
    (activity.EnsembleMember, 'simulation'): "cim.1.activity.EnsembleMember.simulation",
    (activity.EnsembleMember, 'ensemble'): "cim.1.activity.EnsembleMember.ensemble",
    (activity.EnsembleMember, 'ensemble_ids'): "cim.1.activity.EnsembleMember.ensemble_ids",
    (activity.NumericalRequirementOption, 'description'): "cim.1.activity.NumericalRequirementOption.description",
    (activity.NumericalRequirementOption, 'relationship'): "cim.1.activity.NumericalRequirementOption.relationship",
    (activity.NumericalRequirementOption, 'name'): "cim.1.activity.NumericalRequirementOption.name",
    (activity.NumericalRequirementOption, 'sub_options'): "cim.1.activity.NumericalRequirementOption.sub_options",
    (activity.NumericalRequirementOption, 'id'): "cim.1.activity.NumericalRequirementOption.id",
    (activity.NumericalExperiment, 'description'): "cim.1.activity.NumericalExperiment.description",
    (activity.NumericalExperiment, 'short_name'): "cim.1.activity.NumericalExperiment.short_name",
    (activity.NumericalExperiment, 'experiment_id'): "cim.1.activity.NumericalExperiment.experiment_id",
    (activity.NumericalExperiment, 'requirements'): "cim.1.activity.NumericalExperiment.requirements",
    (activity.NumericalExperiment, 'long_name'): "cim.1.activity.NumericalExperiment.long_name",
    (activity.NumericalExperiment, 'meta'): "cim.1.activity.NumericalExperiment.meta",
    (activity.NumericalActivity, 'short_name'): "cim.1.activity.NumericalActivity.short_name",
    (activity.NumericalActivity, 'description'): "cim.1.activity.NumericalActivity.description",
    (activity.NumericalActivity, 'supports'): "cim.1.activity.NumericalActivity.supports",
    (activity.NumericalActivity, 'long_name'): "cim.1.activity.NumericalActivity.long_name",
    (activity.Experiment, 'generates'): "cim.1.activity.Experiment.generates",
    (activity.Experiment, 'supports'): "cim.1.activity.Experiment.supports",
    (activity.Experiment, 'measurement_campaigns'): "cim.1.activity.Experiment.measurement_campaigns",
    (activity.Experiment, 'requires'): "cim.1.activity.Experiment.requires",
    (activity.Conformance, 'type'): "cim.1.activity.Conformance.type",
    (activity.Conformance, 'is_conformant'): "cim.1.activity.Conformance.is_conformant",
    (activity.Conformance, 'requirements'): "cim.1.activity.Conformance.requirements",
    (activity.Conformance, 'description'): "cim.1.activity.Conformance.description",
    (activity.Conformance, 'sources'): "cim.1.activity.Conformance.sources",
    (activity.Conformance, 'frequency'): "cim.1.activity.Conformance.frequency",
    (activity.SimulationRelationship, 'target'): "cim.1.activity.SimulationRelationship.target",
    (activity.SimulationRelationship, 'type'): "cim.1.activity.SimulationRelationship.type",
    (activity.MeasurementCampaign, 'duration'): "cim.1.activity.MeasurementCampaign.duration",
    (activity.ExperimentRelationshipTarget, 'numerical_experiment'): "cim.1.activity.ExperimentRelationshipTarget.numerical_experiment",
    (activity.NumericalRequirement, 'requirement_type'): "cim.1.activity.NumericalRequirement.requirement_type",
    (activity.NumericalRequirement, 'source'): "cim.1.activity.NumericalRequirement.source",
    (activity.NumericalRequirement, 'id'): "cim.1.activity.NumericalRequirement.id",
    (activity.NumericalRequirement, 'name'): "cim.1.activity.NumericalRequirement.name",
    (activity.NumericalRequirement, 'options'): "cim.1.activity.NumericalRequirement.options",
    (activity.NumericalRequirement, 'description'): "cim.1.activity.NumericalRequirement.description",
    (activity.SimulationRelationshipTarget, 'simulation'): "cim.1.activity.SimulationRelationshipTarget.simulation",
    (activity.SimulationRelationshipTarget, 'target'): "cim.1.activity.SimulationRelationshipTarget.target",
    (activity.SimulationComposite, 'rank'): "cim.1.activity.SimulationComposite.rank",
    (activity.SimulationComposite, 'child'): "cim.1.activity.SimulationComposite.child",
    (activity.SimulationComposite, 'meta'): "cim.1.activity.SimulationComposite.meta",
    (activity.SimulationComposite, 'date_range'): "cim.1.activity.SimulationComposite.date_range",
    (activity.SimulationRun, 'date_range'): "cim.1.activity.SimulationRun.date_range",
    (activity.SimulationRun, 'model'): "cim.1.activity.SimulationRun.model",
    (activity.SimulationRun, 'meta'): "cim.1.activity.SimulationRun.meta",
    (activity.ExperimentRelationship, 'target'): "cim.1.activity.ExperimentRelationship.target",
    (activity.ExperimentRelationship, 'type'): "cim.1.activity.ExperimentRelationship.type",
    (activity.Activity, 'funding_sources'): "cim.1.activity.Activity.funding_sources",
    (activity.Activity, 'responsible_parties'): "cim.1.activity.Activity.responsible_parties",
    (activity.Activity, 'rationales'): "cim.1.activity.Activity.rationales",
    (activity.Activity, 'projects'): "cim.1.activity.Activity.projects",
    (activity.Ensemble, 'members'): "cim.1.activity.Ensemble.members",
    (activity.Ensemble, 'outputs'): "cim.1.activity.Ensemble.outputs",
    (activity.Ensemble, 'types'): "cim.1.activity.Ensemble.types",
    (activity.Ensemble, 'meta'): "cim.1.activity.Ensemble.meta",
    (activity.DownscalingSimulation, 'meta'): "cim.1.activity.DownscalingSimulation.meta",
    (activity.DownscalingSimulation, 'outputs'): "cim.1.activity.DownscalingSimulation.outputs",
    (activity.DownscalingSimulation, 'calendar'): "cim.1.activity.DownscalingSimulation.calendar",
    (activity.DownscalingSimulation, 'downscaled_from'): "cim.1.activity.DownscalingSimulation.downscaled_from",
    (activity.DownscalingSimulation, 'downscaling_type'): "cim.1.activity.DownscalingSimulation.downscaling_type",
    (activity.DownscalingSimulation, 'downscaling_id'): "cim.1.activity.DownscalingSimulation.downscaling_id",
    (activity.DownscalingSimulation, 'inputs'): "cim.1.activity.DownscalingSimulation.inputs",
    (software.Timing, 'rate'): "cim.1.software.Timing.rate",
    (software.Timing, 'units'): "cim.1.software.Timing.units",
    (software.Timing, 'start'): "cim.1.software.Timing.start",
    (software.Timing, 'end'): "cim.1.software.Timing.end",
    (software.Timing, 'is_variable_rate'): "cim.1.software.Timing.is_variable_rate",
    (software.SpatialRegriddingUserMethod, 'file'): "cim.1.software.SpatialRegriddingUserMethod.file",
    (software.SpatialRegriddingUserMethod, 'name'): "cim.1.software.SpatialRegriddingUserMethod.name",
    (software.Component, 'long_name'): "cim.1.software.Component.long_name",
    (software.Component, 'version'): "cim.1.software.Component.version",
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
    (software.Component, 'dependencies'): "cim.1.software.Component.dependencies",
    (software.Component, 'deployments'): "cim.1.software.Component.deployments",
    (software.Component, 'description'): "cim.1.software.Component.description",
    (software.Component, 'funding_sources'): "cim.1.software.Component.funding_sources",
    (software.Component, 'grid'): "cim.1.software.Component.grid",
    (software.Component, 'is_embedded'): "cim.1.software.Component.is_embedded",
    (software.Component, 'language'): "cim.1.software.Component.language",
    (software.Component, 'license'): "cim.1.software.Component.license",
    (software.ComponentLanguage, 'name'): "cim.1.software.ComponentLanguage.name",
    (software.ComponentLanguage, 'properties'): "cim.1.software.ComponentLanguage.properties",
    (software.Parallelisation, 'processes'): "cim.1.software.Parallelisation.processes",
    (software.Parallelisation, 'ranks'): "cim.1.software.Parallelisation.ranks",
    (software.ComponentProperty, 'grid'): "cim.1.software.ComponentProperty.grid",
    (software.ComponentProperty, 'values'): "cim.1.software.ComponentProperty.values",
    (software.ComponentProperty, 'is_represented'): "cim.1.software.ComponentProperty.is_represented",
    (software.ComponentProperty, 'sub_properties'): "cim.1.software.ComponentProperty.sub_properties",
    (software.ComponentProperty, 'intent'): "cim.1.software.ComponentProperty.intent",
    (software.ComponentProperty, 'standard_names'): "cim.1.software.ComponentProperty.standard_names",
    (software.ComponentProperty, 'citations'): "cim.1.software.ComponentProperty.citations",
    (software.ComponentProperty, 'units'): "cim.1.software.ComponentProperty.units",
    (software.ComponentProperty, 'description'): "cim.1.software.ComponentProperty.description",
    (software.ComponentProperty, 'long_name'): "cim.1.software.ComponentProperty.long_name",
    (software.ComponentProperty, 'short_name'): "cim.1.software.ComponentProperty.short_name",
    (software.TimeTransformation, 'description'): "cim.1.software.TimeTransformation.description",
    (software.TimeTransformation, 'mapping_type'): "cim.1.software.TimeTransformation.mapping_type",
    (software.CouplingEndpoint, 'data_source'): "cim.1.software.CouplingEndpoint.data_source",
    (software.CouplingEndpoint, 'properties'): "cim.1.software.CouplingEndpoint.properties",
    (software.CouplingEndpoint, 'instance_id'): "cim.1.software.CouplingEndpoint.instance_id",
    (software.Composition, 'couplings'): "cim.1.software.Composition.couplings",
    (software.Composition, 'description'): "cim.1.software.Composition.description",
    (software.ModelComponent, 'activity'): "cim.1.software.ModelComponent.activity",
    (software.ModelComponent, 'types'): "cim.1.software.ModelComponent.types",
    (software.ModelComponent, 'type'): "cim.1.software.ModelComponent.type",
    (software.ModelComponent, 'timing'): "cim.1.software.ModelComponent.timing",
    (software.ModelComponent, 'meta'): "cim.1.software.ModelComponent.meta",
    (software.TimeLag, 'units'): "cim.1.software.TimeLag.units",
    (software.TimeLag, 'value'): "cim.1.software.TimeLag.value",
    (software.Rank, 'min'): "cim.1.software.Rank.min",
    (software.Rank, 'increment'): "cim.1.software.Rank.increment",
    (software.Rank, 'value'): "cim.1.software.Rank.value",
    (software.Rank, 'max'): "cim.1.software.Rank.max",
    (software.ConnectionEndpoint, 'properties'): "cim.1.software.ConnectionEndpoint.properties",
    (software.ConnectionEndpoint, 'data_source'): "cim.1.software.ConnectionEndpoint.data_source",
    (software.ConnectionEndpoint, 'instance_id'): "cim.1.software.ConnectionEndpoint.instance_id",
    (software.StatisticalModelComponent, 'type'): "cim.1.software.StatisticalModelComponent.type",
    (software.StatisticalModelComponent, 'meta'): "cim.1.software.StatisticalModelComponent.meta",
    (software.StatisticalModelComponent, 'types'): "cim.1.software.StatisticalModelComponent.types",
    (software.StatisticalModelComponent, 'timing'): "cim.1.software.StatisticalModelComponent.timing",
    (software.Coupling, 'transformers'): "cim.1.software.Coupling.transformers",
    (software.Coupling, 'is_fully_specified'): "cim.1.software.Coupling.is_fully_specified",
    (software.Coupling, 'sources'): "cim.1.software.Coupling.sources",
    (software.Coupling, 'spatial_regriddings'): "cim.1.software.Coupling.spatial_regriddings",
    (software.Coupling, 'time_lag'): "cim.1.software.Coupling.time_lag",
    (software.Coupling, 'purpose'): "cim.1.software.Coupling.purpose",
    (software.Coupling, 'description'): "cim.1.software.Coupling.description",
    (software.Coupling, 'time_transformation'): "cim.1.software.Coupling.time_transformation",
    (software.Coupling, 'priming'): "cim.1.software.Coupling.priming",
    (software.Coupling, 'target'): "cim.1.software.Coupling.target",
    (software.Coupling, 'time_profile'): "cim.1.software.Coupling.time_profile",
    (software.Coupling, 'type'): "cim.1.software.Coupling.type",
    (software.Coupling, 'connections'): "cim.1.software.Coupling.connections",
    (software.Coupling, 'properties'): "cim.1.software.Coupling.properties",
    (software.Deployment, 'platform'): "cim.1.software.Deployment.platform",
    (software.Deployment, 'description'): "cim.1.software.Deployment.description",
    (software.Deployment, 'deployment_date'): "cim.1.software.Deployment.deployment_date",
    (software.Deployment, 'executable_arguments'): "cim.1.software.Deployment.executable_arguments",
    (software.Deployment, 'executable_name'): "cim.1.software.Deployment.executable_name",
    (software.Deployment, 'parallelisation'): "cim.1.software.Deployment.parallelisation",
    (software.EntryPoint, 'name'): "cim.1.software.EntryPoint.name",
    (software.Connection, 'properties'): "cim.1.software.Connection.properties",
    (software.Connection, 'time_profile'): "cim.1.software.Connection.time_profile",
    (software.Connection, 'time_transformation'): "cim.1.software.Connection.time_transformation",
    (software.Connection, 'priming'): "cim.1.software.Connection.priming",
    (software.Connection, 'spatial_regridding'): "cim.1.software.Connection.spatial_regridding",
    (software.Connection, 'transformers'): "cim.1.software.Connection.transformers",
    (software.Connection, 'target'): "cim.1.software.Connection.target",
    (software.Connection, 'time_lag'): "cim.1.software.Connection.time_lag",
    (software.Connection, 'type'): "cim.1.software.Connection.type",
    (software.Connection, 'sources'): "cim.1.software.Connection.sources",
    (software.Connection, 'description'): "cim.1.software.Connection.description",
    (software.ProcessorComponent, 'meta'): "cim.1.software.ProcessorComponent.meta",
    (software.SpatialRegridding, 'standard_method'): "cim.1.software.SpatialRegridding.standard_method",
    (software.SpatialRegridding, 'user_method'): "cim.1.software.SpatialRegridding.user_method",
    (software.SpatialRegridding, 'dimension'): "cim.1.software.SpatialRegridding.dimension",
    (software.SpatialRegridding, 'properties'): "cim.1.software.SpatialRegridding.properties",
    (data.DataExtentGeographical, 'south'): "cim.1.data.DataExtentGeographical.south",
    (data.DataExtentGeographical, 'west'): "cim.1.data.DataExtentGeographical.west",
    (data.DataExtentGeographical, 'east'): "cim.1.data.DataExtentGeographical.east",
    (data.DataExtentGeographical, 'north'): "cim.1.data.DataExtentGeographical.north",
    (data.DataDistribution, 'access'): "cim.1.data.DataDistribution.access",
    (data.DataDistribution, 'format'): "cim.1.data.DataDistribution.format",
    (data.DataDistribution, 'responsible_party'): "cim.1.data.DataDistribution.responsible_party",
    (data.DataDistribution, 'fee'): "cim.1.data.DataDistribution.fee",
    (data.DataHierarchyLevel, 'value'): "cim.1.data.DataHierarchyLevel.value",
    (data.DataHierarchyLevel, 'is_open'): "cim.1.data.DataHierarchyLevel.is_open",
    (data.DataHierarchyLevel, 'name'): "cim.1.data.DataHierarchyLevel.name",
    (data.DataStorageIp, 'protocol'): "cim.1.data.DataStorageIp.protocol",
    (data.DataStorageIp, 'path'): "cim.1.data.DataStorageIp.path",
    (data.DataStorageIp, 'file_name'): "cim.1.data.DataStorageIp.file_name",
    (data.DataStorageIp, 'host'): "cim.1.data.DataStorageIp.host",
    (data.DataContent, 'topic'): "cim.1.data.DataContent.topic",
    (data.DataContent, 'aggregation'): "cim.1.data.DataContent.aggregation",
    (data.DataContent, 'frequency'): "cim.1.data.DataContent.frequency",
    (data.DataProperty, 'description'): "cim.1.data.DataProperty.description",
    (data.DataRestriction, 'license'): "cim.1.data.DataRestriction.license",
    (data.DataRestriction, 'scope'): "cim.1.data.DataRestriction.scope",
    (data.DataRestriction, 'restriction'): "cim.1.data.DataRestriction.restriction",
    (data.DataObject, 'data_status'): "cim.1.data.DataObject.data_status",
    (data.DataObject, 'restriction'): "cim.1.data.DataObject.restriction",
    (data.DataObject, 'extent'): "cim.1.data.DataObject.extent",
    (data.DataObject, 'hierarchy_level'): "cim.1.data.DataObject.hierarchy_level",
    (data.DataObject, 'distribution'): "cim.1.data.DataObject.distribution",
    (data.DataObject, 'description'): "cim.1.data.DataObject.description",
    (data.DataObject, 'source_simulation'): "cim.1.data.DataObject.source_simulation",
    (data.DataObject, 'purpose'): "cim.1.data.DataObject.purpose",
    (data.DataObject, 'parent_object'): "cim.1.data.DataObject.parent_object",
    (data.DataObject, 'storage'): "cim.1.data.DataObject.storage",
    (data.DataObject, 'citations'): "cim.1.data.DataObject.citations",
    (data.DataObject, 'keyword'): "cim.1.data.DataObject.keyword",
    (data.DataObject, 'geometry_model'): "cim.1.data.DataObject.geometry_model",
    (data.DataObject, 'child_object'): "cim.1.data.DataObject.child_object",
    (data.DataObject, 'content'): "cim.1.data.DataObject.content",
    (data.DataObject, 'properties'): "cim.1.data.DataObject.properties",
    (data.DataObject, 'acronym'): "cim.1.data.DataObject.acronym",
    (data.DataObject, 'meta'): "cim.1.data.DataObject.meta",
    (data.DataStorageFile, 'file_system'): "cim.1.data.DataStorageFile.file_system",
    (data.DataStorageFile, 'file_name'): "cim.1.data.DataStorageFile.file_name",
    (data.DataStorageFile, 'path'): "cim.1.data.DataStorageFile.path",
    (data.DataStorage, 'size'): "cim.1.data.DataStorage.size",
    (data.DataStorage, 'format'): "cim.1.data.DataStorage.format",
    (data.DataStorage, 'modification_date'): "cim.1.data.DataStorage.modification_date",
    (data.DataStorage, 'location'): "cim.1.data.DataStorage.location",
    (data.DataExtent, 'geographical'): "cim.1.data.DataExtent.geographical",
    (data.DataExtent, 'temporal'): "cim.1.data.DataExtent.temporal",
    (data.DataExtentTimeInterval, 'unit'): "cim.1.data.DataExtentTimeInterval.unit",
    (data.DataExtentTimeInterval, 'factor'): "cim.1.data.DataExtentTimeInterval.factor",
    (data.DataExtentTimeInterval, 'radix'): "cim.1.data.DataExtentTimeInterval.radix",
    (data.DataStorageDb, 'table'): "cim.1.data.DataStorageDb.table",
    (data.DataStorageDb, 'access_string'): "cim.1.data.DataStorageDb.access_string",
    (data.DataStorageDb, 'owner'): "cim.1.data.DataStorageDb.owner",
    (data.DataStorageDb, 'name'): "cim.1.data.DataStorageDb.name",
    (data.DataExtentTemporal, 'begin'): "cim.1.data.DataExtentTemporal.begin",
    (data.DataExtentTemporal, 'time_interval'): "cim.1.data.DataExtentTemporal.time_interval",
    (data.DataExtentTemporal, 'end'): "cim.1.data.DataExtentTemporal.end",
    (data.DataTopic, 'description'): "cim.1.data.DataTopic.description",
    (data.DataTopic, 'unit'): "cim.1.data.DataTopic.unit",
    (data.DataTopic, 'name'): "cim.1.data.DataTopic.name",
    (shared.License, 'name'): "cim.1.shared.License.name",
    (shared.License, 'contact'): "cim.1.shared.License.contact",
    (shared.License, 'is_unrestricted'): "cim.1.shared.License.is_unrestricted",
    (shared.License, 'description'): "cim.1.shared.License.description",
    (shared.Machine, 'maximum_processors'): "cim.1.shared.Machine.maximum_processors",
    (shared.Machine, 'operating_system'): "cim.1.shared.Machine.operating_system",
    (shared.Machine, 'vendor'): "cim.1.shared.Machine.vendor",
    (shared.Machine, 'libraries'): "cim.1.shared.Machine.libraries",
    (shared.Machine, 'name'): "cim.1.shared.Machine.name",
    (shared.Machine, 'processor_type'): "cim.1.shared.Machine.processor_type",
    (shared.Machine, 'interconnect'): "cim.1.shared.Machine.interconnect",
    (shared.Machine, 'cores_per_processor'): "cim.1.shared.Machine.cores_per_processor",
    (shared.Machine, 'system'): "cim.1.shared.Machine.system",
    (shared.Machine, 'description'): "cim.1.shared.Machine.description",
    (shared.Machine, 'location'): "cim.1.shared.Machine.location",
    (shared.Machine, 'type'): "cim.1.shared.Machine.type",
    (shared.DataSource, 'purpose'): "cim.1.shared.DataSource.purpose",
    (shared.Relationship, 'description'): "cim.1.shared.Relationship.description",
    (shared.Relationship, 'direction'): "cim.1.shared.Relationship.direction",
    (shared.Property, 'name'): "cim.1.shared.Property.name",
    (shared.Property, 'value'): "cim.1.shared.Property.value",
    (shared.DocGenealogy, 'relationships'): "cim.1.shared.DocGenealogy.relationships",
    (shared.Standard, 'description'): "cim.1.shared.Standard.description",
    (shared.Standard, 'version'): "cim.1.shared.Standard.version",
    (shared.Standard, 'name'): "cim.1.shared.Standard.name",
    (shared.MachineCompilerUnit, 'compilers'): "cim.1.shared.MachineCompilerUnit.compilers",
    (shared.MachineCompilerUnit, 'machine'): "cim.1.shared.MachineCompilerUnit.machine",
    (shared.Platform, 'description'): "cim.1.shared.Platform.description",
    (shared.Platform, 'long_name'): "cim.1.shared.Platform.long_name",
    (shared.Platform, 'contacts'): "cim.1.shared.Platform.contacts",
    (shared.Platform, 'short_name'): "cim.1.shared.Platform.short_name",
    (shared.Platform, 'units'): "cim.1.shared.Platform.units",
    (shared.Platform, 'meta'): "cim.1.shared.Platform.meta",
    (shared.Calendar, 'range'): "cim.1.shared.Calendar.range",
    (shared.Calendar, 'description'): "cim.1.shared.Calendar.description",
    (shared.Calendar, 'length'): "cim.1.shared.Calendar.length",
    (shared.Compiler, 'name'): "cim.1.shared.Compiler.name",
    (shared.Compiler, 'type'): "cim.1.shared.Compiler.type",
    (shared.Compiler, 'options'): "cim.1.shared.Compiler.options",
    (shared.Compiler, 'environment_variables'): "cim.1.shared.Compiler.environment_variables",
    (shared.Compiler, 'language'): "cim.1.shared.Compiler.language",
    (shared.Compiler, 'version'): "cim.1.shared.Compiler.version",
    (shared.Citation, 'location'): "cim.1.shared.Citation.location",
    (shared.Citation, 'title'): "cim.1.shared.Citation.title",
    (shared.Citation, 'date'): "cim.1.shared.Citation.date",
    (shared.Citation, 'collective_title'): "cim.1.shared.Citation.collective_title",
    (shared.Citation, 'date_type'): "cim.1.shared.Citation.date_type",
    (shared.Citation, 'type'): "cim.1.shared.Citation.type",
    (shared.Citation, 'role'): "cim.1.shared.Citation.role",
    (shared.Citation, 'organisation'): "cim.1.shared.Citation.organisation",
    (shared.Citation, 'alternative_title'): "cim.1.shared.Citation.alternative_title",
    (shared.ClosedDateRange, 'end'): "cim.1.shared.ClosedDateRange.end",
    (shared.ClosedDateRange, 'start'): "cim.1.shared.ClosedDateRange.start",
    (shared.ResponsibleParty, 'abbreviation'): "cim.1.shared.ResponsibleParty.abbreviation",
    (shared.ResponsibleParty, 'organisation_name'): "cim.1.shared.ResponsibleParty.organisation_name",
    (shared.ResponsibleParty, 'role'): "cim.1.shared.ResponsibleParty.role",
    (shared.ResponsibleParty, 'url'): "cim.1.shared.ResponsibleParty.url",
    (shared.ResponsibleParty, 'email'): "cim.1.shared.ResponsibleParty.email",
    (shared.ResponsibleParty, 'address'): "cim.1.shared.ResponsibleParty.address",
    (shared.ResponsibleParty, 'individual_name'): "cim.1.shared.ResponsibleParty.individual_name",
    (shared.DocMetaInfo, 'source'): "cim.1.shared.DocMetaInfo.source",
    (shared.DocMetaInfo, 'type_sort_key'): "cim.1.shared.DocMetaInfo.type_sort_key",
    (shared.DocMetaInfo, 'external_ids'): "cim.1.shared.DocMetaInfo.external_ids",
    (shared.DocMetaInfo, 'id'): "cim.1.shared.DocMetaInfo.id",
    (shared.DocMetaInfo, 'language'): "cim.1.shared.DocMetaInfo.language",
    (shared.DocMetaInfo, 'source_key'): "cim.1.shared.DocMetaInfo.source_key",
    (shared.DocMetaInfo, 'type'): "cim.1.shared.DocMetaInfo.type",
    (shared.DocMetaInfo, 'genealogy'): "cim.1.shared.DocMetaInfo.genealogy",
    (shared.DocMetaInfo, 'version'): "cim.1.shared.DocMetaInfo.version",
    (shared.DocMetaInfo, 'create_date'): "cim.1.shared.DocMetaInfo.create_date",
    (shared.DocMetaInfo, 'sort_key'): "cim.1.shared.DocMetaInfo.sort_key",
    (shared.DocMetaInfo, 'update_date'): "cim.1.shared.DocMetaInfo.update_date",
    (shared.DocMetaInfo, 'drs_path'): "cim.1.shared.DocMetaInfo.drs_path",
    (shared.DocMetaInfo, 'institute'): "cim.1.shared.DocMetaInfo.institute",
    (shared.DocMetaInfo, 'project'): "cim.1.shared.DocMetaInfo.project",
    (shared.DocMetaInfo, 'status'): "cim.1.shared.DocMetaInfo.status",
    (shared.DocMetaInfo, 'type_display_name'): "cim.1.shared.DocMetaInfo.type_display_name",
    (shared.DocMetaInfo, 'drs_keys'): "cim.1.shared.DocMetaInfo.drs_keys",
    (shared.DocMetaInfo, 'author'): "cim.1.shared.DocMetaInfo.author",
    (shared.ChangeProperty, 'description'): "cim.1.shared.ChangeProperty.description",
    (shared.ChangeProperty, 'id'): "cim.1.shared.ChangeProperty.id",
    (shared.DateRange, 'duration'): "cim.1.shared.DateRange.duration",
    (shared.Change, 'author'): "cim.1.shared.Change.author",
    (shared.Change, 'name'): "cim.1.shared.Change.name",
    (shared.Change, 'type'): "cim.1.shared.Change.type",
    (shared.Change, 'description'): "cim.1.shared.Change.description",
    (shared.Change, 'date'): "cim.1.shared.Change.date",
    (shared.Change, 'details'): "cim.1.shared.Change.details",
    (shared.StandardName, 'value'): "cim.1.shared.StandardName.value",
    (shared.StandardName, 'is_open'): "cim.1.shared.StandardName.is_open",
    (shared.StandardName, 'standards'): "cim.1.shared.StandardName.standards",
    (shared.DocRelationship, 'type'): "cim.1.shared.DocRelationship.type",
    (shared.DocRelationship, 'target'): "cim.1.shared.DocRelationship.target",
    (shared.OpenDateRange, 'end'): "cim.1.shared.OpenDateRange.end",
    (shared.OpenDateRange, 'start'): "cim.1.shared.OpenDateRange.start",
    (shared.DocRelationshipTarget, 'reference'): "cim.1.shared.DocRelationshipTarget.reference",
    (shared.DocReference, 'description'): "cim.1.shared.DocReference.description",
    (shared.DocReference, 'type'): "cim.1.shared.DocReference.type",
    (shared.DocReference, 'external_id'): "cim.1.shared.DocReference.external_id",
    (shared.DocReference, 'url'): "cim.1.shared.DocReference.url",
    (shared.DocReference, 'id'): "cim.1.shared.DocReference.id",
    (shared.DocReference, 'version'): "cim.1.shared.DocReference.version",
    (shared.DocReference, 'name'): "cim.1.shared.DocReference.name",
    (shared.DocReference, 'changes'): "cim.1.shared.DocReference.changes",
    (grids.CoordinateList, 'has_constant_offset'): "cim.1.grids.CoordinateList.has_constant_offset",
    (grids.CoordinateList, 'uom'): "cim.1.grids.CoordinateList.uom",
    (grids.CoordinateList, 'length'): "cim.1.grids.CoordinateList.length",
    (grids.GridTile, 'is_terrain_following'): "cim.1.grids.GridTile.is_terrain_following",
    (grids.GridTile, 'coord_file'): "cim.1.grids.GridTile.coord_file",
    (grids.GridTile, 'long_name'): "cim.1.grids.GridTile.long_name",
    (grids.GridTile, 'horizontal_crs'): "cim.1.grids.GridTile.horizontal_crs",
    (grids.GridTile, 'mnemonic'): "cim.1.grids.GridTile.mnemonic",
    (grids.GridTile, 'short_name'): "cim.1.grids.GridTile.short_name",
    (grids.GridTile, 'grid_north_pole'): "cim.1.grids.GridTile.grid_north_pole",
    (grids.GridTile, 'ny'): "cim.1.grids.GridTile.ny",
    (grids.GridTile, 'nz'): "cim.1.grids.GridTile.nz",
    (grids.GridTile, 'vertical_crs'): "cim.1.grids.GridTile.vertical_crs",
    (grids.GridTile, 'is_uniform'): "cim.1.grids.GridTile.is_uniform",
    (grids.GridTile, 'refinement_scheme'): "cim.1.grids.GridTile.refinement_scheme",
    (grids.GridTile, 'description'): "cim.1.grids.GridTile.description",
    (grids.GridTile, 'discretization_type'): "cim.1.grids.GridTile.discretization_type",
    (grids.GridTile, 'nx'): "cim.1.grids.GridTile.nx",
    (grids.GridTile, 'extent'): "cim.1.grids.GridTile.extent",
    (grids.GridTile, 'vertical_resolution'): "cim.1.grids.GridTile.vertical_resolution",
    (grids.GridTile, 'geometry_type'): "cim.1.grids.GridTile.geometry_type",
    (grids.GridTile, 'zcoords'): "cim.1.grids.GridTile.zcoords",
    (grids.GridTile, 'horizontal_resolution'): "cim.1.grids.GridTile.horizontal_resolution",
    (grids.GridTile, 'coordinate_pole'): "cim.1.grids.GridTile.coordinate_pole",
    (grids.GridTile, 'id'): "cim.1.grids.GridTile.id",
    (grids.GridTile, 'area'): "cim.1.grids.GridTile.area",
    (grids.GridTile, 'is_conformal'): "cim.1.grids.GridTile.is_conformal",
    (grids.GridTile, 'cell_array'): "cim.1.grids.GridTile.cell_array",
    (grids.GridTile, 'simple_grid_geom'): "cim.1.grids.GridTile.simple_grid_geom",
    (grids.GridTile, 'is_regular'): "cim.1.grids.GridTile.is_regular",
    (grids.GridTile, 'cell_ref_array'): "cim.1.grids.GridTile.cell_ref_array",
    (grids.SimpleGridGeometry, 'dim_order'): "cim.1.grids.SimpleGridGeometry.dim_order",
    (grids.SimpleGridGeometry, 'ycoords'): "cim.1.grids.SimpleGridGeometry.ycoords",
    (grids.SimpleGridGeometry, 'zcoords'): "cim.1.grids.SimpleGridGeometry.zcoords",
    (grids.SimpleGridGeometry, 'num_dims'): "cim.1.grids.SimpleGridGeometry.num_dims",
    (grids.SimpleGridGeometry, 'is_mesh'): "cim.1.grids.SimpleGridGeometry.is_mesh",
    (grids.SimpleGridGeometry, 'xcoords'): "cim.1.grids.SimpleGridGeometry.xcoords",
    (grids.GridMosaic, 'extent'): "cim.1.grids.GridMosaic.extent",
    (grids.GridMosaic, 'mosaic_count'): "cim.1.grids.GridMosaic.mosaic_count",
    (grids.GridMosaic, 'mnemonic'): "cim.1.grids.GridMosaic.mnemonic",
    (grids.GridMosaic, 'tile_count'): "cim.1.grids.GridMosaic.tile_count",
    (grids.GridMosaic, 'type'): "cim.1.grids.GridMosaic.type",
    (grids.GridMosaic, 'has_congruent_tiles'): "cim.1.grids.GridMosaic.has_congruent_tiles",
    (grids.GridMosaic, 'description'): "cim.1.grids.GridMosaic.description",
    (grids.GridMosaic, 'citations'): "cim.1.grids.GridMosaic.citations",
    (grids.GridMosaic, 'mosaics'): "cim.1.grids.GridMosaic.mosaics",
    (grids.GridMosaic, 'long_name'): "cim.1.grids.GridMosaic.long_name",
    (grids.GridMosaic, 'short_name'): "cim.1.grids.GridMosaic.short_name",
    (grids.GridMosaic, 'tiles'): "cim.1.grids.GridMosaic.tiles",
    (grids.GridMosaic, 'is_leaf'): "cim.1.grids.GridMosaic.is_leaf",
    (grids.GridMosaic, 'id'): "cim.1.grids.GridMosaic.id",
    (grids.VerticalCoordinateList, 'type'): "cim.1.grids.VerticalCoordinateList.type",
    (grids.VerticalCoordinateList, 'form'): "cim.1.grids.VerticalCoordinateList.form",
    (grids.VerticalCoordinateList, 'properties'): "cim.1.grids.VerticalCoordinateList.properties",
    (grids.GridExtent, 'maximum_latitude'): "cim.1.grids.GridExtent.maximum_latitude",
    (grids.GridExtent, 'units'): "cim.1.grids.GridExtent.units",
    (grids.GridExtent, 'minimum_latitude'): "cim.1.grids.GridExtent.minimum_latitude",
    (grids.GridExtent, 'minimum_longitude'): "cim.1.grids.GridExtent.minimum_longitude",
    (grids.GridExtent, 'maximum_longitude'): "cim.1.grids.GridExtent.maximum_longitude",
    (grids.GridSpec, 'esm_exchange_grids'): "cim.1.grids.GridSpec.esm_exchange_grids",
    (grids.GridSpec, 'meta'): "cim.1.grids.GridSpec.meta",
    (grids.GridSpec, 'esm_model_grids'): "cim.1.grids.GridSpec.esm_model_grids",
    (grids.GridTileResolutionType, 'description'): "cim.1.grids.GridTileResolutionType.description",
    (grids.GridTileResolutionType, 'properties'): "cim.1.grids.GridTileResolutionType.properties",

    # ------------------------------------------------
    # Enums.
    # ------------------------------------------------

    quality.CimScopeCodeType: "cim.1.quality.CimScopeCodeType",
    quality.QualitySeverityType: "cim.1.quality.QualitySeverityType",
    quality.QualityIssueType: "cim.1.quality.QualityIssueType",
    quality.CimResultType: "cim.1.quality.CimResultType",
    quality.CimFeatureType: "cim.1.quality.CimFeatureType",
    quality.QualityStatusType: "cim.1.quality.QualityStatusType",
    activity.ProjectType: "cim.1.activity.ProjectType",
    activity.ResolutionType: "cim.1.activity.ResolutionType",
    activity.SimulationRelationshipType: "cim.1.activity.SimulationRelationshipType",
    activity.ConformanceType: "cim.1.activity.ConformanceType",
    activity.EnsembleType: "cim.1.activity.EnsembleType",
    activity.ExperimentRelationshipType: "cim.1.activity.ExperimentRelationshipType",
    activity.SimulationType: "cim.1.activity.SimulationType",
    activity.DownscalingType: "cim.1.activity.DownscalingType",
    activity.FrequencyType: "cim.1.activity.FrequencyType",
    software.CouplingFrameworkType: "cim.1.software.CouplingFrameworkType",
    software.ConnectionType: "cim.1.software.ConnectionType",
    software.TimingUnits: "cim.1.software.TimingUnits",
    software.SpatialRegriddingStandardMethodType: "cim.1.software.SpatialRegriddingStandardMethodType",
    software.TimeMappingType: "cim.1.software.TimeMappingType",
    software.ModelComponentType: "cim.1.software.ModelComponentType",
    software.SpatialRegriddingDimensionType: "cim.1.software.SpatialRegriddingDimensionType",
    software.StatisticalModelComponentType: "cim.1.software.StatisticalModelComponentType",
    software.ComponentPropertyIntentType: "cim.1.software.ComponentPropertyIntentType",
    data.DataStatusType: "cim.1.data.DataStatusType",
    data.DataHierarchyType: "cim.1.data.DataHierarchyType",
    shared.DataPurpose: "cim.1.shared.DataPurpose",
    shared.DocRelationshipType: "cim.1.shared.DocRelationshipType",
    shared.ProcessorType: "cim.1.shared.ProcessorType",
    shared.ChangePropertyType: "cim.1.shared.ChangePropertyType",
    shared.OperatingSystemType: "cim.1.shared.OperatingSystemType",
    shared.DocType: "cim.1.shared.DocType",
    shared.DocStatusType: "cim.1.shared.DocStatusType",
    shared.InterconnectType: "cim.1.shared.InterconnectType",
    shared.MachineType: "cim.1.shared.MachineType",
    shared.MachineVendorType: "cim.1.shared.MachineVendorType",
    shared.DocRelationshipDirectionType: "cim.1.shared.DocRelationshipDirectionType",
    shared.CompilerType: "cim.1.shared.CompilerType",
    shared.UnitType: "cim.1.shared.UnitType",
    grids.VerticalCsEnum: "cim.1.grids.VerticalCsEnum",
    grids.RefinementTypeEnum: "cim.1.grids.RefinementTypeEnum",
    grids.GeometryTypeEnum: "cim.1.grids.GeometryTypeEnum",
    grids.DiscretizationEnum: "cim.1.grids.DiscretizationEnum",
    grids.FeatureTypeEnum: "cim.1.grids.FeatureTypeEnum",
    grids.HorizontalCsEnum: "cim.1.grids.HorizontalCsEnum",
    grids.GridNodePositionEnum: "cim.1.grids.GridNodePositionEnum",
    grids.ArcTypeEnum: "cim.1.grids.ArcTypeEnum",
    grids.GridTypeEnum: "cim.1.grids.GridTypeEnum",

    # ------------------------------------------------
    # Enum members.
    # ------------------------------------------------

    (quality.CimScopeCodeType, 'numericalRequirement'): "cim.1.quality.CimScopeCodeType.numericalRequirement",
    (quality.CimScopeCodeType, 'dataset'): "cim.1.quality.CimScopeCodeType.dataset",
    (quality.CimScopeCodeType, 'file'): "cim.1.quality.CimScopeCodeType.file",
    (quality.CimScopeCodeType, 'service'): "cim.1.quality.CimScopeCodeType.service",
    (quality.CimScopeCodeType, 'model'): "cim.1.quality.CimScopeCodeType.model",
    (quality.CimScopeCodeType, 'modelComponent'): "cim.1.quality.CimScopeCodeType.modelComponent",
    (quality.CimScopeCodeType, 'software'): "cim.1.quality.CimScopeCodeType.software",
    (quality.CimScopeCodeType, 'simulation'): "cim.1.quality.CimScopeCodeType.simulation",
    (quality.CimScopeCodeType, 'experiment'): "cim.1.quality.CimScopeCodeType.experiment",
    (quality.CimScopeCodeType, 'ensemble'): "cim.1.quality.CimScopeCodeType.ensemble",
    (quality.QualitySeverityType, 'minor'): "cim.1.quality.QualitySeverityType.minor",
    (quality.QualitySeverityType, 'cosmetic'): "cim.1.quality.QualitySeverityType.cosmetic",
    (quality.QualitySeverityType, 'major'): "cim.1.quality.QualitySeverityType.major",
    (quality.QualityIssueType, 'data_content'): "cim.1.quality.QualityIssueType.data_content",
    (quality.QualityIssueType, 'metadata'): "cim.1.quality.QualityIssueType.metadata",
    (quality.QualityIssueType, 'science'): "cim.1.quality.QualityIssueType.science",
    (quality.QualityIssueType, 'data_format'): "cim.1.quality.QualityIssueType.data_format",
    (quality.QualityIssueType, 'data_indexing'): "cim.1.quality.QualityIssueType.data_indexing",
    (quality.CimResultType, 'document'): "cim.1.quality.CimResultType.document",
    (quality.CimResultType, 'logfile'): "cim.1.quality.CimResultType.logfile",
    (quality.CimResultType, 'plot'): "cim.1.quality.CimResultType.plot",
    (quality.CimFeatureType, 'diagnostic'): "cim.1.quality.CimFeatureType.diagnostic",
    (quality.CimFeatureType, 'file'): "cim.1.quality.CimFeatureType.file",
    (quality.QualityStatusType, 'resolved'): "cim.1.quality.QualityStatusType.resolved",
    (quality.QualityStatusType, 'partially_resolved'): "cim.1.quality.QualityStatusType.partially_resolved",
    (quality.QualityStatusType, 'confirmed'): "cim.1.quality.QualityStatusType.confirmed",
    (quality.QualityStatusType, 'reported'): "cim.1.quality.QualityStatusType.reported",
    (activity.SimulationRelationshipType, 'lowerResolutionVersionOf'): "cim.1.activity.SimulationRelationshipType.lowerResolutionVersionOf",
    (activity.SimulationRelationshipType, 'fixedVersionOf'): "cim.1.activity.SimulationRelationshipType.fixedVersionOf",
    (activity.SimulationRelationshipType, 'followingSimulation'): "cim.1.activity.SimulationRelationshipType.followingSimulation",
    (activity.SimulationRelationshipType, 'extensionOf'): "cim.1.activity.SimulationRelationshipType.extensionOf",
    (activity.SimulationRelationshipType, 'responseTo'): "cim.1.activity.SimulationRelationshipType.responseTo",
    (activity.SimulationRelationshipType, 'continuationOf'): "cim.1.activity.SimulationRelationshipType.continuationOf",
    (activity.SimulationRelationshipType, 'previousSimulation'): "cim.1.activity.SimulationRelationshipType.previousSimulation",
    (activity.SimulationRelationshipType, 'higherResolutionVersionOf'): "cim.1.activity.SimulationRelationshipType.higherResolutionVersionOf",
    (activity.ConformanceType, 'via model mods'): "cim.1.activity.ConformanceType.via-model-mods",
    (activity.ConformanceType, 'combination'): "cim.1.activity.ConformanceType.combination",
    (activity.ConformanceType, 'not-xxx'): "cim.1.activity.ConformanceType.not-xxx",
    (activity.ConformanceType, 'not conformant'): "cim.1.activity.ConformanceType.not-conformant",
    (activity.ConformanceType, 'standard config'): "cim.1.activity.ConformanceType.standard-config",
    (activity.ConformanceType, 'via inputs'): "cim.1.activity.ConformanceType.via-inputs",
    (activity.ExperimentRelationshipType, 'controlExperiment'): "cim.1.activity.ExperimentRelationshipType.controlExperiment",
    (activity.ExperimentRelationshipType, 'higherResolutionVersionOf'): "cim.1.activity.ExperimentRelationshipType.higherResolutionVersionOf",
    (activity.ExperimentRelationshipType, 'lowerResolutionVersionOf'): "cim.1.activity.ExperimentRelationshipType.lowerResolutionVersionOf",
    (activity.ExperimentRelationshipType, 'increaseEnsembleOf'): "cim.1.activity.ExperimentRelationshipType.increaseEnsembleOf",
    (activity.ExperimentRelationshipType, 'modifiedInputMethodOf'): "cim.1.activity.ExperimentRelationshipType.modifiedInputMethodOf",
    (activity.ExperimentRelationshipType, 'shorterVersionOf'): "cim.1.activity.ExperimentRelationshipType.shorterVersionOf",
    (activity.ExperimentRelationshipType, 'previousRealisation'): "cim.1.activity.ExperimentRelationshipType.previousRealisation",
    (activity.ExperimentRelationshipType, 'extensionOf'): "cim.1.activity.ExperimentRelationshipType.extensionOf",
    (activity.ExperimentRelationshipType, 'continuationOf'): "cim.1.activity.ExperimentRelationshipType.continuationOf",
    (activity.SimulationType, 'assimilation'): "cim.1.activity.SimulationType.assimilation",
    (activity.SimulationType, 'simulationComposite'): "cim.1.activity.SimulationType.simulationComposite",
    (activity.SimulationType, 'simulationRun'): "cim.1.activity.SimulationType.simulationRun",
    (activity.DownscalingType, 'dynamic'): "cim.1.activity.DownscalingType.dynamic",
    (activity.DownscalingType, 'statistical'): "cim.1.activity.DownscalingType.statistical",
    (software.CouplingFrameworkType, 'ESMF'): "cim.1.software.CouplingFrameworkType.ESMF",
    (software.CouplingFrameworkType, 'BFG'): "cim.1.software.CouplingFrameworkType.BFG",
    (software.CouplingFrameworkType, 'OASIS'): "cim.1.software.CouplingFrameworkType.OASIS",
    (software.TimingUnits, 'days'): "cim.1.software.TimingUnits.days",
    (software.TimingUnits, 'months'): "cim.1.software.TimingUnits.months",
    (software.TimingUnits, 'years'): "cim.1.software.TimingUnits.years",
    (software.TimingUnits, 'decades'): "cim.1.software.TimingUnits.decades",
    (software.TimingUnits, 'centuries'): "cim.1.software.TimingUnits.centuries",
    (software.TimingUnits, 'seconds'): "cim.1.software.TimingUnits.seconds",
    (software.TimingUnits, 'minutes'): "cim.1.software.TimingUnits.minutes",
    (software.TimingUnits, 'hours'): "cim.1.software.TimingUnits.hours",
    (software.SpatialRegriddingStandardMethodType, 'conservative'): "cim.1.software.SpatialRegriddingStandardMethodType.conservative",
    (software.SpatialRegriddingStandardMethodType, 'non-conservative'): "cim.1.software.SpatialRegriddingStandardMethodType.non-conservative",
    (software.SpatialRegriddingStandardMethodType, 'linear'): "cim.1.software.SpatialRegriddingStandardMethodType.linear",
    (software.SpatialRegriddingStandardMethodType, 'near-neighbour'): "cim.1.software.SpatialRegriddingStandardMethodType.near-neighbour",
    (software.SpatialRegriddingStandardMethodType, 'cubic'): "cim.1.software.SpatialRegriddingStandardMethodType.cubic",
    (software.SpatialRegriddingStandardMethodType, 'conservative-first-order'): "cim.1.software.SpatialRegriddingStandardMethodType.conservative-first-order",
    (software.SpatialRegriddingStandardMethodType, 'conservative-second-order'): "cim.1.software.SpatialRegriddingStandardMethodType.conservative-second-order",
    (software.SpatialRegriddingDimensionType, '1D'): "cim.1.software.SpatialRegriddingDimensionType.1D",
    (software.SpatialRegriddingDimensionType, '2D'): "cim.1.software.SpatialRegriddingDimensionType.2D",
    (software.SpatialRegriddingDimensionType, '3D'): "cim.1.software.SpatialRegriddingDimensionType.3D",
    (software.ComponentPropertyIntentType, 'in'): "cim.1.software.ComponentPropertyIntentType.in",
    (software.ComponentPropertyIntentType, 'out'): "cim.1.software.ComponentPropertyIntentType.out",
    (software.ComponentPropertyIntentType, 'inout'): "cim.1.software.ComponentPropertyIntentType.inout",
    (data.DataStatusType, 'metadataOnly'): "cim.1.data.DataStatusType.metadataOnly",
    (data.DataStatusType, 'complete'): "cim.1.data.DataStatusType.complete",
    (data.DataStatusType, 'continuouslySupplemented'): "cim.1.data.DataStatusType.continuouslySupplemented",
    (shared.DataPurpose, 'boundaryCondition'): "cim.1.shared.DataPurpose.boundaryCondition",
    (shared.DataPurpose, 'ancillaryFile'): "cim.1.shared.DataPurpose.ancillaryFile",
    (shared.DataPurpose, 'initialCondition'): "cim.1.shared.DataPurpose.initialCondition",
    (shared.DocRelationshipType, 'similarTo'): "cim.1.shared.DocRelationshipType.similarTo",
    (shared.DocRelationshipType, 'fixedVersionOf'): "cim.1.shared.DocRelationshipType.fixedVersionOf",
    (shared.DocRelationshipType, 'previousVersionOf'): "cim.1.shared.DocRelationshipType.previousVersionOf",
    (shared.DocRelationshipType, 'other'): "cim.1.shared.DocRelationshipType.other",
    (shared.DocRelationshipType, 'laterVersionOf'): "cim.1.shared.DocRelationshipType.laterVersionOf",
    (shared.ChangePropertyType, 'Replacement'): "cim.1.shared.ChangePropertyType.Replacement",
    (shared.ChangePropertyType, 'ParameterChange'): "cim.1.shared.ChangePropertyType.ParameterChange",
    (shared.ChangePropertyType, 'ModelMod'): "cim.1.shared.ChangePropertyType.ModelMod",
    (shared.ChangePropertyType, 'CodeChange'): "cim.1.shared.ChangePropertyType.CodeChange",
    (shared.ChangePropertyType, 'AncillaryFile'): "cim.1.shared.ChangePropertyType.AncillaryFile",
    (shared.ChangePropertyType, 'InputMod'): "cim.1.shared.ChangePropertyType.InputMod",
    (shared.ChangePropertyType, 'BoundaryCondition'): "cim.1.shared.ChangePropertyType.BoundaryCondition",
    (shared.ChangePropertyType, 'Decrement'): "cim.1.shared.ChangePropertyType.Decrement",
    (shared.ChangePropertyType, 'Unused'): "cim.1.shared.ChangePropertyType.Unused",
    (shared.ChangePropertyType, 'Increment'): "cim.1.shared.ChangePropertyType.Increment",
    (shared.ChangePropertyType, 'Redistribution'): "cim.1.shared.ChangePropertyType.Redistribution",
    (shared.ChangePropertyType, 'InitialCondition'): "cim.1.shared.ChangePropertyType.InitialCondition",
    (shared.DocType, 'processorComponent'): "cim.1.shared.DocType.processorComponent",
    (shared.DocType, 'modelComponent'): "cim.1.shared.DocType.modelComponent",
    (shared.DocType, 'simulationComposite'): "cim.1.shared.DocType.simulationComposite",
    (shared.DocType, 'dataObject'): "cim.1.shared.DocType.dataObject",
    (shared.DocType, 'dataProcessing'): "cim.1.shared.DocType.dataProcessing",
    (shared.DocType, 'ensemble'): "cim.1.shared.DocType.ensemble",
    (shared.DocType, 'platform'): "cim.1.shared.DocType.platform",
    (shared.DocType, 'downscalingSimulation'): "cim.1.shared.DocType.downscalingSimulation",
    (shared.DocType, 'gridSpec'): "cim.1.shared.DocType.gridSpec",
    (shared.DocType, 'simulationRun'): "cim.1.shared.DocType.simulationRun",
    (shared.DocType, 'cimQuality'): "cim.1.shared.DocType.cimQuality",
    (shared.DocType, 'assimilation'): "cim.1.shared.DocType.assimilation",
    (shared.DocType, 'statisticalModelComponent'): "cim.1.shared.DocType.statisticalModelComponent",
    (shared.DocType, 'numericalExperiment'): "cim.1.shared.DocType.numericalExperiment",
    (shared.DocStatusType, 'complete'): "cim.1.shared.DocStatusType.complete",
    (shared.DocStatusType, 'incomplete'): "cim.1.shared.DocStatusType.incomplete",
    (shared.DocStatusType, 'in-progress'): "cim.1.shared.DocStatusType.in-progress",
    (shared.MachineType, 'Parallel'): "cim.1.shared.MachineType.Parallel",
    (shared.MachineType, 'Beowulf'): "cim.1.shared.MachineType.Beowulf",
    (shared.MachineType, 'Vector'): "cim.1.shared.MachineType.Vector",
    (shared.DocRelationshipDirectionType, 'fromTarget'): "cim.1.shared.DocRelationshipDirectionType.fromTarget",
    (shared.DocRelationshipDirectionType, 'toTarget'): "cim.1.shared.DocRelationshipDirectionType.toTarget",
    (grids.VerticalCsEnum, 'mass-based'): "cim.1.grids.VerticalCsEnum.mass-based",
    (grids.VerticalCsEnum, 'space-based'): "cim.1.grids.VerticalCsEnum.space-based",
    (grids.RefinementTypeEnum, 'none'): "cim.1.grids.RefinementTypeEnum.none",
    (grids.RefinementTypeEnum, 'integer'): "cim.1.grids.RefinementTypeEnum.integer",
    (grids.RefinementTypeEnum, 'rational'): "cim.1.grids.RefinementTypeEnum.rational",
    (grids.GeometryTypeEnum, 'plane'): "cim.1.grids.GeometryTypeEnum.plane",
    (grids.GeometryTypeEnum, 'ellipsoid'): "cim.1.grids.GeometryTypeEnum.ellipsoid",
    (grids.GeometryTypeEnum, 'sphere'): "cim.1.grids.GeometryTypeEnum.sphere",
    (grids.DiscretizationEnum, 'unstructured_polygonal'): "cim.1.grids.DiscretizationEnum.unstructured_polygonal",
    (grids.DiscretizationEnum, 'spherical_harmonics'): "cim.1.grids.DiscretizationEnum.spherical_harmonics",
    (grids.DiscretizationEnum, 'other'): "cim.1.grids.DiscretizationEnum.other",
    (grids.DiscretizationEnum, 'logically_rectangular'): "cim.1.grids.DiscretizationEnum.logically_rectangular",
    (grids.DiscretizationEnum, 'structured_triangular'): "cim.1.grids.DiscretizationEnum.structured_triangular",
    (grids.DiscretizationEnum, 'unstructured_triangular'): "cim.1.grids.DiscretizationEnum.unstructured_triangular",
    (grids.DiscretizationEnum, 'pixel-based_catchment'): "cim.1.grids.DiscretizationEnum.pixel-based_catchment",
    (grids.FeatureTypeEnum, 'edge'): "cim.1.grids.FeatureTypeEnum.edge",
    (grids.FeatureTypeEnum, 'point'): "cim.1.grids.FeatureTypeEnum.point",
    (grids.HorizontalCsEnum, 'spherical'): "cim.1.grids.HorizontalCsEnum.spherical",
    (grids.HorizontalCsEnum, 'cartesian'): "cim.1.grids.HorizontalCsEnum.cartesian",
    (grids.HorizontalCsEnum, 'ellipsoidal'): "cim.1.grids.HorizontalCsEnum.ellipsoidal",
    (grids.HorizontalCsEnum, 'polar'): "cim.1.grids.HorizontalCsEnum.polar",
    (grids.GridNodePositionEnum, 'sphere'): "cim.1.grids.GridNodePositionEnum.sphere",
    (grids.GridNodePositionEnum, 'centre'): "cim.1.grids.GridNodePositionEnum.centre",
    (grids.GridNodePositionEnum, 'plane'): "cim.1.grids.GridNodePositionEnum.plane",
    (grids.ArcTypeEnum, 'complex'): "cim.1.grids.ArcTypeEnum.complex",
    (grids.ArcTypeEnum, 'small_circle'): "cim.1.grids.ArcTypeEnum.small_circle",
    (grids.ArcTypeEnum, 'geodesic'): "cim.1.grids.ArcTypeEnum.geodesic",
    (grids.ArcTypeEnum, 'great_circle'): "cim.1.grids.ArcTypeEnum.great_circle",
    (grids.GridTypeEnum, 'composite'): "cim.1.grids.GridTypeEnum.composite",
    (grids.GridTypeEnum, 'other'): "cim.1.grids.GridTypeEnum.other",
    (grids.GridTypeEnum, 'cubed_sphere'): "cim.1.grids.GridTypeEnum.cubed_sphere",
    (grids.GridTypeEnum, 'icosahedral_geodesic'): "cim.1.grids.GridTypeEnum.icosahedral_geodesic",
    (grids.GridTypeEnum, 'reduced_gaussian'): "cim.1.grids.GridTypeEnum.reduced_gaussian",
    (grids.GridTypeEnum, 'regular_lat_lon'): "cim.1.grids.GridTypeEnum.regular_lat_lon",
    (grids.GridTypeEnum, 'spectral_gaussian'): "cim.1.grids.GridTypeEnum.spectral_gaussian",
    (grids.GridTypeEnum, 'tripolar'): "cim.1.grids.GridTypeEnum.tripolar",
    (grids.GridTypeEnum, 'yin_yang'): "cim.1.grids.GridTypeEnum.yin_yang",
    (grids.GridTypeEnum, 'displaced_pole'): "cim.1.grids.GridTypeEnum.displaced_pole",
}

# Set inline type keys.
misc.DocumentSet.type_key = KEYS[misc.DocumentSet]
data.DataProperty.type_key = KEYS[data.DataProperty]
data.DataExtentTemporal.type_key = KEYS[data.DataExtentTemporal]
data.DataContent.type_key = KEYS[data.DataContent]
data.DataStorageIp.type_key = KEYS[data.DataStorageIp]
data.DataRestriction.type_key = KEYS[data.DataRestriction]
data.DataExtentTimeInterval.type_key = KEYS[data.DataExtentTimeInterval]
data.DataDistribution.type_key = KEYS[data.DataDistribution]
data.DataTopic.type_key = KEYS[data.DataTopic]
data.DataStorage.type_key = KEYS[data.DataStorage]
data.DataHierarchyLevel.type_key = KEYS[data.DataHierarchyLevel]
data.DataExtent.type_key = KEYS[data.DataExtent]
data.DataStorageDb.type_key = KEYS[data.DataStorageDb]
data.DataObject.type_key = KEYS[data.DataObject]
data.DataExtentGeographical.type_key = KEYS[data.DataExtentGeographical]
data.DataStorageFile.type_key = KEYS[data.DataStorageFile]
software.ModelComponent.type_key = KEYS[software.ModelComponent]
software.ConnectionProperty.type_key = KEYS[software.ConnectionProperty]
software.ProcessorComponent.type_key = KEYS[software.ProcessorComponent]
software.ComponentProperty.type_key = KEYS[software.ComponentProperty]
software.Component.type_key = KEYS[software.Component]
software.ComponentLanguageProperty.type_key = KEYS[software.ComponentLanguageProperty]
software.SpatialRegriddingProperty.type_key = KEYS[software.SpatialRegriddingProperty]
software.SpatialRegriddingUserMethod.type_key = KEYS[software.SpatialRegriddingUserMethod]
software.Deployment.type_key = KEYS[software.Deployment]
software.StatisticalModelComponent.type_key = KEYS[software.StatisticalModelComponent]
software.Composition.type_key = KEYS[software.Composition]
software.Connection.type_key = KEYS[software.Connection]
software.Parallelisation.type_key = KEYS[software.Parallelisation]
software.Timing.type_key = KEYS[software.Timing]
software.ConnectionEndpoint.type_key = KEYS[software.ConnectionEndpoint]
software.ComponentLanguage.type_key = KEYS[software.ComponentLanguage]
software.TimeTransformation.type_key = KEYS[software.TimeTransformation]
software.TimeLag.type_key = KEYS[software.TimeLag]
software.Coupling.type_key = KEYS[software.Coupling]
software.CouplingEndpoint.type_key = KEYS[software.CouplingEndpoint]
software.CouplingProperty.type_key = KEYS[software.CouplingProperty]
software.EntryPoint.type_key = KEYS[software.EntryPoint]
software.Rank.type_key = KEYS[software.Rank]
software.SpatialRegridding.type_key = KEYS[software.SpatialRegridding]
quality.Evaluation.type_key = KEYS[quality.Evaluation]
quality.Measure.type_key = KEYS[quality.Measure]
quality.CimQuality.type_key = KEYS[quality.CimQuality]
quality.Report.type_key = KEYS[quality.Report]
grids.GridTile.type_key = KEYS[grids.GridTile]
grids.GridExtent.type_key = KEYS[grids.GridExtent]
grids.GridTileResolutionType.type_key = KEYS[grids.GridTileResolutionType]
grids.GridMosaic.type_key = KEYS[grids.GridMosaic]
grids.SimpleGridGeometry.type_key = KEYS[grids.SimpleGridGeometry]
grids.GridProperty.type_key = KEYS[grids.GridProperty]
grids.VerticalCoordinateList.type_key = KEYS[grids.VerticalCoordinateList]
grids.GridSpec.type_key = KEYS[grids.GridSpec]
grids.CoordinateList.type_key = KEYS[grids.CoordinateList]
activity.Conformance.type_key = KEYS[activity.Conformance]
activity.OutputRequirement.type_key = KEYS[activity.OutputRequirement]
activity.MeasurementCampaign.type_key = KEYS[activity.MeasurementCampaign]
activity.PhysicalModification.type_key = KEYS[activity.PhysicalModification]
activity.SimulationComposite.type_key = KEYS[activity.SimulationComposite]
activity.NumericalActivity.type_key = KEYS[activity.NumericalActivity]
activity.Ensemble.type_key = KEYS[activity.Ensemble]
activity.Simulation.type_key = KEYS[activity.Simulation]
activity.NumericalExperiment.type_key = KEYS[activity.NumericalExperiment]
activity.EnsembleMember.type_key = KEYS[activity.EnsembleMember]
activity.NumericalRequirement.type_key = KEYS[activity.NumericalRequirement]
activity.Experiment.type_key = KEYS[activity.Experiment]
activity.SimulationRelationship.type_key = KEYS[activity.SimulationRelationship]
activity.Activity.type_key = KEYS[activity.Activity]
activity.NumericalRequirementOption.type_key = KEYS[activity.NumericalRequirementOption]
activity.ExperimentRelationship.type_key = KEYS[activity.ExperimentRelationship]
activity.SimulationRelationshipTarget.type_key = KEYS[activity.SimulationRelationshipTarget]
activity.BoundaryCondition.type_key = KEYS[activity.BoundaryCondition]
activity.ExperimentRelationshipTarget.type_key = KEYS[activity.ExperimentRelationshipTarget]
activity.SimulationRun.type_key = KEYS[activity.SimulationRun]
activity.DownscalingSimulation.type_key = KEYS[activity.DownscalingSimulation]
activity.InitialCondition.type_key = KEYS[activity.InitialCondition]
activity.LateralBoundaryCondition.type_key = KEYS[activity.LateralBoundaryCondition]
activity.SpatioTemporalConstraint.type_key = KEYS[activity.SpatioTemporalConstraint]
shared.Change.type_key = KEYS[shared.Change]
shared.PerpetualPeriod.type_key = KEYS[shared.PerpetualPeriod]
shared.Platform.type_key = KEYS[shared.Platform]
shared.Standard.type_key = KEYS[shared.Standard]
shared.Compiler.type_key = KEYS[shared.Compiler]
shared.RealCalendar.type_key = KEYS[shared.RealCalendar]
shared.DocRelationshipTarget.type_key = KEYS[shared.DocRelationshipTarget]
shared.Machine.type_key = KEYS[shared.Machine]
shared.Relationship.type_key = KEYS[shared.Relationship]
shared.ResponsibleParty.type_key = KEYS[shared.ResponsibleParty]
shared.StandardName.type_key = KEYS[shared.StandardName]
shared.ChangeProperty.type_key = KEYS[shared.ChangeProperty]
shared.DocRelationship.type_key = KEYS[shared.DocRelationship]
shared.DataSource.type_key = KEYS[shared.DataSource]
shared.MachineCompilerUnit.type_key = KEYS[shared.MachineCompilerUnit]
shared.DocMetaInfo.type_key = KEYS[shared.DocMetaInfo]
shared.Property.type_key = KEYS[shared.Property]
shared.DocGenealogy.type_key = KEYS[shared.DocGenealogy]
shared.Citation.type_key = KEYS[shared.Citation]
shared.Calendar.type_key = KEYS[shared.Calendar]
shared.DocReference.type_key = KEYS[shared.DocReference]
shared.ClosedDateRange.type_key = KEYS[shared.ClosedDateRange]
shared.Daily360.type_key = KEYS[shared.Daily360]
shared.DateRange.type_key = KEYS[shared.DateRange]
shared.OpenDateRange.type_key = KEYS[shared.OpenDateRange]
shared.License.type_key = KEYS[shared.License]
data.DataHierarchyType.type_key = KEYS[data.DataHierarchyType]
data.DataStatusType.type_key = KEYS[data.DataStatusType]
software.CouplingFrameworkType.type_key = KEYS[software.CouplingFrameworkType]
software.ModelComponentType.type_key = KEYS[software.ModelComponentType]
software.SpatialRegriddingDimensionType.type_key = KEYS[software.SpatialRegriddingDimensionType]
software.SpatialRegriddingStandardMethodType.type_key = KEYS[software.SpatialRegriddingStandardMethodType]
software.StatisticalModelComponentType.type_key = KEYS[software.StatisticalModelComponentType]
software.TimeMappingType.type_key = KEYS[software.TimeMappingType]
software.TimingUnits.type_key = KEYS[software.TimingUnits]
software.ComponentPropertyIntentType.type_key = KEYS[software.ComponentPropertyIntentType]
software.ConnectionType.type_key = KEYS[software.ConnectionType]
quality.QualitySeverityType.type_key = KEYS[quality.QualitySeverityType]
quality.CimFeatureType.type_key = KEYS[quality.CimFeatureType]
quality.QualityStatusType.type_key = KEYS[quality.QualityStatusType]
quality.CimResultType.type_key = KEYS[quality.CimResultType]
quality.CimScopeCodeType.type_key = KEYS[quality.CimScopeCodeType]
quality.QualityIssueType.type_key = KEYS[quality.QualityIssueType]
grids.VerticalCsEnum.type_key = KEYS[grids.VerticalCsEnum]
grids.GridNodePositionEnum.type_key = KEYS[grids.GridNodePositionEnum]
grids.DiscretizationEnum.type_key = KEYS[grids.DiscretizationEnum]
grids.RefinementTypeEnum.type_key = KEYS[grids.RefinementTypeEnum]
grids.GridTypeEnum.type_key = KEYS[grids.GridTypeEnum]
grids.FeatureTypeEnum.type_key = KEYS[grids.FeatureTypeEnum]
grids.HorizontalCsEnum.type_key = KEYS[grids.HorizontalCsEnum]
grids.GeometryTypeEnum.type_key = KEYS[grids.GeometryTypeEnum]
grids.ArcTypeEnum.type_key = KEYS[grids.ArcTypeEnum]
activity.EnsembleType.type_key = KEYS[activity.EnsembleType]
activity.ExperimentRelationshipType.type_key = KEYS[activity.ExperimentRelationshipType]
activity.FrequencyType.type_key = KEYS[activity.FrequencyType]
activity.ProjectType.type_key = KEYS[activity.ProjectType]
activity.ResolutionType.type_key = KEYS[activity.ResolutionType]
activity.SimulationType.type_key = KEYS[activity.SimulationType]
activity.DownscalingType.type_key = KEYS[activity.DownscalingType]
activity.SimulationRelationshipType.type_key = KEYS[activity.SimulationRelationshipType]
activity.ConformanceType.type_key = KEYS[activity.ConformanceType]
shared.ChangePropertyType.type_key = KEYS[shared.ChangePropertyType]
shared.CompilerType.type_key = KEYS[shared.CompilerType]
shared.DataPurpose.type_key = KEYS[shared.DataPurpose]
shared.InterconnectType.type_key = KEYS[shared.InterconnectType]
shared.MachineType.type_key = KEYS[shared.MachineType]
shared.MachineVendorType.type_key = KEYS[shared.MachineVendorType]
shared.OperatingSystemType.type_key = KEYS[shared.OperatingSystemType]
shared.ProcessorType.type_key = KEYS[shared.ProcessorType]
shared.UnitType.type_key = KEYS[shared.UnitType]
shared.DocRelationshipDirectionType.type_key = KEYS[shared.DocRelationshipDirectionType]
shared.DocRelationshipType.type_key = KEYS[shared.DocRelationshipType]
shared.DocStatusType.type_key = KEYS[shared.DocStatusType]
shared.DocType.type_key = KEYS[shared.DocType]



# Remove import dross.
del defaultdict
del datetime
del uuid
del misc
del quality
del activity
del software
del data
del shared
del grids

