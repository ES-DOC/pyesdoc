# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_meta.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encpasulates meta-information pertaining to the cim.v2 typeset.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

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
data.RelatedData.type_key = u'cim.2.data.RelatedData'
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
science.Extent.type_key = u'cim.2.science.Extent'
science.GridSummary.type_key = u'cim.2.science.GridSummary'
science.Model.type_key = u'cim.2.science.Model'
science.Process.type_key = u'cim.2.science.Process'
science.ProcessDetail.type_key = u'cim.2.science.ProcessDetail'
science.Resolution.type_key = u'cim.2.science.Resolution'
science.ScientificDomain.type_key = u'cim.2.science.ScientificDomain'
science.SubProcess.type_key = u'cim.2.science.SubProcess'
science.Tuning.type_key = u'cim.2.science.Tuning'
shared.Calendar.type_key = u'cim.2.shared.Calendar'
shared.CimLink.type_key = u'cim.2.shared.CimLink'
shared.Cimtext.type_key = u'cim.2.shared.Cimtext'
shared.Citation.type_key = u'cim.2.shared.Citation'
shared.DateTime.type_key = u'cim.2.shared.DateTime'
shared.DatetimeSet.type_key = u'cim.2.shared.DatetimeSet'
shared.DocMetaInfo.type_key = u'cim.2.shared.DocMetaInfo'
shared.DocReference.type_key = u'cim.2.shared.DocReference'
shared.IrregularDateset.type_key = u'cim.2.shared.IrregularDateset'
shared.KeyFloat.type_key = u'cim.2.shared.KeyFloat'
shared.NumberArray.type_key = u'cim.2.shared.NumberArray'
shared.OnlineResource.type_key = u'cim.2.shared.OnlineResource'
shared.Party.type_key = u'cim.2.shared.Party'
shared.Pid.type_key = u'cim.2.shared.Pid'
shared.Reference.type_key = u'cim.2.shared.Reference'
shared.RegularTimeset.type_key = u'cim.2.shared.RegularTimeset'
shared.Responsibility.type_key = u'cim.2.shared.Responsibility'
shared.StandaloneDocument.type_key = u'cim.2.shared.StandaloneDocument'
shared.TimePeriod.type_key = u'cim.2.shared.TimePeriod'
shared.TimesliceList.type_key = u'cim.2.shared.TimesliceList'
shared.VocabMember.type_key = u'cim.2.shared.VocabMember'
software.ComponentBase.type_key = u'cim.2.software.ComponentBase'
software.Composition.type_key = u'cim.2.software.Composition'
software.DevelopmentPath.type_key = u'cim.2.software.DevelopmentPath'
software.EntryPoint.type_key = u'cim.2.software.EntryPoint'
software.Gridspec.type_key = u'cim.2.software.Gridspec'
software.SoftwareComponent.type_key = u'cim.2.software.SoftwareComponent'
software.Variable.type_key = u'cim.2.software.Variable'


