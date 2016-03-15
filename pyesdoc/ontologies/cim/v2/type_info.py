
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.type_info.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from collections import defaultdict
import datetime
import uuid


import typeset_for_drs_package as drs
import typeset_for_designing_package as designing
import typeset_for_software_package as software
import typeset_for_shared_package as shared
import typeset_for_science_package as science
import typeset_for_platform_package as platform
import typeset_for_data_package as data
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
    'CONSTRAINTS',
    'KEYS',
    'HELP'
    ]

# Supported packages.
PACKAGES = (
    drs,
    designing,
    software,
    shared,
    science,
    platform,
    data,
    activity,
)

# ------------------------------------------------
# Classes.
# ------------------------------------------------

# Supported classes.
CLASSES = (
    activity.Activity,
    drs.DrsAtomicDataset,
    software.Composition,
    drs.DrsGeographicalIndicator,
    designing.SimulationPlan,
    activity.Ensemble,
    science.ScienceContext,
    shared.QualityReview,
    shared.DatetimeSet,
    designing.OutputTemporalRequirement,
    science.ConservationProperties,
    shared.RegularTimeset,
    software.Variable,
    shared.Reference,
    designing.MultiEnsemble,
    shared.Responsibility,
    data.VariableCollection,
    platform.StoragePool,
    platform.Machine,
    designing.MultiTimeEnsemble,
    drs.DrsPublicationDataset,
    science.KeyProperties,
    science.SubProcess,
    science.ScientificDomain,
    designing.NumericalExperiment,
    data.Downscaling,
    drs.DrsTemporalIdentifier,
    shared.TimesliceList,
    science.Resolution,
    software.ComponentBase,
    drs.DrsEnsembleIdentifier,
    shared.KeyFloat,
    software.DevelopmentPath,
    software.SoftwareComponent,
    platform.StorageVolume,
    shared.IrregularDateset,
    shared.Pid,
    activity.EnsembleMember,
    activity.UberEnsemble,
    shared.Party,
    science.Algorithm,
    designing.DomainProperties,
    platform.ComputePool,
    shared.TimePeriod,
    software.Gridspec,
    shared.OnlineResource,
    designing.EnsembleRequirement,
    platform.Partition,
    designing.NumericalRequirement,
    designing.ForcingConstraint,
    shared.ExternalDocument,
    shared.Calendar,
    shared.NumberArray,
    activity.Conformance,
    designing.TemporalConstraint,
    shared.DocMetaInfo,
    designing.Project,
    data.Dataset,
    science.Process,
    shared.DateTime,
    science.Tuning,
    shared.DocReference,
    science.Detail,
    software.EntryPoint,
    data.Simulation,
    science.Model,
    activity.EnsembleAxis,
    activity.AxisMember,
    science.Grid,
    platform.ComponentPerformance,
    science.Extent,
    shared.Cimtext,
    platform.Performance,
    activity.ParentSimulation,
)

# Supported class properties.
CLASS_PROPERTIES = { 
    activity.Activity: (
        'duration',
        'long_name',
        'references',
        'meta',
        'description',
        'keywords',
        'responsible_parties',
        'name',
        'rationale',
        'canonical_name',
    ),
    drs.DrsAtomicDataset: (
        'ensemble_member',
        'temporal_constraint',
        'model',
        'realm',
        'activity',
        'geographical_constraint',
        'product',
        'frequency',
        'variable_name',
        'version_number',
        'mip_table',
        'institute',
        'experiment',
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
    designing.SimulationPlan: (
        'canonical_name',
        'expected_model',
        'long_name',
        'expected_performance_sypd',
        'meta',
        'rationale',
        'description',
        'expected_platform',
        'responsible_parties',
        'duration',
        'will_support_experiments',
        'keywords',
        'name',
        'references',
    ),
    activity.Ensemble: (
        'references',
        'common_conformances',
        'meta',
        'description',
        'responsible_parties',
        'duration',
        'documentation',
        'keywords',
        'long_name',
        'canonical_name',
        'has_ensemble_axes',
        'members',
        'rationale',
        'part_of',
        'supported',
        'name',
    ),
    science.ScienceContext: (
        'context',
        'id',
        'name',
    ),
    shared.QualityReview: (
        'date',
        'metadata_reviewer',
        'quality_description',
        'quality_status',
    ),
    shared.DatetimeSet: (
        'length',
    ),
    designing.OutputTemporalRequirement: (
        'duration',
        'long_name',
        'references',
        'sliced_subset',
        'additional_requirements',
        'conformance_is_requested',
        'throughout',
        'meta',
        'description',
        'rationale',
        'responsible_parties',
        'keywords',
        'name',
        'continuous_subset',
        'canonical_name',
    ),
    science.ConservationProperties: (
        'corrected_conserved_prognostic_variables',
        'correction_methodology',
        'flux_correction_was_used',
    ),
    shared.RegularTimeset: (
        'length',
        'increment',
        'length',
        'start_date',
    ),
    software.Variable: (
        'name',
        'prognostic',
        'description',
    ),
    shared.Reference: (
        'context',
        'document',
    ),
    designing.MultiEnsemble: (
        'duration',
        'references',
        'canonical_name',
        'additional_requirements',
        'conformance_is_requested',
        'meta',
        'description',
        'keywords',
        'rationale',
        'responsible_parties',
        'name',
        'ensemble_axis',
        'long_name',
    ),
    shared.Responsibility: (
        'party',
        'role',
        'when',
    ),
    data.VariableCollection: (
        'collection_name',
        'variables',
    ),
    platform.StoragePool: (
        'description',
        'vendor',
        'volume_available',
        'name',
        'type',
    ),
    platform.Machine: (
        'online_documentation',
        'compute_pools',
        'institution',
        'vendor',
        'partition',
        'name',
        'model_number',
        'storage_pools',
        'when_used',
        'meta',
        'description',
    ),
    designing.MultiTimeEnsemble: (
        'duration',
        'references',
        'canonical_name',
        'additional_requirements',
        'conformance_is_requested',
        'meta',
        'rationale',
        'description',
        'ensemble_members',
        'responsible_parties',
        'name',
        'keywords',
        'long_name',
    ),
    drs.DrsPublicationDataset: (
        'experiment',
        'institute',
        'model',
        'activity',
        'frequency',
        'product',
        'realm',
        'version_number',
    ),
    science.KeyProperties: (
        'grid',
        'extra_conservation_properties',
        'time_step',
        'resolution',
        'tuning_applied',
        'additional_detail',
    ),
    science.SubProcess: (
        'implementation_overview',
        'references',
        'properties',
        'context',
        'id',
        'name',
    ),
    science.ScientificDomain: (
        'meta',
        'simulates',
        'realm',
        'name',
        'overview',
        'differing_key_properties',
        'id',
        'references',
    ),
    designing.NumericalExperiment: (
        'canonical_name',
        'name',
        'long_name',
        'related_experiments',
        'meta',
        'description',
        'rationale',
        'responsible_parties',
        'duration',
        'requirements',
        'keywords',
        'references',
    ),
    data.Downscaling: (
        'primary_ensemble',
        'references',
        'ran_for_experiments',
        'description',
        'responsible_parties',
        'used',
        'part_of_project',
        'keywords',
        'canonical_name',
        'calendar',
        'long_name',
        'ensemble_identifier',
        'meta',
        'parent_simulation',
        'name',
        'downscaled_from',
        'rationale',
        'duration',
    ),
    drs.DrsTemporalIdentifier: (
        'end',
        'start',
        'suffix',
    ),
    shared.TimesliceList: (
        'members',
        'units',
    ),
    science.Resolution: (
        'is_adaptive_grid',
        'number_of_xy_gridpoints',
        'typical_x_degrees',
        'number_of_levels',
        'typical_y_degrees',
        'name',
        'equivalent_resolution_km',
    ),
    software.ComponentBase: (
        'documentation',
        'repository',
        'development_history',
        'version',
        'name',
        'description',
        'release_date',
        'long_name',
    ),
    drs.DrsEnsembleIdentifier: (
        'realisation_number',
        'perturbation_number',
        'initialisation_method_number',
    ),
    shared.KeyFloat: (
        'key',
        'value',
    ),
    software.DevelopmentPath: (
        'creators',
        'developed_in_house',
        'funding_sources',
        'consortium_name',
        'previous_version',
    ),
    software.SoftwareComponent: (
        'language',
        'repository',
        'connection_points',
        'coupling_framework',
        'license',
        'development_history',
        'dependencies',
        'version',
        'sub_components',
        'long_name',
        'grid',
        'name',
        'composition',
        'description',
        'release_date',
        'documentation',
    ),
    platform.StorageVolume: (
        'units',
        'volume',
    ),
    shared.IrregularDateset: (
        'length',
        'date_set',
    ),
    shared.Pid: (
        'id',
        'resolution_service',
    ),
    activity.EnsembleMember: (
        'ran_on',
        'simulation',
        'errata',
        'had_performance',
        'variant_id',
    ),
    activity.UberEnsemble: (
        'references',
        'has_ensemble_axes',
        'common_conformances',
        'description',
        'child_ensembles',
        'responsible_parties',
        'duration',
        'documentation',
        'keywords',
        'canonical_name',
        'long_name',
        'meta',
        'supported',
        'part_of',
        'members',
        'rationale',
        'name',
    ),
    shared.Party: (
        'organisation',
        'address',
        'name',
        'email',
        'meta',
        'url',
        'orcid_id',
    ),
    science.Algorithm: (
        'context',
        'implementation_overview',
        'id',
        'prognostic_variables',
        'name',
        'diagnostic_variables',
        'forced_variables',
        'references',
    ),
    designing.DomainProperties: (
        'duration',
        'long_name',
        'references',
        'required_resolution',
        'additional_requirements',
        'conformance_is_requested',
        'meta',
        'description',
        'keywords',
        'rationale',
        'responsible_parties',
        'name',
        'required_extent',
        'canonical_name',
    ),
    platform.ComputePool: (
        'number_of_nodes',
        'compute_cores_per_node',
        'memory_per_node',
        'cpu_type',
        'interconnect',
        'model_number',
        'accelerator_type',
        'operating_system',
        'name',
        'accelerators_per_node',
        'description',
    ),
    shared.TimePeriod: (
        'calendar',
        'length',
        'date',
        'units',
        'date_type',
    ),
    software.Gridspec: (
        'description',
    ),
    shared.OnlineResource: (
        'linkage',
        'name',
        'description',
        'protocol',
    ),
    designing.EnsembleRequirement: (
        'duration',
        'long_name',
        'references',
        'ensemble_type',
        'additional_requirements',
        'conformance_is_requested',
        'minimum_size',
        'meta',
        'description',
        'rationale',
        'responsible_parties',
        'name',
        'ensemble_member',
        'keywords',
        'canonical_name',
    ),
    platform.Partition: (
        'online_documentation',
        'name',
        'vendor',
        'partition',
        'institution',
        'model_number',
        'description',
        'when_used',
        'compute_pools',
        'storage_pools',
    ),
    designing.NumericalRequirement: (
        'canonical_name',
        'name',
        'long_name',
        'conformance_is_requested',
        'meta',
        'description',
        'keywords',
        'rationale',
        'responsible_parties',
        'duration',
        'additional_requirements',
        'references',
    ),
    designing.ForcingConstraint: (
        'category',
        'additional_requirements',
        'conformance_is_requested',
        'code',
        'meta',
        'description',
        'responsible_parties',
        'data_link',
        'forcing_type',
        'canonical_name',
        'long_name',
        'references',
        'group',
        'origin',
        'keywords',
        'name',
        'additional_constraint',
        'rationale',
        'duration',
    ),
    shared.ExternalDocument: (
        'doi',
        'online_at',
        'title',
        'meta',
        'authorship',
        'name',
        'date',
        'publication_detail',
    ),
    shared.Calendar: (
        'description',
        'month_lengths',
        'name',
        'standard_name',
    ),
    shared.NumberArray: (
        'values',
    ),
    activity.Conformance: (
        'canonical_name',
        'name',
        'long_name',
        'target_requirement',
        'meta',
        'description',
        'rationale',
        'responsible_parties',
        'duration',
        'keywords',
        'references',
    ),
    designing.TemporalConstraint: (
        'canonical_name',
        'additional_requirements',
        'conformance_is_requested',
        'description',
        'meta',
        'responsible_parties',
        'required_calendar',
        'required_duration',
        'long_name',
        'references',
        'start_date',
        'start_flexibility',
        'keywords',
        'name',
        'rationale',
        'duration',
    ),
    shared.DocMetaInfo: (
        'external_ids',
        'create_date',
        'sort_key',
        'source',
        'drs_path',
        'source_key',
        'version',
        'type',
        'id',
        'type_sort_key',
        'language',
        'institute',
        'update_date',
        'type_display_name',
        'drs_keys',
        'project',
        'author',
    ),
    designing.Project: (
        'canonical_name',
        'sub_projects',
        'references',
        'long_name',
        'previous_projects',
        'meta',
        'description',
        'rationale',
        'responsible_parties',
        'requires_experiments',
        'keywords',
        'name',
        'duration',
    ),
    data.Dataset: (
        'meta',
        'description',
        'availability',
        'name',
        'responsible_parties',
        'produced_by',
        'related_to_dataset',
        'drs_datasets',
        'references',
    ),
    science.Process: (
        'algorithms',
        'references',
        'keywords',
        'context',
        'implementation_overview',
        'id',
        'name',
        'sub_processes',
        'properties',
    ),
    shared.DateTime: (
        'offset',
        'value',
    ),
    science.Tuning: (
        'description',
        'global_mean_metrics_used',
        'regional_metrics_used',
        'trend_metrics_used',
    ),
    shared.DocReference: (
        'type',
        'name',
        'context',
        'constraint_vocabulary',
        'protocol',
        'relationship',
        'linkage',
        'description',
        'version',
        'id',
    ),
    science.Detail: (
        'content',
        'with_cardinality',
        'detail_selection',
        'from_vocab',
        'id',
        'select',
        'context',
        'name',
    ),
    software.EntryPoint: (
        'name',
    ),
    data.Simulation: (
        'primary_ensemble',
        'references',
        'ran_for_experiments',
        'description',
        'responsible_parties',
        'used',
        'keywords',
        'canonical_name',
        'calendar',
        'long_name',
        'ensemble_identifier',
        'meta',
        'parent_simulation',
        'name',
        'part_of_project',
        'rationale',
        'duration',
    ),
    science.Model: (
        'meta',
        'repository',
        'coupled_components',
        'coupler',
        'simulates',
        'development_history',
        'version',
        'id',
        'name',
        'long_name',
        'internal_software_components',
        'category',
        'model_default_properties',
        'description',
        'release_date',
        'documentation',
    ),
    activity.EnsembleAxis: (
        'target_requirement',
        'short_identifier',
        'member',
        'extra_detail',
    ),
    activity.AxisMember: (
        'extra_detail',
        'index',
        'value',
        'description',
    ),
    science.Grid: (
        'grid_extent',
        'name',
        'horizontal_grid_layout',
        'vertical_grid_layout',
        'horizontal_grid_type',
        'additional_details',
        'meta',
        'vertical_grid_type',
    ),
    platform.ComponentPerformance: (
        'speed',
        'component_name',
        'component',
        'cores_used',
        'nodes_used',
    ),
    science.Extent: (
        'northern_boundary',
        'western_boundary',
        'bottom_vertical_level',
        'southern_boundary',
        'eastern_boundary',
        'region_known_as',
        'is_global',
        'top_vertical_level',
        'z_units',
    ),
    shared.Cimtext: (
        'content',
        'content_type',
    ),
    platform.Performance: (
        'asypd',
        'io_load',
        'sypd',
        'chsy',
        'load_imbalance',
        'subcomponent_performance',
        'name',
        'total_nodes_used',
        'memory_bloat',
        'coupler_load',
        'compiler',
        'meta',
        'model',
        'platform',
    ),
    activity.ParentSimulation: (
        'branch_time_in_child',
        'branch_time_in_parent',
        'parent',
    ),
}

# Supported class own properties.
CLASS_OWN_PROPERTIES = { 
    activity.Activity: (
        'name',
        'references',
        'canonical_name',
        'meta',
        'description',
        'rationale',
        'responsible_parties',
        'duration',
        'keywords',
        'long_name',
    ),
    drs.DrsAtomicDataset: (
        'geographical_constraint',
        'variable_name',
        'temporal_constraint',
        'ensemble_member',
        'mip_table',
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
    designing.SimulationPlan: (
        'expected_model',
        'expected_platform',
        'will_support_experiments',
        'expected_performance_sypd',
    ),
    activity.Ensemble: (
        'has_ensemble_axes',
        'members',
        'common_conformances',
        'part_of',
        'documentation',
        'supported',
    ),
    science.ScienceContext: (
        'context',
        'name',
        'id',
    ),
    shared.QualityReview: (
        'date',
        'quality_status',
        'quality_description',
        'metadata_reviewer',
    ),
    shared.DatetimeSet: (
        'length',
    ),
    designing.OutputTemporalRequirement: (
        'throughout',
        'continuous_subset',
        'sliced_subset',
    ),
    science.ConservationProperties: (
        'corrected_conserved_prognostic_variables',
        'flux_correction_was_used',
        'correction_methodology',
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
    shared.Reference: (
        'context',
        'document',
    ),
    designing.MultiEnsemble: (
        'ensemble_axis',
    ),
    shared.Responsibility: (
        'party',
        'when',
        'role',
    ),
    data.VariableCollection: (
        'collection_name',
        'variables',
    ),
    platform.StoragePool: (
        'description',
        'type',
        'vendor',
        'volume_available',
        'name',
    ),
    platform.Machine: (
        'meta',
    ),
    designing.MultiTimeEnsemble: (
        'ensemble_members',
    ),
    drs.DrsPublicationDataset: (
        'institute',
        'model',
        'realm',
        'activity',
        'product',
        'version_number',
        'frequency',
        'experiment',
    ),
    science.KeyProperties: (
        'time_step',
        'tuning_applied',
        'grid',
        'resolution',
        'additional_detail',
        'extra_conservation_properties',
    ),
    science.SubProcess: (
        'implementation_overview',
        'references',
        'properties',
    ),
    science.ScientificDomain: (
        'meta',
        'simulates',
        'name',
        'id',
        'overview',
        'references',
        'realm',
        'differing_key_properties',
    ),
    designing.NumericalExperiment: (
        'requirements',
        'related_experiments',
    ),
    data.Downscaling: (
        'downscaled_from',
    ),
    drs.DrsTemporalIdentifier: (
        'end',
        'suffix',
        'start',
    ),
    shared.TimesliceList: (
        'members',
        'units',
    ),
    science.Resolution: (
        'typical_x_degrees',
        'name',
        'equivalent_resolution_km',
        'number_of_levels',
        'typical_y_degrees',
        'number_of_xy_gridpoints',
        'is_adaptive_grid',
    ),
    software.ComponentBase: (
        'documentation',
        'repository',
        'development_history',
        'version',
        'name',
        'description',
        'release_date',
        'long_name',
    ),
    drs.DrsEnsembleIdentifier: (
        'realisation_number',
        'initialisation_method_number',
        'perturbation_number',
    ),
    shared.KeyFloat: (
        'key',
        'value',
    ),
    software.DevelopmentPath: (
        'funding_sources',
        'previous_version',
        'consortium_name',
        'developed_in_house',
        'creators',
    ),
    software.SoftwareComponent: (
        'language',
        'connection_points',
        'coupling_framework',
        'license',
        'dependencies',
        'sub_components',
        'grid',
        'composition',
    ),
    platform.StorageVolume: (
        'units',
        'volume',
    ),
    shared.IrregularDateset: (
        'date_set',
    ),
    shared.Pid: (
        'id',
        'resolution_service',
    ),
    activity.EnsembleMember: (
        'ran_on',
        'variant_id',
        'simulation',
        'errata',
        'had_performance',
    ),
    activity.UberEnsemble: (
        'child_ensembles',
    ),
    shared.Party: (
        'organisation',
        'email',
        'meta',
        'name',
        'orcid_id',
        'address',
        'url',
    ),
    science.Algorithm: (
        'implementation_overview',
        'prognostic_variables',
        'diagnostic_variables',
        'references',
        'forced_variables',
    ),
    designing.DomainProperties: (
        'required_extent',
        'required_resolution',
    ),
    platform.ComputePool: (
        'number_of_nodes',
        'compute_cores_per_node',
        'memory_per_node',
        'cpu_type',
        'accelerators_per_node',
        'model_number',
        'accelerator_type',
        'operating_system',
        'name',
        'interconnect',
        'description',
    ),
    shared.TimePeriod: (
        'calendar',
        'date_type',
        'length',
        'units',
        'date',
    ),
    software.Gridspec: (
        'description',
    ),
    shared.OnlineResource: (
        'linkage',
        'protocol',
        'description',
        'name',
    ),
    designing.EnsembleRequirement: (
        'ensemble_member',
        'ensemble_type',
        'minimum_size',
    ),
    platform.Partition: (
        'online_documentation',
        'partition',
        'institution',
        'compute_pools',
        'model_number',
        'storage_pools',
        'when_used',
        'name',
        'vendor',
        'description',
    ),
    designing.NumericalRequirement: (
        'conformance_is_requested',
        'additional_requirements',
    ),
    designing.ForcingConstraint: (
        'group',
        'code',
        'origin',
        'data_link',
        'additional_constraint',
        'forcing_type',
        'category',
    ),
    shared.ExternalDocument: (
        'doi',
        'title',
        'meta',
        'date',
        'name',
        'publication_detail',
        'online_at',
        'authorship',
    ),
    shared.Calendar: (
        'description',
        'standard_name',
        'name',
        'month_lengths',
    ),
    shared.NumberArray: (
        'values',
    ),
    activity.Conformance: (
        'target_requirement',
    ),
    designing.TemporalConstraint: (
        'start_date',
        'start_flexibility',
        'required_calendar',
        'required_duration',
    ),
    shared.DocMetaInfo: (
        'id',
        'source',
        'project',
        'update_date',
        'create_date',
        'drs_keys',
        'institute',
        'type',
        'drs_path',
        'sort_key',
        'type_display_name',
        'type_sort_key',
        'version',
        'external_ids',
        'author',
        'language',
        'source_key',
    ),
    designing.Project: (
        'sub_projects',
        'previous_projects',
        'requires_experiments',
    ),
    data.Dataset: (
        'meta',
        'responsible_parties',
        'availability',
        'name',
        'description',
        'produced_by',
        'related_to_dataset',
        'drs_datasets',
        'references',
    ),
    science.Process: (
        'keywords',
        'properties',
        'algorithms',
        'references',
        'implementation_overview',
        'sub_processes',
    ),
    shared.DateTime: (
        'offset',
        'value',
    ),
    science.Tuning: (
        'description',
        'trend_metrics_used',
        'regional_metrics_used',
        'global_mean_metrics_used',
    ),
    shared.DocReference: (
        'id',
        'relationship',
        'context',
        'constraint_vocabulary',
        'version',
        'type',
    ),
    science.Detail: (
        'content',
        'from_vocab',
        'select',
        'with_cardinality',
        'detail_selection',
    ),
    software.EntryPoint: (
        'name',
    ),
    data.Simulation: (
        'calendar',
        'primary_ensemble',
        'ran_for_experiments',
        'parent_simulation',
        'used',
        'ensemble_identifier',
        'part_of_project',
    ),
    science.Model: (
        'meta',
        'coupled_components',
        'coupler',
        'simulates',
        'id',
        'internal_software_components',
        'category',
        'model_default_properties',
    ),
    activity.EnsembleAxis: (
        'short_identifier',
        'extra_detail',
        'target_requirement',
        'member',
    ),
    activity.AxisMember: (
        'index',
        'description',
        'value',
        'extra_detail',
    ),
    science.Grid: (
        'name',
        'horizontal_grid_layout',
        'vertical_grid_layout',
        'horizontal_grid_type',
        'additional_details',
        'vertical_grid_type',
        'meta',
        'grid_extent',
    ),
    platform.ComponentPerformance: (
        'cores_used',
        'nodes_used',
        'speed',
        'component',
        'component_name',
    ),
    science.Extent: (
        'northern_boundary',
        'eastern_boundary',
        'bottom_vertical_level',
        'western_boundary',
        'southern_boundary',
        'region_known_as',
        'is_global',
        'top_vertical_level',
        'z_units',
    ),
    shared.Cimtext: (
        'content',
        'content_type',
    ),
    platform.Performance: (
        'asypd',
        'memory_bloat',
        'sypd',
        'platform',
        'load_imbalance',
        'name',
        'chsy',
        'total_nodes_used',
        'compiler',
        'meta',
        'subcomponent_performance',
        'coupler_load',
        'model',
        'io_load',
    ),
    activity.ParentSimulation: (
        'branch_time_in_child',
        'parent',
        'branch_time_in_parent',
    ),
}

# Total class properties.
TOTAL_CLASS_PROPERTIES = sum(len(i) for i in CLASS_OWN_PROPERTIES.values())

# ------------------------------------------------
# Enum.
# ------------------------------------------------

# Supported enums.
ENUMS = (
    designing.ForcingTypes,
    science.ModelTypes,
    activity.EnsembleTypes,
    platform.StorageSystems,
    software.ProgrammingLanguage,
    drs.DrsFrequencyTypes,
    shared.PeriodDateTypes,
    designing.EnsembleTypes,
    shared.TimeUnits,
    shared.QualityStatus,
    science.SelectionCardinality,
    data.DataAssociationTypes,
    platform.VolumeUnits,
    shared.RoleCode,
    activity.ForcingTypes,
    shared.TextCode,
    drs.DrsTimeSuffixes,
    designing.ExperimentalRelationships,
    software.CouplingFramework,
    drs.DrsGeographicalOperators,
    shared.CalendarTypes,
    shared.NilReason,
    shared.SlicetimeUnits,
    drs.DrsRealms,
    shared.DocumentTypes,
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
    designing.Project,
    designing.MultiTimeEnsemble,
    designing.SimulationPlan,
    designing.NumericalExperiment,
    designing.ForcingConstraint,
    designing.DomainProperties,
    designing.TemporalConstraint,
    designing.NumericalRequirement,
    designing.EnsembleRequirement,
    designing.OutputTemporalRequirement,
    designing.MultiEnsemble,
    shared.Party,
    shared.ExternalDocument,
    science.ScientificDomain,
    science.Model,
    science.Grid,
    platform.Performance,
    platform.Machine,
    data.Downscaling,
    data.Dataset,
    data.Simulation,
    activity.Ensemble,
    activity.Activity,
    activity.UberEnsemble,
    activity.Conformance,
)

# Base classes.
BASE_CLASSES = defaultdict(tuple)
BASE_CLASSES[drs.DrsAtomicDataset] = (drs.DrsPublicationDataset, )
BASE_CLASSES[designing.SimulationPlan] = (activity.Activity, )
BASE_CLASSES[activity.Ensemble] = (activity.Activity, )
BASE_CLASSES[designing.OutputTemporalRequirement] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[shared.RegularTimeset] = (shared.DatetimeSet, )
BASE_CLASSES[designing.MultiEnsemble] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[platform.Machine] = (platform.Partition, )
BASE_CLASSES[designing.MultiTimeEnsemble] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[science.SubProcess] = (science.ScienceContext, )
BASE_CLASSES[designing.NumericalExperiment] = (activity.Activity, )
BASE_CLASSES[data.Downscaling] = (data.Simulation, activity.Activity, )
BASE_CLASSES[software.SoftwareComponent] = (software.ComponentBase, )
BASE_CLASSES[shared.IrregularDateset] = (shared.DatetimeSet, )
BASE_CLASSES[activity.UberEnsemble] = (activity.Ensemble, activity.Activity, )
BASE_CLASSES[science.Algorithm] = (science.ScienceContext, )
BASE_CLASSES[designing.DomainProperties] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.EnsembleRequirement] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.NumericalRequirement] = (activity.Activity, )
BASE_CLASSES[designing.ForcingConstraint] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[activity.Conformance] = (activity.Activity, )
BASE_CLASSES[designing.TemporalConstraint] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.Project] = (activity.Activity, )
BASE_CLASSES[science.Process] = (science.ScienceContext, )
BASE_CLASSES[shared.DocReference] = (shared.OnlineResource, )
BASE_CLASSES[science.Detail] = (science.ScienceContext, )
BASE_CLASSES[data.Simulation] = (activity.Activity, )
BASE_CLASSES[science.Model] = (software.ComponentBase, )

