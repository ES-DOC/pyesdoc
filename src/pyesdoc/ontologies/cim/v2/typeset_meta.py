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

import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_drs_package as drs
import typeset_for_platform_package as platform
import typeset_for_science_package as science
import typeset_for_shared_package as shared
import typeset_for_software_package as software




# Set type keys.
activity.Activity.type_key = 'cim.2.activity.Activity'
activity.AxisMember.type_key = 'cim.2.activity.AxisMember'
activity.Conformance.type_key = 'cim.2.activity.Conformance'
activity.DomainProperties.type_key = 'cim.2.activity.DomainProperties'
activity.Downscaling.type_key = 'cim.2.activity.Downscaling'
activity.Ensemble.type_key = 'cim.2.activity.Ensemble'
activity.EnsembleAxis.type_key = 'cim.2.activity.EnsembleAxis'
activity.EnsembleMember.type_key = 'cim.2.activity.EnsembleMember'
activity.EnsembleRequirement.type_key = 'cim.2.activity.EnsembleRequirement'
activity.ForcingConstraint.type_key = 'cim.2.activity.ForcingConstraint'
activity.MultiEnsemble.type_key = 'cim.2.activity.MultiEnsemble'
activity.MultiTimeEnsemble.type_key = 'cim.2.activity.MultiTimeEnsemble'
activity.NumericalExperiment.type_key = 'cim.2.activity.NumericalExperiment'
activity.NumericalRequirement.type_key = 'cim.2.activity.NumericalRequirement'
activity.OutputTemporalRequirement.type_key = 'cim.2.activity.OutputTemporalRequirement'
activity.ParentSimulation.type_key = 'cim.2.activity.ParentSimulation'
activity.Project.type_key = 'cim.2.activity.Project'
activity.Simulation.type_key = 'cim.2.activity.Simulation'
activity.SimulationPlan.type_key = 'cim.2.activity.SimulationPlan'
activity.TemporalConstraint.type_key = 'cim.2.activity.TemporalConstraint'
activity.UberEnsemble.type_key = 'cim.2.activity.UberEnsemble'
data.Dataset.type_key = 'cim.2.data.Dataset'
data.RelatedData.type_key = 'cim.2.data.RelatedData'
data.VariableCollection.type_key = 'cim.2.data.VariableCollection'
drs.DrsAtomicDataset.type_key = 'cim.2.drs.DrsAtomicDataset'
drs.DrsEnsembleIdentifier.type_key = 'cim.2.drs.DrsEnsembleIdentifier'
drs.DrsGeographicalIndicator.type_key = 'cim.2.drs.DrsGeographicalIndicator'
drs.DrsPublicationDataset.type_key = 'cim.2.drs.DrsPublicationDataset'
drs.DrsTemporalIdentifier.type_key = 'cim.2.drs.DrsTemporalIdentifier'
platform.ComponentPerformance.type_key = 'cim.2.platform.ComponentPerformance'
platform.ComputePool.type_key = 'cim.2.platform.ComputePool'
platform.Machine.type_key = 'cim.2.platform.Machine'
platform.Partition.type_key = 'cim.2.platform.Partition'
platform.Performance.type_key = 'cim.2.platform.Performance'
platform.StoragePool.type_key = 'cim.2.platform.StoragePool'
platform.StorageVolume.type_key = 'cim.2.platform.StorageVolume'
science.Algorithm.type_key = 'cim.2.science.Algorithm'
science.ConservationProperties.type_key = 'cim.2.science.ConservationProperties'
science.Extent.type_key = 'cim.2.science.Extent'
science.GridSummary.type_key = 'cim.2.science.GridSummary'
science.Process.type_key = 'cim.2.science.Process'
science.ProcessDetail.type_key = 'cim.2.science.ProcessDetail'
science.Resolution.type_key = 'cim.2.science.Resolution'
science.ScientificDomain.type_key = 'cim.2.science.ScientificDomain'
science.Tuning.type_key = 'cim.2.science.Tuning'
shared.Calendar.type_key = 'cim.2.shared.Calendar'
shared.CimLink.type_key = 'cim.2.shared.CimLink'
shared.Cimtext.type_key = 'cim.2.shared.Cimtext'
shared.Citation.type_key = 'cim.2.shared.Citation'
shared.DateTime.type_key = 'cim.2.shared.DateTime'
shared.DatetimeSet.type_key = 'cim.2.shared.DatetimeSet'
shared.IrregularDateset.type_key = 'cim.2.shared.IrregularDateset'
shared.KeyFloat.type_key = 'cim.2.shared.KeyFloat'
shared.Meta.type_key = 'cim.2.shared.Meta'
shared.MinimalMeta.type_key = 'cim.2.shared.MinimalMeta'
shared.NumberArray.type_key = 'cim.2.shared.NumberArray'
shared.OnlineResource.type_key = 'cim.2.shared.OnlineResource'
shared.Party.type_key = 'cim.2.shared.Party'
shared.Pid.type_key = 'cim.2.shared.Pid'
shared.Reference.type_key = 'cim.2.shared.Reference'
shared.RegularTimeset.type_key = 'cim.2.shared.RegularTimeset'
shared.Responsibility.type_key = 'cim.2.shared.Responsibility'
shared.StandaloneDocument.type_key = 'cim.2.shared.StandaloneDocument'
shared.TimePeriod.type_key = 'cim.2.shared.TimePeriod'
shared.TimesliceList.type_key = 'cim.2.shared.TimesliceList'
shared.VocabMember.type_key = 'cim.2.shared.VocabMember'
software.ComponentBase.type_key = 'cim.2.software.ComponentBase'
software.Composition.type_key = 'cim.2.software.Composition'
software.DevelopmentPath.type_key = 'cim.2.software.DevelopmentPath'
software.EntryPoint.type_key = 'cim.2.software.EntryPoint'
software.Gridspec.type_key = 'cim.2.software.Gridspec'
software.Model.type_key = 'cim.2.software.Model'
software.SoftwareComponent.type_key = 'cim.2.software.SoftwareComponent'
software.Variable.type_key = 'cim.2.software.Variable'


