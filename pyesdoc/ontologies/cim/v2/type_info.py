
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


import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_designing_package as designing
import typeset_for_drs_package as drs
import typeset_for_platform_package as platform
import typeset_for_science_package as science
import typeset_for_shared_package as shared
import typeset_for_software_package as software
import typeset_for_time_package as time



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
    designing,
    drs,
    platform,
    science,
    shared,
    software,
    time,
)

# ------------------------------------------------
# Classes.
# ------------------------------------------------

# Supported classes.
CLASSES = (
    activity.Activity,
    activity.AxisMember,
    activity.Conformance,
    activity.Ensemble,
    activity.EnsembleAxis,
    activity.EnsembleMember,
    activity.ParentSimulation,
    activity.UberEnsemble,
    data.Dataset,
    data.Downscaling,
    data.Simulation,
    data.VariableCollection,
    designing.AxisMember,
    designing.DomainRequirements,
    designing.EnsembleRequirement,
    designing.ForcingConstraint,
    designing.InitialisationRequirement,
    designing.MultiEnsemble,
    designing.NumericalExperiment,
    designing.NumericalRequirement,
    designing.OutputRequirement,
    designing.Project,
    designing.SimulationPlan,
    designing.StartDateEnsemble,
    designing.TemporalConstraint,
    drs.DrsAtomicDataset,
    drs.DrsEnsembleIdentifier,
    drs.DrsExperiment,
    drs.DrsGeographicalIndicator,
    drs.DrsPublicationDataset,
    drs.DrsSimulationIdentifier,
    drs.DrsTemporalIdentifier,
    platform.ComponentPerformance,
    platform.ComputePool,
    platform.Machine,
    platform.Partition,
    platform.Performance,
    platform.StoragePool,
    platform.StorageVolume,
    science.ConservationProperties,
    science.Detail,
    science.Discretisation,
    science.Extent,
    science.Grid,
    science.IsoExtent,
    science.KeyProperties,
    science.Model,
    science.Process,
    science.Resolution,
    science.ScienceContext,
    science.ScientificRealm,
    science.SubProcess,
    science.Tuning,
    shared.Cimtext,
    shared.Citation,
    shared.CitationTarget,
    shared.DocMetaInfo,
    shared.DocReference,
    shared.ExtraAttribute,
    shared.OnlineResource,
    shared.Party,
    shared.QualityReview,
    shared.Reference,
    shared.Responsibility,
    software.ComponentBase,
    software.Composition,
    software.DevelopmentPath,
    software.EntryPoint,
    software.Gridspec,
    software.SoftwareComponent,
    software.Variable,
    time.Calendar,
    time.DateTime,
    time.DatetimeSet,
    time.IrregularDateset,
    time.RegularTimeset,
    time.TimePeriod,
)

