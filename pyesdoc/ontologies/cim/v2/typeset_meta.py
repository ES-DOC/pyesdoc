# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_meta.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encpasulates meta-information pertaining to the cim.v2 typeset.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
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




# Set type keys.
activity.Activity.type_key = u'cim.2.activity.Activity'
activity.AxisMember.type_key = u'cim.2.activity.AxisMember'
activity.Conformance.type_key = u'cim.2.activity.Conformance'
activity.Ensemble.type_key = u'cim.2.activity.Ensemble'
activity.EnsembleAxis.type_key = u'cim.2.activity.EnsembleAxis'
activity.EnsembleMember.type_key = u'cim.2.activity.EnsembleMember'
activity.ParentSimulation.type_key = u'cim.2.activity.ParentSimulation'
activity.UberEnsemble.type_key = u'cim.2.activity.UberEnsemble'
data.Dataset.type_key = u'cim.2.data.Dataset'
data.Downscaling.type_key = u'cim.2.data.Downscaling'
data.Simulation.type_key = u'cim.2.data.Simulation'
data.VariableCollection.type_key = u'cim.2.data.VariableCollection'
designing.DomainProperties.type_key = u'cim.2.designing.DomainProperties'
designing.EnsembleRequirement.type_key = u'cim.2.designing.EnsembleRequirement'
designing.ForcingConstraint.type_key = u'cim.2.designing.ForcingConstraint'
designing.MultiEnsemble.type_key = u'cim.2.designing.MultiEnsemble'
designing.MultiTimeEnsemble.type_key = u'cim.2.designing.MultiTimeEnsemble'
designing.NumericalExperiment.type_key = u'cim.2.designing.NumericalExperiment'
designing.NumericalRequirement.type_key = u'cim.2.designing.NumericalRequirement'
designing.OutputTemporalRequirement.type_key = u'cim.2.designing.OutputTemporalRequirement'
designing.Project.type_key = u'cim.2.designing.Project'
designing.SimulationPlan.type_key = u'cim.2.designing.SimulationPlan'
designing.TemporalConstraint.type_key = u'cim.2.designing.TemporalConstraint'
drs.DrsAtomicDataset.type_key = u'cim.2.drs.DrsAtomicDataset'
drs.DrsEnsembleIdentifier.type_key = u'cim.2.drs.DrsEnsembleIdentifier'
drs.DrsGeographicalIndicator.type_key = u'cim.2.drs.DrsGeographicalIndicator'
drs.DrsPublicationDataset.type_key = u'cim.2.drs.DrsPublicationDataset'
drs.DrsTemporalIdentifier.type_key = u'cim.2.drs.DrsTemporalIdentifier'
platform.ComponentPerformance.type_key = u'cim.2.platform.ComponentPerformance'
platform.ComputePool.type_key = u'cim.2.platform.ComputePool'
platform.Machine.type_key = u'cim.2.platform.Machine'
platform.Partition.type_key = u'cim.2.platform.Partition'
platform.Performance.type_key = u'cim.2.platform.Performance'
platform.StoragePool.type_key = u'cim.2.platform.StoragePool'
platform.StorageVolume.type_key = u'cim.2.platform.StorageVolume'
science.Algorithm.type_key = u'cim.2.science.Algorithm'
science.ConservationProperties.type_key = u'cim.2.science.ConservationProperties'
science.Detail.type_key = u'cim.2.science.Detail'
science.Extent.type_key = u'cim.2.science.Extent'
science.Grid.type_key = u'cim.2.science.Grid'
science.KeyProperties.type_key = u'cim.2.science.KeyProperties'
science.Model.type_key = u'cim.2.science.Model'
science.Process.type_key = u'cim.2.science.Process'
science.Resolution.type_key = u'cim.2.science.Resolution'
science.ScienceContext.type_key = u'cim.2.science.ScienceContext'
science.ScientificDomain.type_key = u'cim.2.science.ScientificDomain'
science.SubProcess.type_key = u'cim.2.science.SubProcess'
science.Tuning.type_key = u'cim.2.science.Tuning'
shared.Calendar.type_key = u'cim.2.shared.Calendar'
shared.Cimtext.type_key = u'cim.2.shared.Cimtext'
shared.DateTime.type_key = u'cim.2.shared.DateTime'
shared.DatetimeSet.type_key = u'cim.2.shared.DatetimeSet'
shared.DocMetaInfo.type_key = u'cim.2.shared.DocMetaInfo'
shared.DocReference.type_key = u'cim.2.shared.DocReference'
shared.ExternalDocument.type_key = u'cim.2.shared.ExternalDocument'
shared.IrregularDateset.type_key = u'cim.2.shared.IrregularDateset'
shared.KeyFloat.type_key = u'cim.2.shared.KeyFloat'
shared.NumberArray.type_key = u'cim.2.shared.NumberArray'
shared.OnlineResource.type_key = u'cim.2.shared.OnlineResource'
shared.Party.type_key = u'cim.2.shared.Party'
shared.Pid.type_key = u'cim.2.shared.Pid'
shared.QualityReview.type_key = u'cim.2.shared.QualityReview'
shared.Reference.type_key = u'cim.2.shared.Reference'
shared.RegularTimeset.type_key = u'cim.2.shared.RegularTimeset'
shared.Responsibility.type_key = u'cim.2.shared.Responsibility'
shared.TimePeriod.type_key = u'cim.2.shared.TimePeriod'
shared.TimesliceList.type_key = u'cim.2.shared.TimesliceList'
software.ComponentBase.type_key = u'cim.2.software.ComponentBase'
software.Composition.type_key = u'cim.2.software.Composition'
software.DevelopmentPath.type_key = u'cim.2.software.DevelopmentPath'
software.EntryPoint.type_key = u'cim.2.software.EntryPoint'
software.Gridspec.type_key = u'cim.2.software.Gridspec'
software.SoftwareComponent.type_key = u'cim.2.software.SoftwareComponent'
software.Variable.type_key = u'cim.2.software.Variable'


# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.Activity.type_info = (
    ('canonical_name', unicode, False, False),
    ('description', unicode, False, False),
    ('duration', shared.TimePeriod, False, False),
    ('keywords', unicode, False, True),
    ('long_name', unicode, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('name', unicode, True, False),
    ('rationale', unicode, False, False),
    ('references', shared.Reference, False, True),
    ('responsible_parties', shared.Responsibility, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.AxisMember.type_info = (
    ('description', unicode, True, False),
    ('extra_detail', unicode, False, False),
    ('index', int, True, False),
    ('value', float, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.Conformance.type_info = (
    ('target_requirement', designing.NumericalRequirement, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.Ensemble.type_info = (
    ('common_conformances', activity.Conformance, False, True),
    ('documentation', shared.OnlineResource, False, True),
    ('has_ensemble_axes', activity.EnsembleAxis, False, True),
    ('members', activity.EnsembleMember, True, True),
    ('part_of', activity.UberEnsemble, False, True),
    ('supported', designing.NumericalExperiment, True, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.EnsembleAxis.type_info = (
    ('extra_detail', unicode, True, False),
    ('member', activity.AxisMember, True, True),
    ('short_identifier', unicode, True, False),
    ('target_requirement', designing.NumericalRequirement, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.EnsembleMember.type_info = (
    ('errata', shared.OnlineResource, False, False),
    ('had_performance', platform.Performance, False, False),
    ('ran_on', platform.Machine, False, False),
    ('simulation', data.Simulation, True, False),
    ('variant_id', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.ParentSimulation.type_info = (
    ('branch_time_in_child', shared.DateTime, False, False),
    ('branch_time_in_parent', shared.DateTime, False, False),
    ('parent', data.Simulation, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.UberEnsemble.type_info = (
    ('child_ensembles', activity.Ensemble, True, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.Dataset.type_info = (
    ('availability', shared.OnlineResource, False, True),
    ('description', unicode, False, False),
    ('drs_datasets', drs.DrsPublicationDataset, False, True),
    ('meta', shared.DocMetaInfo, True, False),
    ('name', unicode, True, False),
    ('produced_by', data.Simulation, False, False),
    ('references', shared.Reference, False, True),
    ('related_to_dataset', shared.OnlineResource, False, True),
    ('responsible_parties', shared.Responsibility, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.Downscaling.type_info = (
    ('downscaled_from', data.Simulation, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.Simulation.type_info = (
    ('calendar', shared.Calendar, False, False),
    ('ensemble_identifier', unicode, True, False),
    ('parent_simulation', activity.ParentSimulation, False, False),
    ('part_of_project', designing.Project, True, True),
    ('primary_ensemble', activity.Ensemble, False, False),
    ('ran_for_experiments', designing.NumericalExperiment, True, True),
    ('used', science.Model, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.VariableCollection.type_info = (
    ('collection_name', unicode, False, False),
    ('variables', unicode, True, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
designing.DomainProperties.type_info = (
    ('required_extent', science.Extent, False, False),
    ('required_resolution', science.Resolution, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
designing.EnsembleRequirement.type_info = (
    ('ensemble_member', designing.NumericalRequirement, False, True),
    ('ensemble_type', unicode, True, False),
    ('minimum_size', int, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
designing.ForcingConstraint.type_info = (
    ('additional_constraint', unicode, False, False),
    ('category', unicode, False, False),
    ('code', unicode, False, False),
    ('data_link', shared.OnlineResource, False, False),
    ('forcing_type', unicode, True, False),
    ('group', unicode, False, False),
    ('origin', shared.Reference, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
designing.MultiEnsemble.type_info = (
    ('ensemble_axis', designing.EnsembleRequirement, True, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
designing.MultiTimeEnsemble.type_info = (
    ('ensemble_members', shared.DatetimeSet, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
designing.NumericalExperiment.type_info = (
    ('related_experiments', designing.NumericalExperiment, False, True),
    ('requirements', designing.NumericalRequirement, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
designing.NumericalRequirement.type_info = (
    ('additional_requirements', designing.NumericalRequirement, False, True),
    ('conformance_is_requested', bool, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
designing.OutputTemporalRequirement.type_info = (
    ('continuous_subset', shared.TimePeriod, False, True),
    ('sliced_subset', shared.TimesliceList, False, False),
    ('throughout', bool, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
designing.Project.type_info = (
    ('previous_projects', designing.Project, False, True),
    ('requires_experiments', designing.NumericalExperiment, False, True),
    ('sub_projects', designing.Project, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
designing.SimulationPlan.type_info = (
    ('expected_model', science.Model, True, False),
    ('expected_performance_sypd', float, False, False),
    ('expected_platform', platform.Machine, False, False),
    ('will_support_experiments', designing.NumericalExperiment, True, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
designing.TemporalConstraint.type_info = (
    ('required_calendar', shared.Calendar, False, False),
    ('required_duration', shared.TimePeriod, False, False),
    ('start_date', shared.DateTime, False, False),
    ('start_flexibility', shared.TimePeriod, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
drs.DrsAtomicDataset.type_info = (
    ('ensemble_member', drs.DrsEnsembleIdentifier, True, False),
    ('geographical_constraint', drs.DrsGeographicalIndicator, False, False),
    ('mip_table', unicode, True, False),
    ('temporal_constraint', drs.DrsTemporalIdentifier, False, False),
    ('variable_name', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
drs.DrsEnsembleIdentifier.type_info = (
    ('initialisation_method_number', int, True, False),
    ('perturbation_number', int, True, False),
    ('realisation_number', int, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
drs.DrsGeographicalIndicator.type_info = (
    ('bounding_box', unicode, False, False),
    ('operator', unicode, False, False),
    ('spatial_domain', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
drs.DrsPublicationDataset.type_info = (
    ('activity', unicode, True, False),
    ('experiment', unicode, True, False),
    ('frequency', unicode, False, False),
    ('institute', unicode, True, False),
    ('model', unicode, True, False),
    ('product', unicode, True, False),
    ('realm', unicode, False, False),
    ('version_number', int, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
drs.DrsTemporalIdentifier.type_info = (
    ('end', unicode, False, False),
    ('start', unicode, True, False),
    ('suffix', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
platform.ComponentPerformance.type_info = (
    ('component', software.SoftwareComponent, False, False),
    ('component_name', unicode, True, False),
    ('cores_used', int, False, False),
    ('nodes_used', int, False, False),
    ('speed', float, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
platform.ComputePool.type_info = (
    ('accelerator_type', unicode, False, False),
    ('accelerators_per_node', int, False, False),
    ('compute_cores_per_node', int, False, False),
    ('cpu_type', unicode, False, False),
    ('description', unicode, False, False),
    ('interconnect', unicode, False, False),
    ('memory_per_node', platform.StorageVolume, False, False),
    ('model_number', unicode, False, False),
    ('name', unicode, False, False),
    ('number_of_nodes', int, False, False),
    ('operating_system', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
platform.Machine.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
platform.Partition.type_info = (
    ('compute_pools', platform.ComputePool, True, True),
    ('description', unicode, False, False),
    ('institution', shared.Party, True, False),
    ('model_number', unicode, False, False),
    ('name', unicode, True, False),
    ('online_documentation', shared.OnlineResource, False, True),
    ('partition', platform.Partition, False, True),
    ('storage_pools', platform.StoragePool, False, True),
    ('vendor', shared.Party, False, False),
    ('when_used', shared.TimePeriod, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
platform.Performance.type_info = (
    ('asypd', float, False, False),
    ('chsy', float, False, False),
    ('compiler', unicode, False, False),
    ('coupler_load', float, False, False),
    ('io_load', float, False, False),
    ('load_imbalance', float, False, False),
    ('memory_bloat', float, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('model', science.Model, True, False),
    ('name', unicode, False, False),
    ('platform', platform.Machine, True, False),
    ('subcomponent_performance', platform.ComponentPerformance, False, False),
    ('sypd', float, False, False),
    ('total_nodes_used', int, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
platform.StoragePool.type_info = (
    ('description', unicode, False, False),
    ('name', unicode, True, False),
    ('type', unicode, False, False),
    ('vendor', shared.Party, False, False),
    ('volume_available', platform.StorageVolume, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
platform.StorageVolume.type_info = (
    ('units', unicode, True, False),
    ('volume', int, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
science.Algorithm.type_info = (
    ('diagnostic_variables', data.VariableCollection, False, False),
    ('forced_variables', data.VariableCollection, False, False),
    ('implementation_overview', unicode, True, False),
    ('prognostic_variables', data.VariableCollection, False, False),
    ('references', shared.Reference, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
science.ConservationProperties.type_info = (
    ('corrected_conserved_prognostic_variables', data.VariableCollection, False, False),
    ('correction_methodology', unicode, False, False),
    ('flux_correction_was_used', bool, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
science.Detail.type_info = (
    ('content', unicode, False, False),
    ('detail_selection', unicode, False, True),
    ('from_vocab', unicode, False, False),
    ('select', unicode, False, False),
    ('with_cardinality', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
science.Extent.type_info = (
    ('bottom_vertical_level', float, False, False),
    ('eastern_boundary', float, False, False),
    ('is_global', bool, True, False),
    ('northern_boundary', float, False, False),
    ('region_known_as', unicode, False, True),
    ('southern_boundary', float, False, False),
    ('top_vertical_level', float, False, False),
    ('western_boundary', float, False, False),
    ('z_units', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
science.Grid.type_info = (
    ('additional_details', science.Detail, False, True),
    ('grid_extent', science.Extent, False, False),
    ('horizontal_grid_layout', unicode, False, False),
    ('horizontal_grid_type', unicode, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('name', unicode, True, False),
    ('vertical_grid_layout', unicode, False, False),
    ('vertical_grid_type', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
science.KeyProperties.type_info = (
    ('additional_detail', science.Detail, False, True),
    ('extra_conservation_properties', science.ConservationProperties, False, False),
    ('grid', science.Grid, True, False),
    ('resolution', science.Resolution, True, False),
    ('time_step', float, True, False),
    ('tuning_applied', science.Tuning, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
science.Model.type_info = (
    ('category', unicode, True, False),
    ('coupled_components', science.Model, False, True),
    ('coupler', unicode, False, False),
    ('id', unicode, False, False),
    ('internal_software_components', software.SoftwareComponent, False, True),
    ('meta', shared.DocMetaInfo, True, False),
    ('model_default_properties', science.KeyProperties, False, False),
    ('simulates', science.ScientificDomain, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
science.Process.type_info = (
    ('algorithms', science.Algorithm, False, True),
    ('implementation_overview', unicode, True, False),
    ('keywords', unicode, False, False),
    ('properties', science.Detail, False, True),
    ('references', shared.Reference, False, True),
    ('sub_processes', science.SubProcess, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
science.Resolution.type_info = (
    ('equivalent_resolution_km', float, False, False),
    ('is_adaptive_grid', bool, False, False),
    ('name', unicode, True, False),
    ('number_of_levels', int, False, False),
    ('number_of_xy_gridpoints', int, False, False),
    ('typical_x_degrees', float, False, False),
    ('typical_y_degrees', float, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
science.ScienceContext.type_info = (
    ('context', unicode, True, False),
    ('id', unicode, True, False),
    ('name', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
science.ScientificDomain.type_info = (
    ('differing_key_properties', science.KeyProperties, False, False),
    ('id', unicode, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('name', unicode, True, False),
    ('overview', unicode, False, False),
    ('realm', unicode, False, False),
    ('references', shared.Reference, False, True),
    ('simulates', science.Process, True, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
science.SubProcess.type_info = (
    ('implementation_overview', unicode, True, False),
    ('properties', science.Detail, False, True),
    ('references', shared.Reference, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
science.Tuning.type_info = (
    ('description', unicode, True, False),
    ('global_mean_metrics_used', data.VariableCollection, False, False),
    ('regional_metrics_used', data.VariableCollection, False, False),
    ('trend_metrics_used', data.VariableCollection, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Calendar.type_info = (
    ('description', unicode, False, False),
    ('month_lengths', int, False, True),
    ('name', unicode, False, False),
    ('standard_name', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Cimtext.type_info = (
    ('content', unicode, True, False),
    ('content_type', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.DateTime.type_info = (
    ('offset', bool, False, False),
    ('value', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.DatetimeSet.type_info = (
    ('length', int, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.DocMetaInfo.type_info = (
    ('author', shared.Party, False, False),
    ('create_date', datetime.datetime, True, False),
    ('drs_keys', unicode, False, True),
    ('drs_path', unicode, False, False),
    ('external_ids', unicode, False, True),
    ('id', unicode, True, False),
    ('institute', unicode, False, False),
    ('language', unicode, True, False),
    ('project', unicode, True, False),
    ('sort_key', unicode, False, False),
    ('source', unicode, True, False),
    ('source_key', unicode, False, False),
    ('type', unicode, True, False),
    ('type_display_name', unicode, False, False),
    ('type_sort_key', unicode, False, False),
    ('update_date', datetime.datetime, True, False),
    ('version', int, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.DocReference.type_info = (
    ('constraint_vocabulary', unicode, False, False),
    ('context', unicode, False, False),
    ('id', unicode, False, False),
    ('relationship', unicode, False, False),
    ('type', unicode, True, False),
    ('version', int, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.ExternalDocument.type_info = (
    ('authorship', unicode, False, False),
    ('date', unicode, False, False),
    ('doi', unicode, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('name', unicode, True, False),
    ('online_at', shared.OnlineResource, False, False),
    ('publication_detail', unicode, False, False),
    ('title', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.IrregularDateset.type_info = (
    ('date_set', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.KeyFloat.type_info = (
    ('key', unicode, True, False),
    ('value', float, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.NumberArray.type_info = (
    ('values', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.OnlineResource.type_info = (
    ('description', unicode, False, False),
    ('linkage', unicode, True, False),
    ('name', unicode, True, False),
    ('protocol', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Party.type_info = (
    ('address', unicode, False, False),
    ('email', unicode, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('name', unicode, False, False),
    ('orcid_id', unicode, False, False),
    ('organisation', bool, False, False),
    ('url', shared.OnlineResource, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Pid.type_info = (
    ('id', unicode, True, False),
    ('resolution_service', shared.OnlineResource, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.QualityReview.type_info = (
    ('date', unicode, True, False),
    ('metadata_reviewer', shared.Party, True, False),
    ('quality_description', unicode, True, False),
    ('quality_status', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Reference.type_info = (
    ('context', unicode, False, False),
    ('document', shared.ExternalDocument, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.RegularTimeset.type_info = (
    ('increment', shared.TimePeriod, True, False),
    ('length', int, True, False),
    ('start_date', shared.DateTime, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Responsibility.type_info = (
    ('party', shared.Party, True, True),
    ('role', unicode, True, False),
    ('when', shared.TimePeriod, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.TimePeriod.type_info = (
    ('calendar', shared.Calendar, False, False),
    ('date', shared.DateTime, False, False),
    ('date_type', unicode, True, False),
    ('length', int, True, False),
    ('units', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.TimesliceList.type_info = (
    ('members', shared.NumberArray, True, False),
    ('units', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.ComponentBase.type_info = (
    ('description', unicode, False, False),
    ('development_history', software.DevelopmentPath, False, False),
    ('documentation', shared.Reference, False, True),
    ('long_name', unicode, False, False),
    ('name', unicode, True, False),
    ('release_date', datetime.datetime, False, False),
    ('repository', shared.OnlineResource, False, False),
    ('version', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.Composition.type_info = (
    ('couplings', unicode, False, True),
    ('description', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.DevelopmentPath.type_info = (
    ('consortium_name', unicode, False, False),
    ('creators', shared.Responsibility, False, True),
    ('developed_in_house', bool, True, False),
    ('funding_sources', shared.Responsibility, False, True),
    ('previous_version', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.EntryPoint.type_info = (
    ('name', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.Gridspec.type_info = (
    ('description', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.SoftwareComponent.type_info = (
    ('composition', software.Composition, False, False),
    ('connection_points', software.Variable, False, True),
    ('coupling_framework', unicode, False, False),
    ('dependencies', software.EntryPoint, False, True),
    ('grid', software.Gridspec, False, False),
    ('language', unicode, False, False),
    ('license', unicode, False, False),
    ('sub_components', software.SoftwareComponent, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.Variable.type_info = (
    ('description', unicode, False, False),
    ('name', unicode, True, False),
    ('prognostic', bool, True, False),
)


