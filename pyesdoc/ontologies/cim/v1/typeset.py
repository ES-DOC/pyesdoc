
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from collections import defaultdict
import datetime
import uuid

from typeset_for_data_package import *
from typeset_for_software_package import *
from typeset_for_shared_package import *
from typeset_for_grids_package import *
from typeset_for_quality_package import *
from typeset_for_misc_package import *
from typeset_for_activity_package import *


import typeset_for_data_package as data
import typeset_for_software_package as software
import typeset_for_shared_package as shared
import typeset_for_grids_package as grids
import typeset_for_quality_package as quality
import typeset_for_misc_package as misc
import typeset_for_activity_package as activity



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
    # Packages
    data,
    software,
    shared,
    grids,
    quality,
    misc,
    activity,
    # Classes
    DocReference,
    DataContent,
    PerpetualPeriod,
    Ensemble,
    OpenDateRange,
    Relationship,
    DataStorage,
    Citation,
    Parallelisation,
    GridTile,
    Activity,
    Conformance,
    Report,
    ProcessorComponent,
    DocMetaInfo,
    SpatialRegridding,
    NumericalActivity,
    CouplingProperty,
    ComponentLanguage,
    GridSpec,
    DocGenealogy,
    Calendar,
    PhysicalModification,
    DocRelationship,
    ClosedDateRange,
    ExperimentRelationship,
    RealCalendar,
    DataHierarchyLevel,
    Change,
    SpatialRegriddingProperty,
    SimulationRun,
    ConnectionEndpoint,
    SimulationRelationshipTarget,
    DataObject,
    DataTopic,
    GridExtent,
    Timing,
    NumericalRequirement,
    SimpleGridGeometry,
    InitialCondition,
    SpatioTemporalConstraint,
    DataExtent,
    DataStorageFile,
    DownscalingSimulation,
    Daily360,
    SimulationComposite,
    SpatialRegriddingUserMethod,
    Deployment,
    DataProperty,
    DataStorageIp,
    Measure,
    ComponentLanguageProperty,
    Composition,
    ResponsibleParty,
    DataExtentTemporal,
    Experiment,
    VerticalCoordinateList,
    GridProperty,
    LateralBoundaryCondition,
    ChangeProperty,
    GridTileResolutionType,
    EnsembleMember,
    TimeLag,
    StatisticalModelComponent,
    DataDistribution,
    CimQuality,
    Component,
    DataRestriction,
    CouplingEndpoint,
    Property,
    Platform,
    DataSource,
    GridMosaic,
    Connection,
    License,
    ExperimentRelationshipTarget,
    DataStorageDb,
    NumericalRequirementOption,
    Standard,
    DataExtentTimeInterval,
    MeasurementCampaign,
    NumericalExperiment,
    BoundaryCondition,
    Compiler,
    ModelComponent,
    OutputRequirement,
    StandardName,
    DocRelationshipTarget,
    MachineCompilerUnit,
    TimeTransformation,
    Rank,
    SimulationRelationship,
    Evaluation,
    DataExtentGeographical,
    CoordinateList,
    DocumentSet,
    Simulation,
    ComponentProperty,
    ConnectionProperty,
    Coupling,
    EntryPoint,
    DateRange,
    Machine,
    # Enums
    DataPurpose,
    ModelComponentType,
    SpatialRegriddingDimensionType,
    DiscretizationEnum,
    GridNodePositionEnum,
    QualityIssueType,
    DocRelationshipDirectionType,
    RefinementTypeEnum,
    EnsembleType,
    SpatialRegriddingStandardMethodType,
    InterconnectType,
    UnitType,
    CouplingFrameworkType,
    DocType,
    HorizontalCsEnum,
    CimFeatureType,
    GridTypeEnum,
    StatisticalModelComponentType,
    TimeMappingType,
    DownscalingType,
    ArcTypeEnum,
    OperatingSystemType,
    FeatureTypeEnum,
    QualityStatusType,
    ExperimentRelationshipType,
    GeometryTypeEnum,
    QualitySeverityType,
    SimulationType,
    VerticalCsEnum,
    TimingUnits,
    DataHierarchyType,
    CimResultType,
    ChangePropertyType,
    ComponentPropertyIntentType,
    MachineType,
    ProjectType,
    ProcessorType,
    CompilerType,
    DocStatusType,
    SimulationRelationshipType,
    MachineVendorType,
    ResolutionType,
    ConnectionType,
    ConformanceType,
    FrequencyType,
    CimScopeCodeType,
    DocRelationshipType,
    DataStatusType,
]

# Supported packages.
PACKAGES = (
    data,
    software,
    shared,
    grids,
    quality,
    misc,
    activity,
)

# Supported classes.
CLASSES = (
    shared.DocReference,
    data.DataContent,
    shared.PerpetualPeriod,
    activity.Ensemble,
    shared.OpenDateRange,
    shared.Relationship,
    data.DataStorage,
    shared.Citation,
    software.Parallelisation,
    grids.GridTile,
    activity.Activity,
    activity.Conformance,
    quality.Report,
    software.ProcessorComponent,
    shared.DocMetaInfo,
    software.SpatialRegridding,
    activity.NumericalActivity,
    software.CouplingProperty,
    software.ComponentLanguage,
    grids.GridSpec,
    shared.DocGenealogy,
    shared.Calendar,
    activity.PhysicalModification,
    shared.DocRelationship,
    shared.ClosedDateRange,
    activity.ExperimentRelationship,
    shared.RealCalendar,
    data.DataHierarchyLevel,
    shared.Change,
    software.SpatialRegriddingProperty,
    activity.SimulationRun,
    software.ConnectionEndpoint,
    activity.SimulationRelationshipTarget,
    data.DataObject,
    data.DataTopic,
    grids.GridExtent,
    software.Timing,
    activity.NumericalRequirement,
    grids.SimpleGridGeometry,
    activity.InitialCondition,
    activity.SpatioTemporalConstraint,
    data.DataExtent,
    data.DataStorageFile,
    activity.DownscalingSimulation,
    shared.Daily360,
    activity.SimulationComposite,
    software.SpatialRegriddingUserMethod,
    software.Deployment,
    data.DataProperty,
    data.DataStorageIp,
    quality.Measure,
    software.ComponentLanguageProperty,
    software.Composition,
    shared.ResponsibleParty,
    data.DataExtentTemporal,
    activity.Experiment,
    grids.VerticalCoordinateList,
    grids.GridProperty,
    activity.LateralBoundaryCondition,
    shared.ChangeProperty,
    grids.GridTileResolutionType,
    activity.EnsembleMember,
    software.TimeLag,
    software.StatisticalModelComponent,
    data.DataDistribution,
    quality.CimQuality,
    software.Component,
    data.DataRestriction,
    software.CouplingEndpoint,
    shared.Property,
    shared.Platform,
    shared.DataSource,
    grids.GridMosaic,
    software.Connection,
    shared.License,
    activity.ExperimentRelationshipTarget,
    data.DataStorageDb,
    activity.NumericalRequirementOption,
    shared.Standard,
    data.DataExtentTimeInterval,
    activity.MeasurementCampaign,
    activity.NumericalExperiment,
    activity.BoundaryCondition,
    shared.Compiler,
    software.ModelComponent,
    activity.OutputRequirement,
    shared.StandardName,
    shared.DocRelationshipTarget,
    shared.MachineCompilerUnit,
    software.TimeTransformation,
    software.Rank,
    activity.SimulationRelationship,
    quality.Evaluation,
    data.DataExtentGeographical,
    grids.CoordinateList,
    misc.DocumentSet,
    activity.Simulation,
    software.ComponentProperty,
    software.ConnectionProperty,
    software.Coupling,
    software.EntryPoint,
    shared.DateRange,
    shared.Machine,
)