# Classes with base classes.
BASE_CLASSED = tuple(BASE_CLASSES.keys())

# Sub classes.
SUB_CLASSES = defaultdict(tuple)
SUB_CLASSES[activity.Activity] = (
    activity.Ensemble,
    activity.Conformance,
    data.Simulation,
    designing.Project,
    designing.SimulationPlan,
    designing.NumericalExperiment,
    designing.NumericalRequirement,
    activity.UberEnsemble,
    data.Downscaling,
    designing.MultiTimeEnsemble,
    designing.ForcingConstraint,
    designing.DomainProperties,
    designing.TemporalConstraint,
    designing.EnsembleRequirement,
    designing.OutputTemporalRequirement,
    designing.MultiEnsemble,
    )
SUB_CLASSES[drs.DrsPublicationDataset] = (
    drs.DrsAtomicDataset,
    )
SUB_CLASSES[shared.DatetimeSet] = (
    shared.RegularTimeset,
    shared.IrregularDateset,
    )
SUB_CLASSES[software.ComponentBase] = (
    software.SoftwareComponent,
    science.Model,
    )
SUB_CLASSES[shared.OnlineResource] = (
    shared.DocReference,
    )
SUB_CLASSES[activity.Ensemble] = (
    activity.UberEnsemble,
    )
SUB_CLASSES[platform.Partition] = (
    platform.Machine,
    )
SUB_CLASSES[designing.NumericalRequirement] = (
    designing.MultiTimeEnsemble,
    designing.ForcingConstraint,
    designing.DomainProperties,
    designing.TemporalConstraint,
    designing.EnsembleRequirement,
    designing.OutputTemporalRequirement,
    designing.MultiEnsemble,
    )
SUB_CLASSES[science.ScienceContext] = (
    science.Detail,
    science.Process,
    science.Algorithm,
    science.SubProcess,
    )
