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

import typeset_for_drs_package as drs
import typeset_for_shared_package as shared
import typeset_for_science_package as science
import typeset_for_software_package as software
import typeset_for_data_package as data
import typeset_for_platform_package as platform
import typeset_for_activity_package as activity




# Set type keys.
software.SoftwareComponent.type_key = 'cim.2.software.SoftwareComponent'
shared.TimePeriod.type_key = 'cim.2.shared.TimePeriod'
software.EntryPoint.type_key = 'cim.2.software.EntryPoint'
shared.Meta.type_key = 'cim.2.shared.Meta'
science.Algorithm.type_key = 'cim.2.science.Algorithm'
activity.DomainProperties.type_key = 'cim.2.activity.DomainProperties'
shared.KeyFloat.type_key = 'cim.2.shared.KeyFloat'
shared.RegularTimeset.type_key = 'cim.2.shared.RegularTimeset'
activity.Ensemble.type_key = 'cim.2.activity.Ensemble'
activity.MultiTimeEnsemble.type_key = 'cim.2.activity.MultiTimeEnsemble'
science.Tuning.type_key = 'cim.2.science.Tuning'
activity.NumericalExperiment.type_key = 'cim.2.activity.NumericalExperiment'
software.Model.type_key = 'cim.2.software.Model'
software.Variable.type_key = 'cim.2.software.Variable'
activity.ForcingConstraint.type_key = 'cim.2.activity.ForcingConstraint'
shared.DatetimeSet.type_key = 'cim.2.shared.DatetimeSet'
shared.OnlineResource.type_key = 'cim.2.shared.OnlineResource'
shared.Reference.type_key = 'cim.2.shared.Reference'
science.Extent.type_key = 'cim.2.science.Extent'
data.Dataset.type_key = 'cim.2.data.Dataset'
activity.EnsembleAxis.type_key = 'cim.2.activity.EnsembleAxis'
platform.Performance.type_key = 'cim.2.platform.Performance'
shared.Cimtext.type_key = 'cim.2.shared.Cimtext'
activity.EnsembleMember.type_key = 'cim.2.activity.EnsembleMember'
shared.NumberArray.type_key = 'cim.2.shared.NumberArray'
drs.DrsTemporalIdentifier.type_key = 'cim.2.drs.DrsTemporalIdentifier'
science.ScientificDomain.type_key = 'cim.2.science.ScientificDomain'
platform.ComponentPerformance.type_key = 'cim.2.platform.ComponentPerformance'
activity.Downscaling.type_key = 'cim.2.activity.Downscaling'
software.Composition.type_key = 'cim.2.software.Composition'
activity.ParentSimulation.type_key = 'cim.2.activity.ParentSimulation'
software.DevelopmentPath.type_key = 'cim.2.software.DevelopmentPath'
drs.DrsGeographicalIndicator.type_key = 'cim.2.drs.DrsGeographicalIndicator'
drs.DrsAtomicDataset.type_key = 'cim.2.drs.DrsAtomicDataset'
activity.Activity.type_key = 'cim.2.activity.Activity'
shared.CimLink.type_key = 'cim.2.shared.CimLink'
activity.EnsembleRequirement.type_key = 'cim.2.activity.EnsembleRequirement'
shared.StandaloneDocument.type_key = 'cim.2.shared.StandaloneDocument'
activity.NumericalRequirement.type_key = 'cim.2.activity.NumericalRequirement'
platform.Machine.type_key = 'cim.2.platform.Machine'
shared.Responsibility.type_key = 'cim.2.shared.Responsibility'
activity.AxisMember.type_key = 'cim.2.activity.AxisMember'
shared.IrregularDateset.type_key = 'cim.2.shared.IrregularDateset'
science.ProcessDetail.type_key = 'cim.2.science.ProcessDetail'
science.ConservationProperties.type_key = 'cim.2.science.ConservationProperties'
science.Process.type_key = 'cim.2.science.Process'
shared.TimesliceList.type_key = 'cim.2.shared.TimesliceList'
platform.ComputePool.type_key = 'cim.2.platform.ComputePool'
activity.Simulation.type_key = 'cim.2.activity.Simulation'
shared.Citation.type_key = 'cim.2.shared.Citation'
shared.Calendar.type_key = 'cim.2.shared.Calendar'
drs.DrsEnsembleIdentifier.type_key = 'cim.2.drs.DrsEnsembleIdentifier'
shared.DateTime.type_key = 'cim.2.shared.DateTime'
activity.Project.type_key = 'cim.2.activity.Project'
platform.StorageVolume.type_key = 'cim.2.platform.StorageVolume'
shared.VocabMember.type_key = 'cim.2.shared.VocabMember'
software.ComponentBase.type_key = 'cim.2.software.ComponentBase'
activity.UberEnsemble.type_key = 'cim.2.activity.UberEnsemble'
activity.Conformance.type_key = 'cim.2.activity.Conformance'
activity.OutputTemporalRequirement.type_key = 'cim.2.activity.OutputTemporalRequirement'
data.VariableCollection.type_key = 'cim.2.data.VariableCollection'
shared.Party.type_key = 'cim.2.shared.Party'
shared.Pid.type_key = 'cim.2.shared.Pid'
shared.MinimalMeta.type_key = 'cim.2.shared.MinimalMeta'
platform.Partition.type_key = 'cim.2.platform.Partition'
activity.MultiEnsemble.type_key = 'cim.2.activity.MultiEnsemble'
software.Gridspec.type_key = 'cim.2.software.Gridspec'
science.GridSummary.type_key = 'cim.2.science.GridSummary'
activity.TemporalConstraint.type_key = 'cim.2.activity.TemporalConstraint'
activity.SimulationPlan.type_key = 'cim.2.activity.SimulationPlan'
science.Resolution.type_key = 'cim.2.science.Resolution'
platform.StoragePool.type_key = 'cim.2.platform.StoragePool'
data.RelatedData.type_key = 'cim.2.data.RelatedData'
drs.DrsPublicationDataset.type_key = 'cim.2.drs.DrsPublicationDataset'