# Set type info (name, type, is_required, is_iterative).
activity.Activity.type_info = (
    ('canonical_name', unicode, False, False),
    ('description', unicode, False, False),
    ('duration', shared.TimePeriod, False, False),
    ('keywords', unicode, False, True),
    ('long_name', unicode, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('name', unicode, True, False),
    ('rationale', unicode, False, False),
    ('references', shared.Citation, False, True),
    ('responsible_parties', shared.Responsibility, False, True),
)

activity.AxisMember.type_info = (
    ('description', unicode, True, False),
    ('index', int, True, False),
    ('value', float, False, False),
)

activity.Conformance.type_info = (
    ('target_requirement', designing.NumericalRequirement, True, False),
    ('target_requirement_reference', shared.DocReference, True, False),
)

activity.Ensemble.type_info = (
    ('common_conformances', activity.Conformance, False, True),
    ('common_conformances_references', shared.DocReference, False, True),
    ('has_ensemble_axes', activity.EnsembleAxis, False, True),
    ('members', activity.EnsembleMember, True, True),
    ('part_of', activity.UberEnsemble, False, True),
    ('supported', designing.NumericalExperiment, True, True),
    ('supported_references', shared.DocReference, True, True),
)

activity.EnsembleAxis.type_info = (
    ('extra_detail', unicode, True, False),
    ('member', activity.AxisMember, True, True),
    ('short_identifier', unicode, True, False),
    ('target_requirement', designing.NumericalRequirement, True, False),
    ('target_requirement_reference', shared.DocReference, True, False),
)

activity.EnsembleMember.type_info = (
    ('had_performance', platform.Performance, False, False),
    ('had_performance_reference', shared.DocReference, False, False),
    ('ran_on', platform.Machine, True, False),
    ('ran_on_reference', shared.DocReference, True, False),
    ('simulation', data.Simulation, True, False),
    ('simulation_reference', shared.DocReference, True, False),
)

activity.ParentSimulation.type_info = (
    ('branch_time_in_child', shared.DateTime, False, False),
    ('branch_time_in_parent', shared.DateTime, False, False),
    ('parent', data.Simulation, True, False),
    ('parent_reference', shared.DocReference, True, False),
)

activity.UberEnsemble.type_info = (
    ('child_ensembles', activity.Ensemble, True, True),
    ('child_ensembles_references', shared.DocReference, True, True),
)

data.Dataset.type_info = (
    ('availability', shared.OnlineResource, False, True),
    ('description', unicode, False, False),
    ('drs_datasets', drs.DrsPublicationDataset, False, True),
    ('meta', shared.DocMetaInfo, True, False),
    ('name', unicode, True, False),
    ('produced_by', data.Simulation, False, False),
    ('produced_by_reference', shared.DocReference, False, False),
    ('references', shared.Citation, False, True),
    ('related_to_dataset', data.RelatedData, False, True),
    ('responsible_parties', shared.Responsibility, False, True),
    ('responsible_parties_references', shared.DocReference, False, True),
)

data.Downscaling.type_info = (
    ('downscaled_from', data.Simulation, True, False),
    ('downscaled_from_reference', shared.DocReference, True, False),
)

data.RelatedData.type_info = (
    ('other_dataset', data.Dataset, True, False),
    ('other_dataset_reference', shared.DocReference, True, False),
    ('relationship', unicode, True, False),
)

data.Simulation.type_info = (
    ('calendar', shared.Calendar, False, False),
    ('ensemble_identifier', unicode, True, False),
    ('parent_simulation', activity.ParentSimulation, False, False),
    ('part_of_project', designing.Project, True, True),
    ('part_of_project_references', shared.DocReference, True, True),
    ('primary_ensemble', activity.Ensemble, False, False),
    ('primary_ensemble_reference', shared.DocReference, False, False),
    ('ran_for_experiments', designing.NumericalExperiment, True, True),
    ('ran_for_experiments_references', shared.DocReference, True, True),
    ('used', science.Model, True, False),
    ('used_reference', shared.DocReference, True, False),
)

data.VariableCollection.type_info = (
    ('collection_name', unicode, False, False),
    ('variables', unicode, True, True),
)

designing.DomainProperties.type_info = (
    ('required_extent', science.Extent, False, False),
    ('required_resolution', science.Resolution, False, False),
)

designing.EnsembleRequirement.type_info = (
    ('ensemble_member', designing.NumericalRequirement, False, True),
    ('ensemble_member_references', shared.DocReference, False, True),
    ('ensemble_type', unicode, True, False),
    ('minimum_size', int, True, False),
)

designing.ForcingConstraint.type_info = (
    ('additional_constraint', unicode, False, False),
    ('category', shared.VocabMember, True, False),
    ('code', shared.VocabMember, True, False),
    ('data_link', shared.OnlineResource, False, False),
    ('forcing_type', unicode, True, False),
    ('group', shared.VocabMember, False, False),
    ('origin', shared.Citation, False, False),
)

designing.MultiEnsemble.type_info = (
    ('ensemble_axis', designing.EnsembleRequirement, True, True),
    ('ensemble_axis_references', shared.DocReference, True, True),
)

designing.MultiTimeEnsemble.type_info = (
    ('ensemble_members', shared.DatetimeSet, True, False),
)

designing.NumericalExperiment.type_info = (
    ('related_experiments', designing.NumericalExperiment, False, True),
    ('related_experiments_references', shared.DocReference, False, True),
    ('requirements', designing.NumericalRequirement, False, True),
    ('requirements_references', shared.DocReference, False, True),
)

designing.NumericalRequirement.type_info = (
    ('additional_requirements', designing.NumericalRequirement, False, True),
    ('additional_requirements_references', shared.DocReference, False, True),
    ('conformance_is_requested', bool, True, False),
)

designing.OutputTemporalRequirement.type_info = (
    ('continuous_subset', shared.TimePeriod, False, True),
    ('sliced_subset', shared.TimesliceList, False, False),
    ('throughout', bool, True, False),
)

designing.Project.type_info = (
    ('previous_projects', designing.Project, False, True),
    ('previous_projects_references', shared.DocReference, False, True),
    ('requires_experiments', designing.NumericalExperiment, False, True),
    ('requires_experiments_references', shared.DocReference, False, True),
    ('sub_projects', designing.Project, False, True),
    ('sub_projects_references', shared.DocReference, False, True),
)

designing.SimulationPlan.type_info = (
    ('expected_model', science.Model, True, False),
    ('expected_model_reference', shared.DocReference, True, False),
    ('expected_performance_sypd', float, False, False),
    ('expected_platform', platform.Machine, False, False),
    ('expected_platform_reference', shared.DocReference, False, False),
    ('will_support_experiments', designing.NumericalExperiment, True, True),
    ('will_support_experiments_references', shared.DocReference, True, True),
)

designing.TemporalConstraint.type_info = (
    ('required_calendar', shared.Calendar, False, False),
    ('required_duration', shared.TimePeriod, False, False),
    ('start_date', shared.DateTime, False, False),
    ('start_flexibility', shared.TimePeriod, False, False),
)

drs.DrsAtomicDataset.type_info = (
    ('ensemble_member', drs.DrsEnsembleIdentifier, True, False),
    ('geographical_constraint', drs.DrsGeographicalIndicator, False, False),
    ('mip_table', unicode, True, False),
    ('temporal_constraint', drs.DrsTemporalIdentifier, False, False),
    ('variable_name', unicode, True, False),
)

drs.DrsEnsembleIdentifier.type_info = (
    ('initialisation_method_number', int, True, False),
    ('perturbation_number', int, True, False),
    ('realisation_number', int, True, False),
)

drs.DrsGeographicalIndicator.type_info = (
    ('bounding_box', unicode, False, False),
    ('operator', unicode, False, False),
    ('spatial_domain', unicode, False, False),
)

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

drs.DrsTemporalIdentifier.type_info = (
    ('end', unicode, False, False),
    ('start', unicode, True, False),
    ('suffix', unicode, False, False),
)

platform.ComponentPerformance.type_info = (
    ('component', software.SoftwareComponent, False, False),
    ('component_name', unicode, True, False),
    ('cores_used', int, False, False),
    ('nodes_used', int, False, False),
    ('speed', float, True, False),
)

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

platform.Machine.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
)