# Set type info (name, type, is_required, is_iterative).
activity.Activity.type_info = (
    ('duration', shared.TimePeriod, False, False),
    ('description', shared.Cimtext, False, False),
    ('canonical_name', str, False, False),
    ('name', str, True, False),
    ('keywords', str, False, True),
    ('rationale', shared.Cimtext, False, False),
    ('responsible_parties', shared.Responsibility, False, True),
    ('references', shared.Citation, False, True),
    ('meta', shared.Meta, True, False),
    ('long_name', str, False, False),
)

activity.AxisMember.type_info = (
    ('description', str, True, False),
    ('value', float, False, False),
    ('index', int, True, False),
)

activity.Conformance.type_info = (
    ('target_requirement', activity.NumericalRequirement, True, False),
)

activity.DomainProperties.type_info = (
    ('required_extent', science.Extent, False, False),
    ('required_resolution', science.Resolution, False, False),
)

activity.Downscaling.type_info = (
    ('downscaled_from', activity.Simulation, True, False),
)

activity.Ensemble.type_info = (
    ('part_of', activity.UberEnsemble, False, True),
    ('members', activity.EnsembleMember, True, True),
    ('supported', activity.NumericalExperiment, True, True),
    ('common_conformances', activity.Conformance, False, True),
    ('has_ensemble_axes', activity.EnsembleAxis, False, True),
)

activity.EnsembleAxis.type_info = (
    ('target_requirement', activity.NumericalRequirement, True, False),
    ('short_identifier', str, True, False),
    ('extra_detail', shared.Cimtext, True, False),
    ('member', activity.AxisMember, True, True),
)

activity.EnsembleMember.type_info = (
    ('simulation', activity.Simulation, True, False),
    ('had_performance', platform.Performance, False, False),
    ('ran_on', platform.Machine, True, False),
)

activity.EnsembleRequirement.type_info = (
    ('minimum_size', int, True, False),
    ('ensemble_member', activity.NumericalRequirement, False, True),
    ('ensemble_type', str, True, False),
)

activity.ForcingConstraint.type_info = (
    ('additional_constraint', shared.Cimtext, False, False),
    ('code', shared.VocabMember, True, False),
    ('category', shared.VocabMember, True, False),
    ('group', shared.VocabMember, False, False),
    ('data_link', shared.OnlineResource, False, False),
    ('origin', shared.Citation, False, False),
    ('forcing_type', str, True, False),
)

activity.MultiEnsemble.type_info = (
    ('ensemble_axis', activity.EnsembleRequirement, True, True),
)

activity.MultiTimeEnsemble.type_info = (
    ('ensemble_members', shared.DatetimeSet, True, False),
)

activity.NumericalExperiment.type_info = (
    ('requirements', activity.NumericalRequirement, False, True),
    ('related_experiments', activity.NumericalExperiment, False, True),
)

activity.NumericalRequirement.type_info = (
    ('additional_requirements', activity.NumericalRequirement, False, True),
    ('conformance_is_requested', bool, True, False),
)