# Set type info (name, type, is_required, is_iterative).
software.SoftwareComponent.type_info = (
    ('coupling_framework', str, False, False),
    ('sub_components', software.SoftwareComponent, False, True),
    ('language', str, False, False),
    ('license', str, False, False),
    ('dependencies', software.EntryPoint, False, True),
    ('grid', software.Gridspec, False, False),
    ('connection_points', software.Variable, False, True),
    ('composition', software.Composition, False, False),
)

shared.TimePeriod.type_info = (
    ('calendar', shared.Calendar, False, False),
    ('units', str, True, False),
    ('date_type', str, True, False),
    ('length', int, True, False),
    ('date', shared.DateTime, False, False),
)

software.EntryPoint.type_info = (
    ('name', str, False, False),
)

shared.Meta.type_info = (
    ('metadata_author', shared.Party, True, False),
    ('metadata_quality', str, False, False),
    ('metadata_reviewer', shared.Party, False, False),
    ('metadata_completeness', str, False, False),
)

science.Algorithm.type_info = (
    ('implementation_overview', shared.Cimtext, True, False),
    ('diagnostic_variables', data.VariableCollection, False, True),
    ('references', shared.Citation, False, True),
    ('prognostic_variables', data.VariableCollection, False, True),
    ('heading', str, True, False),
)

activity.DomainProperties.type_info = (
    ('required_extent', science.Extent, False, False),
    ('required_resolution', science.Resolution, False, False),
)

shared.KeyFloat.type_info = (
    ('key', str, True, False),
    ('value', float, True, False),
)

shared.RegularTimeset.type_info = (
    ('increment', shared.TimePeriod, True, False),
    ('start_date', shared.DateTime, True, False),
    ('length', int, True, False),
)

activity.Ensemble.type_info = (
    ('part_of', activity.UberEnsemble, False, True),
    ('members', activity.EnsembleMember, True, True),
    ('supported', activity.NumericalExperiment, True, True),
    ('common_conformances', activity.Conformance, False, True),
    ('has_ensemble_axes', activity.EnsembleAxis, False, True),
)

activity.MultiTimeEnsemble.type_info = (
    ('ensemble_members', shared.DatetimeSet, True, False),
)

science.Tuning.type_info = (
    ('regional_metrics_used', data.VariableCollection, False, False),
    ('trend_metrics_used', data.VariableCollection, False, False),
    ('description', shared.Cimtext, True, False),
    ('global_mean_metrics_used', data.VariableCollection, False, False),
)

activity.NumericalExperiment.type_info = (
    ('requirements', activity.NumericalRequirement, False, True),
    ('related_experiments', activity.NumericalExperiment, False, True),
)

software.Model.type_info = (
    ('extra_conservation_properties', science.ConservationProperties, False, False),
    ('scientific_domain', science.ScientificDomain, False, True),
    ('coupled_software_components', software.Model, False, True),
    ('meta', shared.Meta, True, False),
    ('internal_software_components', software.SoftwareComponent, False, True),
    ('coupler', str, False, False),
    ('category', str, True, False),
)

