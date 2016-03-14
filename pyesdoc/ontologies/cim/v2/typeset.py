
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from collections import defaultdict
import datetime
import uuid

from typeset_for_activity_package import *
from typeset_for_science_package import *
from typeset_for_software_package import *
from typeset_for_designing_package import *
from typeset_for_data_package import *
from typeset_for_drs_package import *
from typeset_for_shared_package import *
from typeset_for_platform_package import *


import typeset_for_activity_package as activity
import typeset_for_science_package as science
import typeset_for_software_package as software
import typeset_for_designing_package as designing
import typeset_for_data_package as data
import typeset_for_drs_package as drs
import typeset_for_shared_package as shared
import typeset_for_platform_package as platform



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
    activity,
    science,
    software,
    designing,
    data,
    drs,
    shared,
    platform,
    # Classes
    ComputePool,
    DatetimeSet,
    ParentSimulation,
    EnsembleRequirement,
    Activity,
    Downscaling,
    DrsPublicationDataset,
    DrsEnsembleIdentifier,
    OnlineResource,
    MultiTimeEnsemble,
    Dataset,
    Performance,
    ScientificDomain,
    DomainProperties,
    IrregularDateset,
    Ensemble,
    MultiEnsemble,
    Process,
    DocReference,
    Cimtext,
    Machine,
    Partition,
    SoftwareComponent,
    EntryPoint,
    Party,
    Composition,
    ConservationProperties,
    Project,
    TemporalConstraint,
    DateTime,
    DocMetaInfo,
    RegularTimeset,
    Variable,
    Model,
    Conformance,
    OutputTemporalRequirement,
    Pid,
    KeyFloat,
    Tuning,
    EnsembleAxis,
    NumericalExperiment,
    Gridspec,
    Calendar,
    StorageVolume,
    DevelopmentPath,
    VariableCollection,
    SimulationPlan,
    Algorithm,
    EnsembleMember,
    SubProcess,
    ScienceContext,
    DrsTemporalIdentifier,
    TimesliceList,
    ComponentBase,
    Simulation,
    KeyProperties,
    DrsAtomicDataset,
    Reference,
    Grid,
    TimePeriod,
    Extent,
    AxisMember,
    ExternalDocument,
    Detail,
    Responsibility,
    Resolution,
    ComponentPerformance,
    NumericalRequirement,
    UberEnsemble,
    ForcingConstraint,
    NumberArray,
    DrsGeographicalIndicator,
    QualityReview,
    StoragePool,
    # Enums
    VolumeUnits,
    DocumentTypes,
    StorageSystems,
    ForcingTypes,
    ModelTypes,
    CalendarTypes,
    NilReason,
    PeriodDateTypes,
    RoleCode,
    TimeUnits,
    EnsembleTypes,
    DrsGeographicalOperators,
    SlicetimeUnits,
    DrsRealms,
    EnsembleTypes,
    ExperimentalRelationships,
    DrsTimeSuffixes,
    DataAssociationTypes,
    TextCode,
    ForcingTypes,
    SelectionCardinality,
    ProgrammingLanguage,
    QualityStatus,
    DrsFrequencyTypes,
    CouplingFramework,
]

# Supported packages.
PACKAGES = (
    activity,
    science,
    software,
    designing,
    data,
    drs,
    shared,
    platform,
)

# Supported classes.
CLASSES = (
    platform.ComputePool,
    shared.DatetimeSet,
    activity.ParentSimulation,
    designing.EnsembleRequirement,
    activity.Activity,
    data.Downscaling,
    drs.DrsPublicationDataset,
    drs.DrsEnsembleIdentifier,
    shared.OnlineResource,
    designing.MultiTimeEnsemble,
    data.Dataset,
    platform.Performance,
    science.ScientificDomain,
    designing.DomainProperties,
    shared.IrregularDateset,
    activity.Ensemble,
    designing.MultiEnsemble,
    science.Process,
    shared.DocReference,
    shared.Cimtext,
    platform.Machine,
    platform.Partition,
    software.SoftwareComponent,
    software.EntryPoint,
    shared.Party,
    software.Composition,
    science.ConservationProperties,
    designing.Project,
    designing.TemporalConstraint,
    shared.DateTime,
    shared.DocMetaInfo,
    shared.RegularTimeset,
    software.Variable,
    science.Model,
    activity.Conformance,
    designing.OutputTemporalRequirement,
    shared.Pid,
    shared.KeyFloat,
    science.Tuning,
    activity.EnsembleAxis,
    designing.NumericalExperiment,
    software.Gridspec,
    shared.Calendar,
    platform.StorageVolume,
    software.DevelopmentPath,
    data.VariableCollection,
    designing.SimulationPlan,
    science.Algorithm,
    activity.EnsembleMember,
    science.SubProcess,
    science.ScienceContext,
    drs.DrsTemporalIdentifier,
    shared.TimesliceList,
    software.ComponentBase,
    data.Simulation,
    science.KeyProperties,
    drs.DrsAtomicDataset,
    shared.Reference,
    science.Grid,
    shared.TimePeriod,
    science.Extent,
    activity.AxisMember,
    shared.ExternalDocument,
    science.Detail,
    shared.Responsibility,
    science.Resolution,
    platform.ComponentPerformance,
    designing.NumericalRequirement,
    activity.UberEnsemble,
    designing.ForcingConstraint,
    shared.NumberArray,
    drs.DrsGeographicalIndicator,
    shared.QualityReview,
    platform.StoragePool,
)