# Supported class properties.
CLASS_PROPERTIES = { 
    activity.Activity: (
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    activity.AxisMember: (
        'description',
        'extra_detail',
        'index',
        'value',
    ),
    activity.Conformance: (
        'conformance_achieved',
        'target_requirement',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    activity.Ensemble: (
        'common_conformances',
        'documentation',
        'has_ensemble_axes',
        'members',
        'part_of',
        'supported',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    activity.EnsembleAxis: (
        'extra_detail',
        'member',
        'short_identifier',
        'target_requirement',
    ),
    activity.EnsembleMember: (
        'errata',
        'had_performance',
        'ran_on',
        'simulation',
    ),
    activity.ParentSimulation: (
        'branch_method',
        'branch_time_in_child',
        'branch_time_in_parent',
        'parent',
    ),
    activity.UberEnsemble: (
        'child_ensembles',
        'common_conformances',
        'documentation',
        'has_ensemble_axes',
        'members',
        'part_of',
        'supported',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    data.Dataset: (
        'availability',
        'description',
        'drs_datasets',
        'meta',
        'name',
        'produced_by',
        'references',
        'related_to_dataset',
        'responsible_parties',
    ),
    data.Downscaling: (
        'downscaled_from',
        'calendar',
        'contact',
        'end_time',
        'extra_attributes',
        'forcing_index',
        'further_info_url',
        'initialization_index',
        'insitution',
        'parent_simulation',
        'part_of_project',
        'physics_index',
        'primary_ensemble',
        'ran_for_experiments',
        'realization_index',
        'references',
        'start_time',
        'sub_experiment',
        'used',
        'variant_info',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    data.Simulation: (
        'calendar',
        'contact',
        'end_time',
        'extra_attributes',
        'forcing_index',
        'further_info_url',
        'initialization_index',
        'insitution',
        'parent_simulation',
        'part_of_project',
        'physics_index',
        'primary_ensemble',
        'ran_for_experiments',
        'realization_index',
        'references',
        'start_time',
        'sub_experiment',
        'used',
        'variant_info',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    data.VariableCollection: (
        'collection_name',
        'variables',
    ),
    designing.AxisMember: (
    ),
    designing.DomainRequirements: (
        'required_extent',
        'required_resolution',
        'additional_requirements',
        'is_conformance_requested',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    designing.EnsembleRequirement: (
        'ensemble_member',
        'ensemble_type',
        'minimum_size',
        'additional_requirements',
        'is_conformance_requested',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    designing.ForcingConstraint: (
        'additional_constraint',
        'category',
        'code',
        'data_link',
        'forcing_type',
        'group',
        'origin',
        'additional_requirements',
        'is_conformance_requested',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    designing.InitialisationRequirement: (
        'branch_time_in_initialisation_source',
        'initialise_from_data',
        'initialise_from_experiment',
        'additional_requirements',
        'is_conformance_requested',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    designing.MultiEnsemble: (
        'ensemble_axis',
        'additional_requirements',
        'is_conformance_requested',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    designing.NumericalExperiment: (
        'related_experiments',
        'related_mips',
        'required_period',
        'requirements',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    designing.NumericalRequirement: (
        'additional_requirements',
        'is_conformance_requested',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    designing.OutputRequirement: (
        'formal_data_request',
        'additional_requirements',
        'is_conformance_requested',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    designing.Project: (
        'homepage',
        'objectives',
        'previous_projects',
        'requires_experiments',
        'sub_projects',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    designing.SimulationPlan: (
        'expected_model',
        'expected_performance_sypd',
        'expected_platform',
        'will_support_experiments',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    designing.StartDateEnsemble: (
        'ensemble_members',
        'additional_requirements',
        'is_conformance_requested',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    designing.TemporalConstraint: (
        'required_calendar',
        'required_duration',
        'start_date',
        'start_flexibility',
        'additional_requirements',
        'is_conformance_requested',
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    drs.DrsAtomicDataset: (
        'frequency',
        'geographical_constraint',
        'mip_table',
        'realm',
        'temporal_constraint',
        'variable_name',
        'version_number',
    ),
    drs.DrsEnsembleIdentifier: (
        'forcing_number',
        'initialisation_method_number',
        'perturbation_number',
        'realisation_number',
    ),
    drs.DrsExperiment: (
        'axis_identifer',
        'axis_type',
        'family',
    ),
    drs.DrsGeographicalIndicator: (
        'bounding_box',
        'operator',
        'spatial_domain',
    ),
    drs.DrsPublicationDataset: (
    ),
    drs.DrsSimulationIdentifier: (
        'institute',
        'model',
        'run_variant_id',
    ),
    drs.DrsTemporalIdentifier: (
        'end',
        'start',
        'suffix',
    ),
    platform.ComponentPerformance: (
        'component',
        'component_name',
        'cores_used',
        'nodes_used',
        'speed',
    ),
    platform.ComputePool: (
        'accelerator_type',
        'accelerators_per_node',
        'compute_cores_per_node',
        'cpu_type',
        'description',
        'interconnect',
        'memory_per_node',
        'model_number',
        'name',
        'number_of_nodes',
        'operating_system',
    ),
    platform.Machine: (
        'meta',
        'compute_pools',
        'description',
        'institution',
        'model_number',
        'name',
        'online_documentation',
        'partition',
        'storage_pools',
        'vendor',
        'when_used',
    ),
    platform.Partition: (
        'compute_pools',
        'description',
        'institution',
        'model_number',
        'name',
        'online_documentation',
        'partition',
        'storage_pools',
        'vendor',
        'when_used',
    ),
    platform.Performance: (
        'asypd',
        'chsy',
        'compiler',
        'coupler_load',
        'io_load',
        'load_imbalance',
        'memory_bloat',
        'meta',
        'model',
        'name',
        'platform',
        'subcomponent_performance',
        'sypd',
        'total_nodes_used',
    ),
    platform.StoragePool: (
        'description',
        'name',
        'type',
        'vendor',
        'volume_available',
    ),
    platform.StorageVolume: (
        'units',
        'volume',
    ),
    science.ConservationProperties: (
        'corrected_conserved_prognostic_variables',
        'flux_correction_was_used',
        'details',
        'implementation_overview',
        'references',
        'description',
        'id',
        'short_name',
    ),
    science.Detail: (
        'description',
        'id',
        'short_name',
    ),
    science.Discretisation: (
        'details',
        'implementation_overview',
        'references',
        'description',
        'id',
        'short_name',
    ),
    science.Extent: (
        'is_global',
        'region_known_as',
        'details',
        'implementation_overview',
        'references',
        'description',
        'id',
        'short_name',
    ),
    science.Grid: (
        'description',
        'details',
        'discretisation',
        'meta',
        'name',
        'references',
    ),
    science.IsoExtent: (
        'eastern_boundary',
        'northern_boundary',
        'southern_boundary',
        'western_boundary',
        'is_global',
        'region_known_as',
        'details',
        'implementation_overview',
        'references',
        'description',
        'id',
        'short_name',
    ),
    science.KeyProperties: (
        'extent',
        'extra_conservation_properties',
        'resolution',
        'time_step',
        'tuning_applied',
        'details',
        'implementation_overview',
        'keywords',
        'references',
        'sub_processes',
        'description',
        'id',
        'short_name',
    ),
    science.Model: (
        'category',
        'coupled_components',
        'coupler',
        'id',
        'internal_software_components',
        'meta',
        'model_key_properties',
        'simulates',
        'description',
        'development_history',
        'documentation',
        'long_name',
        'name',
        'release_date',
        'repository',
        'version',
    ),
    science.Process: (
        'details',
        'implementation_overview',
        'keywords',
        'references',
        'sub_processes',
        'description',
        'id',
        'short_name',
    ),
    science.Resolution: (
        'canonical_horizontal_resolution',
        'is_adaptive_grid',
        'name',
        'number_of_horizontal_gridpoints',
        'number_of_vertical_levels',
        'details',
        'implementation_overview',
        'references',
        'description',
        'id',
        'short_name',
    ),
    science.ScienceContext: (
        'description',
        'id',
        'short_name',
    ),
    science.ScientificRealm: (
        'grid',
        'id',
        'key_properties',
        'meta',
        'name',
        'overview',
        'realm',
        'references',
        'simulates',
    ),
    science.SubProcess: (
        'details',
        'implementation_overview',
        'references',
        'description',
        'id',
        'short_name',
    ),
    science.Tuning: (
        'description',
        'global_mean_metrics_used',
        'regional_metrics_used',
        'trend_metrics_used',
        'details',
        'implementation_overview',
        'references',
        'description',
        'id',
        'short_name',
    ),
    shared.Cimtext: (
        'content',
        'content_type',
    ),
    shared.Citation: (
        'abstract',
        'citation_detail',
        'collective_title',
        'context',
        'doi',
        'meta',
        'title',
        'type',
        'url',
    ),
    shared.CitationTarget: (
        'citation_detail',
        'doi',
        'meta',
        'name',
        'online_at',
        'title',
    ),
    shared.DocMetaInfo: (
        'author',
        'create_date',
        'drs_keys',
        'drs_path',
        'external_ids',
        'id',
        'institute',
        'language',
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
        'constraint_vocabulary',
        'context',
        'id',
        'relationship',
        'type',
        'version',
        'description',
        'linkage',
        'name',
        'protocol',
    ),
    shared.ExtraAttribute: (
        'doc',
        'key',
        'type',
        'value',
    ),
    shared.OnlineResource: (
        'description',
        'linkage',
        'name',
        'protocol',
    ),
    shared.Party: (
        'address',
        'email',
        'meta',
        'name',
        'orcid_id',
        'organisation',
        'url',
    ),
    shared.QualityReview: (
        'date',
        'meta',
        'metadata_reviewer',
        'quality_description',
        'quality_status',
        'target_document',
    ),
    shared.Reference: (
        'context',
        'document',
    ),
    shared.Responsibility: (
        'party',
        'role',
        'when',
    ),
    software.ComponentBase: (
        'description',
        'development_history',
        'documentation',
        'long_name',
        'name',
        'release_date',
        'repository',
        'version',
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
    software.DevelopmentPath: (
        'consortium_name',
        'creators',
        'developed_in_house',
        'funding_sources',
        'previous_version',
    ),
    software.EntryPoint: (
        'name',
    ),
    software.Gridspec: (
        'description',
    ),
    software.SoftwareComponent: (
        'composition',
        'connection_points',
        'coupling_framework',
        'dependencies',
        'grid',
        'language',
        'license',
        'sub_components',
        'description',
        'development_history',
        'documentation',
        'long_name',
        'name',
        'release_date',
        'repository',
        'version',
    ),
    software.Variable: (
        'description',
        'name',
        'prognostic',
    ),
    time.Calendar: (
        'description',
        'month_lengths',
        'name',
        'standard_name',
    ),
    time.DateTime: (
        'offset',
        'value',
    ),
    time.DatetimeSet: (
        'length',
    ),
    time.IrregularDateset: (
        'date_set',
        'length',
    ),
    time.RegularTimeset: (
        'increment',
        'length',
        'start_date',
        'length',
    ),
    time.TimePeriod: (
        'calendar',
        'date',
        'date_type',
        'length',
        'units',
    ),
}

# Supported class own properties.
CLASS_OWN_PROPERTIES = { 
    activity.Activity: (
        'alternative_names',
        'canonical_name',
        'description',
        'duration',
        'internal_name',
        'keywords',
        'long_name',
        'meta',
        'name',
        'previously_known_as',
        'rationale',
        'references',
        'responsible_parties',
    ),
    activity.AxisMember: (
        'description',
        'extra_detail',
        'index',
        'value',
    ),
    activity.Conformance: (
        'conformance_achieved',
        'target_requirement',
    ),
    activity.Ensemble: (
        'common_conformances',
        'documentation',
        'has_ensemble_axes',
        'members',
        'part_of',
        'supported',
    ),
    activity.EnsembleAxis: (
        'extra_detail',
        'member',
        'short_identifier',
        'target_requirement',
    ),
    activity.EnsembleMember: (
        'errata',
        'had_performance',
        'ran_on',
        'simulation',
    ),
    activity.ParentSimulation: (
        'branch_method',
        'branch_time_in_child',
        'branch_time_in_parent',
        'parent',
    ),
    activity.UberEnsemble: (
        'child_ensembles',
    ),
    data.Dataset: (
        'availability',
        'description',
        'drs_datasets',
        'meta',
        'name',
        'produced_by',
        'references',
        'related_to_dataset',
        'responsible_parties',
    ),
    data.Downscaling: (
        'downscaled_from',
    ),
    data.Simulation: (
        'calendar',
        'contact',
        'end_time',
        'extra_attributes',
        'forcing_index',
        'further_info_url',
        'initialization_index',
        'insitution',
        'parent_simulation',
        'part_of_project',
        'physics_index',
        'primary_ensemble',
        'ran_for_experiments',
        'realization_index',
        'references',
        'start_time',
        'sub_experiment',
        'used',
        'variant_info',
    ),
    data.VariableCollection: (
        'collection_name',
        'variables',
    ),
    designing.AxisMember: (
    ),
    designing.DomainRequirements: (
        'required_extent',
        'required_resolution',
    ),
    designing.EnsembleRequirement: (
        'ensemble_member',
        'ensemble_type',
        'minimum_size',
    ),
    designing.ForcingConstraint: (
        'additional_constraint',
        'category',
        'code',
        'data_link',
        'forcing_type',
        'group',
        'origin',
    ),
    designing.InitialisationRequirement: (
        'branch_time_in_initialisation_source',
        'initialise_from_data',
        'initialise_from_experiment',
    ),
    designing.MultiEnsemble: (
        'ensemble_axis',
    ),
    designing.NumericalExperiment: (
        'related_experiments',
        'related_mips',
        'required_period',
        'requirements',
    ),
    designing.NumericalRequirement: (
        'additional_requirements',
        'is_conformance_requested',
    ),
    designing.OutputRequirement: (
        'formal_data_request',
    ),
    designing.Project: (
        'homepage',
        'objectives',
        'previous_projects',
        'requires_experiments',
        'sub_projects',
    ),
    designing.SimulationPlan: (
        'expected_model',
        'expected_performance_sypd',
        'expected_platform',
        'will_support_experiments',
    ),
    designing.StartDateEnsemble: (
        'ensemble_members',
    ),
    designing.TemporalConstraint: (
        'required_calendar',
        'required_duration',
        'start_date',
        'start_flexibility',
    ),
    drs.DrsAtomicDataset: (
        'frequency',
        'geographical_constraint',
        'mip_table',
        'realm',
        'temporal_constraint',
        'variable_name',
        'version_number',
    ),
    drs.DrsEnsembleIdentifier: (
        'forcing_number',
        'initialisation_method_number',
        'perturbation_number',
        'realisation_number',
    ),
    drs.DrsExperiment: (
        'axis_identifer',
        'axis_type',
        'family',
    ),
    drs.DrsGeographicalIndicator: (
        'bounding_box',
        'operator',
        'spatial_domain',
    ),
    drs.DrsPublicationDataset: (
    ),
    drs.DrsSimulationIdentifier: (
        'institute',
        'model',
        'run_variant_id',
    ),
    drs.DrsTemporalIdentifier: (
        'end',
        'start',
        'suffix',
    ),
    platform.ComponentPerformance: (
        'component',
        'component_name',
        'cores_used',
        'nodes_used',
        'speed',
    ),
    platform.ComputePool: (
        'accelerator_type',
        'accelerators_per_node',
        'compute_cores_per_node',
        'cpu_type',
        'description',
        'interconnect',
        'memory_per_node',
        'model_number',
        'name',
        'number_of_nodes',
        'operating_system',
    ),
    platform.Machine: (
        'meta',
    ),
    platform.Partition: (
        'compute_pools',
        'description',
        'institution',
        'model_number',
        'name',
        'online_documentation',
        'partition',
        'storage_pools',
        'vendor',
        'when_used',
    ),
    platform.Performance: (
        'asypd',
        'chsy',
        'compiler',
        'coupler_load',
        'io_load',
        'load_imbalance',
        'memory_bloat',
        'meta',
        'model',
        'name',
        'platform',
        'subcomponent_performance',
        'sypd',
        'total_nodes_used',
    ),
    platform.StoragePool: (
        'description',
        'name',
        'type',
        'vendor',
        'volume_available',
    ),
    platform.StorageVolume: (
        'units',
        'volume',
    ),
    science.ConservationProperties: (
        'corrected_conserved_prognostic_variables',
        'flux_correction_was_used',
    ),
    science.Detail: (
    ),
    science.Discretisation: (
    ),
    science.Extent: (
        'is_global',
        'region_known_as',
    ),
    science.Grid: (
        'description',
        'details',
        'discretisation',
        'meta',
        'name',
        'references',
    ),
    science.IsoExtent: (
        'eastern_boundary',
        'northern_boundary',
        'southern_boundary',
        'western_boundary',
    ),
    science.KeyProperties: (
        'extent',
        'extra_conservation_properties',
        'resolution',
        'time_step',
        'tuning_applied',
    ),
    science.Model: (
        'category',
        'coupled_components',
        'coupler',
        'id',
        'internal_software_components',
        'meta',
        'model_key_properties',
        'simulates',
    ),
    science.Process: (
        'details',
        'implementation_overview',
        'keywords',
        'references',
        'sub_processes',
    ),
    science.Resolution: (
        'canonical_horizontal_resolution',
        'is_adaptive_grid',
        'name',
        'number_of_horizontal_gridpoints',
        'number_of_vertical_levels',
    ),
    science.ScienceContext: (
        'description',
        'id',
        'short_name',
    ),
    science.ScientificRealm: (
        'grid',
        'id',
        'key_properties',
        'meta',
        'name',
        'overview',
        'realm',
        'references',
        'simulates',
    ),
    science.SubProcess: (
        'details',
        'implementation_overview',
        'references',
    ),
    science.Tuning: (
        'description',
        'global_mean_metrics_used',
        'regional_metrics_used',
        'trend_metrics_used',
    ),
    shared.Cimtext: (
        'content',
        'content_type',
    ),
    shared.Citation: (
        'abstract',
        'citation_detail',
        'collective_title',
        'context',
        'doi',
        'meta',
        'title',
        'type',
        'url',
    ),
    shared.CitationTarget: (
        'citation_detail',
        'doi',
        'meta',
        'name',
        'online_at',
        'title',
    ),
    shared.DocMetaInfo: (
        'author',
        'create_date',
        'drs_keys',
        'drs_path',
        'external_ids',
        'id',
        'institute',
        'language',
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
        'constraint_vocabulary',
        'context',
        'id',
        'relationship',
        'type',
        'version',
    ),
    shared.ExtraAttribute: (
        'doc',
        'key',
        'type',
        'value',
    ),
    shared.OnlineResource: (
        'description',
        'linkage',
        'name',
        'protocol',
    ),
    shared.Party: (
        'address',
        'email',
        'meta',
        'name',
        'orcid_id',
        'organisation',
        'url',
    ),
    shared.QualityReview: (
        'date',
        'meta',
        'metadata_reviewer',
        'quality_description',
        'quality_status',
        'target_document',
    ),
    shared.Reference: (
        'context',
        'document',
    ),
    shared.Responsibility: (
        'party',
        'role',
        'when',
    ),
    software.ComponentBase: (
        'description',
        'development_history',
        'documentation',
        'long_name',
        'name',
        'release_date',
        'repository',
        'version',
    ),
    software.Composition: (
        'couplings',
        'description',
    ),
    software.DevelopmentPath: (
        'consortium_name',
        'creators',
        'developed_in_house',
        'funding_sources',
        'previous_version',
    ),
    software.EntryPoint: (
        'name',
    ),
    software.Gridspec: (
        'description',
    ),
    software.SoftwareComponent: (
        'composition',
        'connection_points',
        'coupling_framework',
        'dependencies',
        'grid',
        'language',
        'license',
        'sub_components',
    ),
    software.Variable: (
        'description',
        'name',
        'prognostic',
    ),
    time.Calendar: (
        'description',
        'month_lengths',
        'name',
        'standard_name',
    ),
    time.DateTime: (
        'offset',
        'value',
    ),
    time.DatetimeSet: (
        'length',
    ),
    time.IrregularDateset: (
        'date_set',
    ),
    time.RegularTimeset: (
        'increment',
        'length',
        'start_date',
    ),
    time.TimePeriod: (
        'calendar',
        'date',
        'date_type',
        'length',
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
    data.DataAssociationTypes,
    designing.EnsembleTypes,
    designing.ExperimentalRelationships,
    designing.ForcingTypes,
    drs.DrsFrequencyTypes,
    drs.DrsGeographicalOperators,
    drs.DrsRealms,
    drs.DrsTimeSuffixes,
    platform.StorageSystems,
    platform.VolumeUnits,
    science.ModelTypes,
    science.SelectionCardinality,
    shared.DocumentTypes,
    shared.NilReason,
    shared.QualityStatus,
    shared.RoleCode,
    shared.TextCode,
    software.CouplingFramework,
    software.ProgrammingLanguage,
    time.CalendarTypes,
    time.PeriodDateTypes,
    time.TimeUnits,
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
    activity.Activity,
    activity.Conformance,
    activity.Ensemble,
    activity.UberEnsemble,
    data.Dataset,
    data.Downscaling,
    data.Simulation,
    designing.DomainRequirements,
    designing.EnsembleRequirement,
    designing.ForcingConstraint,
    designing.InitialisationRequirement,
    designing.MultiEnsemble,
    designing.NumericalExperiment,
    designing.NumericalRequirement,
    designing.OutputRequirement,
    designing.Project,
    designing.SimulationPlan,
    designing.StartDateEnsemble,
    designing.TemporalConstraint,
    platform.Machine,
    platform.Performance,
    science.Grid,
    science.Model,
    science.ScientificRealm,
    shared.Citation,
    shared.CitationTarget,
    shared.Party,
    shared.QualityReview,
)

# Base classes.
BASE_CLASSES = defaultdict(tuple)
BASE_CLASSES[activity.Conformance] = (activity.Activity, )
BASE_CLASSES[activity.Ensemble] = (activity.Activity, )
BASE_CLASSES[activity.UberEnsemble] = (activity.Ensemble, activity.Activity, )
BASE_CLASSES[data.Downscaling] = (data.Simulation, activity.Activity, )
BASE_CLASSES[data.Simulation] = (activity.Activity, )
BASE_CLASSES[designing.DomainRequirements] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.EnsembleRequirement] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.ForcingConstraint] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.InitialisationRequirement] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.MultiEnsemble] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.NumericalExperiment] = (activity.Activity, )
BASE_CLASSES[designing.NumericalRequirement] = (activity.Activity, )
BASE_CLASSES[designing.OutputRequirement] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.Project] = (activity.Activity, )
BASE_CLASSES[designing.SimulationPlan] = (activity.Activity, )
BASE_CLASSES[designing.StartDateEnsemble] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[designing.TemporalConstraint] = (designing.NumericalRequirement, activity.Activity, )
BASE_CLASSES[platform.Machine] = (platform.Partition, )
BASE_CLASSES[science.ConservationProperties] = (science.SubProcess, science.ScienceContext, )
BASE_CLASSES[science.Detail] = (science.ScienceContext, )
BASE_CLASSES[science.Discretisation] = (science.SubProcess, science.ScienceContext, )
BASE_CLASSES[science.Extent] = (science.SubProcess, science.ScienceContext, )
BASE_CLASSES[science.IsoExtent] = (science.Extent, science.SubProcess, science.ScienceContext, )
BASE_CLASSES[science.KeyProperties] = (science.Process, science.ScienceContext, )
BASE_CLASSES[science.Model] = (software.ComponentBase, )
BASE_CLASSES[science.Process] = (science.ScienceContext, )
BASE_CLASSES[science.Resolution] = (science.SubProcess, science.ScienceContext, )
BASE_CLASSES[science.SubProcess] = (science.ScienceContext, )
BASE_CLASSES[science.Tuning] = (science.SubProcess, science.ScienceContext, )
BASE_CLASSES[shared.DocReference] = (shared.OnlineResource, )
BASE_CLASSES[software.SoftwareComponent] = (software.ComponentBase, )
BASE_CLASSES[time.IrregularDateset] = (time.DatetimeSet, )
BASE_CLASSES[time.RegularTimeset] = (time.DatetimeSet, )

# Classes with base classes.
BASE_CLASSED = tuple(BASE_CLASSES.keys())

# Sub classes.
SUB_CLASSES = defaultdict(tuple)
SUB_CLASSES[activity.Activity] = (
    activity.Conformance,
    activity.Ensemble,
    data.Simulation,
    designing.NumericalExperiment,
    designing.NumericalRequirement,
    designing.Project,
    designing.SimulationPlan,
    activity.UberEnsemble,
    data.Downscaling,
    designing.DomainRequirements,
    designing.EnsembleRequirement,
    designing.ForcingConstraint,
    designing.InitialisationRequirement,
    designing.MultiEnsemble,
    designing.OutputRequirement,
    designing.StartDateEnsemble,
    designing.TemporalConstraint,
    )
SUB_CLASSES[activity.Ensemble] = (
    activity.UberEnsemble,
    )
SUB_CLASSES[data.Simulation] = (
    data.Downscaling,
    )
SUB_CLASSES[designing.NumericalRequirement] = (
    designing.DomainRequirements,
    designing.EnsembleRequirement,
    designing.ForcingConstraint,
    designing.InitialisationRequirement,
    designing.MultiEnsemble,
    designing.OutputRequirement,
    designing.StartDateEnsemble,
    designing.TemporalConstraint,
    )
SUB_CLASSES[platform.Partition] = (
    platform.Machine,
    )
SUB_CLASSES[science.Extent] = (
    science.IsoExtent,
    )
SUB_CLASSES[science.Process] = (
    science.KeyProperties,
    )
SUB_CLASSES[science.ScienceContext] = (
    science.Detail,
    science.Process,
    science.SubProcess,
    science.ConservationProperties,
    science.Discretisation,
    science.Extent,
    science.KeyProperties,
    science.Resolution,
    science.Tuning,
    science.IsoExtent,
    )
SUB_CLASSES[science.SubProcess] = (
    science.ConservationProperties,
    science.Discretisation,
    science.Extent,
    science.Resolution,
    science.Tuning,
    science.IsoExtent,
    )
SUB_CLASSES[shared.OnlineResource] = (
    shared.DocReference,
    )
SUB_CLASSES[software.ComponentBase] = (
    science.Model,
    software.SoftwareComponent,
    )
SUB_CLASSES[time.DatetimeSet] = (
    time.IrregularDateset,
    time.RegularTimeset,
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
        ('long_name', 'type', unicode),
        ('previously_known_as', 'type', unicode),
        ('responsible_parties', 'type', shared.Responsibility),
        ('keywords', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('internal_name', 'type', unicode),
        ('duration', 'type', time.TimePeriod),
        ('alternative_names', 'type', unicode),
        ('name', 'type', unicode),

        ('rationale', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('keywords', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('internal_name', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.1"),
        ('alternative_names', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

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
    activity.Conformance: (

        ('description', 'type', unicode),
        ('conformance_achieved', 'type', unicode),
        ('duration', 'type', time.TimePeriod),
        ('canonical_name', 'type', unicode),
        ('responsible_parties', 'type', shared.Responsibility),
        ('internal_name', 'type', unicode),
        ('long_name', 'type', unicode),
        ('previously_known_as', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('rationale', 'type', unicode),
        ('keywords', 'type', unicode),
        ('target_requirement', 'type', designing.NumericalRequirement),
        ('alternative_names', 'type', unicode),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('conformance_achieved', 'cardinality', "1.1"),
        ('duration', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('internal_name', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('rationale', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.1"),
        ('target_requirement', 'cardinality', "1.1"),
        ('alternative_names', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    activity.Ensemble: (

        ('part_of', 'type', activity.UberEnsemble),
        ('common_conformances', 'type', activity.Conformance),
        ('description', 'type', unicode),
        ('supported', 'type', designing.NumericalExperiment),
        ('duration', 'type', time.TimePeriod),
        ('documentation', 'type', shared.OnlineResource),
        ('canonical_name', 'type', unicode),
        ('responsible_parties', 'type', shared.Responsibility),
        ('internal_name', 'type', unicode),
        ('members', 'type', activity.EnsembleMember),
        ('long_name', 'type', unicode),
        ('previously_known_as', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('rationale', 'type', unicode),
        ('keywords', 'type', unicode),
        ('has_ensemble_axes', 'type', activity.EnsembleAxis),
        ('alternative_names', 'type', unicode),
        ('name', 'type', unicode),

        ('part_of', 'cardinality', "0.N"),
        ('common_conformances', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('supported', 'cardinality', "1.N"),
        ('duration', 'cardinality', "0.1"),
        ('documentation', 'cardinality', "0.N"),
        ('canonical_name', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('internal_name', 'cardinality', "0.1"),
        ('members', 'cardinality', "1.N"),
        ('long_name', 'cardinality', "0.1"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('rationale', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.1"),
        ('has_ensemble_axes', 'cardinality', "0.N"),
        ('alternative_names', 'cardinality', "0.N"),
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
    activity.EnsembleMember: (

        ('simulation', 'type', data.Simulation),
        ('ran_on', 'type', platform.Machine),
        ('errata', 'type', shared.OnlineResource),
        ('had_performance', 'type', platform.Performance),

        ('simulation', 'cardinality', "1.1"),
        ('ran_on', 'cardinality', "0.1"),
        ('errata', 'cardinality', "0.1"),
        ('had_performance', 'cardinality', "0.1"),

    ),
    activity.ParentSimulation: (

        ('branch_time_in_parent', 'type', time.DateTime),
        ('branch_time_in_child', 'type', time.DateTime),
        ('branch_method', 'type', unicode),
        ('parent', 'type', data.Simulation),

        ('branch_time_in_parent', 'cardinality', "0.1"),
        ('branch_time_in_child', 'cardinality', "0.1"),
        ('branch_method', 'cardinality', "0.1"),
        ('parent', 'cardinality', "1.1"),

    ),
    activity.UberEnsemble: (

        ('child_ensembles', 'type', activity.Ensemble),
        ('part_of', 'type', activity.UberEnsemble),
        ('common_conformances', 'type', activity.Conformance),
        ('description', 'type', unicode),
        ('name', 'type', unicode),
        ('rationale', 'type', unicode),
        ('supported', 'type', designing.NumericalExperiment),
        ('previously_known_as', 'type', unicode),
        ('responsible_parties', 'type', shared.Responsibility),
        ('keywords', 'type', unicode),
        ('members', 'type', activity.EnsembleMember),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('internal_name', 'type', unicode),
        ('duration', 'type', time.TimePeriod),
        ('has_ensemble_axes', 'type', activity.EnsembleAxis),
        ('alternative_names', 'type', unicode),
        ('documentation', 'type', shared.OnlineResource),

        ('child_ensembles', 'cardinality', "1.N"),
        ('part_of', 'cardinality', "0.N"),
        ('common_conformances', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('rationale', 'cardinality', "0.1"),
        ('supported', 'cardinality', "1.N"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('keywords', 'cardinality', "0.1"),
        ('members', 'cardinality', "1.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('internal_name', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.1"),
        ('has_ensemble_axes', 'cardinality', "0.N"),
        ('alternative_names', 'cardinality', "0.N"),
        ('documentation', 'cardinality', "0.N"),

    ),
    data.Dataset: (

        ('related_to_dataset', 'type', shared.OnlineResource),
        ('name', 'type', unicode),
        ('produced_by', 'type', data.Simulation),
        ('responsible_parties', 'type', shared.Responsibility),
        ('drs_datasets', 'type', drs.DrsPublicationDataset),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('availability', 'type', shared.OnlineResource),
        ('description', 'type', unicode),

        ('related_to_dataset', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),
        ('produced_by', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('drs_datasets', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('availability', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),

    ),
    data.Downscaling: (

        ('insitution', 'type', shared.Party),
        ('realization_index', 'type', int),
        ('variant_info', 'type', unicode),
        ('long_name', 'type', unicode),
        ('downscaled_from', 'type', data.Simulation),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('physics_index', 'type', int),
        ('duration', 'type', time.TimePeriod),
        ('calendar', 'type', time.Calendar),
        ('sub_experiment', 'type', designing.NumericalExperiment),
        ('primary_ensemble', 'type', activity.Ensemble),
        ('previously_known_as', 'type', unicode),
        ('responsible_parties', 'type', shared.Responsibility),
        ('forcing_index', 'type', int),
        ('part_of_project', 'type', designing.Project),
        ('canonical_name', 'type', unicode),
        ('internal_name', 'type', unicode),
        ('used', 'type', science.Model),
        ('description', 'type', unicode),
        ('start_time', 'type', time.DateTime),
        ('ran_for_experiments', 'type', designing.NumericalExperiment),
        ('rationale', 'type', unicode),
        ('extra_attributes', 'type', shared.ExtraAttribute),
        ('name', 'type', unicode),
        ('further_info_url', 'type', unicode),
        ('parent_simulation', 'type', activity.ParentSimulation),
        ('initialization_index', 'type', int),
        ('contact', 'type', unicode),
        ('end_time', 'type', time.DateTime),
        ('keywords', 'type', unicode),
        ('alternative_names', 'type', unicode),

        ('insitution', 'cardinality', "0.1"),
        ('realization_index', 'cardinality', "0.1"),
        ('variant_info', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('downscaled_from', 'cardinality', "1.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('physics_index', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.1"),
        ('calendar', 'cardinality', "0.1"),
        ('sub_experiment', 'cardinality', "0.1"),
        ('primary_ensemble', 'cardinality', "0.1"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('forcing_index', 'cardinality', "0.1"),
        ('part_of_project', 'cardinality', "1.N"),
        ('canonical_name', 'cardinality', "0.1"),
        ('internal_name', 'cardinality', "0.1"),
        ('used', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('start_time', 'cardinality', "0.1"),
        ('ran_for_experiments', 'cardinality', "1.N"),
        ('rationale', 'cardinality', "0.1"),
        ('extra_attributes', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),
        ('further_info_url', 'cardinality', "0.1"),
        ('parent_simulation', 'cardinality', "0.1"),
        ('initialization_index', 'cardinality', "0.1"),
        ('contact', 'cardinality', "0.1"),
        ('end_time', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.1"),
        ('alternative_names', 'cardinality', "0.N"),

    ),
    data.Simulation: (

        ('insitution', 'type', shared.Party),
        ('realization_index', 'type', int),
        ('variant_info', 'type', unicode),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('physics_index', 'type', int),
        ('duration', 'type', time.TimePeriod),
        ('calendar', 'type', time.Calendar),
        ('sub_experiment', 'type', designing.NumericalExperiment),
        ('primary_ensemble', 'type', activity.Ensemble),
        ('previously_known_as', 'type', unicode),
        ('responsible_parties', 'type', shared.Responsibility),
        ('forcing_index', 'type', int),
        ('part_of_project', 'type', designing.Project),
        ('canonical_name', 'type', unicode),
        ('internal_name', 'type', unicode),
        ('used', 'type', science.Model),
        ('description', 'type', unicode),
        ('start_time', 'type', time.DateTime),
        ('ran_for_experiments', 'type', designing.NumericalExperiment),
        ('rationale', 'type', unicode),
        ('extra_attributes', 'type', shared.ExtraAttribute),
        ('name', 'type', unicode),
        ('further_info_url', 'type', unicode),
        ('parent_simulation', 'type', activity.ParentSimulation),
        ('initialization_index', 'type', int),
        ('contact', 'type', unicode),
        ('end_time', 'type', time.DateTime),
        ('keywords', 'type', unicode),
        ('alternative_names', 'type', unicode),

        ('insitution', 'cardinality', "0.1"),
        ('realization_index', 'cardinality', "0.1"),
        ('variant_info', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('physics_index', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.1"),
        ('calendar', 'cardinality', "0.1"),
        ('sub_experiment', 'cardinality', "0.1"),
        ('primary_ensemble', 'cardinality', "0.1"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('forcing_index', 'cardinality', "0.1"),
        ('part_of_project', 'cardinality', "1.N"),
        ('canonical_name', 'cardinality', "0.1"),
        ('internal_name', 'cardinality', "0.1"),
        ('used', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('start_time', 'cardinality', "0.1"),
        ('ran_for_experiments', 'cardinality', "1.N"),
        ('rationale', 'cardinality', "0.1"),
        ('extra_attributes', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),
        ('further_info_url', 'cardinality', "0.1"),
        ('parent_simulation', 'cardinality', "0.1"),
        ('initialization_index', 'cardinality', "0.1"),
        ('contact', 'cardinality', "0.1"),
        ('end_time', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.1"),
        ('alternative_names', 'cardinality', "0.N"),

    ),
    data.VariableCollection: (

        ('collection_name', 'type', unicode),
        ('variables', 'type', unicode),

        ('collection_name', 'cardinality', "0.1"),
        ('variables', 'cardinality', "1.N"),

    ),
    designing.AxisMember: (



    ),
    designing.DomainRequirements: (

        ('rationale', 'type', unicode),
        ('description', 'type', unicode),
        ('keywords', 'type', unicode),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('responsible_parties', 'type', shared.Responsibility),
        ('previously_known_as', 'type', unicode),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('required_extent', 'type', science.Extent),
        ('internal_name', 'type', unicode),
        ('duration', 'type', time.TimePeriod),
        ('required_resolution', 'type', science.Resolution),
        ('is_conformance_requested', 'type', bool),
        ('alternative_names', 'type', unicode),
        ('name', 'type', unicode),

        ('rationale', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.1"),
        ('additional_requirements', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('required_extent', 'cardinality', "0.1"),
        ('internal_name', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.1"),
        ('required_resolution', 'cardinality', "0.1"),
        ('is_conformance_requested', 'cardinality', "1.1"),
        ('alternative_names', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    designing.EnsembleRequirement: (

        ('rationale', 'type', unicode),
        ('minimum_size', 'type', int),
        ('description', 'type', unicode),
        ('keywords', 'type', unicode),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('responsible_parties', 'type', shared.Responsibility),
        ('previously_known_as', 'type', unicode),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('ensemble_type', 'type', unicode),
        ('internal_name', 'type', unicode),
        ('duration', 'type', time.TimePeriod),
        ('ensemble_member', 'type', designing.NumericalRequirement),
        ('is_conformance_requested', 'type', bool),
        ('alternative_names', 'type', unicode),
        ('name', 'type', unicode),

        ('rationale', 'cardinality', "0.1"),
        ('minimum_size', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.1"),
        ('additional_requirements', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('ensemble_type', 'cardinality', "1.1"),
        ('internal_name', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.1"),
        ('ensemble_member', 'cardinality', "0.N"),
        ('is_conformance_requested', 'cardinality', "1.1"),
        ('alternative_names', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    designing.ForcingConstraint: (

        ('origin', 'type', shared.Reference),
        ('code', 'type', unicode),
        ('additional_constraint', 'type', unicode),
        ('long_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('keywords', 'type', unicode),
        ('is_conformance_requested', 'type', bool),
        ('category', 'type', unicode),
        ('group', 'type', unicode),
        ('data_link', 'type', shared.OnlineResource),
        ('canonical_name', 'type', unicode),
        ('responsible_parties', 'type', shared.Responsibility),
        ('forcing_type', 'type', unicode),
        ('previously_known_as', 'type', unicode),
        ('internal_name', 'type', unicode),
        ('description', 'type', unicode),
        ('duration', 'type', time.TimePeriod),
        ('rationale', 'type', unicode),
        ('name', 'type', unicode),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('alternative_names', 'type', unicode),

        ('origin', 'cardinality', "0.1"),
        ('code', 'cardinality', "0.1"),
        ('additional_constraint', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('keywords', 'cardinality', "0.1"),
        ('is_conformance_requested', 'cardinality', "1.1"),
        ('category', 'cardinality', "0.1"),
        ('group', 'cardinality', "0.1"),
        ('data_link', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('forcing_type', 'cardinality', "1.1"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('internal_name', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.1"),
        ('rationale', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('additional_requirements', 'cardinality', "0.N"),
        ('alternative_names', 'cardinality', "0.N"),

    ),
    designing.InitialisationRequirement: (

        ('rationale', 'type', unicode),
        ('description', 'type', unicode),
        ('keywords', 'type', unicode),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('responsible_parties', 'type', shared.Responsibility),
        ('previously_known_as', 'type', unicode),
        ('initialise_from_experiment', 'type', designing.NumericalExperiment),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('branch_time_in_initialisation_source', 'type', time.DateTime),
        ('internal_name', 'type', unicode),
        ('duration', 'type', time.TimePeriod),
        ('is_conformance_requested', 'type', bool),
        ('alternative_names', 'type', unicode),
        ('initialise_from_data', 'type', data.Dataset),
        ('name', 'type', unicode),

        ('rationale', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.1"),
        ('additional_requirements', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('initialise_from_experiment', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('branch_time_in_initialisation_source', 'cardinality', "0.1"),
        ('internal_name', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.1"),
        ('is_conformance_requested', 'cardinality', "1.1"),
        ('alternative_names', 'cardinality', "0.N"),
        ('initialise_from_data', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    designing.MultiEnsemble: (

        ('ensemble_axis', 'type', designing.EnsembleRequirement),
        ('rationale', 'type', unicode),
        ('description', 'type', unicode),
        ('keywords', 'type', unicode),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('responsible_parties', 'type', shared.Responsibility),
        ('previously_known_as', 'type', unicode),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('internal_name', 'type', unicode),
        ('duration', 'type', time.TimePeriod),
        ('is_conformance_requested', 'type', bool),
        ('alternative_names', 'type', unicode),
        ('name', 'type', unicode),

        ('ensemble_axis', 'cardinality', "1.N"),
        ('rationale', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.1"),
        ('additional_requirements', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('internal_name', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.1"),
        ('is_conformance_requested', 'cardinality', "1.1"),
        ('alternative_names', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    designing.NumericalExperiment: (

        ('requirements', 'type', designing.NumericalRequirement),
        ('description', 'type', unicode),
        ('duration', 'type', time.TimePeriod),
        ('required_period', 'type', designing.TemporalConstraint),
        ('canonical_name', 'type', unicode),
        ('responsible_parties', 'type', shared.Responsibility),
        ('internal_name', 'type', unicode),
        ('long_name', 'type', unicode),
        ('previously_known_as', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('related_mips', 'type', designing.Project),
        ('rationale', 'type', unicode),
        ('related_experiments', 'type', designing.NumericalExperiment),
        ('keywords', 'type', unicode),
        ('alternative_names', 'type', unicode),
        ('name', 'type', unicode),

        ('requirements', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.1"),
        ('required_period', 'cardinality', "1.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('internal_name', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('related_mips', 'cardinality', "0.N"),
        ('rationale', 'cardinality', "0.1"),
        ('related_experiments', 'cardinality', "0.N"),
        ('keywords', 'cardinality', "0.1"),
        ('alternative_names', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    designing.NumericalRequirement: (

        ('description', 'type', unicode),
        ('duration', 'type', time.TimePeriod),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('canonical_name', 'type', unicode),
        ('responsible_parties', 'type', shared.Responsibility),
        ('internal_name', 'type', unicode),
        ('long_name', 'type', unicode),
        ('previously_known_as', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('rationale', 'type', unicode),
        ('keywords', 'type', unicode),
        ('is_conformance_requested', 'type', bool),
        ('alternative_names', 'type', unicode),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.1"),
        ('additional_requirements', 'cardinality', "0.N"),
        ('canonical_name', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('internal_name', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('rationale', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.1"),
        ('is_conformance_requested', 'cardinality', "1.1"),
        ('alternative_names', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    designing.OutputRequirement: (

        ('formal_data_request', 'type', shared.OnlineResource),
        ('rationale', 'type', unicode),
        ('description', 'type', unicode),
        ('keywords', 'type', unicode),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('responsible_parties', 'type', shared.Responsibility),
        ('previously_known_as', 'type', unicode),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('internal_name', 'type', unicode),
        ('duration', 'type', time.TimePeriod),
        ('is_conformance_requested', 'type', bool),
        ('alternative_names', 'type', unicode),
        ('name', 'type', unicode),

        ('formal_data_request', 'cardinality', "0.1"),
        ('rationale', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.1"),
        ('additional_requirements', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('internal_name', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.1"),
        ('is_conformance_requested', 'cardinality', "1.1"),
        ('alternative_names', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    designing.Project: (

        ('requires_experiments', 'type', designing.NumericalExperiment),
        ('previous_projects', 'type', designing.Project),
        ('description', 'type', unicode),
        ('sub_projects', 'type', designing.Project),
        ('duration', 'type', time.TimePeriod),
        ('canonical_name', 'type', unicode),
        ('responsible_parties', 'type', shared.Responsibility),
        ('internal_name', 'type', unicode),
        ('long_name', 'type', unicode),
        ('previously_known_as', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('rationale', 'type', unicode),
        ('keywords', 'type', unicode),
        ('objectives', 'type', unicode),
        ('homepage', 'type', unicode),
        ('alternative_names', 'type', unicode),
        ('name', 'type', unicode),

        ('requires_experiments', 'cardinality', "0.N"),
        ('previous_projects', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),
        ('sub_projects', 'cardinality', "0.N"),
        ('duration', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('internal_name', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('rationale', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.1"),
        ('objectives', 'cardinality', "0.N"),
        ('homepage', 'cardinality', "0.1"),
        ('alternative_names', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    designing.SimulationPlan: (

        ('description', 'type', unicode),
        ('duration', 'type', time.TimePeriod),
        ('expected_performance_sypd', 'type', float),
        ('canonical_name', 'type', unicode),
        ('responsible_parties', 'type', shared.Responsibility),
        ('internal_name', 'type', unicode),
        ('long_name', 'type', unicode),
        ('previously_known_as', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('will_support_experiments', 'type', designing.NumericalExperiment),
        ('rationale', 'type', unicode),
        ('expected_model', 'type', science.Model),
        ('keywords', 'type', unicode),
        ('expected_platform', 'type', platform.Machine),
        ('alternative_names', 'type', unicode),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.1"),
        ('expected_performance_sypd', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('internal_name', 'cardinality', "0.1"),
        ('long_name', 'cardinality', "0.1"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('will_support_experiments', 'cardinality', "1.N"),
        ('rationale', 'cardinality', "0.1"),
        ('expected_model', 'cardinality', "1.1"),
        ('keywords', 'cardinality', "0.1"),
        ('expected_platform', 'cardinality', "0.1"),
        ('alternative_names', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    designing.StartDateEnsemble: (

        ('ensemble_members', 'type', time.DatetimeSet),
        ('rationale', 'type', unicode),
        ('description', 'type', unicode),
        ('keywords', 'type', unicode),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('responsible_parties', 'type', shared.Responsibility),
        ('previously_known_as', 'type', unicode),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('internal_name', 'type', unicode),
        ('duration', 'type', time.TimePeriod),
        ('is_conformance_requested', 'type', bool),
        ('alternative_names', 'type', unicode),
        ('name', 'type', unicode),

        ('ensemble_members', 'cardinality', "1.1"),
        ('rationale', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.1"),
        ('additional_requirements', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('internal_name', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.1"),
        ('is_conformance_requested', 'cardinality', "1.1"),
        ('alternative_names', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    designing.TemporalConstraint: (

        ('rationale', 'type', unicode),
        ('description', 'type', unicode),
        ('required_duration', 'type', time.TimePeriod),
        ('start_date', 'type', time.DateTime),
        ('keywords', 'type', unicode),
        ('additional_requirements', 'type', designing.NumericalRequirement),
        ('responsible_parties', 'type', shared.Responsibility),
        ('previously_known_as', 'type', unicode),
        ('long_name', 'type', unicode),
        ('canonical_name', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('required_calendar', 'type', time.Calendar),
        ('internal_name', 'type', unicode),
        ('start_flexibility', 'type', time.TimePeriod),
        ('duration', 'type', time.TimePeriod),
        ('is_conformance_requested', 'type', bool),
        ('alternative_names', 'type', unicode),
        ('name', 'type', unicode),

        ('rationale', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('required_duration', 'cardinality', "0.1"),
        ('start_date', 'cardinality', "0.1"),
        ('keywords', 'cardinality', "0.1"),
        ('additional_requirements', 'cardinality', "0.N"),
        ('responsible_parties', 'cardinality', "0.N"),
        ('previously_known_as', 'cardinality', "0.N"),
        ('long_name', 'cardinality', "0.1"),
        ('canonical_name', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('required_calendar', 'cardinality', "0.1"),
        ('internal_name', 'cardinality', "0.1"),
        ('start_flexibility', 'cardinality', "0.1"),
        ('duration', 'cardinality', "0.1"),
        ('is_conformance_requested', 'cardinality', "1.1"),
        ('alternative_names', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    drs.DrsAtomicDataset: (

        ('version_number', 'type', int),
        ('realm', 'type', unicode),
        ('geographical_constraint', 'type', drs.DrsGeographicalIndicator),
        ('mip_table', 'type', unicode),
        ('frequency', 'type', unicode),
        ('variable_name', 'type', unicode),
        ('temporal_constraint', 'type', drs.DrsTemporalIdentifier),

        ('version_number', 'cardinality', "0.1"),
        ('realm', 'cardinality', "0.1"),
        ('geographical_constraint', 'cardinality', "0.1"),
        ('mip_table', 'cardinality', "1.1"),
        ('frequency', 'cardinality', "1.1"),
        ('variable_name', 'cardinality', "1.1"),
        ('temporal_constraint', 'cardinality', "0.1"),

    ),
    drs.DrsEnsembleIdentifier: (

        ('forcing_number', 'type', int),
        ('realisation_number', 'type', int),
        ('perturbation_number', 'type', int),
        ('initialisation_method_number', 'type', int),

        ('forcing_number', 'cardinality', "0.1"),
        ('realisation_number', 'cardinality', "1.1"),
        ('perturbation_number', 'cardinality', "1.1"),
        ('initialisation_method_number', 'cardinality', "1.1"),

    ),
    drs.DrsExperiment: (

        ('family', 'type', unicode),
        ('axis_identifer', 'type', designing.AxisMember),
        ('axis_type', 'type', unicode),

        ('family', 'cardinality', "1.1"),
        ('axis_identifer', 'cardinality', "0.1"),
        ('axis_type', 'cardinality', "0.1"),

    ),
    drs.DrsGeographicalIndicator: (

        ('operator', 'type', unicode),
        ('bounding_box', 'type', unicode),
        ('spatial_domain', 'type', unicode),

        ('operator', 'cardinality', "0.1"),
        ('bounding_box', 'cardinality', "0.1"),
        ('spatial_domain', 'cardinality', "0.1"),

    ),
    drs.DrsPublicationDataset: (



    ),
    drs.DrsSimulationIdentifier: (

        ('institute', 'type', unicode),
        ('run_variant_id', 'type', drs.DrsEnsembleIdentifier),
        ('model', 'type', unicode),

        ('institute', 'cardinality', "1.1"),
        ('run_variant_id', 'cardinality', "1.1"),
        ('model', 'cardinality', "1.1"),

    ),
    drs.DrsTemporalIdentifier: (

        ('start', 'type', unicode),
        ('end', 'type', unicode),
        ('suffix', 'type', unicode),

        ('start', 'cardinality', "1.1"),
        ('end', 'cardinality', "0.1"),
        ('suffix', 'cardinality', "0.1"),

    ),
    platform.ComponentPerformance: (

        ('speed', 'type', float),
        ('nodes_used', 'type', int),
        ('component', 'type', software.SoftwareComponent),
        ('cores_used', 'type', int),
        ('component_name', 'type', unicode),

        ('speed', 'cardinality', "1.1"),
        ('nodes_used', 'cardinality', "0.1"),
        ('component', 'cardinality', "0.1"),
        ('cores_used', 'cardinality', "0.1"),
        ('component_name', 'cardinality', "1.1"),

    ),
    platform.ComputePool: (

        ('operating_system', 'type', unicode),
        ('interconnect', 'type', unicode),
        ('description', 'type', unicode),
        ('memory_per_node', 'type', platform.StorageVolume),
        ('model_number', 'type', unicode),
        ('compute_cores_per_node', 'type', int),
        ('accelerator_type', 'type', unicode),
        ('cpu_type', 'type', unicode),
        ('number_of_nodes', 'type', int),
        ('accelerators_per_node', 'type', int),
        ('name', 'type', unicode),

        ('operating_system', 'cardinality', "0.1"),
        ('interconnect', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('memory_per_node', 'cardinality', "0.1"),
        ('model_number', 'cardinality', "0.1"),
        ('compute_cores_per_node', 'cardinality', "0.1"),
        ('accelerator_type', 'cardinality', "0.1"),
        ('cpu_type', 'cardinality', "0.1"),
        ('number_of_nodes', 'cardinality', "0.1"),
        ('accelerators_per_node', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),

    ),
    platform.Machine: (

        ('vendor', 'type', shared.Party),
        ('name', 'type', unicode),
        ('partition', 'type', platform.Partition),
        ('model_number', 'type', unicode),
        ('online_documentation', 'type', shared.OnlineResource),
        ('meta', 'type', shared.DocMetaInfo),
        ('storage_pools', 'type', platform.StoragePool),
        ('when_used', 'type', time.TimePeriod),
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
    platform.Partition: (

        ('vendor', 'type', shared.Party),
        ('name', 'type', unicode),
        ('partition', 'type', platform.Partition),
        ('model_number', 'type', unicode),
        ('online_documentation', 'type', shared.OnlineResource),
        ('storage_pools', 'type', platform.StoragePool),
        ('when_used', 'type', time.TimePeriod),
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
    platform.StoragePool: (

        ('vendor', 'type', shared.Party),
        ('volume_available', 'type', platform.StorageVolume),
        ('type', 'type', unicode),
        ('description', 'type', unicode),
        ('name', 'type', unicode),

        ('vendor', 'cardinality', "0.1"),
        ('volume_available', 'cardinality', "1.1"),
        ('type', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),

    ),
    platform.StorageVolume: (

        ('units', 'type', unicode),
        ('volume', 'type', int),

        ('units', 'cardinality', "1.1"),
        ('volume', 'cardinality', "1.1"),

    ),
    science.ConservationProperties: (

        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('corrected_conserved_prognostic_variables', 'type', data.VariableCollection),
        ('references', 'type', shared.Reference),
        ('details', 'type', science.Detail),
        ('implementation_overview', 'type', unicode),
        ('flux_correction_was_used', 'type', bool),
        ('id', 'type', unicode),

        ('description', 'cardinality', "1.1"),
        ('short_name', 'cardinality', "1.1"),
        ('corrected_conserved_prognostic_variables', 'cardinality', "0.1"),
        ('references', 'cardinality', "0.N"),
        ('details', 'cardinality', "0.N"),
        ('implementation_overview', 'cardinality', "1.1"),
        ('flux_correction_was_used', 'cardinality', "0.1"),
        ('id', 'cardinality', "1.1"),

    ),
    science.Detail: (

        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('id', 'type', unicode),

        ('description', 'cardinality', "1.1"),
        ('short_name', 'cardinality', "1.1"),
        ('id', 'cardinality', "1.1"),

    ),
    science.Discretisation: (

        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('references', 'type', shared.Reference),
        ('details', 'type', science.Detail),
        ('implementation_overview', 'type', unicode),
        ('id', 'type', unicode),

        ('description', 'cardinality', "1.1"),
        ('short_name', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('details', 'cardinality', "0.N"),
        ('implementation_overview', 'cardinality', "1.1"),
        ('id', 'cardinality', "1.1"),

    ),
    science.Extent: (

        ('is_global', 'type', bool),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('region_known_as', 'type', unicode),
        ('references', 'type', shared.Reference),
        ('details', 'type', science.Detail),
        ('implementation_overview', 'type', unicode),
        ('id', 'type', unicode),

        ('is_global', 'cardinality', "1.1"),
        ('description', 'cardinality', "1.1"),
        ('short_name', 'cardinality', "1.1"),
        ('region_known_as', 'cardinality', "0.N"),
        ('references', 'cardinality', "0.N"),
        ('details', 'cardinality', "0.N"),
        ('implementation_overview', 'cardinality', "1.1"),
        ('id', 'cardinality', "1.1"),

    ),
    science.Grid: (

        ('description', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('references', 'type', shared.Reference),
        ('discretisation', 'type', science.Discretisation),
        ('details', 'type', science.Detail),
        ('name', 'type', unicode),

        ('description', 'cardinality', "1.1"),
        ('meta', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('discretisation', 'cardinality', "0.1"),
        ('details', 'cardinality', "0.N"),
        ('name', 'cardinality', "1.1"),

    ),
    science.IsoExtent: (

        ('is_global', 'type', bool),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('region_known_as', 'type', unicode),
        ('northern_boundary', 'type', float),
        ('southern_boundary', 'type', float),
        ('references', 'type', shared.Reference),
        ('details', 'type', science.Detail),
        ('implementation_overview', 'type', unicode),
        ('western_boundary', 'type', float),
        ('id', 'type', unicode),
        ('eastern_boundary', 'type', float),

        ('is_global', 'cardinality', "1.1"),
        ('description', 'cardinality', "1.1"),
        ('short_name', 'cardinality', "1.1"),
        ('region_known_as', 'cardinality', "0.N"),
        ('northern_boundary', 'cardinality', "0.1"),
        ('southern_boundary', 'cardinality', "0.1"),
        ('references', 'cardinality', "0.N"),
        ('details', 'cardinality', "0.N"),
        ('implementation_overview', 'cardinality', "1.1"),
        ('western_boundary', 'cardinality', "0.1"),
        ('id', 'cardinality', "1.1"),
        ('eastern_boundary', 'cardinality', "0.1"),

    ),
    science.KeyProperties: (

        ('extra_conservation_properties', 'type', science.ConservationProperties),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('tuning_applied', 'type', science.Tuning),
        ('sub_processes', 'type', science.SubProcess),
        ('references', 'type', shared.Reference),
        ('details', 'type', science.Detail),
        ('extent', 'type', science.Extent),
        ('implementation_overview', 'type', unicode),
        ('keywords', 'type', unicode),
        ('time_step', 'type', float),
        ('resolution', 'type', science.Resolution),
        ('id', 'type', unicode),

        ('extra_conservation_properties', 'cardinality', "0.1"),
        ('description', 'cardinality', "1.1"),
        ('short_name', 'cardinality', "1.1"),
        ('tuning_applied', 'cardinality', "0.1"),
        ('sub_processes', 'cardinality', "0.N"),
        ('references', 'cardinality', "0.N"),
        ('details', 'cardinality', "0.N"),
        ('extent', 'cardinality', "0.1"),
        ('implementation_overview', 'cardinality', "1.1"),
        ('keywords', 'cardinality', "0.1"),
        ('time_step', 'cardinality', "0.1"),
        ('resolution', 'cardinality', "0.1"),
        ('id', 'cardinality', "1.1"),

    ),
    science.Model: (

        ('category', 'type', unicode),
        ('simulates', 'type', science.ScientificRealm),
        ('model_key_properties', 'type', science.KeyProperties),
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

        ('category', 'cardinality', "1.1"),
        ('simulates', 'cardinality', "0.N"),
        ('model_key_properties', 'cardinality', "0.1"),
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
    science.Process: (

        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('sub_processes', 'type', science.SubProcess),
        ('references', 'type', shared.Reference),
        ('details', 'type', science.Detail),
        ('implementation_overview', 'type', unicode),
        ('keywords', 'type', unicode),
        ('id', 'type', unicode),

        ('description', 'cardinality', "1.1"),
        ('short_name', 'cardinality', "1.1"),
        ('sub_processes', 'cardinality', "0.N"),
        ('references', 'cardinality', "0.N"),
        ('details', 'cardinality', "0.N"),
        ('implementation_overview', 'cardinality', "1.1"),
        ('keywords', 'cardinality', "0.1"),
        ('id', 'cardinality', "1.1"),

    ),
    science.Resolution: (

        ('canonical_horizontal_resolution', 'type', unicode),
        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('number_of_vertical_levels', 'type', int),
        ('number_of_horizontal_gridpoints', 'type', int),
        ('references', 'type', shared.Reference),
        ('details', 'type', science.Detail),
        ('implementation_overview', 'type', unicode),
        ('is_adaptive_grid', 'type', bool),
        ('id', 'type', unicode),
        ('name', 'type', unicode),

        ('canonical_horizontal_resolution', 'cardinality', "0.1"),
        ('description', 'cardinality', "1.1"),
        ('short_name', 'cardinality', "1.1"),
        ('number_of_vertical_levels', 'cardinality', "0.1"),
        ('number_of_horizontal_gridpoints', 'cardinality', "0.1"),
        ('references', 'cardinality', "0.N"),
        ('details', 'cardinality', "0.N"),
        ('implementation_overview', 'cardinality', "1.1"),
        ('is_adaptive_grid', 'cardinality', "0.1"),
        ('id', 'cardinality', "1.1"),
        ('name', 'cardinality', "1.1"),

    ),
    science.ScienceContext: (

        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('id', 'type', unicode),

        ('description', 'cardinality', "1.1"),
        ('short_name', 'cardinality', "1.1"),
        ('id', 'cardinality', "1.1"),

    ),
    science.ScientificRealm: (

        ('simulates', 'type', science.Process),
        ('realm', 'type', unicode),
        ('name', 'type', unicode),
        ('overview', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('grid', 'type', science.Grid),
        ('references', 'type', shared.Reference),
        ('key_properties', 'type', science.KeyProperties),
        ('id', 'type', unicode),

        ('simulates', 'cardinality', "1.N"),
        ('realm', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('overview', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('grid', 'cardinality', "0.1"),
        ('references', 'cardinality', "0.N"),
        ('key_properties', 'cardinality', "0.1"),
        ('id', 'cardinality', "0.1"),

    ),
    science.SubProcess: (

        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('references', 'type', shared.Reference),
        ('details', 'type', science.Detail),
        ('implementation_overview', 'type', unicode),
        ('id', 'type', unicode),

        ('description', 'cardinality', "1.1"),
        ('short_name', 'cardinality', "1.1"),
        ('references', 'cardinality', "0.N"),
        ('details', 'cardinality', "0.N"),
        ('implementation_overview', 'cardinality', "1.1"),
        ('id', 'cardinality', "1.1"),

    ),
    science.Tuning: (

        ('description', 'type', unicode),
        ('short_name', 'type', unicode),
        ('trend_metrics_used', 'type', data.VariableCollection),
        ('global_mean_metrics_used', 'type', data.VariableCollection),
        ('regional_metrics_used', 'type', data.VariableCollection),
        ('references', 'type', shared.Reference),
        ('details', 'type', science.Detail),
        ('implementation_overview', 'type', unicode),
        ('id', 'type', unicode),

        ('description', 'cardinality', "1.1"),
        ('short_name', 'cardinality', "1.1"),
        ('trend_metrics_used', 'cardinality', "0.1"),
        ('global_mean_metrics_used', 'cardinality', "0.1"),
        ('regional_metrics_used', 'cardinality', "0.1"),
        ('references', 'cardinality', "0.N"),
        ('details', 'cardinality', "0.N"),
        ('implementation_overview', 'cardinality', "1.1"),
        ('id', 'cardinality', "1.1"),

    ),
    shared.Cimtext: (

        ('content', 'type', unicode),
        ('content_type', 'type', unicode),

        ('content', 'cardinality', "1.1"),
        ('content_type', 'cardinality', "1.1"),

    ),
    shared.Citation: (

        ('doi', 'type', unicode),
        ('title', 'type', unicode),
        ('url', 'type', shared.OnlineResource),
        ('abstract', 'type', unicode),
        ('collective_title', 'type', unicode),
        ('meta', 'type', shared.DocMetaInfo),
        ('context', 'type', unicode),
        ('type', 'type', unicode),
        ('citation_detail', 'type', unicode),

        ('doi', 'cardinality', "0.1"),
        ('title', 'cardinality', "0.1"),
        ('url', 'cardinality', "0.1"),
        ('abstract', 'cardinality', "0.1"),
        ('collective_title', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('context', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('citation_detail', 'cardinality', "0.1"),

    ),
    shared.CitationTarget: (

        ('doi', 'type', unicode),
        ('name', 'type', unicode),
        ('title', 'type', unicode),
        ('online_at', 'type', shared.OnlineResource),
        ('meta', 'type', shared.DocMetaInfo),
        ('citation_detail', 'type', unicode),

        ('doi', 'cardinality', "0.1"),
        ('name', 'cardinality', "1.1"),
        ('title', 'cardinality', "1.1"),
        ('online_at', 'cardinality', "0.1"),
        ('meta', 'cardinality', "1.1"),
        ('citation_detail', 'cardinality', "0.1"),

    ),
    shared.DocMetaInfo: (

        ('drs_keys', 'type', unicode),
        ('drs_path', 'type', unicode),
        ('create_date', 'type', datetime.datetime),
        ('language', 'type', unicode),
        ('author', 'type', shared.Party),
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
        ('language', 'cardinality', "1.1"),
        ('author', 'cardinality', "0.1"),
        ('institute', 'cardinality', "0.1"),
        ('source_key', 'cardinality', "0.1"),
        ('project', 'cardinality', "1.1"),
        ('sort_key', 'cardinality', "0.1"),
        ('version', 'cardinality', "1.1"),
        ('source', 'cardinality', "1.1"),
        ('type_sort_key', 'cardinality', "0.1"),
        ('update_date', 'cardinality', "1.1"),
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
        ('version', 'type', int),
        ('context', 'type', unicode),
        ('type', 'type', unicode),
        ('id', 'type', unicode),
        ('linkage', 'type', unicode),
        ('name', 'type', unicode),

        ('constraint_vocabulary', 'cardinality', "0.1"),
        ('protocol', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('relationship', 'cardinality', "0.1"),
        ('version', 'cardinality', "0.1"),
        ('context', 'cardinality', "0.1"),
        ('type', 'cardinality', "1.1"),
        ('id', 'cardinality', "0.1"),
        ('linkage', 'cardinality', "1.1"),
        ('name', 'cardinality', "1.1"),

    ),
    shared.ExtraAttribute: (

        ('doc', 'type', unicode),
        ('type', 'type', unicode),
        ('value', 'type', unicode),
        ('key', 'type', unicode),

        ('doc', 'cardinality', "0.1"),
        ('type', 'cardinality', "0.1"),
        ('value', 'cardinality', "1.1"),
        ('key', 'cardinality', "1.1"),

    ),
    shared.OnlineResource: (

        ('protocol', 'type', unicode),
        ('description', 'type', unicode),
        ('linkage', 'type', unicode),
        ('name', 'type', unicode),

        ('protocol', 'cardinality', "0.1"),
        ('description', 'cardinality', "0.1"),
        ('linkage', 'cardinality', "1.1"),
        ('name', 'cardinality', "1.1"),

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
    shared.QualityReview: (

        ('quality_status', 'type', unicode),
        ('target_document', 'type', shared.DocReference),
        ('meta', 'type', shared.DocMetaInfo),
        ('quality_description', 'type', unicode),
        ('date', 'type', unicode),
        ('metadata_reviewer', 'type', shared.Party),

        ('quality_status', 'cardinality', "0.1"),
        ('target_document', 'cardinality', "1.1"),
        ('meta', 'cardinality', "1.1"),
        ('quality_description', 'cardinality', "1.1"),
        ('date', 'cardinality', "1.1"),
        ('metadata_reviewer', 'cardinality', "1.1"),

    ),
    shared.Reference: (

        ('document', 'type', shared.CitationTarget),
        ('context', 'type', unicode),

        ('document', 'cardinality', "1.1"),
        ('context', 'cardinality', "0.1"),

    ),
    shared.Responsibility: (

        ('party', 'type', shared.Party),
        ('when', 'type', time.TimePeriod),
        ('role', 'type', unicode),

        ('party', 'cardinality', "1.N"),
        ('when', 'cardinality', "0.1"),
        ('role', 'cardinality', "1.1"),

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
    software.Composition: (

        ('couplings', 'type', unicode),
        ('description', 'type', unicode),

        ('couplings', 'cardinality', "0.N"),
        ('description', 'cardinality', "0.1"),

    ),
    software.DevelopmentPath: (

        ('consortium_name', 'type', unicode),
        ('funding_sources', 'type', shared.Responsibility),
        ('creators', 'type', shared.Responsibility),
        ('developed_in_house', 'type', bool),
        ('previous_version', 'type', unicode),

        ('consortium_name', 'cardinality', "0.1"),
        ('funding_sources', 'cardinality', "0.N"),
        ('creators', 'cardinality', "0.N"),
        ('developed_in_house', 'cardinality', "1.1"),
        ('previous_version', 'cardinality', "0.1"),

    ),
    software.EntryPoint: (

        ('name', 'type', unicode),

        ('name', 'cardinality', "0.1"),

    ),
    software.Gridspec: (

        ('description', 'type', unicode),

        ('description', 'cardinality', "1.1"),

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
    software.Variable: (

        ('description', 'type', unicode),
        ('prognostic', 'type', bool),
        ('name', 'type', unicode),

        ('description', 'cardinality', "0.1"),
        ('prognostic', 'cardinality', "1.1"),
        ('name', 'cardinality', "1.1"),

    ),
    time.Calendar: (

        ('standard_name', 'type', unicode),
        ('description', 'type', unicode),
        ('name', 'type', unicode),
        ('month_lengths', 'type', int),

        ('standard_name', 'cardinality', "1.1"),
        ('description', 'cardinality', "0.1"),
        ('name', 'cardinality', "0.1"),
        ('month_lengths', 'cardinality', "0.N"),

    ),
    time.DateTime: (

        ('value', 'type', unicode),
        ('offset', 'type', bool),

        ('value', 'cardinality', "1.1"),
        ('offset', 'cardinality', "0.1"),

    ),
    time.DatetimeSet: (

        ('length', 'type', int),

        ('length', 'cardinality', "1.1"),

    ),
    time.IrregularDateset: (

        ('length', 'type', int),
        ('date_set', 'type', unicode),

        ('length', 'cardinality', "1.1"),
        ('date_set', 'cardinality', "1.1"),

    ),
    time.RegularTimeset: (

        ('length', 'type', int),
        ('start_date', 'type', time.DateTime),
        ('increment', 'type', time.TimePeriod),

        ('length', 'cardinality', "1.1"),
        ('start_date', 'cardinality', "1.1"),
        ('increment', 'cardinality', "1.1"),

    ),
    time.TimePeriod: (

        ('date', 'type', time.DateTime),
        ('length', 'type', int),
        ('calendar', 'type', time.Calendar),
        ('units', 'type', unicode),
        ('date_type', 'type', unicode),

        ('date', 'cardinality', "0.1"),
        ('length', 'cardinality', "1.1"),
        ('calendar', 'cardinality', "0.1"),
        ('units', 'cardinality', "1.1"),
        ('date_type', 'cardinality', "1.1"),

    ),
    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------


    (activity.Activity, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Activity, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Activity, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Activity, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (activity.Activity, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Activity, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Activity, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Activity, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.Activity, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.Activity, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Activity, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Activity, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (activity.Activity, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (activity.AxisMember, 'description'): (

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

    (activity.Conformance, 'conformance_achieved'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.Conformance, 'target_requirement'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "1.1"),

    ),
    (activity.Conformance, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Conformance, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.Conformance, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.Conformance, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Conformance, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Conformance, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (activity.Conformance, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (activity.Ensemble, 'common_conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'documentation'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'has_ensemble_axes'): (

        ('type', activity.EnsembleAxis),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'members'): (

        ('type', activity.EnsembleMember),

        ('cardinality', "1.N"),

    ),
    (activity.Ensemble, 'part_of'): (

        ('type', activity.UberEnsemble),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'supported'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "1.N"),

    ),
    (activity.Ensemble, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.Ensemble, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.Ensemble, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.Ensemble, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (activity.Ensemble, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (activity.EnsembleAxis, 'extra_detail'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.EnsembleAxis, 'member'): (

        ('type', activity.AxisMember),

        ('cardinality', "1.N"),

    ),
    (activity.EnsembleAxis, 'short_identifier'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.EnsembleAxis, 'target_requirement'): (

        ('type', designing.NumericalRequirement),

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
    (activity.EnsembleMember, 'ran_on'): (

        ('type', platform.Machine),

        ('cardinality', "0.1"),

    ),
    (activity.EnsembleMember, 'simulation'): (

        ('type', data.Simulation),

        ('cardinality', "1.1"),

    ),

    (activity.ParentSimulation, 'branch_method'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.ParentSimulation, 'branch_time_in_child'): (

        ('type', time.DateTime),

        ('cardinality', "0.1"),

    ),
    (activity.ParentSimulation, 'branch_time_in_parent'): (

        ('type', time.DateTime),

        ('cardinality', "0.1"),

    ),
    (activity.ParentSimulation, 'parent'): (

        ('type', data.Simulation),

        ('cardinality', "1.1"),

    ),

    (activity.UberEnsemble, 'child_ensembles'): (

        ('type', activity.Ensemble),

        ('cardinality', "1.N"),

    ),
    (activity.UberEnsemble, 'common_conformances'): (

        ('type', activity.Conformance),

        ('cardinality', "0.N"),

    ),
    (activity.UberEnsemble, 'documentation'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.N"),

    ),
    (activity.UberEnsemble, 'has_ensemble_axes'): (

        ('type', activity.EnsembleAxis),

        ('cardinality', "0.N"),

    ),
    (activity.UberEnsemble, 'members'): (

        ('type', activity.EnsembleMember),

        ('cardinality', "1.N"),

    ),
    (activity.UberEnsemble, 'part_of'): (

        ('type', activity.UberEnsemble),

        ('cardinality', "0.N"),

    ),
    (activity.UberEnsemble, 'supported'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "1.N"),

    ),
    (activity.UberEnsemble, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.UberEnsemble, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.UberEnsemble, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.UberEnsemble, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (activity.UberEnsemble, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.UberEnsemble, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.UberEnsemble, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.UberEnsemble, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (activity.UberEnsemble, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (activity.UberEnsemble, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (activity.UberEnsemble, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (activity.UberEnsemble, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (activity.UberEnsemble, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (data.Dataset, 'availability'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.N"),

    ),
    (data.Dataset, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Dataset, 'drs_datasets'): (

        ('type', drs.DrsPublicationDataset),

        ('cardinality', "0.N"),

    ),
    (data.Dataset, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (data.Dataset, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (data.Dataset, 'produced_by'): (

        ('type', data.Simulation),

        ('cardinality', "0.1"),

    ),
    (data.Dataset, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (data.Dataset, 'related_to_dataset'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.N"),

    ),
    (data.Dataset, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (data.Downscaling, 'downscaled_from'): (

        ('type', data.Simulation),

        ('cardinality', "1.1"),

    ),
    (data.Downscaling, 'calendar'): (

        ('type', time.Calendar),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'contact'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'end_time'): (

        ('type', time.DateTime),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'extra_attributes'): (

        ('type', shared.ExtraAttribute),

        ('cardinality', "0.N"),

    ),
    (data.Downscaling, 'forcing_index'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'further_info_url'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'initialization_index'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'insitution'): (

        ('type', shared.Party),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'parent_simulation'): (

        ('type', activity.ParentSimulation),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'part_of_project'): (

        ('type', designing.Project),

        ('cardinality', "1.N"),

    ),
    (data.Downscaling, 'physics_index'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'primary_ensemble'): (

        ('type', activity.Ensemble),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'ran_for_experiments'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "1.N"),

    ),
    (data.Downscaling, 'realization_index'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (data.Downscaling, 'start_time'): (

        ('type', time.DateTime),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'sub_experiment'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'used'): (

        ('type', science.Model),

        ('cardinality', "1.1"),

    ),
    (data.Downscaling, 'variant_info'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (data.Downscaling, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (data.Downscaling, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (data.Downscaling, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (data.Downscaling, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Downscaling, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (data.Downscaling, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (data.Simulation, 'calendar'): (

        ('type', time.Calendar),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'contact'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'end_time'): (

        ('type', time.DateTime),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'extra_attributes'): (

        ('type', shared.ExtraAttribute),

        ('cardinality', "0.N"),

    ),
    (data.Simulation, 'forcing_index'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'further_info_url'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'initialization_index'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'insitution'): (

        ('type', shared.Party),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'parent_simulation'): (

        ('type', activity.ParentSimulation),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'part_of_project'): (

        ('type', designing.Project),

        ('cardinality', "1.N"),

    ),
    (data.Simulation, 'physics_index'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'primary_ensemble'): (

        ('type', activity.Ensemble),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'ran_for_experiments'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "1.N"),

    ),
    (data.Simulation, 'realization_index'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (data.Simulation, 'start_time'): (

        ('type', time.DateTime),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'sub_experiment'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'used'): (

        ('type', science.Model),

        ('cardinality', "1.1"),

    ),
    (data.Simulation, 'variant_info'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (data.Simulation, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (data.Simulation, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (data.Simulation, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (data.Simulation, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.Simulation, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (data.Simulation, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (data.VariableCollection, 'collection_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (data.VariableCollection, 'variables'): (

        ('type', unicode),

        ('cardinality', "1.N"),

    ),


    (designing.DomainRequirements, 'required_extent'): (

        ('type', science.Extent),

        ('cardinality', "0.1"),

    ),
    (designing.DomainRequirements, 'required_resolution'): (

        ('type', science.Resolution),

        ('cardinality', "0.1"),

    ),
    (designing.DomainRequirements, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (designing.DomainRequirements, 'is_conformance_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.DomainRequirements, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.DomainRequirements, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.DomainRequirements, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.DomainRequirements, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.DomainRequirements, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.DomainRequirements, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.DomainRequirements, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.DomainRequirements, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.DomainRequirements, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.DomainRequirements, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.DomainRequirements, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.DomainRequirements, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.DomainRequirements, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (designing.EnsembleRequirement, 'ensemble_member'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (designing.EnsembleRequirement, 'ensemble_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.EnsembleRequirement, 'minimum_size'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (designing.EnsembleRequirement, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (designing.EnsembleRequirement, 'is_conformance_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.EnsembleRequirement, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.EnsembleRequirement, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.EnsembleRequirement, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.EnsembleRequirement, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.EnsembleRequirement, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.EnsembleRequirement, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.EnsembleRequirement, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.EnsembleRequirement, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.EnsembleRequirement, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.EnsembleRequirement, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.EnsembleRequirement, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.EnsembleRequirement, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.EnsembleRequirement, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (designing.ForcingConstraint, 'additional_constraint'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'category'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'code'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'data_link'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'forcing_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.ForcingConstraint, 'group'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'origin'): (

        ('type', shared.Reference),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (designing.ForcingConstraint, 'is_conformance_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.ForcingConstraint, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.ForcingConstraint, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.ForcingConstraint, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.ForcingConstraint, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.ForcingConstraint, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.ForcingConstraint, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.ForcingConstraint, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (designing.InitialisationRequirement, 'branch_time_in_initialisation_source'): (

        ('type', time.DateTime),

        ('cardinality', "0.1"),

    ),
    (designing.InitialisationRequirement, 'initialise_from_data'): (

        ('type', data.Dataset),

        ('cardinality', "0.1"),

    ),
    (designing.InitialisationRequirement, 'initialise_from_experiment'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "0.1"),

    ),
    (designing.InitialisationRequirement, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (designing.InitialisationRequirement, 'is_conformance_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.InitialisationRequirement, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.InitialisationRequirement, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.InitialisationRequirement, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.InitialisationRequirement, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.InitialisationRequirement, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.InitialisationRequirement, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.InitialisationRequirement, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.InitialisationRequirement, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.InitialisationRequirement, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.InitialisationRequirement, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.InitialisationRequirement, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.InitialisationRequirement, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.InitialisationRequirement, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (designing.MultiEnsemble, 'ensemble_axis'): (

        ('type', designing.EnsembleRequirement),

        ('cardinality', "1.N"),

    ),
    (designing.MultiEnsemble, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (designing.MultiEnsemble, 'is_conformance_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.MultiEnsemble, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.MultiEnsemble, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.MultiEnsemble, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.MultiEnsemble, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.MultiEnsemble, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.MultiEnsemble, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.MultiEnsemble, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.MultiEnsemble, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.MultiEnsemble, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.MultiEnsemble, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.MultiEnsemble, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.MultiEnsemble, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.MultiEnsemble, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (designing.NumericalExperiment, 'related_experiments'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalExperiment, 'related_mips'): (

        ('type', designing.Project),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalExperiment, 'required_period'): (

        ('type', designing.TemporalConstraint),

        ('cardinality', "1.1"),

    ),
    (designing.NumericalExperiment, 'requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalExperiment, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalExperiment, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalExperiment, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalExperiment, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalExperiment, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalExperiment, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalExperiment, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalExperiment, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.NumericalExperiment, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.NumericalExperiment, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalExperiment, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalExperiment, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalExperiment, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (designing.NumericalRequirement, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalRequirement, 'is_conformance_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.NumericalRequirement, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalRequirement, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalRequirement, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalRequirement, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalRequirement, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalRequirement, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalRequirement, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalRequirement, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.NumericalRequirement, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.NumericalRequirement, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalRequirement, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.NumericalRequirement, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.NumericalRequirement, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (designing.OutputRequirement, 'formal_data_request'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.1"),

    ),
    (designing.OutputRequirement, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (designing.OutputRequirement, 'is_conformance_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.OutputRequirement, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.OutputRequirement, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.OutputRequirement, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.OutputRequirement, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.OutputRequirement, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.OutputRequirement, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.OutputRequirement, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.OutputRequirement, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.OutputRequirement, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.OutputRequirement, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.OutputRequirement, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.OutputRequirement, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.OutputRequirement, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (designing.Project, 'homepage'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.Project, 'objectives'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.Project, 'previous_projects'): (

        ('type', designing.Project),

        ('cardinality', "0.N"),

    ),
    (designing.Project, 'requires_experiments'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "0.N"),

    ),
    (designing.Project, 'sub_projects'): (

        ('type', designing.Project),

        ('cardinality', "0.N"),

    ),
    (designing.Project, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.Project, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.Project, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.Project, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.Project, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.Project, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.Project, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.Project, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.Project, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.Project, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.Project, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.Project, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.Project, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (designing.SimulationPlan, 'expected_model'): (

        ('type', science.Model),

        ('cardinality', "1.1"),

    ),
    (designing.SimulationPlan, 'expected_performance_sypd'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (designing.SimulationPlan, 'expected_platform'): (

        ('type', platform.Machine),

        ('cardinality', "0.1"),

    ),
    (designing.SimulationPlan, 'will_support_experiments'): (

        ('type', designing.NumericalExperiment),

        ('cardinality', "1.N"),

    ),
    (designing.SimulationPlan, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.SimulationPlan, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.SimulationPlan, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.SimulationPlan, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.SimulationPlan, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.SimulationPlan, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.SimulationPlan, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.SimulationPlan, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.SimulationPlan, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.SimulationPlan, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.SimulationPlan, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.SimulationPlan, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.SimulationPlan, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (designing.StartDateEnsemble, 'ensemble_members'): (

        ('type', time.DatetimeSet),

        ('cardinality', "1.1"),

    ),
    (designing.StartDateEnsemble, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (designing.StartDateEnsemble, 'is_conformance_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.StartDateEnsemble, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.StartDateEnsemble, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.StartDateEnsemble, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.StartDateEnsemble, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.StartDateEnsemble, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.StartDateEnsemble, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.StartDateEnsemble, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.StartDateEnsemble, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.StartDateEnsemble, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.StartDateEnsemble, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.StartDateEnsemble, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.StartDateEnsemble, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.StartDateEnsemble, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (designing.TemporalConstraint, 'required_calendar'): (

        ('type', time.Calendar),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'required_duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'start_date'): (

        ('type', time.DateTime),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'start_flexibility'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),

        ('cardinality', "0.N"),

    ),
    (designing.TemporalConstraint, 'is_conformance_requested'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (designing.TemporalConstraint, 'alternative_names'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.TemporalConstraint, 'canonical_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'duration'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'internal_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (designing.TemporalConstraint, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (designing.TemporalConstraint, 'previously_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (designing.TemporalConstraint, 'rationale'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (designing.TemporalConstraint, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (designing.TemporalConstraint, 'responsible_parties'): (

        ('type', shared.Responsibility),

        ('cardinality', "0.N"),

    ),

    (drs.DrsAtomicDataset, 'frequency'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsAtomicDataset, 'geographical_constraint'): (

        ('type', drs.DrsGeographicalIndicator),

        ('cardinality', "0.1"),

    ),
    (drs.DrsAtomicDataset, 'mip_table'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsAtomicDataset, 'realm'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (drs.DrsAtomicDataset, 'temporal_constraint'): (

        ('type', drs.DrsTemporalIdentifier),

        ('cardinality', "0.1"),

    ),
    (drs.DrsAtomicDataset, 'variable_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsAtomicDataset, 'version_number'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (drs.DrsEnsembleIdentifier, 'forcing_number'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (drs.DrsEnsembleIdentifier, 'initialisation_method_number'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (drs.DrsEnsembleIdentifier, 'perturbation_number'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (drs.DrsEnsembleIdentifier, 'realisation_number'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),

    (drs.DrsExperiment, 'axis_identifer'): (

        ('type', designing.AxisMember),

        ('cardinality', "0.1"),

    ),
    (drs.DrsExperiment, 'axis_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (drs.DrsExperiment, 'family'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (drs.DrsGeographicalIndicator, 'bounding_box'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (drs.DrsGeographicalIndicator, 'operator'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (drs.DrsGeographicalIndicator, 'spatial_domain'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),


    (drs.DrsSimulationIdentifier, 'institute'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsSimulationIdentifier, 'model'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (drs.DrsSimulationIdentifier, 'run_variant_id'): (

        ('type', drs.DrsEnsembleIdentifier),

        ('cardinality', "1.1"),

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

    (platform.ComponentPerformance, 'component'): (

        ('type', software.SoftwareComponent),

        ('cardinality', "0.1"),

    ),
    (platform.ComponentPerformance, 'component_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (platform.ComponentPerformance, 'cores_used'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (platform.ComponentPerformance, 'nodes_used'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (platform.ComponentPerformance, 'speed'): (

        ('type', float),

        ('cardinality', "1.1"),

    ),

    (platform.ComputePool, 'accelerator_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'accelerators_per_node'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'compute_cores_per_node'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'cpu_type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'interconnect'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'memory_per_node'): (

        ('type', platform.StorageVolume),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'model_number'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'number_of_nodes'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (platform.ComputePool, 'operating_system'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (platform.Machine, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (platform.Machine, 'compute_pools'): (

        ('type', platform.ComputePool),

        ('cardinality', "1.N"),

    ),
    (platform.Machine, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.Machine, 'institution'): (

        ('type', shared.Party),

        ('cardinality', "1.1"),

    ),
    (platform.Machine, 'model_number'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.Machine, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (platform.Machine, 'online_documentation'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.N"),

    ),
    (platform.Machine, 'partition'): (

        ('type', platform.Partition),

        ('cardinality', "0.N"),

    ),
    (platform.Machine, 'storage_pools'): (

        ('type', platform.StoragePool),

        ('cardinality', "0.N"),

    ),
    (platform.Machine, 'vendor'): (

        ('type', shared.Party),

        ('cardinality', "0.1"),

    ),
    (platform.Machine, 'when_used'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),

    (platform.Partition, 'compute_pools'): (

        ('type', platform.ComputePool),

        ('cardinality', "1.N"),

    ),
    (platform.Partition, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.Partition, 'institution'): (

        ('type', shared.Party),

        ('cardinality', "1.1"),

    ),
    (platform.Partition, 'model_number'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.Partition, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (platform.Partition, 'online_documentation'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.N"),

    ),
    (platform.Partition, 'partition'): (

        ('type', platform.Partition),

        ('cardinality', "0.N"),

    ),
    (platform.Partition, 'storage_pools'): (

        ('type', platform.StoragePool),

        ('cardinality', "0.N"),

    ),
    (platform.Partition, 'vendor'): (

        ('type', shared.Party),

        ('cardinality', "0.1"),

    ),
    (platform.Partition, 'when_used'): (

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),

    (platform.Performance, 'asypd'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'chsy'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'compiler'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'coupler_load'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'io_load'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'load_imbalance'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'memory_bloat'): (

        ('type', float),

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
    (platform.Performance, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'platform'): (

        ('type', platform.Machine),

        ('cardinality', "1.1"),

    ),
    (platform.Performance, 'subcomponent_performance'): (

        ('type', platform.ComponentPerformance),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'sypd'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (platform.Performance, 'total_nodes_used'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),

    (platform.StoragePool, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (platform.StoragePool, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (platform.StoragePool, 'type'): (

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

    (platform.StorageVolume, 'units'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (platform.StorageVolume, 'volume'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),

    (science.ConservationProperties, 'corrected_conserved_prognostic_variables'): (

        ('type', data.VariableCollection),

        ('cardinality', "0.1"),

    ),
    (science.ConservationProperties, 'flux_correction_was_used'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (science.ConservationProperties, 'details'): (

        ('type', science.Detail),

        ('cardinality', "0.N"),

    ),
    (science.ConservationProperties, 'implementation_overview'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.ConservationProperties, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (science.ConservationProperties, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.ConservationProperties, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.ConservationProperties, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (science.Detail, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Detail, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Detail, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (science.Discretisation, 'details'): (

        ('type', science.Detail),

        ('cardinality', "0.N"),

    ),
    (science.Discretisation, 'implementation_overview'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Discretisation, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (science.Discretisation, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Discretisation, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Discretisation, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (science.Extent, 'is_global'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (science.Extent, 'region_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (science.Extent, 'details'): (

        ('type', science.Detail),

        ('cardinality', "0.N"),

    ),
    (science.Extent, 'implementation_overview'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Extent, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (science.Extent, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Extent, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Extent, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (science.Grid, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Grid, 'details'): (

        ('type', science.Detail),

        ('cardinality', "0.N"),

    ),
    (science.Grid, 'discretisation'): (

        ('type', science.Discretisation),

        ('cardinality', "0.1"),

    ),
    (science.Grid, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (science.Grid, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Grid, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),

    (science.IsoExtent, 'eastern_boundary'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (science.IsoExtent, 'northern_boundary'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (science.IsoExtent, 'southern_boundary'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (science.IsoExtent, 'western_boundary'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (science.IsoExtent, 'is_global'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),
    (science.IsoExtent, 'region_known_as'): (

        ('type', unicode),

        ('cardinality', "0.N"),

    ),
    (science.IsoExtent, 'details'): (

        ('type', science.Detail),

        ('cardinality', "0.N"),

    ),
    (science.IsoExtent, 'implementation_overview'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.IsoExtent, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (science.IsoExtent, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.IsoExtent, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.IsoExtent, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (science.KeyProperties, 'extent'): (

        ('type', science.Extent),

        ('cardinality', "0.1"),

    ),
    (science.KeyProperties, 'extra_conservation_properties'): (

        ('type', science.ConservationProperties),

        ('cardinality', "0.1"),

    ),
    (science.KeyProperties, 'resolution'): (

        ('type', science.Resolution),

        ('cardinality', "0.1"),

    ),
    (science.KeyProperties, 'time_step'): (

        ('type', float),

        ('cardinality', "0.1"),

    ),
    (science.KeyProperties, 'tuning_applied'): (

        ('type', science.Tuning),

        ('cardinality', "0.1"),

    ),
    (science.KeyProperties, 'details'): (

        ('type', science.Detail),

        ('cardinality', "0.N"),

    ),
    (science.KeyProperties, 'implementation_overview'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.KeyProperties, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.KeyProperties, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (science.KeyProperties, 'sub_processes'): (

        ('type', science.SubProcess),

        ('cardinality', "0.N"),

    ),
    (science.KeyProperties, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.KeyProperties, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.KeyProperties, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (science.Model, 'category'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Model, 'coupled_components'): (

        ('type', science.Model),

        ('cardinality', "0.N"),

    ),
    (science.Model, 'coupler'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'internal_software_components'): (

        ('type', software.SoftwareComponent),

        ('cardinality', "0.N"),

    ),
    (science.Model, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (science.Model, 'model_key_properties'): (

        ('type', science.KeyProperties),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'simulates'): (

        ('type', science.ScientificRealm),

        ('cardinality', "0.N"),

    ),
    (science.Model, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'development_history'): (

        ('type', software.DevelopmentPath),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'documentation'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (science.Model, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Model, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'repository'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.1"),

    ),
    (science.Model, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (science.Process, 'details'): (

        ('type', science.Detail),

        ('cardinality', "0.N"),

    ),
    (science.Process, 'implementation_overview'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Process, 'keywords'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Process, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (science.Process, 'sub_processes'): (

        ('type', science.SubProcess),

        ('cardinality', "0.N"),

    ),
    (science.Process, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Process, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Process, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (science.Resolution, 'canonical_horizontal_resolution'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.Resolution, 'is_adaptive_grid'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (science.Resolution, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Resolution, 'number_of_horizontal_gridpoints'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (science.Resolution, 'number_of_vertical_levels'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (science.Resolution, 'details'): (

        ('type', science.Detail),

        ('cardinality', "0.N"),

    ),
    (science.Resolution, 'implementation_overview'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Resolution, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (science.Resolution, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Resolution, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Resolution, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (science.ScienceContext, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.ScienceContext, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.ScienceContext, 'short_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (science.ScientificRealm, 'grid'): (

        ('type', science.Grid),

        ('cardinality', "0.1"),

    ),
    (science.ScientificRealm, 'id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.ScientificRealm, 'key_properties'): (

        ('type', science.KeyProperties),

        ('cardinality', "0.1"),

    ),
    (science.ScientificRealm, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (science.ScientificRealm, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.ScientificRealm, 'overview'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.ScientificRealm, 'realm'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (science.ScientificRealm, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (science.ScientificRealm, 'simulates'): (

        ('type', science.Process),

        ('cardinality', "1.N"),

    ),

    (science.SubProcess, 'details'): (

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
    (science.SubProcess, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.SubProcess, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.SubProcess, 'short_name'): (

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
    (science.Tuning, 'details'): (

        ('type', science.Detail),

        ('cardinality', "0.N"),

    ),
    (science.Tuning, 'implementation_overview'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Tuning, 'references'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (science.Tuning, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Tuning, 'id'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (science.Tuning, 'short_name'): (

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

    (shared.Citation, 'abstract'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'citation_detail'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'collective_title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'context'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'doi'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (shared.Citation, 'title'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Citation, 'url'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.1"),

    ),

    (shared.CitationTarget, 'citation_detail'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.CitationTarget, 'doi'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.CitationTarget, 'meta'): (

        ('type', shared.DocMetaInfo),

        ('cardinality', "1.1"),

    ),
    (shared.CitationTarget, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.CitationTarget, 'online_at'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.1"),

    ),
    (shared.CitationTarget, 'title'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.DocMetaInfo, 'author'): (

        ('type', shared.Party),

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
    (shared.DocMetaInfo, 'language'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'project'): (

        ('type', unicode),

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

        ('cardinality', "1.1"),

    ),
    (shared.DocMetaInfo, 'version'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),

    (shared.DocReference, 'constraint_vocabulary'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'context'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'id'): (

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
    (shared.DocReference, 'version'): (

        ('type', int),

        ('cardinality', "0.1"),

    ),
    (shared.DocReference, 'description'): (

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

    (shared.ExtraAttribute, 'doc'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ExtraAttribute, 'key'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.ExtraAttribute, 'type'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.ExtraAttribute, 'value'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (shared.OnlineResource, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.OnlineResource, 'linkage'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.OnlineResource, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.OnlineResource, 'protocol'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (shared.Party, 'address'): (

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
    (shared.Party, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Party, 'orcid_id'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Party, 'organisation'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (shared.Party, 'url'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.1"),

    ),

    (shared.QualityReview, 'date'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (shared.QualityReview, 'meta'): (

        ('type', shared.DocMetaInfo),

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
    (shared.QualityReview, 'target_document'): (

        ('type', shared.DocReference),

        ('cardinality', "1.1"),

    ),

    (shared.Reference, 'context'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (shared.Reference, 'document'): (

        ('type', shared.CitationTarget),

        ('cardinality', "1.1"),

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

        ('type', time.TimePeriod),

        ('cardinality', "0.1"),

    ),

    (software.ComponentBase, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentBase, 'development_history'): (

        ('type', software.DevelopmentPath),

        ('cardinality', "0.1"),

    ),
    (software.ComponentBase, 'documentation'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (software.ComponentBase, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.ComponentBase, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.ComponentBase, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.ComponentBase, 'repository'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.1"),

    ),
    (software.ComponentBase, 'version'): (

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

    (software.DevelopmentPath, 'consortium_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

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
    (software.DevelopmentPath, 'previous_version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.EntryPoint, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.Gridspec, 'description'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (software.SoftwareComponent, 'composition'): (

        ('type', software.Composition),

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
    (software.SoftwareComponent, 'dependencies'): (

        ('type', software.EntryPoint),

        ('cardinality', "0.N"),

    ),
    (software.SoftwareComponent, 'grid'): (

        ('type', software.Gridspec),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'language'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'license'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'sub_components'): (

        ('type', software.SoftwareComponent),

        ('cardinality', "0.N"),

    ),
    (software.SoftwareComponent, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'development_history'): (

        ('type', software.DevelopmentPath),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'documentation'): (

        ('type', shared.Reference),

        ('cardinality', "0.N"),

    ),
    (software.SoftwareComponent, 'long_name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.SoftwareComponent, 'release_date'): (

        ('type', datetime.datetime),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'repository'): (

        ('type', shared.OnlineResource),

        ('cardinality', "0.1"),

    ),
    (software.SoftwareComponent, 'version'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),

    (software.Variable, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (software.Variable, 'name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (software.Variable, 'prognostic'): (

        ('type', bool),

        ('cardinality', "1.1"),

    ),

    (time.Calendar, 'description'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (time.Calendar, 'month_lengths'): (

        ('type', int),

        ('cardinality', "0.N"),

    ),
    (time.Calendar, 'name'): (

        ('type', unicode),

        ('cardinality', "0.1"),

    ),
    (time.Calendar, 'standard_name'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (time.DateTime, 'offset'): (

        ('type', bool),

        ('cardinality', "0.1"),

    ),
    (time.DateTime, 'value'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),

    (time.DatetimeSet, 'length'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),

    (time.IrregularDateset, 'date_set'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (time.IrregularDateset, 'length'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),

    (time.RegularTimeset, 'increment'): (

        ('type', time.TimePeriod),

        ('cardinality', "1.1"),

    ),
    (time.RegularTimeset, 'length'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (time.RegularTimeset, 'start_date'): (

        ('type', time.DateTime),

        ('cardinality', "1.1"),

    ),
    (time.RegularTimeset, 'length'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),

    (time.TimePeriod, 'calendar'): (

        ('type', time.Calendar),

        ('cardinality', "0.1"),

    ),
    (time.TimePeriod, 'date'): (

        ('type', time.DateTime),

        ('cardinality', "0.1"),

    ),
    (time.TimePeriod, 'date_type'): (

        ('type', unicode),

        ('cardinality', "1.1"),

    ),
    (time.TimePeriod, 'length'): (

        ('type', int),

        ('cardinality', "1.1"),

    ),
    (time.TimePeriod, 'units'): (

        ('type', unicode),

        ('cardinality', "1.1"),

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
    designing: "Types that describe project design features.",
    drs: "Types that describe the directory structures to which climate model output is written.",
    platform: "Types that describe hardware upon which climate models are run.",
    science: "Types that describe the science being performed.",
    shared: "Shared types that might be imported from other packages within the ontology.",
    software: "Types that describe the software that constiutes a climate model.",
    time: "Types that describe the software that constiutes a climate model.",

    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    activity.Activity: """
        Base class for activities.

    """,
    activity.AxisMember: """
        Description of a given ensemble member. It will normally be related to a specific
    ensemble requirement. Note that start dates can be extracted directly from the simulations
    and do not need to be recorded with an axis member description.

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
    activity.EnsembleAxis: """
        Defines the meaning of r/i/p indices in an ensemble.

    """,
    activity.EnsembleMember: """
        An ensemble may be a complicated interplay of axes, for example, r/i/p, not all of which
    are populated, so we need a list of the actual simulations and how they map onto the ensemble
    axes.

    """,
    activity.ParentSimulation: """
        Defines the relationship between a simulation and its parent.

    """,
    activity.UberEnsemble: """
        An ensemble made up of other ensembles. Often used where parts of an ensemble were run by
    different institutes. Could also be used when a new experiment is designed which can use
    ensemble members from previous experiments and/or projects.

    """,
    data.Dataset: """
        Dataset discovery information.

    """,
    data.Downscaling: """
        Defines a downscaling activity.

    """,
    data.Simulation: """
        Simulation class provides the integrating link about what models were run and wny.
    In many cases this should be auto-generated from output file headers.

    """,
    data.VariableCollection: """
        A collection of variables within the scope of a code or process element.

    """,
    designing.AxisMember: """
        PLACEHOLDER for the real axis_member.

    """,
    designing.DomainRequirements: """
        Properties of the domain which needs to be simulated, extent and/or resolution.

    """,
    designing.EnsembleRequirement: """
        Defines an experiment ensemble.

    """,
    designing.ForcingConstraint: """
        Identifies a model forcing constraint.

    """,
    designing.InitialisationRequirement: """
        A requirement on how a particular simulation should be initialised.

    """,
    designing.MultiEnsemble: """
        In the case of multiple ensemble axes, defines how they
    are set up and ordered.

    """,
    designing.NumericalExperiment: """
        Defines a numerical experiment.

    """,
    designing.NumericalRequirement: """
        A numerical requirement associated with a numerical experiment.

    """,
    designing.OutputRequirement: """
        Provides details of what output is required and when from an experiment.

    """,
    designing.Project: """
        Describes a scientific project.

    """,
    designing.SimulationPlan: """
        Describes a simulation that needs to be run.

    """,
    designing.StartDateEnsemble: """
        Defines an experiment ensemble with multiple start dates.

    """,
    designing.TemporalConstraint: """
        A temporal constraint on a numerical experiment.

    """,
    drs.DrsAtomicDataset: """
        An entity in a DRS file system.

    """,
    drs.DrsEnsembleIdentifier: """
        Identifies a 'response ensemble' realisation using the semantic content ofa 'run_variant_id'.

    """,
    drs.DrsExperiment: """
        An encoding of a drs experiment_id.

    """,
    drs.DrsGeographicalIndicator: """
        Specifies geographical subsets described by bounding boxes or by named regions.
     One of spatial domain or bounding box must appear.

    """,
    drs.DrsPublicationDataset: """
        PLACEHOLDER for the real drs_publication_dataset.

    """,
    drs.DrsSimulationIdentifier: """
        That part of the DRS which identifies the response to the experiment: the simulation.

    """,
    drs.DrsTemporalIdentifier: """
        Provides information about temporal subsetting and/or averaging.
    If only N1 is present, it a temporal instant,
    If N1-N2 are present with no suffix, it is a temporal subset,
    If N1-N2 with a suffix are present, then some sort of temporal averaging has been applied across
    the period.

    """,
    platform.ComponentPerformance: """
        Describes the simulation rate of a component in seconds per model day.

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
    platform.Performance: """
        Describes the properties of a performance of a configured model on a particular system/machine.

    """,
    platform.StoragePool: """
        Homogeneous storage pool on a computing machine.

    """,
    platform.StorageVolume: """
        Volume and units.

    """,
    science.ConservationProperties: """
        Describes how prognostic variables are conserved.

    """,
    science.Detail: """
        Provides details of specific properties of a process, sub-process,
    key properties, etc., there are two possible specialisations
    expected: (1) A detail_vocabulary is identified, and a cardinality
    is assigned to that for possible responses, or (2) Detail is used
    to provide a collection for a set of properties which are defined
    in the sub-class. However, those properties must have a type which
    is selected from the classmap (that is, standard 'non-es-doc'
    types).

    """,
    science.Discretisation: """
        Collection of properties related to method of process discretisation.

    """,
    science.Extent: """
        Key scientific characteristics of the grid use to simulate a
    specific domain.  Note that the extent does not itself describe a
    grid, so, for example, a polar stereographic grid may have an
    extent of northern boundary 90N, southern boundary 45N, but the
    fact that it is PS comes from the grid_type.

    """,
    science.Grid: """
        This describes the numerical grid used for the calculations.  It
    is not necessarily the grid upon which the data is output.  It is
    NOT the resolution, which is a property of a specific domain.

    """,
    science.IsoExtent: """
        Extent on a latitude-longitudinal grid - to aid traditional cartesian discovery.

    """,
    science.KeyProperties: """
        High level list of key properties. It can be specialised in
    extension packages using the detail extensions.

    """,
    science.Model: """
        A model component: can be executed standalone, and has as
    scientific description available via a link to a science.domain
    document. (A configured model can be understood in terms of a
    simulation, a model, and a configuration.).

    """,
    science.Process: """
        Provides structure for description of a process simulated within a
    particular area (or domain/realm/component) of a model. This will
    often be subclassed within a specific implementation so that
    constraints can be used to ensure that the process details
    requested are consistent with project requirements for
    information.

    """,
    science.Resolution: """
        Describes the computational spatial resolution of a component or
    process.  Not intended to replace or replicate the output grid
    description.  When it appears as part of a process description,
    provide only properties that differ from parent domain.  Note that
    this is supposed to capture gross features of the grid, we expect
    many grids will have different variable layouts, those should be
    described in the grid description, and the exact resolution is not
    required. Note that many properties are not appropriate for
    adaptive grids.

    """,
    science.ScienceContext: """
        This is the base class for the science mixins, that is the classes
    which we expect to be specialised and extended by project specific
    vocabularies.  It is expected that values of these will be
    provided within vocabulary definitions.

    """,
    science.ScientificRealm: """
        Scientific area of a numerical model - usually a sub-model or
    component.  Can also be known as a realm.

    """,
    science.SubProcess: """
        Provides structure for description of part of process simulated
    within a particular area (or domain/realm/component) of a
    model. Typically this will be a part of process which shares
    common properties. It will normally be sub classed within a
    specific implementation so that constraints can be used to ensure
    that the process details requested are consistent with projects
    requirements for information.

    """,
    science.Tuning: """
        Method used to optimise equation parameters in model component
    (aka 'tuning').

    """,
    shared.Cimtext: """
        Provides a text class which supports plaintext, html, and
    friends (or will do).

    """,
    shared.Citation: """
        An academic reference to published work.

    """,
    shared.CitationTarget: """
        A real world document, could be a book, a journal article, a manual, a web page ... it might or might
    not be online, although preferably it would be.

    """,
    shared.DocMetaInfo: """
        Encapsulates document meta information used by es-doc machinery. Will not normally be
    populated by humans. May duplicate information held in 'visible' metadata.

    """,
    shared.DocReference: """
        Specialisation of online resource for link between CIM documents, whether the
    remote document exists when complete, or not.

    """,
    shared.ExtraAttribute: """
        An extra attribute with key and value needed to encode further information
    not in the CIM2 domain model or specialisation. Typical use case: in parsing
    data and encoding attributes found in data.

    """,
    shared.OnlineResource: """
        A minimal approximation of ISO19115 CI_ONLINERESOURCE, provides a link and details
    of how to use that link.

    """,
    shared.Party: """
        Implements minimal material for an ISO19115-1 (2014) compliant party.
    For our purposes this is a much better animal than the previous responsibleParty 
    which munged roles together with people. Note we have collapsed CI_Contact,
    CI_Individual and CI_Organisation as well as the abstract CI_Party.

    """,
    shared.QualityReview: """
        Assertions as to the completeness and quality of a document.

    """,
    shared.Reference: """
        An external citation target which can have a context associated with it.

    """,
    shared.Responsibility: """
        Implements the ISO19115-1 (2014) CI_Responsibility (which replaces
    responsibleParty). Combines a person and their role in doing something.

    """,
    software.ComponentBase: """
        Base class for software component properties, whether a top level model,
    or a specific piece of code known as a component. In software terms, a
    component is a discrete set of code that takes input data and generates output data.
    Components may or may not have scientific descriptions.

    """,
    software.Composition: """
        Describes how component variables are coupled together either to/from other
    SoftwareComponents or external data files. The variables specified by a component's
    composition must be owned by that component, or a  child of that component;
    child components cannot couple together parent variables.

    """,
    software.DevelopmentPath: """
        Describes the software development path for this model/component.

    """,
    software.EntryPoint: """
        Describes a function or subroutine of a SoftwareComponent.
    BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model.
    Currently, a very basic schedule can be approximated by using the 'proceeds' and 'follows' attributes,
    however a more complete system is required for full BFG compatibility.
    Every EntryPoint can have a set of arguments associated with it.
    These reference (previously defined) variables.

    """,
    software.Gridspec: """
        Fully defines the computational grid used.

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
    time.Calendar: """
        Describes the calendar required/used in an experiment/simulation.
    This class is based on the calendar attributes and properties found in the
    CF netCDF conventions.

    """,
    time.DateTime: """
        A date or time. Either in simulation time with the simulation
    calendar, or with reference to a simulation start, in which
    case the datetime is an interval after the start date.

    """,
    time.DatetimeSet: """
        A set of times. This is an abstract class which is specialised into
    a periodic or aperiodic (irregular) list.  Note that we assume either a
    periodic set of dates which can be date and/or time, or an irregular set
    which can only be dates.

    """,
    time.IrregularDateset: """
        A set of irregularly spaced times, provided as a comma separated string of yyyy-mm-dd in
     the appropriate calendar.

    """,
    time.RegularTimeset: """
        A regularly spaced set of times.

    """,
    time.TimePeriod: """
        A time period/interval (aka temporal extent).

    """,

    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------

    (activity.Activity, 'alternative_names'):
        "List of names by which the activity is also known.",
    (activity.Activity, 'canonical_name'):
        "Community defined identifier or name.",
    (activity.Activity, 'description'):
        "Description of what is to be done (or was done).",
    (activity.Activity, 'duration'):
        "Time the activity was (or will be) active.",
    (activity.Activity, 'internal_name'):
        "A name used for internal purposes.",
    (activity.Activity, 'keywords'):
        "Comma separated user defined keywords.",
    (activity.Activity, 'long_name'):
        "Longer version of activity name.",
    (activity.Activity, 'meta'):
        "Metadata describing how this document was created.",
    (activity.Activity, 'name'):
        "Short name or abbreviation.",
    (activity.Activity, 'previously_known_as'):
        "List of names by which the activity was formerly known.",
    (activity.Activity, 'rationale'):
        "Explanation of why this activity was carried out and/or what it was intended to achieve.",
    (activity.Activity, 'references'):
        "Relevant documentation.",
    (activity.Activity, 'responsible_parties'):
        "People or organisations responsible for activity.",
    (activity.AxisMember, 'description'):
        "Description of the member (or name of parameter varied).",
    (activity.AxisMember, 'extra_detail'):
        "If necessary: further information about ensemble member conformance.",
    (activity.AxisMember, 'index'):
        "The ensemble member index.",
    (activity.AxisMember, 'value'):
        "If parameter varied, value thereof for this member.",
    (activity.Conformance, 'conformance_achieved'):
        "Summary of conformance status.",
    (activity.Conformance, 'target_requirement'):
        "URI of the target numerical requirement.",
    (activity.Ensemble, 'common_conformances'):
        "Conformance documents for requirements common across ensemble.",
    (activity.Ensemble, 'documentation'):
        "Links to web-pages and other ensemble specific documentation (including workflow descriptions).",
    (activity.Ensemble, 'has_ensemble_axes'):
        "Set of axes for the ensemble.",
    (activity.Ensemble, 'members'):
        "The set of ensemble members.",
    (activity.Ensemble, 'part_of'):
        "Link to one or more over-arching ensembles that might includes this one.",
    (activity.Ensemble, 'supported'):
        "Experiments with which the ensemble is associated (may differ from constituent simulations).",
    (activity.EnsembleAxis, 'extra_detail'):
        "Any extra detail required to describe how this ensemble axis was delivered.",
    (activity.EnsembleAxis, 'member'):
        "Individual member descriptions along axis.",
    (activity.EnsembleAxis, 'short_identifier'):
        "e.g. 'r' or 'i' or 'p' to conform with simulation ensemble variant identifiers.",
    (activity.EnsembleAxis, 'target_requirement'):
        "URI of the target numerical requirement.",
    (activity.EnsembleMember, 'errata'):
        "Link to errata associated with this simulation.",
    (activity.EnsembleMember, 'had_performance'):
        "Performance of the simulation.",
    (activity.EnsembleMember, 'ran_on'):
        "The machine on which the simulation was run.",
    (activity.EnsembleMember, 'simulation'):
        "Actual simulation description for an ensemble member. The variant id is in the simuluation document.",
    (activity.ParentSimulation, 'branch_method'):
        "Description of how the simulation was branched from a parent simualtion, e.g. 'standard', 'none provided'.",
    (activity.ParentSimulation, 'branch_time_in_child'):
        "The time at which the present simulation started in the child calendar.",
    (activity.ParentSimulation, 'branch_time_in_parent'):
        "The time in parent simulation calendar at which this simulation was branched.",
    (activity.ParentSimulation, 'parent'):
        "The parent simulation of this child.",
    (activity.UberEnsemble, 'child_ensembles'):
        "Ensemble which are aggregated into this one.",
    (data.Dataset, 'availability'):
        "Where the data is located, and how it is accessed.",
    (data.Dataset, 'description'):
        "Textural description of dataset.",
    (data.Dataset, 'drs_datasets'):
        "Data available in the DRS.",
    (data.Dataset, 'meta'):
        "Metadata describing the creation of this dataset description document.",
    (data.Dataset, 'name'):
        "Name of dataset.",
    (data.Dataset, 'produced_by'):
        "Makes a link back to originating activity.",
    (data.Dataset, 'references'):
        "Relevant reference document.",
    (data.Dataset, 'related_to_dataset'):
        "Related dataset.",
    (data.Dataset, 'responsible_parties'):
        "Individuals and organisations reponsible for the data.",
    (data.Downscaling, 'downscaled_from'):
        "The simulation that was downscaled by this downscaling activity.",
    (data.Simulation, 'calendar'):
        "The calendar used in the simulation.",
    (data.Simulation, 'contact'):
        "None",
    (data.Simulation, 'end_time'):
        "The start date-time of the simulation. e.g. 2087-11-30 12:00:00.",
    (data.Simulation, 'extra_attributes'):
        "Additional attributes provided with simulation.",
    (data.Simulation, 'forcing_index'):
        "index for variant of forcing, e.g. 2.",
    (data.Simulation, 'further_info_url'):
        "On-line location of documentation.",
    (data.Simulation, 'initialization_index'):
        "Index variant of initialization method, e.g. 1.",
    (data.Simulation, 'insitution'):
        "Institution which carried out the simulation.",
    (data.Simulation, 'parent_simulation'):
        "If appropriate, detailed information about how this simulation branched from a previous one.",
    (data.Simulation, 'part_of_project'):
        "Project or projects for which simulation was run.",
    (data.Simulation, 'physics_index'):
        "index for model physics, e.g. 3.",
    (data.Simulation, 'primary_ensemble'):
        "Primary Ensemble (ensemble for which this simulation was first run).",
    (data.Simulation, 'ran_for_experiments'):
        "One or more experiments with which the simulation is associated.",
    (data.Simulation, 'realization_index'):
        "realization number, e.g. 5.",
    (data.Simulation, 'references'):
        "Published or web-based references that describe the data or methods used to produce it.",
    (data.Simulation, 'start_time'):
        "The start date-time of the simulation. e.g. 2012-04-01 00:00:00.",
    (data.Simulation, 'sub_experiment'):
        "For start-date ensembles, this will indicate the beginning year; for offline models driven by output from another model, this will provide the source_id and variant_label for the 'driving' model.",
    (data.Simulation, 'used'):
        "The model used to run the simulation.",
    (data.Simulation, 'variant_info'):
        "description of run variant differences, e.g. 'forcing: black carbon aerosol only'.",
    (data.VariableCollection, 'collection_name'):
        "Name for this variable collection.",
    (data.VariableCollection, 'variables'):
        "Set of variable names.",
    (designing.DomainRequirements, 'required_extent'):
        "Constraint on extent of domain to be simulated.",
    (designing.DomainRequirements, 'required_resolution'):
        "Constraint on resolution required in simulated domain.",
    (designing.EnsembleRequirement, 'ensemble_member'):
        "Constraint on each ensemble member.",
    (designing.EnsembleRequirement, 'ensemble_type'):
        "Type of ensemble.",
    (designing.EnsembleRequirement, 'minimum_size'):
        "Minimum number of members.",
    (designing.ForcingConstraint, 'additional_constraint'):
        "Additional information, e.g. hold constant from 2100-01-01.",
    (designing.ForcingConstraint, 'category'):
        "Category to which this belongs (from a CV, e.g. GASES).",
    (designing.ForcingConstraint, 'code'):
        "Programme wide code from a controlled vocabulary (e.g. N2O).",
    (designing.ForcingConstraint, 'data_link'):
        "Link to actual data record if possible.",
    (designing.ForcingConstraint, 'forcing_type'):
        "Type of integration.",
    (designing.ForcingConstraint, 'group'):
        "Sub-Category (e.g. GHG).",
    (designing.ForcingConstraint, 'origin'):
        "Pointer to origin, e.g. CMIP6 RCP database.",
    (designing.InitialisationRequirement, 'branch_time_in_initialisation_source'):
        "If appropriate,  the time in the initialisation_source (whether observed or simulated).",
    (designing.InitialisationRequirement, 'initialise_from_data'):
        "Initialisation should use this primary dataset.",
    (designing.InitialisationRequirement, 'initialise_from_experiment'):
        "This experiment should be initialised from the output of this experiment.",
    (designing.MultiEnsemble, 'ensemble_axis'):
        "List of orthogonal ensembles.",
    (designing.NumericalExperiment, 'related_experiments'):
        "Other experiments which have defined relationships to this one.",
    (designing.NumericalExperiment, 'related_mips'):
        "MIP's that require this experiment.",
    (designing.NumericalExperiment, 'required_period'):
        "Constraint on start date and duration.",
    (designing.NumericalExperiment, 'requirements'):
        "Additional requirements that conformant simulations need to satisfy.",
    (designing.NumericalRequirement, 'additional_requirements'):
        "Additional detail for this requirement.",
    (designing.NumericalRequirement, 'is_conformance_requested'):
        "Indicator as to whether ensemble documentation should include conformance information for this requirement.",
    (designing.OutputRequirement, 'formal_data_request'):
        "If available, link to a 'cmip' style online request.",
    (designing.Project, 'homepage'):
        "Project homepage.",
    (designing.Project, 'objectives'):
        "Project objectives.",
    (designing.Project, 'previous_projects'):
        "Previous projects with similar aims.",
    (designing.Project, 'requires_experiments'):
        "Experiments required to deliver project.",
    (designing.Project, 'sub_projects'):
        "Activities within the project with their own name and aim(s).",
    (designing.SimulationPlan, 'expected_model'):
        "The model used to run the simulation.",
    (designing.SimulationPlan, 'expected_performance_sypd'):
        "Expected performance in simulated years per real day.",
    (designing.SimulationPlan, 'expected_platform'):
        "The machine on which the simulation will be run.",
    (designing.SimulationPlan, 'will_support_experiments'):
        "An experiment with which the planned simulation will be associated.",
    (designing.StartDateEnsemble, 'ensemble_members'):
        "Description of date or time set of start dates.",
    (designing.TemporalConstraint, 'required_calendar'):
        "Required calendar (e.g. for paleo simulations).",
    (designing.TemporalConstraint, 'required_duration'):
        "Constraint on time or length of simulation.",
    (designing.TemporalConstraint, 'start_date'):
        "Required start date.",
    (designing.TemporalConstraint, 'start_flexibility'):
        "Amount of time before required start date that it is permissible to begin integration.",
    (drs.DrsAtomicDataset, 'frequency'):
        "Frequency at which data is stored.",
    (drs.DrsAtomicDataset, 'geographical_constraint'):
        "Identifies geographical subsets and spatial means.",
    (drs.DrsAtomicDataset, 'mip_table'):
        "The MIP table, together with the variable defines the physical quantity.",
    (drs.DrsAtomicDataset, 'realm'):
        "Modelling realm.",
    (drs.DrsAtomicDataset, 'temporal_constraint'):
        "Identifies temporal subsets or means.",
    (drs.DrsAtomicDataset, 'variable_name'):
        "Identifies the physical quantity (when used in conjunction with the MIP table).",
    (drs.DrsAtomicDataset, 'version_number'):
        "Uniquely identifies a particular version of a publication level dataset.",
    (drs.DrsEnsembleIdentifier, 'forcing_number'):
        "Identifies possible perturbatinos in forcing.",
    (drs.DrsEnsembleIdentifier, 'initialisation_method_number'):
        "Identifies which method of initialisation was used, if multiple methods used.",
    (drs.DrsEnsembleIdentifier, 'perturbation_number'):
        "Identifies different members of a perturbed physics ensemble.",
    (drs.DrsEnsembleIdentifier, 'realisation_number'):
        "Standard ensemble axis realisation number (usually an initial condition ensemble).",
    (drs.DrsExperiment, 'axis_identifer'):
        "FIXME.",
    (drs.DrsExperiment, 'axis_type'):
        "Type of experimental family ensemble required.",
    (drs.DrsExperiment, 'family'):
        "Main experimental family.",
    (drs.DrsGeographicalIndicator, 'bounding_box'):
        "DRS bounding box of the form 'latJHJJHHlonMZMMZZ' where H, HH, Z, ZZ are from {NS} {EW} respectively.",
    (drs.DrsGeographicalIndicator, 'operator'):
        "Spatial averagin applied to the geographical region.",
    (drs.DrsGeographicalIndicator, 'spatial_domain'):
        "Geographical indicator (currently only 'global' is acceptable).",
    (drs.DrsSimulationIdentifier, 'institute'):
        "The institute responsible for this data entity.",
    (drs.DrsSimulationIdentifier, 'model'):
        "A model identifier (sans blanks/periods and parenthesis).",
    (drs.DrsSimulationIdentifier, 'run_variant_id'):
        "Also known as ensemble_identifier, unambiguously identifiers ensemble realisation information.",
    (drs.DrsTemporalIdentifier, 'end'):
        "N2, required to indicate a period.",
    (drs.DrsTemporalIdentifier, 'start'):
        "N1,  of the form yyyy[MM[dd[hh[mm[ss]]]]].",
    (drs.DrsTemporalIdentifier, 'suffix'):
        "If present, used to indicate climatology or average.",
    (platform.ComponentPerformance, 'component'):
        "Link to a CIM software component description.",
    (platform.ComponentPerformance, 'component_name'):
        "Short name of component.",
    (platform.ComponentPerformance, 'cores_used'):
        "Number of cores used for this component.",
    (platform.ComponentPerformance, 'nodes_used'):
        "Number of nodes used for this component.",
    (platform.ComponentPerformance, 'speed'):
        "Time taken to simulate one real day (s).",
    (platform.ComputePool, 'accelerator_type'):
        "Type of accelerator.",
    (platform.ComputePool, 'accelerators_per_node'):
        "Number of accelerator units on a node.",
    (platform.ComputePool, 'compute_cores_per_node'):
        "Number of CPU cores per node.",
    (platform.ComputePool, 'cpu_type'):
        "CPU type.",
    (platform.ComputePool, 'description'):
        "Textural description of pool.",
    (platform.ComputePool, 'interconnect'):
        "Interconnect used.",
    (platform.ComputePool, 'memory_per_node'):
        "Memory per node.",
    (platform.ComputePool, 'model_number'):
        "Model/Board number/type.",
    (platform.ComputePool, 'name'):
        "Name of compute pool within a machine.",
    (platform.ComputePool, 'number_of_nodes'):
        "Number of nodes.",
    (platform.ComputePool, 'operating_system'):
        "Operating system.",
    (platform.Machine, 'meta'):
        "Document description.",
    (platform.Partition, 'compute_pools'):
        "Layout of compute nodes.",
    (platform.Partition, 'description'):
        "Textural description of machine.",
    (platform.Partition, 'institution'):
        "Institutional location.",
    (platform.Partition, 'model_number'):
        "Vendor's model number/name - if it exists.",
    (platform.Partition, 'name'):
        "Name of partition (or machine).",
    (platform.Partition, 'online_documentation'):
        "Links to documentation.",
    (platform.Partition, 'partition'):
        "If machine is partitioned, treat subpartitions as machines.",
    (platform.Partition, 'storage_pools'):
        "Storage resource available.",
    (platform.Partition, 'vendor'):
        "The system integrator or vendor.",
    (platform.Partition, 'when_used'):
        "If no longer in use, the time period it was in use.",
    (platform.Performance, 'asypd'):
        "Actual simulated years per wall-clock day, all-in.",
    (platform.Performance, 'chsy'):
        "Core-Hours per simulated year.",
    (platform.Performance, 'compiler'):
        "Compiler used.",
    (platform.Performance, 'coupler_load'):
        "Percentage of time spent in coupler.",
    (platform.Performance, 'io_load'):
        "Percentage of time spent in I/O.",
    (platform.Performance, 'load_imbalance'):
        "Load imbalance.",
    (platform.Performance, 'memory_bloat'):
        "Percentage of extra memory needed.",
    (platform.Performance, 'meta'):
        "Document metadata.",
    (platform.Performance, 'model'):
        "Model for which performance was tested.",
    (platform.Performance, 'name'):
        "Short name for performance (experiment/test/whatever).",
    (platform.Performance, 'platform'):
        "Platform on which performance was tested.",
    (platform.Performance, 'subcomponent_performance'):
        "Describes the performance of each subcomponent.",
    (platform.Performance, 'sypd'):
        "Simulated years per wall-clock day.",
    (platform.Performance, 'total_nodes_used'):
        "Number of nodes used.",
    (platform.StoragePool, 'description'):
        "Description of the technology used.",
    (platform.StoragePool, 'name'):
        "Name of storage pool.",
    (platform.StoragePool, 'type'):
        "Type of storage.",
    (platform.StoragePool, 'vendor'):
        "Vendor of the storage unit.",
    (platform.StoragePool, 'volume_available'):
        "Storage capacity.",
    (platform.StorageVolume, 'units'):
        "Volume units.",
    (platform.StorageVolume, 'volume'):
        "Numeric value.",
    (science.ConservationProperties, 'corrected_conserved_prognostic_variables'):
        "Set of variables which are conserved by *more* than the numerical scheme alone.",
    (science.ConservationProperties, 'flux_correction_was_used'):
        "Flag to indicate if correction involved flux correction.",
    (science.Extent, 'is_global'):
        "True if horizontal coverage is global.",
    (science.Extent, 'region_known_as'):
        "Identifier(s) for the region covered by the extent.",
    (science.Grid, 'description'):
        "Abstract description of grid.",
    (science.Grid, 'details'):
        "Specific grid properties.",
    (science.Grid, 'discretisation'):
        "Description of the numerics of the discretisation.",
    (science.Grid, 'meta'):
        "Metadata about how the model description was constructed.",
    (science.Grid, 'name'):
        "This is a string usually used by the modelling group to describe the overall grid.(e.g. the ENDGAME/New Dynamics dynamical cores have their own grids describing variable layouts.",
    (science.Grid, 'references'):
        "Any relevant references describing this grid and/or it's implementation.",
    (science.IsoExtent, 'eastern_boundary'):
        "Eastern boundary in degrees of longitude.",
    (science.IsoExtent, 'northern_boundary'):
        "Northern boundary in degrees of latitude.",
    (science.IsoExtent, 'southern_boundary'):
        "Southern boundary in degrees of latitude.",
    (science.IsoExtent, 'western_boundary'):
        "Western boundary in degrees of longitude.",
    (science.KeyProperties, 'extent'):
        "DESCRIPTION.",
    (science.KeyProperties, 'extra_conservation_properties'):
        "Details of methodology needed to conserve variables between processes.",
    (science.KeyProperties, 'resolution'):
        "The resolution of the grid (e.g. N512L180).",
    (science.KeyProperties, 'time_step'):
        "Timestep (in seconds) of overall component.",
    (science.KeyProperties, 'tuning_applied'):
        "Describe any tuning used to optimise the parameters in this domain.",
    (science.Model, 'category'):
        "Generic type for this model.",
    (science.Model, 'coupled_components'):
        "Software components which are linked together using a coupler to deliver this model.",
    (science.Model, 'coupler'):
        "Overarching coupling framework for model.",
    (science.Model, 'id'):
        "Vocabulary identifier, where this model description was constructed via a controlled vocabulary.",
    (science.Model, 'internal_software_components'):
        "Software modules which together provide the functionality for this model.",
    (science.Model, 'meta'):
        "Metadata about how the model description was constructed.",
    (science.Model, 'model_key_properties'):
        "Model default key properties (may be over-ridden in domain properties).",
    (science.Model, 'simulates'):
        "The scientific domains which this model simulates.",
    (science.Process, 'details'):
        "Sets of properties for this process.",
    (science.Process, 'implementation_overview'):
        "General overview description of the implementation of this process.",
    (science.Process, 'keywords'):
        "keywords to help re-use and discovery of this information.",
    (science.Process, 'references'):
        "Any relevant references describing this process and/or it's implementation.",
    (science.Process, 'sub_processes'):
        "Discrete portion of a process with common process details.",
    (science.Resolution, 'canonical_horizontal_resolution'):
        "Expression quoted for gross comparisons of resolution, eg. 50km or 0.1 degrees etc.",
    (science.Resolution, 'is_adaptive_grid'):
        "Default is False. Set true if grid resolution changes during execution.",
    (science.Resolution, 'name'):
        "This is a string usually used by the modelling group to describe the resolution of this grid,  e.g. N512L180 or T512L70 etc.",
    (science.Resolution, 'number_of_horizontal_gridpoints'):
        "Total number of horizontal points (or degrees of freedom) on computational grid.",
    (science.Resolution, 'number_of_vertical_levels'):
        "Number of vertical levels resolved on computational grid.",
    (science.ScienceContext, 'description'):
        "Scientific context for which this description is provided.",
    (science.ScienceContext, 'id'):
        "Identifier for this collection of properties.",
    (science.ScienceContext, 'short_name'):
        "The name of this process/algorithm/sub-process/detail.",
    (science.ScientificRealm, 'grid'):
        "The grid used to layout the variables (e.g. the Global ENDGAME-grid).",
    (science.ScientificRealm, 'id'):
        "Vocabulary identifier, where this domain description was constructed via a  controlled vocabulary.",
    (science.ScientificRealm, 'key_properties'):
        "Key properties for the domain which differ from model defaults (grid, timestep etc).",
    (science.ScientificRealm, 'meta'):
        "Metadata describing the construction of this domain description.",
    (science.ScientificRealm, 'name'):
        "Name of the scientific domain (e.g. ocean).",
    (science.ScientificRealm, 'overview'):
        "Free text overview description of key properties of domain.",
    (science.ScientificRealm, 'realm'):
        "Canonical name for the domain of this scientific area.",
    (science.ScientificRealm, 'references'):
        "Any relevant references describing the implementation of this domain in a relevant model.",
    (science.ScientificRealm, 'simulates'):
        "Processes simulated within the domain.",
    (science.SubProcess, 'details'):
        "Sets of properties for this process.",
    (science.SubProcess, 'implementation_overview'):
        "General overview description of the implementation of this part of the process.",
    (science.SubProcess, 'references'):
        "Any relevant references describing this part of the process and/or it's implementation.",
    (science.Tuning, 'description'):
        "Brief description of tuning methodology. Include information about observational period(s) used.",
    (science.Tuning, 'global_mean_metrics_used'):
        "Set of metrics of the global mean state used in tuning model parameters.",
    (science.Tuning, 'regional_metrics_used'):
        "Which regional metrics of mean state (e.g Monsoons, tropical means etc) have been used in tuning.",
    (science.Tuning, 'trend_metrics_used'):
        "Which observed trend metrics have been used in tuning model parameters.",
    (shared.Cimtext, 'content'):
        "Raw content (including markup).",
    (shared.Cimtext, 'content_type'):
        "Type of content.",
    (shared.Citation, 'abstract'):
        "Abstract providing high level reference overview.",
    (shared.Citation, 'citation_detail'):
        "Complete citation string as would appear in a bibliography.",
    (shared.Citation, 'collective_title'):
        "Citation collective title, i.e. with all authors declared.",
    (shared.Citation, 'context'):
        "Brief text description of why this resource is being cited.",
    (shared.Citation, 'doi'):
        "Digital Object Identifier, if it exists.",
    (shared.Citation, 'meta'):
        "Metadata about the creation of this document description.",
    (shared.Citation, 'title'):
        "Citation short title.",
    (shared.Citation, 'type'):
        "Citation type.",
    (shared.Citation, 'url'):
        "Location of electronic version.",
    (shared.CitationTarget, 'citation_detail'):
        "Complete citation string as would appear in a bibliography.",
    (shared.CitationTarget, 'doi'):
        "Digital Object Identifier, if it exists.",
    (shared.CitationTarget, 'meta'):
        "Metadata about the creation of this document description.",
    (shared.CitationTarget, 'name'):
        "A name for the citation: short hand description, e.g. Meehl et al (2014).",
    (shared.CitationTarget, 'online_at'):
        "Location of electronic version.",
    (shared.CitationTarget, 'title'):
        "Title or name of the document.",
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
        "Universal document identifier (normally a UUID).",
    (shared.DocMetaInfo, 'institute'):
        "Name of institute with which instance is associated.",
    (shared.DocMetaInfo, 'language'):
        "Language with which instance is associated.",
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
        "Document ontology type.",
    (shared.DocMetaInfo, 'type_display_name'):
        "Document type display name.",
    (shared.DocMetaInfo, 'type_sort_key'):
        "Document type sort key.",
    (shared.DocMetaInfo, 'update_date'):
        "Date upon which the instance was last updated.",
    (shared.DocMetaInfo, 'version'):
        "Document version identifier.",
    (shared.DocReference, 'constraint_vocabulary'):
        "A constraint vocabulary for the relationship.",
    (shared.DocReference, 'context'):
        "Information about remote record in context of reference.",
    (shared.DocReference, 'id'):
        "Identifier of remote resource, if known.",
    (shared.DocReference, 'relationship'):
        "Predicate - relationship of the object target as seen from the subject resource.",
    (shared.DocReference, 'type'):
        "The type of the remote record.",
    (shared.DocReference, 'version'):
        "The version of the remote record.",
    (shared.ExtraAttribute, 'doc'):
        "Documentation associated with this key.",
    (shared.ExtraAttribute, 'key'):
        "Name of attribute.",
    (shared.ExtraAttribute, 'type'):
        "If a non-string type, provide type.",
    (shared.ExtraAttribute, 'value'):
        "Value associated with key.",
    (shared.OnlineResource, 'description'):
        "Detail of how to access the resource.",
    (shared.OnlineResource, 'linkage'):
        "A URL.",
    (shared.OnlineResource, 'name'):
        "Name of online resource.",
    (shared.OnlineResource, 'protocol'):
        "Protocol to use at the linkage.",
    (shared.Party, 'address'):
        "Institutional address.",
    (shared.Party, 'email'):
        "Email address.",
    (shared.Party, 'meta'):
        "Provides a unique identifier for the party.",
    (shared.Party, 'name'):
        "Name of person or organisation.",
    (shared.Party, 'orcid_id'):
        "Orcid ID if available.",
    (shared.Party, 'organisation'):
        "True if an organisation not a person.",
    (shared.Party, 'url'):
        "URL of person or institution.",
    (shared.QualityReview, 'date'):
        "Date upon which review was made.",
    (shared.QualityReview, 'meta'):
        "Metadata about the creation of this document description.",
    (shared.QualityReview, 'metadata_reviewer'):
        "Party who made the metadata quality assessment.",
    (shared.QualityReview, 'quality_description'):
        "Assessment of quality of target document.",
    (shared.QualityReview, 'quality_status'):
        "Status from a controlled vocabulary.",
    (shared.QualityReview, 'target_document'):
        "This is the document about which quality is asserted.",
    (shared.Reference, 'context'):
        "Brief text description of why this resource is being cited.",
    (shared.Reference, 'document'):
        "Reference Target.",
    (shared.Responsibility, 'party'):
        "Parties delivering responsibility.",
    (shared.Responsibility, 'role'):
        "Role that the party plays or played.",
    (shared.Responsibility, 'when'):
        "Period when role was active, if no longer.",
    (software.ComponentBase, 'description'):
        "Textural description of component.",
    (software.ComponentBase, 'development_history'):
        "History of the development of this component.",
    (software.ComponentBase, 'documentation'):
        "Descriptions of the component functionality.",
    (software.ComponentBase, 'long_name'):
        "Long name for component.",
    (software.ComponentBase, 'name'):
        "Short name of component.",
    (software.ComponentBase, 'release_date'):
        "The date of publication of the component code (as opposed to the date of publication of the metadata document, or the date of deployment of the model).",
    (software.ComponentBase, 'repository'):
        "Location of code for this component.",
    (software.ComponentBase, 'version'):
        "Version identifier.",
    (software.Composition, 'couplings'):
        "#FIXME.",
    (software.Composition, 'description'):
        "#FIXME.",
    (software.DevelopmentPath, 'consortium_name'):
        "If model/component is developed as part of a consortium, provide consortium name.",
    (software.DevelopmentPath, 'creators'):
        "Those responsible for creating this component.",
    (software.DevelopmentPath, 'developed_in_house'):
        "Model or component was mostly developed in house.",
    (software.DevelopmentPath, 'funding_sources'):
        "The entities that funded this software component.",
    (software.DevelopmentPath, 'previous_version'):
        "Name of a previous version.",
    (software.EntryPoint, 'name'):
        "#FIXME.",
    (software.Gridspec, 'description'):
        "Textural description.",
    (software.SoftwareComponent, 'composition'):
        "#FIXME.",
    (software.SoftwareComponent, 'connection_points'):
        "The set of data entities which are available for I/O and/or coupling.",
    (software.SoftwareComponent, 'coupling_framework'):
        "The coupling framework that this entire component conforms to.",
    (software.SoftwareComponent, 'dependencies'):
        "#FIXME.",
    (software.SoftwareComponent, 'grid'):
        "A reference to the grid that is used by this component.",
    (software.SoftwareComponent, 'language'):
        "Language the component is written in.",
    (software.SoftwareComponent, 'license'):
        "The license held by this piece of software.",
    (software.SoftwareComponent, 'sub_components'):
        "Internal software sub-components of this component.",
    (software.Variable, 'description'):
        "Description of how the variable is being used in the s/w.",
    (software.Variable, 'name'):
        "Short name for the variable.",
    (software.Variable, 'prognostic'):
        "Whether or not prognostic or diagnostic.",
    (time.Calendar, 'description'):
        "Extra information about the calendar.",
    (time.Calendar, 'month_lengths'):
        "Used for special calendars to provide month lengths.",
    (time.Calendar, 'name'):
        "Can be used to name a special calendar type.",
    (time.Calendar, 'standard_name'):
        "Type of calendar used.",
    (time.DateTime, 'offset'):
        "Date is offset from start of an integration.",
    (time.DateTime, 'value'):
        "Date or time - some of (from left to right): yyyy-mm-dd:hh:mm:ss.",
    (time.DatetimeSet, 'length'):
        "Number of times in set.",
    (time.IrregularDateset, 'date_set'):
        "Set of dates, comma separated yyyy-mm-dd.",
    (time.RegularTimeset, 'increment'):
        "Interval between members of set.",
    (time.RegularTimeset, 'length'):
        "Number of times in set.",
    (time.RegularTimeset, 'start_date'):
        "Beginning of time set.",
    (time.TimePeriod, 'calendar'):
        "Calendar, default is standard aka gregorian.",
    (time.TimePeriod, 'date'):
        "Optional start/end date of time period.",
    (time.TimePeriod, 'date_type'):
        "Describes how the date is used to define the period.",
    (time.TimePeriod, 'length'):
        "Duration of the time period.",
    (time.TimePeriod, 'units'):
        "Appropriate time units.",

    # ------------------------------------------------
    # Enums.
    # ------------------------------------------------

    activity.ConformanceType: """
        Standardised set of conformance responses.

    """,
    data.DataAssociationTypes: """
        Set of possible dataset associations.
    Selected from, and extended from,  ISO19115 (2014) DS_AssociationTypeCode.

    """,
    designing.EnsembleTypes: """
        Defines the various axes along which one can set up an ensemble, whether
     as an experiment designer, or in designing a 'response' ensemble around an
     experiment.

    """,
    designing.ExperimentalRelationships: """
        Defines the canonical set of experimental relationships.

    """,
    designing.ForcingTypes: """
        Defines the possible set of forcing types for a forcing constraint.

    """,
    drs.DrsFrequencyTypes: """
        Set of allowed DRS frequency types.

    """,
    drs.DrsGeographicalOperators: """
        Set of permitted spatial averaging operator suffixes for drs spatial indicators (yyyy-zzzz).

    """,
    drs.DrsRealms: """
        Set of allowed DRS modelling realms.

    """,
    drs.DrsTimeSuffixes: """
        Set of permitted time averaging suffixes for drs temporal identifiers.

    """,
    platform.StorageSystems: """
        Controlled vocabulary for storage  types (including filesystems).

    """,
    platform.VolumeUnits: """
        Appropriate storage volume units.

    """,
    science.ModelTypes: """
        Defines a set of gross model classes.

    """,
    science.SelectionCardinality: """
        Provides the possible cardinalities for selecting from a controlled
    vocabulary.

    """,
    shared.DocumentTypes: """
        The complete set of CIM document types, that is, all classes which carry the
    document metadata attributes.

    """,
    shared.NilReason: """
        Provides an enumeration of possible reasons why a property has not been defined
    Based on GML nilReason as discussed here: https://www.seegrid.csiro.au/wiki/AppSchemas/NilValues.

    """,
    shared.QualityStatus: """
        Assertion as to the review status of document.

    """,
    shared.RoleCode: """
        Responsibility role codes: roles that a party may play in delivering a responsibility.

    """,
    shared.TextCode: """
        Types of text understood by the CIM notebook. Currently only
    plaintext, but we expect safe HTML to be supported as soon as practicable.

    """,
    software.CouplingFramework: """
        The set of terms which define known coupling frameworks.

    """,
    software.ProgrammingLanguage: """
        The set of terms which define programming languages used for earth
    system simulation.

    """,
    time.CalendarTypes: """
        CF calendar types as defined in CF 1.6.

    """,
    time.PeriodDateTypes: """
        A period date type vocabulary (used by time_period).

    """,
    time.TimeUnits: """
        Appropriate Time units for experiment durations in NWP and Climate Modelling.

    """,

    # ------------------------------------------------
    # Enum members.
    # ------------------------------------------------

    (activity.ConformanceType, 'Conformed'):
        "Simulation (or ensemble) conformed to requirement",
    (activity.ConformanceType, 'Not Applicable'):
        "Requirement is not relevant",
    (activity.ConformanceType, 'Not Conformed'):
        "Simulation (or ensemble) was unable to conform to requirement",
    (activity.ConformanceType, 'Partially Conformed'):
        "Simulation (or ensemble) partially conformed to requirement - details in description",
    (data.DataAssociationTypes, 'isComposedOf'):
        "This dataset is composed from the target",
    (data.DataAssociationTypes, 'partOf'):
        "This dataset forms part of the target",
    (data.DataAssociationTypes, 'revisonOf'):
        "This dataset was revised from the target",
    (designing.EnsembleTypes, 'Driven'):
        "Members are/should-be driven by different models.",
    (designing.EnsembleTypes, 'Forced'):
        "Members have differing forcing data.",
    (designing.EnsembleTypes, 'Initialisation Method'):
        "Members differ in how they are initialised.",
    (designing.EnsembleTypes, 'Perturbed Physics'):
        "Members differ in some aspects of their physics.",
    (designing.EnsembleTypes, 'Realization'):
        "Members initialised to sample possible initial conditions.",
    (designing.EnsembleTypes, 'Resolution'):
        "Members are/should-be run at different resolutions.",
    (designing.EnsembleTypes, 'Start Date'):
        "Members initialised at different starting dates.",
    (designing.ExperimentalRelationships, 'control_for'):
        "This experiment provides a control for the target experiment",
    (designing.ExperimentalRelationships, 'initialisation_for'):
        "This experiment provides initialisation for the target experiment",
    (designing.ExperimentalRelationships, 'is_sibling'):
        "Part of a family (e.g. experiments where solar forcing is either increased or reduced)",
    (designing.ExperimentalRelationships, 'provides_constraints'):
        "This experiment provides constraint(s) for the target experiment (e.g SST forcing)",
    (designing.ForcingTypes, 'driven'):
        "Driven from another simulation",
    (designing.ForcingTypes, 'historical'):
        "Best estimates of actual state (included synthesized)",
    (designing.ForcingTypes, 'idealised'):
        "Simplified and/or exemplar, e.g. 1%C02",
    (designing.ForcingTypes, 'scenario'):
        "Intended to represent a possible future, e.g. RCP4.5",
    (drs.DrsFrequencyTypes, '3hr'):
        "Every three hours",
    (drs.DrsFrequencyTypes, '6hr'):
        "Every six hours",
    (drs.DrsFrequencyTypes, 'day'):
        "Daily",
    (drs.DrsFrequencyTypes, 'fx'):
        "Fixed Time independent",
    (drs.DrsFrequencyTypes, 'mon'):
        "Monthly",
    (drs.DrsFrequencyTypes, 'monClim'):
        "Climatological Monthly Mean",
    (drs.DrsFrequencyTypes, 'subhr'):
        "Sampling frequency less than an hour",
    (drs.DrsFrequencyTypes, 'yr'):
        "Yearly",
    (drs.DrsGeographicalOperators, 'areaavg'):
        "Data is averaged over the area of the region",
    (drs.DrsGeographicalOperators, 'lnd-areaavg'):
        "Data is averaged over the land area of the region",
    (drs.DrsGeographicalOperators, 'lnd-zonalavg'):
        "Data is zonally averaged over land in region",
    (drs.DrsGeographicalOperators, 'ocn-areaavg'):
        "Data is averaged over the ocean area of the region",
    (drs.DrsGeographicalOperators, 'ocn-zonalavg'):
        "Data is zonally averaged over oceans in region",
    (drs.DrsGeographicalOperators, 'zonalavg'):
        "Data is zonally averaged",
    (drs.DrsRealms, 'aerosol'):
        "Aerosol",
    (drs.DrsRealms, 'atmos'):
        "Atmosphere",
    (drs.DrsRealms, 'atmosChem'):
        "Atmospheric Chemistry",
    (drs.DrsRealms, 'land'):
        "Land",
    (drs.DrsRealms, 'landIce'):
        "Land Ice",
    (drs.DrsRealms, 'ocean'):
        "Ocean",
    (drs.DrsRealms, 'ocnBgchem'):
        "Ocean Biogeochemistry",
    (drs.DrsRealms, 'seaIce'):
        "Sea Ice",
    (drs.DrsTimeSuffixes, 'avg'):
        "Indicates data is a single average of DRS frequency data across temporal period N1-N2",
    (drs.DrsTimeSuffixes, 'clim'):
        "Indicates data is climatological average data at the DRS frequency from the period N1-N2",
    (platform.StorageSystems, 'GPFS'):
        "IBM GPFS (also known as IBM Spectral Scale",
    (platform.StorageSystems, 'Lustre'):
        "Lustre parallel file system",
    (platform.StorageSystems, 'NFS'):
        "Generic Network File System",
    (platform.StorageSystems, 'Other Disk'):
        "Other disk based file system",
    (platform.StorageSystems, 'PanFS'):
        "Panasas Parallel File system",
    (platform.StorageSystems, 'S3'):
        "Object file system exposing the AWS S3 interface",
    (platform.StorageSystems, 'Tape - Castor'):
        "Tape storage sytsem using CERN Castor",
    (platform.StorageSystems, 'Tape - MARS'):
        "Tape storage system using ECMWF MARS",
    (platform.StorageSystems, 'Tape - MASS'):
        "Tape storage system using Met Office MASS",
    (platform.StorageSystems, 'Tape - Other'):
        "Other tape based system",
    (platform.StorageSystems, 'isilon'):
        "The EMC scaleout NAS solution",
    (platform.VolumeUnits, 'EB'):
        "Exabytes (1000^6)",
    (platform.VolumeUnits, 'EiB'):
        "Exbibytes (1024^6)",
    (platform.VolumeUnits, 'GB'):
        "Gigabytes (1000^3)",
    (platform.VolumeUnits, 'PB'):
        "Petabytes (1000^5)",
    (platform.VolumeUnits, 'PiB'):
        "Pebibytes (1024^5)",
    (platform.VolumeUnits, 'TB'):
        "Terabytes (1000^4)",
    (platform.VolumeUnits, 'TiB'):
        "Tebibytes (1024^4)",
    (science.ModelTypes, 'Atm Only'):
        "Atmosphere Only",
    (science.ModelTypes, 'GCM'):
        "Global Climate Model (Atmosphere, Ocean, no carbon cycle)",
    (science.ModelTypes, 'GCM-MLO'):
        "GCM with mixed layer ocean",
    (science.ModelTypes, 'IGCM'):
        "Intermediate Complexity GCM",
    (science.ModelTypes, 'Mesoscale'):
        "Mesoscale Model",
    (science.ModelTypes, 'Ocean Only'):
        "Ocean Only",
    (science.ModelTypes, 'Planetary'):
        "Non-Earth model",
    (science.ModelTypes, 'Process'):
        "Limited Area process model",
    (science.ModelTypes, 'Regional'):
        "Regional Model",
    (science.SelectionCardinality, '0.1'):
        "Zero or one selections are permitted",
    (science.SelectionCardinality, '0.N'):
        "Zero or many selections are permitted",
    (science.SelectionCardinality, '1.1'):
        "One and only one selection is required",
    (science.SelectionCardinality, '1.N'):
        "At least one, and possibly many, selections are required",
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
    (shared.DocumentTypes, 'Performance'):
        "A formal set of criteria describing how a model performed on a given machine.",
    (shared.DocumentTypes, 'Project'):
        "An umbrella for a set of numerical experiments (e.g. a MIP)",
    (shared.DocumentTypes, 'QualityReview'):
        "A quality control assessment for another CIM artifact",
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
    (shared.NilReason, 'nil:inapplicable'):
        "There is no value",
    (shared.NilReason, 'nil:missing'):
        "The correct value is not available. Furthermore, a correct value may not exist",
    (shared.NilReason, 'nil:template'):
        "The value will be available later",
    (shared.NilReason, 'nil:unknown'):
        "The correct value is not known at this time. However, a correct value probably exists",
    (shared.NilReason, 'nil:withheld'):
        "The value is not divulged",
    (shared.QualityStatus, 'finalised'):
        "Author has completed document, prior to review",
    (shared.QualityStatus, 'incomplete'):
        "Currently being worked on",
    (shared.QualityStatus, 'reviewed'):
        "Document has been formally reviewed and assessed as complete and accurate",
    (shared.QualityStatus, 'under_review'):
        "Document is being reviewed",
    (shared.RoleCode, 'Principal Investigator'):
        "Key party responsible for the existence of the resource",
    (shared.RoleCode, 'author'):
        "Party who created (or co-created) resource",
    (shared.RoleCode, 'collaborator'):
        "Contributor to the production of the resource",
    (shared.RoleCode, 'custodian'):
        "Party that accepts accountability and responsibility for the source resource",
    (shared.RoleCode, 'distributor'):
        "Party who distributes the resource",
    (shared.RoleCode, 'metadata_author'):
        "Party who created (this) documentation",
    (shared.RoleCode, 'metadata_reviewer'):
        "Party who carried out an independent review of (this) documentation",
    (shared.RoleCode, 'originator'):
        "Original source for the resource if obtained from elsewhere",
    (shared.RoleCode, 'owner'):
        "Party with legal ownership of the resource",
    (shared.RoleCode, 'point of contact'):
        "Party who can be contacted for acquiring knowledge about or acquisition of the resource",
    (shared.RoleCode, 'processor'):
        "Party who has taken part in the workflow that resulted in this resource",
    (shared.RoleCode, 'publisher'):
        "Party who published the resource",
    (shared.RoleCode, 'resource provider'):
        "Party that supplies the resource",
    (shared.RoleCode, 'sponsor'):
        "Party who has invested in the production of the resource",
    (shared.RoleCode, 'user'):
        "Party who uses the resource",
    (shared.TextCode, 'plaintext'):
        "Normal plain text",
    (software.CouplingFramework, 'Bespoke'):
        "Customised coupler developed for this model",
    (software.CouplingFramework, 'ESMF'):
        "Vanilla Earth System Modelling Framework",
    (software.CouplingFramework, 'NUOPC'):
        "National Unified Operational Prediction Capability variant of ESMF",
    (software.CouplingFramework, 'None'):
        "No coupler is used",
    (software.CouplingFramework, 'OASIS'):
        "The OASIS coupler - prior to OASIS-MCT",
    (software.CouplingFramework, 'OASIS3-MCT'):
        "The MCT variant of the OASIS coupler",
    (software.CouplingFramework, 'Unknown'):
        "It is not known what/if-a coupler is used",
    (software.ProgrammingLanguage, 'C'):
        "C Programmming Language",
    (software.ProgrammingLanguage, 'C++'):
        "C++ Programming Language",
    (software.ProgrammingLanguage, 'Fortran'):
        "Fortran Programming Language",
    (software.ProgrammingLanguage, 'Python'):
        "Python Programming Language",
    (time.CalendarTypes, '360_day'):
        "All years are 360 days divided into 30 day months.",
    (time.CalendarTypes, '365_day'):
        "Synonym for noleap:Gregorian calendar without leap years, i.e., all years are 365 days long.",
    (time.CalendarTypes, '366_day'):
        "Synonym for all_leap:Gregorian calendar with every year being a leap year, i.e., all years are 366 days long.",
    (time.CalendarTypes, 'all_leap'):
        "Gregorian calendar with every year being a leap year, i.e., all years are 366 days long.",
    (time.CalendarTypes, 'gregorian'):
        "Mixed Gregorian/Julian calendar as defined by Udunits",
    (time.CalendarTypes, 'julian'):
        "Julian Calendar",
    (time.CalendarTypes, 'noleap'):
        "Gregorian calendar without leap years, i.e., all years are 365 days long.",
    (time.CalendarTypes, 'none'):
        "Perpetual time axis",
    (time.CalendarTypes, 'proleptic_gregorian'):
        "A Gregorian calendar extended to dates before 1582-10-15. That is, a year is a leap year if either (i) it is divisible by 4 but not by 100 or (ii) it is divisible by 400.",
    (time.CalendarTypes, 'standard'):
        "Synonym for gregorian: Mixed Gregorian/Julian calendar as defined by Udunits",
    (time.PeriodDateTypes, 'date is end'):
        "The date is the end of the period",
    (time.PeriodDateTypes, 'date is start'):
        "The date defines the start of the period",
    (time.PeriodDateTypes, 'unused'):
        "Date is not used",
    (time.TimeUnits, 'days'):
        "86400 seconds",
    (time.TimeUnits, 'months'):
        "Months in the current calendar",
    (time.TimeUnits, 'seconds'):
        "Standard metric seconds",
    (time.TimeUnits, 'years'):
        "Years in current calendar",
}

# ------------------------------------------------
# Type keys.
# ------------------------------------------------

# Map of ontology types to type keys.
KEYS = {
    # ------------------------------------------------
    # Packages.
    # ------------------------------------------------

    activity: "cim.2.activity",
    data: "cim.2.data",
    designing: "cim.2.designing",
    drs: "cim.2.drs",
    platform: "cim.2.platform",
    science: "cim.2.science",
    shared: "cim.2.shared",
    software: "cim.2.software",
    time: "cim.2.time",

    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    activity.Activity: "cim.2.activity.Activity",
    activity.AxisMember: "cim.2.activity.AxisMember",
    activity.Conformance: "cim.2.activity.Conformance",
    activity.Ensemble: "cim.2.activity.Ensemble",
    activity.EnsembleAxis: "cim.2.activity.EnsembleAxis",
    activity.EnsembleMember: "cim.2.activity.EnsembleMember",
    activity.ParentSimulation: "cim.2.activity.ParentSimulation",
    activity.UberEnsemble: "cim.2.activity.UberEnsemble",
    data.Dataset: "cim.2.data.Dataset",
    data.Downscaling: "cim.2.data.Downscaling",
    data.Simulation: "cim.2.data.Simulation",
    data.VariableCollection: "cim.2.data.VariableCollection",
    designing.AxisMember: "cim.2.designing.AxisMember",
    designing.DomainRequirements: "cim.2.designing.DomainRequirements",
    designing.EnsembleRequirement: "cim.2.designing.EnsembleRequirement",
    designing.ForcingConstraint: "cim.2.designing.ForcingConstraint",
    designing.InitialisationRequirement: "cim.2.designing.InitialisationRequirement",
    designing.MultiEnsemble: "cim.2.designing.MultiEnsemble",
    designing.NumericalExperiment: "cim.2.designing.NumericalExperiment",
    designing.NumericalRequirement: "cim.2.designing.NumericalRequirement",
    designing.OutputRequirement: "cim.2.designing.OutputRequirement",
    designing.Project: "cim.2.designing.Project",
    designing.SimulationPlan: "cim.2.designing.SimulationPlan",
    designing.StartDateEnsemble: "cim.2.designing.StartDateEnsemble",
    designing.TemporalConstraint: "cim.2.designing.TemporalConstraint",
    drs.DrsAtomicDataset: "cim.2.drs.DrsAtomicDataset",
    drs.DrsEnsembleIdentifier: "cim.2.drs.DrsEnsembleIdentifier",
    drs.DrsExperiment: "cim.2.drs.DrsExperiment",
    drs.DrsGeographicalIndicator: "cim.2.drs.DrsGeographicalIndicator",
    drs.DrsPublicationDataset: "cim.2.drs.DrsPublicationDataset",
    drs.DrsSimulationIdentifier: "cim.2.drs.DrsSimulationIdentifier",
    drs.DrsTemporalIdentifier: "cim.2.drs.DrsTemporalIdentifier",
    platform.ComponentPerformance: "cim.2.platform.ComponentPerformance",
    platform.ComputePool: "cim.2.platform.ComputePool",
    platform.Machine: "cim.2.platform.Machine",
    platform.Partition: "cim.2.platform.Partition",
    platform.Performance: "cim.2.platform.Performance",
    platform.StoragePool: "cim.2.platform.StoragePool",
    platform.StorageVolume: "cim.2.platform.StorageVolume",
    science.ConservationProperties: "cim.2.science.ConservationProperties",
    science.Detail: "cim.2.science.Detail",
    science.Discretisation: "cim.2.science.Discretisation",
    science.Extent: "cim.2.science.Extent",
    science.Grid: "cim.2.science.Grid",
    science.IsoExtent: "cim.2.science.IsoExtent",
    science.KeyProperties: "cim.2.science.KeyProperties",
    science.Model: "cim.2.science.Model",
    science.Process: "cim.2.science.Process",
    science.Resolution: "cim.2.science.Resolution",
    science.ScienceContext: "cim.2.science.ScienceContext",
    science.ScientificRealm: "cim.2.science.ScientificRealm",
    science.SubProcess: "cim.2.science.SubProcess",
    science.Tuning: "cim.2.science.Tuning",
    shared.Cimtext: "cim.2.shared.Cimtext",
    shared.Citation: "cim.2.shared.Citation",
    shared.CitationTarget: "cim.2.shared.CitationTarget",
    shared.DocMetaInfo: "cim.2.shared.DocMetaInfo",
    shared.DocReference: "cim.2.shared.DocReference",
    shared.ExtraAttribute: "cim.2.shared.ExtraAttribute",
    shared.OnlineResource: "cim.2.shared.OnlineResource",
    shared.Party: "cim.2.shared.Party",
    shared.QualityReview: "cim.2.shared.QualityReview",
    shared.Reference: "cim.2.shared.Reference",
    shared.Responsibility: "cim.2.shared.Responsibility",
    software.ComponentBase: "cim.2.software.ComponentBase",
    software.Composition: "cim.2.software.Composition",
    software.DevelopmentPath: "cim.2.software.DevelopmentPath",
    software.EntryPoint: "cim.2.software.EntryPoint",
    software.Gridspec: "cim.2.software.Gridspec",
    software.SoftwareComponent: "cim.2.software.SoftwareComponent",
    software.Variable: "cim.2.software.Variable",
    time.Calendar: "cim.2.time.Calendar",
    time.DateTime: "cim.2.time.DateTime",
    time.DatetimeSet: "cim.2.time.DatetimeSet",
    time.IrregularDateset: "cim.2.time.IrregularDateset",
    time.RegularTimeset: "cim.2.time.RegularTimeset",
    time.TimePeriod: "cim.2.time.TimePeriod",

    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------

    (activity.Activity, 'alternative_names'): "cim.2.activity.Activity.alternative_names",
    (activity.Activity, 'canonical_name'): "cim.2.activity.Activity.canonical_name",
    (activity.Activity, 'description'): "cim.2.activity.Activity.description",
    (activity.Activity, 'duration'): "cim.2.activity.Activity.duration",
    (activity.Activity, 'internal_name'): "cim.2.activity.Activity.internal_name",
    (activity.Activity, 'keywords'): "cim.2.activity.Activity.keywords",
    (activity.Activity, 'long_name'): "cim.2.activity.Activity.long_name",
    (activity.Activity, 'meta'): "cim.2.activity.Activity.meta",
    (activity.Activity, 'name'): "cim.2.activity.Activity.name",
    (activity.Activity, 'previously_known_as'): "cim.2.activity.Activity.previously_known_as",
    (activity.Activity, 'rationale'): "cim.2.activity.Activity.rationale",
    (activity.Activity, 'references'): "cim.2.activity.Activity.references",
    (activity.Activity, 'responsible_parties'): "cim.2.activity.Activity.responsible_parties",
    (activity.AxisMember, 'description'): "cim.2.activity.AxisMember.description",
    (activity.AxisMember, 'extra_detail'): "cim.2.activity.AxisMember.extra_detail",
    (activity.AxisMember, 'index'): "cim.2.activity.AxisMember.index",
    (activity.AxisMember, 'value'): "cim.2.activity.AxisMember.value",
    (activity.Conformance, 'conformance_achieved'): "cim.2.activity.Conformance.conformance_achieved",
    (activity.Conformance, 'target_requirement'): "cim.2.activity.Conformance.target_requirement",
    (activity.Ensemble, 'common_conformances'): "cim.2.activity.Ensemble.common_conformances",
    (activity.Ensemble, 'documentation'): "cim.2.activity.Ensemble.documentation",
    (activity.Ensemble, 'has_ensemble_axes'): "cim.2.activity.Ensemble.has_ensemble_axes",
    (activity.Ensemble, 'members'): "cim.2.activity.Ensemble.members",
    (activity.Ensemble, 'part_of'): "cim.2.activity.Ensemble.part_of",
    (activity.Ensemble, 'supported'): "cim.2.activity.Ensemble.supported",
    (activity.EnsembleAxis, 'extra_detail'): "cim.2.activity.EnsembleAxis.extra_detail",
    (activity.EnsembleAxis, 'member'): "cim.2.activity.EnsembleAxis.member",
    (activity.EnsembleAxis, 'short_identifier'): "cim.2.activity.EnsembleAxis.short_identifier",
    (activity.EnsembleAxis, 'target_requirement'): "cim.2.activity.EnsembleAxis.target_requirement",
    (activity.EnsembleMember, 'errata'): "cim.2.activity.EnsembleMember.errata",
    (activity.EnsembleMember, 'had_performance'): "cim.2.activity.EnsembleMember.had_performance",
    (activity.EnsembleMember, 'ran_on'): "cim.2.activity.EnsembleMember.ran_on",
    (activity.EnsembleMember, 'simulation'): "cim.2.activity.EnsembleMember.simulation",
    (activity.ParentSimulation, 'branch_method'): "cim.2.activity.ParentSimulation.branch_method",
    (activity.ParentSimulation, 'branch_time_in_child'): "cim.2.activity.ParentSimulation.branch_time_in_child",
    (activity.ParentSimulation, 'branch_time_in_parent'): "cim.2.activity.ParentSimulation.branch_time_in_parent",
    (activity.ParentSimulation, 'parent'): "cim.2.activity.ParentSimulation.parent",
    (activity.UberEnsemble, 'child_ensembles'): "cim.2.activity.UberEnsemble.child_ensembles",
    (data.Dataset, 'availability'): "cim.2.data.Dataset.availability",
    (data.Dataset, 'description'): "cim.2.data.Dataset.description",
    (data.Dataset, 'drs_datasets'): "cim.2.data.Dataset.drs_datasets",
    (data.Dataset, 'meta'): "cim.2.data.Dataset.meta",
    (data.Dataset, 'name'): "cim.2.data.Dataset.name",
    (data.Dataset, 'produced_by'): "cim.2.data.Dataset.produced_by",
    (data.Dataset, 'references'): "cim.2.data.Dataset.references",
    (data.Dataset, 'related_to_dataset'): "cim.2.data.Dataset.related_to_dataset",
    (data.Dataset, 'responsible_parties'): "cim.2.data.Dataset.responsible_parties",
    (data.Downscaling, 'downscaled_from'): "cim.2.data.Downscaling.downscaled_from",
    (data.Simulation, 'calendar'): "cim.2.data.Simulation.calendar",
    (data.Simulation, 'contact'): "cim.2.data.Simulation.contact",
    (data.Simulation, 'end_time'): "cim.2.data.Simulation.end_time",
    (data.Simulation, 'extra_attributes'): "cim.2.data.Simulation.extra_attributes",
    (data.Simulation, 'forcing_index'): "cim.2.data.Simulation.forcing_index",
    (data.Simulation, 'further_info_url'): "cim.2.data.Simulation.further_info_url",
    (data.Simulation, 'initialization_index'): "cim.2.data.Simulation.initialization_index",
    (data.Simulation, 'insitution'): "cim.2.data.Simulation.insitution",
    (data.Simulation, 'parent_simulation'): "cim.2.data.Simulation.parent_simulation",
    (data.Simulation, 'part_of_project'): "cim.2.data.Simulation.part_of_project",
    (data.Simulation, 'physics_index'): "cim.2.data.Simulation.physics_index",
    (data.Simulation, 'primary_ensemble'): "cim.2.data.Simulation.primary_ensemble",
    (data.Simulation, 'ran_for_experiments'): "cim.2.data.Simulation.ran_for_experiments",
    (data.Simulation, 'realization_index'): "cim.2.data.Simulation.realization_index",
    (data.Simulation, 'references'): "cim.2.data.Simulation.references",
    (data.Simulation, 'start_time'): "cim.2.data.Simulation.start_time",
    (data.Simulation, 'sub_experiment'): "cim.2.data.Simulation.sub_experiment",
    (data.Simulation, 'used'): "cim.2.data.Simulation.used",
    (data.Simulation, 'variant_info'): "cim.2.data.Simulation.variant_info",
    (data.VariableCollection, 'collection_name'): "cim.2.data.VariableCollection.collection_name",
    (data.VariableCollection, 'variables'): "cim.2.data.VariableCollection.variables",
    (designing.DomainRequirements, 'required_extent'): "cim.2.designing.DomainRequirements.required_extent",
    (designing.DomainRequirements, 'required_resolution'): "cim.2.designing.DomainRequirements.required_resolution",
    (designing.EnsembleRequirement, 'ensemble_member'): "cim.2.designing.EnsembleRequirement.ensemble_member",
    (designing.EnsembleRequirement, 'ensemble_type'): "cim.2.designing.EnsembleRequirement.ensemble_type",
    (designing.EnsembleRequirement, 'minimum_size'): "cim.2.designing.EnsembleRequirement.minimum_size",
    (designing.ForcingConstraint, 'additional_constraint'): "cim.2.designing.ForcingConstraint.additional_constraint",
    (designing.ForcingConstraint, 'category'): "cim.2.designing.ForcingConstraint.category",
    (designing.ForcingConstraint, 'code'): "cim.2.designing.ForcingConstraint.code",
    (designing.ForcingConstraint, 'data_link'): "cim.2.designing.ForcingConstraint.data_link",
    (designing.ForcingConstraint, 'forcing_type'): "cim.2.designing.ForcingConstraint.forcing_type",
    (designing.ForcingConstraint, 'group'): "cim.2.designing.ForcingConstraint.group",
    (designing.ForcingConstraint, 'origin'): "cim.2.designing.ForcingConstraint.origin",
    (designing.InitialisationRequirement, 'branch_time_in_initialisation_source'): "cim.2.designing.InitialisationRequirement.branch_time_in_initialisation_source",
    (designing.InitialisationRequirement, 'initialise_from_data'): "cim.2.designing.InitialisationRequirement.initialise_from_data",
    (designing.InitialisationRequirement, 'initialise_from_experiment'): "cim.2.designing.InitialisationRequirement.initialise_from_experiment",
    (designing.MultiEnsemble, 'ensemble_axis'): "cim.2.designing.MultiEnsemble.ensemble_axis",
    (designing.NumericalExperiment, 'related_experiments'): "cim.2.designing.NumericalExperiment.related_experiments",
    (designing.NumericalExperiment, 'related_mips'): "cim.2.designing.NumericalExperiment.related_mips",
    (designing.NumericalExperiment, 'required_period'): "cim.2.designing.NumericalExperiment.required_period",
    (designing.NumericalExperiment, 'requirements'): "cim.2.designing.NumericalExperiment.requirements",
    (designing.NumericalRequirement, 'additional_requirements'): "cim.2.designing.NumericalRequirement.additional_requirements",
    (designing.NumericalRequirement, 'is_conformance_requested'): "cim.2.designing.NumericalRequirement.is_conformance_requested",
    (designing.OutputRequirement, 'formal_data_request'): "cim.2.designing.OutputRequirement.formal_data_request",
    (designing.Project, 'homepage'): "cim.2.designing.Project.homepage",
    (designing.Project, 'objectives'): "cim.2.designing.Project.objectives",
    (designing.Project, 'previous_projects'): "cim.2.designing.Project.previous_projects",
    (designing.Project, 'requires_experiments'): "cim.2.designing.Project.requires_experiments",
    (designing.Project, 'sub_projects'): "cim.2.designing.Project.sub_projects",
    (designing.SimulationPlan, 'expected_model'): "cim.2.designing.SimulationPlan.expected_model",
    (designing.SimulationPlan, 'expected_performance_sypd'): "cim.2.designing.SimulationPlan.expected_performance_sypd",
    (designing.SimulationPlan, 'expected_platform'): "cim.2.designing.SimulationPlan.expected_platform",
    (designing.SimulationPlan, 'will_support_experiments'): "cim.2.designing.SimulationPlan.will_support_experiments",
    (designing.StartDateEnsemble, 'ensemble_members'): "cim.2.designing.StartDateEnsemble.ensemble_members",
    (designing.TemporalConstraint, 'required_calendar'): "cim.2.designing.TemporalConstraint.required_calendar",
    (designing.TemporalConstraint, 'required_duration'): "cim.2.designing.TemporalConstraint.required_duration",
    (designing.TemporalConstraint, 'start_date'): "cim.2.designing.TemporalConstraint.start_date",
    (designing.TemporalConstraint, 'start_flexibility'): "cim.2.designing.TemporalConstraint.start_flexibility",
    (drs.DrsAtomicDataset, 'frequency'): "cim.2.drs.DrsAtomicDataset.frequency",
    (drs.DrsAtomicDataset, 'geographical_constraint'): "cim.2.drs.DrsAtomicDataset.geographical_constraint",
    (drs.DrsAtomicDataset, 'mip_table'): "cim.2.drs.DrsAtomicDataset.mip_table",
    (drs.DrsAtomicDataset, 'realm'): "cim.2.drs.DrsAtomicDataset.realm",
    (drs.DrsAtomicDataset, 'temporal_constraint'): "cim.2.drs.DrsAtomicDataset.temporal_constraint",
    (drs.DrsAtomicDataset, 'variable_name'): "cim.2.drs.DrsAtomicDataset.variable_name",
    (drs.DrsAtomicDataset, 'version_number'): "cim.2.drs.DrsAtomicDataset.version_number",
    (drs.DrsEnsembleIdentifier, 'forcing_number'): "cim.2.drs.DrsEnsembleIdentifier.forcing_number",
    (drs.DrsEnsembleIdentifier, 'initialisation_method_number'): "cim.2.drs.DrsEnsembleIdentifier.initialisation_method_number",
    (drs.DrsEnsembleIdentifier, 'perturbation_number'): "cim.2.drs.DrsEnsembleIdentifier.perturbation_number",
    (drs.DrsEnsembleIdentifier, 'realisation_number'): "cim.2.drs.DrsEnsembleIdentifier.realisation_number",
    (drs.DrsExperiment, 'axis_identifer'): "cim.2.drs.DrsExperiment.axis_identifer",
    (drs.DrsExperiment, 'axis_type'): "cim.2.drs.DrsExperiment.axis_type",
    (drs.DrsExperiment, 'family'): "cim.2.drs.DrsExperiment.family",
    (drs.DrsGeographicalIndicator, 'bounding_box'): "cim.2.drs.DrsGeographicalIndicator.bounding_box",
    (drs.DrsGeographicalIndicator, 'operator'): "cim.2.drs.DrsGeographicalIndicator.operator",
    (drs.DrsGeographicalIndicator, 'spatial_domain'): "cim.2.drs.DrsGeographicalIndicator.spatial_domain",
    (drs.DrsSimulationIdentifier, 'institute'): "cim.2.drs.DrsSimulationIdentifier.institute",
    (drs.DrsSimulationIdentifier, 'model'): "cim.2.drs.DrsSimulationIdentifier.model",
    (drs.DrsSimulationIdentifier, 'run_variant_id'): "cim.2.drs.DrsSimulationIdentifier.run_variant_id",
    (drs.DrsTemporalIdentifier, 'end'): "cim.2.drs.DrsTemporalIdentifier.end",
    (drs.DrsTemporalIdentifier, 'start'): "cim.2.drs.DrsTemporalIdentifier.start",
    (drs.DrsTemporalIdentifier, 'suffix'): "cim.2.drs.DrsTemporalIdentifier.suffix",
    (platform.ComponentPerformance, 'component'): "cim.2.platform.ComponentPerformance.component",
    (platform.ComponentPerformance, 'component_name'): "cim.2.platform.ComponentPerformance.component_name",
    (platform.ComponentPerformance, 'cores_used'): "cim.2.platform.ComponentPerformance.cores_used",
    (platform.ComponentPerformance, 'nodes_used'): "cim.2.platform.ComponentPerformance.nodes_used",
    (platform.ComponentPerformance, 'speed'): "cim.2.platform.ComponentPerformance.speed",
    (platform.ComputePool, 'accelerator_type'): "cim.2.platform.ComputePool.accelerator_type",
    (platform.ComputePool, 'accelerators_per_node'): "cim.2.platform.ComputePool.accelerators_per_node",
    (platform.ComputePool, 'compute_cores_per_node'): "cim.2.platform.ComputePool.compute_cores_per_node",
    (platform.ComputePool, 'cpu_type'): "cim.2.platform.ComputePool.cpu_type",
    (platform.ComputePool, 'description'): "cim.2.platform.ComputePool.description",
    (platform.ComputePool, 'interconnect'): "cim.2.platform.ComputePool.interconnect",
    (platform.ComputePool, 'memory_per_node'): "cim.2.platform.ComputePool.memory_per_node",
    (platform.ComputePool, 'model_number'): "cim.2.platform.ComputePool.model_number",
    (platform.ComputePool, 'name'): "cim.2.platform.ComputePool.name",
    (platform.ComputePool, 'number_of_nodes'): "cim.2.platform.ComputePool.number_of_nodes",
    (platform.ComputePool, 'operating_system'): "cim.2.platform.ComputePool.operating_system",
    (platform.Machine, 'meta'): "cim.2.platform.Machine.meta",
    (platform.Partition, 'compute_pools'): "cim.2.platform.Partition.compute_pools",
    (platform.Partition, 'description'): "cim.2.platform.Partition.description",
    (platform.Partition, 'institution'): "cim.2.platform.Partition.institution",
    (platform.Partition, 'model_number'): "cim.2.platform.Partition.model_number",
    (platform.Partition, 'name'): "cim.2.platform.Partition.name",
    (platform.Partition, 'online_documentation'): "cim.2.platform.Partition.online_documentation",
    (platform.Partition, 'partition'): "cim.2.platform.Partition.partition",
    (platform.Partition, 'storage_pools'): "cim.2.platform.Partition.storage_pools",
    (platform.Partition, 'vendor'): "cim.2.platform.Partition.vendor",
    (platform.Partition, 'when_used'): "cim.2.platform.Partition.when_used",
    (platform.Performance, 'asypd'): "cim.2.platform.Performance.asypd",
    (platform.Performance, 'chsy'): "cim.2.platform.Performance.chsy",
    (platform.Performance, 'compiler'): "cim.2.platform.Performance.compiler",
    (platform.Performance, 'coupler_load'): "cim.2.platform.Performance.coupler_load",
    (platform.Performance, 'io_load'): "cim.2.platform.Performance.io_load",
    (platform.Performance, 'load_imbalance'): "cim.2.platform.Performance.load_imbalance",
    (platform.Performance, 'memory_bloat'): "cim.2.platform.Performance.memory_bloat",
    (platform.Performance, 'meta'): "cim.2.platform.Performance.meta",
    (platform.Performance, 'model'): "cim.2.platform.Performance.model",
    (platform.Performance, 'name'): "cim.2.platform.Performance.name",
    (platform.Performance, 'platform'): "cim.2.platform.Performance.platform",
    (platform.Performance, 'subcomponent_performance'): "cim.2.platform.Performance.subcomponent_performance",
    (platform.Performance, 'sypd'): "cim.2.platform.Performance.sypd",
    (platform.Performance, 'total_nodes_used'): "cim.2.platform.Performance.total_nodes_used",
    (platform.StoragePool, 'description'): "cim.2.platform.StoragePool.description",
    (platform.StoragePool, 'name'): "cim.2.platform.StoragePool.name",
    (platform.StoragePool, 'type'): "cim.2.platform.StoragePool.type",
    (platform.StoragePool, 'vendor'): "cim.2.platform.StoragePool.vendor",
    (platform.StoragePool, 'volume_available'): "cim.2.platform.StoragePool.volume_available",
    (platform.StorageVolume, 'units'): "cim.2.platform.StorageVolume.units",
    (platform.StorageVolume, 'volume'): "cim.2.platform.StorageVolume.volume",
    (science.ConservationProperties, 'corrected_conserved_prognostic_variables'): "cim.2.science.ConservationProperties.corrected_conserved_prognostic_variables",
    (science.ConservationProperties, 'flux_correction_was_used'): "cim.2.science.ConservationProperties.flux_correction_was_used",
    (science.Extent, 'is_global'): "cim.2.science.Extent.is_global",
    (science.Extent, 'region_known_as'): "cim.2.science.Extent.region_known_as",
    (science.Grid, 'description'): "cim.2.science.Grid.description",
    (science.Grid, 'details'): "cim.2.science.Grid.details",
    (science.Grid, 'discretisation'): "cim.2.science.Grid.discretisation",
    (science.Grid, 'meta'): "cim.2.science.Grid.meta",
    (science.Grid, 'name'): "cim.2.science.Grid.name",
    (science.Grid, 'references'): "cim.2.science.Grid.references",
    (science.IsoExtent, 'eastern_boundary'): "cim.2.science.IsoExtent.eastern_boundary",
    (science.IsoExtent, 'northern_boundary'): "cim.2.science.IsoExtent.northern_boundary",
    (science.IsoExtent, 'southern_boundary'): "cim.2.science.IsoExtent.southern_boundary",
    (science.IsoExtent, 'western_boundary'): "cim.2.science.IsoExtent.western_boundary",
    (science.KeyProperties, 'extent'): "cim.2.science.KeyProperties.extent",
    (science.KeyProperties, 'extra_conservation_properties'): "cim.2.science.KeyProperties.extra_conservation_properties",
    (science.KeyProperties, 'resolution'): "cim.2.science.KeyProperties.resolution",
    (science.KeyProperties, 'time_step'): "cim.2.science.KeyProperties.time_step",
    (science.KeyProperties, 'tuning_applied'): "cim.2.science.KeyProperties.tuning_applied",
    (science.Model, 'category'): "cim.2.science.Model.category",
    (science.Model, 'coupled_components'): "cim.2.science.Model.coupled_components",
    (science.Model, 'coupler'): "cim.2.science.Model.coupler",
    (science.Model, 'id'): "cim.2.science.Model.id",
    (science.Model, 'internal_software_components'): "cim.2.science.Model.internal_software_components",
    (science.Model, 'meta'): "cim.2.science.Model.meta",
    (science.Model, 'model_key_properties'): "cim.2.science.Model.model_key_properties",
    (science.Model, 'simulates'): "cim.2.science.Model.simulates",
    (science.Process, 'details'): "cim.2.science.Process.details",
    (science.Process, 'implementation_overview'): "cim.2.science.Process.implementation_overview",
    (science.Process, 'keywords'): "cim.2.science.Process.keywords",
    (science.Process, 'references'): "cim.2.science.Process.references",
    (science.Process, 'sub_processes'): "cim.2.science.Process.sub_processes",
    (science.Resolution, 'canonical_horizontal_resolution'): "cim.2.science.Resolution.canonical_horizontal_resolution",
    (science.Resolution, 'is_adaptive_grid'): "cim.2.science.Resolution.is_adaptive_grid",
    (science.Resolution, 'name'): "cim.2.science.Resolution.name",
    (science.Resolution, 'number_of_horizontal_gridpoints'): "cim.2.science.Resolution.number_of_horizontal_gridpoints",
    (science.Resolution, 'number_of_vertical_levels'): "cim.2.science.Resolution.number_of_vertical_levels",
    (science.ScienceContext, 'description'): "cim.2.science.ScienceContext.description",
    (science.ScienceContext, 'id'): "cim.2.science.ScienceContext.id",
    (science.ScienceContext, 'short_name'): "cim.2.science.ScienceContext.short_name",
    (science.ScientificRealm, 'grid'): "cim.2.science.ScientificRealm.grid",
    (science.ScientificRealm, 'id'): "cim.2.science.ScientificRealm.id",
    (science.ScientificRealm, 'key_properties'): "cim.2.science.ScientificRealm.key_properties",
    (science.ScientificRealm, 'meta'): "cim.2.science.ScientificRealm.meta",
    (science.ScientificRealm, 'name'): "cim.2.science.ScientificRealm.name",
    (science.ScientificRealm, 'overview'): "cim.2.science.ScientificRealm.overview",
    (science.ScientificRealm, 'realm'): "cim.2.science.ScientificRealm.realm",
    (science.ScientificRealm, 'references'): "cim.2.science.ScientificRealm.references",
    (science.ScientificRealm, 'simulates'): "cim.2.science.ScientificRealm.simulates",
    (science.SubProcess, 'details'): "cim.2.science.SubProcess.details",
    (science.SubProcess, 'implementation_overview'): "cim.2.science.SubProcess.implementation_overview",
    (science.SubProcess, 'references'): "cim.2.science.SubProcess.references",
    (science.Tuning, 'description'): "cim.2.science.Tuning.description",
    (science.Tuning, 'global_mean_metrics_used'): "cim.2.science.Tuning.global_mean_metrics_used",
    (science.Tuning, 'regional_metrics_used'): "cim.2.science.Tuning.regional_metrics_used",
    (science.Tuning, 'trend_metrics_used'): "cim.2.science.Tuning.trend_metrics_used",
    (shared.Cimtext, 'content'): "cim.2.shared.Cimtext.content",
    (shared.Cimtext, 'content_type'): "cim.2.shared.Cimtext.content_type",
    (shared.Citation, 'abstract'): "cim.2.shared.Citation.abstract",
    (shared.Citation, 'citation_detail'): "cim.2.shared.Citation.citation_detail",
    (shared.Citation, 'collective_title'): "cim.2.shared.Citation.collective_title",
    (shared.Citation, 'context'): "cim.2.shared.Citation.context",
    (shared.Citation, 'doi'): "cim.2.shared.Citation.doi",
    (shared.Citation, 'meta'): "cim.2.shared.Citation.meta",
    (shared.Citation, 'title'): "cim.2.shared.Citation.title",
    (shared.Citation, 'type'): "cim.2.shared.Citation.type",
    (shared.Citation, 'url'): "cim.2.shared.Citation.url",
    (shared.CitationTarget, 'citation_detail'): "cim.2.shared.CitationTarget.citation_detail",
    (shared.CitationTarget, 'doi'): "cim.2.shared.CitationTarget.doi",
    (shared.CitationTarget, 'meta'): "cim.2.shared.CitationTarget.meta",
    (shared.CitationTarget, 'name'): "cim.2.shared.CitationTarget.name",
    (shared.CitationTarget, 'online_at'): "cim.2.shared.CitationTarget.online_at",
    (shared.CitationTarget, 'title'): "cim.2.shared.CitationTarget.title",
    (shared.DocMetaInfo, 'author'): "cim.2.shared.DocMetaInfo.author",
    (shared.DocMetaInfo, 'create_date'): "cim.2.shared.DocMetaInfo.create_date",
    (shared.DocMetaInfo, 'drs_keys'): "cim.2.shared.DocMetaInfo.drs_keys",
    (shared.DocMetaInfo, 'drs_path'): "cim.2.shared.DocMetaInfo.drs_path",
    (shared.DocMetaInfo, 'external_ids'): "cim.2.shared.DocMetaInfo.external_ids",
    (shared.DocMetaInfo, 'id'): "cim.2.shared.DocMetaInfo.id",
    (shared.DocMetaInfo, 'institute'): "cim.2.shared.DocMetaInfo.institute",
    (shared.DocMetaInfo, 'language'): "cim.2.shared.DocMetaInfo.language",
    (shared.DocMetaInfo, 'project'): "cim.2.shared.DocMetaInfo.project",
    (shared.DocMetaInfo, 'sort_key'): "cim.2.shared.DocMetaInfo.sort_key",
    (shared.DocMetaInfo, 'source'): "cim.2.shared.DocMetaInfo.source",
    (shared.DocMetaInfo, 'source_key'): "cim.2.shared.DocMetaInfo.source_key",
    (shared.DocMetaInfo, 'sub_projects'): "cim.2.shared.DocMetaInfo.sub_projects",
    (shared.DocMetaInfo, 'type'): "cim.2.shared.DocMetaInfo.type",
    (shared.DocMetaInfo, 'type_display_name'): "cim.2.shared.DocMetaInfo.type_display_name",
    (shared.DocMetaInfo, 'type_sort_key'): "cim.2.shared.DocMetaInfo.type_sort_key",
    (shared.DocMetaInfo, 'update_date'): "cim.2.shared.DocMetaInfo.update_date",
    (shared.DocMetaInfo, 'version'): "cim.2.shared.DocMetaInfo.version",
    (shared.DocReference, 'constraint_vocabulary'): "cim.2.shared.DocReference.constraint_vocabulary",
    (shared.DocReference, 'context'): "cim.2.shared.DocReference.context",
    (shared.DocReference, 'id'): "cim.2.shared.DocReference.id",
    (shared.DocReference, 'relationship'): "cim.2.shared.DocReference.relationship",
    (shared.DocReference, 'type'): "cim.2.shared.DocReference.type",
    (shared.DocReference, 'version'): "cim.2.shared.DocReference.version",
    (shared.ExtraAttribute, 'doc'): "cim.2.shared.ExtraAttribute.doc",
    (shared.ExtraAttribute, 'key'): "cim.2.shared.ExtraAttribute.key",
    (shared.ExtraAttribute, 'type'): "cim.2.shared.ExtraAttribute.type",
    (shared.ExtraAttribute, 'value'): "cim.2.shared.ExtraAttribute.value",
    (shared.OnlineResource, 'description'): "cim.2.shared.OnlineResource.description",
    (shared.OnlineResource, 'linkage'): "cim.2.shared.OnlineResource.linkage",
    (shared.OnlineResource, 'name'): "cim.2.shared.OnlineResource.name",
    (shared.OnlineResource, 'protocol'): "cim.2.shared.OnlineResource.protocol",
    (shared.Party, 'address'): "cim.2.shared.Party.address",
    (shared.Party, 'email'): "cim.2.shared.Party.email",
    (shared.Party, 'meta'): "cim.2.shared.Party.meta",
    (shared.Party, 'name'): "cim.2.shared.Party.name",
    (shared.Party, 'orcid_id'): "cim.2.shared.Party.orcid_id",
    (shared.Party, 'organisation'): "cim.2.shared.Party.organisation",
    (shared.Party, 'url'): "cim.2.shared.Party.url",
    (shared.QualityReview, 'date'): "cim.2.shared.QualityReview.date",
    (shared.QualityReview, 'meta'): "cim.2.shared.QualityReview.meta",
    (shared.QualityReview, 'metadata_reviewer'): "cim.2.shared.QualityReview.metadata_reviewer",
    (shared.QualityReview, 'quality_description'): "cim.2.shared.QualityReview.quality_description",
    (shared.QualityReview, 'quality_status'): "cim.2.shared.QualityReview.quality_status",
    (shared.QualityReview, 'target_document'): "cim.2.shared.QualityReview.target_document",
    (shared.Reference, 'context'): "cim.2.shared.Reference.context",
    (shared.Reference, 'document'): "cim.2.shared.Reference.document",
    (shared.Responsibility, 'party'): "cim.2.shared.Responsibility.party",
    (shared.Responsibility, 'role'): "cim.2.shared.Responsibility.role",
    (shared.Responsibility, 'when'): "cim.2.shared.Responsibility.when",
    (software.ComponentBase, 'description'): "cim.2.software.ComponentBase.description",
    (software.ComponentBase, 'development_history'): "cim.2.software.ComponentBase.development_history",
    (software.ComponentBase, 'documentation'): "cim.2.software.ComponentBase.documentation",
    (software.ComponentBase, 'long_name'): "cim.2.software.ComponentBase.long_name",
    (software.ComponentBase, 'name'): "cim.2.software.ComponentBase.name",
    (software.ComponentBase, 'release_date'): "cim.2.software.ComponentBase.release_date",
    (software.ComponentBase, 'repository'): "cim.2.software.ComponentBase.repository",
    (software.ComponentBase, 'version'): "cim.2.software.ComponentBase.version",
    (software.Composition, 'couplings'): "cim.2.software.Composition.couplings",
    (software.Composition, 'description'): "cim.2.software.Composition.description",
    (software.DevelopmentPath, 'consortium_name'): "cim.2.software.DevelopmentPath.consortium_name",
    (software.DevelopmentPath, 'creators'): "cim.2.software.DevelopmentPath.creators",
    (software.DevelopmentPath, 'developed_in_house'): "cim.2.software.DevelopmentPath.developed_in_house",
    (software.DevelopmentPath, 'funding_sources'): "cim.2.software.DevelopmentPath.funding_sources",
    (software.DevelopmentPath, 'previous_version'): "cim.2.software.DevelopmentPath.previous_version",
    (software.EntryPoint, 'name'): "cim.2.software.EntryPoint.name",
    (software.Gridspec, 'description'): "cim.2.software.Gridspec.description",
    (software.SoftwareComponent, 'composition'): "cim.2.software.SoftwareComponent.composition",
    (software.SoftwareComponent, 'connection_points'): "cim.2.software.SoftwareComponent.connection_points",
    (software.SoftwareComponent, 'coupling_framework'): "cim.2.software.SoftwareComponent.coupling_framework",
    (software.SoftwareComponent, 'dependencies'): "cim.2.software.SoftwareComponent.dependencies",
    (software.SoftwareComponent, 'grid'): "cim.2.software.SoftwareComponent.grid",
    (software.SoftwareComponent, 'language'): "cim.2.software.SoftwareComponent.language",
    (software.SoftwareComponent, 'license'): "cim.2.software.SoftwareComponent.license",
    (software.SoftwareComponent, 'sub_components'): "cim.2.software.SoftwareComponent.sub_components",
    (software.Variable, 'description'): "cim.2.software.Variable.description",
    (software.Variable, 'name'): "cim.2.software.Variable.name",
    (software.Variable, 'prognostic'): "cim.2.software.Variable.prognostic",
    (time.Calendar, 'description'): "cim.2.time.Calendar.description",
    (time.Calendar, 'month_lengths'): "cim.2.time.Calendar.month_lengths",
    (time.Calendar, 'name'): "cim.2.time.Calendar.name",
    (time.Calendar, 'standard_name'): "cim.2.time.Calendar.standard_name",
    (time.DateTime, 'offset'): "cim.2.time.DateTime.offset",
    (time.DateTime, 'value'): "cim.2.time.DateTime.value",
    (time.DatetimeSet, 'length'): "cim.2.time.DatetimeSet.length",
    (time.IrregularDateset, 'date_set'): "cim.2.time.IrregularDateset.date_set",
    (time.RegularTimeset, 'increment'): "cim.2.time.RegularTimeset.increment",
    (time.RegularTimeset, 'length'): "cim.2.time.RegularTimeset.length",
    (time.RegularTimeset, 'start_date'): "cim.2.time.RegularTimeset.start_date",
    (time.TimePeriod, 'calendar'): "cim.2.time.TimePeriod.calendar",
    (time.TimePeriod, 'date'): "cim.2.time.TimePeriod.date",
    (time.TimePeriod, 'date_type'): "cim.2.time.TimePeriod.date_type",
    (time.TimePeriod, 'length'): "cim.2.time.TimePeriod.length",
    (time.TimePeriod, 'units'): "cim.2.time.TimePeriod.units",

    # ------------------------------------------------
    # Enums.
    # ------------------------------------------------

    activity.ConformanceType: "cim.2.activity.ConformanceType",
    data.DataAssociationTypes: "cim.2.data.DataAssociationTypes",
    designing.EnsembleTypes: "cim.2.designing.EnsembleTypes",
    designing.ExperimentalRelationships: "cim.2.designing.ExperimentalRelationships",
    designing.ForcingTypes: "cim.2.designing.ForcingTypes",
    drs.DrsFrequencyTypes: "cim.2.drs.DrsFrequencyTypes",
    drs.DrsGeographicalOperators: "cim.2.drs.DrsGeographicalOperators",
    drs.DrsRealms: "cim.2.drs.DrsRealms",
    drs.DrsTimeSuffixes: "cim.2.drs.DrsTimeSuffixes",
    platform.StorageSystems: "cim.2.platform.StorageSystems",
    platform.VolumeUnits: "cim.2.platform.VolumeUnits",
    science.ModelTypes: "cim.2.science.ModelTypes",
    science.SelectionCardinality: "cim.2.science.SelectionCardinality",
    shared.DocumentTypes: "cim.2.shared.DocumentTypes",
    shared.NilReason: "cim.2.shared.NilReason",
    shared.QualityStatus: "cim.2.shared.QualityStatus",
    shared.RoleCode: "cim.2.shared.RoleCode",
    shared.TextCode: "cim.2.shared.TextCode",
    software.CouplingFramework: "cim.2.software.CouplingFramework",
    software.ProgrammingLanguage: "cim.2.software.ProgrammingLanguage",
    time.CalendarTypes: "cim.2.time.CalendarTypes",
    time.PeriodDateTypes: "cim.2.time.PeriodDateTypes",
    time.TimeUnits: "cim.2.time.TimeUnits",

    # ------------------------------------------------
    # Enum members.
    # ------------------------------------------------

    (activity.ConformanceType, 'Conformed'): "cim.2.activity.ConformanceType.Conformed",
    (activity.ConformanceType, 'Not Applicable'): "cim.2.activity.ConformanceType.Not-Applicable",
    (activity.ConformanceType, 'Not Conformed'): "cim.2.activity.ConformanceType.Not-Conformed",
    (activity.ConformanceType, 'Partially Conformed'): "cim.2.activity.ConformanceType.Partially-Conformed",
    (data.DataAssociationTypes, 'isComposedOf'): "cim.2.data.DataAssociationTypes.isComposedOf",
    (data.DataAssociationTypes, 'partOf'): "cim.2.data.DataAssociationTypes.partOf",
    (data.DataAssociationTypes, 'revisonOf'): "cim.2.data.DataAssociationTypes.revisonOf",
    (designing.EnsembleTypes, 'Driven'): "cim.2.designing.EnsembleTypes.Driven",
    (designing.EnsembleTypes, 'Forced'): "cim.2.designing.EnsembleTypes.Forced",
    (designing.EnsembleTypes, 'Initialisation Method'): "cim.2.designing.EnsembleTypes.Initialisation-Method",
    (designing.EnsembleTypes, 'Perturbed Physics'): "cim.2.designing.EnsembleTypes.Perturbed-Physics",
    (designing.EnsembleTypes, 'Realization'): "cim.2.designing.EnsembleTypes.Realization",
    (designing.EnsembleTypes, 'Resolution'): "cim.2.designing.EnsembleTypes.Resolution",
    (designing.EnsembleTypes, 'Start Date'): "cim.2.designing.EnsembleTypes.Start-Date",
    (designing.ExperimentalRelationships, 'control_for'): "cim.2.designing.ExperimentalRelationships.control_for",
    (designing.ExperimentalRelationships, 'initialisation_for'): "cim.2.designing.ExperimentalRelationships.initialisation_for",
    (designing.ExperimentalRelationships, 'is_sibling'): "cim.2.designing.ExperimentalRelationships.is_sibling",
    (designing.ExperimentalRelationships, 'provides_constraints'): "cim.2.designing.ExperimentalRelationships.provides_constraints",
    (designing.ForcingTypes, 'driven'): "cim.2.designing.ForcingTypes.driven",
    (designing.ForcingTypes, 'historical'): "cim.2.designing.ForcingTypes.historical",
    (designing.ForcingTypes, 'idealised'): "cim.2.designing.ForcingTypes.idealised",
    (designing.ForcingTypes, 'scenario'): "cim.2.designing.ForcingTypes.scenario",
    (drs.DrsFrequencyTypes, '3hr'): "cim.2.drs.DrsFrequencyTypes.3hr",
    (drs.DrsFrequencyTypes, '6hr'): "cim.2.drs.DrsFrequencyTypes.6hr",
    (drs.DrsFrequencyTypes, 'day'): "cim.2.drs.DrsFrequencyTypes.day",
    (drs.DrsFrequencyTypes, 'fx'): "cim.2.drs.DrsFrequencyTypes.fx",
    (drs.DrsFrequencyTypes, 'mon'): "cim.2.drs.DrsFrequencyTypes.mon",
    (drs.DrsFrequencyTypes, 'monClim'): "cim.2.drs.DrsFrequencyTypes.monClim",
    (drs.DrsFrequencyTypes, 'subhr'): "cim.2.drs.DrsFrequencyTypes.subhr",
    (drs.DrsFrequencyTypes, 'yr'): "cim.2.drs.DrsFrequencyTypes.yr",
    (drs.DrsGeographicalOperators, 'areaavg'): "cim.2.drs.DrsGeographicalOperators.areaavg",
    (drs.DrsGeographicalOperators, 'lnd-areaavg'): "cim.2.drs.DrsGeographicalOperators.lnd-areaavg",
    (drs.DrsGeographicalOperators, 'lnd-zonalavg'): "cim.2.drs.DrsGeographicalOperators.lnd-zonalavg",
    (drs.DrsGeographicalOperators, 'ocn-areaavg'): "cim.2.drs.DrsGeographicalOperators.ocn-areaavg",
    (drs.DrsGeographicalOperators, 'ocn-zonalavg'): "cim.2.drs.DrsGeographicalOperators.ocn-zonalavg",
    (drs.DrsGeographicalOperators, 'zonalavg'): "cim.2.drs.DrsGeographicalOperators.zonalavg",
    (drs.DrsRealms, 'aerosol'): "cim.2.drs.DrsRealms.aerosol",
    (drs.DrsRealms, 'atmos'): "cim.2.drs.DrsRealms.atmos",
    (drs.DrsRealms, 'atmosChem'): "cim.2.drs.DrsRealms.atmosChem",
    (drs.DrsRealms, 'land'): "cim.2.drs.DrsRealms.land",
    (drs.DrsRealms, 'landIce'): "cim.2.drs.DrsRealms.landIce",
    (drs.DrsRealms, 'ocean'): "cim.2.drs.DrsRealms.ocean",
    (drs.DrsRealms, 'ocnBgchem'): "cim.2.drs.DrsRealms.ocnBgchem",
    (drs.DrsRealms, 'seaIce'): "cim.2.drs.DrsRealms.seaIce",
    (drs.DrsTimeSuffixes, 'avg'): "cim.2.drs.DrsTimeSuffixes.avg",
    (drs.DrsTimeSuffixes, 'clim'): "cim.2.drs.DrsTimeSuffixes.clim",
    (platform.StorageSystems, 'GPFS'): "cim.2.platform.StorageSystems.GPFS",
    (platform.StorageSystems, 'Lustre'): "cim.2.platform.StorageSystems.Lustre",
    (platform.StorageSystems, 'NFS'): "cim.2.platform.StorageSystems.NFS",
    (platform.StorageSystems, 'Other Disk'): "cim.2.platform.StorageSystems.Other-Disk",
    (platform.StorageSystems, 'PanFS'): "cim.2.platform.StorageSystems.PanFS",
    (platform.StorageSystems, 'S3'): "cim.2.platform.StorageSystems.S3",
    (platform.StorageSystems, 'Tape - Castor'): "cim.2.platform.StorageSystems.Tape---Castor",
    (platform.StorageSystems, 'Tape - MARS'): "cim.2.platform.StorageSystems.Tape---MARS",
    (platform.StorageSystems, 'Tape - MASS'): "cim.2.platform.StorageSystems.Tape---MASS",
    (platform.StorageSystems, 'Tape - Other'): "cim.2.platform.StorageSystems.Tape---Other",
    (platform.StorageSystems, 'isilon'): "cim.2.platform.StorageSystems.isilon",
    (platform.VolumeUnits, 'EB'): "cim.2.platform.VolumeUnits.EB",
    (platform.VolumeUnits, 'EiB'): "cim.2.platform.VolumeUnits.EiB",
    (platform.VolumeUnits, 'GB'): "cim.2.platform.VolumeUnits.GB",
    (platform.VolumeUnits, 'PB'): "cim.2.platform.VolumeUnits.PB",
    (platform.VolumeUnits, 'PiB'): "cim.2.platform.VolumeUnits.PiB",
    (platform.VolumeUnits, 'TB'): "cim.2.platform.VolumeUnits.TB",
    (platform.VolumeUnits, 'TiB'): "cim.2.platform.VolumeUnits.TiB",
    (science.ModelTypes, 'Atm Only'): "cim.2.science.ModelTypes.Atm-Only",
    (science.ModelTypes, 'GCM'): "cim.2.science.ModelTypes.GCM",
    (science.ModelTypes, 'GCM-MLO'): "cim.2.science.ModelTypes.GCM-MLO",
    (science.ModelTypes, 'IGCM'): "cim.2.science.ModelTypes.IGCM",
    (science.ModelTypes, 'Mesoscale'): "cim.2.science.ModelTypes.Mesoscale",
    (science.ModelTypes, 'Ocean Only'): "cim.2.science.ModelTypes.Ocean-Only",
    (science.ModelTypes, 'Planetary'): "cim.2.science.ModelTypes.Planetary",
    (science.ModelTypes, 'Process'): "cim.2.science.ModelTypes.Process",
    (science.ModelTypes, 'Regional'): "cim.2.science.ModelTypes.Regional",
    (science.SelectionCardinality, '0.1'): "cim.2.science.SelectionCardinality.0.1",
    (science.SelectionCardinality, '0.N'): "cim.2.science.SelectionCardinality.0.N",
    (science.SelectionCardinality, '1.1'): "cim.2.science.SelectionCardinality.1.1",
    (science.SelectionCardinality, '1.N'): "cim.2.science.SelectionCardinality.1.N",
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
    (shared.DocumentTypes, 'Performance'): "cim.2.shared.DocumentTypes.Performance",
    (shared.DocumentTypes, 'Project'): "cim.2.shared.DocumentTypes.Project",
    (shared.DocumentTypes, 'QualityReview'): "cim.2.shared.DocumentTypes.QualityReview",
    (shared.DocumentTypes, 'ScientificDomain'): "cim.2.shared.DocumentTypes.ScientificDomain",
    (shared.DocumentTypes, 'Simulation'): "cim.2.shared.DocumentTypes.Simulation",
    (shared.DocumentTypes, 'SimulationPlan'): "cim.2.shared.DocumentTypes.SimulationPlan",
    (shared.DocumentTypes, 'TemporalConstraint'): "cim.2.shared.DocumentTypes.TemporalConstraint",
    (shared.DocumentTypes, 'UberEnsemble'): "cim.2.shared.DocumentTypes.UberEnsemble",
    (shared.NilReason, 'nil:inapplicable'): "cim.2.shared.NilReason.nil:inapplicable",
    (shared.NilReason, 'nil:missing'): "cim.2.shared.NilReason.nil:missing",
    (shared.NilReason, 'nil:template'): "cim.2.shared.NilReason.nil:template",
    (shared.NilReason, 'nil:unknown'): "cim.2.shared.NilReason.nil:unknown",
    (shared.NilReason, 'nil:withheld'): "cim.2.shared.NilReason.nil:withheld",
    (shared.QualityStatus, 'finalised'): "cim.2.shared.QualityStatus.finalised",
    (shared.QualityStatus, 'incomplete'): "cim.2.shared.QualityStatus.incomplete",
    (shared.QualityStatus, 'reviewed'): "cim.2.shared.QualityStatus.reviewed",
    (shared.QualityStatus, 'under_review'): "cim.2.shared.QualityStatus.under_review",
    (shared.RoleCode, 'Principal Investigator'): "cim.2.shared.RoleCode.Principal-Investigator",
    (shared.RoleCode, 'author'): "cim.2.shared.RoleCode.author",
    (shared.RoleCode, 'collaborator'): "cim.2.shared.RoleCode.collaborator",
    (shared.RoleCode, 'custodian'): "cim.2.shared.RoleCode.custodian",
    (shared.RoleCode, 'distributor'): "cim.2.shared.RoleCode.distributor",
    (shared.RoleCode, 'metadata_author'): "cim.2.shared.RoleCode.metadata_author",
    (shared.RoleCode, 'metadata_reviewer'): "cim.2.shared.RoleCode.metadata_reviewer",
    (shared.RoleCode, 'originator'): "cim.2.shared.RoleCode.originator",
    (shared.RoleCode, 'owner'): "cim.2.shared.RoleCode.owner",
    (shared.RoleCode, 'point of contact'): "cim.2.shared.RoleCode.point-of-contact",
    (shared.RoleCode, 'processor'): "cim.2.shared.RoleCode.processor",
    (shared.RoleCode, 'publisher'): "cim.2.shared.RoleCode.publisher",
    (shared.RoleCode, 'resource provider'): "cim.2.shared.RoleCode.resource-provider",
    (shared.RoleCode, 'sponsor'): "cim.2.shared.RoleCode.sponsor",
    (shared.RoleCode, 'user'): "cim.2.shared.RoleCode.user",
    (shared.TextCode, 'plaintext'): "cim.2.shared.TextCode.plaintext",
    (software.CouplingFramework, 'Bespoke'): "cim.2.software.CouplingFramework.Bespoke",
    (software.CouplingFramework, 'ESMF'): "cim.2.software.CouplingFramework.ESMF",
    (software.CouplingFramework, 'NUOPC'): "cim.2.software.CouplingFramework.NUOPC",
    (software.CouplingFramework, 'None'): "cim.2.software.CouplingFramework.None",
    (software.CouplingFramework, 'OASIS'): "cim.2.software.CouplingFramework.OASIS",
    (software.CouplingFramework, 'OASIS3-MCT'): "cim.2.software.CouplingFramework.OASIS3-MCT",
    (software.CouplingFramework, 'Unknown'): "cim.2.software.CouplingFramework.Unknown",
    (software.ProgrammingLanguage, 'C'): "cim.2.software.ProgrammingLanguage.C",
    (software.ProgrammingLanguage, 'C++'): "cim.2.software.ProgrammingLanguage.C++",
    (software.ProgrammingLanguage, 'Fortran'): "cim.2.software.ProgrammingLanguage.Fortran",
    (software.ProgrammingLanguage, 'Python'): "cim.2.software.ProgrammingLanguage.Python",
    (time.CalendarTypes, '360_day'): "cim.2.time.CalendarTypes.360_day",
    (time.CalendarTypes, '365_day'): "cim.2.time.CalendarTypes.365_day",
    (time.CalendarTypes, '366_day'): "cim.2.time.CalendarTypes.366_day",
    (time.CalendarTypes, 'all_leap'): "cim.2.time.CalendarTypes.all_leap",
    (time.CalendarTypes, 'gregorian'): "cim.2.time.CalendarTypes.gregorian",
    (time.CalendarTypes, 'julian'): "cim.2.time.CalendarTypes.julian",
    (time.CalendarTypes, 'noleap'): "cim.2.time.CalendarTypes.noleap",
    (time.CalendarTypes, 'none'): "cim.2.time.CalendarTypes.none",
    (time.CalendarTypes, 'proleptic_gregorian'): "cim.2.time.CalendarTypes.proleptic_gregorian",
    (time.CalendarTypes, 'standard'): "cim.2.time.CalendarTypes.standard",
    (time.PeriodDateTypes, 'date is end'): "cim.2.time.PeriodDateTypes.date-is-end",
    (time.PeriodDateTypes, 'date is start'): "cim.2.time.PeriodDateTypes.date-is-start",
    (time.PeriodDateTypes, 'unused'): "cim.2.time.PeriodDateTypes.unused",
    (time.TimeUnits, 'days'): "cim.2.time.TimeUnits.days",
    (time.TimeUnits, 'months'): "cim.2.time.TimeUnits.months",
    (time.TimeUnits, 'seconds'): "cim.2.time.TimeUnits.seconds",
    (time.TimeUnits, 'years'): "cim.2.time.TimeUnits.years",
}

# Set inline type keys.
activity.Activity.type_key = KEYS[activity.Activity]
activity.AxisMember.type_key = KEYS[activity.AxisMember]
activity.Conformance.type_key = KEYS[activity.Conformance]
activity.ConformanceType.type_key = KEYS[activity.ConformanceType]
activity.Ensemble.type_key = KEYS[activity.Ensemble]
activity.EnsembleAxis.type_key = KEYS[activity.EnsembleAxis]
activity.EnsembleMember.type_key = KEYS[activity.EnsembleMember]
activity.ParentSimulation.type_key = KEYS[activity.ParentSimulation]
activity.UberEnsemble.type_key = KEYS[activity.UberEnsemble]
data.DataAssociationTypes.type_key = KEYS[data.DataAssociationTypes]
data.Dataset.type_key = KEYS[data.Dataset]
data.Downscaling.type_key = KEYS[data.Downscaling]
data.Simulation.type_key = KEYS[data.Simulation]
data.VariableCollection.type_key = KEYS[data.VariableCollection]
designing.AxisMember.type_key = KEYS[designing.AxisMember]
designing.DomainRequirements.type_key = KEYS[designing.DomainRequirements]
designing.EnsembleRequirement.type_key = KEYS[designing.EnsembleRequirement]
designing.EnsembleTypes.type_key = KEYS[designing.EnsembleTypes]
designing.ExperimentalRelationships.type_key = KEYS[designing.ExperimentalRelationships]
designing.ForcingConstraint.type_key = KEYS[designing.ForcingConstraint]
designing.ForcingTypes.type_key = KEYS[designing.ForcingTypes]
designing.InitialisationRequirement.type_key = KEYS[designing.InitialisationRequirement]
designing.MultiEnsemble.type_key = KEYS[designing.MultiEnsemble]
designing.NumericalExperiment.type_key = KEYS[designing.NumericalExperiment]
designing.NumericalRequirement.type_key = KEYS[designing.NumericalRequirement]
designing.OutputRequirement.type_key = KEYS[designing.OutputRequirement]
designing.Project.type_key = KEYS[designing.Project]
designing.SimulationPlan.type_key = KEYS[designing.SimulationPlan]
designing.StartDateEnsemble.type_key = KEYS[designing.StartDateEnsemble]
designing.TemporalConstraint.type_key = KEYS[designing.TemporalConstraint]
drs.DrsAtomicDataset.type_key = KEYS[drs.DrsAtomicDataset]
drs.DrsEnsembleIdentifier.type_key = KEYS[drs.DrsEnsembleIdentifier]
drs.DrsExperiment.type_key = KEYS[drs.DrsExperiment]
drs.DrsFrequencyTypes.type_key = KEYS[drs.DrsFrequencyTypes]
drs.DrsGeographicalIndicator.type_key = KEYS[drs.DrsGeographicalIndicator]
drs.DrsGeographicalOperators.type_key = KEYS[drs.DrsGeographicalOperators]
drs.DrsPublicationDataset.type_key = KEYS[drs.DrsPublicationDataset]
drs.DrsRealms.type_key = KEYS[drs.DrsRealms]
drs.DrsSimulationIdentifier.type_key = KEYS[drs.DrsSimulationIdentifier]
drs.DrsTemporalIdentifier.type_key = KEYS[drs.DrsTemporalIdentifier]
drs.DrsTimeSuffixes.type_key = KEYS[drs.DrsTimeSuffixes]
platform.ComponentPerformance.type_key = KEYS[platform.ComponentPerformance]
platform.ComputePool.type_key = KEYS[platform.ComputePool]
platform.Machine.type_key = KEYS[platform.Machine]
platform.Partition.type_key = KEYS[platform.Partition]
platform.Performance.type_key = KEYS[platform.Performance]
platform.StoragePool.type_key = KEYS[platform.StoragePool]
platform.StorageSystems.type_key = KEYS[platform.StorageSystems]
platform.StorageVolume.type_key = KEYS[platform.StorageVolume]
platform.VolumeUnits.type_key = KEYS[platform.VolumeUnits]
science.ConservationProperties.type_key = KEYS[science.ConservationProperties]
science.Detail.type_key = KEYS[science.Detail]
science.Discretisation.type_key = KEYS[science.Discretisation]
science.Extent.type_key = KEYS[science.Extent]
science.Grid.type_key = KEYS[science.Grid]
science.IsoExtent.type_key = KEYS[science.IsoExtent]
science.KeyProperties.type_key = KEYS[science.KeyProperties]
science.Model.type_key = KEYS[science.Model]
science.ModelTypes.type_key = KEYS[science.ModelTypes]
science.Process.type_key = KEYS[science.Process]
science.Resolution.type_key = KEYS[science.Resolution]
science.ScienceContext.type_key = KEYS[science.ScienceContext]
science.ScientificRealm.type_key = KEYS[science.ScientificRealm]
science.SelectionCardinality.type_key = KEYS[science.SelectionCardinality]
science.SubProcess.type_key = KEYS[science.SubProcess]
science.Tuning.type_key = KEYS[science.Tuning]
shared.Cimtext.type_key = KEYS[shared.Cimtext]
shared.Citation.type_key = KEYS[shared.Citation]
shared.CitationTarget.type_key = KEYS[shared.CitationTarget]
shared.DocMetaInfo.type_key = KEYS[shared.DocMetaInfo]
shared.DocReference.type_key = KEYS[shared.DocReference]
shared.DocumentTypes.type_key = KEYS[shared.DocumentTypes]
shared.ExtraAttribute.type_key = KEYS[shared.ExtraAttribute]
shared.NilReason.type_key = KEYS[shared.NilReason]
shared.OnlineResource.type_key = KEYS[shared.OnlineResource]
shared.Party.type_key = KEYS[shared.Party]
shared.QualityReview.type_key = KEYS[shared.QualityReview]
shared.QualityStatus.type_key = KEYS[shared.QualityStatus]
shared.Reference.type_key = KEYS[shared.Reference]
shared.Responsibility.type_key = KEYS[shared.Responsibility]
shared.RoleCode.type_key = KEYS[shared.RoleCode]
shared.TextCode.type_key = KEYS[shared.TextCode]
software.ComponentBase.type_key = KEYS[software.ComponentBase]
software.Composition.type_key = KEYS[software.Composition]
software.CouplingFramework.type_key = KEYS[software.CouplingFramework]
software.DevelopmentPath.type_key = KEYS[software.DevelopmentPath]
software.EntryPoint.type_key = KEYS[software.EntryPoint]
software.Gridspec.type_key = KEYS[software.Gridspec]
software.ProgrammingLanguage.type_key = KEYS[software.ProgrammingLanguage]
software.SoftwareComponent.type_key = KEYS[software.SoftwareComponent]
software.Variable.type_key = KEYS[software.Variable]
time.Calendar.type_key = KEYS[time.Calendar]
time.CalendarTypes.type_key = KEYS[time.CalendarTypes]
time.DateTime.type_key = KEYS[time.DateTime]
time.DatetimeSet.type_key = KEYS[time.DatetimeSet]
time.IrregularDateset.type_key = KEYS[time.IrregularDateset]
time.PeriodDateTypes.type_key = KEYS[time.PeriodDateTypes]
time.RegularTimeset.type_key = KEYS[time.RegularTimeset]
time.TimePeriod.type_key = KEYS[time.TimePeriod]
time.TimeUnits.type_key = KEYS[time.TimeUnits]



# Remove import dross.
del defaultdict
del datetime
del uuid
del activity
del data
del designing
del drs
del platform
del science
del shared
del software
del time