# Supported enums.
ENUMS = (
    shared.DataPurpose,
    software.ModelComponentType,
    software.SpatialRegriddingDimensionType,
    grids.DiscretizationEnum,
    grids.GridNodePositionEnum,
    quality.QualityIssueType,
    shared.DocRelationshipDirectionType,
    grids.RefinementTypeEnum,
    activity.EnsembleType,
    software.SpatialRegriddingStandardMethodType,
    shared.InterconnectType,
    shared.UnitType,
    software.CouplingFrameworkType,
    shared.DocType,
    grids.HorizontalCsEnum,
    quality.CimFeatureType,
    grids.GridTypeEnum,
    software.StatisticalModelComponentType,
    software.TimeMappingType,
    activity.DownscalingType,
    grids.ArcTypeEnum,
    shared.OperatingSystemType,
    grids.FeatureTypeEnum,
    quality.QualityStatusType,
    activity.ExperimentRelationshipType,
    grids.GeometryTypeEnum,
    quality.QualitySeverityType,
    activity.SimulationType,
    grids.VerticalCsEnum,
    software.TimingUnits,
    data.DataHierarchyType,
    quality.CimResultType,
    shared.ChangePropertyType,
    software.ComponentPropertyIntentType,
    shared.MachineType,
    activity.ProjectType,
    shared.ProcessorType,
    shared.CompilerType,
    shared.DocStatusType,
    activity.SimulationRelationshipType,
    shared.MachineVendorType,
    activity.ResolutionType,
    software.ConnectionType,
    activity.ConformanceType,
    activity.FrequencyType,
    quality.CimScopeCodeType,
    shared.DocRelationshipType,
    data.DataStatusType,
)

# Supported document types.
DOCUMENT_TYPES = (
    data.DataObject,
    software.StatisticalModelComponent,
    software.ModelComponent,
    software.ProcessorComponent,
    shared.Platform,
    grids.GridSpec,
    quality.CimQuality,
    misc.DocumentSet,
    activity.DownscalingSimulation,
    activity.NumericalExperiment,
    activity.SimulationComposite,
    activity.SimulationRun,
    activity.Ensemble,
)

