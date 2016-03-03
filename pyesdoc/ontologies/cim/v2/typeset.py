
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
    Detail,
    Responsibility,
    RegularTimeset,
    TemporalConstraint,
    Party,
    NumericalRequirement,
    OnlineResource,
    Ensemble,
    ScientificDomain,
    EntryPoint,
    DrsEnsembleIdentifier,
    Calendar,
    Cimtext,
    ScienceContext,
    Extent,
    Downscaling,
    DatetimeSet,
    KeyFloat,
    ConservationProperties,
    DrsAtomicDataset,
    Activity,
    DrsPublicationDataset,
    SoftwareComponent,
    Grid,
    ComponentBase,
    NumericalExperiment,
    DocReference,
    IrregularDateset,
    DrsTemporalIdentifier,
    DevelopmentPath,
    ForcingConstraint,
    TimePeriod,
    Composition,
    Algorithm,
    Simulation,
    MultiEnsemble,
    QualityReview,
    OutputTemporalRequirement,
    KeyProperties,
    MultiTimeEnsemble,
    DomainProperties,
    Tuning,
    Model,
    Variable,
    Partition,
    UberEnsemble,
    AxisMember,
    Resolution,
    SubProcess,
    TimesliceList,
    Performance,
    ComputePool,
    ParentSimulation,
    ExternalDocument,
    EnsembleMember,
    DocMetaInfo,
    DrsGeographicalIndicator,
    NumberArray,
    Dataset,
    Conformance,
    Reference,
    SimulationPlan,
    Pid,
    ComponentPerformance,
    DateTime,
    StoragePool,
    Gridspec,
    EnsembleRequirement,
    Process,
    Project,
    StorageVolume,
    EnsembleAxis,
    VariableCollection,
    # Enums
    PeriodDateTypes,
    ForcingTypes,
    TimeUnits,
    NilReason,
    DrsGeographicalOperators,
    EnsembleTypes,
    SelectionCardinality,
    SlicetimeUnits,
    VolumeUnits,
    ProgrammingLanguage,
    DrsFrequencyTypes,
    RoleCode,
    QualityStatus,
    ModelTypes,
    CalendarTypes,
    ExperimentalRelationships,
    ForcingTypes,
    CouplingFramework,
    DocumentTypes,
    EnsembleTypes,
    DrsRealms,
    DataAssociationTypes,
    TextCode,
    DrsTimeSuffixes,
    StorageSystems,
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
    science.Detail,
    shared.Responsibility,
    shared.RegularTimeset,
    designing.TemporalConstraint,
    shared.Party,
    designing.NumericalRequirement,
    shared.OnlineResource,
    activity.Ensemble,
    science.ScientificDomain,
    software.EntryPoint,
    drs.DrsEnsembleIdentifier,
    shared.Calendar,
    shared.Cimtext,
    science.ScienceContext,
    science.Extent,
    data.Downscaling,
    shared.DatetimeSet,
    shared.KeyFloat,
    science.ConservationProperties,
    drs.DrsAtomicDataset,
    activity.Activity,
    drs.DrsPublicationDataset,
    software.SoftwareComponent,
    science.Grid,
    software.ComponentBase,
    designing.NumericalExperiment,
    shared.DocReference,
    shared.IrregularDateset,
    drs.DrsTemporalIdentifier,
    software.DevelopmentPath,
    designing.ForcingConstraint,
    shared.TimePeriod,
    software.Composition,
    science.Algorithm,
    data.Simulation,
    designing.MultiEnsemble,
    shared.QualityReview,
    designing.OutputTemporalRequirement,
    science.KeyProperties,
    designing.MultiTimeEnsemble,
    designing.DomainProperties,
    science.Tuning,
    science.Model,
    software.Variable,
    platform.Partition,
    activity.UberEnsemble,
    activity.AxisMember,
    science.Resolution,
    science.SubProcess,
    shared.TimesliceList,
    platform.Performance,
    platform.ComputePool,
    activity.ParentSimulation,
    shared.ExternalDocument,
    activity.EnsembleMember,
    shared.DocMetaInfo,
    drs.DrsGeographicalIndicator,
    shared.NumberArray,
    data.Dataset,
    activity.Conformance,
    shared.Reference,
    designing.SimulationPlan,
    shared.Pid,
    platform.ComponentPerformance,
    shared.DateTime,
    platform.StoragePool,
    software.Gridspec,
    designing.EnsembleRequirement,
    science.Process,
    designing.Project,
    platform.StorageVolume,
    activity.EnsembleAxis,
    data.VariableCollection,
)

