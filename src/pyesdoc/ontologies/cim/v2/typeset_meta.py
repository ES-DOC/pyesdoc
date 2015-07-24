# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_meta.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encpasulates meta-information pertaining to the cim.v2 typeset.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
import datetime
import uuid

import typeset_for_data_package as data
import typeset_for_platform_package as platform
import typeset_for_drs_package as drs
import typeset_for_shared_package as shared
import typeset_for_software_package as software
import typeset_for_science_package as science
import typeset_for_activity_package as activity




# Set type keys.
activity.EnsembleRequirement.type_key = 'cim.2.activity.EnsembleRequirement'
activity.ForcingConstraint.type_key = 'cim.2.activity.ForcingConstraint'
science.Tuning.type_key = 'cim.2.science.Tuning'
activity.ParentSimulation.type_key = 'cim.2.activity.ParentSimulation'
shared.KeyFloat.type_key = 'cim.2.shared.KeyFloat'
activity.DomainProperties.type_key = 'cim.2.activity.DomainProperties'
shared.TimesliceList.type_key = 'cim.2.shared.TimesliceList'
shared.CimLink.type_key = 'cim.2.shared.CimLink'
shared.Reference.type_key = 'cim.2.shared.Reference'
activity.EnsembleAxis.type_key = 'cim.2.activity.EnsembleAxis'
shared.VocabMember.type_key = 'cim.2.shared.VocabMember'
software.EntryPoint.type_key = 'cim.2.software.EntryPoint'
shared.Cimtext.type_key = 'cim.2.shared.Cimtext'
shared.OnlineResource.type_key = 'cim.2.shared.OnlineResource'
shared.Meta.type_key = 'cim.2.shared.Meta'
activity.EnsembleMember.type_key = 'cim.2.activity.EnsembleMember'
drs.DrsPublicationDataset.type_key = 'cim.2.drs.DrsPublicationDataset'
shared.MinimalMeta.type_key = 'cim.2.shared.MinimalMeta'
software.ComponentBase.type_key = 'cim.2.software.ComponentBase'
activity.Downscaling.type_key = 'cim.2.activity.Downscaling'
software.Composition.type_key = 'cim.2.software.Composition'
activity.SimulationPlan.type_key = 'cim.2.activity.SimulationPlan'
data.VariableCollection.type_key = 'cim.2.data.VariableCollection'
drs.DrsEnsembleIdentifier.type_key = 'cim.2.drs.DrsEnsembleIdentifier'
activity.Activity.type_key = 'cim.2.activity.Activity'
shared.TimePeriod.type_key = 'cim.2.shared.TimePeriod'
activity.NumericalExperiment.type_key = 'cim.2.activity.NumericalExperiment'
platform.Machine.type_key = 'cim.2.platform.Machine'
activity.UberEnsemble.type_key = 'cim.2.activity.UberEnsemble'
shared.IrregularDateset.type_key = 'cim.2.shared.IrregularDateset'
data.RelatedData.type_key = 'cim.2.data.RelatedData'
shared.Responsibility.type_key = 'cim.2.shared.Responsibility'
science.ConservationProperties.type_key = 'cim.2.science.ConservationProperties'
science.Resolution.type_key = 'cim.2.science.Resolution'
activity.Ensemble.type_key = 'cim.2.activity.Ensemble'
platform.ComputePool.type_key = 'cim.2.platform.ComputePool'
activity.Project.type_key = 'cim.2.activity.Project'
shared.StandaloneDocument.type_key = 'cim.2.shared.StandaloneDocument'
shared.Citation.type_key = 'cim.2.shared.Citation'
platform.ComponentPerformance.type_key = 'cim.2.platform.ComponentPerformance'
activity.AxisMember.type_key = 'cim.2.activity.AxisMember'
activity.MultiEnsemble.type_key = 'cim.2.activity.MultiEnsemble'
platform.StorageVolume.type_key = 'cim.2.platform.StorageVolume'
shared.NumberArray.type_key = 'cim.2.shared.NumberArray'
platform.StoragePool.type_key = 'cim.2.platform.StoragePool'
science.Extent.type_key = 'cim.2.science.Extent'
drs.DrsTemporalIdentifier.type_key = 'cim.2.drs.DrsTemporalIdentifier'
platform.Performance.type_key = 'cim.2.platform.Performance'
shared.Calendar.type_key = 'cim.2.shared.Calendar'
software.DevelopmentPath.type_key = 'cim.2.software.DevelopmentPath'
activity.OutputTemporalRequirement.type_key = 'cim.2.activity.OutputTemporalRequirement'
shared.Party.type_key = 'cim.2.shared.Party'
activity.Simulation.type_key = 'cim.2.activity.Simulation'
software.Gridspec.type_key = 'cim.2.software.Gridspec'
science.GridSummary.type_key = 'cim.2.science.GridSummary'
platform.Partition.type_key = 'cim.2.platform.Partition'
software.Model.type_key = 'cim.2.software.Model'
science.ScientificDomain.type_key = 'cim.2.science.ScientificDomain'
software.Variable.type_key = 'cim.2.software.Variable'
activity.MultiTimeEnsemble.type_key = 'cim.2.activity.MultiTimeEnsemble'
shared.Pid.type_key = 'cim.2.shared.Pid'
activity.Conformance.type_key = 'cim.2.activity.Conformance'
activity.TemporalConstraint.type_key = 'cim.2.activity.TemporalConstraint'
science.Algorithm.type_key = 'cim.2.science.Algorithm'
shared.DatetimeSet.type_key = 'cim.2.shared.DatetimeSet'
shared.DateTime.type_key = 'cim.2.shared.DateTime'
software.SoftwareComponent.type_key = 'cim.2.software.SoftwareComponent'
science.ProcessDetail.type_key = 'cim.2.science.ProcessDetail'
drs.DrsGeographicalIndicator.type_key = 'cim.2.drs.DrsGeographicalIndicator'
activity.NumericalRequirement.type_key = 'cim.2.activity.NumericalRequirement'
drs.DrsAtomicDataset.type_key = 'cim.2.drs.DrsAtomicDataset'
shared.RegularTimeset.type_key = 'cim.2.shared.RegularTimeset'
science.Process.type_key = 'cim.2.science.Process'
data.Dataset.type_key = 'cim.2.data.Dataset'