# Supported class properties.
CLASS_PROPERTIES = { 
    shared.DocReference: (
        'type',
        'description',
        'external_id',
        'url',
        'version',
        'name',
        'changes',
        'id',
    ),
    data.DataContent: (
        'aggregation',
        'topic',
        'purpose',
        'frequency',
    ),
    shared.PerpetualPeriod: (
        'description',
        'length',
        'range',
    ),
    activity.Ensemble: (
        'funding_sources',
        'members',
        'projects',
        'short_name',
        'types',
        'rationales',
        'description',
        'responsible_parties',
        'outputs',
        'long_name',
        'meta',
        'supports',
    ),
    shared.OpenDateRange: (
        'duration',
        'end',
        'start',
    ),
    shared.Relationship: (
        'description',
        'direction',
    ),
    data.DataStorage: (
        'location',
        'size',
        'modification_date',
        'format',
    ),
    shared.Citation: (
        'location',
        'type',
        'date',
        'organisation',
        'date_type',
        'title',
        'collective_title',
        'alternative_title',
        'role',
    ),
    software.Parallelisation: (
        'processes',
        'ranks',
    ),
    grids.GridTile: (
        'mnemonic',
        'nz',
        'horizontal_resolution',
        'horizontal_crs',
        'grid_north_pole',
        'simple_grid_geom',
        'discretization_type',
        'id',
        'ny',
        'is_conformal',
        'area',
        'vertical_crs',
        'zcoords',
        'cell_array',
        'description',
        'coord_file',
        'is_terrain_following',
        'cell_ref_array',
        'short_name',
        'geometry_type',
        'is_uniform',
        'refinement_scheme',
        'vertical_resolution',
        'is_regular',
        'nx',
        'long_name',
        'coordinate_pole',
        'extent',
    ),
    activity.Activity: (
        'funding_sources',
        'projects',
        'responsible_parties',
        'rationales',
    ),
    activity.Conformance: (
        'sources',
        'frequency',
        'type',
        'description',
        'is_conformant',
        'requirements',
    ),
    quality.Report: (
        'date',
        'evaluation',
        'evaluator',
        'measure',
    ),
    software.ProcessorComponent: (
        'online_resource',
        'release_date',
        'description',
        'purpose',
        'responsible_parties',
        'funding_sources',
        'grid',
        'code_access',
        'is_embedded',
        'sub_components',
        'coupling_framework',
        'meta',
        'citations',
        'language',
        'properties',
        'version',
        'license',
        'composition',
        'dependencies',
        'parent',
        'long_name',
        'deployments',
        'previous_version',
        'short_name',
    ),
    shared.DocMetaInfo: (
        'drs_keys',
        'drs_path',
        'type_display_name',
        'type',
        'source_key',
        'status',
        'update_date',
        'genealogy',
        'sort_key',
        'id',
        'language',
        'institute',
        'external_ids',
        'create_date',
        'type_sort_key',
        'project',
        'author',
        'source',
        'version',
    ),
    software.SpatialRegridding: (
        'standard_method',
        'properties',
        'dimension',
        'user_method',
    ),
    activity.NumericalActivity: (
        'rationales',
        'supports',
        'description',
        'funding_sources',
        'responsible_parties',
        'long_name',
        'short_name',
        'projects',
    ),
    software.CouplingProperty: (
        'name',
        'value',
    ),
    software.ComponentLanguage: (
        'name',
        'properties',
    ),
    grids.GridSpec: (
        'esm_model_grids',
        'meta',
        'esm_exchange_grids',
    ),
    shared.DocGenealogy: (
        'relationships',
    ),
    shared.Calendar: (
        'length',
        'range',
        'description',
    ),
    activity.PhysicalModification: (
        'sources',
        'frequency',
        'type',
        'requirements',
        'description',
        'is_conformant',
    ),
    shared.DocRelationship: (
        'target',
        'direction',
        'type',
        'description',
    ),
    shared.ClosedDateRange: (
        'duration',
        'end',
        'start',
    ),
    activity.ExperimentRelationship: (
        'description',
        'direction',
        'target',
        'type',
    ),
    shared.RealCalendar: (
        'description',
        'length',
        'range',
    ),
    data.DataHierarchyLevel: (
        'is_open',
        'name',
        'value',
    ),
    shared.Change: (
        'date',
        'details',
        'description',
        'type',
        'name',
        'author',
    ),
    software.SpatialRegriddingProperty: (
        'name',
        'value',
    ),
    activity.SimulationRun: (
        'long_name',
        'authors',
        'spinup_simulation',
        'calendar',
        'inputs',
        'meta',
        'description',
        'projects',
        'control_simulation',
        'spinup_date_range',
        'date_range',
        'funding_sources',
        'supports',
        'simulation_id',
        'model',
        'deployments',
        'rationales',
        'restarts',
        'outputs',
        'conformances',
        'short_name',
        'responsible_parties',
    ),
    software.ConnectionEndpoint: (
        'instance_id',
        'data_source',
        'properties',
    ),
    activity.SimulationRelationshipTarget: (
        'simulation',
        'target',
    ),
    data.DataObject: (
        'parent_object',
        'purpose',
        'distribution',
        'meta',
        'keyword',
        'extent',
        'acronym',
        'geometry_model',
        'child_object',
        'hierarchy_level',
        'citations',
        'purpose',
        'content',
        'storage',
        'properties',
        'data_status',
        'description',
        'restriction',
        'source_simulation',
    ),
    data.DataTopic: (
        'name',
        'unit',
        'description',
    ),
    grids.GridExtent: (
        'units',
        'minimum_latitude',
        'maximum_longitude',
        'minimum_longitude',
        'maximum_latitude',
    ),
    software.Timing: (
        'units',
        'start',
        'rate',
        'is_variable_rate',
        'end',
    ),
    activity.NumericalRequirement: (
        'name',
        'requirement_type',
        'options',
        'source',
        'description',
        'id',
    ),
    grids.SimpleGridGeometry: (
        'xcoords',
        'num_dims',
        'is_mesh',
        'zcoords',
        'dim_order',
        'ycoords',
    ),
    activity.InitialCondition: (
        'source',
        'description',
        'name',
        'id',
        'options',
        'requirement_type',
    ),
    activity.SpatioTemporalConstraint: (
        'id',
        'requirement_type',
        'date_range',
        'source',
        'description',
        'spatial_resolution',
        'options',
        'name',
    ),
    data.DataExtent: (
        'geographical',
        'temporal',
    ),
    data.DataStorageFile: (
        'modification_date',
        'path',
        'size',
        'file_system',
        'format',
        'file_name',
        'location',
    ),
    activity.DownscalingSimulation: (
        'downscaling_id',
        'supports',
        'inputs',
        'downscaled_from',
        'rationales',
        'description',
        'downscaling_type',
        'short_name',
        'projects',
        'responsible_parties',
        'calendar',
        'outputs',
        'meta',
        'funding_sources',
        'long_name',
    ),
    shared.Daily360: (
        'description',
        'length',
        'range',
    ),
    activity.SimulationComposite: (
        'child',
        'long_name',
        'authors',
        'spinup_simulation',
        'date_range',
        'calendar',
        'inputs',
        'rank',
        'description',
        'projects',
        'control_simulation',
        'spinup_date_range',
        'funding_sources',
        'supports',
        'simulation_id',
        'deployments',
        'rationales',
        'restarts',
        'outputs',
        'conformances',
        'meta',
        'short_name',
        'responsible_parties',
    ),
    software.SpatialRegriddingUserMethod: (
        'file',
        'name',
    ),
    software.Deployment: (
        'parallelisation',
        'deployment_date',
        'executable_name',
        'description',
        'executable_arguments',
        'platform',
    ),
    data.DataProperty: (
        'description',
        'value',
        'name',
    ),
    data.DataStorageIp: (
        'protocol',
        'modification_date',
        'host',
        'location',
        'path',
        'format',
        'file_name',
        'size',
    ),
    quality.Measure: (
        'identification',
        'name',
        'description',
    ),
    software.ComponentLanguageProperty: (
        'name',
        'value',
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
    shared.ResponsibleParty: (
        'abbreviation',
        'role',
        'email',
        'url',
        'address',
        'individual_name',
        'organisation_name',
    ),
    data.DataExtentTemporal: (
        'begin',
        'end',
        'time_interval',
    ),
    activity.Experiment: (
        'requires',
        'generates',
        'rationales',
        'responsible_parties',
        'supports',
        'measurement_campaigns',
        'funding_sources',
        'projects',
    ),
    grids.VerticalCoordinateList: (
        'uom',
        'properties',
        'has_constant_offset',
        'length',
        'form',
        'type',
    ),
    grids.GridProperty: (
        'name',
        'value',
    ),
    activity.LateralBoundaryCondition: (
        'source',
        'description',
        'name',
        'id',
        'options',
        'requirement_type',
    ),
    shared.ChangeProperty: (
        'name',
        'value',
        'description',
        'id',
    ),
    grids.GridTileResolutionType: (
        'description',
        'properties',
    ),
    activity.EnsembleMember: (
        'supports',
        'ensemble',
        'rationales',
        'description',
        'ensemble_ids',
        'short_name',
        'projects',
        'responsible_parties',
        'simulation',
        'funding_sources',
        'long_name',
    ),
    software.TimeLag: (
        'units',
        'value',
    ),
    software.StatisticalModelComponent: (
        'timing',
        'online_resource',
        'description',
        'purpose',
        'parent',
        'responsible_parties',
        'funding_sources',
        'grid',
        'code_access',
        'release_date',
        'is_embedded',
        'sub_components',
        'coupling_framework',
        'citations',
        'meta',
        'long_name',
        'properties',
        'version',
        'type',
        'composition',
        'dependencies',
        'language',
        'types',
        'deployments',
        'license',
        'previous_version',
        'short_name',
    ),
    data.DataDistribution: (
        'fee',
        'responsible_party',
        'access',
        'format',
    ),
    quality.CimQuality: (
        'meta',
        'reports',
    ),
    software.Component: (
        'online_resource',
        'is_embedded',
        'description',
        'language',
        'parent',
        'purpose',
        'funding_sources',
        'code_access',
        'grid',
        'release_date',
        'coupling_framework',
        'citations',
        'responsible_parties',
        'long_name',
        'properties',
        'license',
        'composition',
        'dependencies',
        'sub_components',
        'version',
        'deployments',
        'previous_version',
        'short_name',
    ),
    data.DataRestriction: (
        'license',
        'restriction',
        'scope',
    ),
    software.CouplingEndpoint: (
        'instance_id',
        'properties',
        'data_source',
    ),
    shared.Property: (
        'name',
        'value',
    ),
    shared.Platform: (
        'contacts',
        'long_name',
        'units',
        'description',
        'meta',
        'short_name',
    ),
    shared.DataSource: (
        'purpose',
    ),
    grids.GridMosaic: (
        'tiles',
        'description',
        'is_leaf',
        'mosaics',
        'extent',
        'citations',
        'short_name',
        'id',
        'long_name',
        'mnemonic',
        'type',
        'tile_count',
        'mosaic_count',
        'has_congruent_tiles',
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
    shared.License: (
        'description',
        'is_unrestricted',
        'name',
        'contact',
    ),
    activity.ExperimentRelationshipTarget: (
        'numerical_experiment',
    ),
    data.DataStorageDb: (
        'table',
        'size',
        'access_string',
        'format',
        'name',
        'modification_date',
        'owner',
        'location',
    ),
    activity.NumericalRequirementOption: (
        'sub_options',
        'name',
        'relationship',
        'id',
        'description',
    ),
    shared.Standard: (
        'name',
        'version',
        'description',
    ),
    data.DataExtentTimeInterval: (
        'radix',
        'unit',
        'factor',
    ),
    activity.MeasurementCampaign: (
        'duration',
        'rationales',
        'responsible_parties',
        'funding_sources',
        'projects',
    ),
    activity.NumericalExperiment: (
        'experiment_id',
        'funding_sources',
        'requires',
        'requirements',
        'long_name',
        'generates',
        'rationales',
        'meta',
        'projects',
        'responsible_parties',
        'measurement_campaigns',
        'description',
        'short_name',
        'supports',
    ),
    activity.BoundaryCondition: (
        'source',
        'description',
        'name',
        'id',
        'options',
        'requirement_type',
    ),
    shared.Compiler: (
        'type',
        'name',
        'language',
        'options',
        'version',
        'environment_variables',
    ),
    software.ModelComponent: (
        'online_resource',
        'release_date',
        'activity',
        'purpose',
        'parent',
        'responsible_parties',
        'funding_sources',
        'grid',
        'code_access',
        'meta',
        'is_embedded',
        'sub_components',
        'coupling_framework',
        'type',
        'citations',
        'language',
        'properties',
        'version',
        'types',
        'license',
        'composition',
        'dependencies',
        'description',
        'long_name',
        'deployments',
        'timing',
        'previous_version',
        'short_name',
    ),
    activity.OutputRequirement: (
        'source',
        'description',
        'name',
        'id',
        'options',
        'requirement_type',
    ),
    shared.StandardName: (
        'is_open',
        'standards',
        'value',
    ),
    shared.DocRelationshipTarget: (
        'reference',
    ),
    shared.MachineCompilerUnit: (
        'compilers',
        'machine',
    ),
    software.TimeTransformation: (
        'description',
        'mapping_type',
    ),
    software.Rank: (
        'increment',
        'min',
        'value',
        'max',
    ),
    activity.SimulationRelationship: (
        'description',
        'direction',
        'target',
        'type',
    ),
    quality.Evaluation: (
        'type',
        'did_pass',
        'specification_hyperlink',
        'explanation',
        'type_hyperlink',
        'title',
        'specification',
        'description',
        'date',
    ),
    data.DataExtentGeographical: (
        'east',
        'north',
        'south',
        'west',
    ),
    grids.CoordinateList: (
        'length',
        'uom',
        'has_constant_offset',
    ),
    misc.DocumentSet: (
        'meta',
        'grids',
        'data',
        'model',
        'ensembles',
        'platform',
        'experiment',
        'simulation',
    ),
    activity.Simulation: (
        'funding_sources',
        'rationales',
        'deployments',
        'authors',
        'outputs',
        'simulation_id',
        'projects',
        'short_name',
        'inputs',
        'calendar',
        'description',
        'responsible_parties',
        'control_simulation',
        'restarts',
        'spinup_date_range',
        'long_name',
        'conformances',
        'supports',
        'spinup_simulation',
    ),
    software.ComponentProperty: (
        'is_represented',
        'units',
        'long_name',
        'short_name',
        'purpose',
        'grid',
        'sub_properties',
        'description',
        'standard_names',
        'intent',
        'citations',
        'values',
    ),
    software.ConnectionProperty: (
        'name',
        'value',
    ),
    software.Coupling: (
        'description',
        'spatial_regriddings',
        'properties',
        'purpose',
        'time_lag',
        'transformers',
        'sources',
        'is_fully_specified',
        'time_transformation',
        'connections',
        'target',
        'priming',
        'time_profile',
        'type',
    ),
    software.EntryPoint: (
        'name',
    ),
    shared.DateRange: (
        'duration',
    ),
    shared.Machine: (
        'location',
        'type',
        'description',
        'maximum_processors',
        'vendor',
        'cores_per_processor',
        'operating_system',
        'processor_type',
        'interconnect',
        'libraries',
        'system',
        'name',
    ),
}

# Supported class own properties.
CLASS_OWN_PROPERTIES = { 
    shared.DocReference: (
        'type',
        'version',
        'external_id',
        'changes',
        'id',
        'url',
        'name',
        'description',
    ),
    data.DataContent: (
        'aggregation',
        'topic',
        'frequency',
    ),
    shared.PerpetualPeriod: (
    ),
    activity.Ensemble: (
        'types',
        'outputs',
        'members',
        'meta',
    ),
    shared.OpenDateRange: (
        'end',
        'start',
    ),
    shared.Relationship: (
        'description',
        'direction',
    ),
    data.DataStorage: (
        'size',
        'format',
        'modification_date',
        'location',
    ),
    shared.Citation: (
        'location',
        'date_type',
        'date',
        'title',
        'type',
        'alternative_title',
        'collective_title',
        'organisation',
        'role',
    ),
    software.Parallelisation: (
        'processes',
        'ranks',
    ),
    grids.GridTile: (
        'horizontal_resolution',
        'mnemonic',
        'short_name',
        'id',
        'area',
        'is_conformal',
        'zcoords',
        'cell_array',
        'is_uniform',
        'is_terrain_following',
        'coord_file',
        'grid_north_pole',
        'long_name',
        'vertical_resolution',
        'horizontal_crs',
        'is_regular',
        'nx',
        'ny',
        'coordinate_pole',
        'nz',
        'vertical_crs',
        'refinement_scheme',
        'description',
        'simple_grid_geom',
        'discretization_type',
        'extent',
        'cell_ref_array',
        'geometry_type',
    ),
    activity.Activity: (
        'responsible_parties',
        'rationales',
        'funding_sources',
        'projects',
    ),
    activity.Conformance: (
        'sources',
        'frequency',
        'type',
        'is_conformant',
        'requirements',
        'description',
    ),
    quality.Report: (
        'date',
        'measure',
        'evaluator',
        'evaluation',
    ),
    software.ProcessorComponent: (
        'meta',
    ),
    shared.DocMetaInfo: (
        'drs_keys',
        'project',
        'type_sort_key',
        'version',
        'id',
        'create_date',
        'source_key',
        'author',
        'institute',
        'status',
        'genealogy',
        'sort_key',
        'type_display_name',
        'update_date',
        'external_ids',
        'source',
        'drs_path',
        'language',
        'type',
    ),
    software.SpatialRegridding: (
        'standard_method',
        'dimension',
        'user_method',
        'properties',
    ),
    activity.NumericalActivity: (
        'short_name',
        'description',
        'supports',
        'long_name',
    ),
    software.CouplingProperty: (
    ),
    software.ComponentLanguage: (
        'name',
        'properties',
    ),
    grids.GridSpec: (
        'meta',
        'esm_exchange_grids',
        'esm_model_grids',
    ),
    shared.DocGenealogy: (
        'relationships',
    ),
    shared.Calendar: (
        'range',
        'description',
        'length',
    ),
    activity.PhysicalModification: (
    ),
    shared.DocRelationship: (
        'target',
        'type',
    ),
    shared.ClosedDateRange: (
        'end',
        'start',
    ),
    activity.ExperimentRelationship: (
        'target',
        'type',
    ),
    shared.RealCalendar: (
    ),
    data.DataHierarchyLevel: (
        'is_open',
        'value',
        'name',
    ),
    shared.Change: (
        'details',
        'name',
        'author',
        'type',
        'description',
        'date',
    ),
    software.SpatialRegriddingProperty: (
    ),
    activity.SimulationRun: (
        'date_range',
        'model',
        'meta',
    ),
    software.ConnectionEndpoint: (
        'data_source',
        'properties',
        'instance_id',
    ),
    activity.SimulationRelationshipTarget: (
        'simulation',
        'target',
    ),
    data.DataObject: (
        'hierarchy_level',
        'citations',
        'keyword',
        'distribution',
        'purpose',
        'content',
        'properties',
        'child_object',
        'extent',
        'meta',
        'data_status',
        'parent_object',
        'geometry_model',
        'source_simulation',
        'storage',
        'description',
        'restriction',
        'acronym',
    ),
    data.DataTopic: (
        'unit',
        'description',
        'name',
    ),
    grids.GridExtent: (
        'units',
        'maximum_latitude',
        'minimum_longitude',
        'minimum_latitude',
        'maximum_longitude',
    ),
    software.Timing: (
        'start',
        'end',
        'rate',
        'units',
        'is_variable_rate',
    ),
    activity.NumericalRequirement: (
        'requirement_type',
        'source',
        'id',
        'name',
        'options',
        'description',
    ),
    grids.SimpleGridGeometry: (
        'xcoords',
        'is_mesh',
        'dim_order',
        'zcoords',
        'ycoords',
        'num_dims',
    ),
    activity.InitialCondition: (
    ),
    activity.SpatioTemporalConstraint: (
        'date_range',
        'spatial_resolution',
    ),
    data.DataExtent: (
        'geographical',
        'temporal',
    ),
    data.DataStorageFile: (
        'file_system',
        'file_name',
        'path',
    ),
    activity.DownscalingSimulation: (
        'downscaling_id',
        'inputs',
        'calendar',
        'downscaling_type',
        'downscaled_from',
        'outputs',
        'meta',
    ),
    shared.Daily360: (
    ),
    activity.SimulationComposite: (
        'rank',
        'child',
        'meta',
        'date_range',
    ),
    software.SpatialRegriddingUserMethod: (
        'file',
        'name',
    ),
    software.Deployment: (
        'deployment_date',
        'executable_name',
        'executable_arguments',
        'parallelisation',
        'description',
        'platform',
    ),
    data.DataProperty: (
        'description',
    ),
    data.DataStorageIp: (
        'path',
        'protocol',
        'file_name',
        'host',
    ),
    quality.Measure: (
        'name',
        'description',
        'identification',
    ),
    software.ComponentLanguageProperty: (
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
    shared.ResponsibleParty: (
        'email',
        'individual_name',
        'abbreviation',
        'organisation_name',
        'address',
        'role',
        'url',
    ),
    data.DataExtentTemporal: (
        'begin',
        'time_interval',
        'end',
    ),
    activity.Experiment: (
        'measurement_campaigns',
        'generates',
        'supports',
        'requires',
    ),
    grids.VerticalCoordinateList: (
        'type',
        'form',
        'properties',
    ),
    grids.GridProperty: (
    ),
    activity.LateralBoundaryCondition: (
    ),
    shared.ChangeProperty: (
        'description',
        'id',
    ),
    grids.GridTileResolutionType: (
        'description',
        'properties',
    ),
    activity.EnsembleMember: (
        'ensemble',
        'simulation',
        'ensemble_ids',
    ),
    software.TimeLag: (
        'units',
        'value',
    ),
    software.StatisticalModelComponent: (
        'meta',
        'types',
        'type',
        'timing',
    ),
    data.DataDistribution: (
        'responsible_party',
        'format',
        'access',
        'fee',
    ),
    quality.CimQuality: (
        'meta',
        'reports',
    ),
    software.Component: (
        'description',
        'funding_sources',
        'code_access',
        'grid',
        'is_embedded',
        'language',
        'license',
        'parent',
        'long_name',
        'online_resource',
        'release_date',
        'sub_components',
        'citations',
        'properties',
        'composition',
        'previous_version',
        'coupling_framework',
        'short_name',
        'dependencies',
        'responsible_parties',
        'version',
        'deployments',
    ),
    data.DataRestriction: (
        'license',
        'scope',
        'restriction',
    ),
    software.CouplingEndpoint: (
        'properties',
        'data_source',
        'instance_id',
    ),
    shared.Property: (
        'name',
        'value',
    ),
    shared.Platform: (
        'contacts',
        'units',
        'description',
        'long_name',
        'short_name',
        'meta',
    ),
    shared.DataSource: (
        'purpose',
    ),
    grids.GridMosaic: (
        'tiles',
        'mosaic_count',
        'mnemonic',
        'is_leaf',
        'mosaics',
        'extent',
        'citations',
        'short_name',
        'long_name',
        'has_congruent_tiles',
        'type',
        'tile_count',
        'id',
        'description',
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
    shared.License: (
        'is_unrestricted',
        'contact',
        'name',
        'description',
    ),
    activity.ExperimentRelationshipTarget: (
        'numerical_experiment',
    ),
    data.DataStorageDb: (
        'access_string',
        'table',
        'owner',
        'name',
    ),
    activity.NumericalRequirementOption: (
        'sub_options',
        'description',
        'name',
        'relationship',
        'id',
    ),
    shared.Standard: (
        'version',
        'description',
        'name',
    ),
    data.DataExtentTimeInterval: (
        'unit',
        'factor',
        'radix',
    ),
    activity.MeasurementCampaign: (
        'duration',
    ),
    activity.NumericalExperiment: (
        'experiment_id',
        'meta',
        'long_name',
        'requirements',
        'description',
        'short_name',
    ),
    activity.BoundaryCondition: (
    ),
    shared.Compiler: (
        'type',
        'language',
        'name',
        'version',
        'options',
        'environment_variables',
    ),
    software.ModelComponent: (
        'activity',
        'type',
        'meta',
        'types',
        'timing',
    ),
    activity.OutputRequirement: (
    ),
    shared.StandardName: (
        'is_open',
        'value',
        'standards',
    ),
    shared.DocRelationshipTarget: (
        'reference',
    ),
    shared.MachineCompilerUnit: (
        'compilers',
        'machine',
    ),
    software.TimeTransformation: (
        'description',
        'mapping_type',
    ),
    software.Rank: (
        'increment',
        'value',
        'max',
        'min',
    ),
    activity.SimulationRelationship: (
        'target',
        'type',
    ),
    quality.Evaluation: (
        'title',
        'did_pass',
        'explanation',
        'description',
        'type_hyperlink',
        'date',
        'type',
        'specification_hyperlink',
        'specification',
    ),
    data.DataExtentGeographical: (
        'south',
        'west',
        'east',
        'north',
    ),
    grids.CoordinateList: (
        'uom',
        'has_constant_offset',
        'length',
    ),
    misc.DocumentSet: (
        'meta',
        'grids',
        'data',
        'model',
        'ensembles',
        'platform',
        'experiment',
        'simulation',
    ),
    activity.Simulation: (
        'deployments',
        'outputs',
        'simulation_id',
        'inputs',
        'calendar',
        'spinup_simulation',
        'control_simulation',
        'restarts',
        'spinup_date_range',
        'conformances',
        'authors',
    ),
    software.ComponentProperty: (
        'is_represented',
        'short_name',
        'long_name',
        'units',
        'grid',
        'standard_names',
        'sub_properties',
        'description',
        'intent',
        'citations',
        'values',
    ),
    software.ConnectionProperty: (
    ),
    software.Coupling: (
        'description',
        'sources',
        'properties',
        'time_transformation',
        'spatial_regriddings',
        'transformers',
        'purpose',
        'is_fully_specified',
        'priming',
        'time_lag',
        'target',
        'connections',
        'time_profile',
        'type',
    ),
    software.EntryPoint: (
        'name',
    ),
    shared.DateRange: (
        'duration',
    ),
    shared.Machine: (
        'operating_system',
        'location',
        'type',
        'description',
        'maximum_processors',
        'vendor',
        'interconnect',
        'name',
        'processor_type',
        'libraries',
        'cores_per_processor',
        'system',
    ),
}

# Base classes.
BASE_CLASSES = defaultdict(tuple)
BASE_CLASSES[data.DataContent] = (shared.DataSource, )
BASE_CLASSES[shared.PerpetualPeriod] = (shared.Calendar, )
BASE_CLASSES[activity.Ensemble] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[shared.OpenDateRange] = (shared.DateRange, )
BASE_CLASSES[software.ProcessorComponent] = (software.Component, shared.DataSource, )
BASE_CLASSES[activity.NumericalActivity] = (activity.Activity, )
BASE_CLASSES[software.CouplingProperty] = (shared.Property, )
BASE_CLASSES[activity.PhysicalModification] = (activity.Conformance, )
BASE_CLASSES[shared.DocRelationship] = (shared.Relationship, )
BASE_CLASSES[shared.ClosedDateRange] = (shared.DateRange, )
BASE_CLASSES[activity.ExperimentRelationship] = (shared.Relationship, )
BASE_CLASSES[shared.RealCalendar] = (shared.Calendar, )
BASE_CLASSES[software.SpatialRegriddingProperty] = (shared.Property, )
BASE_CLASSES[activity.SimulationRun] = (activity.Simulation, activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[data.DataObject] = (shared.DataSource, )
BASE_CLASSES[activity.InitialCondition] = (activity.NumericalRequirement, )
BASE_CLASSES[activity.SpatioTemporalConstraint] = (activity.NumericalRequirement, )
BASE_CLASSES[data.DataStorageFile] = (data.DataStorage, )
BASE_CLASSES[activity.DownscalingSimulation] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[shared.Daily360] = (shared.Calendar, )
BASE_CLASSES[activity.SimulationComposite] = (activity.Simulation, activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[data.DataProperty] = (shared.Property, )
BASE_CLASSES[data.DataStorageIp] = (data.DataStorage, )
BASE_CLASSES[software.ComponentLanguageProperty] = (shared.Property, )
BASE_CLASSES[activity.Experiment] = (activity.Activity, )
BASE_CLASSES[grids.VerticalCoordinateList] = (grids.CoordinateList, )
BASE_CLASSES[grids.GridProperty] = (shared.Property, )
BASE_CLASSES[activity.LateralBoundaryCondition] = (activity.NumericalRequirement, )
BASE_CLASSES[shared.ChangeProperty] = (shared.Property, )
BASE_CLASSES[activity.EnsembleMember] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[software.StatisticalModelComponent] = (software.Component, shared.DataSource, )
BASE_CLASSES[software.Component] = (shared.DataSource, )
BASE_CLASSES[data.DataStorageDb] = (data.DataStorage, )
BASE_CLASSES[activity.MeasurementCampaign] = (activity.Activity, )
BASE_CLASSES[activity.NumericalExperiment] = (activity.Experiment, activity.Activity, )
BASE_CLASSES[activity.BoundaryCondition] = (activity.NumericalRequirement, )
BASE_CLASSES[software.ModelComponent] = (software.Component, shared.DataSource, )
BASE_CLASSES[activity.OutputRequirement] = (activity.NumericalRequirement, )
BASE_CLASSES[activity.SimulationRelationship] = (shared.Relationship, )
BASE_CLASSES[activity.Simulation] = (activity.NumericalActivity, activity.Activity, )
BASE_CLASSES[software.ComponentProperty] = (shared.DataSource, )
BASE_CLASSES[software.ConnectionProperty] = (shared.Property, )

# Classes with base classes.
BASE_CLASSED = tuple(BASE_CLASSES.keys())

# Sub classes.
SUB_CLASSES = defaultdict(tuple)
SUB_CLASSES[activity.NumericalRequirement] = (
    activity.BoundaryCondition,
    activity.InitialCondition,
    activity.SpatioTemporalConstraint,
    activity.LateralBoundaryCondition,
    activity.OutputRequirement,
    )
SUB_CLASSES[grids.CoordinateList] = (
    grids.VerticalCoordinateList,
    )
SUB_CLASSES[software.Component] = (
    software.StatisticalModelComponent,
    software.ModelComponent,
    software.ProcessorComponent,
    )
SUB_CLASSES[activity.Simulation] = (
    activity.SimulationComposite,
    activity.SimulationRun,
    )
SUB_CLASSES[activity.NumericalActivity] = (
    activity.DownscalingSimulation,
    activity.Simulation,
    activity.EnsembleMember,
    activity.Ensemble,
    activity.SimulationComposite,
    activity.SimulationRun,
    )
SUB_CLASSES[shared.Relationship] = (
    activity.SimulationRelationship,
    activity.ExperimentRelationship,
    shared.DocRelationship,
    )
SUB_CLASSES[data.DataStorage] = (
    data.DataStorageDb,
    data.DataStorageFile,
    data.DataStorageIp,
    )
SUB_CLASSES[activity.Experiment] = (
    activity.NumericalExperiment,
    )
SUB_CLASSES[shared.DataSource] = (
    software.Component,
    software.ComponentProperty,
    data.DataObject,
    data.DataContent,
    software.StatisticalModelComponent,
    software.ModelComponent,
    software.ProcessorComponent,
    )
SUB_CLASSES[activity.Conformance] = (
    activity.PhysicalModification,
    )
SUB_CLASSES[activity.Activity] = (
    activity.Experiment,
    activity.MeasurementCampaign,
    activity.NumericalActivity,
    activity.DownscalingSimulation,
    activity.Simulation,
    activity.NumericalExperiment,
    activity.EnsembleMember,
    activity.Ensemble,
    activity.SimulationComposite,
    activity.SimulationRun,
    )
SUB_CLASSES[shared.Calendar] = (
    shared.Daily360,
    shared.PerpetualPeriod,
    shared.RealCalendar,
    )
SUB_CLASSES[shared.DateRange] = (
    shared.ClosedDateRange,
    shared.OpenDateRange,
    )
SUB_CLASSES[shared.Property] = (
    software.CouplingProperty,
    software.ComponentLanguageProperty,
    software.ConnectionProperty,
    software.SpatialRegriddingProperty,
    grids.GridProperty,
    shared.ChangeProperty,
    data.DataProperty,
    )

# Classes that have been sub classed.
SUB_CLASSED = tuple(SUB_CLASSES.keys())

# Maximum class depth in hierarchy.
CLASS_HIERACHY_DEPTH = max(len(v) for v in BASE_CLASSES.values())

# Set type keys.
# TODO deprecate
software.Rank.type_key = u"cim.1.software.Rank"
software.Parallelisation.type_key = u"cim.1.software.Parallelisation"
software.CouplingProperty.type_key = u"cim.1.software.CouplingProperty"
software.SpatialRegridding.type_key = u"cim.1.software.SpatialRegridding"
software.SpatialRegriddingUserMethod.type_key = u"cim.1.software.SpatialRegriddingUserMethod"
software.ComponentLanguageProperty.type_key = u"cim.1.software.ComponentLanguageProperty"
software.Composition.type_key = u"cim.1.software.Composition"
software.TimeLag.type_key = u"cim.1.software.TimeLag"
software.Connection.type_key = u"cim.1.software.Connection"
software.Timing.type_key = u"cim.1.software.Timing"
software.StatisticalModelComponent.type_key = u"cim.1.software.StatisticalModelComponent"
software.TimeTransformation.type_key = u"cim.1.software.TimeTransformation"
software.ConnectionProperty.type_key = u"cim.1.software.ConnectionProperty"
software.Coupling.type_key = u"cim.1.software.Coupling"
software.Component.type_key = u"cim.1.software.Component"
software.CouplingEndpoint.type_key = u"cim.1.software.CouplingEndpoint"
software.ComponentProperty.type_key = u"cim.1.software.ComponentProperty"
software.Deployment.type_key = u"cim.1.software.Deployment"
software.EntryPoint.type_key = u"cim.1.software.EntryPoint"
software.ModelComponent.type_key = u"cim.1.software.ModelComponent"
software.ProcessorComponent.type_key = u"cim.1.software.ProcessorComponent"
software.ComponentLanguage.type_key = u"cim.1.software.ComponentLanguage"
software.SpatialRegriddingProperty.type_key = u"cim.1.software.SpatialRegriddingProperty"
software.ConnectionEndpoint.type_key = u"cim.1.software.ConnectionEndpoint"
quality.Report.type_key = u"cim.1.quality.Report"
quality.Evaluation.type_key = u"cim.1.quality.Evaluation"
quality.Measure.type_key = u"cim.1.quality.Measure"
quality.CimQuality.type_key = u"cim.1.quality.CimQuality"
grids.VerticalCoordinateList.type_key = u"cim.1.grids.VerticalCoordinateList"
grids.GridSpec.type_key = u"cim.1.grids.GridSpec"
grids.CoordinateList.type_key = u"cim.1.grids.CoordinateList"
grids.GridTile.type_key = u"cim.1.grids.GridTile"
grids.GridExtent.type_key = u"cim.1.grids.GridExtent"
grids.GridTileResolutionType.type_key = u"cim.1.grids.GridTileResolutionType"
grids.GridMosaic.type_key = u"cim.1.grids.GridMosaic"
grids.SimpleGridGeometry.type_key = u"cim.1.grids.SimpleGridGeometry"
grids.GridProperty.type_key = u"cim.1.grids.GridProperty"
activity.NumericalRequirement.type_key = u"cim.1.activity.NumericalRequirement"
activity.ExperimentRelationshipTarget.type_key = u"cim.1.activity.ExperimentRelationshipTarget"
activity.BoundaryCondition.type_key = u"cim.1.activity.BoundaryCondition"
activity.Activity.type_key = u"cim.1.activity.Activity"
activity.InitialCondition.type_key = u"cim.1.activity.InitialCondition"
activity.Conformance.type_key = u"cim.1.activity.Conformance"
activity.Experiment.type_key = u"cim.1.activity.Experiment"
activity.DownscalingSimulation.type_key = u"cim.1.activity.DownscalingSimulation"
activity.PhysicalModification.type_key = u"cim.1.activity.PhysicalModification"
activity.Simulation.type_key = u"cim.1.activity.Simulation"
activity.NumericalExperiment.type_key = u"cim.1.activity.NumericalExperiment"
activity.EnsembleMember.type_key = u"cim.1.activity.EnsembleMember"
activity.SimulationComposite.type_key = u"cim.1.activity.SimulationComposite"
activity.SimulationRelationship.type_key = u"cim.1.activity.SimulationRelationship"
activity.NumericalRequirementOption.type_key = u"cim.1.activity.NumericalRequirementOption"
activity.ExperimentRelationship.type_key = u"cim.1.activity.ExperimentRelationship"
activity.SimulationRelationshipTarget.type_key = u"cim.1.activity.SimulationRelationshipTarget"
activity.SpatioTemporalConstraint.type_key = u"cim.1.activity.SpatioTemporalConstraint"
activity.SimulationRun.type_key = u"cim.1.activity.SimulationRun"
activity.LateralBoundaryCondition.type_key = u"cim.1.activity.LateralBoundaryCondition"
activity.OutputRequirement.type_key = u"cim.1.activity.OutputRequirement"
activity.MeasurementCampaign.type_key = u"cim.1.activity.MeasurementCampaign"
activity.Ensemble.type_key = u"cim.1.activity.Ensemble"
activity.NumericalActivity.type_key = u"cim.1.activity.NumericalActivity"
shared.Relationship.type_key = u"cim.1.shared.Relationship"
shared.Standard.type_key = u"cim.1.shared.Standard"
shared.StandardName.type_key = u"cim.1.shared.StandardName"
shared.Daily360.type_key = u"cim.1.shared.Daily360"
shared.License.type_key = u"cim.1.shared.License"
shared.ClosedDateRange.type_key = u"cim.1.shared.ClosedDateRange"
shared.DocRelationship.type_key = u"cim.1.shared.DocRelationship"
shared.MachineCompilerUnit.type_key = u"cim.1.shared.MachineCompilerUnit"
shared.DateRange.type_key = u"cim.1.shared.DateRange"
shared.ChangeProperty.type_key = u"cim.1.shared.ChangeProperty"
shared.Citation.type_key = u"cim.1.shared.Citation"
shared.DocRelationshipTarget.type_key = u"cim.1.shared.DocRelationshipTarget"
shared.Platform.type_key = u"cim.1.shared.Platform"
shared.OpenDateRange.type_key = u"cim.1.shared.OpenDateRange"
shared.DocMetaInfo.type_key = u"cim.1.shared.DocMetaInfo"
shared.Property.type_key = u"cim.1.shared.Property"
shared.PerpetualPeriod.type_key = u"cim.1.shared.PerpetualPeriod"
shared.Calendar.type_key = u"cim.1.shared.Calendar"
shared.DocGenealogy.type_key = u"cim.1.shared.DocGenealogy"
shared.RealCalendar.type_key = u"cim.1.shared.RealCalendar"
shared.Change.type_key = u"cim.1.shared.Change"
shared.DocReference.type_key = u"cim.1.shared.DocReference"
shared.Compiler.type_key = u"cim.1.shared.Compiler"
shared.DataSource.type_key = u"cim.1.shared.DataSource"
shared.Machine.type_key = u"cim.1.shared.Machine"
shared.ResponsibleParty.type_key = u"cim.1.shared.ResponsibleParty"
misc.DocumentSet.type_key = u"cim.1.misc.DocumentSet"
data.DataStorageDb.type_key = u"cim.1.data.DataStorageDb"
data.DataObject.type_key = u"cim.1.data.DataObject"
data.DataExtentGeographical.type_key = u"cim.1.data.DataExtentGeographical"
data.DataContent.type_key = u"cim.1.data.DataContent"
data.DataStorageFile.type_key = u"cim.1.data.DataStorageFile"
data.DataProperty.type_key = u"cim.1.data.DataProperty"
data.DataExtentTemporal.type_key = u"cim.1.data.DataExtentTemporal"
data.DataDistribution.type_key = u"cim.1.data.DataDistribution"
data.DataStorageIp.type_key = u"cim.1.data.DataStorageIp"
data.DataRestriction.type_key = u"cim.1.data.DataRestriction"
data.DataExtentTimeInterval.type_key = u"cim.1.data.DataExtentTimeInterval"
data.DataExtent.type_key = u"cim.1.data.DataExtent"
data.DataTopic.type_key = u"cim.1.data.DataTopic"
data.DataStorage.type_key = u"cim.1.data.DataStorage"
data.DataHierarchyLevel.type_key = u"cim.1.data.DataHierarchyLevel"
software.SpatialRegriddingStandardMethodType.type_key = u"cim.1.software.SpatialRegriddingStandardMethodType"
software.StatisticalModelComponentType.type_key = u"cim.1.software.StatisticalModelComponentType"
software.TimeMappingType.type_key = u"cim.1.software.TimeMappingType"
software.TimingUnits.type_key = u"cim.1.software.TimingUnits"
software.ComponentPropertyIntentType.type_key = u"cim.1.software.ComponentPropertyIntentType"
software.ConnectionType.type_key = u"cim.1.software.ConnectionType"
software.CouplingFrameworkType.type_key = u"cim.1.software.CouplingFrameworkType"
software.ModelComponentType.type_key = u"cim.1.software.ModelComponentType"
software.SpatialRegriddingDimensionType.type_key = u"cim.1.software.SpatialRegriddingDimensionType"
quality.QualityIssueType.type_key = u"cim.1.quality.QualityIssueType"
quality.QualitySeverityType.type_key = u"cim.1.quality.QualitySeverityType"
quality.CimFeatureType.type_key = u"cim.1.quality.CimFeatureType"
quality.QualityStatusType.type_key = u"cim.1.quality.QualityStatusType"
quality.CimResultType.type_key = u"cim.1.quality.CimResultType"
quality.CimScopeCodeType.type_key = u"cim.1.quality.CimScopeCodeType"
grids.RefinementTypeEnum.type_key = u"cim.1.grids.RefinementTypeEnum"
grids.GridNodePositionEnum.type_key = u"cim.1.grids.GridNodePositionEnum"
grids.ArcTypeEnum.type_key = u"cim.1.grids.ArcTypeEnum"
grids.VerticalCsEnum.type_key = u"cim.1.grids.VerticalCsEnum"
grids.GridTypeEnum.type_key = u"cim.1.grids.GridTypeEnum"
grids.DiscretizationEnum.type_key = u"cim.1.grids.DiscretizationEnum"
grids.HorizontalCsEnum.type_key = u"cim.1.grids.HorizontalCsEnum"
grids.FeatureTypeEnum.type_key = u"cim.1.grids.FeatureTypeEnum"
grids.GeometryTypeEnum.type_key = u"cim.1.grids.GeometryTypeEnum"
activity.ProjectType.type_key = u"cim.1.activity.ProjectType"
activity.ResolutionType.type_key = u"cim.1.activity.ResolutionType"
activity.SimulationRelationshipType.type_key = u"cim.1.activity.SimulationRelationshipType"
activity.SimulationType.type_key = u"cim.1.activity.SimulationType"
activity.ConformanceType.type_key = u"cim.1.activity.ConformanceType"
activity.DownscalingType.type_key = u"cim.1.activity.DownscalingType"
activity.EnsembleType.type_key = u"cim.1.activity.EnsembleType"
activity.ExperimentRelationshipType.type_key = u"cim.1.activity.ExperimentRelationshipType"
activity.FrequencyType.type_key = u"cim.1.activity.FrequencyType"
shared.DocRelationshipDirectionType.type_key = u"cim.1.shared.DocRelationshipDirectionType"
shared.CompilerType.type_key = u"cim.1.shared.CompilerType"
shared.DocRelationshipType.type_key = u"cim.1.shared.DocRelationshipType"
shared.DataPurpose.type_key = u"cim.1.shared.DataPurpose"
shared.DocStatusType.type_key = u"cim.1.shared.DocStatusType"
shared.InterconnectType.type_key = u"cim.1.shared.InterconnectType"
shared.UnitType.type_key = u"cim.1.shared.UnitType"
shared.DocType.type_key = u"cim.1.shared.DocType"
shared.MachineVendorType.type_key = u"cim.1.shared.MachineVendorType"
shared.ProcessorType.type_key = u"cim.1.shared.ProcessorType"
shared.ChangePropertyType.type_key = u"cim.1.shared.ChangePropertyType"
shared.MachineType.type_key = u"cim.1.shared.MachineType"
shared.OperatingSystemType.type_key = u"cim.1.shared.OperatingSystemType"
data.DataStatusType.type_key = u"cim.1.data.DataStatusType"
data.DataHierarchyType.type_key = u"cim.1.data.DataHierarchyType"

