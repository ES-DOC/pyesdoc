# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_meta.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encpasulates meta-information pertaining to the cim.v2 typeset.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-07-24 23:58:29.520941.

"""
import datetime
import uuid

import typeset_for_data_package as data
import typeset_for_platform_package as platform
import typeset_for_drs_package as drs
import typeset_for_activity_package as activity
import typeset_for_software_package as software
import typeset_for_science_package as science
import typeset_for_shared_package as shared




# Set type keys.
activity.Project.type_key = 'cim.2.activity.Project'
science.ProcessDetail.type_key = 'cim.2.science.ProcessDetail'
shared.Cimtext.type_key = 'cim.2.shared.Cimtext'
platform.ComputePool.type_key = 'cim.2.platform.ComputePool'
activity.ParentSimulation.type_key = 'cim.2.activity.ParentSimulation'
activity.MultiEnsemble.type_key = 'cim.2.activity.MultiEnsemble'
drs.DrsTemporalIdentifier.type_key = 'cim.2.drs.DrsTemporalIdentifier'
science.Process.type_key = 'cim.2.science.Process'
software.Gridspec.type_key = 'cim.2.software.Gridspec'
shared.Responsibility.type_key = 'cim.2.shared.Responsibility'
science.Algorithm.type_key = 'cim.2.science.Algorithm'
data.Dataset.type_key = 'cim.2.data.Dataset'
software.EntryPoint.type_key = 'cim.2.software.EntryPoint'
shared.CimLink.type_key = 'cim.2.shared.CimLink'
shared.DateTime.type_key = 'cim.2.shared.DateTime'
shared.NumberArray.type_key = 'cim.2.shared.NumberArray'
platform.ComponentPerformance.type_key = 'cim.2.platform.ComponentPerformance'
software.Composition.type_key = 'cim.2.software.Composition'
activity.Simulation.type_key = 'cim.2.activity.Simulation'
platform.Performance.type_key = 'cim.2.platform.Performance'
drs.DrsAtomicDataset.type_key = 'cim.2.drs.DrsAtomicDataset'
shared.OnlineResource.type_key = 'cim.2.shared.OnlineResource'
shared.Party.type_key = 'cim.2.shared.Party'
activity.SimulationPlan.type_key = 'cim.2.activity.SimulationPlan'
shared.Citation.type_key = 'cim.2.shared.Citation'
software.ComponentBase.type_key = 'cim.2.software.ComponentBase'
activity.UberEnsemble.type_key = 'cim.2.activity.UberEnsemble'
platform.Machine.type_key = 'cim.2.platform.Machine'
software.DevelopmentPath.type_key = 'cim.2.software.DevelopmentPath'
shared.Calendar.type_key = 'cim.2.shared.Calendar'
activity.Activity.type_key = 'cim.2.activity.Activity'
science.Resolution.type_key = 'cim.2.science.Resolution'
activity.MultiTimeEnsemble.type_key = 'cim.2.activity.MultiTimeEnsemble'
science.Tuning.type_key = 'cim.2.science.Tuning'
shared.MinimalMeta.type_key = 'cim.2.shared.MinimalMeta'
activity.DomainProperties.type_key = 'cim.2.activity.DomainProperties'
software.Model.type_key = 'cim.2.software.Model'
activity.EnsembleRequirement.type_key = 'cim.2.activity.EnsembleRequirement'
shared.TimesliceList.type_key = 'cim.2.shared.TimesliceList'
activity.Ensemble.type_key = 'cim.2.activity.Ensemble'
activity.Downscaling.type_key = 'cim.2.activity.Downscaling'
drs.DrsPublicationDataset.type_key = 'cim.2.drs.DrsPublicationDataset'
activity.TemporalConstraint.type_key = 'cim.2.activity.TemporalConstraint'
data.VariableCollection.type_key = 'cim.2.data.VariableCollection'
platform.StorageVolume.type_key = 'cim.2.platform.StorageVolume'
platform.StoragePool.type_key = 'cim.2.platform.StoragePool'
shared.DatetimeSet.type_key = 'cim.2.shared.DatetimeSet'
activity.ForcingConstraint.type_key = 'cim.2.activity.ForcingConstraint'
shared.RegularTimeset.type_key = 'cim.2.shared.RegularTimeset'
activity.NumericalExperiment.type_key = 'cim.2.activity.NumericalExperiment'
activity.EnsembleAxis.type_key = 'cim.2.activity.EnsembleAxis'
shared.Meta.type_key = 'cim.2.shared.Meta'
activity.AxisMember.type_key = 'cim.2.activity.AxisMember'
shared.KeyFloat.type_key = 'cim.2.shared.KeyFloat'
platform.Partition.type_key = 'cim.2.platform.Partition'
science.Extent.type_key = 'cim.2.science.Extent'
shared.StandaloneDocument.type_key = 'cim.2.shared.StandaloneDocument'
software.Variable.type_key = 'cim.2.software.Variable'
shared.TimePeriod.type_key = 'cim.2.shared.TimePeriod'
shared.IrregularDateset.type_key = 'cim.2.shared.IrregularDateset'
activity.NumericalRequirement.type_key = 'cim.2.activity.NumericalRequirement'
data.RelatedData.type_key = 'cim.2.data.RelatedData'
science.ConservationProperties.type_key = 'cim.2.science.ConservationProperties'
science.GridSummary.type_key = 'cim.2.science.GridSummary'
software.SoftwareComponent.type_key = 'cim.2.software.SoftwareComponent'
activity.EnsembleMember.type_key = 'cim.2.activity.EnsembleMember'
drs.DrsGeographicalIndicator.type_key = 'cim.2.drs.DrsGeographicalIndicator'
activity.OutputTemporalRequirement.type_key = 'cim.2.activity.OutputTemporalRequirement'
drs.DrsEnsembleIdentifier.type_key = 'cim.2.drs.DrsEnsembleIdentifier'
shared.Reference.type_key = 'cim.2.shared.Reference'
activity.Conformance.type_key = 'cim.2.activity.Conformance'
shared.Pid.type_key = 'cim.2.shared.Pid'
shared.VocabMember.type_key = 'cim.2.shared.VocabMember'
science.ScientificDomain.type_key = 'cim.2.science.ScientificDomain'


# Set type info (name, type, is_required, is_iterative).
activity.Project.type_info = (
    ('previous_projects', activity.Project, False, True),
    ('sub_projects', activity.Project, False, True),
    ('requires_experiments', activity.NumericalExperiment, False, True),
)

science.ProcessDetail.type_info = (
    ('content', shared.Cimtext, False, False),
    ('vocabulary', str, False, False),
    ('selection', str, False, True),
    ('properties', shared.KeyFloat, False, True),
    ('heading', str, False, False),
)

shared.Cimtext.type_info = (
    ('content', str, True, False),
    ('content_type', str, True, False),
)

platform.ComputePool.type_info = (
    ('operating_system', str, False, False),
    ('model_number', str, False, False),
    ('accelerators_per_node', int, False, False),
    ('memory_per_node', platform.StorageVolume, False, False),
    ('compute_cores_per_node', int, False, False),
    ('description', shared.Cimtext, False, False),
    ('number_of_nodes', int, False, False),
    ('accelerator_type', str, False, False),
    ('interconnect', str, False, False),
    ('cpu_type', str, False, False),
    ('name', str, False, False),
)

activity.ParentSimulation.type_info = (
    ('parent', activity.Simulation, True, False),
    ('branch_time_in_child', shared.DateTime, False, False),
    ('branch_time_in_parent', shared.DateTime, False, False),
)

activity.MultiEnsemble.type_info = (
    ('ensemble_axis', activity.EnsembleRequirement, True, True),
)

drs.DrsTemporalIdentifier.type_info = (
    ('end', str, False, False),
    ('suffix', str, False, False),
    ('start', str, True, False),
)

science.Process.type_info = (
    ('algorithm_properties', science.Algorithm, False, True),
    ('name', str, True, False),
    ('detailed_properties', science.ProcessDetail, False, True),
    ('references', shared.Reference, False, True),
    ('keywords', str, True, False),
    ('description', str, False, False),
    ('implementation_overview', shared.Cimtext, True, False),
    ('time_step_in_process', float, False, False),
)

software.Gridspec.type_info = (
    ('description', str, True, False),
)

shared.Responsibility.type_info = (
    ('when', shared.TimePeriod, False, False),
    ('party', shared.Party, True, True),
    ('role', str, True, False),
)

science.Algorithm.type_info = (
    ('prognostic_variables', data.VariableCollection, False, True),
    ('diagnostic_variables', data.VariableCollection, False, True),
    ('references', shared.Citation, False, True),
    ('implementation_overview', shared.Cimtext, True, False),
    ('heading', str, True, False),
)

data.Dataset.type_info = (
    ('meta', shared.Meta, True, False),
    ('description', str, False, False),
    ('availability', shared.OnlineResource, False, True),
    ('produced_by', activity.Simulation, False, False),
    ('dataset_author', shared.Party, False, True),
    ('drs_datasets', drs.DrsPublicationDataset, False, True),
    ('name', str, True, False),
    ('references', shared.Citation, False, True),
    ('related_to_dataset', data.RelatedData, False, True),
)

software.EntryPoint.type_info = (
    ('name', str, False, False),
)

shared.CimLink.type_info = (
    ('remote_type', str, True, False),
)

shared.DateTime.type_info = (
    ('offset', bool, False, False),
    ('value', str, True, False),
)

shared.NumberArray.type_info = (
    ('values', str, True, False),
)

platform.ComponentPerformance.type_info = (
    ('cores_used', int, False, False),
    ('speed', float, True, False),
    ('component', software.SoftwareComponent, False, False),
    ('nodes_used', int, False, False),
    ('component_name', str, True, False),
)

software.Composition.type_info = (
    ('couplings', str, False, True),
    ('description', str, False, False),
)

activity.Simulation.type_info = (
    ('ensemble_identifier', str, True, False),
    ('run_for_experiments', activity.NumericalExperiment, True, True),
    ('parent_simulation', activity.ParentSimulation, False, False),
    ('used', software.Model, True, False),
    ('primary_ensemble', activity.Ensemble, False, False),
    ('part_of_project', activity.Project, True, True),
)

platform.Performance.type_info = (
    ('meta', shared.Meta, True, False),
    ('chsy', float, False, False),
    ('compiler', str, False, False),
    ('memory_bloat', float, False, False),
    ('asypd', float, False, False),
    ('model', software.Model, True, False),
    ('sypd', float, False, False),
    ('subcomponent_performance', platform.ComponentPerformance, False, False),
    ('load_imbalance', float, False, False),
    ('platform', platform.Machine, True, False),
    ('coupler_load', float, False, False),
    ('io_load', float, False, False),
    ('total_nodes_used', int, False, False),
    ('name', str, False, False),
)

drs.DrsAtomicDataset.type_info = (
    ('temporal_constraint', drs.DrsTemporalIdentifier, False, False),
    ('mip_table', str, True, False),
    ('ensemble_member', drs.DrsEnsembleIdentifier, True, False),
    ('variable_name', str, True, False),
    ('geographical_constraint', drs.DrsGeographicalIndicator, False, False),
)

shared.OnlineResource.type_info = (
    ('protocol', str, False, False),
    ('name', str, True, False),
    ('description', str, False, False),
    ('linkage', str, True, False),
)

shared.Party.type_info = (
    ('address', str, False, False),
    ('name', str, False, False),
    ('email', str, False, False),
    ('url', shared.OnlineResource, False, False),
    ('meta', shared.MinimalMeta, True, False),
    ('organisation', bool, False, False),
)

activity.SimulationPlan.type_info = (
    ('expected_platform', platform.Machine, False, False),
    ('will_support_experiments', activity.NumericalExperiment, True, True),
    ('expected_model', software.Model, True, False),
    ('expected_performance_sypd', float, False, False),
)

shared.Citation.type_info = (
    ('context', shared.Cimtext, False, False),
    ('citation_str', shared.Cimtext, True, False),
    ('title', str, False, False),
    ('url', shared.OnlineResource, False, False),
    ('abstract', str, False, False),
    ('doi', str, False, False),
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

activity.UberEnsemble.type_info = (
    ('child_ensembles', activity.Ensemble, True, True),
)

platform.Machine.type_info = (
    ('meta', shared.Meta, True, False),
)

software.DevelopmentPath.type_info = (
    ('previous_version', str, False, False),
    ('developed_in_house', bool, True, False),
    ('consortium_name', str, False, False),
    ('funding_sources', shared.Responsibility, False, True),
    ('creators', shared.Responsibility, False, True),
)

shared.Calendar.type_info = (
    ('cal_type', str, True, False),
    ('name', str, False, False),
    ('month_lengths', int, False, True),
    ('description', str, False, False),
)

activity.Activity.type_info = (
    ('long_name', str, False, False),
    ('duration', shared.TimePeriod, False, False),
    ('canonical_name', str, False, False),
    ('rationale', shared.Cimtext, False, False),
    ('responsible_parties', shared.Responsibility, False, True),
    ('references', shared.Citation, False, True),
    ('keywords', str, False, True),
    ('name', str, True, False),
    ('meta', shared.Meta, True, False),
    ('description', shared.Cimtext, False, False),
)

science.Resolution.type_info = (
    ('equivalent_horizontal_resolution', float, True, False),
    ('number_of_levels', int, False, True),
    ('number_of_xy_gridpoints', int, False, True),
    ('name', str, True, False),
    ('is_adaptive_grid', bool, False, False),
)

activity.MultiTimeEnsemble.type_info = (
    ('ensemble_members', shared.DatetimeSet, True, False),
)

science.Tuning.type_info = (
    ('trend_metrics_used', data.VariableCollection, False, False),
    ('regional_metrics_used', data.VariableCollection, False, False),
    ('description', shared.Cimtext, True, False),
    ('global_mean_metrics_used', data.VariableCollection, False, False),
)

shared.MinimalMeta.type_info = (
    ('document_version', int, False, False),
    ('uid', str, True, False),
    ('metadata_last_updated', datetime.datetime, True, False),
)

activity.DomainProperties.type_info = (
    ('required_extent', science.Extent, False, False),
    ('required_resolution', science.Resolution, False, False),
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

activity.EnsembleRequirement.type_info = (
    ('ensemble_member', activity.NumericalRequirement, False, True),
    ('minimum_size', int, True, False),
    ('ensemble_type', str, True, False),
)

shared.TimesliceList.type_info = (
    ('members', shared.NumberArray, True, False),
    ('units', str, True, False),
)

activity.Ensemble.type_info = (
    ('part_of', activity.UberEnsemble, False, True),
    ('members', activity.EnsembleMember, True, True),
    ('supported', activity.NumericalExperiment, True, True),
    ('common_conformances', activity.Conformance, False, True),
    ('has_ensemble_axes', activity.EnsembleAxis, False, True),
)

activity.Downscaling.type_info = (
    ('downscaled_from', activity.Simulation, True, False),
)

drs.DrsPublicationDataset.type_info = (
    ('model', str, True, False),
    ('realm', str, False, False),
    ('version_number', int, False, False),
    ('product', str, True, False),
    ('activity', str, True, False),
    ('frequency', str, False, False),
    ('experiment', str, True, False),
    ('institute', str, True, False),
)

activity.TemporalConstraint.type_info = (
    ('required_calendar', shared.Calendar, False, False),
    ('start_flexibility', shared.TimePeriod, False, False),
    ('start_date', shared.DateTime, False, False),
    ('required_duration', shared.TimePeriod, False, False),
)

data.VariableCollection.type_info = (
    ('collection_name', str, False, False),
    ('variables', str, True, True),
)

platform.StorageVolume.type_info = (
    ('units', str, True, False),
    ('volume', int, True, False),
)

platform.StoragePool.type_info = (
    ('description', shared.Cimtext, False, False),
    ('volume_available', platform.StorageVolume, True, False),
    ('vendor', shared.Party, False, False),
    ('name', str, True, False),
    ('type', str, False, False),
)

shared.DatetimeSet.type_info = (
    ('length', int, True, False),
)

activity.ForcingConstraint.type_info = (
    ('category', shared.VocabMember, True, False),
    ('origin', shared.Citation, False, False),
    ('group', shared.VocabMember, False, False),
    ('data_link', shared.OnlineResource, False, False),
    ('forcing_type', str, True, False),
    ('code', shared.VocabMember, True, False),
    ('additional_constraint', shared.Cimtext, False, False),
)

shared.RegularTimeset.type_info = (
    ('increment', shared.TimePeriod, True, False),
    ('length', int, True, False),
    ('start_date', shared.DateTime, True, False),
)

activity.NumericalExperiment.type_info = (
    ('requirements', activity.NumericalRequirement, False, True),
    ('related_experiments', activity.NumericalExperiment, False, True),
)

activity.EnsembleAxis.type_info = (
    ('short_identifier', str, True, False),
    ('target_requirement', activity.NumericalRequirement, True, False),
    ('extra_detail', shared.Cimtext, True, False),
    ('member', activity.AxisMember, True, True),
)

shared.Meta.type_info = (
    ('metadata_author', shared.Party, True, False),
    ('metadata_quality', str, False, False),
    ('metadata_reviewer', shared.Party, False, False),
    ('metadata_completeness', str, False, False),
)

activity.AxisMember.type_info = (
    ('value', float, False, False),
    ('description', str, True, False),
    ('index', int, True, False),
)

shared.KeyFloat.type_info = (
    ('key', str, True, False),
    ('value', float, True, False),
)

platform.Partition.type_info = (
    ('vendor', shared.Party, False, False),
    ('storage_pools', platform.StoragePool, False, True),
    ('name', str, True, False),
    ('online_documentation', shared.OnlineResource, False, True),
    ('institution', shared.Party, True, False),
    ('compute_pools', platform.ComputePool, True, True),
    ('description', shared.Cimtext, False, False),
    ('when_used', shared.TimePeriod, False, False),
    ('model_number', str, False, False),
    ('partition', platform.Partition, False, True),
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

shared.StandaloneDocument.type_info = (
    ('responsible_parties', shared.Responsibility, False, True),
    ('references', shared.Citation, False, True),
    ('name', str, True, False),
    ('long_name', str, False, False),
    ('meta', shared.Meta, True, False),
)

software.Variable.type_info = (
    ('description', str, False, False),
    ('prognostic', bool, True, False),
    ('name', str, True, False),
)

shared.TimePeriod.type_info = (
    ('length', int, True, False),
    ('date_type', str, True, False),
    ('units', str, True, False),
    ('calendar', shared.Calendar, False, False),
    ('date', shared.DateTime, False, False),
)

shared.IrregularDateset.type_info = (
    ('date_set', str, True, False),
)

activity.NumericalRequirement.type_info = (
    ('additional_requirements', activity.NumericalRequirement, False, True),
    ('conformance_is_requested', bool, True, False),
)

data.RelatedData.type_info = (
    ('relationship', str, True, False),
    ('other_dataset', data.Dataset, True, False),
)

science.ConservationProperties.type_info = (
    ('flux_correction_was_used', bool, True, False),
    ('corrected_conserved_prognostic_variables', data.VariableCollection, False, False),
    ('correction_methodology', shared.Cimtext, False, False),
)

science.GridSummary.type_info = (
    ('grid_type', str, True, False),
    ('grid_extent', science.Extent, True, False),
    ('grid_layout', str, True, False),
)

software.SoftwareComponent.type_info = (
    ('grid', software.Gridspec, False, False),
    ('license', str, False, False),
    ('composition', software.Composition, False, False),
    ('sub_components', software.SoftwareComponent, False, True),
    ('coupling_framework', str, False, False),
    ('language', str, False, False),
    ('connection_points', software.Variable, False, True),
    ('dependencies', software.EntryPoint, False, True),
)

activity.EnsembleMember.type_info = (
    ('had_performance', platform.Performance, False, False),
    ('simulation', activity.Simulation, True, False),
    ('ran_on', platform.Machine, True, False),
)

drs.DrsGeographicalIndicator.type_info = (
    ('spatial_domain', str, False, False),
    ('bounding_box', str, False, False),
    ('operator', str, False, False),
)

activity.OutputTemporalRequirement.type_info = (
    ('continuous_subset', shared.TimePeriod, False, True),
    ('throughout', bool, True, False),
    ('sliced_subset', shared.TimesliceList, False, False),
)

drs.DrsEnsembleIdentifier.type_info = (
    ('realisation_number', int, True, False),
    ('initialisation_method_number', int, True, False),
    ('perturbation_number', int, True, False),
)

shared.Reference.type_info = (
)

activity.Conformance.type_info = (
    ('target_requirement', activity.NumericalRequirement, True, False),
)

shared.Pid.type_info = (
    ('id', str, True, False),
    ('resolution_service', shared.OnlineResource, True, False),
)

shared.VocabMember.type_info = (
    ('vocab', shared.Citation, False, False),
    ('uri', str, False, False),
    ('value', str, True, False),
)

science.ScientificDomain.type_info = (
    ('realm', str, False, False),
    ('meta', shared.Meta, True, False),
    ('simulates', science.Process, True, True),
    ('extra_conservation_properties', science.ConservationProperties, False, False),
    ('resolution', science.Resolution, True, False),
    ('references', shared.Reference, False, True),
    ('grid', science.GridSummary, False, False),
    ('overview', shared.Cimtext, False, False),
    ('name', str, True, False),
    ('time_step', float, True, False),
)

