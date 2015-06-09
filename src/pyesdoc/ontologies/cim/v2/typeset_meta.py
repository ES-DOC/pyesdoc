# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_meta.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encpasulates meta-information pertaining to the cim.v2 typeset.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-05 14:48:44.250539.

"""
import datetime
import uuid

import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_platform_package as platform
import typeset_for_shared_package as shared




# Set type keys.
shared.VocabMember.type_key = 'cim.2.shared.VocabMember'
activity.Simulation.type_key = 'cim.2.activity.Simulation'
data.Dataset.type_key = 'cim.2.data.Dataset'
shared.OnlineResource.type_key = 'cim.2.shared.OnlineResource'
shared.NumberArray.type_key = 'cim.2.shared.NumberArray'
activity.NumericalRequirement.type_key = 'cim.2.activity.NumericalRequirement'
shared.TimePeriod.type_key = 'cim.2.shared.TimePeriod'
platform.StoragePool.type_key = 'cim.2.platform.StoragePool'
activity.MultiTimeEnsemble.type_key = 'cim.2.activity.MultiTimeEnsemble'
activity.Ensemble.type_key = 'cim.2.activity.Ensemble'
shared.IrregularDateSet.type_key = 'cim.2.shared.IrregularDateSet'
activity.Project.type_key = 'cim.2.activity.Project'
activity.Activity.type_key = 'cim.2.activity.Activity'
activity.EnsembleRequirement.type_key = 'cim.2.activity.EnsembleRequirement'
activity.EnsembleRequirement.type_key = 'cim.2.activity.EnsembleRequirement'
shared.CimLink.type_key = 'cim.2.shared.CimLink'
shared.Calendar.type_key = 'cim.2.shared.Calendar'
shared.Citation.type_key = 'cim.2.shared.Citation'
activity.NumericalExperiment.type_key = 'cim.2.activity.NumericalExperiment'
activity.Conformance.type_key = 'cim.2.activity.Conformance'
shared.CimText.type_key = 'cim.2.shared.CimText'
platform.Partition.type_key = 'cim.2.platform.Partition'
shared.Responsibility.type_key = 'cim.2.shared.Responsibility'
activity.Configuration.type_key = 'cim.2.activity.Configuration'
shared.DateTime.type_key = 'cim.2.shared.DateTime'
platform.StorageVolume.type_key = 'cim.2.platform.StorageVolume'
shared.TimesliceList.type_key = 'cim.2.shared.TimesliceList'
shared.RegularTimeSet.type_key = 'cim.2.shared.RegularTimeSet'
platform.ComputePool.type_key = 'cim.2.platform.ComputePool'
activity.AxisMember.type_key = 'cim.2.activity.AxisMember'
platform.Machine.type_key = 'cim.2.platform.Machine'
activity.MultiEnsemble.type_key = 'cim.2.activity.MultiEnsemble'
activity.SimulationPlan.type_key = 'cim.2.activity.SimulationPlan'
platform.Performance.type_key = 'cim.2.platform.Performance'
activity.OutputTemporalRequirement.type_key = 'cim.2.activity.OutputTemporalRequirement'
platform.ComponentPerformance.type_key = 'cim.2.platform.ComponentPerformance'
shared.Party.type_key = 'cim.2.shared.Party'
shared.DatetimeSet.type_key = 'cim.2.shared.DatetimeSet'
activity.TemporalConstraint.type_key = 'cim.2.activity.TemporalConstraint'
shared.Meta.type_key = 'cim.2.shared.Meta'
activity.MemberDescription.type_key = 'cim.2.activity.MemberDescription'
activity.ForcingConstraint.type_key = 'cim.2.activity.ForcingConstraint'


# Set type info (name, type, is_required, is_iterative).
shared.VocabMember.type_info = (
    ('vocab', shared.Citation, False, False),
    ('uri', str, False, False),
    ('value', str, True, False),
)

activity.Simulation.type_info = (
    ('supported', str, True, True),
    ('used', str, True, False),
    ('ran_on', str, False, False),
    ('conformed_via', str, False, False),
    ('had_performance', str, False, False),
)

data.Dataset.type_info = (
    ('description', str, False, False),
    ('references', shared.Citation, False, True),
    ('dataset_author', str, False, True),
    ('meta', shared.Meta, True, False),
    ('name', str, True, False),
    ('related_to_dataset', str, False, True),
    ('produced_by', str, False, False),
    ('availability', str, False, True),
)

shared.OnlineResource.type_info = (
    ('protocol', str, False, False),
    ('description', str, False, False),
    ('name', str, True, False),
    ('linkage', str, True, False),
)

shared.NumberArray.type_info = (
    ('values', str, True, False),
)

activity.NumericalRequirement.type_info = (
    ('additional_requirements', str, False, True),
    ('was_conformance_requested', bool, True, False),
)

shared.TimePeriod.type_info = (
    ('calendar', str, False, False),
    ('date_type', str, True, False),
    ('units', str, True, False),
    ('length', int, True, False),
    ('date', str, False, False),
)

platform.StoragePool.type_info = (
    ('vendor', str, False, False),
    ('type', str, False, False),
    ('description', shared.CimText, False, False),
    ('volume_available', platform.StorageVolume, True, False),
    ('name', str, True, False),
)

activity.MultiTimeEnsemble.type_info = (
    ('ensemble_members', str, True, False),
)

activity.Ensemble.type_info = (
    ('s_defined_by', str, False, False),
    ('simulations_include', str, True, True),
    ('r_defined_by', str, True, False),
    ('i_defined_by', str, True, False),
    ('supported', str, True, True),
    ('p_defined_by', str, True, False),
)

shared.IrregularDateSet.type_info = (
    ('date_set', str, True, False),
)

activity.Project.type_info = (
    ('sub_projects', str, False, True),
    ('previous_projects', str, False, True),
    ('required_experiments', str, False, True),
)

activity.Activity.type_info = (
    ('references', shared.Citation, False, True),
    ('meta', shared.Meta, True, False),
    ('responsible_parties', shared.Responsibility, False, True),
    ('description', shared.CimText, False, False),
    ('long_name', str, False, False),
    ('name', str, True, False),
    ('keywords', str, False, True),
    ('canonical_name', str, False, False),
    ('duration', str, False, False),
)

activity.EnsembleRequirement.type_info = (
    ('ensemble_member', str, False, True),
    ('minimum_size', int, True, False),
    ('ensemble_type', str, True, False),
)

activity.EnsembleRequirement.type_info = (
    ('minimum_size', int, True, False),
    ('ensemble_member', str, False, True),
    ('ensemble_type', str, True, False),
)

shared.CimLink.type_info = (
    ('remote_type', str, True, False),
)

shared.Calendar.type_info = (
    ('month_lengths', int, False, True),
    ('name', str, False, False),
    ('cal_type', str, True, False),
    ('description', str, False, False),
)

shared.Citation.type_info = (
    ('abstract', str, False, False),
    ('title', str, False, False),
    ('url', shared.OnlineResource, False, False),
    ('description', str, False, False),
    ('citation_str', str, True, False),
    ('doi', str, False, False),
)

activity.NumericalExperiment.type_info = (
    ('experiment_id', str, False, False),
    ('requirements', str, False, True),
    ('related_experiments', str, False, True),
)

activity.Conformance.type_info = (
    ('conformance_detail', shared.CimText, True, False),
    ('target_requirement', str, True, False),
    ('target_name', str, True, False),
)

shared.CimText.type_info = (
    ('content', str, True, False),
    ('content_type', str, True, False),
)

platform.Partition.type_info = (
    ('storage_pool', str, False, True),
    ('institution', str, True, False),
    ('name', str, True, False),
    ('model_number', str, False, False),
    ('when_used', str, False, False),
    ('partition', platform.Partition, False, True),
    ('compute_pool', str, True, True),
    ('description', shared.CimText, False, False),
    ('online_documentation', str, False, True),
    ('vendor', str, False, False),
)

shared.Responsibility.type_info = (
    ('party', str, True, True),
    ('when', str, False, False),
    ('role', str, True, False),
)

activity.Configuration.type_info = (
    ('conformances', str, True, True),
    ('description', str, False, False),
)

shared.DateTime.type_info = (
    ('offset', bool, False, False),
    ('value', str, True, False),
)

platform.StorageVolume.type_info = (
    ('units', str, True, False),
    ('volume', int, True, False),
)

shared.TimesliceList.type_info = (
    ('members', str, True, False),
    ('units', str, True, False),
)

shared.RegularTimeSet.type_info = (
    ('increment', str, True, False),
    ('start_date', str, True, False),
    ('length', int, True, False),
)

platform.ComputePool.type_info = (
    ('operating_system', str, False, False),
    ('accelerators_per_node', int, False, False),
    ('name', str, False, False),
    ('model_number', str, False, False),
    ('interconnect', str, False, False),
    ('accelerator_type', str, False, False),
    ('compute_cores_per_node', int, False, False),
    ('number_of_nodes', int, False, False),
    ('memory_per_node', platform.StorageVolume, False, False),
    ('CPU_type', str, False, False),
    ('description', shared.CimText, False, False),
)

activity.AxisMember.type_info = (
    ('start_date', str, False, False),
    ('value', float, False, False),
    ('description', str, True, False),
    ('index', int, True, False),
)

platform.Machine.type_info = (
    ('meta', shared.Meta, True, False),
)

activity.MultiEnsemble.type_info = (
    ('ensemble_axis', str, True, True),
)

activity.SimulationPlan.type_info = (
    ('machine', str, False, False),
    ('model', str, True, False),
    ('expected_performance', str, False, False),
    ('experiments', str, True, True),
)

platform.Performance.type_info = (
    ('coupler_load', float, False, False),
    ('subcomponent_performance', platform.ComponentPerformance, False, False),
    ('name', str, False, False),
    ('io_load', float, False, False),
    ('compiler', str, False, False),
    ('model', str, True, False),
    ('asypd', float, False, False),
    ('platform', str, True, False),
    ('meta', shared.Meta, True, False),
    ('sypd', float, False, False),
    ('chsy', float, False, False),
    ('load_imbalance', float, False, False),
    ('memory_bloat', float, False, False),
    ('total_nodes_used', int, False, False),
)

activity.OutputTemporalRequirement.type_info = (
    ('continuous_subset', str, False, True),
    ('throughout', bool, True, False),
    ('sliced_subset', str, False, False),
)

platform.ComponentPerformance.type_info = (
    ('cores_used', int, False, False),
    ('speed', float, True, False),
    ('nodes_used', int, False, False),
    ('component', str, False, False),
    ('component_name', str, True, False),
)

shared.Party.type_info = (
    ('email', str, False, False),
    ('meta', shared.Meta, True, False),
    ('name', str, False, False),
    ('address', str, False, False),
    ('organisation', bool, False, False),
    ('url', shared.OnlineResource, False, False),
)

shared.DatetimeSet.type_info = (
    ('length', int, True, False),
)

activity.TemporalConstraint.type_info = (
    ('required_calendar', str, False, False),
    ('start_flexibility', str, False, False),
    ('required_duration', str, False, False),
    ('start_date', str, False, False),
)

shared.Meta.type_info = (
    ('uid', uuid.UUID, True, False),
    ('version', int, True, False),
    ('update_date', datetime.datetime, True, False),
    ('completeness', str, False, False),
    ('create_date', datetime.datetime, True, False),
    ('quality', str, False, False),
    ('author', str, True, False),
)

activity.MemberDescription.type_info = (
    ('member', activity.AxisMember, True, True),
    ('axis', str, True, False),
    ('description', shared.CimText, False, False),
)

activity.ForcingConstraint.type_info = (
    ('category', str, True, False),
    ('origin', shared.Citation, False, False),
    ('group', str, False, False),
    ('data_link', str, False, False),
    ('forcing_Type', str, True, False),
    ('code', str, True, False),
    ('additional_constraint', shared.CimText, False, False),
)