# Set type info (name, type, is_required, is_iterative).
activity.EnsembleRequirement.type_info = (
    ('minimum_size', int, True, False),
    ('ensemble_member', activity.NumericalRequirement, False, True),
    ('ensemble_type', str, True, False),
)

activity.ForcingConstraint.type_info = (
    ('forcing_type', str, True, False),
    ('data_link', shared.OnlineResource, False, False),
    ('origin', shared.Citation, False, False),
    ('additional_constraint', shared.Cimtext, False, False),
    ('category', shared.VocabMember, True, False),
    ('code', shared.VocabMember, True, False),
    ('group', shared.VocabMember, False, False),
)

science.Tuning.type_info = (
    ('regional_metrics_used', data.VariableCollection, False, False),
    ('trend_metrics_used', data.VariableCollection, False, False),
    ('description', shared.Cimtext, True, False),
    ('global_mean_metrics_used', data.VariableCollection, False, False),
)

activity.ParentSimulation.type_info = (
    ('branch_time_in_child', shared.DateTime, False, False),
    ('parent', activity.Simulation, True, False),
    ('branch_time_in_parent', shared.DateTime, False, False),
)

shared.KeyFloat.type_info = (
    ('value', float, True, False),
    ('key', str, True, False),
)

activity.DomainProperties.type_info = (
    ('required_extent', science.Extent, False, False),
    ('required_resolution', science.Resolution, False, False),
)