platform.Partition.type_info = (
    ('compute_pools', platform.ComputePool, True, True),
    ('description', unicode, False, False),
    ('institution', shared.Party, True, False),
    ('institution_reference', shared.DocReference, True, False),
    ('model_number', unicode, False, False),
    ('name', unicode, True, False),
    ('online_documentation', shared.OnlineResource, False, True),
    ('partition', platform.Partition, False, True),
    ('storage_pools', platform.StoragePool, False, True),
    ('vendor', shared.Party, False, False),
    ('vendor_reference', shared.DocReference, False, False),
    ('when_used', shared.TimePeriod, False, False),
)

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
    ('model_reference', shared.DocReference, True, False),
    ('name', unicode, False, False),
    ('platform', platform.Machine, True, False),
    ('platform_reference', shared.DocReference, True, False),
    ('subcomponent_performance', platform.ComponentPerformance, False, False),
    ('sypd', float, False, False),
    ('total_nodes_used', int, False, False),
)

platform.StoragePool.type_info = (
    ('description', unicode, False, False),
    ('name', unicode, True, False),
    ('type', unicode, False, False),
    ('vendor', shared.Party, False, False),
    ('vendor_reference', shared.DocReference, False, False),
    ('volume_available', platform.StorageVolume, True, False),
)

platform.StorageVolume.type_info = (
    ('units', unicode, True, False),
    ('volume', int, True, False),
)

