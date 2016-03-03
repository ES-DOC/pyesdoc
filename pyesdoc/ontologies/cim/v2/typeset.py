
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

from typeset_for_designing_package import *
from typeset_for_data_package import *
from typeset_for_platform_package import *
from typeset_for_drs_package import *
from typeset_for_activity_package import *
from typeset_for_software_package import *
from typeset_for_science_package import *
from typeset_for_shared_package import *


import typeset_for_designing_package as designing
import typeset_for_data_package as data
import typeset_for_platform_package as platform
import typeset_for_drs_package as drs
import typeset_for_activity_package as activity
import typeset_for_software_package as software
import typeset_for_science_package as science
import typeset_for_shared_package as shared



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
    designing,
    data,
    platform,
    drs,
    activity,
    software,
    science,
    shared,
    # Classes
    Machine,
    Responsibility,
    Tuning,
    RegularTimeset,
    ComponentPerformance,
    Pid,
    DrsAtomicDataset,
    NumericalRequirement,
    Detail,
    OnlineResource,
    Ensemble,
    IrregularDateset,
    StorageVolume,
    EntryPoint,
    DrsEnsembleIdentifier,
    Calendar,
    Gridspec,
    ScienceContext,
    Downscaling,
    MultiTimeEnsemble,
    KeyFloat,
    ExternalDocument,
    EnsembleRequirement,
    ScientificDomain,
    EnsembleAxis,
    ComponentBase,
    NumericalExperiment,
    DocReference,
    KeyProperties,
    DrsTemporalIdentifier,
    ForcingConstraint,
    TimePeriod,
    Composition,
    DrsGeographicalIndicator,
    Algorithm,
    Simulation,
    Process,
    Grid,
    OutputTemporalRequirement,
    Extent,
    DatetimeSet,
    DomainProperties,
    Model,
    DateTime,
    NumberArray,
    Party,
    UberEnsemble,
    ConservationProperties,
    Partition,
    AxisMember,
    DevelopmentPath,
    TimesliceList,
    ComputePool,
    TemporalConstraint,
    Resolution,
    ParentSimulation,
    DocMetaInfo,
    SimulationPlan,
    DrsPublicationDataset,
    Dataset,
    MultiEnsemble,
    SubProcess,
    Conformance,
    Reference,
    SoftwareComponent,
    StoragePool,
    Performance,
    Activity,
    Project,
    Cimtext,
    QualityReview,
    EnsembleMember,
    Variable,
    VariableCollection,
    # Enums
    PeriodDateTypes,
    ForcingTypes,
    TimeUnits,
    StorageSystems,
    DrsGeographicalOperators,
    EnsembleTypes,
    SlicetimeUnits,
    VolumeUnits,
    DrsFrequencyTypes,
    ProgrammingLanguage,
    QualityStatus,
    ModelTypes,
    DocumentTypes,
    CalendarTypes,
    SelectionCardinality,
    ExperimentalRelationships,
    ForcingTypes,
    CouplingFramework,
    NilReason,
    EnsembleTypes,
    DrsRealms,
    DataAssociationTypes,
    TextCode,
    DrsTimeSuffixes,
    RoleCode,
]

# Supported packages.
PACKAGES = (
    designing,
    data,
    platform,
    drs,
    activity,
    software,
    science,
    shared,
)

# Supported classes.
CLASSES = (
    platform.Machine,
    shared.Responsibility,
    science.Tuning,
    shared.RegularTimeset,
    platform.ComponentPerformance,
    shared.Pid,
    drs.DrsAtomicDataset,
    designing.NumericalRequirement,
    science.Detail,
    shared.OnlineResource,
    activity.Ensemble,
    shared.IrregularDateset,
    platform.StorageVolume,
    software.EntryPoint,
    drs.DrsEnsembleIdentifier,
    shared.Calendar,
    software.Gridspec,
    science.ScienceContext,
    data.Downscaling,
    designing.MultiTimeEnsemble,
    shared.KeyFloat,
    shared.ExternalDocument,
    designing.EnsembleRequirement,
    science.ScientificDomain,
    activity.EnsembleAxis,
    software.ComponentBase,
    designing.NumericalExperiment,
    shared.DocReference,
    science.KeyProperties,
    drs.DrsTemporalIdentifier,
    designing.ForcingConstraint,
    shared.TimePeriod,
    software.Composition,
    drs.DrsGeographicalIndicator,
    science.Algorithm,
    data.Simulation,
    science.Process,
    science.Grid,
    designing.OutputTemporalRequirement,
    science.Extent,
    shared.DatetimeSet,
    designing.DomainProperties,
    science.Model,
    shared.DateTime,
    shared.NumberArray,
    shared.Party,
    activity.UberEnsemble,
    science.ConservationProperties,
    platform.Partition,
    activity.AxisMember,
    software.DevelopmentPath,
    shared.TimesliceList,
    platform.ComputePool,
    designing.TemporalConstraint,
    science.Resolution,
    activity.ParentSimulation,
    shared.DocMetaInfo,
    designing.SimulationPlan,
    drs.DrsPublicationDataset,
    data.Dataset,
    designing.MultiEnsemble,
    science.SubProcess,
    activity.Conformance,
    shared.Reference,
    software.SoftwareComponent,
    platform.StoragePool,
    platform.Performance,
    activity.Activity,
    designing.Project,
    shared.Cimtext,
    shared.QualityReview,
    activity.EnsembleMember,
    software.Variable,
    data.VariableCollection,
)