shared.TimesliceList.type_info = (
    ('members', shared.NumberArray, True, False),
    ('units', str, True, False),
)

shared.CimLink.type_info = (
    ('remote_type', str, True, False),
)

shared.Reference.type_info = (
)

activity.EnsembleAxis.type_info = (
    ('extra_detail', shared.Cimtext, True, False),
    ('short_identifier', str, True, False),
    ('target_requirement', activity.NumericalRequirement, True, False),
    ('member', activity.AxisMember, True, True),
)

shared.VocabMember.type_info = (
    ('uri', str, False, False),
    ('vocab', shared.Citation, False, False),
    ('value', str, True, False),
)

software.EntryPoint.type_info = (
    ('name', str, False, False),
)

shared.Cimtext.type_info = (
    ('content', str, True, False),
    ('content_type', str, True, False),
)

shared.OnlineResource.type_info = (
    ('protocol', str, False, False),
    ('description', str, False, False),
    ('name', str, True, False),
    ('linkage', str, True, False),
)

shared.Meta.type_info = (
    ('metadata_author', shared.Party, True, False),
    ('metadata_quality', str, False, False),
    ('metadata_reviewer', shared.Party, False, False),
    ('metadata_completeness', str, False, False),
)

activity.EnsembleMember.type_info = (
    ('had_performance', platform.Performance, False, False),
    ('simulation', activity.Simulation, True, False),
    ('ran_on', platform.Machine, True, False),
)

drs.DrsPublicationDataset.type_info = (
    ('model', str, True, False),
    ('version_number', int, False, False),
    ('frequency', str, False, False),
    ('activity', str, True, False),
    ('product', str, True, False),
    ('realm', str, False, False),
    ('experiment', str, True, False),
    ('institute', str, True, False),
)

shared.MinimalMeta.type_info = (
    ('uid', str, True, False),
    ('document_version', int, False, False),
    ('metadata_last_updated', datetime.datetime, True, False),
)

software.ComponentBase.type_info = (
    ('version', str, False, False),
    ('development_history', software.DevelopmentPath, False, False),
    ('release_date', datetime.datetime, False, False),
    ('documentation', shared.Citation, False, True),
    ('tuning_applied', science.Tuning, False, False),
    ('name', str, True, False),
    ('long_name', str, False, False),
    ('description', shared.Cimtext, False, False),
)

activity.Downscaling.type_info = (
    ('downscaled_from', activity.Simulation, True, False),
)

software.Composition.type_info = (
    ('couplings', str, False, True),
    ('description', str, False, False),
)

activity.SimulationPlan.type_info = (
    ('will_support_experiments', activity.NumericalExperiment, True, True),
    ('expected_platform', platform.Machine, False, False),
    ('expected_model', software.Model, True, False),
    ('expected_performance_sypd', float, False, False),
)

data.VariableCollection.type_info = (
    ('collection_name', str, False, False),
    ('variables', str, True, True),
)

drs.DrsEnsembleIdentifier.type_info = (
    ('realisation_number', int, True, False),
    ('initialisation_method_number', int, True, False),
    ('perturbation_number', int, True, False),
)

activity.Activity.type_info = (
    ('canonical_name', str, False, False),
    ('name', str, True, False),
    ('keywords', str, False, True),
    ('rationale', shared.Cimtext, False, False),
    ('responsible_parties', shared.Responsibility, False, True),
    ('meta', shared.Meta, True, False),
    ('duration', shared.TimePeriod, False, False),
    ('long_name', str, False, False),
    ('description', shared.Cimtext, False, False),
    ('references', shared.Citation, False, True),
)

shared.TimePeriod.type_info = (
    ('calendar', shared.Calendar, False, False),
    ('units', str, True, False),
    ('length', int, True, False),
    ('date_type', str, True, False),
    ('date', shared.DateTime, False, False),
)