science.Algorithm.type_info = (
    ('diagnostic_variables', data.VariableCollection, False, True),
    ('heading', unicode, True, False),
    ('implementation_overview', unicode, True, False),
    ('prognostic_variables', data.VariableCollection, False, True),
    ('references', shared.Citation, False, True),
)

science.ConservationProperties.type_info = (
    ('corrected_conserved_prognostic_variables', data.VariableCollection, False, False),
    ('correction_methodology', unicode, False, False),
    ('flux_correction_was_used', bool, True, False),
)

science.Extent.type_info = (
    ('eastern_boundary', float, False, False),
    ('is_global', bool, True, False),
    ('maximum_vertical_level', float, False, False),
    ('minimum_vertical_level', float, False, False),
    ('northern_boundary', float, False, False),
    ('region_known_as', unicode, False, True),
    ('southern_boundary', float, False, False),
    ('western_boundary', float, False, False),
    ('z_units', unicode, True, False),
)

science.GridSummary.type_info = (
    ('grid_extent', science.Extent, True, False),
    ('grid_layout', unicode, True, False),
    ('grid_type', unicode, True, False),
)

science.Model.type_info = (
    ('category', unicode, True, False),
    ('coupled_software_components', science.Model, False, True),
    ('coupled_software_components_references', shared.DocReference, False, True),
    ('coupler', unicode, False, False),
    ('extra_conservation_properties', science.ConservationProperties, False, False),
    ('internal_software_components', software.SoftwareComponent, False, True),
    ('meta', shared.DocMetaInfo, True, False),
    ('scientific_domain', science.ScientificDomain, False, True),
    ('scientific_domain_references', shared.DocReference, False, True),
)

science.Process.type_info = (
    ('algorithms', science.Algorithm, False, True),
    ('description', unicode, False, False),
    ('implementation_overview', unicode, True, False),
    ('keywords', unicode, True, False),
    ('name', unicode, True, False),
    ('properties', science.ProcessDetail, False, True),
    ('references', shared.Reference, False, True),
    ('sub_processes', science.SubProcess, False, True),
    ('time_step_in_process', float, False, False),
)

science.ProcessDetail.type_info = (
    ('content', unicode, False, False),
    ('detail_selection', unicode, False, True),
    ('detail_vocabulary', unicode, False, False),
    ('heading', unicode, False, False),
    ('numeric_properties', shared.KeyFloat, False, True),
)

science.Resolution.type_info = (
    ('equivalent_horizontal_resolution', float, True, False),
    ('is_adaptive_grid', bool, False, False),
    ('name', unicode, True, False),
    ('number_of_levels', int, False, True),
    ('number_of_xy_gridpoints', int, False, True),
)