# Supported enums.
ENUMS = (
    shared.PeriodDateTypes,
    activity.ForcingTypes,
    shared.TimeUnits,
    platform.StorageSystems,
    drs.DrsGeographicalOperators,
    designing.EnsembleTypes,
    shared.SlicetimeUnits,
    platform.VolumeUnits,
    drs.DrsFrequencyTypes,
    software.ProgrammingLanguage,
    shared.QualityStatus,
    science.ModelTypes,
    shared.DocumentTypes,
    shared.CalendarTypes,
    science.SelectionCardinality,
    designing.ExperimentalRelationships,
    designing.ForcingTypes,
    software.CouplingFramework,
    shared.NilReason,
    activity.EnsembleTypes,
    drs.DrsRealms,
    data.DataAssociationTypes,
    shared.TextCode,
    drs.DrsTimeSuffixes,
    shared.RoleCode,
)

# Supported document types.
DOCUMENT_TYPES = (
    designing.OutputTemporalRequirement,
    designing.MultiEnsemble,
    designing.Project,
    designing.MultiTimeEnsemble,
    designing.SimulationPlan,
    designing.NumericalExperiment,
    designing.ForcingConstraint,
    designing.DomainProperties,
    designing.TemporalConstraint,
    designing.NumericalRequirement,
    designing.EnsembleRequirement,
    data.Dataset,
    data.Simulation,
    data.Downscaling,
    platform.Performance,
    platform.Machine,
    activity.UberEnsemble,
    activity.Conformance,
    activity.Ensemble,
    activity.Activity,
    science.Grid,
    science.ScientificDomain,
    science.Model,
    shared.ExternalDocument,
    shared.Party,
)