# Supported enums.
ENUMS = (
    shared.PeriodDateTypes,
    designing.ForcingTypes,
    shared.TimeUnits,
    shared.NilReason,
    drs.DrsGeographicalOperators,
    designing.EnsembleTypes,
    science.SelectionCardinality,
    shared.SlicetimeUnits,
    platform.VolumeUnits,
    software.ProgrammingLanguage,
    drs.DrsFrequencyTypes,
    shared.RoleCode,
    shared.QualityStatus,
    science.ModelTypes,
    shared.CalendarTypes,
    designing.ExperimentalRelationships,
    activity.ForcingTypes,
    software.CouplingFramework,
    shared.DocumentTypes,
    activity.EnsembleTypes,
    drs.DrsRealms,
    data.DataAssociationTypes,
    shared.TextCode,
    drs.DrsTimeSuffixes,
    platform.StorageSystems,
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
        'storage_pools',
        'partition',
        'description',
        'meta',
        'when_used',
        'institution',
        'online_documentation',
        'model_number',
        'compute_pools',
        'vendor',
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
    shared.Responsibility: (
        'role',
        'when',
        'party',
    ),
    shared.RegularTimeset: (
        'length',
        'increment',
        'length',
        'start_date',
    ),
    designing.TemporalConstraint: (
        'keywords',
        'conformance_is_requested',
        'long_name',
        'references',
        'additional_requirements',
        'meta',
        'responsible_parties',
        'name',
        'rationale',
        'required_calendar',
        'required_duration',
        'duration',
        'start_date',
        'canonical_name',
        'start_flexibility',
        'description',
    ),
    shared.Party: (
        'organisation',
        'address',
        'name',
        'meta',
        'orcid_id',
        'url',
        'email',
    ),
    designing.NumericalRequirement: (
        'name',
        'keywords',
        'long_name',
        'references',
        'duration',
        'additional_requirements',
        'description',
        'meta',
        'rationale',
        'canonical_name',
        'conformance_is_requested',
        'responsible_parties',
    ),
    shared.OnlineResource: (
        'protocol',
        'name',
        'linkage',
        'description',
    ),
    activity.Ensemble: (
        'supported',
        'long_name',
        'references',
        'common_conformances',
        'meta',
        'responsible_parties',
        'name',
        'keywords',
        'documentation',
        'rationale',
        'has_ensemble_axes',
        'duration',
        'members',
        'canonical_name',
        'part_of',
        'description',
    ),
    science.ScientificDomain: (
        'name',
        'realm',
        'differing_key_properties',
        'meta',
        'id',
        'overview',
        'references',
        'simulates',
    ),
    software.EntryPoint: (
        'name',
    ),
    drs.DrsEnsembleIdentifier: (
        'initialisation_method_number',
        'perturbation_number',
        'realisation_number',
    ),
    shared.Calendar: (
        'month_lengths',
        'description',
        'standard_name',
        'name',
    ),
    shared.Cimtext: (
        'content',
        'content_type',
    ),
    science.ScienceContext: (
        'context',
        'id',
        'name',
    ),
    science.Extent: (
        'is_global',
        'southern_boundary',
        'western_boundary',
        'northern_boundary',
        'z_units',
        'bottom_vertical_level',
        'top_vertical_level',
        'eastern_boundary',
        'region_known_as',
    ),
    data.Downscaling: (
        'calendar',
        'downscaled_from',
        'ensemble_identifier',
        'long_name',
        'parent_simulation',
        'responsible_parties',
        'part_of_project',
        'keywords',
        'ran_for_experiments',
        'primary_ensemble',
        'references',
        'name',
        'description',
        'rationale',
        'used',
        'canonical_name',
        'duration',
        'meta',
    ),
    shared.DatetimeSet: (
        'length',
    ),
    shared.KeyFloat: (
        'key',
        'value',
    ),
    science.ConservationProperties: (
        'corrected_conserved_prognostic_variables',
        'correction_methodology',
        'flux_correction_was_used',
    ),
    drs.DrsAtomicDataset: (
        'geographical_constraint',
        'activity',
        'model',
        'frequency',
        'variable_name',
        'realm',
        'mip_table',
        'institute',
        'version_number',
        'experiment',
        'temporal_constraint',
        'product',
        'ensemble_member',
    ),
    activity.Activity: (
        'keywords',
        'description',
        'duration',
        'references',
        'long_name',
        'responsible_parties',
        'rationale',
        'canonical_name',
        'name',
        'meta',
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
    software.SoftwareComponent: (
        'language',
        'description',
        'development_history',
        'documentation',
        'coupling_framework',
        'name',
        'repository',
        'license',
        'dependencies',
        'composition',
        'long_name',
        'grid',
        'release_date',
        'version',
        'connection_points',
        'sub_components',
    ),
    science.Grid: (
        'meta',
        'name',
        'vertical_grid_layout',
        'horizontal_grid_layout',
        'grid_extent',
        'horizontal_grid_type',
        'additional_details',
        'vertical_grid_type',
    ),
    software.ComponentBase: (
        'documentation',
        'description',
        'repository',
        'long_name',
        'name',
        'release_date',
        'development_history',
        'version',
    ),
    designing.NumericalExperiment: (
        'related_experiments',
        'name',
        'keywords',
        'long_name',
        'requirements',
        'references',
        'description',
        'meta',
        'rationale',
        'canonical_name',
        'duration',
        'responsible_parties',
    ),
    shared.DocReference: (
        'context',
        'name',
        'linkage',
        'id',
        'version',
        'protocol',
        'constraint_vocabulary',
        'description',
        'relationship',
        'type',
    ),
    shared.IrregularDateset: (
        'date_set',
        'length',
    ),
    drs.DrsTemporalIdentifier: (
        'end',
        'start',
        'suffix',
    ),
    software.DevelopmentPath: (
        'funding_sources',
        'developed_in_house',
        'previous_version',
        'creators',
        'consortium_name',
    ),
    designing.ForcingConstraint: (
        'keywords',
        'conformance_is_requested',
        'additional_constraint',
        'long_name',
        'additional_requirements',
        'category',
        'meta',
        'responsible_parties',
        'duration',
        'code',
        'rationale',
        'data_link',
        'references',
        'forcing_type',
        'name',
        'group',
        'canonical_name',
        'origin',
        'description',
    ),
    shared.TimePeriod: (
        'date',
        'calendar',
        'length',
        'date_type',
        'units',
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
    science.Algorithm: (
        'forced_variables',
        'context',
        'implementation_overview',
        'name',
        'prognostic_variables',
        'references',
        'diagnostic_variables',
        'id',
    ),
    data.Simulation: (
        'calendar',
        'ensemble_identifier',
        'references',
        'parent_simulation',
        'meta',
        'part_of_project',
        'keywords',
        'primary_ensemble',
        'long_name',
        'ran_for_experiments',
        'name',
        'description',
        'rationale',
        'used',
        'canonical_name',
        'duration',
        'responsible_parties',
    ),
    designing.MultiEnsemble: (
        'keywords',
        'ensemble_axis',
        'canonical_name',
        'conformance_is_requested',
        'long_name',
        'references',
        'additional_requirements',
        'responsible_parties',
        'description',
        'rationale',
        'duration',
        'name',
        'meta',
    ),
    shared.QualityReview: (
        'metadata_reviewer',
        'quality_status',
        'quality_description',
        'date',
    ),
    designing.OutputTemporalRequirement: (
        'keywords',
        'additional_requirements',
        'continuous_subset',
        'canonical_name',
        'conformance_is_requested',
        'long_name',
        'references',
        'sliced_subset',
        'responsible_parties',
        'description',
        'rationale',
        'throughout',
        'duration',
        'name',
        'meta',
    ),
    science.KeyProperties: (
        'time_step',
        'resolution',
        'extra_conservation_properties',
        'grid',
        'tuning_applied',
        'additional_detail',
    ),
    designing.MultiTimeEnsemble: (
        'ensemble_members',
        'canonical_name',
        'conformance_is_requested',
        'long_name',
        'references',
        'additional_requirements',
        'responsible_parties',
        'description',
        'meta',
        'rationale',
        'duration',
        'name',
        'keywords',
    ),
    designing.DomainProperties: (
        'keywords',
        'references',
        'canonical_name',
        'conformance_is_requested',
        'required_extent',
        'long_name',
        'additional_requirements',
        'responsible_parties',
        'required_resolution',
        'meta',
        'rationale',
        'duration',
        'name',
        'description',
    ),
    science.Tuning: (
        'global_mean_metrics_used',
        'description',
        'regional_metrics_used',
        'trend_metrics_used',
    ),
    science.Model: (
        'documentation',
        'id',
        'development_history',
        'repository',
        'model_default_properties',
        'long_name',
        'name',
        'category',
        'internal_software_components',
        'description',
        'meta',
        'release_date',
        'simulates',
        'version',
        'coupler',
        'coupled_components',
    ),
    software.Variable: (
        'description',
        'name',
        'prognostic',
    ),
    platform.Partition: (
        'name',
        'institution',
        'description',
        'model_number',
        'online_documentation',
        'partition',
        'when_used',
        'storage_pools',
        'compute_pools',
        'vendor',
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
        'members',
        'rationale',
        'description',
        'references',
        'part_of',
        'responsible_parties',
        'canonical_name',
        'duration',
        'meta',
    ),
    activity.AxisMember: (
        'extra_detail',
        'value',
        'index',
        'description',
    ),
    science.Resolution: (
        'typical_y_degrees',
        'number_of_levels',
        'is_adaptive_grid',
        'number_of_xy_gridpoints',
        'typical_x_degrees',
        'name',
        'equivalent_resolution_km',
    ),
    science.SubProcess: (
        'implementation_overview',
        'id',
        'name',
        'references',
        'properties',
        'context',
    ),
    shared.TimesliceList: (
        'members',
        'units',
    ),
    platform.Performance: (
        'platform',
        'total_nodes_used',
        'compiler',
        'chsy',
        'coupler_load',
        'load_imbalance',
        'meta',
        'subcomponent_performance',
        'io_load',
        'asypd',
        'model',
        'sypd',
        'name',
        'memory_bloat',
    ),
    platform.ComputePool: (
        'cpu_type',
        'accelerators_per_node',
        'accelerator_type',
        'compute_cores_per_node',
        'description',
        'operating_system',
        'number_of_nodes',
        'name',
        'memory_per_node',
        'interconnect',
        'model_number',
    ),
    activity.ParentSimulation: (
        'branch_time_in_parent',
        'parent',
        'branch_time_in_child',
    ),
    shared.ExternalDocument: (
        'authorship',
        'date',
        'name',
        'publication_detail',
        'online_at',
        'meta',
        'title',
        'doi',
    ),
    activity.EnsembleMember: (
        'ran_on',
        'variant_id',
        'had_performance',
        'simulation',
        'errata',
    ),
    shared.DocMetaInfo: (
        'external_ids',
        'drs_path',
        'source_key',
        'type',
        'type_display_name',
        'update_date',
        'drs_keys',
        'institute',
        'language',
        'type_sort_key',
        'sort_key',
        'id',
        'version',
        'create_date',
        'project',
        'author',
        'source',
    ),
    drs.DrsGeographicalIndicator: (
        'spatial_domain',
        'bounding_box',
        'operator',
    ),
    shared.NumberArray: (
        'values',
    ),
    data.Dataset: (
        'references',
        'availability',
        'meta',
        'responsible_parties',
        'related_to_dataset',
        'description',
        'produced_by',
        'drs_datasets',
        'name',
    ),
    activity.Conformance: (
        'keywords',
        'name',
        'references',
        'long_name',
        'target_requirement',
        'description',
        'meta',
        'rationale',
        'canonical_name',
        'duration',
        'responsible_parties',
    ),
    shared.Reference: (
        'context',
        'document',
    ),
    designing.SimulationPlan: (
        'name',
        'expected_platform',
        'long_name',
        'references',
        'description',
        'will_support_experiments',
        'duration',
        'rationale',
        'expected_model',
        'meta',
        'responsible_parties',
        'canonical_name',
        'expected_performance_sypd',
        'keywords',
    ),
    shared.Pid: (
        'id',
        'resolution_service',
    ),
    platform.ComponentPerformance: (
        'component',
        'speed',
        'component_name',
        'cores_used',
        'nodes_used',
    ),
    shared.DateTime: (
        'offset',
        'value',
    ),
    platform.StoragePool: (
        'description',
        'volume_available',
        'vendor',
        'type',
        'name',
    ),
    software.Gridspec: (
        'description',
    ),
    designing.EnsembleRequirement: (
        'minimum_size',
        'keywords',
        'references',
        'canonical_name',
        'conformance_is_requested',
        'ensemble_member',
        'long_name',
        'additional_requirements',
        'responsible_parties',
        'description',
        'rationale',
        'ensemble_type',
        'duration',
        'name',
        'meta',
    ),
    science.Process: (
        'context',
        'implementation_overview',
        'algorithms',
        'name',
        'references',
        'id',
        'sub_processes',
        'properties',
        'keywords',
    ),
    designing.Project: (
        'name',
        'keywords',
        'long_name',
        'requires_experiments',
        'references',
        'duration',
        'rationale',
        'sub_projects',
        'meta',
        'responsible_parties',
        'canonical_name',
        'previous_projects',
        'description',
    ),
    platform.StorageVolume: (
        'units',
        'volume',
    ),
    activity.EnsembleAxis: (
        'member',
        'extra_detail',
        'target_requirement',
        'short_identifier',
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
    science.Detail: (
        'with_cardinality',
        'from_vocab',
        'select',
        'content',
        'detail_selection',
    ),
    shared.Responsibility: (
        'when',
        'party',
        'role',
    ),
    shared.RegularTimeset: (
        'start_date',
        'increment',
        'length',
    ),
    designing.TemporalConstraint: (
        'start_date',
        'required_calendar',
        'start_flexibility',
        'required_duration',
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
    designing.NumericalRequirement: (
        'additional_requirements',
        'conformance_is_requested',
    ),
    shared.OnlineResource: (
        'protocol',
        'description',
        'name',
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
    science.ScientificDomain: (
        'name',
        'id',
        'differing_key_properties',
        'references',
        'realm',
        'overview',
        'meta',
        'simulates',
    ),
    software.EntryPoint: (
        'name',
    ),
    drs.DrsEnsembleIdentifier: (
        'initialisation_method_number',
        'realisation_number',
        'perturbation_number',
    ),
    shared.Calendar: (
        'standard_name',
        'name',
        'description',
        'month_lengths',
    ),
    shared.Cimtext: (
        'content',
        'content_type',
    ),
    science.ScienceContext: (
        'context',
        'name',
        'id',
    ),
    science.Extent: (
        'is_global',
        'western_boundary',
        'northern_boundary',
        'eastern_boundary',
        'z_units',
        'region_known_as',
        'top_vertical_level',
        'southern_boundary',
        'bottom_vertical_level',
    ),
    data.Downscaling: (
        'downscaled_from',
    ),
    shared.DatetimeSet: (
        'length',
    ),
    shared.KeyFloat: (
        'key',
        'value',
    ),
    science.ConservationProperties: (
        'corrected_conserved_prognostic_variables',
        'flux_correction_was_used',
        'correction_methodology',
    ),
    drs.DrsAtomicDataset: (
        'temporal_constraint',
        'geographical_constraint',
        'variable_name',
        'ensemble_member',
        'mip_table',
    ),
    activity.Activity: (
        'keywords',
        'name',
        'references',
        'long_name',
        'canonical_name',
        'responsible_parties',
        'meta',
        'rationale',
        'duration',
        'description',
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
    science.Grid: (
        'name',
        'vertical_grid_layout',
        'horizontal_grid_layout',
        'additional_details',
        'horizontal_grid_type',
        'vertical_grid_type',
        'meta',
        'grid_extent',
    ),
    software.ComponentBase: (
        'documentation',
        'name',
        'long_name',
        'repository',
        'description',
        'development_history',
        'release_date',
        'version',
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
    shared.IrregularDateset: (
        'date_set',
    ),
    drs.DrsTemporalIdentifier: (
        'end',
        'suffix',
        'start',
    ),
    software.DevelopmentPath: (
        'developed_in_house',
        'consortium_name',
        'funding_sources',
        'previous_version',
        'creators',
    ),
    designing.ForcingConstraint: (
        'data_link',
        'forcing_type',
        'additional_constraint',
        'origin',
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
    designing.MultiEnsemble: (
        'ensemble_axis',
    ),
    shared.QualityReview: (
        'quality_status',
        'date',
        'quality_description',
        'metadata_reviewer',
    ),
    designing.OutputTemporalRequirement: (
        'continuous_subset',
        'throughout',
        'sliced_subset',
    ),
    science.KeyProperties: (
        'time_step',
        'extra_conservation_properties',
        'tuning_applied',
        'grid',
        'resolution',
        'additional_detail',
    ),
    designing.MultiTimeEnsemble: (
        'ensemble_members',
    ),
    designing.DomainProperties: (
        'required_extent',
        'required_resolution',
    ),
    science.Tuning: (
        'regional_metrics_used',
        'trend_metrics_used',
        'description',
        'global_mean_metrics_used',
    ),
    science.Model: (
        'id',
        'model_default_properties',
        'category',
        'internal_software_components',
        'meta',
        'simulates',
        'coupler',
        'coupled_components',
    ),
    software.Variable: (
        'description',
        'prognostic',
        'name',
    ),
    platform.Partition: (
        'name',
        'partition',
        'description',
        'storage_pools',
        'when_used',
        'institution',
        'online_documentation',
        'model_number',
        'compute_pools',
        'vendor',
    ),
    activity.UberEnsemble: (
        'child_ensembles',
    ),
    activity.AxisMember: (
        'value',
        'description',
        'index',
        'extra_detail',
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
    science.SubProcess: (
        'implementation_overview',
        'references',
        'properties',
    ),
    shared.TimesliceList: (
        'members',
        'units',
    ),
    platform.Performance: (
        'total_nodes_used',
        'compiler',
        'meta',
        'subcomponent_performance',
        'name',
        'coupler_load',
        'chsy',
        'io_load',
        'sypd',
        'memory_bloat',
        'platform',
        'model',
        'load_imbalance',
        'asypd',
    ),
    platform.ComputePool: (
        'number_of_nodes',
        'cpu_type',
        'accelerators_per_node',
        'accelerator_type',
        'memory_per_node',
        'name',
        'operating_system',
        'interconnect',
        'description',
        'compute_cores_per_node',
        'model_number',
    ),
    activity.ParentSimulation: (
        'parent',
        'branch_time_in_child',
        'branch_time_in_parent',
    ),
    shared.ExternalDocument: (
        'authorship',
        'date',
        'name',
        'publication_detail',
        'online_at',
        'meta',
        'title',
        'doi',
    ),
    activity.EnsembleMember: (
        'variant_id',
        'errata',
        'had_performance',
        'simulation',
        'ran_on',
    ),
    shared.DocMetaInfo: (
        'institute',
        'drs_path',
        'type',
        'version',
        'language',
        'create_date',
        'author',
        'type_display_name',
        'source',
        'id',
        'source_key',
        'update_date',
        'project',
        'external_ids',
        'drs_keys',
        'type_sort_key',
        'sort_key',
    ),
    drs.DrsGeographicalIndicator: (
        'spatial_domain',
        'bounding_box',
        'operator',
    ),
    shared.NumberArray: (
        'values',
    ),
    data.Dataset: (
        'references',
        'responsible_parties',
        'availability',
        'meta',
        'drs_datasets',
        'name',
        'related_to_dataset',
        'produced_by',
        'description',
    ),
    activity.Conformance: (
        'target_requirement',
    ),
    shared.Reference: (
        'context',
        'document',
    ),
    designing.SimulationPlan: (
        'will_support_experiments',
        'expected_model',
        'expected_platform',
        'expected_performance_sypd',
    ),
    shared.Pid: (
        'id',
        'resolution_service',
    ),
    platform.ComponentPerformance: (
        'cores_used',
        'nodes_used',
        'speed',
        'component',
        'component_name',
    ),
    shared.DateTime: (
        'offset',
        'value',
    ),
    platform.StoragePool: (
        'description',
        'vendor',
        'name',
        'volume_available',
        'type',
    ),
    software.Gridspec: (
        'description',
    ),
    designing.EnsembleRequirement: (
        'ensemble_type',
        'ensemble_member',
        'minimum_size',
    ),
    science.Process: (
        'references',
        'sub_processes',
        'implementation_overview',
        'keywords',
        'properties',
        'algorithms',
    ),
    designing.Project: (
        'requires_experiments',
        'previous_projects',
        'sub_projects',
    ),
    platform.StorageVolume: (
        'units',
        'volume',
    ),
    activity.EnsembleAxis: (
        'target_requirement',
        'short_identifier',
        'extra_detail',
        'member',
    ),
    data.VariableCollection: (
        'collection_name',
        'variables',
    ),
}

# Base classes.
BASE_CLASSES = defaultdict(tuple)
BASE_CLASSES[platform.Machine] = (platform.Partition, )
BASE_CLASSES[science.Detail] = (science.ScienceContext, )
BASE_CLASSES[shared.RegularTimeset] = (shared.DatetimeSet, )
BASE_CLASSES[designing.TemporalConstraint] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.NumericalRequirement] = (activity.Activity, )
BASE_CLASSES[activity.Ensemble] = (activity.Activity, )
BASE_CLASSES[data.Downscaling] = (data.Simulation, activity.Activity, )
BASE_CLASSES[drs.DrsAtomicDataset] = (drs.DrsPublicationDataset, )
BASE_CLASSES[software.SoftwareComponent] = (software.ComponentBase, )
BASE_CLASSES[designing.NumericalExperiment] = (activity.Activity, )
BASE_CLASSES[shared.DocReference] = (shared.OnlineResource, )
BASE_CLASSES[shared.IrregularDateset] = (shared.DatetimeSet, )
BASE_CLASSES[designing.ForcingConstraint] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[science.Algorithm] = (science.ScienceContext, )
BASE_CLASSES[data.Simulation] = (activity.Activity, )
BASE_CLASSES[designing.MultiEnsemble] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.OutputTemporalRequirement] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.MultiTimeEnsemble] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.DomainProperties] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[science.Model] = (software.ComponentBase, )
BASE_CLASSES[activity.UberEnsemble] = (activity.Ensemble, activity.Activity, )
BASE_CLASSES[science.SubProcess] = (science.ScienceContext, )
BASE_CLASSES[activity.Conformance] = (activity.Activity, )
BASE_CLASSES[designing.SimulationPlan] = (activity.Activity, )
BASE_CLASSES[designing.EnsembleRequirement] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[science.Process] = (science.ScienceContext, )
BASE_CLASSES[designing.Project] = (activity.Activity, )

# Classes with base classes.
BASE_CLASSED = tuple(BASE_CLASSES.keys())

# Sub classes.
SUB_CLASSES = defaultdict(tuple)
SUB_CLASSES[shared.DatetimeSet] = (
    shared.IrregularDateset,
    shared.RegularTimeset,
    )
SUB_CLASSES[data.Simulation] = (
    data.Downscaling,
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
SUB_CLASSES[drs.DrsPublicationDataset] = (
    drs.DrsAtomicDataset,
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