SUB_CLASSES[data.Simulation] = (
    data.Downscaling,
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

        ('rationale', 'type', unicode),
        ('description', 'type', unicode),
        ('responsible_parties', 'type', shared.Responsibility),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('keywords', 'type', unicode),
        ('duration', 'type', shared.TimePeriod),
        ('name', 'type', unicode),

        ('rationale', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('keywords', 'cardinality', "0.N"),
        ('duration', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    drs.DrsAtomicDataset: (

        ('product', 'type', unicode),
        ('realm', 'type', unicode),
        ('experiment', 'type', unicode),
        ('institute', 'type', unicode),
        ('geographical_constraint', 'type', drs.DrsGeographicalIndicator),
        ('version_number', 'type', int),
        ('mip_table', 'type', unicode),
        ('variable_name', 'type', unicode),
        ('frequency', 'type', unicode),
        ('activity', 'type', unicode),
        ('ensemble_member', 'type', drs.DrsEnsembleIdentifier),
        ('model', 'type', unicode),
        ('temporal_constraint', 'type', drs.DrsTemporalIdentifier),

        ('version_number', 'cardinality', "1.1"),
        ('realm', 'cardinality', "1.1"),
        ('experiment', 'cardinality', "1.1"),
        ('institute', 'cardinality', "1.1"),
        ('geographical_constraint', 'cardinality', "0.1"),
        ('product', 'cardinality', "1.1"),
        ('mip_table', 'cardinality', "1.1"),
        ('variable_name', 'cardinality', "1.1"),
        ('frequency', 'cardinality', "1.1"),
        ('activity', 'cardinality', "1.1"),
        ('ensemble_member', 'cardinality', "1.1"),
        ('model', 'cardinality', "1.1"),
        ('temporal_constraint', 'cardinality', "0.1"),

    ),
    software.Composition: (

        ('couplings', 'type', unicode),
        ('description', 'type', unicode),

        ('couplings', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),

    ),
    drs.DrsGeographicalIndicator: (

        ('operator', 'type', unicode),
        ('bounding_box', 'type', unicode),
        ('spatial_domain', 'type', unicode),

        ('operator', 'cardinality', "0.1"),
        ('bounding_box', 'cardinality', "0.1"),
        ('spatial_domain', 'cardinality', "0.1"),

    ),
    designing.SimulationPlan: (

        ('description', 'type', unicode),
        ('duration', 'type', shared.TimePeriod),
        ('expected_performance_sypd', 'type', float),
        ('expected_model', 'type', science.Model),
        ('responsible_parties', 'type', shared.Responsibility),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('rationale', 'type', unicode),
        ('keywords', 'type', unicode),
        ('expected_platform', 'type', platform.Machine),
        ('will_support_experiments', 'type', designing.NumericalExperiment),
        ('name', 'type', unicode),

        ('expected_performance_sypd', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.N"),
        ('expected_model', 'cardinality', "1.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('rationale', 'cardinality', "0.1"),
        ('duration', 'cardinality', "1.1"),
        ('expected_platform', 'cardinality', "0.1"),
        ('will_support_experiments', 'cardinality', "1.N"),
        ('name', 'cardinality', "1.1"),

    ),
    activity.Ensemble: (

        ('part_of', 'type', activity.UberEnsemble),
        ('common_conformances', 'type', activity.Conformance),
        ('description', 'type', unicode),
        ('supported', 'type', designing.NumericalExperiment),
        ('duration', 'type', shared.TimePeriod),
        ('documentation', 'type', shared.OnlineResource),
        ('responsible_parties', 'type', shared.Responsibility),
        ('members', 'type', activity.EnsembleMember),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('rationale', 'type', unicode),
        ('keywords', 'type', unicode),
        ('has_ensemble_axes', 'type', activity.EnsembleAxis),
        ('name', 'type', unicode),

        ('part_of', 'cardinality', "0.N"),
        ('common_conformances', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('supported', 'cardinality', "1.N"),
        ('documentation', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('members', 'cardinality', "1.N"),
        ('keywords', 'cardinality', "0.0"),
        ('canonical_name', 'cardinality', "0.0"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('rationale', 'cardinality', "0.0"),
        ('duration', 'cardinality', "0.0"),
        ('has_ensemble_axes', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    science.ScienceContext: (

        ('id', 'type', unicode),
        ('context', 'type', unicode),
        ('name', 'type', unicode),

        ('id', 'cardinality', "1.1"),
        ('context', 'cardinality', "1.1"),
        ('name', 'cardinality', "1.1"),

    ),
    shared.QualityReview: (

        ('date', 'type', unicode),
        ('metadata_reviewer', 'type', shared.Party),
        ('quality_status', 'type', unicode),
        ('quality_description', 'type', unicode),

        ('date', 'cardinality', "1.1"),
        ('metadata_reviewer', 'cardinality', "1.1"),
        ('quality_status', 'cardinality', "0.1"),
        ('quality_description', 'cardinality', "1.1"),

    ),
    shared.DatetimeSet: (

        ('length', 'type', int),

        ('length', 'cardinality', "1.1"),

    ),
    designing.OutputTemporalRequirement: (

        ('throughout', 'type', bool),
        ('description', 'type', unicode),
        ('continuous_subset', 'type', shared.TimePeriod),
        ('keywords', 'type', unicode),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('responsible_parties', 'type', shared.Responsibility),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('sliced_subset', 'type', shared.TimesliceList),
        ('rationale', 'type', unicode),
        ('duration', 'type', shared.TimePeriod),
        ('conformance_is_requested', 'type', bool),
        ('name', 'type', unicode),

        ('throughout', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.0"),
        ('continuous_subset', 'cardinality', "0.N"),
        ('additional_requirements', 'cardinality', "0.0"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('sliced_subset', 'cardinality', "0.1"),
        ('rationale', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.N"),
        ('conformance_is_requested', 'cardinality', "1.1"),
        ('name', 'cardinality', "1.1"),

    ),
    science.ConservationProperties: (

        ('corrected_conserved_prognostic_variables', 'type', data.VariableCollection),
        ('flux_correction_was_used', 'type', bool),
        ('correction_methodology', 'type', unicode),

        ('corrected_conserved_prognostic_variables', 'cardinality', "0.1"),
        ('flux_correction_was_used', 'cardinality', "1.1"),
        ('correction_methodology', 'cardinality', "0.1"),

    ),
    shared.RegularTimeset: (

        ('length', 'type', int),
        ('start_date', 'type', shared.DateTime),
        ('increment', 'type', shared.TimePeriod),

        ('length', 'cardinality', "1.1"),
        ('start_date', 'cardinality', "1.1"),
        ('increment', 'cardinality', "1.1"),

    ),
    software.Variable: (

        ('name', 'type', unicode),
        ('prognostic', 'type', bool),
        ('description', 'type', unicode),

        ('name', 'cardinality', "1.1"),
        ('prognostic', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),

    ),
    shared.Reference: (

        ('document', 'type', shared.ExternalDocument),
        ('context', 'type', unicode),

        ('document', 'cardinality', "1.1"),
        ('context', 'cardinality', "0.1"),

    ),
    designing.MultiEnsemble: (

        ('ensemble_axis', 'type', designing.EnsembleRequirement),
        ('description', 'type', unicode),
        ('keywords', 'type', unicode),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('responsible_parties', 'type', shared.Responsibility),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('rationale', 'type', unicode),
        ('duration', 'type', shared.TimePeriod),
        ('conformance_is_requested', 'type', bool),
        ('name', 'type', unicode),

        ('ensemble_axis', 'cardinality', "1.N"),
        ('description', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.0"),
        ('additional_requirements', 'cardinality', "0.0"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('rationale', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.N"),
        ('conformance_is_requested', 'cardinality', "1.1"),
        ('name', 'cardinality', "1.1"),

    ),
    shared.Responsibility: (

        ('party', 'type', shared.Party),
        ('when', 'type', shared.TimePeriod),
        ('role', 'type', unicode),

        ('party', 'cardinality', "1.N"),
        ('when', 'cardinality', "0.1"),
        ('role', 'cardinality', "1.1"),

    ),
    data.VariableCollection: (

        ('collection_name', 'type', unicode),
        ('variables', 'type', unicode),

        ('collection_name', 'cardinality', "0.1"),
        ('variables', 'cardinality', "1.N"),

    ),
    platform.StoragePool: (

        ('type', 'type', unicode),
        ('volume_available', 'type', platform.StorageVolume),
        ('vendor', 'type', shared.Party),
        ('description', 'type', unicode),
        ('name', 'type', unicode),

        ('type', 'cardinality', "0.1"),
        ('volume_available', 'cardinality', "1.1"),
        ('vendor', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    platform.Machine: (

        ('vendor', 'type', shared.Party),
        ('name', 'type', unicode),
        ('partition', 'type', platform.Partition),
        ('model_number', 'type', unicode),
        ('online_documentation', 'type', shared.OnlineResource),
        ('meta', 'type', shared.DocMetaInfo),
        ('storage_pools', 'type', platform.StoragePool),
        ('when_used', 'type', shared.TimePeriod),
        ('institution', 'type', shared.Party),
        ('compute_pools', 'type', platform.ComputePool),
        ('description', 'type', unicode),

        ('vendor', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('partition', 'cardinality', "0.N"),
        ('model_number', 'cardinality', "0.1"),
        ('online_documentation', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('storage_pools', 'cardinality', "0.N"),
        ('when_used', 'cardinality', "0.1"),
        ('institution', 'cardinality', "1.1"),
        ('compute_pools', 'cardinality', "1.N"),
        ('description', 'cardinality', "0.1"),

    ),
    designing.MultiTimeEnsemble: (

        ('ensemble_members', 'type', shared.DatetimeSet),
        ('description', 'type', unicode),
        ('keywords', 'type', unicode),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('responsible_parties', 'type', shared.Responsibility),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('rationale', 'type', unicode),
        ('duration', 'type', shared.TimePeriod),
        ('conformance_is_requested', 'type', bool),
        ('name', 'type', unicode),

        ('ensemble_members', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.0"),
        ('additional_requirements', 'cardinality', "0.0"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('rationale', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.N"),
        ('conformance_is_requested', 'cardinality', "1.1"),
        ('name', 'cardinality', "1.1"),

    ),
    drs.DrsPublicationDataset: (

        ('product', 'type', unicode),
        ('realm', 'type', unicode),
        ('institute', 'type', unicode),
        ('version_number', 'type', int),
        ('experiment', 'type', unicode),
        ('frequency', 'type', unicode),
        ('activity', 'type', unicode),
        ('model', 'type', unicode),

        ('product', 'cardinality', "1.1"),
        ('realm', 'cardinality', "0.1"),
        ('institute', 'cardinality', "1.1"),
        ('version_number', 'cardinality', "0.1"),
        ('experiment', 'cardinality', "1.1"),
        ('frequency', 'cardinality', "0.1"),
        ('activity', 'cardinality', "1.1"),
        ('model', 'cardinality', "1.1"),

    ),
    science.KeyProperties: (

        ('extra_conservation_properties', 'type', science.ConservationProperties),
        ('additional_detail', 'type', science.Detail),
        ('grid', 'type', science.Grid),
        ('tuning_applied', 'type', science.Tuning),
        ('time_step', 'type', float),
        ('resolution', 'type', science.Resolution),

        ('extra_conservation_properties', 'cardinality', "0.1"),
        ('additional_detail', 'cardinality', "0.N"),
        ('grid', 'cardinality', "1.1"),
        ('tuning_applied', 'cardinality', "0.1"),
        ('time_step', 'cardinality', "1.1"),
        ('resolution', 'cardinality', "1.1"),

    ),
    science.SubProcess: (

        ('name', 'type', unicode),
        ('id', 'type', unicode),
        ('references', 'type', shared.Reference),
        ('context', 'type', unicode),
        ('implementation_overview', 'type', unicode),
        ('properties', 'type', science.Detail),

        ('name', 'cardinality', "1.1"),
        ('id', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('context', 'cardinality', "1.1"),
        ('implementation_overview', 'cardinality', "1.1"),
        ('properties', 'cardinality', "0.N"),

    ),
    science.ScientificDomain: (

        ('simulates', 'type', science.Process),
        ('realm', 'type', unicode),
        ('name', 'type', unicode),
        ('overview', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('differing_key_properties', 'type', science.KeyProperties),
        ('id', 'type', unicode),

        ('simulates', 'cardinality', "1.N"),
        ('realm', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('overview', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('differing_key_properties', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),

    ),
    designing.NumericalExperiment: (

        ('requirements', 'type', designing.NumericalRequirement),
        ('description', 'type', unicode),
        ('duration', 'type', shared.TimePeriod),
        ('responsible_parties', 'type', shared.Responsibility),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('rationale', 'type', unicode),
        ('related_experiments', 'type', designing.NumericalExperiment),
        ('keywords', 'type', unicode),
        ('name', 'type', unicode),

        ('requirements', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('rationale', 'cardinality', "1.1"),
        ('related_experiments', 'cardinality', "0.N"),
        ('duration', 'cardinality', "0.0"),
        ('name', 'cardinality', "1.1"),

    ),
    data.Downscaling: (

        ('ensemble_identifier', 'type', unicode),
        ('used', 'type', science.Model),
        ('description', 'type', unicode),
        ('part_of_project', 'type', designing.Project),
        ('parent_simulation', 'type', activity.ParentSimulation),
        ('primary_ensemble', 'type', activity.Ensemble),
        ('downscaled_from', 'type', data.Simulation),
        ('responsible_parties', 'type', shared.Responsibility),
        ('keywords', 'type', unicode),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('ran_for_experiments', 'type', designing.NumericalExperiment),
        ('rationale', 'type', unicode),
        ('duration', 'type', shared.TimePeriod),
        ('calendar', 'type', shared.Calendar),
        ('name', 'type', unicode),

        ('ensemble_identifier', 'cardinality', "1.1"),
        ('used', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('part_of_project', 'cardinality', "1.N"),
        ('parent_simulation', 'cardinality', "0.0"),
        ('primary_ensemble', 'cardinality', "0.1"),
        ('downscaled_from', 'cardinality', "1.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('keywords', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('ran_for_experiments', 'cardinality', "1.N"),
        ('rationale', 'cardinality', "0.0"),
        ('duration', 'cardinality', "0.1"),
        ('calendar', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    drs.DrsTemporalIdentifier: (

        ('start', 'type', unicode),
        ('end', 'type', unicode),
        ('suffix', 'type', unicode),

        ('start', 'cardinality', "1.1"),
        ('end', 'cardinality', "0.1"),
        ('suffix', 'cardinality', "0.1"),

    ),
    shared.TimesliceList: (

        ('units', 'type', unicode),
        ('members', 'type', shared.NumberArray),

        ('units', 'cardinality', "1.1"),
        ('members', 'cardinality', "1.1"),

    ),
    science.Resolution: (

        ('number_of_levels', 'type', int),
        ('name', 'type', unicode),
        ('equivalent_resolution_km', 'type', float),
        ('typical_y_degrees', 'type', float),
        ('number_of_xy_gridpoints', 'type', int),
        ('is_adaptive_grid', 'type', bool),
        ('typical_x_degrees', 'type', float),

        ('number_of_levels', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('equivalent_resolution_km', 'cardinality', "0.1"),
        ('typical_y_degrees', 'cardinality', "0.1"),
        ('number_of_xy_gridpoints', 'cardinality', "0.1"),
        ('is_adaptive_grid', 'cardinality', "0.1"),
        ('typical_x_degrees', 'cardinality', "0.1"),

    ),
    software.ComponentBase: (

        ('description', 'type', unicode),
        ('repository', 'type', shared.OnlineResource),
        ('release_date', 'type', datetime.datetime),
        ('documentation', 'type', shared.Reference),
        ('development_history', 'type', software.DevelopmentPath),
        ('long_name', 'type', unicode),
        ('version', 'type', unicode),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('repository', 'cardinality', "0.1"),
        ('release_date', 'cardinality', "0.1"),
        ('documentation', 'cardinality', "0.N"),
        ('development_history', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('version', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    drs.DrsEnsembleIdentifier: (

        ('perturbation_number', 'type', int),
        ('initialisation_method_number', 'type', int),
        ('realisation_number', 'type', int),

        ('perturbation_number', 'cardinality', "1.1"),
        ('initialisation_method_number', 'cardinality', "1.1"),
        ('realisation_number', 'cardinality', "1.1"),

    ),
    shared.KeyFloat: (

        ('value', 'type', float),
        ('key', 'type', unicode),

        ('value', 'cardinality', "1.1"),
        ('key', 'cardinality', "1.1"),

    ),
    software.DevelopmentPath: (

        ('funding_sources', 'type', shared.Responsibility),
        ('consortium_name', 'type', unicode),
        ('creators', 'type', shared.Responsibility),
        ('developed_in_house', 'type', bool),
        ('previous_version', 'type', unicode),

        ('funding_sources', 'cardinality', "0.N"),
        ('consortium_name', 'cardinality', "0.1"),
        ('creators', 'cardinality', "0.N"),
        ('developed_in_house', 'cardinality', "1.1"),
        ('previous_version', 'cardinality', "0.1"),

    ),
    software.SoftwareComponent: (

        ('license', 'type', unicode),
        ('coupling_framework', 'type', unicode),
        ('description', 'type', unicode),
        ('repository', 'type', shared.OnlineResource),
        ('language', 'type', unicode),
        ('release_date', 'type', datetime.datetime),
        ('documentation', 'type', shared.Reference),
        ('development_history', 'type', software.DevelopmentPath),
        ('sub_components', 'type', software.SoftwareComponent),
        ('long_name', 'type', unicode),
        ('version', 'type', unicode),
        ('grid', 'type', software.Gridspec),
        ('dependencies', 'type', software.EntryPoint),
        ('composition', 'type', software.Composition),
        ('connection_points', 'type', software.Variable),
        ('name', 'type', unicode),

        ('license', 'cardinality', "0.1"),
        ('coupling_framework', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('repository', 'cardinality', "0.1"),
        ('language', 'cardinality', "0.1"),
        ('release_date', 'cardinality', "0.1"),
        ('documentation', 'cardinality', "0.N"),
        ('development_history', 'cardinality', "0.1"),
        ('sub_components', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('version', 'cardinality', "0.1"),
        ('grid', 'cardinality', "0.1"),
        ('dependencies', 'cardinality', "0.N"),
        ('composition', 'cardinality', "0.1"),
        ('connection_points', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    platform.StorageVolume: (

        ('units', 'type', unicode),
        ('volume', 'type', int),

        ('units', 'cardinality', "1.1"),
        ('volume', 'cardinality', "1.1"),

    ),
    shared.IrregularDateset: (

        ('length', 'type', int),
        ('date_set', 'type', unicode),

        ('length', 'cardinality', "1.1"),
        ('date_set', 'cardinality', "1.1"),

    ),
    shared.Pid: (

        ('resolution_service', 'type', shared.OnlineResource),
        ('id', 'type', unicode),

        ('resolution_service', 'cardinality', "1.1"),
        ('id', 'cardinality', "1.1"),

    ),
    activity.EnsembleMember: (

        ('variant_id', 'type', unicode),
        ('simulation', 'type', data.Simulation),
        ('errata', 'type', shared.OnlineResource),
        ('had_performance', 'type', platform.Performance),
        ('ran_on', 'type', platform.Machine),

        ('variant_id', 'cardinality', "1.1"),
        ('simulation', 'cardinality', "1.1"),
        ('errata', 'cardinality', "0.1"),
        ('had_performance', 'cardinality', "0.1"),
        ('ran_on', 'cardinality', "0.1"),

    ),
    activity.UberEnsemble: (

        ('child_ensembles', 'type', activity.Ensemble),
        ('part_of', 'type', activity.UberEnsemble),
        ('common_conformances', 'type', activity.Conformance),
        ('description', 'type', unicode),
        ('name', 'type', unicode),
        ('rationale', 'type', unicode),
        ('supported', 'type', designing.NumericalExperiment),
        ('responsible_parties', 'type', shared.Responsibility),
        ('keywords', 'type', unicode),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('members', 'type', activity.EnsembleMember),
        ('duration', 'type', shared.TimePeriod),
        ('has_ensemble_axes', 'type', activity.EnsembleAxis),
        ('documentation', 'type', shared.OnlineResource),

        ('child_ensembles', 'cardinality', "1.N"),
        ('part_of', 'cardinality', "0.N"),
        ('common_conformances', 'cardinality', "0.0"),
        ('description', 'cardinality', "0.1"),
        ('rationale', 'cardinality', "0.0"),
        ('supported', 'cardinality', "1.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.0"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('members', 'cardinality', "0.0"),
        ('keywords', 'cardinality', "0.0"),
        ('has_ensemble_axes', 'cardinality', "1.N"),
        ('duration', 'cardinality', "0.0"),
        ('documentation', 'cardinality', "0.N"),

    ),
    shared.Party: (

        ('name', 'type', unicode),
        ('url', 'type', shared.OnlineResource),
        ('organisation', 'type', bool),
        ('meta', 'type', shared.DocMetaInfo),
        ('address', 'type', unicode),
        ('email', 'type', unicode),
        ('orcid_id', 'type', unicode),

        ('name', 'cardinality', "0.1"),
        ('url', 'cardinality', "0.1"),
        ('organisation', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('address', 'cardinality', "0.1"),
        ('email', 'cardinality', "0.1"),
        ('orcid_id', 'cardinality', "0.1"),

    ),
    science.Algorithm: (

        ('name', 'type', unicode),
        ('diagnostic_variables', 'type', data.VariableCollection),
        ('prognostic_variables', 'type', data.VariableCollection),
        ('references', 'type', shared.Reference),
        ('context', 'type', unicode),
        ('implementation_overview', 'type', unicode),
        ('forced_variables', 'type', data.VariableCollection),
        ('id', 'type', unicode),

        ('name', 'cardinality', "1.1"),
        ('diagnostic_variables', 'cardinality', "0.1"),
        ('prognostic_variables', 'cardinality', "0.1"),
        ('references', 'cardinality', "0.N"),
        ('context', 'cardinality', "1.1"),
        ('implementation_overview', 'cardinality', "1.1"),
        ('forced_variables', 'cardinality', "0.1"),
        ('id', 'cardinality', "1.1"),

    ),
    designing.DomainProperties: (

        ('required_resolution', 'type', science.Resolution),
        ('description', 'type', unicode),
        ('keywords', 'type', unicode),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('responsible_parties', 'type', shared.Responsibility),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('required_extent', 'type', science.Extent),
        ('rationale', 'type', unicode),
        ('duration', 'type', shared.TimePeriod),
        ('conformance_is_requested', 'type', bool),
        ('name', 'type', unicode),

        ('required_resolution', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.0"),
        ('additional_requirements', 'cardinality', "0.0"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('required_extent', 'cardinality', "0.1"),
        ('rationale', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.N"),
        ('conformance_is_requested', 'cardinality', "1.1"),
        ('name', 'cardinality', "1.1"),

    ),
    platform.ComputePool: (

        ('operating_system', 'type', unicode),
        ('interconnect', 'type', unicode),
        ('name', 'type', unicode),
        ('memory_per_node', 'type', platform.StorageVolume),
        ('model_number', 'type', unicode),
        ('compute_cores_per_node', 'type', int),
        ('accelerator_type', 'type', unicode),
        ('cpu_type', 'type', unicode),
        ('number_of_nodes', 'type', int),
        ('accelerators_per_node', 'type', int),
        ('description', 'type', unicode),

        ('operating_system', 'cardinality', "0.1"),
        ('interconnect', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),
        ('memory_per_node', 'cardinality', "0.1"),
        ('model_number', 'cardinality', "0.1"),
        ('compute_cores_per_node', 'cardinality', "0.1"),
        ('accelerator_type', 'cardinality', "0.1"),
        ('cpu_type', 'cardinality', "0.1"),
        ('number_of_nodes', 'cardinality', "0.1"),
        ('accelerators_per_node', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),

    ),
    shared.TimePeriod: (

        ('date', 'type', shared.DateTime),
        ('units', 'type', unicode),
        ('calendar', 'type', shared.Calendar),
        ('length', 'type', int),
        ('date_type', 'type', unicode),

        ('date', 'cardinality', "0.1"),
        ('units', 'cardinality', "1.1"),
        ('calendar', 'cardinality', "0.1"),
        ('length', 'cardinality', "1.1"),
        ('date_type', 'cardinality', "1.1"),

    ),
    software.Gridspec: (

        ('description', 'type', unicode),

        ('description', 'cardinality', "1.1"),

    ),
    shared.OnlineResource: (

        ('protocol', 'type', unicode),
        ('name', 'type', unicode),
        ('linkage', 'type', unicode),
        ('description', 'type', unicode),

        ('protocol', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('linkage', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),

    ),
    designing.EnsembleRequirement: (

        ('minimum_size', 'type', int),
        ('description', 'type', unicode),
        ('keywords', 'type', unicode),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('responsible_parties', 'type', shared.Responsibility),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('ensemble_type', 'type', unicode),
        ('rationale', 'type', unicode),
        ('duration', 'type', shared.TimePeriod),
        ('ensemble_member', 'type', designing.NumericalRequirement),
        ('conformance_is_requested', 'type', bool),
        ('name', 'type', unicode),

        ('minimum_size', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.0"),
        ('additional_requirements', 'cardinality', "0.0"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('ensemble_type', 'cardinality', "1.1"),
        ('rationale', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.N"),
        ('ensemble_member', 'cardinality', "0.N"),
        ('conformance_is_requested', 'cardinality', "1.1"),
        ('name', 'cardinality', "1.1"),

    ),
    platform.Partition: (

        ('vendor', 'type', shared.Party),
        ('name', 'type', unicode),
        ('partition', 'type', platform.Partition),
        ('model_number', 'type', unicode),
        ('online_documentation', 'type', shared.OnlineResource),
        ('storage_pools', 'type', platform.StoragePool),
        ('when_used', 'type', shared.TimePeriod),
        ('institution', 'type', shared.Party),
        ('compute_pools', 'type', platform.ComputePool),
        ('description', 'type', unicode),

        ('vendor', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('partition', 'cardinality', "0.N"),
        ('model_number', 'cardinality', "0.1"),
        ('online_documentation', 'cardinality', "0.N"),
        ('storage_pools', 'cardinality', "0.N"),
        ('when_used', 'cardinality', "0.1"),
        ('institution', 'cardinality', "1.1"),
        ('compute_pools', 'cardinality', "1.N"),
        ('description', 'cardinality', "0.1"),

    ),
    designing.NumericalRequirement: (

        ('description', 'type', unicode),
        ('duration', 'type', shared.TimePeriod),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('responsible_parties', 'type', shared.Responsibility),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('rationale', 'type', unicode),
        ('keywords', 'type', unicode),
        ('conformance_is_requested', 'type', bool),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.N"),
        ('additional_requirements', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('rationale', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.0"),
        ('conformance_is_requested', 'cardinality', "1.1"),
        ('name', 'cardinality', "1.1"),

    ),
    designing.ForcingConstraint: (

        ('category', 'type', unicode),
        ('origin', 'type', shared.Reference),
        ('code', 'type', unicode),
        ('group', 'type', unicode),
        ('description', 'type', unicode),
        ('data_link', 'type', shared.OnlineResource),
        ('keywords', 'type', unicode),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('responsible_parties', 'type', shared.Responsibility),
        ('forcing_type', 'type', unicode),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('rationale', 'type', unicode),
        ('duration', 'type', shared.TimePeriod),
        ('conformance_is_requested', 'type', bool),
        ('additional_constraint', 'type', unicode),
        ('name', 'type', unicode),

        ('category', 'cardinality', "0.1"),
        ('origin', 'cardinality', "0.1"),
        ('code', 'cardinality', "0.1"),
        ('group', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.0"),
        ('additional_requirements', 'cardinality', "0.0"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('forcing_type', 'cardinality', "1.1"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('rationale', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.N"),
        ('additional_constraint', 'cardinality', "0.1"),
        ('conformance_is_requested', 'cardinality', "1.1"),
        ('data_link', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    shared.ExternalDocument: (

        ('doi', 'type', unicode),
        ('name', 'type', unicode),
        ('title', 'type', unicode),
        ('publication_detail', 'type', unicode),
        ('online_at', 'type', shared.OnlineResource),
        ('meta', 'type', shared.DocMetaInfo),
        ('date', 'type', unicode),
        ('authorship', 'type', unicode),

        ('doi', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('title', 'cardinality', "1.1"),
        ('publication_detail', 'cardinality', "0.1"),
        ('online_at', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('date', 'cardinality', "0.1"),
        ('authorship', 'cardinality', "0.1"),

    ),
    shared.Calendar: (

        ('standard_name', 'type', unicode),
        ('description', 'type', unicode),
        ('name', 'type', unicode),
        ('month_lengths', 'type', int),

        ('standard_name', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),
        ('month_lengths', 'cardinality', "0.N"),

    ),
    shared.NumberArray: (

        ('values', 'type', unicode),

        ('values', 'cardinality', "1.1"),

    ),
    activity.Conformance: (

        ('description', 'type', unicode),
        ('duration', 'type', shared.TimePeriod),
        ('responsible_parties', 'type', shared.Responsibility),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('rationale', 'type', unicode),
        ('keywords', 'type', unicode),
        ('target_requirement', 'type', designing.NumericalRequirement),
        ('name', 'type', unicode),

        ('description', 'cardinality', "1.1"),
        ('long_name', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('duration', 'cardinality', "0.0"),
        ('canonical_name', 'cardinality', "0.0"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('rationale', 'cardinality', "0.0"),
        ('keywords', 'cardinality', "0.0"),
        ('target_requirement', 'cardinality', "1.1"),
        ('name', 'cardinality', "1.1"),

    ),
    designing.TemporalConstraint: (

        ('required_duration', 'type', shared.TimePeriod),
        ('description', 'type', unicode),
        ('keywords', 'type', unicode),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('responsible_parties', 'type', shared.Responsibility),
        ('start_date', 'type', shared.DateTime),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('rationale', 'type', unicode),
        ('start_flexibility', 'type', shared.TimePeriod),
        ('duration', 'type', shared.TimePeriod),
        ('conformance_is_requested', 'type', bool),
        ('required_calendar', 'type', shared.Calendar),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.0"),
        ('required_duration', 'cardinality', "0.1"),
        ('additional_requirements', 'cardinality', "0.0"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('start_date', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('rationale', 'cardinality', "0.1"),
        ('start_flexibility', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.N"),
        ('conformance_is_requested', 'cardinality', "1.1"),
        ('required_calendar', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    shared.DocMetaInfo: (

        ('drs_keys', 'type', unicode),
        ('drs_path', 'type', unicode),
        ('create_date', 'type', datetime.datetime),
        ('language', 'type', unicode),
        ('update_date', 'type', datetime.datetime),
        ('sort_key', 'type', unicode),
        ('author', 'type', shared.Party),
        ('source_key', 'type', unicode),
        ('project', 'type', unicode),
        ('source', 'type', unicode),
        ('version', 'type', int),
        ('type_sort_key', 'type', unicode),
        ('external_ids', 'type', unicode),
        ('type', 'type', unicode),
        ('id', 'type', unicode),
        ('type_display_name', 'type', unicode),
        ('institute', 'type', unicode),

        ('drs_keys', 'cardinality', "0.N"),
        ('drs_path', 'cardinality', "0.1"),
        ('create_date', 'cardinality', "1.1"),
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

    ),
    designing.Project: (

        ('requires_experiments', 'type', designing.NumericalExperiment),
        ('description', 'type', unicode),
        ('duration', 'type', shared.TimePeriod),
        ('previous_projects', 'type', designing.Project),
        ('responsible_parties', 'type', shared.Responsibility),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('rationale', 'type', unicode),
        ('keywords', 'type', unicode),
        ('sub_projects', 'type', designing.Project),
        ('name', 'type', unicode),

        ('requires_experiments', 'cardinality', "0.N"),
        ('description', 'cardinality', "1.1"),
        ('duration', 'cardinality', "0.1"),
        ('previous_projects', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('rationale', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.N"),
        ('sub_projects', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    data.Dataset: (

        ('related_to_dataset', 'type', shared.OnlineResource),
        ('description', 'type', unicode),
        ('produced_by', 'type', data.Simulation),
        ('drs_datasets', 'type', drs.DrsPublicationDataset),
        ('responsible_parties', 'type', shared.Responsibility),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('availability', 'type', shared.OnlineResource),
        ('name', 'type', unicode),

        ('related_to_dataset', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('produced_by', 'cardinality', "0.1"),
        ('drs_datasets', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('availability', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    science.Process: (

        ('name', 'type', unicode),
        ('sub_processes', 'type', science.SubProcess),
        ('properties', 'type', science.Detail),
        ('references', 'type', shared.Reference),
        ('context', 'type', unicode),
        ('implementation_overview', 'type', unicode),
        ('keywords', 'type', unicode),
        ('algorithms', 'type', science.Algorithm),
        ('id', 'type', unicode),

        ('name', 'cardinality', "1.1"),
        ('sub_processes', 'cardinality', "0.N"),
        ('properties', 'cardinality', "0.N"),
        ('references', 'cardinality', "0.N"),
        ('context', 'cardinality', "1.1"),
        ('implementation_overview', 'cardinality', "1.1"),
        ('keywords', 'cardinality', "0.1"),
        ('algorithms', 'cardinality', "0.N"),
        ('id', 'cardinality', "1.1"),

    ),
    shared.DateTime: (

        ('value', 'type', unicode),
        ('offset', 'type', bool),

        ('value', 'cardinality', "1.1"),
        ('offset', 'cardinality', "0.1"),

    ),
    science.Tuning: (

        ('regional_metrics_used', 'type', data.VariableCollection),
        ('trend_metrics_used', 'type', data.VariableCollection),
        ('description', 'type', unicode),
        ('global_mean_metrics_used', 'type', data.VariableCollection),

        ('regional_metrics_used', 'cardinality', "0.1"),
        ('trend_metrics_used', 'cardinality', "0.1"),
        ('description', 'cardinality', "1.1"),
        ('global_mean_metrics_used', 'cardinality', "0.1"),

    ),
    shared.DocReference: (

        ('constraint_vocabulary', 'type', unicode),
        ('protocol', 'type', unicode),
        ('name', 'type', unicode),
        ('relationship', 'type', unicode),
        ('version', 'type', int),
        ('context', 'type', unicode),
        ('type', 'type', unicode),
        ('id', 'type', unicode),
        ('linkage', 'type', unicode),
        ('description', 'type', unicode),

        ('constraint_vocabulary', 'cardinality', "0.1"),
        ('protocol', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('relationship', 'cardinality', "0.1"),
        ('version', 'cardinality', "0.1"),
        ('context', 'cardinality', "0.1"),
        ('type', 'cardinality', "1.1"),
        ('id', 'cardinality', "0.1"),
        ('linkage', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),

    ),
    science.Detail: (

        ('with_cardinality', 'type', unicode),
        ('from_vocab', 'type', unicode),
        ('content', 'type', unicode),
        ('detail_selection', 'type', unicode),
        ('context', 'type', unicode),
        ('id', 'type', unicode),
        ('select', 'type', unicode),
        ('name', 'type', unicode),

        ('with_cardinality', 'cardinality', "0.1"),
        ('from_vocab', 'cardinality', "0.1"),
        ('content', 'cardinality', "0.1"),
        ('detail_selection', 'cardinality', "0.N"),
        ('context', 'cardinality', "1.1"),
        ('id', 'cardinality', "1.1"),
        ('select', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    software.EntryPoint: (

        ('name', 'type', unicode),

        ('name', 'cardinality', "0.1"),

    ),
    data.Simulation: (

        ('ensemble_identifier', 'type', unicode),
        ('used', 'type', science.Model),
        ('description', 'type', unicode),
        ('part_of_project', 'type', designing.Project),
        ('duration', 'type', shared.TimePeriod),
        ('parent_simulation', 'type', activity.ParentSimulation),
        ('primary_ensemble', 'type', activity.Ensemble),
        ('responsible_parties', 'type', shared.Responsibility),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('ran_for_experiments', 'type', designing.NumericalExperiment),
        ('rationale', 'type', unicode),
        ('keywords', 'type', unicode),
        ('calendar', 'type', shared.Calendar),
        ('name', 'type', unicode),

        ('ensemble_identifier', 'cardinality', "1.1"),
        ('used', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('part_of_project', 'cardinality', "1.N"),
        ('duration', 'cardinality', "0.1"),
        ('parent_simulation', 'cardinality', "0.1"),
        ('primary_ensemble', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('ran_for_experiments', 'cardinality', "1.N"),
        ('rationale', 'cardinality', "0.0"),
        ('keywords', 'cardinality', "0.N"),
        ('calendar', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    science.Model: (

        ('simulates', 'type', science.ScientificDomain),
        ('category', 'type', unicode),
        ('model_default_properties', 'type', science.KeyProperties),
        ('description', 'type', unicode),
        ('repository', 'type', shared.OnlineResource),
        ('coupler', 'type', unicode),
        ('coupled_components', 'type', science.Model),
        ('release_date', 'type', datetime.datetime),
        ('documentation', 'type', shared.Reference),
        ('internal_software_components', 'type', software.SoftwareComponent),
        ('development_history', 'type', software.DevelopmentPath),
        ('long_name', 'type', unicode),
        ('version', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('id', 'type', unicode),
        ('name', 'type', unicode),

        ('simulates', 'cardinality', "0.N"),
        ('category', 'cardinality', "1.1"),
        ('model_default_properties', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('repository', 'cardinality', "0.1"),
        ('coupler', 'cardinality', "0.1"),
        ('coupled_components', 'cardinality', "0.N"),
        ('release_date', 'cardinality', "0.1"),
        ('documentation', 'cardinality', "0.N"),
        ('internal_software_components', 'cardinality', "0.N"),
        ('development_history', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('version', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('id', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    activity.EnsembleAxis: (

        ('member', 'type', activity.AxisMember),
        ('extra_detail', 'type', unicode),
        ('short_identifier', 'type', unicode),
        ('target_requirement', 'type', designing.NumericalRequirement),

        ('member', 'cardinality', "1.N"),
        ('extra_detail', 'cardinality', "1.1"),
        ('short_identifier', 'cardinality', "1.1"),
        ('target_requirement', 'cardinality', "1.1"),

    ),
    activity.AxisMember: (

        ('index', 'type', int),
        ('extra_detail', 'type', unicode),
        ('description', 'type', unicode),
        ('value', 'type', float),

        ('index', 'cardinality', "1.1"),
        ('extra_detail', 'cardinality', "0.1"),
        ('description', 'cardinality', "1.1"),
        ('value', 'cardinality', "0.1"),

    ),
    science.Grid: (

        ('horizontal_grid_layout', 'type', unicode),
        ('vertical_grid_type', 'type', unicode),
        ('name', 'type', unicode),
        ('grid_extent', 'type', science.Extent),
        ('horizontal_grid_type', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('additional_details', 'type', science.Detail),
        ('vertical_grid_layout', 'type', unicode),

        ('horizontal_grid_layout', 'cardinality', "0.1"),
        ('vertical_grid_type', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('grid_extent', 'cardinality', "0.1"),
        ('horizontal_grid_type', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('additional_details', 'cardinality', "0.N"),
        ('vertical_grid_layout', 'cardinality', "0.1"),

    ),
    platform.ComponentPerformance: (

        ('component', 'type', software.SoftwareComponent),
        ('nodes_used', 'type', int),
        ('speed', 'type', float),
        ('cores_used', 'type', int),
        ('component_name', 'type', unicode),

        ('component', 'cardinality', "0.1"),
        ('nodes_used', 'cardinality', "0.1"),
        ('speed', 'cardinality', "1.1"),
        ('cores_used', 'cardinality', "0.1"),
        ('component_name', 'cardinality', "1.1"),

    ),
    science.Extent: (

        ('is_global', 'type', bool),
        ('bottom_vertical_level', 'type', float),
        ('eastern_boundary', 'type', float),
        ('southern_boundary', 'type', float),
        ('northern_boundary', 'type', float),
        ('region_known_as', 'type', unicode),
        ('top_vertical_level', 'type', float),
        ('z_units', 'type', unicode),
        ('western_boundary', 'type', float),

        ('is_global', 'cardinality', "1.1"),
        ('bottom_vertical_level', 'cardinality', "0.1"),
        ('eastern_boundary', 'cardinality', "0.1"),
        ('southern_boundary', 'cardinality', "0.1"),
        ('northern_boundary', 'cardinality', "0.1"),
        ('region_known_as', 'cardinality', "0.N"),
        ('top_vertical_level', 'cardinality', "0.1"),
        ('z_units', 'cardinality', "1.1"),
        ('western_boundary', 'cardinality', "0.1"),

    ),
    shared.Cimtext: (

        ('content', 'type', unicode),
        ('content_type', 'type', unicode),

        ('content', 'cardinality', "1.1"),
        ('content_type', 'cardinality', "1.1"),

    ),
    platform.Performance: (

        ('asypd', 'type', float),
        ('io_load', 'type', float),
        ('memory_bloat', 'type', float),
        ('name', 'type', unicode),
        ('load_imbalance', 'type', float),
        ('subcomponent_performance', 'type', platform.ComponentPerformance),
        ('chsy', 'type', float),
        ('total_nodes_used', 'type', int),
        ('sypd', 'type', float),
        ('platform', 'type', platform.Machine),
        ('meta', 'type', shared.DocMetaInfo),
        ('coupler_load', 'type', float),
        ('model', 'type', science.Model),
        ('compiler', 'type', unicode),

        ('asypd', 'cardinality', "0.1"),
        ('io_load', 'cardinality', "0.1"),
        ('memory_bloat', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),
        ('load_imbalance', 'cardinality', "0.1"),
        ('subcomponent_performance', 'cardinality', "0.1"),
        ('chsy', 'cardinality', "0.1"),
        ('total_nodes_used', 'cardinality', "0.1"),
        ('sypd', 'cardinality', "0.1"),
        ('platform', 'cardinality', "1.1"),
        ('meta', 'cardinality', "1.1"),
        ('coupler_load', 'cardinality', "0.1"),
        ('model', 'cardinality', "1.1"),
        ('compiler', 'cardinality', "0.1"),

    ),
    activity.ParentSimulation: (

        ('branch_time_in_parent', 'type', shared.DateTime),
        ('branch_time_in_child', 'type', shared.DateTime),
        ('parent', 'type', data.Simulation),

        ('branch_time_in_parent', 'cardinality', "0.1"),
        ('branch_time_in_child', 'cardinality', "0.1"),
        ('parent', 'cardinality', "1.1"),

    ),
    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------


    (activity.Activity, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (activity.Activity, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Activity, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (activity.Activity, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.Activity, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Activity, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Activity, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (activity.Activity, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.Activity, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Activity, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (drs.DrsAtomicDataset, 'ensemble_member'): (

        ('type', drs.DrsEnsembleIdentifier),

        ('cardinality', "1.1"),

    ),
    (drs.DrsAtomicDataset, 'temporal_constraint'): (

        ('type', drs.DrsTemporalIdentifier),

        ('cardinality', "0.1"),

    ),
    (drs.DrsAtomicDataset, 'model'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsAtomicDataset, 'realm'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsAtomicDataset, 'activity'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsAtomicDataset, 'geographical_constraint'): (

        ('type', drs.DrsGeographicalIndicator),

        ('cardinality', "0.1"),

    ),
    (drs.DrsAtomicDataset, 'product'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsAtomicDataset, 'frequency'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsAtomicDataset, 'variable_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsAtomicDataset, 'version_number'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (drs.DrsAtomicDataset, 'mip_table'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsAtomicDataset, 'institute'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsAtomicDataset, 'experiment'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (software.Composition, 'couplings'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (software.Composition, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (drs.DrsGeographicalIndicator, 'spatial_domain'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (drs.DrsGeographicalIndicator, 'bounding_box'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (drs.DrsGeographicalIndicator, 'operator'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (designing.SimulationPlan, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.SimulationPlan, 'expected_model'): (

        ('type', science.Model),

        ('cardinality', "1.1"),

    ),
    (designing.SimulationPlan, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.SimulationPlan, 'expected_performance_sypd'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (designing.SimulationPlan, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.SimulationPlan, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.SimulationPlan, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.SimulationPlan, 'expected_platform'): (

        ('type', platform.Machine),

        ('cardinality', "0.1"),

    ),
    (designing.SimulationPlan, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (designing.SimulationPlan, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "1.1"),

    ),
    (designing.SimulationPlan, 'will_support_experiments'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "1.N"),

    ),
    (designing.SimulationPlan, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.SimulationPlan, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.SimulationPlan, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),

    (activity.Ensemble, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'common_conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.Ensemble, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.0"),

    ),
    (activity.Ensemble, 'documentation'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.0"),

    ),
    (activity.Ensemble, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.0"),

    ),
    (activity.Ensemble, 'has_ensemble_axes'): (

        ('type', activity.EnsembleAxis),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'members'): (

        ('type', activity.EnsembleMember),

        ('cardinality', "1.N"),

    ),
    (activity.Ensemble, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.0"),

    ),
    (activity.Ensemble, 'part_of'): (

        ('type', activity.UberEnsemble),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'supported'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "1.N"),

    ),
    (activity.Ensemble, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (science.ScienceContext, 'context'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.ScienceContext, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.ScienceContext, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.QualityReview, 'date'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.QualityReview, 'metadata_reviewer'): (

        ('type', shared.Party),

        ('cardinality', "1.1"),

    ),
    (shared.QualityReview, 'quality_description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.QualityReview, 'quality_status'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.DatetimeSet, 'length'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),

    (designing.OutputTemporalRequirement, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.0"),

    ),
    (designing.OutputTemporalRequirement, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.OutputTemporalRequirement, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.OutputTemporalRequirement, 'sliced_subset'): (

        ('type', shared.TimesliceList),

        ('cardinality', "0.1"),

    ),
    (designing.OutputTemporalRequirement, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.0"),

    ),
    (designing.OutputTemporalRequirement, 'conformance_is_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.OutputTemporalRequirement, 'throughout'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.OutputTemporalRequirement, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.OutputTemporalRequirement, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.OutputTemporalRequirement, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.OutputTemporalRequirement, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (designing.OutputTemporalRequirement, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.OutputTemporalRequirement, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.OutputTemporalRequirement, 'continuous_subset'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.N"),

    ),
    (designing.OutputTemporalRequirement, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (science.ConservationProperties, 'corrected_conserved_prognostic_variables'): (

        ('type', data.VariableCollection),

        ('cardinality', "0.1"),

    ),
    (science.ConservationProperties, 'correction_methodology'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.ConservationProperties, 'flux_correction_was_used'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),

    (shared.RegularTimeset, 'length'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (shared.RegularTimeset, 'increment'): (

        ('type', shared.TimePeriod),

        ('cardinality', "1.1"),

    ),
    (shared.RegularTimeset, 'length'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (shared.RegularTimeset, 'start_date'): (

        ('type', shared.DateTime),

        ('cardinality', "1.1"),

    ),

    (software.Variable, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.Variable, 'prognostic'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (software.Variable, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Reference, 'context'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Reference, 'document'): (

        ('type', shared.ExternalDocument),

        ('cardinality', "1.1"),

    ),

    (designing.MultiEnsemble, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.0"),

    ),
    (designing.MultiEnsemble, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.MultiEnsemble, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.MultiEnsemble, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.0"),

    ),
    (designing.MultiEnsemble, 'conformance_is_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.MultiEnsemble, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.MultiEnsemble, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.MultiEnsemble, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.MultiEnsemble, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.MultiEnsemble, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (designing.MultiEnsemble, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.MultiEnsemble, 'ensemble_axis'): (

        ('type', designing.EnsembleRequirement),

        ('cardinality', "1.N"),

    ),
    (designing.MultiEnsemble, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Responsibility, 'party'): (

        ('type', shared.Party),

        ('cardinality', "1.N"),

    ),
    (shared.Responsibility, 'role'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Responsibility, 'when'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.1"),

    ),

    (data.VariableCollection, 'collection_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.VariableCollection, 'variables'): (

        ('type', unicode),

        ('cardinality', "1.N"),

    ),

    (platform.StoragePool, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.StoragePool, 'vendor'): (

        ('type', shared.Party),

        ('cardinality', "0.1"),

    ),
    (platform.StoragePool, 'volume_available'): (

        ('type', platform.StorageVolume),

        ('cardinality', "1.1"),

    ),
    (platform.StoragePool, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (platform.StoragePool, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (platform.Machine, 'online_documentation'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.N"),

    ),
    (platform.Machine, 'compute_pools'): (

        ('type', platform.ComputePool),

        ('cardinality', "1.N"),

    ),
    (platform.Machine, 'institution'): (

        ('type', shared.Party),

        ('cardinality', "1.1"),

    ),
    (platform.Machine, 'vendor'): (

        ('type', shared.Party),

        ('cardinality', "0.1"),

    ),
    (platform.Machine, 'partition'): (

        ('type', platform.Partition),

        ('cardinality', "0.N"),

    ),
    (platform.Machine, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (platform.Machine, 'model_number'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.Machine, 'storage_pools'): (

        ('type', platform.StoragePool),

        ('cardinality', "0.N"),

    ),
    (platform.Machine, 'when_used'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (platform.Machine, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (platform.Machine, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (designing.MultiTimeEnsemble, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.0"),

    ),
    (designing.MultiTimeEnsemble, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.MultiTimeEnsemble, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.MultiTimeEnsemble, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.0"),

    ),
    (designing.MultiTimeEnsemble, 'conformance_is_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.MultiTimeEnsemble, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.MultiTimeEnsemble, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.MultiTimeEnsemble, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.MultiTimeEnsemble, 'ensemble_members'): (

        ('type', shared.DatetimeSet),

        ('cardinality', "1.1"),

    ),
    (designing.MultiTimeEnsemble, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (designing.MultiTimeEnsemble, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.MultiTimeEnsemble, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.MultiTimeEnsemble, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (drs.DrsPublicationDataset, 'experiment'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsPublicationDataset, 'institute'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsPublicationDataset, 'model'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsPublicationDataset, 'activity'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsPublicationDataset, 'frequency'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (drs.DrsPublicationDataset, 'product'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsPublicationDataset, 'realm'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (drs.DrsPublicationDataset, 'version_number'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (science.KeyProperties, 'grid'): (

        ('type', science.Grid),

        ('cardinality', "1.1"),

    ),
    (science.KeyProperties, 'extra_conservation_properties'): (

        ('type', science.ConservationProperties),

        ('cardinality', "0.1"),

    ),
    (science.KeyProperties, 'time_step'): (

        ('type', float),

        ('cardinality', "1.1"),

    ),
    (science.KeyProperties, 'resolution'): (

        ('type', science.Resolution),

        ('cardinality', "1.1"),

    ),
    (science.KeyProperties, 'tuning_applied'): (

        ('type', science.Tuning),

        ('cardinality', "0.1"),

    ),
    (science.KeyProperties, 'additional_detail'): (

        ('type', science.Detail),

        ('cardinality', "0.N"),

    ),

    (science.SubProcess, 'implementation_overview'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.SubProcess, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (science.SubProcess, 'properties'): (

        ('type', science.Detail),

        ('cardinality', "0.N"),

    ),
    (science.SubProcess, 'context'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.SubProcess, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.SubProcess, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (science.ScientificDomain, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (science.ScientificDomain, 'simulates'): (

        ('type', science.Process),

        ('cardinality', "1.N"),

    ),
    (science.ScientificDomain, 'realm'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.ScientificDomain, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.ScientificDomain, 'overview'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.ScientificDomain, 'differing_key_properties'): (

        ('type', science.KeyProperties),

        ('cardinality', "0.1"),

    ),
    (science.ScientificDomain, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.ScientificDomain, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),

    (designing.NumericalExperiment, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalExperiment, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.NumericalExperiment, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalExperiment, 'related_experiments'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalExperiment, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.NumericalExperiment, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalExperiment, 'rationale'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.NumericalExperiment, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalExperiment, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.0"),

    ),
    (designing.NumericalExperiment, 'requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalExperiment, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalExperiment, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),

    (data.Downscaling, 'primary_ensemble'): (

        ('type', activity.Ensemble),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (data.Downscaling, 'ran_for_experiments'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "1.N"),

    ),
    (data.Downscaling, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (data.Downscaling, 'used'): (

        ('type', science.Model),

        ('cardinality', "1.1"),

    ),
    (data.Downscaling, 'part_of_project'): (

        ('type', designing.Project),

        ('cardinality', "1.N"),

    ),
    (data.Downscaling, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (data.Downscaling, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'ensemble_identifier'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (data.Downscaling, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (data.Downscaling, 'parent_simulation'): (

        ('type', activity.ParentSimulation),

        ('cardinality', "0.0"),

    ),
    (data.Downscaling, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (data.Downscaling, 'downscaled_from'): (

        ('type', data.Simulation),

        ('cardinality', "1.1"),

    ),
    (data.Downscaling, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.0"),

    ),
    (data.Downscaling, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.1"),

    ),

    (drs.DrsTemporalIdentifier, 'end'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (drs.DrsTemporalIdentifier, 'start'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsTemporalIdentifier, 'suffix'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.TimesliceList, 'members'): (

        ('type', shared.NumberArray),

        ('cardinality', "1.1"),

    ),
    (shared.TimesliceList, 'units'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (science.Resolution, 'is_adaptive_grid'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (science.Resolution, 'number_of_xy_gridpoints'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (science.Resolution, 'typical_x_degrees'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (science.Resolution, 'number_of_levels'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (science.Resolution, 'typical_y_degrees'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (science.Resolution, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Resolution, 'equivalent_resolution_km'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),

    (software.ComponentBase, 'documentation'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (software.ComponentBase, 'repository'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.1"),

    ),
    (software.ComponentBase, 'development_history'): (

        ('type', software.DevelopmentPath),

        ('cardinality', "0.1"),

    ),
    (software.ComponentBase, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentBase, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.ComponentBase, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentBase, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.ComponentBase, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (drs.DrsEnsembleIdentifier, 'realisation_number'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (drs.DrsEnsembleIdentifier, 'perturbation_number'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (drs.DrsEnsembleIdentifier, 'initialisation_method_number'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),

    (shared.KeyFloat, 'key'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.KeyFloat, 'value'): (

        ('type', float),

        ('cardinality', "1.1"),

    ),

    (software.DevelopmentPath, 'creators'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (software.DevelopmentPath, 'developed_in_house'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (software.DevelopmentPath, 'funding_sources'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (software.DevelopmentPath, 'consortium_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.DevelopmentPath, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.SoftwareComponent, 'language'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'repository'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'connection_points'): (

        ('type', software.Variable),

        ('cardinality', "0.N"),

    ),
    (software.SoftwareComponent, 'coupling_framework'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'license'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'development_history'): (

        ('type', software.DevelopmentPath),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.SoftwareComponent, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'sub_components'): (

        ('type', software.SoftwareComponent),

        ('cardinality', "0.N"),

    ),
    (software.SoftwareComponent, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'grid'): (

        ('type', software.Gridspec),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.SoftwareComponent, 'composition'): (

        ('type', software.Composition),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'documentation'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),

    (platform.StorageVolume, 'units'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (platform.StorageVolume, 'volume'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),

    (shared.IrregularDateset, 'length'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (shared.IrregularDateset, 'date_set'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.Pid, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Pid, 'resolution_service'): (

        ('type', shared.OnlineResource),

        ('cardinality', "1.1"),

    ),

    (activity.EnsembleMember, 'ran_on'): (

        ('type', platform.Machine),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'simulation'): (

        ('type', data.Simulation),

        ('cardinality', "1.1"),

    ),
    (activity.EnsembleMember, 'errata'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'had_performance'): (

        ('type', platform.Performance),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'variant_id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (activity.UberEnsemble, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (activity.UberEnsemble, 'has_ensemble_axes'): (

        ('type', activity.EnsembleAxis),

        ('cardinality', "1.N"),

    ),
    (activity.UberEnsemble, 'common_conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.0"),

    ),
    (activity.UberEnsemble, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.UberEnsemble, 'child_ensembles'): (

        ('type', activity.Ensemble),

        ('cardinality', "1.N"),

    ),
    (activity.UberEnsemble, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (activity.UberEnsemble, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.0"),

    ),
    (activity.UberEnsemble, 'documentation'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.N"),

    ),
    (activity.UberEnsemble, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.0"),

    ),
    (activity.UberEnsemble, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.0"),

    ),
    (activity.UberEnsemble, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.UberEnsemble, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.UberEnsemble, 'supported'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "1.N"),

    ),
    (activity.UberEnsemble, 'part_of'): (

        ('type', activity.UberEnsemble),

        ('cardinality', "0.N"),

    ),
    (activity.UberEnsemble, 'members'): (

        ('type', activity.EnsembleMember),

        ('cardinality', "0.0"),

    ),
    (activity.UberEnsemble, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.0"),

    ),
    (activity.UberEnsemble, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.Party, 'organisation'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (shared.Party, 'address'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Party, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Party, 'email'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Party, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (shared.Party, 'url'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.1"),

    ),
    (shared.Party, 'orcid_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (science.Algorithm, 'context'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Algorithm, 'implementation_overview'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Algorithm, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Algorithm, 'prognostic_variables'): (

        ('type', data.VariableCollection),

        ('cardinality', "0.1"),

    ),
    (science.Algorithm, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Algorithm, 'diagnostic_variables'): (

        ('type', data.VariableCollection),

        ('cardinality', "0.1"),

    ),
    (science.Algorithm, 'forced_variables'): (

        ('type', data.VariableCollection),

        ('cardinality', "0.1"),

    ),
    (science.Algorithm, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),

    (designing.DomainProperties, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.0"),

    ),
    (designing.DomainProperties, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.DomainProperties, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.DomainProperties, 'required_resolution'): (

        ('type', science.Resolution),

        ('cardinality', "0.1"),

    ),
    (designing.DomainProperties, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.0"),

    ),
    (designing.DomainProperties, 'conformance_is_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.DomainProperties, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.DomainProperties, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.DomainProperties, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.DomainProperties, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.DomainProperties, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (designing.DomainProperties, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.DomainProperties, 'required_extent'): (

        ('type', science.Extent),

        ('cardinality', "0.1"),

    ),
    (designing.DomainProperties, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (platform.ComputePool, 'number_of_nodes'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'compute_cores_per_node'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'memory_per_node'): (

        ('type', platform.StorageVolume),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'cpu_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'interconnect'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'model_number'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'accelerator_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'operating_system'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'accelerators_per_node'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.TimePeriod, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "0.1"),

    ),
    (shared.TimePeriod, 'length'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (shared.TimePeriod, 'date'): (

        ('type', shared.DateTime),

        ('cardinality', "0.1"),

    ),
    (shared.TimePeriod, 'units'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.TimePeriod, 'date_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (software.Gridspec, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.OnlineResource, 'linkage'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.OnlineResource, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.OnlineResource, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.OnlineResource, 'protocol'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (designing.EnsembleRequirement, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.0"),

    ),
    (designing.EnsembleRequirement, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.EnsembleRequirement, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.EnsembleRequirement, 'ensemble_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.EnsembleRequirement, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.0"),

    ),
    (designing.EnsembleRequirement, 'conformance_is_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.EnsembleRequirement, 'minimum_size'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (designing.EnsembleRequirement, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.EnsembleRequirement, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.EnsembleRequirement, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.EnsembleRequirement, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (designing.EnsembleRequirement, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.EnsembleRequirement, 'ensemble_member'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (designing.EnsembleRequirement, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.EnsembleRequirement, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (platform.Partition, 'online_documentation'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.N"),

    ),
    (platform.Partition, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (platform.Partition, 'vendor'): (

        ('type', shared.Party),

        ('cardinality', "0.1"),

    ),
    (platform.Partition, 'partition'): (

        ('type', platform.Partition),

        ('cardinality', "0.N"),

    ),
    (platform.Partition, 'institution'): (

        ('type', shared.Party),

        ('cardinality', "1.1"),

    ),
    (platform.Partition, 'model_number'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.Partition, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.Partition, 'when_used'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (platform.Partition, 'compute_pools'): (

        ('type', platform.ComputePool),

        ('cardinality', "1.N"),

    ),
    (platform.Partition, 'storage_pools'): (

        ('type', platform.StoragePool),

        ('cardinality', "0.N"),

    ),

    (designing.NumericalRequirement, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalRequirement, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.NumericalRequirement, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalRequirement, 'conformance_is_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.NumericalRequirement, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.NumericalRequirement, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalRequirement, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalRequirement, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalRequirement, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalRequirement, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.0"),

    ),
    (designing.NumericalRequirement, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalRequirement, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),

    (designing.ForcingConstraint, 'category'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.0"),

    ),
    (designing.ForcingConstraint, 'conformance_is_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.ForcingConstraint, 'code'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.ForcingConstraint, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (designing.ForcingConstraint, 'data_link'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'forcing_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.ForcingConstraint, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.ForcingConstraint, 'group'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'origin'): (

        ('type', shared.Reference),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.ForcingConstraint, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.ForcingConstraint, 'additional_constraint'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.0"),

    ),

    (shared.ExternalDocument, 'doi'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ExternalDocument, 'online_at'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.1"),

    ),
    (shared.ExternalDocument, 'title'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.ExternalDocument, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (shared.ExternalDocument, 'authorship'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ExternalDocument, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.ExternalDocument, 'date'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ExternalDocument, 'publication_detail'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Calendar, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Calendar, 'month_lengths'): (

        ('type', int),

        ('cardinality', "0.N"),

    ),
    (shared.Calendar, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Calendar, 'standard_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.NumberArray, 'values'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (activity.Conformance, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.0"),

    ),
    (activity.Conformance, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.Conformance, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'target_requirement'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "1.1"),

    ),
    (activity.Conformance, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.Conformance, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.Conformance, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.0"),

    ),
    (activity.Conformance, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (activity.Conformance, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.0"),

    ),
    (activity.Conformance, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.0"),

    ),
    (activity.Conformance, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),

    (designing.TemporalConstraint, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.0"),

    ),
    (designing.TemporalConstraint, 'conformance_is_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.TemporalConstraint, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.TemporalConstraint, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (designing.TemporalConstraint, 'required_calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'required_duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.TemporalConstraint, 'start_date'): (

        ('type', shared.DateTime),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'start_flexibility'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.TemporalConstraint, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.TemporalConstraint, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.0"),

    ),

    (shared.DocMetaInfo, 'external_ids'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (shared.DocMetaInfo, 'create_date'): (

        ('type', datetime.datetime),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'sort_key'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'source'): (

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
    (shared.DocMetaInfo, 'version'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'type_sort_key'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'language'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'institute'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'update_date'): (

        ('type', datetime.datetime),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'type_display_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocMetaInfo, 'drs_keys'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (shared.DocMetaInfo, 'project'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'author'): (

        ('type', shared.Party),

        ('cardinality', "0.1"),

    ),

    (designing.Project, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.Project, 'sub_projects'): (

        ('type', designing.Project),

        ('cardinality', "0.N"),

    ),
    (designing.Project, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.Project, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.Project, 'previous_projects'): (

        ('type', designing.Project),

        ('cardinality', "0.N"),

    ),
    (designing.Project, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.Project, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.Project, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.Project, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (designing.Project, 'requires_experiments'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "0.N"),

    ),
    (designing.Project, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.Project, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.Project, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.1"),

    ),

    (data.Dataset, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (data.Dataset, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Dataset, 'availability'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.N"),

    ),
    (data.Dataset, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (data.Dataset, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (data.Dataset, 'produced_by'): (

        ('type', data.Simulation),

        ('cardinality', "0.1"),

    ),
    (data.Dataset, 'related_to_dataset'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.N"),

    ),
    (data.Dataset, 'drs_datasets'): (

        ('type', drs.DrsPublicationDataset),

        ('cardinality', "0.N"),

    ),
    (data.Dataset, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),

    (science.Process, 'algorithms'): (

        ('type', science.Algorithm),

        ('cardinality', "0.N"),

    ),
    (science.Process, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (science.Process, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Process, 'context'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Process, 'implementation_overview'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Process, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Process, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Process, 'sub_processes'): (

        ('type', science.SubProcess),

        ('cardinality', "0.N"),

    ),
    (science.Process, 'properties'): (

        ('type', science.Detail),

        ('cardinality', "0.N"),

    ),

    (shared.DateTime, 'offset'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (shared.DateTime, 'value'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (science.Tuning, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Tuning, 'global_mean_metrics_used'): (

        ('type', data.VariableCollection),

        ('cardinality', "0.1"),

    ),
    (science.Tuning, 'regional_metrics_used'): (

        ('type', data.VariableCollection),

        ('cardinality', "0.1"),

    ),
    (science.Tuning, 'trend_metrics_used'): (

        ('type', data.VariableCollection),

        ('cardinality', "0.1"),

    ),

    (shared.DocReference, 'type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocReference, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocReference, 'context'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'constraint_vocabulary'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'protocol'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'relationship'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'linkage'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocReference, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'version'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (science.Detail, 'content'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Detail, 'with_cardinality'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Detail, 'detail_selection'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (science.Detail, 'from_vocab'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Detail, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Detail, 'select'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Detail, 'context'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Detail, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (software.EntryPoint, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (data.Simulation, 'primary_ensemble'): (

        ('type', activity.Ensemble),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (data.Simulation, 'ran_for_experiments'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "1.N"),

    ),
    (data.Simulation, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),
    (data.Simulation, 'used'): (

        ('type', science.Model),

        ('cardinality', "1.1"),

    ),
    (data.Simulation, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (data.Simulation, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'calendar'): (

        ('type', shared.Calendar),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'ensemble_identifier'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (data.Simulation, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (data.Simulation, 'parent_simulation'): (

        ('type', activity.ParentSimulation),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (data.Simulation, 'part_of_project'): (

        ('type', designing.Project),

        ('cardinality', "1.N"),

    ),
    (data.Simulation, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.0"),

    ),
    (data.Simulation, 'duration'): (

        ('type', shared.TimePeriod),

        ('cardinality', "0.1"),

    ),

    (science.Model, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (science.Model, 'repository'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'coupled_components'): (

        ('type', science.Model),

        ('cardinality', "0.N"),

    ),
    (science.Model, 'coupler'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'simulates'): (

        ('type', science.ScientificDomain),

        ('cardinality', "0.N"),

    ),
    (science.Model, 'development_history'): (

        ('type', software.DevelopmentPath),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Model, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'internal_software_components'): (

        ('type', software.SoftwareComponent),

        ('cardinality', "0.N"),

    ),
    (science.Model, 'category'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Model, 'model_default_properties'): (

        ('type', science.KeyProperties),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'documentation'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),

    (activity.EnsembleAxis, 'target_requirement'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "1.1"),

    ),
    (activity.EnsembleAxis, 'short_identifier'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.EnsembleAxis, 'member'): (

        ('type', activity.AxisMember),

        ('cardinality', "1.N"),

    ),
    (activity.EnsembleAxis, 'extra_detail'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (activity.AxisMember, 'extra_detail'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.AxisMember, 'index'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (activity.AxisMember, 'value'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (activity.AxisMember, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (science.Grid, 'grid_extent'): (

        ('type', science.Extent),

        ('cardinality', "0.1"),

    ),
    (science.Grid, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Grid, 'horizontal_grid_layout'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Grid, 'vertical_grid_layout'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Grid, 'horizontal_grid_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Grid, 'additional_details'): (

        ('type', science.Detail),

        ('cardinality', "0.N"),

    ),
    (science.Grid, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (science.Grid, 'vertical_grid_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (platform.ComponentPerformance, 'speed'): (

        ('type', float),

        ('cardinality', "1.1"),

    ),
    (platform.ComponentPerformance, 'component_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (platform.ComponentPerformance, 'component'): (

        ('type', software.SoftwareComponent),

        ('cardinality', "0.1"),

    ),
    (platform.ComponentPerformance, 'cores_used'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (platform.ComponentPerformance, 'nodes_used'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (science.Extent, 'northern_boundary'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (science.Extent, 'western_boundary'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (science.Extent, 'bottom_vertical_level'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (science.Extent, 'southern_boundary'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (science.Extent, 'eastern_boundary'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (science.Extent, 'region_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (science.Extent, 'is_global'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (science.Extent, 'top_vertical_level'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (science.Extent, 'z_units'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.Cimtext, 'content'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.Cimtext, 'content_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (platform.Performance, 'asypd'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'io_load'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'sypd'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'chsy'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'load_imbalance'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'subcomponent_performance'): (

        ('type', platform.ComponentPerformance),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'total_nodes_used'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'memory_bloat'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'coupler_load'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'compiler'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (platform.Performance, 'model'): (

        ('type', science.Model),

        ('cardinality', "1.1"),

    ),
    (platform.Performance, 'platform'): (

        ('type', platform.Machine),

        ('cardinality', "1.1"),

    ),

    (activity.ParentSimulation, 'branch_time_in_child'): (

        ('type', shared.DateTime),

        ('cardinality', "0.1"),

    ),
    (activity.ParentSimulation, 'branch_time_in_parent'): (

        ('type', shared.DateTime),

        ('cardinality', "0.1"),

    ),
    (activity.ParentSimulation, 'parent'): (

        ('type', data.Simulation),

        ('cardinality', "1.1"),

    ),
}

# Count of class constraints.
TOTAL_CONSTRAINTS = sum(len(CONSTRAINTS[c]) for c in CLASSES)

# ------------------------------------------------
# Type help text.
# ------------------------------------------------
HELP = {
    # ------------------------------------------------
    # Packages.
    # ------------------------------------------------

    drs: "Types that describe the directory structures to which climate model output is written.",
    designing: "Types that describe project design features.",
    software: "Types that describe the software that constiutes a climate model.",
    shared: "Shared types that might be imported from other packages within the ontology.",
    science: "Types that describe the science being performed.",
    platform: "Types that describe hardware upon which climate models are run.",
    data: "Types that describe output that climate models emit.",
    activity: "Types that describe context against which climate models are run.",

    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    drs.DrsAtomicDataset: """
        An entity in a DRS file system.

    """,
    drs.DrsPublicationDataset: """
        A collection of atomic datasets which share a single combination of DRS component values.

    """,
    drs.DrsEnsembleIdentifier: """
        Identifies an ensemble realisation.

    """,
    drs.DrsTemporalIdentifier: """
        Provides information about temporal subsetting and/or averaging.
    If only N1 is present, it a temporal instant,
    If N1-N2 are present with no suffix, it is a temporal subset,
    If N1-N2 with a suffix are present, then some sort of temporal averaging has been applied across
    the period.

    """,
    drs.DrsGeographicalIndicator: """
        Specifies geographical subsets described by bounding boxes or by named regions.
     One of spatial domain or bounding box must appear.

    """,
    designing.TemporalConstraint: """
        A temporal constraint on a numerical experiment.

    """,
    designing.NumericalExperiment: """
        Defines a numerical experiment.

    """,
    designing.MultiTimeEnsemble: """
        Defines an experiment ensemble with multiple start dates.

    """,
    designing.NumericalRequirement: """
        A numerical requirement associated with a numerical experiment.

    """,
    designing.OutputTemporalRequirement: """
        Provides details of when output is required from an experiment.
    Typically output will be required in one of three modes:
    (1) continuous,
    (2) continuous for a set of subset periods, or
    (3) sliced for a set of months in a year or days in a month.

    """,
    designing.EnsembleRequirement: """
        Defines an experiment ensemble.

    """,
    designing.MultiEnsemble: """
        In the case of multiple ensemble axes, defines how they
    are set up and ordered.

    """,
    designing.Project: """
        Describes a scientific project.

    """,
    designing.DomainProperties: """
        Properties of the domain which needs to be simulated, extend and/or resolution.

    """,
    designing.SimulationPlan: """
        Describes a simulation that needs to be run.

    """,
    designing.ForcingConstraint: """
        Identifies a model forcing constraint.

    """,
    software.DevelopmentPath: """
        Describes the software development path for this model/component.

    """,
    software.Composition: """
        Describes how component variables are coupled together either to/from other
    SoftwareComponents or external data files. The variables specified by a component's
    composition must be owned by that component, or a  child of that component;
    child components cannot couple together parent variables.

    """,
    software.SoftwareComponent: """
        An embedded piece of software that does not normally function as a standalone model (although
    it may be used standalone in a test harness).

    """,
    software.Variable: """
        An instance of a model software variable which may be prognostic or diagnostic, and which is
    available as a connection to other software components. Note that these variables may only exist
    within the software workflow as interim quantities or coupling endpoints. Input and output
    variables will be a subset of these software variables.

    """,
    software.EntryPoint: """
        Describes a function or subroutine of a SoftwareComponent.
    BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model.
    Currently, a very basic schedule can be approximated by using the 'proceeds' and 'follows' attributes,
    however a more complete system is required for full BFG compatibility.
    Every EntryPoint can have a set of arguments associated with it.
    These reference (previously defined) variables.

    """,
    software.ComponentBase: """
        Base class for software component properties, whether a top level model,
    or a specific piece of code known as a component. In software terms, a
    component is a discrete set of code that takes input data and generates output data.
    Components may or may not have scientific descriptions.

    """,
    software.Gridspec: """
        Fully defines the computational grid used.

    """,
    shared.IrregularDateset: """
        A set of irregularly spaced times.

    """,
    shared.NumberArray: """
        Provides a class for entering an array of numbers.

    """,
    shared.Calendar: """
        Describes the calendar required/used in an experiment/simulation.
    This class is based on the calendar attributes and properties found in the
    CF netCDF conventions.

    """,
    shared.DocReference: """
        Specialisation of online resource for link between CIM documents, whether the
    remote document exists when complete, or not.

    """,
    shared.Reference: """
        An external document which can have a context associated with it.

    """,
    shared.Pid: """
        A permanent identifier (with a resolution service).

    """,
    shared.DatetimeSet: """
        Base class for a set of dates or times.
    Note that we assume either a periodic set of dates which can
    be date and/or time, or an irregular set which can only be dates.

    """,
    shared.Party: """
        Implements minimal material for an ISO19115-1 (2014) compliant party.
    For our purposes this is a much better animal than the previous responsibleParty 
    which munged roles together with people. Note we have collapsed CI_Contact,
    CI_Individual and CI_Organisation as well as the abstract CI_Party.

    """,
    shared.QualityReview: """
        Assertations as to the completeness and quality of a document.

    """,
    shared.TimesliceList: """
        A list of referential dates, 
        e.g. yearlist, 1,4,5 would refer to jan,april,may,
             monthlist, 1,5,6 would refer to the 1st, 5th and 6th of the month.

    """,
    shared.DateTime: """
        A date or time. Either in simulation time with the simulation
    calendar, or with reference to a simulation start, in which
    case the datetime is an interval after the start date.

    """,
    shared.TimePeriod: """
        A time period class aka a temporal extent.

    """,
    shared.RegularTimeset: """
        A regularly spaced set of times.

    """,
    shared.DocMetaInfo: """
        Encapsulates document meta information used by es-doc machinery. Will not normally be
    populated by humans. May duplicate information held in 'visible' metadata.

    """,
    shared.KeyFloat: """
        Holds a key and a float value.

    """,
    shared.OnlineResource: """
        A minimal approximation of ISO19115 CI_ONLINERESOURCE, provides a link and details
    of how to use that link.

    """,
    shared.Responsibility: """
        Implements the ISO19115-1 (2014) CI_Responsibility (which replaces
    responsibleParty). Combines a person and their role in doing something.

    """,
    shared.ExternalDocument: """
        A real world document, could be a book, a journal article, a manual, a web page ... it might or might
    not be online, although preferably it would be. We expect a typical citation to be built up
    as in the following 'authorship, date: title, publication_detail (doi if present)'.

    """,
    shared.Cimtext: """
        Provides a text class which supports plaintext, html, and
    friends (or will do).

    """,
    science.Extent: """
        Key scientific characteristics of the grid use to simulate a specific domain.
    Note that the extent does not itself describe a grid, so, for example, a polar
    stereographic grid may have an extent of northern boundary 90N, southern boundary
    45N, but the fact that it is PS comes from the grid_type.

    """,
    science.ScientificDomain: """
        Scientific area of a numerical model - usually a sub-model or component.
    Can also be known as a realm.

    """,
    science.Tuning: """
        Method used to optimise equation parameters in model component (aka 'tuning').

    """,
    science.Process: """
        Provides structure for description of a process simulated within a particular
    area (or domain/realm/component) of a model. This will often be subclassed
    within a specific implementation so that constraints can be used to ensure
    that the process details requested are consistent with project requirements
    for information.

    """,
    science.SubProcess: """
        Provides structure for description of part of process simulated within a particular
    area (or domain/realm/component) of a model. Typically this will be a part of process
    which shares common properties. It will normally be sub classed within a specific
    implementation so that constraints can be used to ensure that the process details requested are
    consistent with projects requirements for information.

    """,
    science.ScienceContext: """
        This is the base class for the science mixins, that is the classes which
    we expect to be specialised and extended by project specific vocabularies.
    It is expected that values of these will be provided within vocabulary
    definitions.

    """,
    science.Algorithm: """
        Used to hold information associated with an algorithm which implements some key
    part of a process. In most cases this is quite a high level concept and isn't intended
    to describe the gory detail of how the code implements the algorithm rather the key
    scientific aspects of the algorithm. In particular, it provides a method
    of grouping variables which take part in an algorithm within a process.

    """,
    science.Grid: """
        This describes the numerical grid used for the calculations.
    It is not necessarily the grid upon which the data is output.
    It is NOT the resolution, which is a property of a specific domain.

    """,
    science.Resolution: """
        Describes the computational spatial resolution of a component or process.
    Not intended to replace or replicate the output grid description.
    When it appears as part of a process description, provide only properties that differ from parent domain.
    Note that this is supposed to capture gross features of the grid, we expect many grids will have
    different variable layouts, those should be described in the grid description, and the exact resolution
    is not required. Note that many properties are not appropriate for adaptive grids.

    """,
    science.Model: """
        A model component: can be executed standalone, and has as scientific
    description available via a link to a science.domain document. (A configured model can
     be understood in terms of a simulation, a model, and a configuration.).

    """,
    science.KeyProperties: """
        High level list of key properties. It can be specialised in
    extension packages using the detail extensions.

    """,
    science.Detail: """
        Provides detail of specific properties, there are two possible specialisations
    expected: (1) A detail_vocabulary is identified, and a cardinality is assigned to that
    for possible responses, or (2) Detail is used to provide a collection for a set of
    properties which are defined in the sub-class. However, those properties must have a type
    which is selected from the classmap (that is, standard 'non-es-doc' types).

    """,
    science.ConservationProperties: """
        Describes how prognostic variables are conserved.

    """,
    platform.StoragePool: """
        Homogeneous storage pool on a computing machine.

    """,
    platform.ComputePool: """
        Homogeneous pool of nodes within a computing machine.

    """,
    platform.Machine: """
        A computer/system/platform/machine which is used for simulation.

    """,
    platform.Partition: """
        A major partition (component) of a computing system (aka machine).

    """,
    platform.ComponentPerformance: """
        Describes the simulation rate of a component in seconds per model day.

    """,
    platform.Performance: """
        Describes the properties of a performance of a configured model on a particular system/machine.

    """,
    platform.StorageVolume: """
        Volume and units.

    """,
    data.VariableCollection: """
        A collection of variables within the scope of a code or process element.

    """,
    data.Simulation: """
        Simulation class provides the integrating link about what models were run and wny.
    In many cases this should be auto-generated from output file headers.

    """,
    data.Dataset: """
        Dataset discovery information.

    """,
    data.Downscaling: """
        Defines a downscaling activity.

    """,
    activity.Activity: """
        Base class for activities.

    """,
    activity.Conformance: """
        A specific conformance. Describes how a particular numerical requirement has been implemented.
    Will normally be linked from an ensemble descriptor.

    """,
    activity.Ensemble: """
        Generic ensemble definition.
    Holds the definition of how the various ensemble members have been configured.
    If ensemble axes are not present, then this is either a single member ensemble,
    or part of an uber ensemble.

    """,
    activity.UberEnsemble: """
        An ensemble made up of other ensembles. Often used where parts of an ensemble were run by
    different institutes. Could also be used when a new experiment is designed which can use
    ensemble members from previous experiments and/or projects.

    """,
    activity.EnsembleMember: """
        An ensemble may be a complicated interplay of axes, for example, r/i/p, not all of which
    are populated, so we need a list of the actual simulations and how they map onto the ensemble
    axes.

    """,
    activity.ParentSimulation: """
        Defines the relationship between a simulation and its parent.

    """,
    activity.AxisMember: """
        Description of a given ensemble member. It will normally be related to a specific
    ensemble requirement. Note that start dates can be extracted directly from the simulations
    and do not need to be recorded with an axis member description.

    """,
    activity.EnsembleAxis: """
        Defines the meaning of r/i/p indices in an ensemble.

    """,

    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------

    (drs.DrsAtomicDataset, 'geographical_constraint'):
        "Identifies geographical subsets and spatial means.",
    (drs.DrsAtomicDataset, 'variable_name'):
        "Identifies the physical quantity (when used in conjunction with the MIP table).",
    (drs.DrsAtomicDataset, 'temporal_constraint'):
        "Identifies temporal subsets or means.",
    (drs.DrsAtomicDataset, 'ensemble_member'):
        "Unambiguously identifiers ensemble realisation information.",
    (drs.DrsAtomicDataset, 'mip_table'):
        "The MIP table, together with the variable defines the physical quantity.",
    (drs.DrsPublicationDataset, 'institute'):
        "The institute responsible for this data entity.",
    (drs.DrsPublicationDataset, 'model'):
        "A model identifier (sans blanks/periods and parenthesis).",
    (drs.DrsPublicationDataset, 'realm'):
        "Modelling realm.",
    (drs.DrsPublicationDataset, 'activity'):
        "A model intercomparison activity or other project which aggregates or collects data.",
    (drs.DrsPublicationDataset, 'product'):
        "Used to provide categories of data products within the activity.",
    (drs.DrsPublicationDataset, 'version_number'):
        "Uniquely identifies a particular version of a publication level dataset.",
    (drs.DrsPublicationDataset, 'frequency'):
        "Frequency of data stored in this entity.",
    (drs.DrsPublicationDataset, 'experiment'):
        "An experiment (or experiment family and type, e.g. rcp45).",
    (drs.DrsEnsembleIdentifier, 'realisation_number'):
        "Standard ensemble axis realisation number (usually an initial condition ensemble).",
    (drs.DrsEnsembleIdentifier, 'initialisation_method_number'):
        "Identifies which method of initialisation was used, if multiple methods used.",
    (drs.DrsEnsembleIdentifier, 'perturbation_number'):
        "Identifies different members of a perturbed physics ensemble.",
    (drs.DrsTemporalIdentifier, 'end'):
        "N2, required to indicate a period.",
    (drs.DrsTemporalIdentifier, 'suffix'):
        "If present, used to indicate climatology or average.",
    (drs.DrsTemporalIdentifier, 'start'):
        "N1,  of the form yyyy[MM[dd[hh[mm[ss]]]]].",
    (drs.DrsGeographicalIndicator, 'spatial_domain'):
        "Geographical indicator (currently only 'global' is acceptable).",
    (drs.DrsGeographicalIndicator, 'bounding_box'):
        "DRS bounding box of the form 'latJHJJHHlonMZMMZZ' where H, HH, Z, ZZ are from {NS} {EW} respectively.",
    (drs.DrsGeographicalIndicator, 'operator'):
        "Spatial averagin applied to the geographical region.",
    (designing.TemporalConstraint, 'start_date'):
        "Required start date.",
    (designing.TemporalConstraint, 'start_flexibility'):
        "Amount of time before required start date that it is permissible to begin integration.",
    (designing.TemporalConstraint, 'required_calendar'):
        "Required calendar (e.g. for paleo simulations).",
    (designing.TemporalConstraint, 'required_duration'):
        "Constraint on time or length of simulation.",
    (designing.NumericalExperiment, 'requirements'):
        "Requirements that conformant simulations need to satisfy.",
    (designing.NumericalExperiment, 'related_experiments'):
        "A related experiment.",
    (designing.MultiTimeEnsemble, 'ensemble_members'):
        "Description of date or time set of start dates.",
    (designing.NumericalRequirement, 'conformance_is_requested'):
        "Indicator as to whether ensemble documentation should include conformance information for this requirement.",
    (designing.NumericalRequirement, 'additional_requirements'):
        "Additional detail for this requirement.",
    (designing.OutputTemporalRequirement, 'throughout'):
        "Whether or not output is required throughout simulation.",
    (designing.OutputTemporalRequirement, 'continuous_subset'):
        "Set of periods for which continuous output is required.",
    (designing.OutputTemporalRequirement, 'sliced_subset'):
        "Description of how slices are laid out.",
    (designing.EnsembleRequirement, 'ensemble_member'):
        "Constraint on each ensemble member.",
    (designing.EnsembleRequirement, 'ensemble_type'):
        "Type of ensemble.",
    (designing.EnsembleRequirement, 'minimum_size'):
        "Minimum number of members.",
    (designing.MultiEnsemble, 'ensemble_axis'):
        "List of orthogonal ensembles.",
    (designing.Project, 'sub_projects'):
        "Activities within the project with their own name and aim(s).",
    (designing.Project, 'previous_projects'):
        "Previous projects with similar aims.",
    (designing.Project, 'requires_experiments'):
        "Experiments required to deliver project.",
    (designing.DomainProperties, 'required_extent'):
        "Constraint on extent of domain to be simulated.",
    (designing.DomainProperties, 'required_resolution'):
        "Constraint on resolution required in simulated domain.",
    (designing.SimulationPlan, 'expected_model'):
        "The model used to run the simulation.",
    (designing.SimulationPlan, 'expected_platform'):
        "The machine on which the simulation will be run.",
    (designing.SimulationPlan, 'will_support_experiments'):
        "An experiment with which the planned simulation will be associated.",
    (designing.SimulationPlan, 'expected_performance_sypd'):
        "Expected performance in simulated years per real day.",
    (designing.ForcingConstraint, 'group'):
        "Sub-Category (e.g. GHG).",
    (designing.ForcingConstraint, 'code'):
        "Programme wide code from a controlled vocabulary (e.g. N2O).",
    (designing.ForcingConstraint, 'origin'):
        "Pointer to origin, e.g. CMIP6 RCP database.",
    (designing.ForcingConstraint, 'data_link'):
        "Link to actual data record if possible.",
    (designing.ForcingConstraint, 'additional_constraint'):
        "Additional information, e.g. hold constant from 2100-01-01.",
    (designing.ForcingConstraint, 'forcing_type'):
        "Type of integration.",
    (designing.ForcingConstraint, 'category'):
        "Category to which this belongs (from a CV, e.g. GASES).",
    (software.DevelopmentPath, 'funding_sources'):
        "The entities that funded this software component.",
    (software.DevelopmentPath, 'previous_version'):
        "Name of a previous version.",
    (software.DevelopmentPath, 'consortium_name'):
        "If model/component is developed as part of a consortium, provide consortium name.",
    (software.DevelopmentPath, 'developed_in_house'):
        "Model or component was mostly developed in house.",
    (software.DevelopmentPath, 'creators'):
        "Those responsible for creating this component.",
    (software.Composition, 'couplings'):
        "#FIXME.",
    (software.Composition, 'description'):
        "#FIXME.",
    (software.SoftwareComponent, 'language'):
        "Language the component is written in.",
    (software.SoftwareComponent, 'connection_points'):
        "The set of data entities which are available for I/O and/or coupling.",
    (software.SoftwareComponent, 'coupling_framework'):
        "The coupling framework that this entire component conforms to.",
    (software.SoftwareComponent, 'license'):
        "The license held by this piece of software.",
    (software.SoftwareComponent, 'dependencies'):
        "#FIXME.",
    (software.SoftwareComponent, 'sub_components'):
        "Internal software sub-components of this component.",
    (software.SoftwareComponent, 'grid'):
        "A reference to the grid that is used by this component.",
    (software.SoftwareComponent, 'composition'):
        "#FIXME.",
    (software.Variable, 'prognostic'):
        "Whether or not prognostic or diagnostic.",
    (software.Variable, 'description'):
        "Description of how the variable is being used in the s/w.",
    (software.Variable, 'name'):
        "Short name for the variable.",
    (software.EntryPoint, 'name'):
        "#FIXME.",
    (software.ComponentBase, 'documentation'):
        "Descriptions of the component functionality.",
    (software.ComponentBase, 'repository'):
        "Location of code for this component.",
    (software.ComponentBase, 'development_history'):
        "History of the development of this component.",
    (software.ComponentBase, 'version'):
        "Version identifier.",
    (software.ComponentBase, 'name'):
        "Short name of component.",
    (software.ComponentBase, 'description'):
        "Textural description of component.",
    (software.ComponentBase, 'release_date'):
        "The date of publication of the component code (as opposed to the date of publication of the metadata document, or the date of deployment of the model).",
    (software.ComponentBase, 'long_name'):
        "Long name for component.",
    (software.Gridspec, 'description'):
        "Textural description.",
    (shared.IrregularDateset, 'date_set'):
        "Set of dates, comma separated yyyy-mm-dd.",
    (shared.NumberArray, 'values'):
        "A space separated list of numbers.",
    (shared.Calendar, 'description'):
        "Extra information about the calendar.",
    (shared.Calendar, 'standard_name'):
        "Type of calendar used.",
    (shared.Calendar, 'name'):
        "Can be used to name a special calendar type.",
    (shared.Calendar, 'month_lengths'):
        "Used for special calendars to provide month lengths.",
    (shared.DocReference, 'id'):
        "Identifier of remote resource, if known.",
    (shared.DocReference, 'relationship'):
        "Predicate - relationship of the object target as seen from the subject resource.",
    (shared.DocReference, 'context'):
        "Information about remote record in context of reference.",
    (shared.DocReference, 'constraint_vocabulary'):
        "A constraint vocabulary for the relationship.",
    (shared.DocReference, 'version'):
        "The version of the remote record.",
    (shared.DocReference, 'type'):
        "The type of the remote record.",
    (shared.Reference, 'context'):
        "Brief text description of why this resource is being cited.",
    (shared.Reference, 'document'):
        "Reference Target.",
    (shared.Pid, 'id'):
        "The identifier.",
    (shared.Pid, 'resolution_service'):
        "The resolution service.",
    (shared.DatetimeSet, 'length'):
        "Number of times in set.",
    (shared.Party, 'organisation'):
        "True if an organisation not a person.",
    (shared.Party, 'email'):
        "Email address.",
    (shared.Party, 'meta'):
        "Provides a unique identifier for the party.",
    (shared.Party, 'name'):
        "Name of person or organisation.",
    (shared.Party, 'orcid_id'):
        "Orcid ID if available.",
    (shared.Party, 'address'):
        "Institutional address.",
    (shared.Party, 'url'):
        "URL of person or institution.",
    (shared.QualityReview, 'date'):
        "Date upon which review was made.",
    (shared.QualityReview, 'quality_status'):
        "Status from a controlled vocabulary.",
    (shared.QualityReview, 'quality_description'):
        "Assessment of quality of this document.",
    (shared.QualityReview, 'metadata_reviewer'):
        "Party who made the metadata quality assessment.",
    (shared.TimesliceList, 'members'):
        "Values as integers.",
    (shared.TimesliceList, 'units'):
        "Interval against which members refer.",
    (shared.DateTime, 'offset'):
        "Date is offset from start of an integration.",
    (shared.DateTime, 'value'):
        "Date or time - some of (from left to right): yyyy-mm-dd:hh:mm:ss.",
    (shared.TimePeriod, 'calendar'):
        "Calendar, default is standard aka gregorian.",
    (shared.TimePeriod, 'date_type'):
        "Describes how the date is used to define the period.",
    (shared.TimePeriod, 'length'):
        "Duration of the time period.",
    (shared.TimePeriod, 'units'):
        "Appropriate time units.",
    (shared.TimePeriod, 'date'):
        "Optional start/end date of time period.",
    (shared.RegularTimeset, 'start_date'):
        "Beginning of time set.",
    (shared.RegularTimeset, 'increment'):
        "Interval between members of set.",
    (shared.RegularTimeset, 'length'):
        "Number of times in set.",
    (shared.DocMetaInfo, 'id'):
        "Universal document identifier (normally a UUID).",
    (shared.DocMetaInfo, 'source'):
        "Name of application that created the instance.",
    (shared.DocMetaInfo, 'project'):
        "Name of project with which instance is associated with.",
    (shared.DocMetaInfo, 'update_date'):
        "Date upon which the instance was last updated.",
    (shared.DocMetaInfo, 'create_date'):
        "Date upon which the instance was created.",
    (shared.DocMetaInfo, 'drs_keys'):
        "DRS related keys to support correlation of documents with datasets.",
    (shared.DocMetaInfo, 'institute'):
        "Name of institute with which instance is associated with.",
    (shared.DocMetaInfo, 'type'):
        "Document ontology type.",
    (shared.DocMetaInfo, 'drs_path'):
        "DRS related path to support documents with datasets.",
    (shared.DocMetaInfo, 'sort_key'):
        "Document sort key.",
    (shared.DocMetaInfo, 'type_display_name'):
        "Document type display name.",
    (shared.DocMetaInfo, 'type_sort_key'):
        "Document type sort key.",
    (shared.DocMetaInfo, 'version'):
        "Document version identifier.",
    (shared.DocMetaInfo, 'external_ids'):
        "Set of identifiers used to reference the document by external parties.",
    (shared.DocMetaInfo, 'author'):
        "Author of the metadata in the parent document.",
    (shared.DocMetaInfo, 'language'):
        "Language with which instance is associated with.",
    (shared.DocMetaInfo, 'source_key'):
        "Key of application that created the instance.",
    (shared.KeyFloat, 'key'):
        "User defined key.",
    (shared.KeyFloat, 'value'):
        "Value associated with a key (real number).",
    (shared.OnlineResource, 'linkage'):
        "A URL.",
    (shared.OnlineResource, 'protocol'):
        "Protocol to use at the linkage.",
    (shared.OnlineResource, 'description'):
        "Detail of how to access the resource.",
    (shared.OnlineResource, 'name'):
        "Name of online resource.",
    (shared.Responsibility, 'party'):
        "Parties delivering responsibility.",
    (shared.Responsibility, 'when'):
        "Period when role was active, if no longer.",
    (shared.Responsibility, 'role'):
        "Role that the party plays or played.",
    (shared.ExternalDocument, 'doi'):
        "Digital Object Identifier, if it exists.",
    (shared.ExternalDocument, 'title'):
        "Title or name of the document.",
    (shared.ExternalDocument, 'meta'):
        "Metadata about the creation of this document description.",
    (shared.ExternalDocument, 'date'):
        "Date of publication, or of access in the case of a URL.",
    (shared.ExternalDocument, 'name'):
        "A name for the citation: short hand description, e.g. Meehl et al (2014).",
    (shared.ExternalDocument, 'publication_detail'):
        "Journal/publisher, page and volume information as appropriate.",
    (shared.ExternalDocument, 'online_at'):
        "Location of electronic version.",
    (shared.ExternalDocument, 'authorship'):
        "List of authors expressed using an appropriate syntax.",
    (shared.Cimtext, 'content'):
        "Raw content (including markup).",
    (shared.Cimtext, 'content_type'):
        "Type of content.",
    (science.Extent, 'northern_boundary'):
        "If not global, northern boundary in degrees of latitude.",
    (science.Extent, 'eastern_boundary'):
        "If not global, eastern boundary in degrees of longitude.",
    (science.Extent, 'bottom_vertical_level'):
        "Bottom vertical level centre (e.g. level near land surface or level ocean floor).",
    (science.Extent, 'western_boundary'):
        "If not global, western boundary in degrees of longitude.",
    (science.Extent, 'southern_boundary'):
        "If not global, southern boundary in degrees of latitude.",
    (science.Extent, 'region_known_as'):
        "Identifier or identifiers for the region covered by the extent.",
    (science.Extent, 'is_global'):
        "True if horizontal coverage is global.",
    (science.Extent, 'top_vertical_level'):
        "Top vertical level centre (e.g. level at TOA or level near ocean surface).",
    (science.Extent, 'z_units'):
        "Units of vertical measure (e.g. m, Pa, sigma_level.",
    (science.ScientificDomain, 'meta'):
        "Metadata describing the construction of this domain description.",
    (science.ScientificDomain, 'simulates'):
        "Processes simulated within the domain.",
    (science.ScientificDomain, 'name'):
        "Name of the scientific domain (e.g. ocean).",
    (science.ScientificDomain, 'id'):
        "Vocabulary identifier, where this domain description was constructed via a  controlled vocabulary.",
    (science.ScientificDomain, 'overview'):
        "Free text overview description of key properties of domain.",
    (science.ScientificDomain, 'references'):
        "Any relevant references describing the implementation of this domain in a relevant model.",
    (science.ScientificDomain, 'realm'):
        "Canonical name for the domain of this scientific area.",
    (science.ScientificDomain, 'differing_key_properties'):
        "Key properties for the domain which differ from model defaults (grid, timestep etc).",
    (science.Tuning, 'description'):
        "Brief description of tuning methodology. Include information about observational period(s) used.",
    (science.Tuning, 'trend_metrics_used'):
        "Which observed trend metrics have been used in tuning model parameters.",
    (science.Tuning, 'regional_metrics_used'):
        "Which regional metrics of mean state (e.g Monsoons, tropical means etc) have been used in tuning.",
    (science.Tuning, 'global_mean_metrics_used'):
        "Set of metrics of the global mean state used in tuning model parameters.",
    (science.Process, 'keywords'):
        "keywords to help re-use and discovery of this information.",
    (science.Process, 'properties'):
        "Sets of properties for this process.",
    (science.Process, 'algorithms'):
        "Descriptions of algorithms and their properties used in the process.",
    (science.Process, 'references'):
        "Any relevant references describing this process and/or it's implementation.",
    (science.Process, 'implementation_overview'):
        "General overview description of the implementation of this process.",
    (science.Process, 'sub_processes'):
        "Discrete portion of a process with common process details.",
    (science.SubProcess, 'implementation_overview'):
        "General overview description of the implementation of this part of the process.",
    (science.SubProcess, 'references'):
        "Any relevant references describing this part of the process and/or it's implementation.",
    (science.SubProcess, 'properties'):
        "Sets of properties for this process.",
    (science.ScienceContext, 'context'):
        "Scientific context for which this description is provided.",
    (science.ScienceContext, 'name'):
        "The name of this process/algorithm/sub-process/detail.",
    (science.ScienceContext, 'id'):
        "Identifier for this collection of properties.",
    (science.Algorithm, 'implementation_overview'):
        "Overview of the algorithm implementation.",
    (science.Algorithm, 'prognostic_variables'):
        "Prognostic variables associated with this algorithm.",
    (science.Algorithm, 'diagnostic_variables'):
        "Diagnostic variables associated with this algorithm.",
    (science.Algorithm, 'references'):
        "Relevant references.",
    (science.Algorithm, 'forced_variables'):
        "Variables held constant within algorithm.",
    (science.Grid, 'name'):
        "This is a string usually used by the modelling group to describe the grid.(e.g. the ENDGAME/New Dynamics dynamical cores have their own grids describing variable layouts.",
    (science.Grid, 'horizontal_grid_layout'):
        "Type of horizontal grid-layout (e.g. Arakawa C-Grid.",
    (science.Grid, 'vertical_grid_layout'):
        "Type of vertical grid-layout (e.g. Charney-Phillips.",
    (science.Grid, 'horizontal_grid_type'):
        "Description of basic horizontal grid (e.g. 'cubed-sphere').",
    (science.Grid, 'additional_details'):
        "Additional grid properties.",
    (science.Grid, 'vertical_grid_type'):
        "Description of basic vertical grid (e.g. 'atmosphere_hybrid_height_coordinate').",
    (science.Grid, 'meta'):
        "Metadata about how the model description was constructed.",
    (science.Grid, 'grid_extent'):
        "Key geographic characteristics of the grid use to simulate a specific domain.",
    (science.Resolution, 'typical_x_degrees'):
        "Horizontal X resolution in degrees of grid cells, if applicable eg. 3.75.",
    (science.Resolution, 'name'):
        "This is a string usually used by the modelling group to describe the resolution of this grid,  e.g. N512L180 or T512L70 etc.",
    (science.Resolution, 'equivalent_resolution_km'):
        "Resolution in km of 'typical grid cell' (at the equator, for gross comparisons of resolution), eg. 50.",
    (science.Resolution, 'number_of_levels'):
        "Number of vertical levels resolved.",
    (science.Resolution, 'typical_y_degrees'):
        "Horizontal Y resolution in degrees of grid cells, if applicable eg. 2.5.",
    (science.Resolution, 'number_of_xy_gridpoints'):
        "Total number of horizontal points on computational grids.",
    (science.Resolution, 'is_adaptive_grid'):
        "Default is False. Set true if grid resolution changes during execution.",
    (science.Model, 'meta'):
        "Metadata about how the model description was constructed.",
    (science.Model, 'coupled_components'):
        "Software components which are linked together using a coupler to deliver this model.",
    (science.Model, 'coupler'):
        "Overarching coupling framework for model.",
    (science.Model, 'simulates'):
        "The scientific domains which this model simulates.",
    (science.Model, 'id'):
        "Vocabulary identifier, where this model description was constructed via a controlled vocabulary.",
    (science.Model, 'internal_software_components'):
        "Software modules which together provide the functionality for this model.",
    (science.Model, 'category'):
        "Generic type for this model.",
    (science.Model, 'model_default_properties'):
        "Model default key properties (may be over-ridden in domain properties).",
    (science.KeyProperties, 'time_step'):
        "Timestep (in seconds) of overall component.",
    (science.KeyProperties, 'tuning_applied'):
        "Describe any tuning used to optimise the parameters in this domain.",
    (science.KeyProperties, 'grid'):
        "The grid used to layout the variables (e.g. the Global ENDGAME-grid).",
    (science.KeyProperties, 'resolution'):
        "The resolution of the grid (e.g. N512L180).",
    (science.KeyProperties, 'additional_detail'):
        "Additional property details.",
    (science.KeyProperties, 'extra_conservation_properties'):
        "Details of methodology needed to conserve variables between processes.",
    (science.Detail, 'content'):
        "Free text description of process detail (if required).",
    (science.Detail, 'from_vocab'):
        "Name of an enumeration vocabulary of possible detail options.",
    (science.Detail, 'select'):
        "Name of property to be selected from vocab.",
    (science.Detail, 'with_cardinality'):
        "Required cardinality of selection from vocabulary.",
    (science.Detail, 'detail_selection'):
        "List of choices from the vocabulary of possible detailed options.",
    (science.ConservationProperties, 'corrected_conserved_prognostic_variables'):
        "Set of variables which are conserved by *more* than the numerical scheme alone.",
    (science.ConservationProperties, 'flux_correction_was_used'):
        "Flag to indicate if correction involved flux correction.",
    (science.ConservationProperties, 'correction_methodology'):
        "Description of method by which correction was achieved.",
    (platform.StoragePool, 'description'):
        "Description of the technology used.",
    (platform.StoragePool, 'type'):
        "Type of storage.",
    (platform.StoragePool, 'vendor'):
        "Vendor of the storage unit.",
    (platform.StoragePool, 'volume_available'):
        "Storage capacity.",
    (platform.StoragePool, 'name'):
        "Name of storage pool.",
    (platform.ComputePool, 'number_of_nodes'):
        "Number of nodes.",
    (platform.ComputePool, 'compute_cores_per_node'):
        "Number of CPU cores per node.",
    (platform.ComputePool, 'memory_per_node'):
        "Memory per node.",
    (platform.ComputePool, 'cpu_type'):
        "CPU type.",
    (platform.ComputePool, 'accelerators_per_node'):
        "Number of accelerator units on a node.",
    (platform.ComputePool, 'model_number'):
        "Model/Board number/type.",
    (platform.ComputePool, 'accelerator_type'):
        "Type of accelerator.",
    (platform.ComputePool, 'operating_system'):
        "Operating system.",
    (platform.ComputePool, 'name'):
        "Name of compute pool within a machine.",
    (platform.ComputePool, 'interconnect'):
        "Interconnect used.",
    (platform.ComputePool, 'description'):
        "Textural description of pool.",
    (platform.Machine, 'meta'):
        "Document description.",
    (platform.Partition, 'online_documentation'):
        "Links to documentation.",
    (platform.Partition, 'partition'):
        "If machine is partitioned, treat subpartitions as machines.",
    (platform.Partition, 'institution'):
        "Institutional location.",
    (platform.Partition, 'compute_pools'):
        "Layout of compute nodes.",
    (platform.Partition, 'model_number'):
        "Vendor's model number/name - if it exists.",
    (platform.Partition, 'storage_pools'):
        "Storage resource available.",
    (platform.Partition, 'when_used'):
        "If no longer in use, the time period it was in use.",
    (platform.Partition, 'name'):
        "Name of partition (or machine).",
    (platform.Partition, 'vendor'):
        "The system integrator or vendor.",
    (platform.Partition, 'description'):
        "Textural description of machine.",
    (platform.ComponentPerformance, 'cores_used'):
        "Number of cores used for this component.",
    (platform.ComponentPerformance, 'nodes_used'):
        "Number of nodes used for this component.",
    (platform.ComponentPerformance, 'speed'):
        "Time taken to simulate one real day (s).",
    (platform.ComponentPerformance, 'component'):
        "Link to a CIM software component description.",
    (platform.ComponentPerformance, 'component_name'):
        "Short name of component.",
    (platform.Performance, 'asypd'):
        "Actual simulated years per wall-clock day, all-in.",
    (platform.Performance, 'memory_bloat'):
        "Percentage of extra memory needed.",
    (platform.Performance, 'sypd'):
        "Simulated years per wall-clock day.",
    (platform.Performance, 'platform'):
        "Platform on which performance was tested.",
    (platform.Performance, 'load_imbalance'):
        "Load imbalance.",
    (platform.Performance, 'name'):
        "Short name for performance (experiment/test/whatever).",
    (platform.Performance, 'chsy'):
        "Core-Hours per simulated year.",
    (platform.Performance, 'total_nodes_used'):
        "Number of nodes used.",
    (platform.Performance, 'compiler'):
        "Compiler used.",
    (platform.Performance, 'meta'):
        "Document metadata.",
    (platform.Performance, 'subcomponent_performance'):
        "Describes the performance of each subcomponent.",
    (platform.Performance, 'coupler_load'):
        "Percentage of time spent in coupler.",
    (platform.Performance, 'model'):
        "Model for which performance was tested.",
    (platform.Performance, 'io_load'):
        "Percentage of time spent in I/O.",
    (platform.StorageVolume, 'units'):
        "Volume units.",
    (platform.StorageVolume, 'volume'):
        "Numeric value.",
    (data.VariableCollection, 'collection_name'):
        "Name for this variable collection.",
    (data.VariableCollection, 'variables'):
        "Set of variable names.",
    (data.Simulation, 'calendar'):
        "The calendar used in the simulation.",
    (data.Simulation, 'primary_ensemble'):
        "Primary Ensemble (ensemble for which this simulation was first run).",
    (data.Simulation, 'ran_for_experiments'):
        "One or more experiments with which the simulation is associated.",
    (data.Simulation, 'parent_simulation'):
        "If appropriate, detailed information about how this simulation branched from a previous one.",
    (data.Simulation, 'used'):
        "The model used to run the simulation.",
    (data.Simulation, 'ensemble_identifier'):
        "String that can be used to extract ensemble axis membership from the primary ensemble(e.g. cmip6 rip string as in the DRS).",
    (data.Simulation, 'part_of_project'):
        "Project or projects for which simulation was run.",
    (data.Dataset, 'meta'):
        "Metadata describing the creation of this dataset description document.",
    (data.Dataset, 'responsible_parties'):
        "Individuals and organisations reponsible for the data.",
    (data.Dataset, 'availability'):
        "Where the data is located, and how it is accessed.",
    (data.Dataset, 'name'):
        "Name of dataset.",
    (data.Dataset, 'description'):
        "Textural description of dataset.",
    (data.Dataset, 'produced_by'):
        "Makes a link back to originating activity.",
    (data.Dataset, 'related_to_dataset'):
        "Related dataset.",
    (data.Dataset, 'drs_datasets'):
        "Data available in the DRS.",
    (data.Dataset, 'references'):
        "Relevant reference document.",
    (data.Downscaling, 'downscaled_from'):
        "The simulation that was downscaled by this downscaling activity.",
    (activity.Activity, 'name'):
        "Short name or abbreviation.",
    (activity.Activity, 'references'):
        "Relevant documentation.",
    (activity.Activity, 'canonical_name'):
        "Community defined identifier or name.",
    (activity.Activity, 'meta'):
        "Metadata describing how this document was created.",
    (activity.Activity, 'description'):
        "Description of what is to be done (or was done).",
    (activity.Activity, 'rationale'):
        "Explanation of why this activity was carried out and/or what it was intended to achieve.",
    (activity.Activity, 'responsible_parties'):
        "People or organisations responsible for activity.",
    (activity.Activity, 'duration'):
        "Time the activity was (or will be) active.",
    (activity.Activity, 'keywords'):
        "User defined keywords.",
    (activity.Activity, 'long_name'):
        "Longer version of activity name.",
    (activity.Conformance, 'target_requirement'):
        "URI of the target numerical requirement.",
    (activity.Ensemble, 'has_ensemble_axes'):
        "Set of axes for the ensemble.",
    (activity.Ensemble, 'members'):
        "The set of ensemble members.",
    (activity.Ensemble, 'common_conformances'):
        "Conformance documents for requirements common across ensemble.",
    (activity.Ensemble, 'part_of'):
        "Link to one or more over-arching ensembles that might includes this one.",
    (activity.Ensemble, 'documentation'):
        "Links to web-pages and other ensemble specific documentation (including workflow descriptions).",
    (activity.Ensemble, 'supported'):
        "Experiments with which the ensemble is associated (may differ from constituent simulations).",
    (activity.UberEnsemble, 'child_ensembles'):
        "Ensemble which are aggregated into this one.",
    (activity.EnsembleMember, 'ran_on'):
        "The machine on which the simulation was run.",
    (activity.EnsembleMember, 'variant_id'):
        "A string which concatenates axis member short identiers (e.g r1i1p1f1).",
    (activity.EnsembleMember, 'simulation'):
        "Actual simulation description for an ensemble member.",
    (activity.EnsembleMember, 'errata'):
        "Link to errata associated with this simulation.",
    (activity.EnsembleMember, 'had_performance'):
        "Performance of the simulation.",
    (activity.ParentSimulation, 'branch_time_in_child'):
        "The time at which the present simulation started in the child calendar.",
    (activity.ParentSimulation, 'parent'):
        "The parent simulation of this child.",
    (activity.ParentSimulation, 'branch_time_in_parent'):
        "The time in parent simulation calendar at which this simulation was branched.",
    (activity.AxisMember, 'index'):
        "The ensemble member index.",
    (activity.AxisMember, 'description'):
        "Description of the member (or name of parameter varied).",
    (activity.AxisMember, 'value'):
        "If parameter varied, value thereof for this member.",
    (activity.AxisMember, 'extra_detail'):
        "If necessary: further information about ensemble member conformance.",
    (activity.EnsembleAxis, 'short_identifier'):
        "e.g. 'r' or 'i' or 'p' to conform with simulation ensemble variant identifiers.",
    (activity.EnsembleAxis, 'extra_detail'):
        "Any extra detail required to describe how this ensemble axis was delivered.",
    (activity.EnsembleAxis, 'target_requirement'):
        "URI of the target numerical requirement.",
    (activity.EnsembleAxis, 'member'):
        "Individual member descriptions along axis.",

    # ------------------------------------------------
    # Enums.
    # ------------------------------------------------

    drs.DrsRealms: """
        Set of allowed DRS modelling realms.

    """,
    drs.DrsTimeSuffixes: """
        Set of permitted time averaging suffixes for drs temporal identifiers.

    """,
    drs.DrsFrequencyTypes: """
        Set of allowed DRS frequency types.

    """,
    drs.DrsGeographicalOperators: """
        Set of permitted spatial averaging operator suffixes for drs spatial indicators (yyyy-zzzz).

    """,
    designing.EnsembleTypes: """
        Defines the various axes along which one can set up an ensemble.

    """,
    designing.ExperimentalRelationships: """
        Defines the canonical set of experimental relationships.

    """,
    designing.ForcingTypes: """
        Defines the possible set of forcing types for a forcing constraint.

    """,
    software.CouplingFramework: """
        The set of terms which define known coupling frameworks.

    """,
    software.ProgrammingLanguage: """
        The set of terms which define programming languages used for earth
    system simulation.

    """,
    shared.TextCode: """
        Types of text understood by the CIM notebook. Currently only
    plaintext, but we expect safe HTML to be supported as soon as practicable.

    """,
    shared.NilReason: """
        Provides an enumeration of possible reasons why a property has not been defined
    Based on GML nilReason as discussed here: https://www.seegrid.csiro.au/wiki/AppSchemas/NilValues.

    """,
    shared.RoleCode: """
        Responsibility role codes: roles that a party may play in delivering a responsibility.

    """,
    shared.SlicetimeUnits: """
        Units for integers in a timeslice.

    """,
    shared.CalendarTypes: """
        CF calendar types as defined in CF 1.6.

    """,
    shared.PeriodDateTypes: """
        A period date type enum (used by time_period).

    """,
    shared.DocumentTypes: """
        The complete set of CIM document types, that is, all classes which carry the
    document metadata attributes.

    """,
    shared.TimeUnits: """
        Appropriate Time units for experiment durations in NWP and Climate Modelling.

    """,
    shared.QualityStatus: """
        Assertion as to the review status of document.

    """,
    science.ModelTypes: """
        Defines a set of gross model classes.

    """,
    science.SelectionCardinality: """
        Provides the possible cardinalities for selecting from a controlled vocabulary.

    """,
    platform.StorageSystems: """
        Controlled vocabulary for storage  types (including filesystems).

    """,
    platform.VolumeUnits: """
        Appropriate storage volume units.

    """,
    data.DataAssociationTypes: """
        Set of possible dataset associations.
    Selected from, and extended from,  ISO19115 (2014) DS_AssociationTypeCode.

    """,
    activity.EnsembleTypes: """
        Defines the various axes along which one can set up an ensemble.

    """,
    activity.ForcingTypes: """
        Defines the possible set of forcing types for a forcing constraint.

    """,

    # ------------------------------------------------
    # Enum members.
    # ------------------------------------------------

    (drs.DrsRealms, 'aerosol'):
        "Aerosol",
    (drs.DrsRealms, 'atmosChem'):
        "Atmospheric Chemistry",
    (drs.DrsRealms, 'ocnBgchem'):
        "Ocean Biogeochemistry",
    (drs.DrsRealms, 'atmos'):
        "Atmosphere",
    (drs.DrsRealms, 'ocean'):
        "Ocean",
    (drs.DrsRealms, 'land'):
        "Land",
    (drs.DrsRealms, 'landIce'):
        "Land Ice",
    (drs.DrsRealms, 'seaIce'):
        "Sea Ice",
    (drs.DrsTimeSuffixes, 'clim'):
        "Indicates data is climatological average data at the DRS frequency from the period N1-N2",
    (drs.DrsTimeSuffixes, 'avg'):
        "Indicates data is a single average of DRS frequency data across temporal period N1-N2",
    (drs.DrsFrequencyTypes, '3hr'):
        "Every three hours",
    (drs.DrsFrequencyTypes, 'subhr'):
        "Sampling frequency less than an hour",
    (drs.DrsFrequencyTypes, 'monClim'):
        "Climatological Monthly Mean",
    (drs.DrsFrequencyTypes, 'fx'):
        "Fixed Time independent",
    (drs.DrsFrequencyTypes, 'yr'):
        "Yearly",
    (drs.DrsFrequencyTypes, 'mon'):
        "Monthly",
    (drs.DrsFrequencyTypes, 'day'):
        "Daily",
    (drs.DrsFrequencyTypes, '6hr'):
        "Every six hours",
    (drs.DrsGeographicalOperators, 'zonalavg'):
        "Data is zonally averaged",
    (drs.DrsGeographicalOperators, 'lnd-zonalavg'):
        "Data is zonally averaged over land in region",
    (drs.DrsGeographicalOperators, 'ocn-zonalavg'):
        "Data is zonally averaged over oceans in region",
    (drs.DrsGeographicalOperators, 'areaavg'):
        "Data is averaged over the area of the region",
    (drs.DrsGeographicalOperators, 'lnd-areaavg'):
        "Data is averaged over the land area of the region",
    (drs.DrsGeographicalOperators, 'ocn-areaavg'):
        "Data is averaged over the ocean area of the region",
    (designing.EnsembleTypes, 'Initialisation Method'):
        "Members differ in how they are initialised",
    (designing.EnsembleTypes, 'Initialisation'):
        "Members are initialised to sample possible starting states",
    (designing.EnsembleTypes, 'Staggered Start'):
        "Members are initialised at different starting dates",
    (designing.EnsembleTypes, 'Forced'):
        "Members used differing forcing data",
    (designing.EnsembleTypes, 'Resolution'):
        "Members are run at different resolutions",
    (designing.EnsembleTypes, 'Perturbed Physics'):
        "Members differ in some aspects of their physics",
    (designing.ExperimentalRelationships, 'control_for'):
        "This experiment provides a control for the target experiment",
    (designing.ExperimentalRelationships, 'provides_constraints'):
        "This experiment provides constraint(s) for the target experiment (e.g SST forcing)",
    (designing.ExperimentalRelationships, 'initialisation_for'):
        "This experiment provides initialisation for the target experiment",
    (designing.ExperimentalRelationships, 'is_sibling'):
        "Part of a family (e.g. experiments where solar forcing is either increased or reduced)",
    (designing.ForcingTypes, 'historical'):
        "Best estimates of actual state (included synthesized)",
    (designing.ForcingTypes, 'scenario'):
        "Intended to represent a possible future, e.g. RCP4.5",
    (designing.ForcingTypes, 'another simulation'):
        "From another simulation",
    (designing.ForcingTypes, 'idealised'):
        "Simplified and/or exemplar, e.g. 1%C02",
    (software.CouplingFramework, 'Bespoke'):
        "Customised coupler developed for this model",
    (software.CouplingFramework, 'Unknown'):
        "It is not known what/if-a coupler is used",
    (software.CouplingFramework, 'None'):
        "No coupler is used",
    (software.CouplingFramework, 'OASIS'):
        None,
    (software.CouplingFramework, 'OASIS3-MCT'):
        None,
    (software.CouplingFramework, 'ESMF'):
        None,
    (software.CouplingFramework, 'NUOPC'):
        None,
    (software.ProgrammingLanguage, 'Python'):
        None,
    (software.ProgrammingLanguage, 'C++'):
        None,
    (software.ProgrammingLanguage, 'C'):
        None,
    (software.ProgrammingLanguage, 'Fortran'):
        None,
    (shared.TextCode, 'plaintext'):
        "Normal plain text",
    (shared.NilReason, 'nil:missing'):
        "The correct value is not available. Furthermore, a correct value may not exist",
    (shared.NilReason, 'nil:unknown'):
        "The correct value is not known at this time. However, a correct value probably exists",
    (shared.NilReason, 'nil:inapplicable'):
        "There is no value",
    (shared.NilReason, 'nil:withheld'):
        "The value is not divulged",
    (shared.NilReason, 'nil:template'):
        "The value will be available later",
    (shared.RoleCode, 'custodian'):
        "Party that accepts accountability and responsibility for the source resource",
    (shared.RoleCode, 'metadata_reviewer'):
        "Party who carried out an independent review of (this) documentation",
    (shared.RoleCode, 'publisher'):
        "Party who published the resource",
    (shared.RoleCode, 'metadata_author'):
        "Party who created (this) documentation",
    (shared.RoleCode, 'distributor'):
        "Party who distributes the resource",
    (shared.RoleCode, 'processor'):
        "Party who has taken part in the workflow that resulted in this resource",
    (shared.RoleCode, 'resource provider'):
        "Party that supplies the resource",
    (shared.RoleCode, 'Principal Investigator'):
        "Key party responsible for the existence of the resource",
    (shared.RoleCode, 'originator'):
        "Original source for the resource if obtained from elsewhere",
    (shared.RoleCode, 'user'):
        "Party who uses the resource",
    (shared.RoleCode, 'point of contact'):
        "Party who can be contacted for acquiring knowledge about or acquisition of the resource",
    (shared.RoleCode, 'author'):
        "Party who created (or co-created) resource",
    (shared.RoleCode, 'collaborator'):
        "Contributor to the production of the resource",
    (shared.RoleCode, 'sponsor'):
        "Party who has invested in the production of the resource",
    (shared.RoleCode, 'owner'):
        "Party with legal ownership of the resource",
    (shared.SlicetimeUnits, 'yearly'):
        None,
    (shared.SlicetimeUnits, 'monthly'):
        None,
    (shared.CalendarTypes, 'noleap'):
        "Gregorian calendar without leap years, i.e., all years are 365 days long.",
    (shared.CalendarTypes, '365_day'):
        "Synonym for noleap:Gregorian calendar without leap years, i.e., all years are 365 days long.",
    (shared.CalendarTypes, 'all_leap'):
        "Gregorian calendar with every year being a leap year, i.e., all years are 366 days long.",
    (shared.CalendarTypes, '366_day'):
        "Synonym for all_leap:Gregorian calendar with every year being a leap year, i.e., all years are 366 days long.",
    (shared.CalendarTypes, '360_day'):
        "All years are 360 days divided into 30 day months.",
    (shared.CalendarTypes, 'julian'):
        "Julian Calendar",
    (shared.CalendarTypes, 'standard'):
        "Synonym for gregorian: Mixed Gregorian/Julian calendar as defined by Udunits",
    (shared.CalendarTypes, 'none'):
        "Perpetual time axis",
    (shared.CalendarTypes, 'proleptic_gregorian'):
        "A Gregorian calendar extended to dates before 1582-10-15. That is, a year is a leap year if either (i) it is divisible by 4 but not by 100 or (ii) it is divisible by 400.",
    (shared.CalendarTypes, 'gregorian'):
        "Mixed Gregorian/Julian calendar as defined by Udunits",
    (shared.PeriodDateTypes, 'date is end'):
        "The date is the end of the period",
    (shared.PeriodDateTypes, 'date is start'):
        "The date defines the start of the period",
    (shared.PeriodDateTypes, 'unused'):
        "Date is not used",
    (shared.DocumentTypes, 'Performance'):
        "A formal set of criteria describing how a model performed on a given machine.",
    (shared.DocumentTypes, 'Project'):
        "An umbrella for a set of numerical experiments (e.g. a MIP)",
    (shared.DocumentTypes, 'ScientificDomain'):
        "A scientifically coherent realm of a numerical model (typically modelled independently).",
    (shared.DocumentTypes, 'Simulation'):
        "A simulation carried out as part of an ensemble for a numerical experiment.",
    (shared.DocumentTypes, 'SimulationPlan'):
        "A plan to carry out a simulations for a numerical experiment.",
    (shared.DocumentTypes, 'TemporalConstraint'):
        "A constraint on the real time simulations need to represent for a numerical experiment.",
    (shared.DocumentTypes, 'UberEnsemble'):
        "An ensemble description that crosses multiple modelling groups.",
    (shared.DocumentTypes, 'Conformance'):
        "Used to hold information about how simulations and ensemble met experimental requirements",
    (shared.DocumentTypes, 'Dataset'):
        "An Atomic Dataset description, that is the minimal set of files with common publication characteristics.",
    (shared.DocumentTypes, 'DomainProperties'):
        "SpatioTemporal domain requirements for a numerical experiment.",
    (shared.DocumentTypes, 'Downscaling'):
        "Description of the techniques and software used to downscale data.",
    (shared.DocumentTypes, 'Ensemble'):
        "Parent  description for set of runs conforming to a numerical experiment.",
    (shared.DocumentTypes, 'EnsembleRequirement'):
        "Description of the ensemble requirements of a numerical experiment.",
    (shared.DocumentTypes, 'ExternalDocument'):
        "A document held outside of es-doc.",
    (shared.DocumentTypes, 'ForcingConstraint'):
        "A constraint on how a model must be forced to meet the requirements of a numerical experiment.",
    (shared.DocumentTypes, 'Grid'):
        "The sampling discretisation used by a model or dataset.",
    (shared.DocumentTypes, 'Machine'):
        "A computer used for numerical experimentation (and/or post-processing).",
    (shared.DocumentTypes, 'Model'):
        "A piece of software used to carry out simulations.",
    (shared.DocumentTypes, 'MultiEnsemble'):
        "An ensemble requirement describing multiple ensemble axes.",
    (shared.DocumentTypes, 'MultiTimeEnsemble'):
        "An ensemble requirement with multple time axes.",
    (shared.DocumentTypes, 'NumericalExperiment'):
        "The scientific description of a numerical experiment",
    (shared.DocumentTypes, 'NumericalRequirement'):
        "A numerical requirement of a numerical experiment.",
    (shared.DocumentTypes, 'OutputTemporalRequirement'):
        "The output requirements for one or more numerical experiments",
    (shared.DocumentTypes, 'Party'):
        "A person or organisation which has a role in the documentation of the simulation workflow",
    (shared.TimeUnits, 'days'):
        None,
    (shared.TimeUnits, 'years'):
        None,
    (shared.TimeUnits, 'months'):
        None,
    (shared.TimeUnits, 'seconds'):
        None,
    (shared.QualityStatus, 'incomplete'):
        "Currently being worked on",
    (shared.QualityStatus, 'finalised'):
        "Author has completed document, prior to review",
    (shared.QualityStatus, 'under_review'):
        "Document is being reviewed",
    (shared.QualityStatus, 'reviewed'):
        "Document has been formally reviewed and assessed as complete and accurate",
    (science.ModelTypes, 'Process'):
        "Limited Area process model",
    (science.ModelTypes, 'Atm Only'):
        "Atmosphere Only",
    (science.ModelTypes, 'Ocean Only'):
        "Ocean Only",
    (science.ModelTypes, 'Regional'):
        "Regional Model",
    (science.ModelTypes, 'GCM'):
        "Global Climate Model (Atmosphere, Ocean, no carbon cycle)",
    (science.ModelTypes, 'IGCM'):
        "Intermediate Complexity GCM",
    (science.ModelTypes, 'GCM-MLO'):
        "GCM with mixed layer ocean",
    (science.ModelTypes, 'Mesoscale'):
        "Mesoscale Model",
    (science.ModelTypes, 'Planetary'):
        "Non-Earth model",
    (science.SelectionCardinality, '1.N'):
        "At least one, and possibly many, selections are required",
    (science.SelectionCardinality, '0.N'):
        "Zero or many selections are permitted",
    (science.SelectionCardinality, '0.1'):
        "Zero or one selections are permitted",
    (science.SelectionCardinality, '1.1'):
        "One and only one selection is required",
    (platform.StorageSystems, 'Panasas'):
        None,
    (platform.StorageSystems, 'Other Disk'):
        None,
    (platform.StorageSystems, 'Tape - Castor'):
        None,
    (platform.StorageSystems, 'Tape - MARS'):
        None,
    (platform.StorageSystems, 'Tape - MASS'):
        None,
    (platform.StorageSystems, 'Lustre'):
        None,
    (platform.StorageSystems, 'GPFS'):
        None,
    (platform.StorageSystems, 'isilon'):
        None,
    (platform.StorageSystems, 'Unknown'):
        None,
    (platform.StorageSystems, 'NFS'):
        None,
    (platform.StorageSystems, 'Tape - Other'):
        None,
    (platform.VolumeUnits, 'TiB'):
        "Tebibytes (1024^4)",
    (platform.VolumeUnits, 'PiB'):
        "Pebibytes (1024^5)",
    (platform.VolumeUnits, 'EiB'):
        "Exbibytes (1024^6)",
    (platform.VolumeUnits, 'GB'):
        "Gigabytes (1000^3)",
    (platform.VolumeUnits, 'TB'):
        "Terabytes (1000^4)",
    (platform.VolumeUnits, 'PB'):
        "Petabytes (1000^5)",
    (platform.VolumeUnits, 'EB'):
        "Exabytes (1000^6)",
    (data.DataAssociationTypes, 'partOf'):
        None,
    (data.DataAssociationTypes, 'isComposedOf'):
        None,
    (data.DataAssociationTypes, 'revisonOf'):
        None,
    (activity.EnsembleTypes, 'Resolution'):
        "Members are run at different resolutions",
    (activity.EnsembleTypes, 'Perturbed Physics'):
        "Members differ in some aspects of their physics",
    (activity.EnsembleTypes, 'Initialisation Method'):
        "Members differ in how they are initialised",
    (activity.EnsembleTypes, 'Initialisation'):
        "Members are initialised to sample possible starting states",
    (activity.EnsembleTypes, 'Staggered Start'):
        "Members are initialised at different starting dates",
    (activity.EnsembleTypes, 'Forced'):
        "Members used differing forcing data",
    (activity.ForcingTypes, 'historical'):
        "Best estimates of actual state (included synthesized)",
    (activity.ForcingTypes, 'scenario'):
        "Intended to represent a possible future, e.g. RCP4.5",
    (activity.ForcingTypes, 'another simulation'):
        "From another simulation",
    (activity.ForcingTypes, 'idealised'):
        "Simplified and/or exemplar, e.g. 1%C02",
}

# ------------------------------------------------
# Type keys.
# ------------------------------------------------

# Map of ontology types to type keys.
KEYS = {
    # ------------------------------------------------
    # Packages.
    # ------------------------------------------------

    drs: "cim.2.drs",
    designing: "cim.2.designing",
    software: "cim.2.software",
    shared: "cim.2.shared",
    science: "cim.2.science",
    platform: "cim.2.platform",
    data: "cim.2.data",
    activity: "cim.2.activity",

    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    drs.DrsAtomicDataset: "cim.2.drs.DrsAtomicDataset",
    drs.DrsPublicationDataset: "cim.2.drs.DrsPublicationDataset",
    drs.DrsEnsembleIdentifier: "cim.2.drs.DrsEnsembleIdentifier",
    drs.DrsTemporalIdentifier: "cim.2.drs.DrsTemporalIdentifier",
    drs.DrsGeographicalIndicator: "cim.2.drs.DrsGeographicalIndicator",
    designing.TemporalConstraint: "cim.2.designing.TemporalConstraint",
    designing.NumericalExperiment: "cim.2.designing.NumericalExperiment",
    designing.MultiTimeEnsemble: "cim.2.designing.MultiTimeEnsemble",
    designing.NumericalRequirement: "cim.2.designing.NumericalRequirement",
    designing.OutputTemporalRequirement: "cim.2.designing.OutputTemporalRequirement",
    designing.EnsembleRequirement: "cim.2.designing.EnsembleRequirement",
    designing.MultiEnsemble: "cim.2.designing.MultiEnsemble",
    designing.Project: "cim.2.designing.Project",
    designing.DomainProperties: "cim.2.designing.DomainProperties",
    designing.SimulationPlan: "cim.2.designing.SimulationPlan",
    designing.ForcingConstraint: "cim.2.designing.ForcingConstraint",
    software.DevelopmentPath: "cim.2.software.DevelopmentPath",
    software.Composition: "cim.2.software.Composition",
    software.SoftwareComponent: "cim.2.software.SoftwareComponent",
    software.Variable: "cim.2.software.Variable",
    software.EntryPoint: "cim.2.software.EntryPoint",
    software.ComponentBase: "cim.2.software.ComponentBase",
    software.Gridspec: "cim.2.software.Gridspec",
    shared.IrregularDateset: "cim.2.shared.IrregularDateset",
    shared.NumberArray: "cim.2.shared.NumberArray",
    shared.Calendar: "cim.2.shared.Calendar",
    shared.DocReference: "cim.2.shared.DocReference",
    shared.Reference: "cim.2.shared.Reference",
    shared.Pid: "cim.2.shared.Pid",
    shared.DatetimeSet: "cim.2.shared.DatetimeSet",
    shared.Party: "cim.2.shared.Party",
    shared.QualityReview: "cim.2.shared.QualityReview",
    shared.TimesliceList: "cim.2.shared.TimesliceList",
    shared.DateTime: "cim.2.shared.DateTime",
    shared.TimePeriod: "cim.2.shared.TimePeriod",
    shared.RegularTimeset: "cim.2.shared.RegularTimeset",
    shared.DocMetaInfo: "cim.2.shared.DocMetaInfo",
    shared.KeyFloat: "cim.2.shared.KeyFloat",
    shared.OnlineResource: "cim.2.shared.OnlineResource",
    shared.Responsibility: "cim.2.shared.Responsibility",
    shared.ExternalDocument: "cim.2.shared.ExternalDocument",
    shared.Cimtext: "cim.2.shared.Cimtext",
    science.Extent: "cim.2.science.Extent",
    science.ScientificDomain: "cim.2.science.ScientificDomain",
    science.Tuning: "cim.2.science.Tuning",
    science.Process: "cim.2.science.Process",
    science.SubProcess: "cim.2.science.SubProcess",
    science.ScienceContext: "cim.2.science.ScienceContext",
    science.Algorithm: "cim.2.science.Algorithm",
    science.Grid: "cim.2.science.Grid",
    science.Resolution: "cim.2.science.Resolution",
    science.Model: "cim.2.science.Model",
    science.KeyProperties: "cim.2.science.KeyProperties",
    science.Detail: "cim.2.science.Detail",
    science.ConservationProperties: "cim.2.science.ConservationProperties",
    platform.StoragePool: "cim.2.platform.StoragePool",
    platform.ComputePool: "cim.2.platform.ComputePool",
    platform.Machine: "cim.2.platform.Machine",
    platform.Partition: "cim.2.platform.Partition",
    platform.ComponentPerformance: "cim.2.platform.ComponentPerformance",
    platform.Performance: "cim.2.platform.Performance",
    platform.StorageVolume: "cim.2.platform.StorageVolume",
    data.VariableCollection: "cim.2.data.VariableCollection",
    data.Simulation: "cim.2.data.Simulation",
    data.Dataset: "cim.2.data.Dataset",
    data.Downscaling: "cim.2.data.Downscaling",
    activity.Activity: "cim.2.activity.Activity",
    activity.Conformance: "cim.2.activity.Conformance",
    activity.Ensemble: "cim.2.activity.Ensemble",
    activity.UberEnsemble: "cim.2.activity.UberEnsemble",
    activity.EnsembleMember: "cim.2.activity.EnsembleMember",
    activity.ParentSimulation: "cim.2.activity.ParentSimulation",
    activity.AxisMember: "cim.2.activity.AxisMember",
    activity.EnsembleAxis: "cim.2.activity.EnsembleAxis",

    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------

    (drs.DrsAtomicDataset, 'geographical_constraint'): "cim.2.drs.DrsAtomicDataset.geographical_constraint",
    (drs.DrsAtomicDataset, 'variable_name'): "cim.2.drs.DrsAtomicDataset.variable_name",
    (drs.DrsAtomicDataset, 'temporal_constraint'): "cim.2.drs.DrsAtomicDataset.temporal_constraint",
    (drs.DrsAtomicDataset, 'ensemble_member'): "cim.2.drs.DrsAtomicDataset.ensemble_member",
    (drs.DrsAtomicDataset, 'mip_table'): "cim.2.drs.DrsAtomicDataset.mip_table",
    (drs.DrsPublicationDataset, 'institute'): "cim.2.drs.DrsPublicationDataset.institute",
    (drs.DrsPublicationDataset, 'model'): "cim.2.drs.DrsPublicationDataset.model",
    (drs.DrsPublicationDataset, 'realm'): "cim.2.drs.DrsPublicationDataset.realm",
    (drs.DrsPublicationDataset, 'activity'): "cim.2.drs.DrsPublicationDataset.activity",
    (drs.DrsPublicationDataset, 'product'): "cim.2.drs.DrsPublicationDataset.product",
    (drs.DrsPublicationDataset, 'version_number'): "cim.2.drs.DrsPublicationDataset.version_number",
    (drs.DrsPublicationDataset, 'frequency'): "cim.2.drs.DrsPublicationDataset.frequency",
    (drs.DrsPublicationDataset, 'experiment'): "cim.2.drs.DrsPublicationDataset.experiment",
    (drs.DrsEnsembleIdentifier, 'realisation_number'): "cim.2.drs.DrsEnsembleIdentifier.realisation_number",
    (drs.DrsEnsembleIdentifier, 'initialisation_method_number'): "cim.2.drs.DrsEnsembleIdentifier.initialisation_method_number",
    (drs.DrsEnsembleIdentifier, 'perturbation_number'): "cim.2.drs.DrsEnsembleIdentifier.perturbation_number",
    (drs.DrsTemporalIdentifier, 'end'): "cim.2.drs.DrsTemporalIdentifier.end",
    (drs.DrsTemporalIdentifier, 'suffix'): "cim.2.drs.DrsTemporalIdentifier.suffix",
    (drs.DrsTemporalIdentifier, 'start'): "cim.2.drs.DrsTemporalIdentifier.start",
    (drs.DrsGeographicalIndicator, 'spatial_domain'): "cim.2.drs.DrsGeographicalIndicator.spatial_domain",
    (drs.DrsGeographicalIndicator, 'bounding_box'): "cim.2.drs.DrsGeographicalIndicator.bounding_box",
    (drs.DrsGeographicalIndicator, 'operator'): "cim.2.drs.DrsGeographicalIndicator.operator",
    (designing.TemporalConstraint, 'start_date'): "cim.2.designing.TemporalConstraint.start_date",
    (designing.TemporalConstraint, 'start_flexibility'): "cim.2.designing.TemporalConstraint.start_flexibility",
    (designing.TemporalConstraint, 'required_calendar'): "cim.2.designing.TemporalConstraint.required_calendar",
    (designing.TemporalConstraint, 'required_duration'): "cim.2.designing.TemporalConstraint.required_duration",
    (designing.NumericalExperiment, 'requirements'): "cim.2.designing.NumericalExperiment.requirements",
    (designing.NumericalExperiment, 'related_experiments'): "cim.2.designing.NumericalExperiment.related_experiments",
    (designing.MultiTimeEnsemble, 'ensemble_members'): "cim.2.designing.MultiTimeEnsemble.ensemble_members",
    (designing.NumericalRequirement, 'conformance_is_requested'): "cim.2.designing.NumericalRequirement.conformance_is_requested",
    (designing.NumericalRequirement, 'additional_requirements'): "cim.2.designing.NumericalRequirement.additional_requirements",
    (designing.OutputTemporalRequirement, 'throughout'): "cim.2.designing.OutputTemporalRequirement.throughout",
    (designing.OutputTemporalRequirement, 'continuous_subset'): "cim.2.designing.OutputTemporalRequirement.continuous_subset",
    (designing.OutputTemporalRequirement, 'sliced_subset'): "cim.2.designing.OutputTemporalRequirement.sliced_subset",
    (designing.EnsembleRequirement, 'ensemble_member'): "cim.2.designing.EnsembleRequirement.ensemble_member",
    (designing.EnsembleRequirement, 'ensemble_type'): "cim.2.designing.EnsembleRequirement.ensemble_type",
    (designing.EnsembleRequirement, 'minimum_size'): "cim.2.designing.EnsembleRequirement.minimum_size",
    (designing.MultiEnsemble, 'ensemble_axis'): "cim.2.designing.MultiEnsemble.ensemble_axis",
    (designing.Project, 'sub_projects'): "cim.2.designing.Project.sub_projects",
    (designing.Project, 'previous_projects'): "cim.2.designing.Project.previous_projects",
    (designing.Project, 'requires_experiments'): "cim.2.designing.Project.requires_experiments",
    (designing.DomainProperties, 'required_extent'): "cim.2.designing.DomainProperties.required_extent",
    (designing.DomainProperties, 'required_resolution'): "cim.2.designing.DomainProperties.required_resolution",
    (designing.SimulationPlan, 'expected_model'): "cim.2.designing.SimulationPlan.expected_model",
    (designing.SimulationPlan, 'expected_platform'): "cim.2.designing.SimulationPlan.expected_platform",
    (designing.SimulationPlan, 'will_support_experiments'): "cim.2.designing.SimulationPlan.will_support_experiments",
    (designing.SimulationPlan, 'expected_performance_sypd'): "cim.2.designing.SimulationPlan.expected_performance_sypd",
    (designing.ForcingConstraint, 'group'): "cim.2.designing.ForcingConstraint.group",
    (designing.ForcingConstraint, 'code'): "cim.2.designing.ForcingConstraint.code",
    (designing.ForcingConstraint, 'origin'): "cim.2.designing.ForcingConstraint.origin",
    (designing.ForcingConstraint, 'data_link'): "cim.2.designing.ForcingConstraint.data_link",
    (designing.ForcingConstraint, 'additional_constraint'): "cim.2.designing.ForcingConstraint.additional_constraint",
    (designing.ForcingConstraint, 'forcing_type'): "cim.2.designing.ForcingConstraint.forcing_type",
    (designing.ForcingConstraint, 'category'): "cim.2.designing.ForcingConstraint.category",
    (software.DevelopmentPath, 'funding_sources'): "cim.2.software.DevelopmentPath.funding_sources",
    (software.DevelopmentPath, 'previous_version'): "cim.2.software.DevelopmentPath.previous_version",
    (software.DevelopmentPath, 'consortium_name'): "cim.2.software.DevelopmentPath.consortium_name",
    (software.DevelopmentPath, 'developed_in_house'): "cim.2.software.DevelopmentPath.developed_in_house",
    (software.DevelopmentPath, 'creators'): "cim.2.software.DevelopmentPath.creators",
    (software.Composition, 'couplings'): "cim.2.software.Composition.couplings",
    (software.Composition, 'description'): "cim.2.software.Composition.description",
    (software.SoftwareComponent, 'language'): "cim.2.software.SoftwareComponent.language",
    (software.SoftwareComponent, 'connection_points'): "cim.2.software.SoftwareComponent.connection_points",
    (software.SoftwareComponent, 'coupling_framework'): "cim.2.software.SoftwareComponent.coupling_framework",
    (software.SoftwareComponent, 'license'): "cim.2.software.SoftwareComponent.license",
    (software.SoftwareComponent, 'dependencies'): "cim.2.software.SoftwareComponent.dependencies",
    (software.SoftwareComponent, 'sub_components'): "cim.2.software.SoftwareComponent.sub_components",
    (software.SoftwareComponent, 'grid'): "cim.2.software.SoftwareComponent.grid",
    (software.SoftwareComponent, 'composition'): "cim.2.software.SoftwareComponent.composition",
    (software.Variable, 'prognostic'): "cim.2.software.Variable.prognostic",
    (software.Variable, 'description'): "cim.2.software.Variable.description",
    (software.Variable, 'name'): "cim.2.software.Variable.name",
    (software.EntryPoint, 'name'): "cim.2.software.EntryPoint.name",
    (software.ComponentBase, 'documentation'): "cim.2.software.ComponentBase.documentation",
    (software.ComponentBase, 'repository'): "cim.2.software.ComponentBase.repository",
    (software.ComponentBase, 'development_history'): "cim.2.software.ComponentBase.development_history",
    (software.ComponentBase, 'version'): "cim.2.software.ComponentBase.version",
    (software.ComponentBase, 'name'): "cim.2.software.ComponentBase.name",
    (software.ComponentBase, 'description'): "cim.2.software.ComponentBase.description",
    (software.ComponentBase, 'release_date'): "cim.2.software.ComponentBase.release_date",
    (software.ComponentBase, 'long_name'): "cim.2.software.ComponentBase.long_name",
    (software.Gridspec, 'description'): "cim.2.software.Gridspec.description",
    (shared.IrregularDateset, 'date_set'): "cim.2.shared.IrregularDateset.date_set",
    (shared.NumberArray, 'values'): "cim.2.shared.NumberArray.values",
    (shared.Calendar, 'description'): "cim.2.shared.Calendar.description",
    (shared.Calendar, 'standard_name'): "cim.2.shared.Calendar.standard_name",
    (shared.Calendar, 'name'): "cim.2.shared.Calendar.name",
    (shared.Calendar, 'month_lengths'): "cim.2.shared.Calendar.month_lengths",
    (shared.DocReference, 'id'): "cim.2.shared.DocReference.id",
    (shared.DocReference, 'relationship'): "cim.2.shared.DocReference.relationship",
    (shared.DocReference, 'context'): "cim.2.shared.DocReference.context",
    (shared.DocReference, 'constraint_vocabulary'): "cim.2.shared.DocReference.constraint_vocabulary",
    (shared.DocReference, 'version'): "cim.2.shared.DocReference.version",
    (shared.DocReference, 'type'): "cim.2.shared.DocReference.type",
    (shared.Reference, 'context'): "cim.2.shared.Reference.context",
    (shared.Reference, 'document'): "cim.2.shared.Reference.document",
    (shared.Pid, 'id'): "cim.2.shared.Pid.id",
    (shared.Pid, 'resolution_service'): "cim.2.shared.Pid.resolution_service",
    (shared.DatetimeSet, 'length'): "cim.2.shared.DatetimeSet.length",
    (shared.Party, 'organisation'): "cim.2.shared.Party.organisation",
    (shared.Party, 'email'): "cim.2.shared.Party.email",
    (shared.Party, 'meta'): "cim.2.shared.Party.meta",
    (shared.Party, 'name'): "cim.2.shared.Party.name",
    (shared.Party, 'orcid_id'): "cim.2.shared.Party.orcid_id",
    (shared.Party, 'address'): "cim.2.shared.Party.address",
    (shared.Party, 'url'): "cim.2.shared.Party.url",
    (shared.QualityReview, 'date'): "cim.2.shared.QualityReview.date",
    (shared.QualityReview, 'quality_status'): "cim.2.shared.QualityReview.quality_status",
    (shared.QualityReview, 'quality_description'): "cim.2.shared.QualityReview.quality_description",
    (shared.QualityReview, 'metadata_reviewer'): "cim.2.shared.QualityReview.metadata_reviewer",
    (shared.TimesliceList, 'members'): "cim.2.shared.TimesliceList.members",
    (shared.TimesliceList, 'units'): "cim.2.shared.TimesliceList.units",
    (shared.DateTime, 'offset'): "cim.2.shared.DateTime.offset",
    (shared.DateTime, 'value'): "cim.2.shared.DateTime.value",
    (shared.TimePeriod, 'calendar'): "cim.2.shared.TimePeriod.calendar",
    (shared.TimePeriod, 'date_type'): "cim.2.shared.TimePeriod.date_type",
    (shared.TimePeriod, 'length'): "cim.2.shared.TimePeriod.length",
    (shared.TimePeriod, 'units'): "cim.2.shared.TimePeriod.units",
    (shared.TimePeriod, 'date'): "cim.2.shared.TimePeriod.date",
    (shared.RegularTimeset, 'start_date'): "cim.2.shared.RegularTimeset.start_date",
    (shared.RegularTimeset, 'increment'): "cim.2.shared.RegularTimeset.increment",
    (shared.RegularTimeset, 'length'): "cim.2.shared.RegularTimeset.length",
    (shared.DocMetaInfo, 'id'): "cim.2.shared.DocMetaInfo.id",
    (shared.DocMetaInfo, 'source'): "cim.2.shared.DocMetaInfo.source",
    (shared.DocMetaInfo, 'project'): "cim.2.shared.DocMetaInfo.project",
    (shared.DocMetaInfo, 'update_date'): "cim.2.shared.DocMetaInfo.update_date",
    (shared.DocMetaInfo, 'create_date'): "cim.2.shared.DocMetaInfo.create_date",
    (shared.DocMetaInfo, 'drs_keys'): "cim.2.shared.DocMetaInfo.drs_keys",
    (shared.DocMetaInfo, 'institute'): "cim.2.shared.DocMetaInfo.institute",
    (shared.DocMetaInfo, 'type'): "cim.2.shared.DocMetaInfo.type",
    (shared.DocMetaInfo, 'drs_path'): "cim.2.shared.DocMetaInfo.drs_path",
    (shared.DocMetaInfo, 'sort_key'): "cim.2.shared.DocMetaInfo.sort_key",
    (shared.DocMetaInfo, 'type_display_name'): "cim.2.shared.DocMetaInfo.type_display_name",
    (shared.DocMetaInfo, 'type_sort_key'): "cim.2.shared.DocMetaInfo.type_sort_key",
    (shared.DocMetaInfo, 'version'): "cim.2.shared.DocMetaInfo.version",
    (shared.DocMetaInfo, 'external_ids'): "cim.2.shared.DocMetaInfo.external_ids",
    (shared.DocMetaInfo, 'author'): "cim.2.shared.DocMetaInfo.author",
    (shared.DocMetaInfo, 'language'): "cim.2.shared.DocMetaInfo.language",
    (shared.DocMetaInfo, 'source_key'): "cim.2.shared.DocMetaInfo.source_key",
    (shared.KeyFloat, 'key'): "cim.2.shared.KeyFloat.key",
    (shared.KeyFloat, 'value'): "cim.2.shared.KeyFloat.value",
    (shared.OnlineResource, 'linkage'): "cim.2.shared.OnlineResource.linkage",
    (shared.OnlineResource, 'protocol'): "cim.2.shared.OnlineResource.protocol",
    (shared.OnlineResource, 'description'): "cim.2.shared.OnlineResource.description",
    (shared.OnlineResource, 'name'): "cim.2.shared.OnlineResource.name",
    (shared.Responsibility, 'party'): "cim.2.shared.Responsibility.party",
    (shared.Responsibility, 'when'): "cim.2.shared.Responsibility.when",
    (shared.Responsibility, 'role'): "cim.2.shared.Responsibility.role",
    (shared.ExternalDocument, 'doi'): "cim.2.shared.ExternalDocument.doi",
    (shared.ExternalDocument, 'title'): "cim.2.shared.ExternalDocument.title",
    (shared.ExternalDocument, 'meta'): "cim.2.shared.ExternalDocument.meta",
    (shared.ExternalDocument, 'date'): "cim.2.shared.ExternalDocument.date",
    (shared.ExternalDocument, 'name'): "cim.2.shared.ExternalDocument.name",
    (shared.ExternalDocument, 'publication_detail'): "cim.2.shared.ExternalDocument.publication_detail",
    (shared.ExternalDocument, 'online_at'): "cim.2.shared.ExternalDocument.online_at",
    (shared.ExternalDocument, 'authorship'): "cim.2.shared.ExternalDocument.authorship",
    (shared.Cimtext, 'content'): "cim.2.shared.Cimtext.content",
    (shared.Cimtext, 'content_type'): "cim.2.shared.Cimtext.content_type",
    (science.Extent, 'northern_boundary'): "cim.2.science.Extent.northern_boundary",
    (science.Extent, 'eastern_boundary'): "cim.2.science.Extent.eastern_boundary",
    (science.Extent, 'bottom_vertical_level'): "cim.2.science.Extent.bottom_vertical_level",
    (science.Extent, 'western_boundary'): "cim.2.science.Extent.western_boundary",
    (science.Extent, 'southern_boundary'): "cim.2.science.Extent.southern_boundary",
    (science.Extent, 'region_known_as'): "cim.2.science.Extent.region_known_as",
    (science.Extent, 'is_global'): "cim.2.science.Extent.is_global",
    (science.Extent, 'top_vertical_level'): "cim.2.science.Extent.top_vertical_level",
    (science.Extent, 'z_units'): "cim.2.science.Extent.z_units",
    (science.ScientificDomain, 'meta'): "cim.2.science.ScientificDomain.meta",
    (science.ScientificDomain, 'simulates'): "cim.2.science.ScientificDomain.simulates",
    (science.ScientificDomain, 'name'): "cim.2.science.ScientificDomain.name",
    (science.ScientificDomain, 'id'): "cim.2.science.ScientificDomain.id",
    (science.ScientificDomain, 'overview'): "cim.2.science.ScientificDomain.overview",
    (science.ScientificDomain, 'references'): "cim.2.science.ScientificDomain.references",
    (science.ScientificDomain, 'realm'): "cim.2.science.ScientificDomain.realm",
    (science.ScientificDomain, 'differing_key_properties'): "cim.2.science.ScientificDomain.differing_key_properties",
    (science.Tuning, 'description'): "cim.2.science.Tuning.description",
    (science.Tuning, 'trend_metrics_used'): "cim.2.science.Tuning.trend_metrics_used",
    (science.Tuning, 'regional_metrics_used'): "cim.2.science.Tuning.regional_metrics_used",
    (science.Tuning, 'global_mean_metrics_used'): "cim.2.science.Tuning.global_mean_metrics_used",
    (science.Process, 'keywords'): "cim.2.science.Process.keywords",
    (science.Process, 'properties'): "cim.2.science.Process.properties",
    (science.Process, 'algorithms'): "cim.2.science.Process.algorithms",
    (science.Process, 'references'): "cim.2.science.Process.references",
    (science.Process, 'implementation_overview'): "cim.2.science.Process.implementation_overview",
    (science.Process, 'sub_processes'): "cim.2.science.Process.sub_processes",
    (science.SubProcess, 'implementation_overview'): "cim.2.science.SubProcess.implementation_overview",
    (science.SubProcess, 'references'): "cim.2.science.SubProcess.references",
    (science.SubProcess, 'properties'): "cim.2.science.SubProcess.properties",
    (science.ScienceContext, 'context'): "cim.2.science.ScienceContext.context",
    (science.ScienceContext, 'name'): "cim.2.science.ScienceContext.name",
    (science.ScienceContext, 'id'): "cim.2.science.ScienceContext.id",
    (science.Algorithm, 'implementation_overview'): "cim.2.science.Algorithm.implementation_overview",
    (science.Algorithm, 'prognostic_variables'): "cim.2.science.Algorithm.prognostic_variables",
    (science.Algorithm, 'diagnostic_variables'): "cim.2.science.Algorithm.diagnostic_variables",
    (science.Algorithm, 'references'): "cim.2.science.Algorithm.references",
    (science.Algorithm, 'forced_variables'): "cim.2.science.Algorithm.forced_variables",
    (science.Grid, 'name'): "cim.2.science.Grid.name",
    (science.Grid, 'horizontal_grid_layout'): "cim.2.science.Grid.horizontal_grid_layout",
    (science.Grid, 'vertical_grid_layout'): "cim.2.science.Grid.vertical_grid_layout",
    (science.Grid, 'horizontal_grid_type'): "cim.2.science.Grid.horizontal_grid_type",
    (science.Grid, 'additional_details'): "cim.2.science.Grid.additional_details",
    (science.Grid, 'vertical_grid_type'): "cim.2.science.Grid.vertical_grid_type",
    (science.Grid, 'meta'): "cim.2.science.Grid.meta",
    (science.Grid, 'grid_extent'): "cim.2.science.Grid.grid_extent",
    (science.Resolution, 'typical_x_degrees'): "cim.2.science.Resolution.typical_x_degrees",
    (science.Resolution, 'name'): "cim.2.science.Resolution.name",
    (science.Resolution, 'equivalent_resolution_km'): "cim.2.science.Resolution.equivalent_resolution_km",
    (science.Resolution, 'number_of_levels'): "cim.2.science.Resolution.number_of_levels",
    (science.Resolution, 'typical_y_degrees'): "cim.2.science.Resolution.typical_y_degrees",
    (science.Resolution, 'number_of_xy_gridpoints'): "cim.2.science.Resolution.number_of_xy_gridpoints",
    (science.Resolution, 'is_adaptive_grid'): "cim.2.science.Resolution.is_adaptive_grid",
    (science.Model, 'meta'): "cim.2.science.Model.meta",
    (science.Model, 'coupled_components'): "cim.2.science.Model.coupled_components",
    (science.Model, 'coupler'): "cim.2.science.Model.coupler",
    (science.Model, 'simulates'): "cim.2.science.Model.simulates",
    (science.Model, 'id'): "cim.2.science.Model.id",
    (science.Model, 'internal_software_components'): "cim.2.science.Model.internal_software_components",
    (science.Model, 'category'): "cim.2.science.Model.category",
    (science.Model, 'model_default_properties'): "cim.2.science.Model.model_default_properties",
    (science.KeyProperties, 'time_step'): "cim.2.science.KeyProperties.time_step",
    (science.KeyProperties, 'tuning_applied'): "cim.2.science.KeyProperties.tuning_applied",
    (science.KeyProperties, 'grid'): "cim.2.science.KeyProperties.grid",
    (science.KeyProperties, 'resolution'): "cim.2.science.KeyProperties.resolution",
    (science.KeyProperties, 'additional_detail'): "cim.2.science.KeyProperties.additional_detail",
    (science.KeyProperties, 'extra_conservation_properties'): "cim.2.science.KeyProperties.extra_conservation_properties",
    (science.Detail, 'content'): "cim.2.science.Detail.content",
    (science.Detail, 'from_vocab'): "cim.2.science.Detail.from_vocab",
    (science.Detail, 'select'): "cim.2.science.Detail.select",
    (science.Detail, 'with_cardinality'): "cim.2.science.Detail.with_cardinality",
    (science.Detail, 'detail_selection'): "cim.2.science.Detail.detail_selection",
    (science.ConservationProperties, 'corrected_conserved_prognostic_variables'): "cim.2.science.ConservationProperties.corrected_conserved_prognostic_variables",
    (science.ConservationProperties, 'flux_correction_was_used'): "cim.2.science.ConservationProperties.flux_correction_was_used",
    (science.ConservationProperties, 'correction_methodology'): "cim.2.science.ConservationProperties.correction_methodology",
    (platform.StoragePool, 'description'): "cim.2.platform.StoragePool.description",
    (platform.StoragePool, 'type'): "cim.2.platform.StoragePool.type",
    (platform.StoragePool, 'vendor'): "cim.2.platform.StoragePool.vendor",
    (platform.StoragePool, 'volume_available'): "cim.2.platform.StoragePool.volume_available",
    (platform.StoragePool, 'name'): "cim.2.platform.StoragePool.name",
    (platform.ComputePool, 'number_of_nodes'): "cim.2.platform.ComputePool.number_of_nodes",
    (platform.ComputePool, 'compute_cores_per_node'): "cim.2.platform.ComputePool.compute_cores_per_node",
    (platform.ComputePool, 'memory_per_node'): "cim.2.platform.ComputePool.memory_per_node",
    (platform.ComputePool, 'cpu_type'): "cim.2.platform.ComputePool.cpu_type",
    (platform.ComputePool, 'accelerators_per_node'): "cim.2.platform.ComputePool.accelerators_per_node",
    (platform.ComputePool, 'model_number'): "cim.2.platform.ComputePool.model_number",
    (platform.ComputePool, 'accelerator_type'): "cim.2.platform.ComputePool.accelerator_type",
    (platform.ComputePool, 'operating_system'): "cim.2.platform.ComputePool.operating_system",
    (platform.ComputePool, 'name'): "cim.2.platform.ComputePool.name",
    (platform.ComputePool, 'interconnect'): "cim.2.platform.ComputePool.interconnect",
    (platform.ComputePool, 'description'): "cim.2.platform.ComputePool.description",
    (platform.Machine, 'meta'): "cim.2.platform.Machine.meta",
    (platform.Partition, 'online_documentation'): "cim.2.platform.Partition.online_documentation",
    (platform.Partition, 'partition'): "cim.2.platform.Partition.partition",
    (platform.Partition, 'institution'): "cim.2.platform.Partition.institution",
    (platform.Partition, 'compute_pools'): "cim.2.platform.Partition.compute_pools",
    (platform.Partition, 'model_number'): "cim.2.platform.Partition.model_number",
    (platform.Partition, 'storage_pools'): "cim.2.platform.Partition.storage_pools",
    (platform.Partition, 'when_used'): "cim.2.platform.Partition.when_used",
    (platform.Partition, 'name'): "cim.2.platform.Partition.name",
    (platform.Partition, 'vendor'): "cim.2.platform.Partition.vendor",
    (platform.Partition, 'description'): "cim.2.platform.Partition.description",
    (platform.ComponentPerformance, 'cores_used'): "cim.2.platform.ComponentPerformance.cores_used",
    (platform.ComponentPerformance, 'nodes_used'): "cim.2.platform.ComponentPerformance.nodes_used",
    (platform.ComponentPerformance, 'speed'): "cim.2.platform.ComponentPerformance.speed",
    (platform.ComponentPerformance, 'component'): "cim.2.platform.ComponentPerformance.component",
    (platform.ComponentPerformance, 'component_name'): "cim.2.platform.ComponentPerformance.component_name",
    (platform.Performance, 'asypd'): "cim.2.platform.Performance.asypd",
    (platform.Performance, 'memory_bloat'): "cim.2.platform.Performance.memory_bloat",
    (platform.Performance, 'sypd'): "cim.2.platform.Performance.sypd",
    (platform.Performance, 'platform'): "cim.2.platform.Performance.platform",
    (platform.Performance, 'load_imbalance'): "cim.2.platform.Performance.load_imbalance",
    (platform.Performance, 'name'): "cim.2.platform.Performance.name",
    (platform.Performance, 'chsy'): "cim.2.platform.Performance.chsy",
    (platform.Performance, 'total_nodes_used'): "cim.2.platform.Performance.total_nodes_used",
    (platform.Performance, 'compiler'): "cim.2.platform.Performance.compiler",
    (platform.Performance, 'meta'): "cim.2.platform.Performance.meta",
    (platform.Performance, 'subcomponent_performance'): "cim.2.platform.Performance.subcomponent_performance",
    (platform.Performance, 'coupler_load'): "cim.2.platform.Performance.coupler_load",
    (platform.Performance, 'model'): "cim.2.platform.Performance.model",
    (platform.Performance, 'io_load'): "cim.2.platform.Performance.io_load",
    (platform.StorageVolume, 'units'): "cim.2.platform.StorageVolume.units",
    (platform.StorageVolume, 'volume'): "cim.2.platform.StorageVolume.volume",
    (data.VariableCollection, 'collection_name'): "cim.2.data.VariableCollection.collection_name",
    (data.VariableCollection, 'variables'): "cim.2.data.VariableCollection.variables",
    (data.Simulation, 'calendar'): "cim.2.data.Simulation.calendar",
    (data.Simulation, 'primary_ensemble'): "cim.2.data.Simulation.primary_ensemble",
    (data.Simulation, 'ran_for_experiments'): "cim.2.data.Simulation.ran_for_experiments",
    (data.Simulation, 'parent_simulation'): "cim.2.data.Simulation.parent_simulation",
    (data.Simulation, 'used'): "cim.2.data.Simulation.used",
    (data.Simulation, 'ensemble_identifier'): "cim.2.data.Simulation.ensemble_identifier",
    (data.Simulation, 'part_of_project'): "cim.2.data.Simulation.part_of_project",
    (data.Dataset, 'meta'): "cim.2.data.Dataset.meta",
    (data.Dataset, 'responsible_parties'): "cim.2.data.Dataset.responsible_parties",
    (data.Dataset, 'availability'): "cim.2.data.Dataset.availability",
    (data.Dataset, 'name'): "cim.2.data.Dataset.name",
    (data.Dataset, 'description'): "cim.2.data.Dataset.description",
    (data.Dataset, 'produced_by'): "cim.2.data.Dataset.produced_by",
    (data.Dataset, 'related_to_dataset'): "cim.2.data.Dataset.related_to_dataset",
    (data.Dataset, 'drs_datasets'): "cim.2.data.Dataset.drs_datasets",
    (data.Dataset, 'references'): "cim.2.data.Dataset.references",
    (data.Downscaling, 'downscaled_from'): "cim.2.data.Downscaling.downscaled_from",
    (activity.Activity, 'name'): "cim.2.activity.Activity.name",
    (activity.Activity, 'references'): "cim.2.activity.Activity.references",
    (activity.Activity, 'canonical_name'): "cim.2.activity.Activity.canonical_name",
    (activity.Activity, 'meta'): "cim.2.activity.Activity.meta",
    (activity.Activity, 'description'): "cim.2.activity.Activity.description",
    (activity.Activity, 'rationale'): "cim.2.activity.Activity.rationale",
    (activity.Activity, 'responsible_parties'): "cim.2.activity.Activity.responsible_parties",
    (activity.Activity, 'duration'): "cim.2.activity.Activity.duration",
    (activity.Activity, 'keywords'): "cim.2.activity.Activity.keywords",
    (activity.Activity, 'long_name'): "cim.2.activity.Activity.long_name",
    (activity.Conformance, 'target_requirement'): "cim.2.activity.Conformance.target_requirement",
    (activity.Ensemble, 'has_ensemble_axes'): "cim.2.activity.Ensemble.has_ensemble_axes",
    (activity.Ensemble, 'members'): "cim.2.activity.Ensemble.members",
    (activity.Ensemble, 'common_conformances'): "cim.2.activity.Ensemble.common_conformances",
    (activity.Ensemble, 'part_of'): "cim.2.activity.Ensemble.part_of",
    (activity.Ensemble, 'documentation'): "cim.2.activity.Ensemble.documentation",
    (activity.Ensemble, 'supported'): "cim.2.activity.Ensemble.supported",
    (activity.UberEnsemble, 'child_ensembles'): "cim.2.activity.UberEnsemble.child_ensembles",
    (activity.EnsembleMember, 'ran_on'): "cim.2.activity.EnsembleMember.ran_on",
    (activity.EnsembleMember, 'variant_id'): "cim.2.activity.EnsembleMember.variant_id",
    (activity.EnsembleMember, 'simulation'): "cim.2.activity.EnsembleMember.simulation",
    (activity.EnsembleMember, 'errata'): "cim.2.activity.EnsembleMember.errata",
    (activity.EnsembleMember, 'had_performance'): "cim.2.activity.EnsembleMember.had_performance",
    (activity.ParentSimulation, 'branch_time_in_child'): "cim.2.activity.ParentSimulation.branch_time_in_child",
    (activity.ParentSimulation, 'parent'): "cim.2.activity.ParentSimulation.parent",
    (activity.ParentSimulation, 'branch_time_in_parent'): "cim.2.activity.ParentSimulation.branch_time_in_parent",
    (activity.AxisMember, 'index'): "cim.2.activity.AxisMember.index",
    (activity.AxisMember, 'description'): "cim.2.activity.AxisMember.description",
    (activity.AxisMember, 'value'): "cim.2.activity.AxisMember.value",
    (activity.AxisMember, 'extra_detail'): "cim.2.activity.AxisMember.extra_detail",
    (activity.EnsembleAxis, 'short_identifier'): "cim.2.activity.EnsembleAxis.short_identifier",
    (activity.EnsembleAxis, 'extra_detail'): "cim.2.activity.EnsembleAxis.extra_detail",
    (activity.EnsembleAxis, 'target_requirement'): "cim.2.activity.EnsembleAxis.target_requirement",
    (activity.EnsembleAxis, 'member'): "cim.2.activity.EnsembleAxis.member",

    # ------------------------------------------------
    # Enums.
    # ------------------------------------------------

    drs.DrsRealms: "cim.2.drs.DrsRealms",
    drs.DrsTimeSuffixes: "cim.2.drs.DrsTimeSuffixes",
    drs.DrsFrequencyTypes: "cim.2.drs.DrsFrequencyTypes",
    drs.DrsGeographicalOperators: "cim.2.drs.DrsGeographicalOperators",
    designing.EnsembleTypes: "cim.2.designing.EnsembleTypes",
    designing.ExperimentalRelationships: "cim.2.designing.ExperimentalRelationships",
    designing.ForcingTypes: "cim.2.designing.ForcingTypes",
    software.CouplingFramework: "cim.2.software.CouplingFramework",
    software.ProgrammingLanguage: "cim.2.software.ProgrammingLanguage",
    shared.TextCode: "cim.2.shared.TextCode",
    shared.NilReason: "cim.2.shared.NilReason",
    shared.RoleCode: "cim.2.shared.RoleCode",
    shared.SlicetimeUnits: "cim.2.shared.SlicetimeUnits",
    shared.CalendarTypes: "cim.2.shared.CalendarTypes",
    shared.PeriodDateTypes: "cim.2.shared.PeriodDateTypes",
    shared.DocumentTypes: "cim.2.shared.DocumentTypes",
    shared.TimeUnits: "cim.2.shared.TimeUnits",
    shared.QualityStatus: "cim.2.shared.QualityStatus",
    science.ModelTypes: "cim.2.science.ModelTypes",
    science.SelectionCardinality: "cim.2.science.SelectionCardinality",
    platform.StorageSystems: "cim.2.platform.StorageSystems",
    platform.VolumeUnits: "cim.2.platform.VolumeUnits",
    data.DataAssociationTypes: "cim.2.data.DataAssociationTypes",
    activity.EnsembleTypes: "cim.2.activity.EnsembleTypes",
    activity.ForcingTypes: "cim.2.activity.ForcingTypes",

    # ------------------------------------------------
    # Enum members.
    # ------------------------------------------------

    (drs.DrsRealms, 'aerosol'): "cim.2.drs.DrsRealms.aerosol",
    (drs.DrsRealms, 'atmosChem'): "cim.2.drs.DrsRealms.atmosChem",
    (drs.DrsRealms, 'ocnBgchem'): "cim.2.drs.DrsRealms.ocnBgchem",
    (drs.DrsRealms, 'atmos'): "cim.2.drs.DrsRealms.atmos",
    (drs.DrsRealms, 'ocean'): "cim.2.drs.DrsRealms.ocean",
    (drs.DrsRealms, 'land'): "cim.2.drs.DrsRealms.land",
    (drs.DrsRealms, 'landIce'): "cim.2.drs.DrsRealms.landIce",
    (drs.DrsRealms, 'seaIce'): "cim.2.drs.DrsRealms.seaIce",
    (drs.DrsTimeSuffixes, 'clim'): "cim.2.drs.DrsTimeSuffixes.clim",
    (drs.DrsTimeSuffixes, 'avg'): "cim.2.drs.DrsTimeSuffixes.avg",
    (drs.DrsFrequencyTypes, '3hr'): "cim.2.drs.DrsFrequencyTypes.3hr",
    (drs.DrsFrequencyTypes, 'subhr'): "cim.2.drs.DrsFrequencyTypes.subhr",
    (drs.DrsFrequencyTypes, 'monClim'): "cim.2.drs.DrsFrequencyTypes.monClim",
    (drs.DrsFrequencyTypes, 'fx'): "cim.2.drs.DrsFrequencyTypes.fx",
    (drs.DrsFrequencyTypes, 'yr'): "cim.2.drs.DrsFrequencyTypes.yr",
    (drs.DrsFrequencyTypes, 'mon'): "cim.2.drs.DrsFrequencyTypes.mon",
    (drs.DrsFrequencyTypes, 'day'): "cim.2.drs.DrsFrequencyTypes.day",
    (drs.DrsFrequencyTypes, '6hr'): "cim.2.drs.DrsFrequencyTypes.6hr",
    (drs.DrsGeographicalOperators, 'zonalavg'): "cim.2.drs.DrsGeographicalOperators.zonalavg",
    (drs.DrsGeographicalOperators, 'lnd-zonalavg'): "cim.2.drs.DrsGeographicalOperators.lnd-zonalavg",
    (drs.DrsGeographicalOperators, 'ocn-zonalavg'): "cim.2.drs.DrsGeographicalOperators.ocn-zonalavg",
    (drs.DrsGeographicalOperators, 'areaavg'): "cim.2.drs.DrsGeographicalOperators.areaavg",
    (drs.DrsGeographicalOperators, 'lnd-areaavg'): "cim.2.drs.DrsGeographicalOperators.lnd-areaavg",
    (drs.DrsGeographicalOperators, 'ocn-areaavg'): "cim.2.drs.DrsGeographicalOperators.ocn-areaavg",
    (designing.EnsembleTypes, 'Initialisation Method'): "cim.2.designing.EnsembleTypes.Initialisation-Method",
    (designing.EnsembleTypes, 'Initialisation'): "cim.2.designing.EnsembleTypes.Initialisation",
    (designing.EnsembleTypes, 'Staggered Start'): "cim.2.designing.EnsembleTypes.Staggered-Start",
    (designing.EnsembleTypes, 'Forced'): "cim.2.designing.EnsembleTypes.Forced",
    (designing.EnsembleTypes, 'Resolution'): "cim.2.designing.EnsembleTypes.Resolution",
    (designing.EnsembleTypes, 'Perturbed Physics'): "cim.2.designing.EnsembleTypes.Perturbed-Physics",
    (designing.ExperimentalRelationships, 'control_for'): "cim.2.designing.ExperimentalRelationships.control_for",
    (designing.ExperimentalRelationships, 'provides_constraints'): "cim.2.designing.ExperimentalRelationships.provides_constraints",
    (designing.ExperimentalRelationships, 'initialisation_for'): "cim.2.designing.ExperimentalRelationships.initialisation_for",
    (designing.ExperimentalRelationships, 'is_sibling'): "cim.2.designing.ExperimentalRelationships.is_sibling",
    (designing.ForcingTypes, 'historical'): "cim.2.designing.ForcingTypes.historical",
    (designing.ForcingTypes, 'scenario'): "cim.2.designing.ForcingTypes.scenario",
    (designing.ForcingTypes, 'another simulation'): "cim.2.designing.ForcingTypes.another-simulation",
    (designing.ForcingTypes, 'idealised'): "cim.2.designing.ForcingTypes.idealised",
    (software.CouplingFramework, 'Bespoke'): "cim.2.software.CouplingFramework.Bespoke",
    (software.CouplingFramework, 'Unknown'): "cim.2.software.CouplingFramework.Unknown",
    (software.CouplingFramework, 'None'): "cim.2.software.CouplingFramework.None",
    (software.CouplingFramework, 'OASIS'): "cim.2.software.CouplingFramework.OASIS",
    (software.CouplingFramework, 'OASIS3-MCT'): "cim.2.software.CouplingFramework.OASIS3-MCT",
    (software.CouplingFramework, 'ESMF'): "cim.2.software.CouplingFramework.ESMF",
    (software.CouplingFramework, 'NUOPC'): "cim.2.software.CouplingFramework.NUOPC",
    (software.ProgrammingLanguage, 'Python'): "cim.2.software.ProgrammingLanguage.Python",
    (software.ProgrammingLanguage, 'C++'): "cim.2.software.ProgrammingLanguage.C++",
    (software.ProgrammingLanguage, 'C'): "cim.2.software.ProgrammingLanguage.C",
    (software.ProgrammingLanguage, 'Fortran'): "cim.2.software.ProgrammingLanguage.Fortran",
    (shared.TextCode, 'plaintext'): "cim.2.shared.TextCode.plaintext",
    (shared.NilReason, 'nil:missing'): "cim.2.shared.NilReason.nil:missing",
    (shared.NilReason, 'nil:unknown'): "cim.2.shared.NilReason.nil:unknown",
    (shared.NilReason, 'nil:inapplicable'): "cim.2.shared.NilReason.nil:inapplicable",
    (shared.NilReason, 'nil:withheld'): "cim.2.shared.NilReason.nil:withheld",
    (shared.NilReason, 'nil:template'): "cim.2.shared.NilReason.nil:template",
    (shared.RoleCode, 'custodian'): "cim.2.shared.RoleCode.custodian",
    (shared.RoleCode, 'metadata_reviewer'): "cim.2.shared.RoleCode.metadata_reviewer",
    (shared.RoleCode, 'publisher'): "cim.2.shared.RoleCode.publisher",
    (shared.RoleCode, 'metadata_author'): "cim.2.shared.RoleCode.metadata_author",
    (shared.RoleCode, 'distributor'): "cim.2.shared.RoleCode.distributor",
    (shared.RoleCode, 'processor'): "cim.2.shared.RoleCode.processor",
    (shared.RoleCode, 'resource provider'): "cim.2.shared.RoleCode.resource-provider",
    (shared.RoleCode, 'Principal Investigator'): "cim.2.shared.RoleCode.Principal-Investigator",
    (shared.RoleCode, 'originator'): "cim.2.shared.RoleCode.originator",
    (shared.RoleCode, 'user'): "cim.2.shared.RoleCode.user",
    (shared.RoleCode, 'point of contact'): "cim.2.shared.RoleCode.point-of-contact",
    (shared.RoleCode, 'author'): "cim.2.shared.RoleCode.author",
    (shared.RoleCode, 'collaborator'): "cim.2.shared.RoleCode.collaborator",
    (shared.RoleCode, 'sponsor'): "cim.2.shared.RoleCode.sponsor",
    (shared.RoleCode, 'owner'): "cim.2.shared.RoleCode.owner",
    (shared.SlicetimeUnits, 'yearly'): "cim.2.shared.SlicetimeUnits.yearly",
    (shared.SlicetimeUnits, 'monthly'): "cim.2.shared.SlicetimeUnits.monthly",
    (shared.CalendarTypes, 'noleap'): "cim.2.shared.CalendarTypes.noleap",
    (shared.CalendarTypes, '365_day'): "cim.2.shared.CalendarTypes.365_day",
    (shared.CalendarTypes, 'all_leap'): "cim.2.shared.CalendarTypes.all_leap",
    (shared.CalendarTypes, '366_day'): "cim.2.shared.CalendarTypes.366_day",
    (shared.CalendarTypes, '360_day'): "cim.2.shared.CalendarTypes.360_day",
    (shared.CalendarTypes, 'julian'): "cim.2.shared.CalendarTypes.julian",
    (shared.CalendarTypes, 'standard'): "cim.2.shared.CalendarTypes.standard",
    (shared.CalendarTypes, 'none'): "cim.2.shared.CalendarTypes.none",
    (shared.CalendarTypes, 'proleptic_gregorian'): "cim.2.shared.CalendarTypes.proleptic_gregorian",
    (shared.CalendarTypes, 'gregorian'): "cim.2.shared.CalendarTypes.gregorian",
    (shared.PeriodDateTypes, 'date is end'): "cim.2.shared.PeriodDateTypes.date-is-end",
    (shared.PeriodDateTypes, 'date is start'): "cim.2.shared.PeriodDateTypes.date-is-start",
    (shared.PeriodDateTypes, 'unused'): "cim.2.shared.PeriodDateTypes.unused",
    (shared.DocumentTypes, 'Performance'): "cim.2.shared.DocumentTypes.Performance",
    (shared.DocumentTypes, 'Project'): "cim.2.shared.DocumentTypes.Project",
    (shared.DocumentTypes, 'ScientificDomain'): "cim.2.shared.DocumentTypes.ScientificDomain",
    (shared.DocumentTypes, 'Simulation'): "cim.2.shared.DocumentTypes.Simulation",
    (shared.DocumentTypes, 'SimulationPlan'): "cim.2.shared.DocumentTypes.SimulationPlan",
    (shared.DocumentTypes, 'TemporalConstraint'): "cim.2.shared.DocumentTypes.TemporalConstraint",
    (shared.DocumentTypes, 'UberEnsemble'): "cim.2.shared.DocumentTypes.UberEnsemble",
    (shared.DocumentTypes, 'Conformance'): "cim.2.shared.DocumentTypes.Conformance",
    (shared.DocumentTypes, 'Dataset'): "cim.2.shared.DocumentTypes.Dataset",
    (shared.DocumentTypes, 'DomainProperties'): "cim.2.shared.DocumentTypes.DomainProperties",
    (shared.DocumentTypes, 'Downscaling'): "cim.2.shared.DocumentTypes.Downscaling",
    (shared.DocumentTypes, 'Ensemble'): "cim.2.shared.DocumentTypes.Ensemble",
    (shared.DocumentTypes, 'EnsembleRequirement'): "cim.2.shared.DocumentTypes.EnsembleRequirement",
    (shared.DocumentTypes, 'ExternalDocument'): "cim.2.shared.DocumentTypes.ExternalDocument",
    (shared.DocumentTypes, 'ForcingConstraint'): "cim.2.shared.DocumentTypes.ForcingConstraint",
    (shared.DocumentTypes, 'Grid'): "cim.2.shared.DocumentTypes.Grid",
    (shared.DocumentTypes, 'Machine'): "cim.2.shared.DocumentTypes.Machine",
    (shared.DocumentTypes, 'Model'): "cim.2.shared.DocumentTypes.Model",
    (shared.DocumentTypes, 'MultiEnsemble'): "cim.2.shared.DocumentTypes.MultiEnsemble",
    (shared.DocumentTypes, 'MultiTimeEnsemble'): "cim.2.shared.DocumentTypes.MultiTimeEnsemble",
    (shared.DocumentTypes, 'NumericalExperiment'): "cim.2.shared.DocumentTypes.NumericalExperiment",
    (shared.DocumentTypes, 'NumericalRequirement'): "cim.2.shared.DocumentTypes.NumericalRequirement",
    (shared.DocumentTypes, 'OutputTemporalRequirement'): "cim.2.shared.DocumentTypes.OutputTemporalRequirement",
    (shared.DocumentTypes, 'Party'): "cim.2.shared.DocumentTypes.Party",
    (shared.TimeUnits, 'days'): "cim.2.shared.TimeUnits.days",
    (shared.TimeUnits, 'years'): "cim.2.shared.TimeUnits.years",
    (shared.TimeUnits, 'months'): "cim.2.shared.TimeUnits.months",
    (shared.TimeUnits, 'seconds'): "cim.2.shared.TimeUnits.seconds",
    (shared.QualityStatus, 'incomplete'): "cim.2.shared.QualityStatus.incomplete",
    (shared.QualityStatus, 'finalised'): "cim.2.shared.QualityStatus.finalised",
    (shared.QualityStatus, 'under_review'): "cim.2.shared.QualityStatus.under_review",
    (shared.QualityStatus, 'reviewed'): "cim.2.shared.QualityStatus.reviewed",
    (science.ModelTypes, 'Process'): "cim.2.science.ModelTypes.Process",
    (science.ModelTypes, 'Atm Only'): "cim.2.science.ModelTypes.Atm-Only",
    (science.ModelTypes, 'Ocean Only'): "cim.2.science.ModelTypes.Ocean-Only",
    (science.ModelTypes, 'Regional'): "cim.2.science.ModelTypes.Regional",
    (science.ModelTypes, 'GCM'): "cim.2.science.ModelTypes.GCM",
    (science.ModelTypes, 'IGCM'): "cim.2.science.ModelTypes.IGCM",
    (science.ModelTypes, 'GCM-MLO'): "cim.2.science.ModelTypes.GCM-MLO",
    (science.ModelTypes, 'Mesoscale'): "cim.2.science.ModelTypes.Mesoscale",
    (science.ModelTypes, 'Planetary'): "cim.2.science.ModelTypes.Planetary",
    (science.SelectionCardinality, '1.N'): "cim.2.science.SelectionCardinality.1.N",
    (science.SelectionCardinality, '0.N'): "cim.2.science.SelectionCardinality.0.N",
    (science.SelectionCardinality, '0.1'): "cim.2.science.SelectionCardinality.0.1",
    (science.SelectionCardinality, '1.1'): "cim.2.science.SelectionCardinality.1.1",
    (platform.StorageSystems, 'Panasas'): "cim.2.platform.StorageSystems.Panasas",
    (platform.StorageSystems, 'Other Disk'): "cim.2.platform.StorageSystems.Other-Disk",
    (platform.StorageSystems, 'Tape - Castor'): "cim.2.platform.StorageSystems.Tape---Castor",
    (platform.StorageSystems, 'Tape - MARS'): "cim.2.platform.StorageSystems.Tape---MARS",
    (platform.StorageSystems, 'Tape - MASS'): "cim.2.platform.StorageSystems.Tape---MASS",
    (platform.StorageSystems, 'Lustre'): "cim.2.platform.StorageSystems.Lustre",
    (platform.StorageSystems, 'GPFS'): "cim.2.platform.StorageSystems.GPFS",
    (platform.StorageSystems, 'isilon'): "cim.2.platform.StorageSystems.isilon",
    (platform.StorageSystems, 'Unknown'): "cim.2.platform.StorageSystems.Unknown",
    (platform.StorageSystems, 'NFS'): "cim.2.platform.StorageSystems.NFS",
    (platform.StorageSystems, 'Tape - Other'): "cim.2.platform.StorageSystems.Tape---Other",
    (platform.VolumeUnits, 'TiB'): "cim.2.platform.VolumeUnits.TiB",
    (platform.VolumeUnits, 'PiB'): "cim.2.platform.VolumeUnits.PiB",
    (platform.VolumeUnits, 'EiB'): "cim.2.platform.VolumeUnits.EiB",
    (platform.VolumeUnits, 'GB'): "cim.2.platform.VolumeUnits.GB",
    (platform.VolumeUnits, 'TB'): "cim.2.platform.VolumeUnits.TB",
    (platform.VolumeUnits, 'PB'): "cim.2.platform.VolumeUnits.PB",
    (platform.VolumeUnits, 'EB'): "cim.2.platform.VolumeUnits.EB",
    (data.DataAssociationTypes, 'partOf'): "cim.2.data.DataAssociationTypes.partOf",
    (data.DataAssociationTypes, 'isComposedOf'): "cim.2.data.DataAssociationTypes.isComposedOf",
    (data.DataAssociationTypes, 'revisonOf'): "cim.2.data.DataAssociationTypes.revisonOf",
    (activity.EnsembleTypes, 'Resolution'): "cim.2.activity.EnsembleTypes.Resolution",
    (activity.EnsembleTypes, 'Perturbed Physics'): "cim.2.activity.EnsembleTypes.Perturbed-Physics",
    (activity.EnsembleTypes, 'Initialisation Method'): "cim.2.activity.EnsembleTypes.Initialisation-Method",
    (activity.EnsembleTypes, 'Initialisation'): "cim.2.activity.EnsembleTypes.Initialisation",
    (activity.EnsembleTypes, 'Staggered Start'): "cim.2.activity.EnsembleTypes.Staggered-Start",
    (activity.EnsembleTypes, 'Forced'): "cim.2.activity.EnsembleTypes.Forced",
    (activity.ForcingTypes, 'historical'): "cim.2.activity.ForcingTypes.historical",
    (activity.ForcingTypes, 'scenario'): "cim.2.activity.ForcingTypes.scenario",
    (activity.ForcingTypes, 'another simulation'): "cim.2.activity.ForcingTypes.another-simulation",
    (activity.ForcingTypes, 'idealised'): "cim.2.activity.ForcingTypes.idealised",
}