software.Variable.type_info = (
    ('name', str, True, False),
    ('description', str, False, False),
    ('prognostic', bool, True, False),
)

activity.ForcingConstraint.type_info = (
    ('category', shared.VocabMember, True, False),
    ('origin', shared.Citation, False, False),
    ('group', shared.VocabMember, False, False),
    ('forcing_type', str, True, False),
    ('data_link', shared.OnlineResource, False, False),
    ('code', shared.VocabMember, True, False),
    ('additional_constraint', shared.Cimtext, False, False),
)

shared.DatetimeSet.type_info = (
    ('length', int, True, False),
)

shared.OnlineResource.type_info = (
    ('name', str, True, False),
    ('description', str, False, False),
    ('protocol', str, False, False),
    ('linkage', str, True, False),
)

shared.Reference.type_info = (
)

science.Extent.type_info = (
    ('western_boundary', float, False, False),
    ('z_units', str, True, False),
    ('eastern_boundary', float, False, False),
    ('southern_boundary', float, False, False),
    ('northern_boundary', float, False, False),
    ('region_known_as', str, False, True),
    ('maximum_vertical_level', float, False, False),
    ('is_global', bool, True, False),
    ('minimum_vertical_level', float, False, False),
)

data.Dataset.type_info = (
    ('dataset_author', shared.Party, False, True),
    ('meta', shared.Meta, True, False),
    ('drs_datasets', drs.DrsPublicationDataset, False, True),
    ('produced_by', activity.Simulation, False, False),
    ('description', str, False, False),
    ('name', str, True, False),
    ('related_to_dataset', data.RelatedData, False, True),
    ('availability', shared.OnlineResource, False, True),
    ('references', shared.Citation, False, True),
)

activity.EnsembleAxis.type_info = (
    ('extra_detail', shared.Cimtext, True, False),
    ('short_identifier', str, True, False),
    ('target_requirement', activity.NumericalRequirement, True, False),
    ('member', activity.AxisMember, True, True),
)

platform.Performance.type_info = (
    ('load_imbalance', float, False, False),
    ('platform', platform.Machine, True, False),
    ('memory_bloat', float, False, False),
    ('io_load', float, False, False),
    ('meta', shared.Meta, True, False),
    ('total_nodes_used', int, False, False),
    ('subcomponent_performance', platform.ComponentPerformance, False, False),
    ('chsy', float, False, False),
    ('compiler', str, False, False),
    ('coupler_load', float, False, False),
    ('asypd', float, False, False),
    ('sypd', float, False, False),
    ('model', software.Model, True, False),
    ('name', str, False, False),
)

shared.Cimtext.type_info = (
    ('content', str, True, False),
    ('content_type', str, True, False),
)

activity.EnsembleMember.type_info = (
    ('had_performance', platform.Performance, False, False),
    ('simulation', activity.Simulation, True, False),
    ('ran_on', platform.Machine, True, False),
)

shared.NumberArray.type_info = (
    ('values', str, True, False),
)

drs.DrsTemporalIdentifier.type_info = (
    ('end', str, False, False),
    ('suffix', str, False, False),
    ('start', str, True, False),
)

science.ScientificDomain.type_info = (
    ('references', shared.Reference, False, True),
    ('grid', science.GridSummary, False, False),
    ('simulates', science.Process, True, True),
    ('name', str, True, False),
    ('time_step', float, True, False),
    ('resolution', science.Resolution, True, False),
    ('realm', str, False, False),
    ('meta', shared.Meta, True, False),
    ('overview', shared.Cimtext, False, False),
    ('extra_conservation_properties', science.ConservationProperties, False, False),
)

platform.ComponentPerformance.type_info = (
    ('nodes_used', int, False, False),
    ('speed', float, True, False),
    ('component', software.SoftwareComponent, False, False),
    ('cores_used', int, False, False),
    ('component_name', str, True, False),
)

activity.Downscaling.type_info = (
    ('downscaled_from', activity.Simulation, True, False),
)

software.Composition.type_info = (
    ('couplings', str, False, True),
    ('description', str, False, False),
)

activity.ParentSimulation.type_info = (
    ('parent', activity.Simulation, True, False),
    ('branch_time_in_child', shared.DateTime, False, False),
    ('branch_time_in_parent', shared.DateTime, False, False),
)

software.DevelopmentPath.type_info = (
    ('previous_version', str, False, False),
    ('developed_in_house', bool, True, False),
    ('funding_sources', shared.Responsibility, False, True),
    ('consortium_name', str, False, False),
    ('creators', shared.Responsibility, False, True),
)