# Supported enums.
ENUMS = (
    platform.VolumeUnits,
    shared.DocumentTypes,
    platform.StorageSystems,
    designing.ForcingTypes,
    science.ModelTypes,
    shared.CalendarTypes,
    shared.NilReason,
    shared.PeriodDateTypes,
    shared.RoleCode,
    shared.TimeUnits,
    designing.EnsembleTypes,
    drs.DrsGeographicalOperators,
    shared.SlicetimeUnits,
    drs.DrsRealms,
    activity.EnsembleTypes,
    designing.ExperimentalRelationships,
    drs.DrsTimeSuffixes,
    data.DataAssociationTypes,
    shared.TextCode,
    activity.ForcingTypes,
    science.SelectionCardinality,
    software.ProgrammingLanguage,
    shared.QualityStatus,
    drs.DrsFrequencyTypes,
    software.CouplingFramework,
)

# Supported document types.
DOCUMENT_TYPES = (
    activity.Activity,
    activity.UberEnsemble,
    activity.Conformance,
    activity.Ensemble,
    science.Grid,
    science.ScientificDomain,
    science.Model,
    designing.TemporalConstraint,
    designing.NumericalRequirement,
    designing.EnsembleRequirement,
    designing.OutputTemporalRequirement,
    designing.MultiEnsemble,
    designing.Project,
    designing.MultiTimeEnsemble,
    designing.SimulationPlan,
    designing.NumericalExperiment,
    designing.ForcingConstraint,
    designing.DomainProperties,
    data.Downscaling,
    data.Dataset,
    data.Simulation,
    shared.ExternalDocument,
    shared.Party,
    platform.Machine,
    platform.Performance,
)