science.ScientificDomain.type_info = (
    ('extra_conservation_properties', science.ConservationProperties, False, False),
    ('grid', science.GridSummary, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('name', unicode, True, False),
    ('overview', unicode, False, False),
    ('realm', unicode, False, False),
    ('references', shared.Reference, False, True),
    ('resolution', science.Resolution, True, False),
    ('simulates', science.Process, True, True),
    ('time_step', float, True, False),
    ('tuning_applied', science.Tuning, False, False),
)

science.SubProcess.type_info = (
    ('description', unicode, False, False),
    ('implementation_overview', unicode, False, False),
    ('keywords', unicode, False, False),
    ('name', unicode, True, False),
    ('properties', science.ProcessDetail, False, True),
    ('references', shared.Reference, False, True),
)

science.Tuning.type_info = (
    ('description', unicode, True, False),
    ('global_mean_metrics_used', data.VariableCollection, False, False),
    ('regional_metrics_used', data.VariableCollection, False, False),
    ('trend_metrics_used', data.VariableCollection, False, False),
)

shared.Calendar.type_info = (
    ('description', unicode, False, False),
    ('month_lengths', int, False, True),
    ('name', unicode, False, False),
    ('standard_name', unicode, True, False),
)

shared.CimLink.type_info = (
    ('remote_type', unicode, True, False),
)

shared.Cimtext.type_info = (
    ('content', unicode, True, False),
    ('content_type', unicode, True, False),
)

shared.Citation.type_info = (
    ('abstract', unicode, False, False),
    ('citation_str', unicode, True, False),
    ('context', unicode, False, False),
    ('doi', unicode, False, False),
    ('short_cite', unicode, False, False),
    ('title', unicode, False, False),
    ('url', shared.OnlineResource, False, False),
)

shared.DateTime.type_info = (
    ('offset', bool, False, False),
    ('value', unicode, True, False),
)

shared.DatetimeSet.type_info = (
    ('length', int, True, False),
)

shared.DocMetaInfo.type_info = (
    ('author', shared.Party, False, False),
    ('author_reference', shared.DocReference, False, False),
    ('create_date', datetime.datetime, True, False),
    ('drs_keys', unicode, False, True),
    ('drs_path', unicode, False, False),
    ('external_ids', unicode, False, True),
    ('id', uuid.UUID, True, False),
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

shared.DocReference.type_info = (
    ('description', unicode, False, False),
    ('id', uuid.UUID, False, False),
    ('name', unicode, False, False),
    ('type', unicode, False, False),
    ('url', unicode, False, False),
    ('version', int, False, False),
)

shared.IrregularDateset.type_info = (
    ('date_set', unicode, True, False),
)

shared.KeyFloat.type_info = (
    ('key', unicode, True, False),
    ('value', float, True, False),
)

shared.NumberArray.type_info = (
    ('values', unicode, True, False),
)

shared.OnlineResource.type_info = (
    ('description', unicode, False, False),
    ('linkage', unicode, True, False),
    ('name', unicode, True, False),
    ('protocol', unicode, False, False),
)

shared.Party.type_info = (
    ('address', unicode, False, False),
    ('email', unicode, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('name', unicode, False, False),
    ('organisation', bool, False, False),
    ('url', shared.OnlineResource, False, False),
)

shared.Pid.type_info = (
    ('id', unicode, True, False),
    ('resolution_service', shared.OnlineResource, True, False),
)

shared.Reference.type_info = (
)

shared.RegularTimeset.type_info = (
    ('increment', shared.TimePeriod, True, False),
    ('length', int, True, False),
    ('start_date', shared.DateTime, True, False),
)

shared.Responsibility.type_info = (
    ('party', shared.Party, True, True),
    ('party_references', shared.DocReference, True, True),
    ('role', unicode, True, False),
    ('when', shared.TimePeriod, False, False),
)

shared.StandaloneDocument.type_info = (
    ('long_name', unicode, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('name', unicode, True, False),
    ('references', shared.Citation, False, True),
    ('responsible_parties', shared.Responsibility, False, True),
)

shared.TimePeriod.type_info = (
    ('calendar', shared.Calendar, False, False),
    ('date', shared.DateTime, False, False),
    ('date_type', unicode, True, False),
    ('length', int, True, False),
    ('units', unicode, True, False),
)

shared.TimesliceList.type_info = (
    ('members', shared.NumberArray, True, False),
    ('units', unicode, True, False),
)

shared.VocabMember.type_info = (
    ('uri', unicode, False, False),
    ('value', unicode, True, False),
    ('vocab', shared.Citation, False, False),
)

software.ComponentBase.type_info = (
    ('description', unicode, False, False),
    ('development_history', software.DevelopmentPath, False, False),
    ('documentation', shared.Citation, False, True),
    ('long_name', unicode, False, False),
    ('name', unicode, True, False),
    ('release_date', datetime.datetime, False, False),
    ('repository', shared.OnlineResource, False, False),
    ('version', unicode, False, False),
)

software.Composition.type_info = (
    ('couplings', unicode, False, True),
    ('description', unicode, False, False),
)

software.DevelopmentPath.type_info = (
    ('consortium_name', unicode, False, False),
    ('creators', shared.Responsibility, False, True),
    ('developed_in_house', bool, True, False),
    ('funding_sources', shared.Responsibility, False, True),
    ('previous_version', unicode, False, False),
)

software.EntryPoint.type_info = (
    ('name', unicode, False, False),
)

software.Gridspec.type_info = (
    ('description', unicode, True, False),
)

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

software.Variable.type_info = (
    ('description', unicode, False, False),
    ('name', unicode, True, False),
    ('prognostic', bool, True, False),
)