# Supported class properties.
CLASS_PROPERTIES = { 
    platform.Machine: (
        'name',
        'description',
        'storage_pools',
        'partition',
        'online_documentation',
        'meta',
        'institution',
        'vendor',
        'when_used',
        'model_number',
        'compute_pools',
    ),
    shared.Responsibility: (
        'role',
        'when',
        'party',
    ),
    science.Tuning: (
        'global_mean_metrics_used',
        'description',
        'regional_metrics_used',
        'trend_metrics_used',
    ),
    shared.RegularTimeset: (
        'length',
        'increment',
        'length',
        'start_date',
    ),
    platform.ComponentPerformance: (
        'component',
        'nodes_used',
        'speed',
        'component_name',
        'cores_used',
    ),
    shared.Pid: (
        'id',
        'resolution_service',
    ),
    drs.DrsAtomicDataset: (
        'geographical_constraint',
        'frequency',
        'variable_name',
        'realm',
        'experiment',
        'mip_table',
        'institute',
        'version_number',
        'ensemble_member',
        'activity',
        'model',
        'product',
        'temporal_constraint',
    ),
    designing.NumericalRequirement: (
        'duration',
        'keywords',
        'rationale',
        'long_name',
        'meta',
        'canonical_name',
        'additional_requirements',
        'responsible_parties',
        'references',
        'conformance_is_requested',
        'name',
        'description',
    ),
    science.Detail: (
        'context',
        'name',
        'from_vocab',
        'select',
        'content',
        'id',
        'with_cardinality',
        'detail_selection',
    ),
    shared.OnlineResource: (
        'description',
        'protocol',
        'linkage',
        'name',
    ),
    activity.Ensemble: (
        'supported',
        'long_name',
        'canonical_name',
        'description',
        'common_conformances',
        'name',
        'keywords',
        'documentation',
        'rationale',
        'has_ensemble_axes',
        'meta',
        'duration',
        'members',
        'references',
        'part_of',
        'responsible_parties',
    ),
    shared.IrregularDateset: (
        'date_set',
        'length',
    ),
    platform.StorageVolume: (
        'units',
        'volume',
    ),
    software.EntryPoint: (
        'name',
    ),
    drs.DrsEnsembleIdentifier: (
        'perturbation_number',
        'realisation_number',
        'initialisation_method_number',
    ),
    shared.Calendar: (
        'month_lengths',
        'standard_name',
        'name',
        'description',
    ),
    software.Gridspec: (
        'description',
    ),
    science.ScienceContext: (
        'context',
        'id',
        'name',
    ),
    data.Downscaling: (
        'calendar',
        'primary_ensemble',
        'downscaled_from',
        'ensemble_identifier',
        'long_name',
        'description',
        'parent_simulation',
        'part_of_project',
        'keywords',
        'canonical_name',
        'rationale',
        'references',
        'name',
        'responsible_parties',
        'ran_for_experiments',
        'used',
        'duration',
        'meta',
    ),
    designing.MultiTimeEnsemble: (
        'canonical_name',
        'conformance_is_requested',
        'ensemble_members',
        'responsible_parties',
        'long_name',
        'rationale',
        'additional_requirements',
        'description',
        'meta',
        'references',
        'duration',
        'name',
        'keywords',
    ),
    shared.KeyFloat: (
        'key',
        'value',
    ),
    shared.ExternalDocument: (
        'authorship',
        'date',
        'name',
        'publication_detail',
        'meta',
        'online_at',
        'title',
        'doi',
    ),
    designing.EnsembleRequirement: (
        'minimum_size',
        'canonical_name',
        'conformance_is_requested',
        'keywords',
        'responsible_parties',
        'references',
        'ensemble_member',
        'long_name',
        'additional_requirements',
        'description',
        'meta',
        'ensemble_type',
        'duration',
        'name',
        'rationale',
    ),
    science.ScientificDomain: (
        'name',
        'meta',
        'realm',
        'differing_key_properties',
        'id',
        'overview',
        'references',
        'simulates',
    ),
    activity.EnsembleAxis: (
        'member',
        'extra_detail',
        'target_requirement',
        'short_identifier',
    ),
    software.ComponentBase: (
        'documentation',
        'repository',
        'long_name',
        'name',
        'release_date',
        'version',
        'development_history',
        'description',
    ),
    designing.NumericalExperiment: (
        'related_experiments',
        'duration',
        'keywords',
        'rationale',
        'requirements',
        'meta',
        'long_name',
        'responsible_parties',
        'references',
        'canonical_name',
        'name',
        'description',
    ),
    shared.DocReference: (
        'context',
        'type',
        'linkage',
        'constraint_vocabulary',
        'description',
        'protocol',
        'name',
        'version',
        'relationship',
        'id',
    ),
    science.KeyProperties: (
        'time_step',
        'extra_conservation_properties',
        'grid',
        'tuning_applied',
        'resolution',
        'additional_detail',
    ),
    drs.DrsTemporalIdentifier: (
        'end',
        'start',
        'suffix',
    ),
    designing.ForcingConstraint: (
        'keywords',
        'additional_constraint',
        'long_name',
        'additional_requirements',
        'description',
        'category',
        'code',
        'name',
        'rationale',
        'canonical_name',
        'conformance_is_requested',
        'data_link',
        'responsible_parties',
        'forcing_type',
        'duration',
        'group',
        'references',
        'origin',
        'meta',
    ),
    shared.TimePeriod: (
        'calendar',
        'date',
        'length',
        'date_type',
        'units',
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
    drs.DrsGeographicalIndicator: (
        'spatial_domain',
        'bounding_box',
        'operator',
    ),
    science.Algorithm: (
        'forced_variables',
        'name',
        'context',
        'implementation_overview',
        'prognostic_variables',
        'id',
        'references',
        'diagnostic_variables',
    ),
    data.Simulation: (
        'calendar',
        'rationale',
        'ensemble_identifier',
        'long_name',
        'parent_simulation',
        'part_of_project',
        'name',
        'keywords',
        'primary_ensemble',
        'references',
        'ran_for_experiments',
        'meta',
        'duration',
        'responsible_parties',
        'used',
        'canonical_name',
        'description',
    ),
    science.Process: (
        'context',
        'name',
        'algorithms',
        'implementation_overview',
        'id',
        'sub_processes',
        'keywords',
        'properties',
        'references',
    ),
    science.Grid: (
        'name',
        'grid_extent',
        'horizontal_grid_layout',
        'additional_details',
        'vertical_grid_type',
        'meta',
        'vertical_grid_layout',
        'horizontal_grid_type',
    ),
    designing.OutputTemporalRequirement: (
        'conformance_is_requested',
        'keywords',
        'additional_requirements',
        'continuous_subset',
        'references',
        'long_name',
        'canonical_name',
        'sliced_subset',
        'description',
        'meta',
        'throughout',
        'responsible_parties',
        'duration',
        'name',
        'rationale',
    ),
    science.Extent: (
        'southern_boundary',
        'is_global',
        'western_boundary',
        'northern_boundary',
        'bottom_vertical_level',
        'region_known_as',
        'z_units',
        'eastern_boundary',
        'top_vertical_level',
    ),
    shared.DatetimeSet: (
        'length',
    ),
    designing.DomainProperties: (
        'canonical_name',
        'conformance_is_requested',
        'keywords',
        'responsible_parties',
        'required_extent',
        'meta',
        'long_name',
        'additional_requirements',
        'description',
        'required_resolution',
        'references',
        'duration',
        'name',
        'rationale',
    ),
    science.Model: (
        'model_default_properties',
        'documentation',
        'name',
        'id',
        'repository',
        'long_name',
        'development_history',
        'internal_software_components',
        'category',
        'simulates',
        'coupled_components',
        'version',
        'release_date',
        'description',
        'coupler',
        'meta',
    ),
    shared.DateTime: (
        'offset',
        'value',
    ),
    shared.NumberArray: (
        'values',
    ),
    shared.Party: (
        'organisation',
        'orcid_id',
        'address',
        'name',
        'url',
        'meta',
        'email',
    ),
    activity.UberEnsemble: (
        'supported',
        'long_name',
        'has_ensemble_axes',
        'common_conformances',
        'child_ensembles',
        'name',
        'keywords',
        'documentation',
        'rationale',
        'responsible_parties',
        'references',
        'canonical_name',
        'part_of',
        'description',
        'members',
        'duration',
        'meta',
    ),
    science.ConservationProperties: (
        'corrected_conserved_prognostic_variables',
        'correction_methodology',
        'flux_correction_was_used',
    ),
    platform.Partition: (
        'name',
        'model_number',
        'online_documentation',
        'institution',
        'when_used',
        'partition',
        'vendor',
        'description',
        'storage_pools',
        'compute_pools',
    ),
    activity.AxisMember: (
        'extra_detail',
        'value',
        'index',
        'description',
    ),
    software.DevelopmentPath: (
        'funding_sources',
        'developed_in_house',
        'creators',
        'previous_version',
        'consortium_name',
    ),
    shared.TimesliceList: (
        'members',
        'units',
    ),
    platform.ComputePool: (
        'compute_cores_per_node',
        'cpu_type',
        'operating_system',
        'accelerators_per_node',
        'name',
        'number_of_nodes',
        'model_number',
        'interconnect',
        'description',
        'memory_per_node',
        'accelerator_type',
    ),
    designing.TemporalConstraint: (
        'keywords',
        'long_name',
        'canonical_name',
        'additional_requirements',
        'description',
        'meta',
        'conformance_is_requested',
        'name',
        'rationale',
        'required_calendar',
        'required_duration',
        'duration',
        'start_date',
        'references',
        'start_flexibility',
        'responsible_parties',
    ),
    science.Resolution: (
        'number_of_xy_gridpoints',
        'typical_y_degrees',
        'is_adaptive_grid',
        'typical_x_degrees',
        'number_of_levels',
        'name',
        'equivalent_resolution_km',
    ),
    activity.ParentSimulation: (
        'branch_time_in_parent',
        'parent',
        'branch_time_in_child',
    ),
    shared.DocMetaInfo: (
        'drs_path',
        'drs_keys',
        'source_key',
        'external_ids',
        'type_display_name',
        'id',
        'institute',
        'type_sort_key',
        'type',
        'version',
        'update_date',
        'create_date',
        'author',
        'sort_key',
        'project',
        'source',
        'language',
    ),
    designing.SimulationPlan: (
        'canonical_name',
        'expected_platform',
        'duration',
        'rationale',
        'will_support_experiments',
        'meta',
        'responsible_parties',
        'description',
        'name',
        'expected_model',
        'references',
        'expected_performance_sypd',
        'long_name',
        'keywords',
    ),
    drs.DrsPublicationDataset: (
        'frequency',
        'realm',
        'institute',
        'product',
        'version_number',
        'model',
        'experiment',
        'activity',
    ),
    data.Dataset: (
        'references',
        'availability',
        'meta',
        'description',
        'produced_by',
        'responsible_parties',
        'related_to_dataset',
        'drs_datasets',
        'name',
    ),
    designing.MultiEnsemble: (
        'conformance_is_requested',
        'keywords',
        'ensemble_axis',
        'long_name',
        'canonical_name',
        'additional_requirements',
        'description',
        'meta',
        'references',
        'responsible_parties',
        'duration',
        'name',
        'rationale',
    ),
    science.SubProcess: (
        'implementation_overview',
        'context',
        'name',
        'references',
        'properties',
        'id',
    ),
    activity.Conformance: (
        'keywords',
        'rationale',
        'long_name',
        'meta',
        'canonical_name',
        'target_requirement',
        'responsible_parties',
        'references',
        'duration',
        'name',
        'description',
    ),
    shared.Reference: (
        'context',
        'document',
    ),
    software.SoftwareComponent: (
        'language',
        'name',
        'repository',
        'documentation',
        'coupling_framework',
        'development_history',
        'license',
        'dependencies',
        'release_date',
        'version',
        'composition',
        'long_name',
        'grid',
        'description',
        'connection_points',
        'sub_components',
    ),
    platform.StoragePool: (
        'description',
        'volume_available',
        'vendor',
        'type',
        'name',
    ),
    platform.Performance: (
        'name',
        'total_nodes_used',
        'compiler',
        'io_load',
        'meta',
        'asypd',
        'subcomponent_performance',
        'memory_bloat',
        'platform',
        'model',
        'sypd',
        'load_imbalance',
        'chsy',
        'coupler_load',
    ),
    activity.Activity: (
        'keywords',
        'responsible_parties',
        'long_name',
        'canonical_name',
        'description',
        'meta',
        'references',
        'duration',
        'name',
        'rationale',
    ),
    designing.Project: (
        'duration',
        'keywords',
        'requires_experiments',
        'long_name',
        'meta',
        'canonical_name',
        'description',
        'sub_projects',
        'references',
        'rationale',
        'previous_projects',
        'name',
        'responsible_parties',
    ),
    shared.Cimtext: (
        'content',
        'content_type',
    ),
    shared.QualityReview: (
        'quality_status',
        'quality_description',
        'metadata_reviewer',
        'date',
    ),
    activity.EnsembleMember: (
        'ran_on',
        'errata',
        'variant_id',
        'had_performance',
        'simulation',
    ),
    software.Variable: (
        'prognostic',
        'name',
        'description',
    ),
    data.VariableCollection: (
        'collection_name',
        'variables',
    ),
}

# Supported class own properties.
CLASS_OWN_PROPERTIES = { 
    platform.Machine: (
        'meta',
    ),
    shared.Responsibility: (
        'when',
        'party',
        'role',
    ),
    science.Tuning: (
        'regional_metrics_used',
        'trend_metrics_used',
        'description',
        'global_mean_metrics_used',
    ),
    shared.RegularTimeset: (
        'start_date',
        'increment',
        'length',
    ),
    platform.ComponentPerformance: (
        'speed',
        'cores_used',
        'nodes_used',
        'component',
        'component_name',
    ),
    shared.Pid: (
        'id',
        'resolution_service',
    ),
    drs.DrsAtomicDataset: (
        'temporal_constraint',
        'geographical_constraint',
        'variable_name',
        'ensemble_member',
        'mip_table',
    ),
    designing.NumericalRequirement: (
        'additional_requirements',
        'conformance_is_requested',
    ),
    science.Detail: (
        'from_vocab',
        'with_cardinality',
        'select',
        'content',
        'detail_selection',
    ),
    shared.OnlineResource: (
        'description',
        'name',
        'protocol',
        'linkage',
    ),
    activity.Ensemble: (
        'documentation',
        'supported',
        'has_ensemble_axes',
        'members',
        'part_of',
        'common_conformances',
    ),
    shared.IrregularDateset: (
        'date_set',
    ),
    platform.StorageVolume: (
        'units',
        'volume',
    ),
    software.EntryPoint: (
        'name',
    ),
    drs.DrsEnsembleIdentifier: (
        'realisation_number',
        'initialisation_method_number',
        'perturbation_number',
    ),
    shared.Calendar: (
        'standard_name',
        'description',
        'name',
        'month_lengths',
    ),
    software.Gridspec: (
        'description',
    ),
    science.ScienceContext: (
        'context',
        'name',
        'id',
    ),
    data.Downscaling: (
        'downscaled_from',
    ),
    designing.MultiTimeEnsemble: (
        'ensemble_members',
    ),
    shared.KeyFloat: (
        'key',
        'value',
    ),
    shared.ExternalDocument: (
        'authorship',
        'date',
        'name',
        'publication_detail',
        'meta',
        'online_at',
        'title',
        'doi',
    ),
    designing.EnsembleRequirement: (
        'ensemble_type',
        'ensemble_member',
        'minimum_size',
    ),
    science.ScientificDomain: (
        'name',
        'references',
        'id',
        'differing_key_properties',
        'realm',
        'overview',
        'meta',
        'simulates',
    ),
    activity.EnsembleAxis: (
        'target_requirement',
        'short_identifier',
        'extra_detail',
        'member',
    ),
    software.ComponentBase: (
        'documentation',
        'repository',
        'name',
        'long_name',
        'description',
        'version',
        'development_history',
        'release_date',
    ),
    designing.NumericalExperiment: (
        'related_experiments',
        'requirements',
    ),
    shared.DocReference: (
        'id',
        'relationship',
        'context',
        'type',
        'version',
        'constraint_vocabulary',
    ),
    science.KeyProperties: (
        'time_step',
        'extra_conservation_properties',
        'tuning_applied',
        'grid',
        'resolution',
        'additional_detail',
    ),
    drs.DrsTemporalIdentifier: (
        'end',
        'suffix',
        'start',
    ),
    designing.ForcingConstraint: (
        'data_link',
        'origin',
        'forcing_type',
        'additional_constraint',
        'group',
        'code',
        'category',
    ),
    shared.TimePeriod: (
        'length',
        'units',
        'calendar',
        'date_type',
        'date',
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
    drs.DrsGeographicalIndicator: (
        'spatial_domain',
        'bounding_box',
        'operator',
    ),
    science.Algorithm: (
        'diagnostic_variables',
        'prognostic_variables',
        'references',
        'implementation_overview',
        'forced_variables',
    ),
    data.Simulation: (
        'primary_ensemble',
        'ran_for_experiments',
        'ensemble_identifier',
        'parent_simulation',
        'used',
        'part_of_project',
        'calendar',
    ),
    science.Process: (
        'references',
        'sub_processes',
        'implementation_overview',
        'keywords',
        'properties',
        'algorithms',
    ),
    science.Grid: (
        'name',
        'horizontal_grid_layout',
        'vertical_grid_type',
        'meta',
        'horizontal_grid_type',
        'additional_details',
        'vertical_grid_layout',
        'grid_extent',
    ),
    designing.OutputTemporalRequirement: (
        'continuous_subset',
        'throughout',
        'sliced_subset',
    ),
    science.Extent: (
        'western_boundary',
        'is_global',
        'z_units',
        'northern_boundary',
        'eastern_boundary',
        'top_vertical_level',
        'region_known_as',
        'southern_boundary',
        'bottom_vertical_level',
    ),
    shared.DatetimeSet: (
        'length',
    ),
    designing.DomainProperties: (
        'required_extent',
        'required_resolution',
    ),
    science.Model: (
        'model_default_properties',
        'id',
        'internal_software_components',
        'category',
        'simulates',
        'meta',
        'coupler',
        'coupled_components',
    ),
    shared.DateTime: (
        'offset',
        'value',
    ),
    shared.NumberArray: (
        'values',
    ),
    shared.Party: (
        'organisation',
        'meta',
        'name',
        'address',
        'url',
        'orcid_id',
        'email',
    ),
    activity.UberEnsemble: (
        'child_ensembles',
    ),
    science.ConservationProperties: (
        'corrected_conserved_prognostic_variables',
        'flux_correction_was_used',
        'correction_methodology',
    ),
    platform.Partition: (
        'name',
        'storage_pools',
        'when_used',
        'partition',
        'description',
        'institution',
        'vendor',
        'online_documentation',
        'model_number',
        'compute_pools',
    ),
    activity.AxisMember: (
        'value',
        'description',
        'index',
        'extra_detail',
    ),
    software.DevelopmentPath: (
        'developed_in_house',
        'consortium_name',
        'funding_sources',
        'previous_version',
        'creators',
    ),
    shared.TimesliceList: (
        'members',
        'units',
    ),
    platform.ComputePool: (
        'cpu_type',
        'number_of_nodes',
        'name',
        'memory_per_node',
        'accelerators_per_node',
        'description',
        'interconnect',
        'operating_system',
        'model_number',
        'accelerator_type',
        'compute_cores_per_node',
    ),
    designing.TemporalConstraint: (
        'start_date',
        'start_flexibility',
        'required_calendar',
        'required_duration',
    ),
    science.Resolution: (
        'is_adaptive_grid',
        'typical_x_degrees',
        'name',
        'equivalent_resolution_km',
        'typical_y_degrees',
        'number_of_levels',
        'number_of_xy_gridpoints',
    ),
    activity.ParentSimulation: (
        'parent',
        'branch_time_in_child',
        'branch_time_in_parent',
    ),
    shared.DocMetaInfo: (
        'drs_path',
        'sort_key',
        'create_date',
        'author',
        'source_key',
        'update_date',
        'project',
        'type_sort_key',
        'id',
        'source',
        'external_ids',
        'institute',
        'drs_keys',
        'type',
        'version',
        'language',
        'type_display_name',
    ),
    designing.SimulationPlan: (
        'will_support_experiments',
        'expected_model',
        'expected_platform',
        'expected_performance_sypd',
    ),
    drs.DrsPublicationDataset: (
        'frequency',
        'realm',
        'institute',
        'experiment',
        'version_number',
        'model',
        'product',
        'activity',
    ),
    data.Dataset: (
        'availability',
        'references',
        'responsible_parties',
        'meta',
        'drs_datasets',
        'name',
        'related_to_dataset',
        'produced_by',
        'description',
    ),
    designing.MultiEnsemble: (
        'ensemble_axis',
    ),
    science.SubProcess: (
        'implementation_overview',
        'references',
        'properties',
    ),
    activity.Conformance: (
        'target_requirement',
    ),
    shared.Reference: (
        'context',
        'document',
    ),
    software.SoftwareComponent: (
        'language',
        'coupling_framework',
        'license',
        'dependencies',
        'composition',
        'grid',
        'connection_points',
        'sub_components',
    ),
    platform.StoragePool: (
        'description',
        'vendor',
        'name',
        'volume_available',
        'type',
    ),
    platform.Performance: (
        'meta',
        'subcomponent_performance',
        'compiler',
        'total_nodes_used',
        'model',
        'coupler_load',
        'chsy',
        'memory_bloat',
        'platform',
        'io_load',
        'name',
        'sypd',
        'load_imbalance',
        'asypd',
    ),
    activity.Activity: (
        'keywords',
        'rationale',
        'long_name',
        'canonical_name',
        'meta',
        'references',
        'responsible_parties',
        'duration',
        'name',
        'description',
    ),
    designing.Project: (
        'requires_experiments',
        'previous_projects',
        'sub_projects',
    ),
    shared.Cimtext: (
        'content',
        'content_type',
    ),
    shared.QualityReview: (
        'quality_status',
        'date',
        'quality_description',
        'metadata_reviewer',
    ),
    activity.EnsembleMember: (
        'errata',
        'simulation',
        'variant_id',
        'had_performance',
        'ran_on',
    ),
    software.Variable: (
        'prognostic',
        'description',
        'name',
    ),
    data.VariableCollection: (
        'collection_name',
        'variables',
    ),
}

# Base classes.
BASE_CLASSES = defaultdict(tuple)
BASE_CLASSES[platform.Machine] = (platform.Partition, )
BASE_CLASSES[shared.RegularTimeset] = (shared.DatetimeSet, )
BASE_CLASSES[drs.DrsAtomicDataset] = (drs.DrsPublicationDataset, )
BASE_CLASSES[designing.NumericalRequirement] = (activity.Activity, )
BASE_CLASSES[science.Detail] = (science.ScienceContext, )
BASE_CLASSES[activity.Ensemble] = (activity.Activity, )
BASE_CLASSES[shared.IrregularDateset] = (shared.DatetimeSet, )
BASE_CLASSES[data.Downscaling] = (data.Simulation, activity.Activity, )
BASE_CLASSES[designing.MultiTimeEnsemble] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.EnsembleRequirement] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.NumericalExperiment] = (activity.Activity, )
BASE_CLASSES[shared.DocReference] = (shared.OnlineResource, )
BASE_CLASSES[designing.ForcingConstraint] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[science.Algorithm] = (science.ScienceContext, )
BASE_CLASSES[data.Simulation] = (activity.Activity, )
BASE_CLASSES[science.Process] = (science.ScienceContext, )
BASE_CLASSES[designing.OutputTemporalRequirement] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.DomainProperties] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[science.Model] = (software.ComponentBase, )
BASE_CLASSES[activity.UberEnsemble] = (activity.Ensemble, activity.Activity, )
BASE_CLASSES[designing.TemporalConstraint] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.SimulationPlan] = (activity.Activity, )
BASE_CLASSES[designing.MultiEnsemble] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[science.SubProcess] = (science.ScienceContext, )
BASE_CLASSES[activity.Conformance] = (activity.Activity, )
BASE_CLASSES[software.SoftwareComponent] = (software.ComponentBase, )
BASE_CLASSES[designing.Project] = (activity.Activity, )

