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
    ('canonical_name', unicode, False, False),
    ('description', unicode, False, False),
    ('duration', shared.TimePeriod, False, False),
    ('keywords', unicode, False, True),
    ('long_name', unicode, False, False),
    ('meta', shared.Meta, True, False),
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
    ('common_conformances', activity.Conformance, False, True),
    ('has_ensemble_axes', activity.EnsembleAxis, False, True),
    ('members', activity.EnsembleMember, True, True),
    ('part_of', activity.UberEnsemble, False, True),
    ('supported', activity.NumericalExperiment, True, True),
)

activity.EnsembleAxis.type_info = (
    ('extra_detail', unicode, True, False),
    ('member', activity.AxisMember, True, True),
    ('short_identifier', unicode, True, False),
    ('target_requirement', activity.NumericalRequirement, True, False),
)

activity.EnsembleMember.type_info = (
    ('had_performance', platform.Performance, False, False),
    ('ran_on', platform.Machine, True, False),
    ('simulation', activity.Simulation, True, False),
)

activity.EnsembleRequirement.type_info = (
    ('ensemble_member', activity.NumericalRequirement, False, True),
    ('ensemble_type', unicode, True, False),
    ('minimum_size', int, True, False),
)

activity.ForcingConstraint.type_info = (
    ('additional_constraint', unicode, False, False),
    ('category', shared.VocabMember, True, False),
    ('code', shared.VocabMember, True, False),
    ('data_link', shared.OnlineResource, False, False),
    ('forcing_type', unicode, True, False),
    ('group', shared.VocabMember, False, False),
    ('origin', shared.Citation, False, False),
)

activity.MultiEnsemble.type_info = (
    ('ensemble_axis', activity.EnsembleRequirement, True, True),
)

activity.MultiTimeEnsemble.type_info = (
    ('ensemble_members', shared.DatetimeSet, True, False),
)

activity.NumericalExperiment.type_info = (
    ('related_experiments', activity.NumericalExperiment, False, True),
    ('requirements', activity.NumericalRequirement, False, True),
)

activity.NumericalRequirement.type_info = (
    ('additional_requirements', activity.NumericalRequirement, False, True),
    ('conformance_is_requested', bool, True, False),
)

activity.OutputTemporalRequirement.type_info = (
    ('continuous_subset', shared.TimePeriod, False, True),
    ('sliced_subset', shared.TimesliceList, False, False),
    ('throughout', bool, True, False),
)

activity.ParentSimulation.type_info = (
    ('branch_time_in_child', shared.DateTime, False, False),
    ('branch_time_in_parent', shared.DateTime, False, False),
    ('parent', activity.Simulation, True, False),
)

activity.Project.type_info = (
    ('previous_projects', activity.Project, False, True),
    ('requires_experiments', activity.NumericalExperiment, False, True),
    ('sub_projects', activity.Project, False, True),
)

activity.Simulation.type_info = (
    ('calendar', shared.Calendar, False, False),
    ('ensemble_identifier', unicode, True, False),
    ('parent_simulation', activity.ParentSimulation, False, False),
    ('part_of_project', activity.Project, True, True),
    ('primary_ensemble', activity.Ensemble, False, False),
    ('ran_for_experiments', activity.NumericalExperiment, True, True),
    ('used', software.Model, True, False),
)

activity.SimulationPlan.type_info = (
    ('expected_model', software.Model, True, False),
    ('expected_performance_sypd', float, False, False),
    ('expected_platform', platform.Machine, False, False),
    ('will_support_experiments', activity.NumericalExperiment, True, True),
)

activity.TemporalConstraint.type_info = (
    ('required_calendar', shared.Calendar, False, False),
    ('required_duration', shared.TimePeriod, False, False),
    ('start_date', shared.DateTime, False, False),
    ('start_flexibility', shared.TimePeriod, False, False),
)

activity.UberEnsemble.type_info = (
    ('child_ensembles', activity.Ensemble, True, True),
)

data.Dataset.type_info = (
    ('availability', shared.OnlineResource, False, True),
    ('description', unicode, False, False),
    ('drs_datasets', drs.DrsPublicationDataset, False, True),
    ('meta', shared.Meta, True, False),
    ('name', unicode, True, False),
    ('produced_by', activity.Simulation, False, False),
    ('references', shared.Citation, False, True),
    ('related_to_dataset', data.RelatedData, False, True),
    ('responsible_parties', shared.Responsibility, False, True),
)