activity.OutputTemporalRequirement.type_info = (
    ('continuous_subset', shared.TimePeriod, False, True),
    ('throughout', bool, True, False),
    ('sliced_subset', shared.TimesliceList, False, False),
)

activity.ParentSimulation.type_info = (
    ('branch_time_in_child', shared.DateTime, False, False),
    ('parent', activity.Simulation, True, False),
    ('branch_time_in_parent', shared.DateTime, False, False),
)

activity.Project.type_info = (
    ('sub_projects', activity.Project, False, True),
    ('previous_projects', activity.Project, False, True),
    ('requires_experiments', activity.NumericalExperiment, False, True),
)

activity.Simulation.type_info = (
    ('ensemble_identifier', str, True, False),
    ('run_for_experiments', activity.NumericalExperiment, True, True),
    ('parent_simulation', activity.ParentSimulation, False, False),
    ('primary_ensemble', activity.Ensemble, False, False),
    ('used', software.Model, True, False),
    ('part_of_project', activity.Project, True, True),
)

activity.SimulationPlan.type_info = (
    ('expected_model', software.Model, True, False),
    ('expected_platform', platform.Machine, False, False),
    ('will_support_experiments', activity.NumericalExperiment, True, True),
    ('expected_performance_sypd', float, False, False),
)

activity.TemporalConstraint.type_info = (
    ('start_date', shared.DateTime, False, False),
    ('required_calendar', shared.Calendar, False, False),
    ('start_flexibility', shared.TimePeriod, False, False),
    ('required_duration', shared.TimePeriod, False, False),
)

activity.UberEnsemble.type_info = (
    ('child_ensembles', activity.Ensemble, True, True),
)

data.Dataset.type_info = (
    ('dataset_author', shared.Party, False, True),
    ('meta', shared.Meta, True, False),
    ('drs_datasets', drs.DrsPublicationDataset, False, True),
    ('produced_by', activity.Simulation, False, False),
    ('description', str, False, False),
    ('related_to_dataset', data.RelatedData, False, True),
    ('name', str, True, False),
    ('availability', shared.OnlineResource, False, True),
    ('references', shared.Citation, False, True),
)

data.RelatedData.type_info = (
    ('other_dataset', data.Dataset, True, False),
    ('relationship', str, True, False),
)

data.VariableCollection.type_info = (
    ('collection_name', str, False, False),
    ('variables', str, True, True),
)

drs.DrsAtomicDataset.type_info = (
    ('mip_table', str, True, False),
    ('ensemble_member', drs.DrsEnsembleIdentifier, True, False),
    ('variable_name', str, True, False),
    ('temporal_constraint', drs.DrsTemporalIdentifier, False, False),
    ('geographical_constraint', drs.DrsGeographicalIndicator, False, False),
)

drs.DrsEnsembleIdentifier.type_info = (
    ('realisation_number', int, True, False),
    ('initialisation_method_number', int, True, False),
    ('perturbation_number', int, True, False),
)

drs.DrsGeographicalIndicator.type_info = (
    ('bounding_box', str, False, False),
    ('spatial_domain', str, False, False),
    ('operator', str, False, False),
)

drs.DrsPublicationDataset.type_info = (
    ('product', str, True, False),
    ('frequency', str, False, False),
    ('institute', str, True, False),
    ('realm', str, False, False),
    ('model', str, True, False),
    ('experiment', str, True, False),
    ('activity', str, True, False),
    ('version_number', int, False, False),
)

drs.DrsTemporalIdentifier.type_info = (
    ('suffix', str, False, False),
    ('end', str, False, False),
    ('start', str, True, False),
)

platform.ComponentPerformance.type_info = (
    ('cores_used', int, False, False),
    ('speed', float, True, False),
    ('nodes_used', int, False, False),
    ('component', software.SoftwareComponent, False, False),
    ('component_name', str, True, False),
)

platform.ComputePool.type_info = (
    ('memory_per_node', platform.StorageVolume, False, False),
    ('compute_cores_per_node', int, False, False),
    ('operating_system', str, False, False),
    ('cpu_type', str, False, False),
    ('accelerators_per_node', int, False, False),
    ('name', str, False, False),
    ('model_number', str, False, False),
    ('description', shared.Cimtext, False, False),
    ('interconnect', str, False, False),
    ('accelerator_type', str, False, False),
    ('number_of_nodes', int, False, False),
)

platform.Machine.type_info = (
    ('meta', shared.Meta, True, False),
)

