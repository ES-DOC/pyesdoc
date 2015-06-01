# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_meta.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encpasulates meta-information pertaining to the cim.v2 typeset.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-01 16:50:05.523857.

"""
import datetime
import uuid

import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_platform_package as platform
import typeset_for_shared_package as shared




# Set type keys.
activity.Activity.type_key = 'cim.2.activity.Activity'
activity.AxisMember.type_key = 'cim.2.activity.AxisMember'
activity.Configuration.type_key = 'cim.2.activity.Configuration'
activity.Conformance.type_key = 'cim.2.activity.Conformance'
activity.Ensemble.type_key = 'cim.2.activity.Ensemble'
activity.EnsembleRequirement.type_key = 'cim.2.activity.EnsembleRequirement'
activity.EnsembleRequirement.type_key = 'cim.2.activity.EnsembleRequirement'
activity.ForcingConstraint.type_key = 'cim.2.activity.ForcingConstraint'
activity.MemberDescription.type_key = 'cim.2.activity.MemberDescription'
activity.MultiEnsemble.type_key = 'cim.2.activity.MultiEnsemble'
activity.MultiTimeEnsemble.type_key = 'cim.2.activity.MultiTimeEnsemble'
activity.NumericalExperiment.type_key = 'cim.2.activity.NumericalExperiment'
activity.NumericalRequirement.type_key = 'cim.2.activity.NumericalRequirement'
activity.OutputTemporalRequirement.type_key = 'cim.2.activity.OutputTemporalRequirement'
activity.Project.type_key = 'cim.2.activity.Project'
activity.Simulation.type_key = 'cim.2.activity.Simulation'
activity.SimulationPlan.type_key = 'cim.2.activity.SimulationPlan'
activity.TemporalConstraint.type_key = 'cim.2.activity.TemporalConstraint'
data.Dataset.type_key = 'cim.2.data.Dataset'
platform.ComponentPerformance.type_key = 'cim.2.platform.ComponentPerformance'
platform.ComputePool.type_key = 'cim.2.platform.ComputePool'
platform.Machine.type_key = 'cim.2.platform.Machine'
platform.Partition.type_key = 'cim.2.platform.Partition'
platform.Performance.type_key = 'cim.2.platform.Performance'
platform.StoragePool.type_key = 'cim.2.platform.StoragePool'
platform.StorageVolume.type_key = 'cim.2.platform.StorageVolume'
shared.Calendar.type_key = 'cim.2.shared.Calendar'
shared.CimLink.type_key = 'cim.2.shared.CimLink'
shared.CimText.type_key = 'cim.2.shared.CimText'
shared.Citation.type_key = 'cim.2.shared.Citation'
shared.DateTime.type_key = 'cim.2.shared.DateTime'
shared.DatetimeSet.type_key = 'cim.2.shared.DatetimeSet'
shared.IrregularDateSet.type_key = 'cim.2.shared.IrregularDateSet'
shared.Meta.type_key = 'cim.2.shared.Meta'
shared.NumberArray.type_key = 'cim.2.shared.NumberArray'
shared.OnlineResource.type_key = 'cim.2.shared.OnlineResource'
shared.Party.type_key = 'cim.2.shared.Party'
shared.RegularTimeSet.type_key = 'cim.2.shared.RegularTimeSet'
shared.Responsibility.type_key = 'cim.2.shared.Responsibility'
shared.TimePeriod.type_key = 'cim.2.shared.TimePeriod'
shared.TimesliceList.type_key = 'cim.2.shared.TimesliceList'
shared.VocabMember.type_key = 'cim.2.shared.VocabMember'


# Set type info (name, type, is_required, is_iterative).
activity.Activity.type_info = (
    ('canonical_name', str, False, False),
    ('description', shared.CimText, False, False),
    ('duration', str, False, False),
    ('keywords', str, False, True),
    ('long_name', str, False, False),
    ('meta', shared.Meta, True, False),
    ('name', str, True, False),
    ('references', shared.Citation, False, True),
    ('responsible_parties', shared.Responsibility, False, True),
)

activity.AxisMember.type_info = (
    ('description', str, True, False),
    ('index', int, True, False),
    ('start_date', str, False, False),
    ('value', float, False, False),
)

activity.Configuration.type_info = (
    ('conformances', str, True, True),
    ('description', str, False, False),
)

activity.Conformance.type_info = (
    ('conformance_detail', shared.CimText, True, False),
    ('target_name', str, True, False),
    ('target_requirement', str, True, False),
)

activity.Ensemble.type_info = (
    ('i_defined_by', str, True, False),
    ('p_defined_by', str, True, False),
    ('r_defined_by', str, True, False),
    ('s_defined_by', str, False, False),
    ('simulations_include', str, True, True),
    ('supported', str, True, True),
)

activity.EnsembleRequirement.type_info = (
    ('ensemble_member', str, False, True),
    ('ensemble_type', str, True, False),
    ('minimum_size', int, True, False),
)

activity.EnsembleRequirement.type_info = (
    ('ensemble_member', str, False, True),
    ('ensemble_type', str, True, False),
    ('minimum_size', int, True, False),
)

activity.ForcingConstraint.type_info = (
    ('additional_constraint', shared.CimText, False, False),
    ('category', str, True, False),
    ('code', str, True, False),
    ('data_link', str, False, False),
    ('forcing_Type', str, True, False),
    ('group', str, False, False),
    ('origin', shared.Citation, False, False),
)

activity.MemberDescription.type_info = (
    ('axis', str, True, False),
    ('description', shared.CimText, False, False),
    ('member', activity.AxisMember, True, True),
)

activity.MultiEnsemble.type_info = (
    ('ensemble_axis', str, True, True),
)

activity.MultiTimeEnsemble.type_info = (
    ('ensemble_members', str, True, False),
)

activity.NumericalExperiment.type_info = (
    ('experiment_id', str, False, False),
    ('related_experiments', str, False, True),
    ('requirements', str, False, True),
)

activity.NumericalRequirement.type_info = (
    ('additional_requirements', str, False, True),
    ('was_conformance_requested', bool, True, False),
)

activity.OutputTemporalRequirement.type_info = (
    ('continuous_subset', str, False, True),
    ('sliced_subset', str, False, False),
    ('throughout', bool, True, False),
)

activity.Project.type_info = (
    ('previous_projects', str, False, True),
    ('required_experiments', str, False, True),
    ('sub_projects', str, False, True),
)

activity.Simulation.type_info = (
    ('conformed_via', str, False, False),
    ('had_performance', str, False, False),
    ('ran_on', str, False, False),
    ('supported', str, True, True),
    ('used', str, True, False),
)

activity.SimulationPlan.type_info = (
    ('expected_performance', str, False, False),
    ('experiments', str, True, True),
    ('machine', str, False, False),
    ('model', str, True, False),
)

activity.TemporalConstraint.type_info = (
    ('required_calendar', str, False, False),
    ('required_duration', str, False, False),
    ('start_date', str, False, False),
    ('start_flexibility', str, False, False),
)

data.Dataset.type_info = (
    ('availability', str, False, True),
    ('dataset_author', str, False, True),
    ('description', str, False, False),
    ('meta', shared.Meta, True, False),
    ('name', str, True, False),
    ('produced_by', str, False, False),
    ('references', shared.Citation, False, True),
    ('related_to_dataset', str, False, True),
)

platform.ComponentPerformance.type_info = (
    ('component', str, False, False),
    ('component_name', str, True, False),
    ('cores_used', int, False, False),
    ('nodes_used', int, False, False),
    ('speed', float, True, False),
)

platform.ComputePool.type_info = (
    ('CPU_type', str, False, False),
    ('accelerator_type', str, False, False),
    ('accelerators_per_node', int, False, False),
    ('compute_cores_per_node', int, False, False),
    ('description', shared.CimText, False, False),
    ('interconnect', str, False, False),
    ('memory_per_node', platform.StorageVolume, False, False),
    ('model_number', str, False, False),
    ('name', str, False, False),
    ('number_of_nodes', int, False, False),
    ('operating_system', str, False, False),
)

platform.Machine.type_info = (
    ('meta', shared.Meta, True, False),
)

platform.Partition.type_info = (
    ('compute_pool', str, True, True),
    ('description', shared.CimText, False, False),
    ('institution', str, True, False),
    ('model_number', str, False, False),
    ('name', str, True, False),
    ('online_documentation', str, False, True),
    ('partition', platform.Partition, False, True),
    ('storage_pool', str, False, True),
    ('vendor', str, False, False),
    ('when_used', str, False, False),
)

platform.Performance.type_info = (
    ('asypd', float, False, False),
    ('chsy', float, False, False),
    ('compiler', str, False, False),
    ('coupler_load', float, False, False),
    ('io_load', float, False, False),
    ('load_imbalance', float, False, False),
    ('memory_bloat', float, False, False),
    ('meta', shared.Meta, True, False),
    ('model', str, True, False),
    ('name', str, False, False),
    ('platform', str, True, False),
    ('subcomponent_performance', platform.ComponentPerformance, False, False),
    ('sypd', float, False, False),
    ('total_nodes_used', int, False, False),
)

platform.StoragePool.type_info = (
    ('description', shared.CimText, False, False),
    ('name', str, True, False),
    ('type', str, False, False),
    ('vendor', str, False, False),
    ('volume_available', platform.StorageVolume, True, False),
)

platform.StorageVolume.type_info = (
    ('units', str, True, False),
    ('volume', int, True, False),
)

shared.Calendar.type_info = (
    ('cal_type', str, True, False),
    ('description', str, False, False),
    ('month_lengths', int, False, True),
    ('name', str, False, False),
)

shared.CimLink.type_info = (
    ('remote_type', str, True, False),
)

shared.CimText.type_info = (
    ('content', str, True, False),
    ('content_type', str, True, False),
)

shared.Citation.type_info = (
    ('abstract', str, False, False),
    ('citation_str', str, True, False),
    ('description', str, False, False),
    ('doi', str, False, False),
    ('title', str, False, False),
    ('url', shared.OnlineResource, False, False),
)

shared.DateTime.type_info = (
    ('offset', bool, False, False),
    ('value', str, True, False),
)

shared.DatetimeSet.type_info = (
    ('length', int, True, False),
)

shared.IrregularDateSet.type_info = (
    ('date_set', str, True, False),
)

shared.Meta.type_info = (
    ('author', str, True, False),
    ('completeness', str, False, False),
    ('create_date', datetime.datetime, True, False),
    ('quality', str, False, False),
    ('uid', uuid.UUID, True, False),
    ('update_date', datetime.datetime, True, False),
    ('version', int, True, False),
)

shared.NumberArray.type_info = (
    ('values', str, True, False),
)

shared.OnlineResource.type_info = (
    ('description', str, False, False),
    ('linkage', str, True, False),
    ('name', str, True, False),
    ('protocol', str, False, False),
)

shared.Party.type_info = (
    ('address', str, False, False),
    ('email', str, False, False),
    ('meta', shared.Meta, True, False),
    ('name', str, False, False),
    ('organisation', bool, False, False),
    ('url', shared.OnlineResource, False, False),
)

shared.RegularTimeSet.type_info = (
    ('increment', str, True, False),
    ('length', int, True, False),
    ('start_date', str, True, False),
)

shared.Responsibility.type_info = (
    ('party', str, True, True),
    ('role', str, True, False),
    ('when', str, False, False),
)

shared.TimePeriod.type_info = (
    ('calendar', str, False, False),
    ('date', str, False, False),
    ('date_type', str, True, False),
    ('length', int, True, False),
    ('units', str, True, False),
)

shared.TimesliceList.type_info = (
    ('members', str, True, False),
    ('units', str, True, False),
)

shared.VocabMember.type_info = (
    ('uri', str, False, False),
    ('value', str, True, False),
    ('vocab', shared.Citation, False, False),
)