activity.NumericalExperiment.type_info = (
    ('related_experiments', activity.NumericalExperiment, False, True),
    ('requirements', activity.NumericalRequirement, False, True),
)

platform.Machine.type_info = (
    ('meta', shared.Meta, True, False),
)

activity.UberEnsemble.type_info = (
    ('child_ensembles', activity.Ensemble, True, True),
)

shared.IrregularDateset.type_info = (
    ('date_set', str, True, False),
)

data.RelatedData.type_info = (
    ('relationship', str, True, False),
    ('other_dataset', data.Dataset, True, False),
)

shared.Responsibility.type_info = (
    ('when', shared.TimePeriod, False, False),
    ('party', shared.Party, True, True),
    ('role', str, True, False),
)

science.ConservationProperties.type_info = (
    ('flux_correction_was_used', bool, True, False),
    ('corrected_conserved_prognostic_variables', data.VariableCollection, False, False),
    ('correction_methodology', shared.Cimtext, False, False),
)

science.Resolution.type_info = (
    ('equivalent_horizontal_resolution', float, True, False),
    ('number_of_levels', int, False, True),
    ('name', str, True, False),
    ('number_of_xy_gridpoints', int, False, True),
    ('is_adaptive_grid', bool, False, False),
)

activity.Ensemble.type_info = (
    ('part_of', activity.UberEnsemble, False, True),
    ('members', activity.EnsembleMember, True, True),
    ('common_conformances', activity.Conformance, False, True),
    ('supported', activity.NumericalExperiment, True, True),
    ('has_ensemble_axes', activity.EnsembleAxis, False, True),
)

platform.ComputePool.type_info = (
    ('number_of_nodes', int, False, False),
    ('model_number', str, False, False),
    ('accelerators_per_node', int, False, False),
    ('memory_per_node', platform.StorageVolume, False, False),
    ('compute_cores_per_node', int, False, False),
    ('description', shared.Cimtext, False, False),
    ('operating_system', str, False, False),
    ('accelerator_type', str, False, False),
    ('interconnect', str, False, False),
    ('cpu_type', str, False, False),
    ('name', str, False, False),
)

activity.Project.type_info = (
    ('previous_projects', activity.Project, False, True),
    ('sub_projects', activity.Project, False, True),
    ('requires_experiments', activity.NumericalExperiment, False, True),
)

shared.StandaloneDocument.type_info = (
    ('references', shared.Citation, False, True),
    ('responsible_parties', shared.Responsibility, False, True),
    ('name', str, True, False),
    ('long_name', str, False, False),
    ('meta', shared.Meta, True, False),
)

shared.Citation.type_info = (
    ('citation_str', shared.Cimtext, True, False),
    ('title', str, False, False),
    ('url', shared.OnlineResource, False, False),
    ('abstract', str, False, False),
    ('doi', str, False, False),
    ('context', shared.Cimtext, False, False),
)

platform.ComponentPerformance.type_info = (
    ('cores_used', int, False, False),
    ('speed', float, True, False),
    ('component', software.SoftwareComponent, False, False),
    ('nodes_used', int, False, False),
    ('component_name', str, True, False),
)

activity.AxisMember.type_info = (
    ('value', float, False, False),
    ('description', str, True, False),
    ('index', int, True, False),
)

activity.MultiEnsemble.type_info = (
    ('ensemble_axis', activity.EnsembleRequirement, True, True),
)

platform.StorageVolume.type_info = (
    ('units', str, True, False),
    ('volume', int, True, False),
)

shared.NumberArray.type_info = (
    ('values', str, True, False),
)

platform.StoragePool.type_info = (
    ('description', shared.Cimtext, False, False),
    ('volume_available', platform.StorageVolume, True, False),
    ('vendor', shared.Party, False, False),
    ('name', str, True, False),
    ('type', str, False, False),
)