platform.Partition.type_info = (
    ('model_number', str, False, False),
    ('vendor', shared.Party, False, False),
    ('storage_pools', platform.StoragePool, False, True),
    ('name', str, True, False),
    ('partition', platform.Partition, False, True),
    ('institution', shared.Party, True, False),
    ('when_used', shared.TimePeriod, False, False),
    ('compute_pools', platform.ComputePool, True, True),
    ('description', shared.Cimtext, False, False),
    ('online_documentation', shared.OnlineResource, False, True),
)

platform.Performance.type_info = (
    ('memory_bloat', float, False, False),
    ('compiler', str, False, False),
    ('total_nodes_used', int, False, False),
    ('model', software.Model, True, False),
    ('subcomponent_performance', platform.ComponentPerformance, False, False),
    ('coupler_load', float, False, False),
    ('asypd', float, False, False),
    ('meta', shared.Meta, True, False),
    ('load_imbalance', float, False, False),
    ('platform', platform.Machine, True, False),
    ('sypd', float, False, False),
    ('name', str, False, False),
    ('io_load', float, False, False),
    ('chsy', float, False, False),
)

platform.StoragePool.type_info = (
    ('description', shared.Cimtext, False, False),
    ('type', str, False, False),
    ('volume_available', platform.StorageVolume, True, False),
    ('vendor', shared.Party, False, False),
    ('name', str, True, False),
)

platform.StorageVolume.type_info = (
    ('units', str, True, False),
    ('volume', int, True, False),
)

science.Algorithm.type_info = (
    ('diagnostic_variables', data.VariableCollection, False, True),
    ('prognostic_variables', data.VariableCollection, False, True),
    ('references', shared.Citation, False, True),
    ('implementation_overview', shared.Cimtext, True, False),
    ('heading', str, True, False),
)

science.ConservationProperties.type_info = (
    ('flux_correction_was_used', bool, True, False),
    ('corrected_conserved_prognostic_variables', data.VariableCollection, False, False),
    ('correction_methodology', shared.Cimtext, False, False),
)

science.Extent.type_info = (
    ('southern_boundary', float, False, False),
    ('minimum_vertical_level', float, False, False),
    ('western_boundary', float, False, False),
    ('maximum_vertical_level', float, False, False),
    ('is_global', bool, True, False),
    ('eastern_boundary', float, False, False),
    ('z_units', str, True, False),
    ('northern_boundary', float, False, False),
    ('region_known_as', str, False, True),
)

science.GridSummary.type_info = (
    ('grid_extent', science.Extent, True, False),
    ('grid_type', str, True, False),
    ('grid_layout', str, True, False),
)

science.Process.type_info = (
    ('implementation_overview', shared.Cimtext, True, False),
    ('description', str, False, False),
    ('references', shared.Reference, False, True),
    ('algorithm_properties', science.Algorithm, False, True),
    ('detailed_properties', science.ProcessDetail, False, True),
    ('name', str, True, False),
    ('keywords', str, True, False),
    ('time_step_in_process', float, False, False),
)

science.ProcessDetail.type_info = (
    ('content', shared.Cimtext, False, False),
    ('properties', shared.KeyFloat, False, True),
    ('vocabulary', str, False, False),
    ('selection', str, False, True),
    ('heading', str, False, False),
)

science.Resolution.type_info = (
    ('equivalent_horizontal_resolution', float, True, False),
    ('number_of_levels', int, False, True),
    ('number_of_xy_gridpoints', int, False, True),
    ('name', str, True, False),
    ('is_adaptive_grid', bool, False, False),
)

science.ScientificDomain.type_info = (
    ('meta', shared.Meta, True, False),
    ('realm', str, False, False),
    ('simulates', science.Process, True, True),
    ('overview', shared.Cimtext, False, False),
    ('grid', science.GridSummary, False, False),
    ('extra_conservation_properties', science.ConservationProperties, False, False),
    ('resolution', science.Resolution, True, False),
    ('references', shared.Reference, False, True),
    ('name', str, True, False),
    ('time_step', float, True, False),
)

science.Tuning.type_info = (
    ('trend_metrics_used', data.VariableCollection, False, False),
    ('regional_metrics_used', data.VariableCollection, False, False),
    ('description', shared.Cimtext, True, False),
    ('global_mean_metrics_used', data.VariableCollection, False, False),
)

shared.Calendar.type_info = (
    ('description', str, False, False),
    ('name', str, False, False),
    ('cal_type', str, True, False),
    ('month_lengths', int, False, True),
)

shared.CimLink.type_info = (
    ('remote_type', str, True, False),
)

shared.Cimtext.type_info = (
    ('content', str, True, False),
    ('content_type', str, True, False),
)