# Classes with base classes.
BASE_CLASSED = tuple(BASE_CLASSES.keys())

# Sub classes.
SUB_CLASSES = defaultdict(tuple)
SUB_CLASSES[shared.DatetimeSet] = (
    shared.IrregularDateset,
    shared.RegularTimeset,
    )
SUB_CLASSES[drs.DrsPublicationDataset] = (
    drs.DrsAtomicDataset,
    )
SUB_CLASSES[activity.Activity] = (
    designing.Project,
    designing.SimulationPlan,
    designing.NumericalExperiment,
    designing.NumericalRequirement,
    activity.Conformance,
    activity.Ensemble,
    data.Simulation,
    designing.OutputTemporalRequirement,
    designing.MultiEnsemble,
    designing.MultiTimeEnsemble,
    designing.ForcingConstraint,
    designing.DomainProperties,
    designing.TemporalConstraint,
    designing.EnsembleRequirement,
    activity.UberEnsemble,
    data.Downscaling,
    )
SUB_CLASSES[designing.NumericalRequirement] = (
    designing.OutputTemporalRequirement,
    designing.MultiEnsemble,
    designing.MultiTimeEnsemble,
    designing.ForcingConstraint,
    designing.DomainProperties,
    designing.TemporalConstraint,
    designing.EnsembleRequirement,
    )