science.Extent.type_info = (
    ('northern_boundary', float, False, False),
    ('region_known_as', str, False, True),
    ('is_global', bool, True, False),
    ('minimum_vertical_level', float, False, False),
    ('western_boundary', float, False, False),
    ('maximum_vertical_level', float, False, False),
    ('southern_boundary', float, False, False),
    ('eastern_boundary', float, False, False),
    ('z_units', str, True, False),
)

drs.DrsTemporalIdentifier.type_info = (
    ('end', str, False, False),
    ('suffix', str, False, False),
    ('start', str, True, False),
)

platform.Performance.type_info = (
    ('chsy', float, False, False),
    ('compiler', str, False, False),
    ('memory_bloat', float, False, False),
    ('asypd', float, False, False),
    ('model', software.Model, True, False),
    ('subcomponent_performance', platform.ComponentPerformance, False, False),
    ('meta', shared.Meta, True, False),
    ('load_imbalance', float, False, False),
    ('platform', platform.Machine, True, False),
    ('coupler_load', float, False, False),
    ('io_load', float, False, False),
    ('total_nodes_used', int, False, False),
    ('sypd', float, False, False),
    ('name', str, False, False),
)

shared.Calendar.type_info = (
    ('name', str, False, False),
    ('month_lengths', int, False, True),
    ('cal_type', str, True, False),
    ('description', str, False, False),
)

software.DevelopmentPath.type_info = (
    ('funding_sources', shared.Responsibility, False, True),
    ('developed_in_house', bool, True, False),
    ('previous_version', str, False, False),
    ('consortium_name', str, False, False),
    ('creators', shared.Responsibility, False, True),
)

activity.OutputTemporalRequirement.type_info = (
    ('throughout', bool, True, False),
    ('continuous_subset', shared.TimePeriod, False, True),
    ('sliced_subset', shared.TimesliceList, False, False),
)

shared.Party.type_info = (
    ('meta', shared.MinimalMeta, True, False),
    ('address', str, False, False),
    ('name', str, False, False),
    ('email', str, False, False),
    ('url', shared.OnlineResource, False, False),
    ('organisation', bool, False, False),
)

activity.Simulation.type_info = (
    ('primary_ensemble', activity.Ensemble, False, False),
    ('part_of_project', activity.Project, True, True),
    ('ensemble_identifier', str, True, False),
    ('run_for_experiments', activity.NumericalExperiment, True, True),
    ('parent_simulation', activity.ParentSimulation, False, False),
    ('used', software.Model, True, False),
)

software.Gridspec.type_info = (
    ('description', str, True, False),
)

science.GridSummary.type_info = (
    ('grid_type', str, True, False),
    ('grid_extent', science.Extent, True, False),
    ('grid_layout', str, True, False),
)

platform.Partition.type_info = (
    ('compute_pools', platform.ComputePool, True, True),
    ('name', str, True, False),
    ('institution', shared.Party, True, False),
    ('online_documentation', shared.OnlineResource, False, True),
    ('vendor', shared.Party, False, False),
    ('storage_pools', platform.StoragePool, False, True),
    ('when_used', shared.TimePeriod, False, False),
    ('description', shared.Cimtext, False, False),
    ('model_number', str, False, False),
    ('partition', platform.Partition, False, True),
)

software.Model.type_info = (
    ('internal_software_components', software.SoftwareComponent, False, True),
    ('scientific_domain', science.ScientificDomain, False, True),
    ('category', str, True, False),
    ('extra_conservation_properties', science.ConservationProperties, False, False),
    ('coupler', str, False, False),
    ('coupled_software_components', software.Model, False, True),
    ('meta', shared.Meta, True, False),
)

science.ScientificDomain.type_info = (
    ('realm', str, False, False),
    ('meta', shared.Meta, True, False),
    ('simulates', science.Process, True, True),
    ('overview', shared.Cimtext, False, False),
    ('time_step', float, True, False),
    ('references', shared.Reference, False, True),
    ('grid', science.GridSummary, False, False),
    ('extra_conservation_properties', science.ConservationProperties, False, False),
    ('name', str, True, False),
    ('resolution', science.Resolution, True, False),
)