# Supported class properties.
CLASS_PROPERTIES = { 
    platform.ComputePool: (
        'compute_cores_per_node',
        'accelerators_per_node',
        'interconnect',
        'memory_per_node',
        'cpu_type',
        'name',
        'accelerator_type',
        'description',
        'model_number',
        'operating_system',
        'number_of_nodes',
    ),
    shared.DatetimeSet: (
        'length',
    ),
    activity.ParentSimulation: (
        'branch_time_in_parent',
        'parent',
        'branch_time_in_child',
    ),
    designing.EnsembleRequirement: (
        'minimum_size',
        'duration',
        'rationale',
        'additional_requirements',
        'ensemble_member',
        'canonical_name',
        'name',
        'long_name',
        'conformance_is_requested',
        'references',
        'keywords',
        'ensemble_type',
        'description',
        'meta',
        'responsible_parties',
    ),
    activity.Activity: (
        'duration',
        'name',
        'keywords',
        'canonical_name',
        'references',
        'long_name',
        'description',
        'responsible_parties',
        'meta',
        'rationale',
    ),
    data.Downscaling: (
        'ensemble_identifier',
        'duration',
        'parent_simulation',
        'part_of_project',
        'downscaled_from',
        'meta',
        'primary_ensemble',
        'responsible_parties',
        'name',
        'ran_for_experiments',
        'long_name',
        'calendar',
        'rationale',
        'canonical_name',
        'used',
        'references',
        'keywords',
        'description',
    ),
    drs.DrsPublicationDataset: (
        'product',
        'activity',
        'experiment',
        'realm',
        'institute',
        'version_number',
        'frequency',
        'model',
    ),
    drs.DrsEnsembleIdentifier: (
        'perturbation_number',
        'realisation_number',
        'initialisation_method_number',
    ),
    shared.OnlineResource: (
        'description',
        'linkage',
        'name',
        'protocol',
    ),
    designing.MultiTimeEnsemble: (
        'meta',
        'duration',
        'name',
        'ensemble_members',
        'canonical_name',
        'additional_requirements',
        'references',
        'long_name',
        'conformance_is_requested',
        'rationale',
        'description',
        'keywords',
        'responsible_parties',
    ),
    data.Dataset: (
        'meta',
        'availability',
        'related_to_dataset',
        'name',
        'description',
        'produced_by',
        'drs_datasets',
        'responsible_parties',
        'references',
    ),
    platform.Performance: (
        'sypd',
        'io_load',
        'load_imbalance',
        'total_nodes_used',
        'memory_bloat',
        'platform',
        'meta',
        'name',
        'chsy',
        'subcomponent_performance',
        'coupler_load',
        'model',
        'asypd',
        'compiler',
    ),
    science.ScientificDomain: (
        'meta',
        'differing_key_properties',
        'name',
        'realm',
        'overview',
        'simulates',
        'id',
        'references',
    ),
    designing.DomainProperties: (
        'duration',
        'name',
        'rationale',
        'canonical_name',
        'additional_requirements',
        'references',
        'long_name',
        'conformance_is_requested',
        'required_extent',
        'keywords',
        'description',
        'required_resolution',
        'meta',
        'responsible_parties',
    ),
    shared.IrregularDateset: (
        'length',
        'date_set',
    ),
    activity.Ensemble: (
        'duration',
        'documentation',
        'name',
        'keywords',
        'has_ensemble_axes',
        'description',
        'members',
        'meta',
        'responsible_parties',
        'part_of',
        'references',
        'supported',
        'long_name',
        'canonical_name',
        'rationale',
        'common_conformances',
    ),
    designing.MultiEnsemble: (
        'duration',
        'name',
        'rationale',
        'canonical_name',
        'additional_requirements',
        'long_name',
        'references',
        'ensemble_axis',
        'conformance_is_requested',
        'keywords',
        'description',
        'meta',
        'responsible_parties',
    ),
    science.Process: (
        'algorithms',
        'references',
        'implementation_overview',
        'id',
        'context',
        'keywords',
        'name',
        'properties',
        'sub_processes',
    ),
    shared.DocReference: (
        'protocol',
        'version',
        'name',
        'linkage',
        'description',
        'context',
        'relationship',
        'constraint_vocabulary',
        'type',
        'id',
    ),
    shared.Cimtext: (
        'content',
        'content_type',
    ),
    platform.Machine: (
        'model_number',
        'compute_pools',
        'meta',
        'description',
        'name',
        'online_documentation',
        'storage_pools',
        'vendor',
        'institution',
        'partition',
        'when_used',
    ),
    platform.Partition: (
        'model_number',
        'institution',
        'name',
        'online_documentation',
        'vendor',
        'description',
        'storage_pools',
        'compute_pools',
        'partition',
        'when_used',
    ),
    software.SoftwareComponent: (
        'dependencies',
        'description',
        'name',
        'sub_components',
        'version',
        'connection_points',
        'composition',
        'documentation',
        'language',
        'long_name',
        'release_date',
        'repository',
        'grid',
        'coupling_framework',
        'license',
        'development_history',
    ),
    software.EntryPoint: (
        'name',
    ),
    shared.Party: (
        'organisation',
        'name',
        'address',
        'email',
        'url',
        'orcid_id',
        'meta',
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
    science.ConservationProperties: (
        'corrected_conserved_prognostic_variables',
        'correction_methodology',
        'flux_correction_was_used',
    ),
    designing.Project: (
        'duration',
        'previous_projects',
        'name',
        'keywords',
        'requires_experiments',
        'long_name',
        'references',
        'rationale',
        'canonical_name',
        'description',
        'sub_projects',
        'meta',
        'responsible_parties',
    ),
    designing.TemporalConstraint: (
        'duration',
        'required_calendar',
        'keywords',
        'required_duration',
        'long_name',
        'start_date',
        'conformance_is_requested',
        'meta',
        'start_flexibility',
        'responsible_parties',
        'name',
        'canonical_name',
        'rationale',
        'additional_requirements',
        'references',
        'description',
    ),
    shared.DateTime: (
        'offset',
        'value',
    ),
    shared.DocMetaInfo: (
        'institute',
        'type_sort_key',
        'language',
        'drs_path',
        'update_date',
        'project',
        'version',
        'sort_key',
        'source',
        'id',
        'drs_keys',
        'source_key',
        'create_date',
        'author',
        'external_ids',
        'type_display_name',
        'type',
    ),
    shared.RegularTimeset: (
        'increment',
        'length',
        'length',
        'start_date',
    ),
    software.Variable: (
        'prognostic',
        'name',
        'description',
    ),
    science.Model: (
        'description',
        'name',
        'coupler',
        'version',
        'coupled_components',
        'release_date',
        'simulates',
        'id',
        'documentation',
        'development_history',
        'repository',
        'internal_software_components',
        'long_name',
        'model_default_properties',
        'meta',
        'category',
    ),
    activity.Conformance: (
        'duration',
        'name',
        'keywords',
        'long_name',
        'references',
        'canonical_name',
        'target_requirement',
        'responsible_parties',
        'description',
        'meta',
        'rationale',
    ),
    designing.OutputTemporalRequirement: (
        'throughout',
        'duration',
        'rationale',
        'canonical_name',
        'additional_requirements',
        'long_name',
        'name',
        'continuous_subset',
        'conformance_is_requested',
        'references',
        'keywords',
        'sliced_subset',
        'description',
        'meta',
        'responsible_parties',
    ),
    shared.Pid: (
        'id',
        'resolution_service',
    ),
    shared.KeyFloat: (
        'key',
        'value',
    ),
    science.Tuning: (
        'description',
        'global_mean_metrics_used',
        'regional_metrics_used',
        'trend_metrics_used',
    ),
    activity.EnsembleAxis: (
        'member',
        'short_identifier',
        'target_requirement',
        'extra_detail',
    ),
    designing.NumericalExperiment: (
        'duration',
        'related_experiments',
        'name',
        'keywords',
        'canonical_name',
        'long_name',
        'references',
        'requirements',
        'responsible_parties',
        'description',
        'meta',
        'rationale',
    ),
    software.Gridspec: (
        'description',
    ),
    shared.Calendar: (
        'month_lengths',
        'description',
        'name',
        'standard_name',
    ),
    platform.StorageVolume: (
        'units',
        'volume',
    ),
    software.DevelopmentPath: (
        'consortium_name',
        'funding_sources',
        'creators',
        'developed_in_house',
        'previous_version',
    ),
    data.VariableCollection: (
        'variables',
        'collection_name',
    ),
    designing.SimulationPlan: (
        'expected_performance_sypd',
        'rationale',
        'duration',
        'expected_platform',
        'canonical_name',
        'long_name',
        'name',
        'will_support_experiments',
        'references',
        'keywords',
        'expected_model',
        'description',
        'meta',
        'responsible_parties',
    ),
    science.Algorithm: (
        'forced_variables',
        'context',
        'implementation_overview',
        'diagnostic_variables',
        'id',
        'prognostic_variables',
        'name',
        'references',
    ),
    activity.EnsembleMember: (
        'errata',
        'variant_id',
        'ran_on',
        'had_performance',
        'simulation',
    ),
    science.SubProcess: (
        'properties',
        'id',
        'name',
        'context',
        'references',
        'implementation_overview',
    ),
    science.ScienceContext: (
        'context',
        'id',
        'name',
    ),
    drs.DrsTemporalIdentifier: (
        'start',
        'suffix',
        'end',
    ),
    shared.TimesliceList: (
        'members',
        'units',
    ),
    software.ComponentBase: (
        'description',
        'documentation',
        'name',
        'release_date',
        'repository',
        'long_name',
        'development_history',
        'version',
    ),
    data.Simulation: (
        'ensemble_identifier',
        'duration',
        'parent_simulation',
        'name',
        'part_of_project',
        'description',
        'primary_ensemble',
        'meta',
        'responsible_parties',
        'ran_for_experiments',
        'references',
        'rationale',
        'used',
        'long_name',
        'canonical_name',
        'keywords',
        'calendar',
    ),
    science.KeyProperties: (
        'resolution',
        'grid',
        'additional_detail',
        'tuning_applied',
        'time_step',
        'extra_conservation_properties',
    ),
    drs.DrsAtomicDataset: (
        'product',
        'frequency',
        'ensemble_member',
        'mip_table',
        'institute',
        'geographical_constraint',
        'temporal_constraint',
        'experiment',
        'version_number',
        'realm',
        'activity',
        'model',
        'variable_name',
    ),
    shared.Reference: (
        'context',
        'document',
    ),
    science.Grid: (
        'additional_details',
        'meta',
        'name',
        'grid_extent',
        'vertical_grid_layout',
        'horizontal_grid_type',
        'vertical_grid_type',
        'horizontal_grid_layout',
    ),
    shared.TimePeriod: (
        'calendar',
        'date',
        'units',
        'length',
        'date_type',
    ),
    science.Extent: (
        'z_units',
        'top_vertical_level',
        'is_global',
        'northern_boundary',
        'southern_boundary',
        'region_known_as',
        'western_boundary',
        'eastern_boundary',
        'bottom_vertical_level',
    ),
    activity.AxisMember: (
        'description',
        'extra_detail',
        'value',
        'index',
    ),
    shared.ExternalDocument: (
        'authorship',
        'online_at',
        'name',
        'date',
        'publication_detail',
        'meta',
        'title',
        'doi',
    ),
    science.Detail: (
        'with_cardinality',
        'name',
        'id',
        'detail_selection',
        'from_vocab',
        'context',
        'select',
        'content',
    ),
    shared.Responsibility: (
        'role',
        'when',
        'party',
    ),
    science.Resolution: (
        'typical_x_degrees',
        'equivalent_resolution_km',
        'typical_y_degrees',
        'number_of_xy_gridpoints',
        'number_of_levels',
        'is_adaptive_grid',
        'name',
    ),
    platform.ComponentPerformance: (
        'component_name',
        'component',
        'cores_used',
        'nodes_used',
        'speed',
    ),
    designing.NumericalRequirement: (
        'duration',
        'rationale',
        'name',
        'keywords',
        'additional_requirements',
        'long_name',
        'references',
        'canonical_name',
        'description',
        'conformance_is_requested',
        'meta',
        'responsible_parties',
    ),
    activity.UberEnsemble: (
        'duration',
        'documentation',
        'part_of',
        'keywords',
        'has_ensemble_axes',
        'description',
        'members',
        'meta',
        'responsible_parties',
        'name',
        'common_conformances',
        'long_name',
        'supported',
        'canonical_name',
        'references',
        'rationale',
        'child_ensembles',
    ),
    designing.ForcingConstraint: (
        'duration',
        'code',
        'keywords',
        'data_link',
        'long_name',
        'forcing_type',
        'description',
        'meta',
        'group',
        'responsible_parties',
        'name',
        'origin',
        'references',
        'rationale',
        'canonical_name',
        'additional_requirements',
        'additional_constraint',
        'conformance_is_requested',
        'category',
    ),
    shared.NumberArray: (
        'values',
    ),
    drs.DrsGeographicalIndicator: (
        'spatial_domain',
        'bounding_box',
        'operator',
    ),
    shared.QualityReview: (
        'metadata_reviewer',
        'quality_description',
        'date',
        'quality_status',
    ),
    platform.StoragePool: (
        'name',
        'description',
        'type',
        'volume_available',
        'vendor',
    ),
}

# Supported class own properties.
CLASS_OWN_PROPERTIES = { 
    platform.ComputePool: (
        'compute_cores_per_node',
        'memory_per_node',
        'name',
        'description',
        'cpu_type',
        'accelerator_type',
        'model_number',
        'number_of_nodes',
        'accelerators_per_node',
        'operating_system',
        'interconnect',
    ),
    shared.DatetimeSet: (
        'length',
    ),
    activity.ParentSimulation: (
        'parent',
        'branch_time_in_child',
        'branch_time_in_parent',
    ),
    designing.EnsembleRequirement: (
        'ensemble_type',
        'ensemble_member',
        'minimum_size',
    ),
    activity.Activity: (
        'duration',
        'responsible_parties',
        'long_name',
        'keywords',
        'name',
        'canonical_name',
        'references',
        'description',
        'meta',
        'rationale',
    ),
    data.Downscaling: (
        'downscaled_from',
    ),
    drs.DrsPublicationDataset: (
        'product',
        'realm',
        'experiment',
        'frequency',
        'institute',
        'version_number',
        'model',
        'activity',
    ),
    drs.DrsEnsembleIdentifier: (
        'realisation_number',
        'initialisation_method_number',
        'perturbation_number',
    ),
    shared.OnlineResource: (
        'description',
        'protocol',
        'name',
        'linkage',
    ),
    designing.MultiTimeEnsemble: (
        'ensemble_members',
    ),
    data.Dataset: (
        'meta',
        'availability',
        'related_to_dataset',
        'name',
        'description',
        'produced_by',
        'drs_datasets',
        'responsible_parties',
        'references',
    ),
    platform.Performance: (
        'memory_bloat',
        'platform',
        'subcomponent_performance',
        'load_imbalance',
        'sypd',
        'total_nodes_used',
        'compiler',
        'model',
        'asypd',
        'meta',
        'name',
        'coupler_load',
        'io_load',
        'chsy',
    ),
    science.ScientificDomain: (
        'meta',
        'overview',
        'name',
        'simulates',
        'differing_key_properties',
        'id',
        'realm',
        'references',
    ),
    designing.DomainProperties: (
        'required_extent',
        'required_resolution',
    ),
    shared.IrregularDateset: (
        'date_set',
    ),
    activity.Ensemble: (
        'part_of',
        'documentation',
        'supported',
        'has_ensemble_axes',
        'members',
        'common_conformances',
    ),
    designing.MultiEnsemble: (
        'ensemble_axis',
    ),
    science.Process: (
        'sub_processes',
        'properties',
        'algorithms',
        'references',
        'keywords',
        'implementation_overview',
    ),
    shared.DocReference: (
        'version',
        'context',
        'id',
        'relationship',
        'type',
        'constraint_vocabulary',
    ),
    shared.Cimtext: (
        'content',
        'content_type',
    ),
    platform.Machine: (
        'meta',
    ),
    platform.Partition: (
        'model_number',
        'partition',
        'vendor',
        'description',
        'compute_pools',
        'online_documentation',
        'storage_pools',
        'name',
        'institution',
        'when_used',
    ),
    software.SoftwareComponent: (
        'dependencies',
        'sub_components',
        'connection_points',
        'composition',
        'language',
        'grid',
        'coupling_framework',
        'license',
    ),
    software.EntryPoint: (
        'name',
    ),
    shared.Party: (
        'organisation',
        'email',
        'url',
        'meta',
        'name',
        'orcid_id',
        'address',
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
    science.ConservationProperties: (
        'corrected_conserved_prognostic_variables',
        'flux_correction_was_used',
        'correction_methodology',
    ),
    designing.Project: (
        'sub_projects',
        'previous_projects',
        'requires_experiments',
    ),
    designing.TemporalConstraint: (
        'start_flexibility',
        'start_date',
        'required_calendar',
        'required_duration',
    ),
    shared.DateTime: (
        'offset',
        'value',
    ),
    shared.DocMetaInfo: (
        'version',
        'language',
        'source_key',
        'sort_key',
        'drs_keys',
        'type_display_name',
        'drs_path',
        'create_date',
        'update_date',
        'institute',
        'source',
        'project',
        'external_ids',
        'type_sort_key',
        'type',
        'id',
        'author',
    ),
    shared.RegularTimeset: (
        'start_date',
        'increment',
        'length',
    ),
    software.Variable: (
        'prognostic',
        'description',
        'name',
    ),
    science.Model: (
        'coupler',
        'simulates',
        'id',
        'coupled_components',
        'internal_software_components',
        'model_default_properties',
        'meta',
        'category',
    ),
    activity.Conformance: (
        'target_requirement',
    ),
    designing.OutputTemporalRequirement: (
        'continuous_subset',
        'throughout',
        'sliced_subset',
    ),
    shared.Pid: (
        'id',
        'resolution_service',
    ),
    shared.KeyFloat: (
        'key',
        'value',
    ),
    science.Tuning: (
        'regional_metrics_used',
        'trend_metrics_used',
        'description',
        'global_mean_metrics_used',
    ),
    activity.EnsembleAxis: (
        'short_identifier',
        'extra_detail',
        'target_requirement',
        'member',
    ),
    designing.NumericalExperiment: (
        'requirements',
        'related_experiments',
    ),
    software.Gridspec: (
        'description',
    ),
    shared.Calendar: (
        'description',
        'standard_name',
        'name',
        'month_lengths',
    ),
    platform.StorageVolume: (
        'units',
        'volume',
    ),
    software.DevelopmentPath: (
        'developed_in_house',
        'previous_version',
        'funding_sources',
        'consortium_name',
        'creators',
    ),
    data.VariableCollection: (
        'variables',
        'collection_name',
    ),
    designing.SimulationPlan: (
        'expected_model',
        'expected_platform',
        'will_support_experiments',
        'expected_performance_sypd',
    ),
    science.Algorithm: (
        'implementation_overview',
        'references',
        'prognostic_variables',
        'diagnostic_variables',
        'forced_variables',
    ),
    activity.EnsembleMember: (
        'errata',
        'simulation',
        'variant_id',
        'had_performance',
        'ran_on',
    ),
    science.SubProcess: (
        'implementation_overview',
        'references',
        'properties',
    ),
    science.ScienceContext: (
        'context',
        'name',
        'id',
    ),
    drs.DrsTemporalIdentifier: (
        'suffix',
        'end',
        'start',
    ),
    shared.TimesliceList: (
        'members',
        'units',
    ),
    software.ComponentBase: (
        'description',
        'repository',
        'name',
        'release_date',
        'documentation',
        'version',
        'development_history',
        'long_name',
    ),
    data.Simulation: (
        'ran_for_experiments',
        'ensemble_identifier',
        'parent_simulation',
        'used',
        'part_of_project',
        'primary_ensemble',
        'calendar',
    ),
    science.KeyProperties: (
        'resolution',
        'additional_detail',
        'time_step',
        'extra_conservation_properties',
        'tuning_applied',
        'grid',
    ),
    drs.DrsAtomicDataset: (
        'variable_name',
        'ensemble_member',
        'temporal_constraint',
        'geographical_constraint',
        'mip_table',
    ),
    shared.Reference: (
        'context',
        'document',
    ),
    science.Grid: (
        'additional_details',
        'vertical_grid_layout',
        'name',
        'grid_extent',
        'horizontal_grid_layout',
        'vertical_grid_type',
        'horizontal_grid_type',
        'meta',
    ),
    shared.TimePeriod: (
        'calendar',
        'date_type',
        'units',
        'length',
        'date',
    ),
    science.Extent: (
        'top_vertical_level',
        'is_global',
        'region_known_as',
        'northern_boundary',
        'western_boundary',
        'bottom_vertical_level',
        'eastern_boundary',
        'southern_boundary',
        'z_units',
    ),
    activity.AxisMember: (
        'value',
        'index',
        'description',
        'extra_detail',
    ),
    shared.ExternalDocument: (
        'authorship',
        'online_at',
        'publication_detail',
        'date',
        'doi',
        'meta',
        'title',
        'name',
    ),
    science.Detail: (
        'with_cardinality',
        'detail_selection',
        'select',
        'content',
        'from_vocab',
    ),
    shared.Responsibility: (
        'when',
        'party',
        'role',
    ),
    science.Resolution: (
        'equivalent_resolution_km',
        'number_of_xy_gridpoints',
        'is_adaptive_grid',
        'typical_x_degrees',
        'name',
        'typical_y_degrees',
        'number_of_levels',
    ),
    platform.ComponentPerformance: (
        'nodes_used',
        'speed',
        'cores_used',
        'component',
        'component_name',
    ),
    designing.NumericalRequirement: (
        'conformance_is_requested',
        'additional_requirements',
    ),
    activity.UberEnsemble: (
        'child_ensembles',
    ),
    designing.ForcingConstraint: (
        'code',
        'data_link',
        'additional_constraint',
        'forcing_type',
        'category',
        'group',
        'origin',
    ),
    shared.NumberArray: (
        'values',
    ),
    drs.DrsGeographicalIndicator: (
        'spatial_domain',
        'bounding_box',
        'operator',
    ),
    shared.QualityReview: (
        'metadata_reviewer',
        'quality_status',
        'date',
        'quality_description',
    ),
    platform.StoragePool: (
        'volume_available',
        'vendor',
        'type',
        'description',
        'name',
    ),
}

# Base classes.
BASE_CLASSES = defaultdict(tuple)
BASE_CLASSES[designing.EnsembleRequirement] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[data.Downscaling] = (data.Simulation, activity.Activity, )
BASE_CLASSES[designing.MultiTimeEnsemble] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.DomainProperties] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[shared.IrregularDateset] = (shared.DatetimeSet, )
BASE_CLASSES[activity.Ensemble] = (activity.Activity, )
BASE_CLASSES[designing.MultiEnsemble] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[science.Process] = (science.ScienceContext, )
BASE_CLASSES[shared.DocReference] = (shared.OnlineResource, )
BASE_CLASSES[platform.Machine] = (platform.Partition, )
BASE_CLASSES[software.SoftwareComponent] = (software.ComponentBase, )
BASE_CLASSES[designing.Project] = (activity.Activity, )
BASE_CLASSES[designing.TemporalConstraint] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[shared.RegularTimeset] = (shared.DatetimeSet, )
BASE_CLASSES[science.Model] = (software.ComponentBase, )
BASE_CLASSES[activity.Conformance] = (activity.Activity, )
BASE_CLASSES[designing.OutputTemporalRequirement] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.NumericalExperiment] = (activity.Activity, )
BASE_CLASSES[designing.SimulationPlan] = (activity.Activity, )
BASE_CLASSES[science.Algorithm] = (science.ScienceContext, )
BASE_CLASSES[science.SubProcess] = (science.ScienceContext, )
BASE_CLASSES[data.Simulation] = (activity.Activity, )
BASE_CLASSES[drs.DrsAtomicDataset] = (drs.DrsPublicationDataset, )
BASE_CLASSES[science.Detail] = (science.ScienceContext, )
BASE_CLASSES[designing.NumericalRequirement] = (activity.Activity, )
BASE_CLASSES[activity.UberEnsemble] = (activity.Ensemble, activity.Activity, )
BASE_CLASSES[designing.ForcingConstraint] = (designing.NumericalRequirement, activity.Activity, )