SUB_CLASSES[data.Simulation] = (
    data.Downscaling,
    )
SUB_CLASSES[software.ComponentBase] = (
    software.SoftwareComponent,
    science.Model,
    )
SUB_CLASSES[activity.Ensemble] = (
    activity.UberEnsemble,
    )
SUB_CLASSES[platform.Partition] = (
    platform.Machine,
    )
SUB_CLASSES[shared.OnlineResource] = (
    shared.DocReference,
    )
SUB_CLASSES[science.ScienceContext] = (
    science.SubProcess,
    science.Detail,
    science.Process,
    science.Algorithm,
    )

# Classes that have been sub classed.
SUB_CLASSED = tuple(SUB_CLASSES.keys())

# Maximum class depth in hierarchy.
CLASS_HIERACHY_DEPTH = max(len(v) for v in BASE_CLASSES.values())

# Set type keys.
# TODO deprecate
shared.ExternalDocument.type_key = u"cim.2.shared.ExternalDocument"
shared.Calendar.type_key = u"cim.2.shared.Calendar"
shared.Reference.type_key = u"cim.2.shared.Reference"
shared.NumberArray.type_key = u"cim.2.shared.NumberArray"
shared.TimesliceList.type_key = u"cim.2.shared.TimesliceList"
shared.DateTime.type_key = u"cim.2.shared.DateTime"
shared.Responsibility.type_key = u"cim.2.shared.Responsibility"
shared.DatetimeSet.type_key = u"cim.2.shared.DatetimeSet"
shared.OnlineResource.type_key = u"cim.2.shared.OnlineResource"
shared.IrregularDateset.type_key = u"cim.2.shared.IrregularDateset"
shared.Cimtext.type_key = u"cim.2.shared.Cimtext"
shared.Party.type_key = u"cim.2.shared.Party"
shared.DocReference.type_key = u"cim.2.shared.DocReference"
shared.DocMetaInfo.type_key = u"cim.2.shared.DocMetaInfo"
shared.Pid.type_key = u"cim.2.shared.Pid"
shared.RegularTimeset.type_key = u"cim.2.shared.RegularTimeset"
shared.KeyFloat.type_key = u"cim.2.shared.KeyFloat"
shared.TimePeriod.type_key = u"cim.2.shared.TimePeriod"
shared.QualityReview.type_key = u"cim.2.shared.QualityReview"
designing.OutputTemporalRequirement.type_key = u"cim.2.designing.OutputTemporalRequirement"
designing.MultiEnsemble.type_key = u"cim.2.designing.MultiEnsemble"
designing.Project.type_key = u"cim.2.designing.Project"
designing.MultiTimeEnsemble.type_key = u"cim.2.designing.MultiTimeEnsemble"
designing.SimulationPlan.type_key = u"cim.2.designing.SimulationPlan"
designing.NumericalExperiment.type_key = u"cim.2.designing.NumericalExperiment"
designing.ForcingConstraint.type_key = u"cim.2.designing.ForcingConstraint"
designing.DomainProperties.type_key = u"cim.2.designing.DomainProperties"
designing.TemporalConstraint.type_key = u"cim.2.designing.TemporalConstraint"
designing.NumericalRequirement.type_key = u"cim.2.designing.NumericalRequirement"
designing.EnsembleRequirement.type_key = u"cim.2.designing.EnsembleRequirement"
software.EntryPoint.type_key = u"cim.2.software.EntryPoint"
software.Gridspec.type_key = u"cim.2.software.Gridspec"
software.ComponentBase.type_key = u"cim.2.software.ComponentBase"
software.SoftwareComponent.type_key = u"cim.2.software.SoftwareComponent"
software.Composition.type_key = u"cim.2.software.Composition"
software.Variable.type_key = u"cim.2.software.Variable"
software.DevelopmentPath.type_key = u"cim.2.software.DevelopmentPath"
drs.DrsPublicationDataset.type_key = u"cim.2.drs.DrsPublicationDataset"
drs.DrsEnsembleIdentifier.type_key = u"cim.2.drs.DrsEnsembleIdentifier"
drs.DrsTemporalIdentifier.type_key = u"cim.2.drs.DrsTemporalIdentifier"
drs.DrsGeographicalIndicator.type_key = u"cim.2.drs.DrsGeographicalIndicator"
drs.DrsAtomicDataset.type_key = u"cim.2.drs.DrsAtomicDataset"
activity.AxisMember.type_key = u"cim.2.activity.AxisMember"
activity.UberEnsemble.type_key = u"cim.2.activity.UberEnsemble"
activity.Conformance.type_key = u"cim.2.activity.Conformance"
activity.Ensemble.type_key = u"cim.2.activity.Ensemble"
activity.ParentSimulation.type_key = u"cim.2.activity.ParentSimulation"
activity.EnsembleAxis.type_key = u"cim.2.activity.EnsembleAxis"
activity.Activity.type_key = u"cim.2.activity.Activity"
activity.EnsembleMember.type_key = u"cim.2.activity.EnsembleMember"
platform.StorageVolume.type_key = u"cim.2.platform.StorageVolume"
platform.Partition.type_key = u"cim.2.platform.Partition"
platform.Performance.type_key = u"cim.2.platform.Performance"
platform.ComponentPerformance.type_key = u"cim.2.platform.ComponentPerformance"
platform.StoragePool.type_key = u"cim.2.platform.StoragePool"
platform.ComputePool.type_key = u"cim.2.platform.ComputePool"
platform.Machine.type_key = u"cim.2.platform.Machine"
data.Dataset.type_key = u"cim.2.data.Dataset"
data.Simulation.type_key = u"cim.2.data.Simulation"
data.Downscaling.type_key = u"cim.2.data.Downscaling"
data.VariableCollection.type_key = u"cim.2.data.VariableCollection"
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
science.Extent.type_key = u"cim.2.science.Extent"
science.Process.type_key = u"cim.2.science.Process"
science.Algorithm.type_key = u"cim.2.science.Algorithm"
shared.TimeUnits.type_key = u"cim.2.shared.TimeUnits"
shared.QualityStatus.type_key = u"cim.2.shared.QualityStatus"
shared.CalendarTypes.type_key = u"cim.2.shared.CalendarTypes"
shared.NilReason.type_key = u"cim.2.shared.NilReason"
shared.RoleCode.type_key = u"cim.2.shared.RoleCode"
shared.TextCode.type_key = u"cim.2.shared.TextCode"
shared.PeriodDateTypes.type_key = u"cim.2.shared.PeriodDateTypes"
shared.SlicetimeUnits.type_key = u"cim.2.shared.SlicetimeUnits"
shared.DocumentTypes.type_key = u"cim.2.shared.DocumentTypes"
designing.EnsembleTypes.type_key = u"cim.2.designing.EnsembleTypes"
designing.ExperimentalRelationships.type_key = u"cim.2.designing.ExperimentalRelationships"
designing.ForcingTypes.type_key = u"cim.2.designing.ForcingTypes"
software.ProgrammingLanguage.type_key = u"cim.2.software.ProgrammingLanguage"
software.CouplingFramework.type_key = u"cim.2.software.CouplingFramework"
drs.DrsRealms.type_key = u"cim.2.drs.DrsRealms"
drs.DrsFrequencyTypes.type_key = u"cim.2.drs.DrsFrequencyTypes"
drs.DrsTimeSuffixes.type_key = u"cim.2.drs.DrsTimeSuffixes"
drs.DrsGeographicalOperators.type_key = u"cim.2.drs.DrsGeographicalOperators"
activity.EnsembleTypes.type_key = u"cim.2.activity.EnsembleTypes"
activity.ForcingTypes.type_key = u"cim.2.activity.ForcingTypes"
platform.VolumeUnits.type_key = u"cim.2.platform.VolumeUnits"
platform.StorageSystems.type_key = u"cim.2.platform.StorageSystems"
data.DataAssociationTypes.type_key = u"cim.2.data.DataAssociationTypes"
science.ModelTypes.type_key = u"cim.2.science.ModelTypes"
science.SelectionCardinality.type_key = u"cim.2.science.SelectionCardinality"