software.Variable.type_info = (
    ('description', str, False, False),
    ('prognostic', bool, True, False),
    ('name', str, True, False),
)

activity.MultiTimeEnsemble.type_info = (
    ('ensemble_members', shared.DatetimeSet, True, False),
)

shared.Pid.type_info = (
    ('id', str, True, False),
    ('resolution_service', shared.OnlineResource, True, False),
)

activity.Conformance.type_info = (
    ('target_requirement', activity.NumericalRequirement, True, False),
)

activity.TemporalConstraint.type_info = (
    ('start_flexibility', shared.TimePeriod, False, False),
    ('start_date', shared.DateTime, False, False),
    ('required_calendar', shared.Calendar, False, False),
    ('required_duration', shared.TimePeriod, False, False),
)

science.Algorithm.type_info = (
    ('prognostic_variables', data.VariableCollection, False, True),
    ('diagnostic_variables', data.VariableCollection, False, True),
    ('implementation_overview', shared.Cimtext, True, False),
    ('references', shared.Citation, False, True),
    ('heading', str, True, False),
)

shared.DatetimeSet.type_info = (
    ('length', int, True, False),
)

shared.DateTime.type_info = (
    ('offset', bool, False, False),
    ('value', str, True, False),
)

software.SoftwareComponent.type_info = (
    ('grid', software.Gridspec, False, False),
    ('license', str, False, False),
    ('composition', software.Composition, False, False),
    ('coupling_framework', str, False, False),
    ('language', str, False, False),
    ('connection_points', software.Variable, False, True),
    ('dependencies', software.EntryPoint, False, True),
    ('sub_components', software.SoftwareComponent, False, True),
)

science.ProcessDetail.type_info = (
    ('content', shared.Cimtext, False, False),
    ('vocabulary', str, False, False),
    ('selection', str, False, True),
    ('properties', shared.KeyFloat, False, True),
    ('heading', str, False, False),
)

drs.DrsGeographicalIndicator.type_info = (
    ('spatial_domain', str, False, False),
    ('bounding_box', str, False, False),
    ('operator', str, False, False),
)

activity.NumericalRequirement.type_info = (
    ('additional_requirements', activity.NumericalRequirement, False, True),
    ('conformance_is_requested', bool, True, False),
)

drs.DrsAtomicDataset.type_info = (
    ('mip_table', str, True, False),
    ('temporal_constraint', drs.DrsTemporalIdentifier, False, False),
    ('variable_name', str, True, False),
    ('ensemble_member', drs.DrsEnsembleIdentifier, True, False),
    ('geographical_constraint', drs.DrsGeographicalIndicator, False, False),
)

shared.RegularTimeset.type_info = (
    ('increment', shared.TimePeriod, True, False),
    ('length', int, True, False),
    ('start_date', shared.DateTime, True, False),
)

science.Process.type_info = (
    ('algorithm_properties', science.Algorithm, False, True),
    ('references', shared.Reference, False, True),
    ('name', str, True, False),
    ('detailed_properties', science.ProcessDetail, False, True),
    ('keywords', str, True, False),
    ('time_step_in_process', float, False, False),
    ('description', str, False, False),
    ('implementation_overview', shared.Cimtext, True, False),
)

data.Dataset.type_info = (
    ('meta', shared.Meta, True, False),
    ('description', str, False, False),
    ('availability', shared.OnlineResource, False, True),
    ('references', shared.Citation, False, True),
    ('related_to_dataset', data.RelatedData, False, True),
    ('dataset_author', shared.Party, False, True),
    ('drs_datasets', drs.DrsPublicationDataset, False, True),
    ('name', str, True, False),
    ('produced_by', activity.Simulation, False, False),
)