# Classes with base classes.
BASE_CLASSED = tuple(BASE_CLASSES.keys())

# Sub classes.
SUB_CLASSES = defaultdict(tuple)
SUB_CLASSES[science.ScienceContext] = (
    science.Process,
    science.Algorithm,
    science.SubProcess,
    science.Detail,
    )
SUB_CLASSES[designing.NumericalRequirement] = (
    designing.TemporalConstraint,
    designing.EnsembleRequirement,
    designing.OutputTemporalRequirement,
    designing.MultiEnsemble,
    designing.MultiTimeEnsemble,
    designing.ForcingConstraint,
    designing.DomainProperties,
    )
SUB_CLASSES[shared.DatetimeSet] = (
    shared.IrregularDateset,
    shared.RegularTimeset,
    )
SUB_CLASSES[activity.Activity] = (
    data.Simulation,
    designing.NumericalRequirement,
    designing.Project,
    designing.SimulationPlan,
    designing.NumericalExperiment,
    activity.Conformance,
    activity.Ensemble,
    data.Downscaling,
    designing.TemporalConstraint,
    designing.EnsembleRequirement,
    designing.OutputTemporalRequirement,
    designing.MultiEnsemble,
    designing.MultiTimeEnsemble,
    designing.ForcingConstraint,
    designing.DomainProperties,
    activity.UberEnsemble,
    )