drs.DrsGeographicalIndicator.type_info = (
    ('spatial_domain', str, False, False),
    ('bounding_box', str, False, False),
    ('operator', str, False, False),
)

drs.DrsAtomicDataset.type_info = (
    ('temporal_constraint', drs.DrsTemporalIdentifier, False, False),
    ('variable_name', str, True, False),
    ('ensemble_member', drs.DrsEnsembleIdentifier, True, False),
    ('mip_table', str, True, False),
    ('geographical_constraint', drs.DrsGeographicalIndicator, False, False),
)

activity.Activity.type_info = (
    ('canonical_name', str, False, False),
    ('rationale', shared.Cimtext, False, False),
    ('responsible_parties', shared.Responsibility, False, True),
    ('keywords', str, False, True),
    ('duration', shared.TimePeriod, False, False),
    ('meta', shared.Meta, True, False),
    ('description', shared.Cimtext, False, False),
    ('references', shared.Citation, False, True),
    ('long_name', str, False, False),
    ('name', str, True, False),
)

shared.CimLink.type_info = (
    ('remote_type', str, True, False),
)

activity.EnsembleRequirement.type_info = (
    ('ensemble_member', activity.NumericalRequirement, False, True),
    ('minimum_size', int, True, False),
    ('ensemble_type', str, True, False),
)

shared.StandaloneDocument.type_info = (
    ('long_name', str, False, False),
    ('responsible_parties', shared.Responsibility, False, True),
    ('name', str, True, False),
    ('references', shared.Citation, False, True),
    ('meta', shared.Meta, True, False),
)

activity.NumericalRequirement.type_info = (
    ('additional_requirements', activity.NumericalRequirement, False, True),
    ('conformance_is_requested', bool, True, False),
)

platform.Machine.type_info = (
    ('meta', shared.Meta, True, False),
)

shared.Responsibility.type_info = (
    ('when', shared.TimePeriod, False, False),
    ('party', shared.Party, True, True),
    ('role', str, True, False),
)

activity.AxisMember.type_info = (
    ('value', float, False, False),
    ('description', str, True, False),
    ('index', int, True, False),
)

shared.IrregularDateset.type_info = (
    ('date_set', str, True, False),
)

science.ProcessDetail.type_info = (
    ('heading', str, False, False),
    ('vocabulary', str, False, False),
    ('selection', str, False, True),
    ('content', shared.Cimtext, False, False),
    ('properties', shared.KeyFloat, False, True),
)

science.ConservationProperties.type_info = (
    ('flux_correction_was_used', bool, True, False),
    ('corrected_conserved_prognostic_variables', data.VariableCollection, False, False),
    ('correction_methodology', shared.Cimtext, False, False),
)

science.Process.type_info = (
    ('keywords', str, True, False),
    ('references', shared.Reference, False, True),
    ('algorithm_properties', science.Algorithm, False, True),
    ('implementation_overview', shared.Cimtext, True, False),
    ('name', str, True, False),
    ('time_step_in_process', float, False, False),
    ('description', str, False, False),
    ('detailed_properties', science.ProcessDetail, False, True),
)

shared.TimesliceList.type_info = (
    ('members', shared.NumberArray, True, False),
    ('units', str, True, False),
)

platform.ComputePool.type_info = (
    ('description', shared.Cimtext, False, False),
    ('operating_system', str, False, False),
    ('accelerator_type', str, False, False),
    ('cpu_type', str, False, False),
    ('number_of_nodes', int, False, False),
    ('compute_cores_per_node', int, False, False),
    ('model_number', str, False, False),
    ('interconnect', str, False, False),
    ('accelerators_per_node', int, False, False),
    ('memory_per_node', platform.StorageVolume, False, False),
    ('name', str, False, False),
)

activity.Simulation.type_info = (
    ('part_of_project', activity.Project, True, True),
    ('ensemble_identifier', str, True, False),
    ('run_for_experiments', activity.NumericalExperiment, True, True),
    ('parent_simulation', activity.ParentSimulation, False, False),
    ('used', software.Model, True, False),
    ('primary_ensemble', activity.Ensemble, False, False),
)

shared.Citation.type_info = (
    ('title', str, False, False),
    ('abstract', str, False, False),
    ('context', shared.Cimtext, False, False),
    ('citation_str', shared.Cimtext, True, False),
    ('doi', str, False, False),
    ('url', shared.OnlineResource, False, False),
)

shared.Calendar.type_info = (
    ('name', str, False, False),
    ('cal_type', str, True, False),
    ('month_lengths', int, False, True),
    ('description', str, False, False),
)