shared.Citation.type_info = (
    ('doi', str, False, False),
    ('title', str, False, False),
    ('abstract', str, False, False),
    ('context', shared.Cimtext, False, False),
    ('citation_str', shared.Cimtext, True, False),
    ('url', shared.OnlineResource, False, False),
)

shared.DateTime.type_info = (
    ('offset', bool, False, False),
    ('value', str, True, False),
)

shared.DatetimeSet.type_info = (
    ('length', int, True, False),
)

shared.IrregularDateset.type_info = (
    ('date_set', str, True, False),
)

shared.KeyFloat.type_info = (
    ('key', str, True, False),
    ('value', float, True, False),
)

shared.Meta.type_info = (
    ('metadata_quality', str, False, False),
    ('metadata_author', shared.Party, True, False),
    ('metadata_reviewer', shared.Party, False, False),
    ('metadata_completeness', str, False, False),
)

shared.MinimalMeta.type_info = (
    ('document_version', int, False, False),
    ('uid', str, True, False),
    ('metadata_last_updated', datetime.datetime, True, False),
)

shared.NumberArray.type_info = (
    ('values', str, True, False),
)

shared.OnlineResource.type_info = (
    ('name', str, True, False),
    ('description', str, False, False),
    ('protocol', str, False, False),
    ('linkage', str, True, False),
)

shared.Party.type_info = (
    ('address', str, False, False),
    ('url', shared.OnlineResource, False, False),
    ('email', str, False, False),
    ('name', str, False, False),
    ('meta', shared.MinimalMeta, True, False),
    ('organisation', bool, False, False),
)

shared.Pid.type_info = (
    ('id', str, True, False),
    ('resolution_service', shared.OnlineResource, True, False),
)

shared.Reference.type_info = (
)

shared.RegularTimeset.type_info = (
    ('start_date', shared.DateTime, True, False),
    ('increment', shared.TimePeriod, True, False),
    ('length', int, True, False),
)

shared.Responsibility.type_info = (
    ('when', shared.TimePeriod, False, False),
    ('party', shared.Party, True, True),
    ('role', str, True, False),
)

shared.StandaloneDocument.type_info = (
    ('responsible_parties', shared.Responsibility, False, True),
    ('name', str, True, False),
    ('references', shared.Citation, False, True),
    ('long_name', str, False, False),
    ('meta', shared.Meta, True, False),
)

shared.TimePeriod.type_info = (
    ('units', str, True, False),
    ('calendar', shared.Calendar, False, False),
    ('date_type', str, True, False),
    ('length', int, True, False),
    ('date', shared.DateTime, False, False),
)

shared.TimesliceList.type_info = (
    ('members', shared.NumberArray, True, False),
    ('units', str, True, False),
)

shared.VocabMember.type_info = (
    ('uri', str, False, False),
    ('vocab', shared.Citation, False, False),
    ('value', str, True, False),
)

software.ComponentBase.type_info = (
    ('description', shared.Cimtext, False, False),
    ('name', str, True, False),
    ('documentation', shared.Citation, False, True),
    ('version', str, False, False),
    ('development_history', software.DevelopmentPath, False, False),
    ('long_name', str, False, False),
    ('release_date', datetime.datetime, False, False),
    ('tuning_applied', science.Tuning, False, False),
)

software.Composition.type_info = (
    ('couplings', str, False, True),
    ('description', str, False, False),
)

software.DevelopmentPath.type_info = (
    ('previous_version', str, False, False),
    ('consortium_name', str, False, False),
    ('developed_in_house', bool, True, False),
    ('funding_sources', shared.Responsibility, False, True),
    ('creators', shared.Responsibility, False, True),
)

software.EntryPoint.type_info = (
    ('name', str, False, False),
)

software.Gridspec.type_info = (
    ('description', str, True, False),
)

software.Model.type_info = (
    ('coupled_software_components', software.Model, False, True),
    ('meta', shared.Meta, True, False),
    ('coupler', str, False, False),
    ('internal_software_components', software.SoftwareComponent, False, True),
    ('category', str, True, False),
    ('scientific_domain', science.ScientificDomain, False, True),
    ('extra_conservation_properties', science.ConservationProperties, False, False),
)

software.SoftwareComponent.type_info = (
    ('dependencies', software.EntryPoint, False, True),
    ('license', str, False, False),
    ('grid', software.Gridspec, False, False),
    ('sub_components', software.SoftwareComponent, False, True),
    ('composition', software.Composition, False, False),
    ('connection_points', software.Variable, False, True),
    ('coupling_framework', str, False, False),
    ('language', str, False, False),
)

software.Variable.type_info = (
    ('description', str, False, False),
    ('prognostic', bool, True, False),
    ('name', str, True, False),
)