SUB_CLASSES[software.ComponentBase] = (
    science.Model,
    software.SoftwareComponent,
    )
SUB_CLASSES[data.Simulation] = (
    data.Downscaling,
    )
SUB_CLASSES[drs.DrsPublicationDataset] = (
    drs.DrsAtomicDataset,
    )
SUB_CLASSES[activity.Ensemble] = (
    activity.UberEnsemble,
    )
SUB_CLASSES[shared.OnlineResource] = (
    shared.DocReference,
    )
SUB_CLASSES[platform.Partition] = (
    platform.Machine,
    )

# Classes that have been sub classed.
SUB_CLASSED = tuple(SUB_CLASSES.keys())

# Maximum class depth in hierarchy.
CLASS_HIERACHY_DEPTH = max(len(v) for v in BASE_CLASSES.values())

# Set type keys.
# TODO deprecate
science.Process.type_key = u"cim.2.science.Process"
science.Extent.type_key = u"cim.2.science.Extent"
science.Algorithm.type_key = u"cim.2.science.Algorithm"
science.SubProcess.type_key = u"cim.2.science.SubProcess"
science.Resolution.type_key = u"cim.2.science.Resolution"
science.Grid.type_key = u"cim.2.science.Grid"
science.ConservationProperties.type_key = u"cim.2.science.ConservationProperties"
science.Tuning.type_key = u"cim.2.science.Tuning"
science.ScienceContext.type_key = u"cim.2.science.ScienceContext"
science.KeyProperties.type_key = u"cim.2.science.KeyProperties"
science.Detail.type_key = u"cim.2.science.Detail"
science.ScientificDomain.type_key = u"cim.2.science.ScientificDomain"
science.Model.type_key = u"cim.2.science.Model"
data.VariableCollection.type_key = u"cim.2.data.VariableCollection"
data.Downscaling.type_key = u"cim.2.data.Downscaling"
data.Dataset.type_key = u"cim.2.data.Dataset"
data.Simulation.type_key = u"cim.2.data.Simulation"
shared.TimePeriod.type_key = u"cim.2.shared.TimePeriod"
shared.QualityReview.type_key = u"cim.2.shared.QualityReview"
shared.ExternalDocument.type_key = u"cim.2.shared.ExternalDocument"
shared.DateTime.type_key = u"cim.2.shared.DateTime"
shared.KeyFloat.type_key = u"cim.2.shared.KeyFloat"
shared.Calendar.type_key = u"cim.2.shared.Calendar"
shared.TimesliceList.type_key = u"cim.2.shared.TimesliceList"
shared.Reference.type_key = u"cim.2.shared.Reference"
shared.Responsibility.type_key = u"cim.2.shared.Responsibility"
shared.NumberArray.type_key = u"cim.2.shared.NumberArray"
shared.DatetimeSet.type_key = u"cim.2.shared.DatetimeSet"
shared.IrregularDateset.type_key = u"cim.2.shared.IrregularDateset"
shared.OnlineResource.type_key = u"cim.2.shared.OnlineResource"
shared.Cimtext.type_key = u"cim.2.shared.Cimtext"
shared.Party.type_key = u"cim.2.shared.Party"
shared.DocMetaInfo.type_key = u"cim.2.shared.DocMetaInfo"
shared.Pid.type_key = u"cim.2.shared.Pid"
shared.DocReference.type_key = u"cim.2.shared.DocReference"
shared.RegularTimeset.type_key = u"cim.2.shared.RegularTimeset"
designing.TemporalConstraint.type_key = u"cim.2.designing.TemporalConstraint"
designing.NumericalRequirement.type_key = u"cim.2.designing.NumericalRequirement"
designing.EnsembleRequirement.type_key = u"cim.2.designing.EnsembleRequirement"
designing.OutputTemporalRequirement.type_key = u"cim.2.designing.OutputTemporalRequirement"
designing.MultiEnsemble.type_key = u"cim.2.designing.MultiEnsemble"
designing.Project.type_key = u"cim.2.designing.Project"
designing.MultiTimeEnsemble.type_key = u"cim.2.designing.MultiTimeEnsemble"
designing.SimulationPlan.type_key = u"cim.2.designing.SimulationPlan"
designing.NumericalExperiment.type_key = u"cim.2.designing.NumericalExperiment"
designing.ForcingConstraint.type_key = u"cim.2.designing.ForcingConstraint"
designing.DomainProperties.type_key = u"cim.2.designing.DomainProperties"
software.DevelopmentPath.type_key = u"cim.2.software.DevelopmentPath"
software.ComponentBase.type_key = u"cim.2.software.ComponentBase"
software.SoftwareComponent.type_key = u"cim.2.software.SoftwareComponent"
software.EntryPoint.type_key = u"cim.2.software.EntryPoint"
software.Composition.type_key = u"cim.2.software.Composition"
software.Variable.type_key = u"cim.2.software.Variable"
software.Gridspec.type_key = u"cim.2.software.Gridspec"
drs.DrsAtomicDataset.type_key = u"cim.2.drs.DrsAtomicDataset"
drs.DrsPublicationDataset.type_key = u"cim.2.drs.DrsPublicationDataset"
drs.DrsEnsembleIdentifier.type_key = u"cim.2.drs.DrsEnsembleIdentifier"
drs.DrsTemporalIdentifier.type_key = u"cim.2.drs.DrsTemporalIdentifier"
drs.DrsGeographicalIndicator.type_key = u"cim.2.drs.DrsGeographicalIndicator"
activity.Activity.type_key = u"cim.2.activity.Activity"
activity.ParentSimulation.type_key = u"cim.2.activity.ParentSimulation"
activity.EnsembleMember.type_key = u"cim.2.activity.EnsembleMember"
activity.AxisMember.type_key = u"cim.2.activity.AxisMember"
activity.UberEnsemble.type_key = u"cim.2.activity.UberEnsemble"
activity.Conformance.type_key = u"cim.2.activity.Conformance"
activity.Ensemble.type_key = u"cim.2.activity.Ensemble"
activity.EnsembleAxis.type_key = u"cim.2.activity.EnsembleAxis"
platform.Machine.type_key = u"cim.2.platform.Machine"
platform.StorageVolume.type_key = u"cim.2.platform.StorageVolume"
platform.Partition.type_key = u"cim.2.platform.Partition"
platform.Performance.type_key = u"cim.2.platform.Performance"
platform.ComponentPerformance.type_key = u"cim.2.platform.ComponentPerformance"
platform.StoragePool.type_key = u"cim.2.platform.StoragePool"
platform.ComputePool.type_key = u"cim.2.platform.ComputePool"
science.SelectionCardinality.type_key = u"cim.2.science.SelectionCardinality"
science.ModelTypes.type_key = u"cim.2.science.ModelTypes"
data.DataAssociationTypes.type_key = u"cim.2.data.DataAssociationTypes"
shared.DocumentTypes.type_key = u"cim.2.shared.DocumentTypes"
shared.TimeUnits.type_key = u"cim.2.shared.TimeUnits"
shared.QualityStatus.type_key = u"cim.2.shared.QualityStatus"
shared.NilReason.type_key = u"cim.2.shared.NilReason"
shared.CalendarTypes.type_key = u"cim.2.shared.CalendarTypes"
shared.RoleCode.type_key = u"cim.2.shared.RoleCode"
shared.PeriodDateTypes.type_key = u"cim.2.shared.PeriodDateTypes"
shared.SlicetimeUnits.type_key = u"cim.2.shared.SlicetimeUnits"
shared.TextCode.type_key = u"cim.2.shared.TextCode"
designing.ForcingTypes.type_key = u"cim.2.designing.ForcingTypes"
designing.EnsembleTypes.type_key = u"cim.2.designing.EnsembleTypes"
designing.ExperimentalRelationships.type_key = u"cim.2.designing.ExperimentalRelationships"
software.CouplingFramework.type_key = u"cim.2.software.CouplingFramework"
software.ProgrammingLanguage.type_key = u"cim.2.software.ProgrammingLanguage"
drs.DrsTimeSuffixes.type_key = u"cim.2.drs.DrsTimeSuffixes"
drs.DrsGeographicalOperators.type_key = u"cim.2.drs.DrsGeographicalOperators"
drs.DrsRealms.type_key = u"cim.2.drs.DrsRealms"
drs.DrsFrequencyTypes.type_key = u"cim.2.drs.DrsFrequencyTypes"
activity.EnsembleTypes.type_key = u"cim.2.activity.EnsembleTypes"
activity.ForcingTypes.type_key = u"cim.2.activity.ForcingTypes"
platform.StorageSystems.type_key = u"cim.2.platform.StorageSystems"
platform.VolumeUnits.type_key = u"cim.2.platform.VolumeUnits"