drs.DrsEnsembleIdentifier.type_info = (
    ('realisation_number', int, True, False),
    ('initialisation_method_number', int, True, False),
    ('perturbation_number', int, True, False),
)

shared.DateTime.type_info = (
    ('offset', bool, False, False),
    ('value', str, True, False),
)

activity.Project.type_info = (
    ('previous_projects', activity.Project, False, True),
    ('sub_projects', activity.Project, False, True),
    ('requires_experiments', activity.NumericalExperiment, False, True),
)

platform.StorageVolume.type_info = (
    ('units', str, True, False),
    ('volume', int, True, False),
)

shared.VocabMember.type_info = (
    ('uri', str, False, False),
    ('vocab', shared.Citation, False, False),
    ('value', str, True, False),
)

software.ComponentBase.type_info = (
    ('tuning_applied', science.Tuning, False, False),
    ('name', str, True, False),
    ('description', shared.Cimtext, False, False),
    ('long_name', str, False, False),
    ('documentation', shared.Citation, False, True),
    ('version', str, False, False),
    ('development_history', software.DevelopmentPath, False, False),
    ('release_date', datetime.datetime, False, False),
)

activity.UberEnsemble.type_info = (
    ('child_ensembles', activity.Ensemble, True, True),
)

activity.Conformance.type_info = (
    ('target_requirement', activity.NumericalRequirement, True, False),
)

activity.OutputTemporalRequirement.type_info = (
    ('continuous_subset', shared.TimePeriod, False, True),
    ('throughout', bool, True, False),
    ('sliced_subset', shared.TimesliceList, False, False),
)

data.VariableCollection.type_info = (
    ('collection_name', str, False, False),
    ('variables', str, True, True),
)

shared.Party.type_info = (
    ('email', str, False, False),
    ('url', shared.OnlineResource, False, False),
    ('name', str, False, False),
    ('meta', shared.MinimalMeta, True, False),
    ('address', str, False, False),
    ('organisation', bool, False, False),
)

shared.Pid.type_info = (
    ('id', str, True, False),
    ('resolution_service', shared.OnlineResource, True, False),
)

shared.MinimalMeta.type_info = (
    ('document_version', int, False, False),
    ('uid', str, True, False),
    ('metadata_last_updated', datetime.datetime, True, False),
)

platform.Partition.type_info = (
    ('description', shared.Cimtext, False, False),
    ('vendor', shared.Party, False, False),
    ('storage_pools', platform.StoragePool, False, True),
    ('model_number', str, False, False),
    ('institution', shared.Party, True, False),
    ('name', str, True, False),
    ('when_used', shared.TimePeriod, False, False),
    ('compute_pools', platform.ComputePool, True, True),
    ('online_documentation', shared.OnlineResource, False, True),
    ('partition', platform.Partition, False, True),
)

activity.MultiEnsemble.type_info = (
    ('ensemble_axis', activity.EnsembleRequirement, True, True),
)

software.Gridspec.type_info = (
    ('description', str, True, False),
)

science.GridSummary.type_info = (
    ('grid_type', str, True, False),
    ('grid_extent', science.Extent, True, False),
    ('grid_layout', str, True, False),
)

activity.TemporalConstraint.type_info = (
    ('required_calendar', shared.Calendar, False, False),
    ('start_flexibility', shared.TimePeriod, False, False),
    ('start_date', shared.DateTime, False, False),
    ('required_duration', shared.TimePeriod, False, False),
)

activity.SimulationPlan.type_info = (
    ('will_support_experiments', activity.NumericalExperiment, True, True),
    ('expected_platform', platform.Machine, False, False),
    ('expected_model', software.Model, True, False),
    ('expected_performance_sypd', float, False, False),
)

science.Resolution.type_info = (
    ('equivalent_horizontal_resolution', float, True, False),
    ('name', str, True, False),
    ('number_of_levels', int, False, True),
    ('number_of_xy_gridpoints', int, False, True),
    ('is_adaptive_grid', bool, False, False),
)

platform.StoragePool.type_info = (
    ('description', shared.Cimtext, False, False),
    ('volume_available', platform.StorageVolume, True, False),
    ('vendor', shared.Party, False, False),
    ('type', str, False, False),
    ('name', str, True, False),
)

data.RelatedData.type_info = (
    ('other_dataset', data.Dataset, True, False),
    ('relationship', str, True, False),
)

drs.DrsPublicationDataset.type_info = (
    ('product', str, True, False),
    ('frequency', str, False, False),
    ('institute', str, True, False),
    ('realm', str, False, False),
    ('model', str, True, False),
    ('version_number', int, False, False),
    ('experiment', str, True, False),
    ('activity', str, True, False),
)