data.RelatedData.type_info = (
    ('other_dataset', data.Dataset, True, False),
    ('relationship', unicode, True, False),
)

data.VariableCollection.type_info = (
    ('collection_name', unicode, False, False),
    ('variables', unicode, True, True),
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
    ('meta', shared.Meta, True, False),
)

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

platform.Performance.type_info = (
    ('asypd', float, False, False),
    ('chsy', float, False, False),
    ('compiler', unicode, False, False),
    ('coupler_load', float, False, False),
    ('io_load', float, False, False),
    ('load_imbalance', float, False, False),
    ('memory_bloat', float, False, False),
    ('meta', shared.Meta, True, False),
    ('model', software.Model, True, False),
    ('name', unicode, False, False),
    ('platform', platform.Machine, True, False),
    ('subcomponent_performance', platform.ComponentPerformance, False, False),
    ('sypd', float, False, False),
    ('total_nodes_used', int, False, False),
)

platform.StoragePool.type_info = (
    ('description', unicode, False, False),
    ('name', unicode, True, False),
    ('type', unicode, False, False),
    ('vendor', shared.Party, False, False),
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

science.Process.type_info = (
    ('algorithm_properties', science.Algorithm, False, True),
    ('description', unicode, False, False),
    ('detailed_properties', science.ProcessDetail, False, True),
    ('implementation_overview', unicode, True, False),
    ('keywords', unicode, True, False),
    ('name', unicode, True, False),
    ('references', shared.Reference, False, True),
    ('time_step_in_process', float, False, False),
)

science.ProcessDetail.type_info = (
    ('content', unicode, False, False),
    ('heading', unicode, False, False),
    ('properties', shared.KeyFloat, False, True),
    ('selection', unicode, False, True),
    ('vocabulary', unicode, False, False),
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
    ('meta', shared.Meta, True, False),
    ('name', unicode, True, False),
    ('overview', unicode, False, False),
    ('realm', unicode, False, False),
    ('references', shared.Reference, False, True),
    ('resolution', science.Resolution, True, False),
    ('simulates', science.Process, True, True),
    ('time_step', float, True, False),
)

science.Tuning.type_info = (
    ('description', unicode, True, False),
    ('global_mean_metrics_used', data.VariableCollection, False, False),
    ('regional_metrics_used', data.VariableCollection, False, False),
    ('trend_metrics_used', data.VariableCollection, False, False),
)

shared.Calendar.type_info = (
    ('cal_type', unicode, True, False),
    ('description', unicode, False, False),
    ('month_lengths', int, False, True),
    ('name', unicode, False, False),
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

shared.IrregularDateset.type_info = (
    ('date_set', unicode, True, False),
)

shared.KeyFloat.type_info = (
    ('key', unicode, True, False),
    ('value', float, True, False),
)

shared.Meta.type_info = (
    ('metadata_author', shared.Party, True, False),
    ('metadata_completeness', unicode, False, False),
    ('metadata_quality', unicode, False, False),
    ('metadata_reviewer', shared.Party, False, False),
)

shared.MinimalMeta.type_info = (
    ('document_version', int, False, False),
    ('metadata_last_updated', datetime.datetime, True, False),
    ('uid', unicode, True, False),
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
    ('meta', shared.MinimalMeta, True, False),
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
    ('role', unicode, True, False),
    ('when', shared.TimePeriod, False, False),
)

shared.StandaloneDocument.type_info = (
    ('long_name', unicode, False, False),
    ('meta', shared.Meta, True, False),
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
    ('tuning_applied', science.Tuning, False, False),
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

software.Model.type_info = (
    ('category', unicode, True, False),
    ('coupled_software_components', software.Model, False, True),
    ('coupler', unicode, False, False),
    ('extra_conservation_properties', science.ConservationProperties, False, False),
    ('internal_software_components', software.SoftwareComponent, False, True),
    ('meta', shared.Meta, True, False),
    ('scientific_domain', science.ScientificDomain, False, True),
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

