
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.constraints.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The ontology constraint set.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import datetime
import uuid

import typeset_for_designing_package as designing
import typeset_for_data_package as data
import typeset_for_platform_package as platform
import typeset_for_drs_package as drs
import typeset_for_activity_package as activity
import typeset_for_software_package as software
import typeset_for_science_package as science
import typeset_for_shared_package as shared




# Map of ontology types to constraints.
CONSTRAINTS = {
    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    platform.Machine: (

        ('vendor', 'type', shared.Party),

        ('name', 'type', unicode),

        ('partition', 'type', platform.Partition),

        ('model_number', 'type', unicode),

        ('online_documentation', 'type', shared.OnlineResource),

        ('meta', 'type', shared.DocMetaInfo),

        ('storage_pools', 'type', platform.StoragePool),

        ('when_used', 'type', shared.TimePeriod),

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

    shared.Responsibility: (

        ('when', 'type', shared.TimePeriod),

        ('role', 'type', unicode),

        ('party', 'type', shared.Party),


        ('when', 'cardinality', "0.1"),

        ('role', 'cardinality', "1.1"),

        ('party', 'cardinality', "1.N"),



    ),

    science.Tuning: (

        ('regional_metrics_used', 'type', data.VariableCollection),

        ('trend_metrics_used', 'type', data.VariableCollection),

        ('description', 'type', unicode),

        ('global_mean_metrics_used', 'type', data.VariableCollection),


        ('regional_metrics_used', 'cardinality', "0.1"),

        ('trend_metrics_used', 'cardinality', "0.1"),

        ('description', 'cardinality', "1.1"),

        ('global_mean_metrics_used', 'cardinality', "0.1"),



    ),

    shared.RegularTimeset: (

        ('length', 'type', int),

        ('start_date', 'type', shared.DateTime),

        ('increment', 'type', shared.TimePeriod),


        ('length', 'cardinality', "1.1"),

        ('start_date', 'cardinality', "1.1"),

        ('increment', 'cardinality', "1.1"),



    ),

    platform.ComponentPerformance: (

        ('speed', 'type', float),

        ('component_name', 'type', unicode),

        ('component', 'type', software.SoftwareComponent),

        ('cores_used', 'type', int),

        ('nodes_used', 'type', int),


        ('speed', 'cardinality', "1.1"),

        ('component_name', 'cardinality', "1.1"),

        ('component', 'cardinality', "0.1"),

        ('cores_used', 'cardinality', "0.1"),

        ('nodes_used', 'cardinality', "0.1"),



    ),

    shared.Pid: (

        ('resolution_service', 'type', shared.OnlineResource),

        ('id', 'type', unicode),


        ('resolution_service', 'cardinality', "1.1"),

        ('id', 'cardinality', "1.1"),



    ),

    drs.DrsAtomicDataset: (

        ('product', 'type', unicode),

        ('realm', 'type', unicode),

        ('experiment', 'type', unicode),

        ('institute', 'type', unicode),

        ('geographical_constraint', 'type', drs.DrsGeographicalIndicator),

        ('version_number', 'type', int),

        ('mip_table', 'type', unicode),

        ('variable_name', 'type', unicode),

        ('frequency', 'type', unicode),

        ('activity', 'type', unicode),

        ('ensemble_member', 'type', drs.DrsEnsembleIdentifier),

        ('model', 'type', unicode),

        ('temporal_constraint', 'type', drs.DrsTemporalIdentifier),


        ('version_number', 'cardinality', "1.1"),

        ('realm', 'cardinality', "1.1"),

        ('institute', 'cardinality', "1.1"),

        ('geographical_constraint', 'cardinality', "0.1"),

        ('product', 'cardinality', "1.1"),

        ('mip_table', 'cardinality', "1.1"),

        ('variable_name', 'cardinality', "1.1"),

        ('experiment', 'cardinality', "1.1"),

        ('frequency', 'cardinality', "1.1"),

        ('activity', 'cardinality', "1.1"),

        ('ensemble_member', 'cardinality', "1.1"),

        ('model', 'cardinality', "1.1"),

        ('temporal_constraint', 'cardinality', "0.1"),



    ),

    designing.NumericalRequirement: (

        ('description', 'type', unicode),

        ('keywords', 'type', unicode),

        ('additional_requirements', 'type', designing.NumericalRequirement),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('conformance_is_requested', 'type', bool),

        ('name', 'type', unicode),


        ('description', 'cardinality', "0.1"),

        ('keywords', 'cardinality', "0.N"),

        ('additional_requirements', 'cardinality', "0.N"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('rationale', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.0"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('name', 'cardinality', "1.1"),



    ),

    science.Detail: (

        ('name', 'type', unicode),

        ('from_vocab', 'type', unicode),

        ('content', 'type', unicode),

        ('detail_selection', 'type', unicode),

        ('context', 'type', unicode),

        ('id', 'type', unicode),

        ('select', 'type', unicode),

        ('with_cardinality', 'type', unicode),


        ('name', 'cardinality', "1.1"),

        ('from_vocab', 'cardinality', "0.1"),

        ('content', 'cardinality', "0.1"),

        ('detail_selection', 'cardinality', "0.N"),

        ('context', 'cardinality', "1.1"),

        ('id', 'cardinality', "1.1"),

        ('select', 'cardinality', "0.1"),

        ('with_cardinality', 'cardinality', "0.1"),



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

    activity.Ensemble: (

        ('part_of', 'type', activity.UberEnsemble),

        ('supported', 'type', designing.NumericalExperiment),

        ('description', 'type', unicode),

        ('documentation', 'type', shared.OnlineResource),

        ('common_conformances', 'type', activity.Conformance),

        ('keywords', 'type', unicode),

        ('responsible_parties', 'type', shared.Responsibility),

        ('members', 'type', activity.EnsembleMember),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('has_ensemble_axes', 'type', activity.EnsembleAxis),

        ('name', 'type', unicode),


        ('part_of', 'cardinality', "0.N"),

        ('common_conformances', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('long_name', 'cardinality', "0.1"),

        ('documentation', 'cardinality', "0.N"),

        ('supported', 'cardinality', "1.N"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('members', 'cardinality', "1.N"),

        ('keywords', 'cardinality', "0.0"),

        ('canonical_name', 'cardinality', "0.0"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('rationale', 'cardinality', "0.0"),

        ('duration', 'cardinality', "0.0"),

        ('has_ensemble_axes', 'cardinality', "0.N"),

        ('name', 'cardinality', "1.1"),



    ),

    shared.IrregularDateset: (

        ('length', 'type', int),

        ('date_set', 'type', unicode),


        ('length', 'cardinality', "1.1"),

        ('date_set', 'cardinality', "1.1"),



    ),

    platform.StorageVolume: (

        ('units', 'type', unicode),

        ('volume', 'type', int),


        ('units', 'cardinality', "1.1"),

        ('volume', 'cardinality', "1.1"),



    ),

    software.EntryPoint: (

        ('name', 'type', unicode),


        ('name', 'cardinality', "0.1"),



    ),

    drs.DrsEnsembleIdentifier: (

        ('perturbation_number', 'type', int),

        ('initialisation_method_number', 'type', int),

        ('realisation_number', 'type', int),


        ('perturbation_number', 'cardinality', "1.1"),

        ('initialisation_method_number', 'cardinality', "1.1"),

        ('realisation_number', 'cardinality', "1.1"),



    ),

    shared.Calendar: (

        ('standard_name', 'type', unicode),

        ('description', 'type', unicode),

        ('month_lengths', 'type', int),

        ('name', 'type', unicode),


        ('standard_name', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),

        ('month_lengths', 'cardinality', "0.N"),

        ('name', 'cardinality', "0.1"),



    ),

    software.Gridspec: (

        ('description', 'type', unicode),


        ('description', 'cardinality', "1.1"),



    ),

    science.ScienceContext: (

        ('id', 'type', unicode),

        ('context', 'type', unicode),

        ('name', 'type', unicode),


        ('id', 'cardinality', "1.1"),

        ('context', 'cardinality', "1.1"),

        ('name', 'cardinality', "1.1"),



    ),

    data.Downscaling: (

        ('ensemble_identifier', 'type', unicode),

        ('used', 'type', science.Model),

        ('description', 'type', unicode),

        ('part_of_project', 'type', designing.Project),

        ('duration', 'type', shared.TimePeriod),

        ('parent_simulation', 'type', activity.ParentSimulation),

        ('primary_ensemble', 'type', activity.Ensemble),

        ('downscaled_from', 'type', data.Simulation),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('ran_for_experiments', 'type', designing.NumericalExperiment),

        ('rationale', 'type', unicode),

        ('keywords', 'type', unicode),

        ('calendar', 'type', shared.Calendar),

        ('name', 'type', unicode),


        ('ensemble_identifier', 'cardinality', "1.1"),

        ('used', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),

        ('part_of_project', 'cardinality', "1.N"),

        ('duration', 'cardinality', "0.1"),

        ('parent_simulation', 'cardinality', "0.0"),

        ('primary_ensemble', 'cardinality', "0.1"),

        ('downscaled_from', 'cardinality', "1.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('ran_for_experiments', 'cardinality', "1.N"),

        ('rationale', 'cardinality', "0.0"),

        ('keywords', 'cardinality', "0.N"),

        ('calendar', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),



    ),

    designing.MultiTimeEnsemble: (

        ('ensemble_members', 'type', shared.DatetimeSet),

        ('description', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('additional_requirements', 'type', designing.NumericalRequirement),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('keywords', 'type', unicode),

        ('conformance_is_requested', 'type', bool),

        ('name', 'type', unicode),


        ('ensemble_members', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.0"),

        ('additional_requirements', 'cardinality', "0.0"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('rationale', 'cardinality', "0.1"),

        ('keywords', 'cardinality', "0.N"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('name', 'cardinality', "1.1"),



    ),

    shared.KeyFloat: (

        ('value', 'type', float),

        ('key', 'type', unicode),


        ('value', 'cardinality', "1.1"),

        ('key', 'cardinality', "1.1"),



    ),

    shared.ExternalDocument: (

        ('doi', 'type', unicode),

        ('name', 'type', unicode),

        ('title', 'type', unicode),

        ('publication_detail', 'type', unicode),

        ('online_at', 'type', shared.OnlineResource),

        ('meta', 'type', shared.DocMetaInfo),

        ('date', 'type', unicode),

        ('authorship', 'type', unicode),


        ('doi', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

        ('title', 'cardinality', "1.1"),

        ('publication_detail', 'cardinality', "0.1"),

        ('online_at', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('date', 'cardinality', "0.1"),

        ('authorship', 'cardinality', "0.1"),



    ),

    designing.EnsembleRequirement: (

        ('minimum_size', 'type', int),

        ('description', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('additional_requirements', 'type', designing.NumericalRequirement),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('ensemble_type', 'type', unicode),

        ('rationale', 'type', unicode),

        ('keywords', 'type', unicode),

        ('ensemble_member', 'type', designing.NumericalRequirement),

        ('conformance_is_requested', 'type', bool),

        ('name', 'type', unicode),


        ('minimum_size', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.0"),

        ('additional_requirements', 'cardinality', "0.0"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('ensemble_type', 'cardinality', "1.1"),

        ('rationale', 'cardinality', "0.1"),

        ('keywords', 'cardinality', "0.N"),

        ('ensemble_member', 'cardinality', "0.N"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('name', 'cardinality', "1.1"),



    ),

    science.ScientificDomain: (

        ('simulates', 'type', science.Process),

        ('differing_key_properties', 'type', science.KeyProperties),

        ('name', 'type', unicode),

        ('overview', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('realm', 'type', unicode),

        ('id', 'type', unicode),


        ('simulates', 'cardinality', "1.N"),

        ('differing_key_properties', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

        ('overview', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('realm', 'cardinality', "0.1"),

        ('id', 'cardinality', "0.1"),



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

    software.ComponentBase: (

        ('name', 'type', unicode),

        ('repository', 'type', shared.OnlineResource),

        ('release_date', 'type', datetime.datetime),

        ('documentation', 'type', shared.Reference),

        ('development_history', 'type', software.DevelopmentPath),

        ('long_name', 'type', unicode),

        ('version', 'type', unicode),

        ('description', 'type', unicode),


        ('name', 'cardinality', "1.1"),

        ('repository', 'cardinality', "0.1"),

        ('release_date', 'cardinality', "0.1"),

        ('documentation', 'cardinality', "0.N"),

        ('development_history', 'cardinality', "0.1"),

        ('long_name', 'cardinality', "0.1"),

        ('version', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



    ),

    designing.NumericalExperiment: (

        ('requirements', 'type', designing.NumericalRequirement),

        ('description', 'type', unicode),

        ('keywords', 'type', unicode),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('related_experiments', 'type', designing.NumericalExperiment),

        ('duration', 'type', shared.TimePeriod),

        ('name', 'type', unicode),


        ('requirements', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('keywords', 'cardinality', "0.N"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('rationale', 'cardinality', "1.1"),

        ('related_experiments', 'cardinality', "0.N"),

        ('duration', 'cardinality', "0.0"),

        ('name', 'cardinality', "1.1"),



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

    science.KeyProperties: (

        ('extra_conservation_properties', 'type', science.ConservationProperties),

        ('additional_detail', 'type', science.Detail),

        ('grid', 'type', science.Grid),

        ('tuning_applied', 'type', science.Tuning),

        ('time_step', 'type', float),

        ('resolution', 'type', science.Resolution),


        ('extra_conservation_properties', 'cardinality', "0.1"),

        ('additional_detail', 'cardinality', "0.N"),

        ('grid', 'cardinality', "1.1"),

        ('tuning_applied', 'cardinality', "0.1"),

        ('time_step', 'cardinality', "1.1"),

        ('resolution', 'cardinality', "1.1"),



    ),

    drs.DrsTemporalIdentifier: (

        ('start', 'type', unicode),

        ('end', 'type', unicode),

        ('suffix', 'type', unicode),


        ('start', 'cardinality', "1.1"),

        ('end', 'cardinality', "0.1"),

        ('suffix', 'cardinality', "0.1"),



    ),

    designing.ForcingConstraint: (

        ('category', 'type', unicode),

        ('origin', 'type', shared.Reference),

        ('code', 'type', unicode),

        ('group', 'type', unicode),

        ('description', 'type', unicode),

        ('data_link', 'type', shared.OnlineResource),

        ('duration', 'type', shared.TimePeriod),

        ('additional_requirements', 'type', designing.NumericalRequirement),

        ('responsible_parties', 'type', shared.Responsibility),

        ('forcing_type', 'type', unicode),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('keywords', 'type', unicode),

        ('conformance_is_requested', 'type', bool),

        ('additional_constraint', 'type', unicode),

        ('name', 'type', unicode),


        ('category', 'cardinality', "0.1"),

        ('origin', 'cardinality', "0.1"),

        ('code', 'cardinality', "0.1"),

        ('group', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('data_link', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.0"),

        ('additional_requirements', 'cardinality', "0.0"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('forcing_type', 'cardinality', "1.1"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('rationale', 'cardinality', "0.1"),

        ('keywords', 'cardinality', "0.N"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('additional_constraint', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),



    ),

    shared.TimePeriod: (

        ('date', 'type', shared.DateTime),

        ('units', 'type', unicode),

        ('calendar', 'type', shared.Calendar),

        ('length', 'type', int),

        ('date_type', 'type', unicode),


        ('date', 'cardinality', "0.1"),

        ('units', 'cardinality', "1.1"),

        ('calendar', 'cardinality', "0.1"),

        ('length', 'cardinality', "1.1"),

        ('date_type', 'cardinality', "1.1"),



    ),

    software.Composition: (

        ('couplings', 'type', unicode),

        ('description', 'type', unicode),


        ('couplings', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),



    ),

    drs.DrsGeographicalIndicator: (

        ('operator', 'type', unicode),

        ('bounding_box', 'type', unicode),

        ('spatial_domain', 'type', unicode),


        ('operator', 'cardinality', "0.1"),

        ('bounding_box', 'cardinality', "0.1"),

        ('spatial_domain', 'cardinality', "0.1"),



    ),

    science.Algorithm: (

        ('name', 'type', unicode),

        ('diagnostic_variables', 'type', data.VariableCollection),

        ('prognostic_variables', 'type', data.VariableCollection),

        ('references', 'type', shared.Reference),

        ('context', 'type', unicode),

        ('implementation_overview', 'type', unicode),

        ('forced_variables', 'type', data.VariableCollection),

        ('id', 'type', unicode),


        ('name', 'cardinality', "1.1"),

        ('diagnostic_variables', 'cardinality', "0.1"),

        ('prognostic_variables', 'cardinality', "0.1"),

        ('references', 'cardinality', "0.N"),

        ('context', 'cardinality', "1.1"),

        ('implementation_overview', 'cardinality', "1.1"),

        ('forced_variables', 'cardinality', "0.1"),

        ('id', 'cardinality', "1.1"),



    ),

    data.Simulation: (

        ('ensemble_identifier', 'type', unicode),

        ('parent_simulation', 'type', activity.ParentSimulation),

        ('description', 'type', unicode),

        ('part_of_project', 'type', designing.Project),

        ('keywords', 'type', unicode),

        ('primary_ensemble', 'type', activity.Ensemble),

        ('responsible_parties', 'type', shared.Responsibility),

        ('used', 'type', science.Model),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('ran_for_experiments', 'type', designing.NumericalExperiment),

        ('rationale', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('calendar', 'type', shared.Calendar),

        ('name', 'type', unicode),


        ('ensemble_identifier', 'cardinality', "1.1"),

        ('parent_simulation', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('part_of_project', 'cardinality', "1.N"),

        ('keywords', 'cardinality', "0.N"),

        ('primary_ensemble', 'cardinality', "0.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('used', 'cardinality', "1.1"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('ran_for_experiments', 'cardinality', "1.N"),

        ('rationale', 'cardinality', "0.0"),

        ('duration', 'cardinality', "0.1"),

        ('calendar', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),



    ),

    science.Process: (

        ('name', 'type', unicode),

        ('sub_processes', 'type', science.SubProcess),

        ('properties', 'type', science.Detail),

        ('algorithms', 'type', science.Algorithm),

        ('context', 'type', unicode),

        ('implementation_overview', 'type', unicode),

        ('keywords', 'type', unicode),

        ('references', 'type', shared.Reference),

        ('id', 'type', unicode),


        ('name', 'cardinality', "1.1"),

        ('sub_processes', 'cardinality', "0.N"),

        ('properties', 'cardinality', "0.N"),

        ('algorithms', 'cardinality', "0.N"),

        ('context', 'cardinality', "1.1"),

        ('implementation_overview', 'cardinality', "1.1"),

        ('keywords', 'cardinality', "0.1"),

        ('references', 'cardinality', "0.N"),

        ('id', 'cardinality', "1.1"),



    ),

    science.Grid: (

        ('horizontal_grid_layout', 'type', unicode),

        ('name', 'type', unicode),

        ('grid_extent', 'type', science.Extent),

        ('horizontal_grid_type', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('vertical_grid_type', 'type', unicode),

        ('additional_details', 'type', science.Detail),

        ('vertical_grid_layout', 'type', unicode),


        ('horizontal_grid_layout', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

        ('grid_extent', 'cardinality', "0.1"),

        ('horizontal_grid_type', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('vertical_grid_type', 'cardinality', "0.1"),

        ('additional_details', 'cardinality', "0.N"),

        ('vertical_grid_layout', 'cardinality', "0.1"),



    ),

    designing.OutputTemporalRequirement: (

        ('throughout', 'type', bool),

        ('description', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('continuous_subset', 'type', shared.TimePeriod),

        ('additional_requirements', 'type', designing.NumericalRequirement),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('sliced_subset', 'type', shared.TimesliceList),

        ('rationale', 'type', unicode),

        ('keywords', 'type', unicode),

        ('conformance_is_requested', 'type', bool),

        ('name', 'type', unicode),


        ('throughout', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.0"),

        ('continuous_subset', 'cardinality', "0.N"),

        ('additional_requirements', 'cardinality', "0.0"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('sliced_subset', 'cardinality', "0.1"),

        ('rationale', 'cardinality', "0.1"),

        ('keywords', 'cardinality', "0.N"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('name', 'cardinality', "1.1"),



    ),

    science.Extent: (

        ('is_global', 'type', bool),

        ('bottom_vertical_level', 'type', float),

        ('eastern_boundary', 'type', float),

        ('southern_boundary', 'type', float),

        ('northern_boundary', 'type', float),

        ('region_known_as', 'type', unicode),

        ('top_vertical_level', 'type', float),

        ('z_units', 'type', unicode),

        ('western_boundary', 'type', float),


        ('is_global', 'cardinality', "1.1"),

        ('bottom_vertical_level', 'cardinality', "0.1"),

        ('eastern_boundary', 'cardinality', "0.1"),

        ('southern_boundary', 'cardinality', "0.1"),

        ('northern_boundary', 'cardinality', "0.1"),

        ('region_known_as', 'cardinality', "0.N"),

        ('top_vertical_level', 'cardinality', "0.1"),

        ('z_units', 'cardinality', "1.1"),

        ('western_boundary', 'cardinality', "0.1"),



    ),

    shared.DatetimeSet: (

        ('length', 'type', int),


        ('length', 'cardinality', "1.1"),



    ),

    designing.DomainProperties: (

        ('required_resolution', 'type', science.Resolution),

        ('description', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('additional_requirements', 'type', designing.NumericalRequirement),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('required_extent', 'type', science.Extent),

        ('rationale', 'type', unicode),

        ('keywords', 'type', unicode),

        ('conformance_is_requested', 'type', bool),

        ('name', 'type', unicode),


        ('required_resolution', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.0"),

        ('additional_requirements', 'cardinality', "0.0"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('required_extent', 'cardinality', "0.1"),

        ('rationale', 'cardinality', "0.1"),

        ('keywords', 'cardinality', "0.N"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('name', 'cardinality', "1.1"),



    ),

    science.Model: (

        ('category', 'type', unicode),

        ('simulates', 'type', science.ScientificDomain),

        ('model_default_properties', 'type', science.KeyProperties),

        ('name', 'type', unicode),

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

        ('description', 'type', unicode),


        ('category', 'cardinality', "1.1"),

        ('simulates', 'cardinality', "0.N"),

        ('model_default_properties', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

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

        ('description', 'cardinality', "0.1"),



    ),

    shared.DateTime: (

        ('value', 'type', unicode),

        ('offset', 'type', bool),


        ('value', 'cardinality', "1.1"),

        ('offset', 'cardinality', "0.1"),



    ),

    shared.NumberArray: (

        ('values', 'type', unicode),


        ('values', 'cardinality', "1.1"),



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

    activity.UberEnsemble: (

        ('child_ensembles', 'type', activity.Ensemble),

        ('part_of', 'type', activity.UberEnsemble),

        ('common_conformances', 'type', activity.Conformance),

        ('description', 'type', unicode),

        ('rationale', 'type', unicode),

        ('supported', 'type', designing.NumericalExperiment),

        ('responsible_parties', 'type', shared.Responsibility),

        ('name', 'type', unicode),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('members', 'type', activity.EnsembleMember),

        ('keywords', 'type', unicode),

        ('has_ensemble_axes', 'type', activity.EnsembleAxis),

        ('duration', 'type', shared.TimePeriod),

        ('documentation', 'type', shared.OnlineResource),


        ('child_ensembles', 'cardinality', "1.N"),

        ('part_of', 'cardinality', "0.N"),

        ('common_conformances', 'cardinality', "0.0"),

        ('description', 'cardinality', "0.1"),

        ('rationale', 'cardinality', "0.0"),

        ('documentation', 'cardinality', "0.N"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('supported', 'cardinality', "1.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.0"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('members', 'cardinality', "0.0"),

        ('keywords', 'cardinality', "0.0"),

        ('has_ensemble_axes', 'cardinality', "1.N"),

        ('duration', 'cardinality', "0.0"),

        ('name', 'cardinality', "1.1"),



    ),

    science.ConservationProperties: (

        ('corrected_conserved_prognostic_variables', 'type', data.VariableCollection),

        ('flux_correction_was_used', 'type', bool),

        ('correction_methodology', 'type', unicode),


        ('corrected_conserved_prognostic_variables', 'cardinality', "0.1"),

        ('flux_correction_was_used', 'cardinality', "1.1"),

        ('correction_methodology', 'cardinality', "0.1"),



    ),

    platform.Partition: (

        ('vendor', 'type', shared.Party),

        ('name', 'type', unicode),

        ('partition', 'type', platform.Partition),

        ('model_number', 'type', unicode),

        ('online_documentation', 'type', shared.OnlineResource),

        ('storage_pools', 'type', platform.StoragePool),

        ('when_used', 'type', shared.TimePeriod),

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

    software.DevelopmentPath: (

        ('consortium_name', 'type', unicode),

        ('funding_sources', 'type', shared.Responsibility),

        ('developed_in_house', 'type', bool),

        ('previous_version', 'type', unicode),

        ('creators', 'type', shared.Responsibility),


        ('consortium_name', 'cardinality', "0.1"),

        ('funding_sources', 'cardinality', "0.N"),

        ('developed_in_house', 'cardinality', "1.1"),

        ('previous_version', 'cardinality', "0.1"),

        ('creators', 'cardinality', "0.N"),



    ),

    shared.TimesliceList: (

        ('units', 'type', unicode),

        ('members', 'type', shared.NumberArray),


        ('units', 'cardinality', "1.1"),

        ('members', 'cardinality', "1.1"),



    ),

    platform.ComputePool: (

        ('operating_system', 'type', unicode),

        ('number_of_nodes', 'type', int),

        ('name', 'type', unicode),

        ('memory_per_node', 'type', platform.StorageVolume),

        ('model_number', 'type', unicode),

        ('compute_cores_per_node', 'type', int),

        ('accelerator_type', 'type', unicode),

        ('cpu_type', 'type', unicode),

        ('interconnect', 'type', unicode),

        ('accelerators_per_node', 'type', int),

        ('description', 'type', unicode),


        ('operating_system', 'cardinality', "0.1"),

        ('number_of_nodes', 'cardinality', "0.1"),

        ('name', 'cardinality', "0.1"),

        ('memory_per_node', 'cardinality', "0.1"),

        ('model_number', 'cardinality', "0.1"),

        ('compute_cores_per_node', 'cardinality', "0.1"),

        ('accelerator_type', 'cardinality', "0.1"),

        ('cpu_type', 'cardinality', "0.1"),

        ('interconnect', 'cardinality', "0.1"),

        ('accelerators_per_node', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



    ),

    designing.TemporalConstraint: (

        ('description', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('required_duration', 'type', shared.TimePeriod),

        ('additional_requirements', 'type', designing.NumericalRequirement),

        ('responsible_parties', 'type', shared.Responsibility),

        ('start_date', 'type', shared.DateTime),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('start_flexibility', 'type', shared.TimePeriod),

        ('keywords', 'type', unicode),

        ('conformance_is_requested', 'type', bool),

        ('required_calendar', 'type', shared.Calendar),

        ('name', 'type', unicode),


        ('description', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.0"),

        ('required_duration', 'cardinality', "0.1"),

        ('additional_requirements', 'cardinality', "0.0"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('start_date', 'cardinality', "0.1"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('rationale', 'cardinality', "0.1"),

        ('start_flexibility', 'cardinality', "0.1"),

        ('keywords', 'cardinality', "0.N"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('required_calendar', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),



    ),

    science.Resolution: (

        ('number_of_levels', 'type', int),

        ('name', 'type', unicode),

        ('equivalent_resolution_km', 'type', float),

        ('typical_y_degrees', 'type', float),

        ('number_of_xy_gridpoints', 'type', int),

        ('is_adaptive_grid', 'type', bool),

        ('typical_x_degrees', 'type', float),


        ('number_of_levels', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

        ('equivalent_resolution_km', 'cardinality', "0.1"),

        ('typical_y_degrees', 'cardinality', "0.1"),

        ('number_of_xy_gridpoints', 'cardinality', "0.1"),

        ('is_adaptive_grid', 'cardinality', "0.1"),

        ('typical_x_degrees', 'cardinality', "0.1"),



    ),

    activity.ParentSimulation: (

        ('branch_time_in_parent', 'type', shared.DateTime),

        ('branch_time_in_child', 'type', shared.DateTime),

        ('parent', 'type', data.Simulation),


        ('branch_time_in_parent', 'cardinality', "0.1"),

        ('branch_time_in_child', 'cardinality', "0.1"),

        ('parent', 'cardinality', "1.1"),



    ),

    shared.DocMetaInfo: (

        ('drs_keys', 'type', unicode),

        ('drs_path', 'type', unicode),

        ('create_date', 'type', datetime.datetime),

        ('language', 'type', unicode),

        ('update_date', 'type', datetime.datetime),

        ('institute', 'type', unicode),

        ('author', 'type', shared.Party),

        ('source_key', 'type', unicode),

        ('project', 'type', unicode),

        ('sort_key', 'type', unicode),

        ('version', 'type', int),

        ('source', 'type', unicode),

        ('type_sort_key', 'type', unicode),

        ('external_ids', 'type', unicode),

        ('type', 'type', unicode),

        ('id', 'type', unicode),

        ('type_display_name', 'type', unicode),


        ('drs_keys', 'cardinality', "0.N"),

        ('drs_path', 'cardinality', "0.1"),

        ('create_date', 'cardinality', "1.1"),

        ('language', 'cardinality', "1.1"),

        ('update_date', 'cardinality', "1.1"),

        ('institute', 'cardinality', "0.1"),

        ('author', 'cardinality', "0.1"),

        ('source_key', 'cardinality', "0.1"),

        ('project', 'cardinality', "1.1"),

        ('sort_key', 'cardinality', "0.1"),

        ('version', 'cardinality', "1.1"),

        ('source', 'cardinality', "1.1"),

        ('type_sort_key', 'cardinality', "0.1"),

        ('external_ids', 'cardinality', "0.N"),

        ('type', 'cardinality', "1.1"),

        ('id', 'cardinality', "1.1"),

        ('type_display_name', 'cardinality', "0.1"),



    ),

    designing.SimulationPlan: (

        ('expected_performance_sypd', 'type', float),

        ('description', 'type', unicode),

        ('keywords', 'type', unicode),

        ('expected_model', 'type', science.Model),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('expected_platform', 'type', platform.Machine),

        ('will_support_experiments', 'type', designing.NumericalExperiment),

        ('name', 'type', unicode),


        ('expected_performance_sypd', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('keywords', 'cardinality', "0.N"),

        ('expected_model', 'cardinality', "1.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('rationale', 'cardinality', "0.1"),

        ('duration', 'cardinality', "1.1"),

        ('expected_platform', 'cardinality', "0.1"),

        ('will_support_experiments', 'cardinality', "1.N"),

        ('name', 'cardinality', "1.1"),



    ),

    drs.DrsPublicationDataset: (

        ('product', 'type', unicode),

        ('realm', 'type', unicode),

        ('experiment', 'type', unicode),

        ('institute', 'type', unicode),

        ('version_number', 'type', int),

        ('frequency', 'type', unicode),

        ('activity', 'type', unicode),

        ('model', 'type', unicode),


        ('product', 'cardinality', "1.1"),

        ('realm', 'cardinality', "0.1"),

        ('experiment', 'cardinality', "1.1"),

        ('institute', 'cardinality', "1.1"),

        ('version_number', 'cardinality', "0.1"),

        ('frequency', 'cardinality', "0.1"),

        ('activity', 'cardinality', "1.1"),

        ('model', 'cardinality', "1.1"),



    ),

    data.Dataset: (

        ('related_to_dataset', 'type', shared.OnlineResource),

        ('description', 'type', unicode),

        ('produced_by', 'type', data.Simulation),

        ('drs_datasets', 'type', drs.DrsPublicationDataset),

        ('responsible_parties', 'type', shared.Responsibility),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('availability', 'type', shared.OnlineResource),

        ('name', 'type', unicode),


        ('related_to_dataset', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('produced_by', 'cardinality', "0.1"),

        ('drs_datasets', 'cardinality', "0.N"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('availability', 'cardinality', "0.N"),

        ('name', 'cardinality', "1.1"),



    ),

    designing.MultiEnsemble: (

        ('ensemble_axis', 'type', designing.EnsembleRequirement),

        ('description', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('additional_requirements', 'type', designing.NumericalRequirement),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('keywords', 'type', unicode),

        ('conformance_is_requested', 'type', bool),

        ('name', 'type', unicode),


        ('ensemble_axis', 'cardinality', "1.N"),

        ('description', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.0"),

        ('additional_requirements', 'cardinality', "0.0"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('rationale', 'cardinality', "0.1"),

        ('keywords', 'cardinality', "0.N"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('name', 'cardinality', "1.1"),



    ),

    science.SubProcess: (

        ('name', 'type', unicode),

        ('id', 'type', unicode),

        ('references', 'type', shared.Reference),

        ('context', 'type', unicode),

        ('implementation_overview', 'type', unicode),

        ('properties', 'type', science.Detail),


        ('name', 'cardinality', "1.1"),

        ('id', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('context', 'cardinality', "1.1"),

        ('implementation_overview', 'cardinality', "1.1"),

        ('properties', 'cardinality', "0.N"),



    ),

    activity.Conformance: (

        ('description', 'type', unicode),

        ('keywords', 'type', unicode),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('target_requirement', 'type', designing.NumericalRequirement),

        ('name', 'type', unicode),


        ('description', 'cardinality', "1.1"),

        ('long_name', 'cardinality', "0.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('duration', 'cardinality', "0.0"),

        ('canonical_name', 'cardinality', "0.0"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('rationale', 'cardinality', "0.0"),

        ('keywords', 'cardinality', "0.0"),

        ('target_requirement', 'cardinality', "1.1"),

        ('name', 'cardinality', "1.1"),



    ),

    shared.Reference: (

        ('document', 'type', shared.ExternalDocument),

        ('context', 'type', unicode),


        ('document', 'cardinality', "1.1"),

        ('context', 'cardinality', "0.1"),



    ),

    software.SoftwareComponent: (

        ('license', 'type', unicode),

        ('coupling_framework', 'type', unicode),

        ('name', 'type', unicode),

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

        ('description', 'type', unicode),


        ('license', 'cardinality', "0.1"),

        ('coupling_framework', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

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

        ('description', 'cardinality', "0.1"),



    ),

    platform.StoragePool: (

        ('type', 'type', unicode),

        ('volume_available', 'type', platform.StorageVolume),

        ('vendor', 'type', shared.Party),

        ('description', 'type', unicode),

        ('name', 'type', unicode),


        ('type', 'cardinality', "0.1"),

        ('volume_available', 'cardinality', "1.1"),

        ('vendor', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),



    ),

    platform.Performance: (

        ('io_load', 'type', float),

        ('asypd', 'type', float),

        ('memory_bloat', 'type', float),

        ('name', 'type', unicode),

        ('subcomponent_performance', 'type', platform.ComponentPerformance),

        ('total_nodes_used', 'type', int),

        ('chsy', 'type', float),

        ('sypd', 'type', float),

        ('platform', 'type', platform.Machine),

        ('meta', 'type', shared.DocMetaInfo),

        ('load_imbalance', 'type', float),

        ('coupler_load', 'type', float),

        ('model', 'type', science.Model),

        ('compiler', 'type', unicode),


        ('io_load', 'cardinality', "0.1"),

        ('asypd', 'cardinality', "0.1"),

        ('memory_bloat', 'cardinality', "0.1"),

        ('name', 'cardinality', "0.1"),

        ('subcomponent_performance', 'cardinality', "0.1"),

        ('total_nodes_used', 'cardinality', "0.1"),

        ('chsy', 'cardinality', "0.1"),

        ('sypd', 'cardinality', "0.1"),

        ('platform', 'cardinality', "1.1"),

        ('meta', 'cardinality', "1.1"),

        ('load_imbalance', 'cardinality', "0.1"),

        ('coupler_load', 'cardinality', "0.1"),

        ('model', 'cardinality', "1.1"),

        ('compiler', 'cardinality', "0.1"),



    ),

    activity.Activity: (

        ('description', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('keywords', 'type', unicode),

        ('name', 'type', unicode),


        ('description', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('rationale', 'cardinality', "0.1"),

        ('keywords', 'cardinality', "0.N"),

        ('name', 'cardinality', "1.1"),



    ),

    designing.Project: (

        ('requires_experiments', 'type', designing.NumericalExperiment),

        ('description', 'type', unicode),

        ('keywords', 'type', unicode),

        ('previous_projects', 'type', designing.Project),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('sub_projects', 'type', designing.Project),

        ('name', 'type', unicode),


        ('requires_experiments', 'cardinality', "0.N"),

        ('description', 'cardinality', "1.1"),

        ('keywords', 'cardinality', "0.N"),

        ('previous_projects', 'cardinality', "0.N"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('rationale', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.1"),

        ('sub_projects', 'cardinality', "0.N"),

        ('name', 'cardinality', "1.1"),



    ),

    shared.Cimtext: (

        ('content', 'type', unicode),

        ('content_type', 'type', unicode),


        ('content', 'cardinality', "1.1"),

        ('content_type', 'cardinality', "1.1"),



    ),

    shared.QualityReview: (

        ('date', 'type', unicode),

        ('quality_status', 'type', unicode),

        ('metadata_reviewer', 'type', shared.Party),

        ('quality_description', 'type', unicode),


        ('date', 'cardinality', "1.1"),

        ('quality_status', 'cardinality', "0.1"),

        ('metadata_reviewer', 'cardinality', "1.1"),

        ('quality_description', 'cardinality', "1.1"),



    ),

    activity.EnsembleMember: (

        ('simulation', 'type', data.Simulation),

        ('variant_id', 'type', unicode),

        ('errata', 'type', shared.OnlineResource),

        ('had_performance', 'type', platform.Performance),

        ('ran_on', 'type', platform.Machine),


        ('simulation', 'cardinality', "1.1"),

        ('variant_id', 'cardinality', "1.1"),

        ('errata', 'cardinality', "0.1"),

        ('had_performance', 'cardinality', "0.1"),

        ('ran_on', 'cardinality', "0.1"),



    ),

    software.Variable: (

        ('name', 'type', unicode),

        ('prognostic', 'type', bool),

        ('description', 'type', unicode),


        ('name', 'cardinality', "1.1"),

        ('prognostic', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),



    ),

    data.VariableCollection: (

        ('collection_name', 'type', unicode),

        ('variables', 'type', unicode),


        ('collection_name', 'cardinality', "0.1"),

        ('variables', 'cardinality', "1.N"),



    ),

    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------


    (platform.Machine, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (platform.Machine, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.Machine, 'storage_pools'): (

        ('type', platform.StoragePool),


        ('cardinality', "0.N"),



    ),

    (platform.Machine, 'partition'): (

        ('type', platform.Partition),


        ('cardinality', "0.N"),



    ),

    (platform.Machine, 'online_documentation'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.N"),



    ),

    (platform.Machine, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (platform.Machine, 'institution'): (

        ('type', shared.Party),


        ('cardinality', "1.1"),



    ),

    (platform.Machine, 'vendor'): (

        ('type', shared.Party),


        ('cardinality', "0.1"),



    ),

    (platform.Machine, 'when_used'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.1"),



    ),

    (platform.Machine, 'model_number'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.Machine, 'compute_pools'): (

        ('type', platform.ComputePool),


        ('cardinality', "1.N"),



    ),



    (shared.Responsibility, 'role'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.Responsibility, 'when'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.1"),



    ),

    (shared.Responsibility, 'party'): (

        ('type', shared.Party),


        ('cardinality', "1.N"),



    ),



    (science.Tuning, 'global_mean_metrics_used'): (

        ('type', data.VariableCollection),


        ('cardinality', "0.1"),



    ),

    (science.Tuning, 'description'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Tuning, 'regional_metrics_used'): (

        ('type', data.VariableCollection),


        ('cardinality', "0.1"),



    ),

    (science.Tuning, 'trend_metrics_used'): (

        ('type', data.VariableCollection),


        ('cardinality', "0.1"),



    ),



    (shared.RegularTimeset, 'length'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (shared.RegularTimeset, 'increment'): (

        ('type', shared.TimePeriod),


        ('cardinality', "1.1"),



    ),

    (shared.RegularTimeset, 'length'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (shared.RegularTimeset, 'start_date'): (

        ('type', shared.DateTime),


        ('cardinality', "1.1"),



    ),



    (platform.ComponentPerformance, 'component'): (

        ('type', software.SoftwareComponent),


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

    (platform.ComponentPerformance, 'component_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (platform.ComponentPerformance, 'cores_used'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),



    (shared.Pid, 'id'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.Pid, 'resolution_service'): (

        ('type', shared.OnlineResource),


        ('cardinality', "1.1"),



    ),



    (drs.DrsAtomicDataset, 'geographical_constraint'): (

        ('type', drs.DrsGeographicalIndicator),


        ('cardinality', "0.1"),



    ),

    (drs.DrsAtomicDataset, 'frequency'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsAtomicDataset, 'variable_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsAtomicDataset, 'realm'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsAtomicDataset, 'experiment'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsAtomicDataset, 'mip_table'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsAtomicDataset, 'institute'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsAtomicDataset, 'version_number'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (drs.DrsAtomicDataset, 'ensemble_member'): (

        ('type', drs.DrsEnsembleIdentifier),


        ('cardinality', "1.1"),



    ),

    (drs.DrsAtomicDataset, 'activity'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsAtomicDataset, 'model'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsAtomicDataset, 'product'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsAtomicDataset, 'temporal_constraint'): (

        ('type', drs.DrsTemporalIdentifier),


        ('cardinality', "0.1"),



    ),



    (designing.NumericalRequirement, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.0"),



    ),

    (designing.NumericalRequirement, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (designing.NumericalRequirement, 'rationale'): (

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

    (designing.NumericalRequirement, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.NumericalRequirement, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "0.N"),



    ),

    (designing.NumericalRequirement, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (designing.NumericalRequirement, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (designing.NumericalRequirement, 'conformance_is_requested'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (designing.NumericalRequirement, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.NumericalRequirement, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (science.Detail, 'context'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Detail, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Detail, 'from_vocab'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Detail, 'select'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Detail, 'content'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Detail, 'id'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Detail, 'with_cardinality'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Detail, 'detail_selection'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),



    (shared.OnlineResource, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.OnlineResource, 'protocol'): (

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



    (activity.Ensemble, 'supported'): (

        ('type', designing.NumericalExperiment),


        ('cardinality', "1.N"),



    ),

    (activity.Ensemble, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Ensemble, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.0"),



    ),

    (activity.Ensemble, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Ensemble, 'common_conformances'): (

        ('type', activity.Conformance),


        ('cardinality', "0.N"),



    ),

    (activity.Ensemble, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.Ensemble, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.0"),



    ),

    (activity.Ensemble, 'documentation'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.N"),



    ),

    (activity.Ensemble, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.0"),



    ),

    (activity.Ensemble, 'has_ensemble_axes'): (

        ('type', activity.EnsembleAxis),


        ('cardinality', "0.N"),



    ),

    (activity.Ensemble, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (activity.Ensemble, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.0"),



    ),

    (activity.Ensemble, 'members'): (

        ('type', activity.EnsembleMember),


        ('cardinality', "1.N"),



    ),

    (activity.Ensemble, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (activity.Ensemble, 'part_of'): (

        ('type', activity.UberEnsemble),


        ('cardinality', "0.N"),



    ),

    (activity.Ensemble, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),



    (shared.IrregularDateset, 'date_set'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.IrregularDateset, 'length'): (

        ('type', int),


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



    (software.EntryPoint, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (drs.DrsEnsembleIdentifier, 'perturbation_number'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (drs.DrsEnsembleIdentifier, 'realisation_number'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (drs.DrsEnsembleIdentifier, 'initialisation_method_number'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),



    (shared.Calendar, 'month_lengths'): (

        ('type', int),


        ('cardinality', "0.N"),



    ),

    (shared.Calendar, 'standard_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.Calendar, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Calendar, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (software.Gridspec, 'description'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (science.ScienceContext, 'context'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.ScienceContext, 'id'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.ScienceContext, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (data.Downscaling, 'calendar'): (

        ('type', shared.Calendar),


        ('cardinality', "0.1"),



    ),

    (data.Downscaling, 'primary_ensemble'): (

        ('type', activity.Ensemble),


        ('cardinality', "0.1"),



    ),

    (data.Downscaling, 'downscaled_from'): (

        ('type', data.Simulation),


        ('cardinality', "1.1"),



    ),

    (data.Downscaling, 'ensemble_identifier'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (data.Downscaling, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.Downscaling, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.Downscaling, 'parent_simulation'): (

        ('type', activity.ParentSimulation),


        ('cardinality', "0.0"),



    ),

    (data.Downscaling, 'part_of_project'): (

        ('type', designing.Project),


        ('cardinality', "1.N"),



    ),

    (data.Downscaling, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (data.Downscaling, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.Downscaling, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.0"),



    ),

    (data.Downscaling, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (data.Downscaling, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (data.Downscaling, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (data.Downscaling, 'ran_for_experiments'): (

        ('type', designing.NumericalExperiment),


        ('cardinality', "1.N"),



    ),

    (data.Downscaling, 'used'): (

        ('type', science.Model),


        ('cardinality', "1.1"),



    ),

    (data.Downscaling, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.1"),



    ),

    (data.Downscaling, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),



    (designing.MultiTimeEnsemble, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.MultiTimeEnsemble, 'conformance_is_requested'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (designing.MultiTimeEnsemble, 'ensemble_members'): (

        ('type', shared.DatetimeSet),


        ('cardinality', "1.1"),



    ),

    (designing.MultiTimeEnsemble, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (designing.MultiTimeEnsemble, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.MultiTimeEnsemble, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.MultiTimeEnsemble, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "0.0"),



    ),

    (designing.MultiTimeEnsemble, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.MultiTimeEnsemble, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (designing.MultiTimeEnsemble, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (designing.MultiTimeEnsemble, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.0"),



    ),

    (designing.MultiTimeEnsemble, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.MultiTimeEnsemble, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),



    (shared.KeyFloat, 'key'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.KeyFloat, 'value'): (

        ('type', float),


        ('cardinality', "1.1"),



    ),



    (shared.ExternalDocument, 'authorship'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ExternalDocument, 'date'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ExternalDocument, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.ExternalDocument, 'publication_detail'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ExternalDocument, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (shared.ExternalDocument, 'online_at'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.1"),



    ),

    (shared.ExternalDocument, 'title'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.ExternalDocument, 'doi'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (designing.EnsembleRequirement, 'minimum_size'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (designing.EnsembleRequirement, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.EnsembleRequirement, 'conformance_is_requested'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (designing.EnsembleRequirement, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (designing.EnsembleRequirement, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (designing.EnsembleRequirement, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (designing.EnsembleRequirement, 'ensemble_member'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "0.N"),



    ),

    (designing.EnsembleRequirement, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.EnsembleRequirement, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "0.0"),



    ),

    (designing.EnsembleRequirement, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.EnsembleRequirement, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (designing.EnsembleRequirement, 'ensemble_type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.EnsembleRequirement, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.0"),



    ),

    (designing.EnsembleRequirement, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.EnsembleRequirement, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (science.ScientificDomain, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.ScientificDomain, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (science.ScientificDomain, 'realm'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.ScientificDomain, 'differing_key_properties'): (

        ('type', science.KeyProperties),


        ('cardinality', "0.1"),



    ),

    (science.ScientificDomain, 'id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.ScientificDomain, 'overview'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.ScientificDomain, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (science.ScientificDomain, 'simulates'): (

        ('type', science.Process),


        ('cardinality', "1.N"),



    ),



    (activity.EnsembleAxis, 'member'): (

        ('type', activity.AxisMember),


        ('cardinality', "1.N"),



    ),

    (activity.EnsembleAxis, 'extra_detail'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.EnsembleAxis, 'target_requirement'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "1.1"),



    ),

    (activity.EnsembleAxis, 'short_identifier'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (software.ComponentBase, 'documentation'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (software.ComponentBase, 'repository'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.1"),



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

    (software.ComponentBase, 'version'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ComponentBase, 'development_history'): (

        ('type', software.DevelopmentPath),


        ('cardinality', "0.1"),



    ),

    (software.ComponentBase, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (designing.NumericalExperiment, 'related_experiments'): (

        ('type', designing.NumericalExperiment),


        ('cardinality', "0.N"),



    ),

    (designing.NumericalExperiment, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.0"),



    ),

    (designing.NumericalExperiment, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (designing.NumericalExperiment, 'rationale'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.NumericalExperiment, 'requirements'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "0.N"),



    ),

    (designing.NumericalExperiment, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (designing.NumericalExperiment, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.NumericalExperiment, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (designing.NumericalExperiment, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (designing.NumericalExperiment, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.NumericalExperiment, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.NumericalExperiment, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (shared.DocReference, 'context'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocReference, 'linkage'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocReference, 'constraint_vocabulary'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'protocol'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocReference, 'version'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'relationship'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (science.KeyProperties, 'time_step'): (

        ('type', float),


        ('cardinality', "1.1"),



    ),

    (science.KeyProperties, 'extra_conservation_properties'): (

        ('type', science.ConservationProperties),


        ('cardinality', "0.1"),



    ),

    (science.KeyProperties, 'grid'): (

        ('type', science.Grid),


        ('cardinality', "1.1"),



    ),

    (science.KeyProperties, 'tuning_applied'): (

        ('type', science.Tuning),


        ('cardinality', "0.1"),



    ),

    (science.KeyProperties, 'resolution'): (

        ('type', science.Resolution),


        ('cardinality', "1.1"),



    ),

    (science.KeyProperties, 'additional_detail'): (

        ('type', science.Detail),


        ('cardinality', "0.N"),



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



    (designing.ForcingConstraint, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (designing.ForcingConstraint, 'additional_constraint'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.ForcingConstraint, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.ForcingConstraint, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "0.0"),



    ),

    (designing.ForcingConstraint, 'description'): (

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

    (designing.ForcingConstraint, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.ForcingConstraint, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.ForcingConstraint, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.ForcingConstraint, 'conformance_is_requested'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (designing.ForcingConstraint, 'data_link'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.1"),



    ),

    (designing.ForcingConstraint, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (designing.ForcingConstraint, 'forcing_type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.ForcingConstraint, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.0"),



    ),

    (designing.ForcingConstraint, 'group'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.ForcingConstraint, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (designing.ForcingConstraint, 'origin'): (

        ('type', shared.Reference),


        ('cardinality', "0.1"),



    ),

    (designing.ForcingConstraint, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),



    (shared.TimePeriod, 'calendar'): (

        ('type', shared.Calendar),


        ('cardinality', "0.1"),



    ),

    (shared.TimePeriod, 'date'): (

        ('type', shared.DateTime),


        ('cardinality', "0.1"),



    ),

    (shared.TimePeriod, 'length'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (shared.TimePeriod, 'date_type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.TimePeriod, 'units'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (software.Composition, 'couplings'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (software.Composition, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (drs.DrsGeographicalIndicator, 'spatial_domain'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (drs.DrsGeographicalIndicator, 'bounding_box'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (drs.DrsGeographicalIndicator, 'operator'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (science.Algorithm, 'forced_variables'): (

        ('type', data.VariableCollection),


        ('cardinality', "0.1"),



    ),

    (science.Algorithm, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Algorithm, 'context'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Algorithm, 'implementation_overview'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Algorithm, 'prognostic_variables'): (

        ('type', data.VariableCollection),


        ('cardinality', "0.1"),



    ),

    (science.Algorithm, 'id'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Algorithm, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (science.Algorithm, 'diagnostic_variables'): (

        ('type', data.VariableCollection),


        ('cardinality', "0.1"),



    ),



    (data.Simulation, 'calendar'): (

        ('type', shared.Calendar),


        ('cardinality', "0.1"),



    ),

    (data.Simulation, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.0"),



    ),

    (data.Simulation, 'ensemble_identifier'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (data.Simulation, 'long_name'): (

        ('type', unicode),


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

    (data.Simulation, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (data.Simulation, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (data.Simulation, 'primary_ensemble'): (

        ('type', activity.Ensemble),


        ('cardinality', "0.1"),



    ),

    (data.Simulation, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (data.Simulation, 'ran_for_experiments'): (

        ('type', designing.NumericalExperiment),


        ('cardinality', "1.N"),



    ),

    (data.Simulation, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (data.Simulation, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.1"),



    ),

    (data.Simulation, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (data.Simulation, 'used'): (

        ('type', science.Model),


        ('cardinality', "1.1"),



    ),

    (data.Simulation, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.Simulation, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (science.Process, 'context'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Process, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Process, 'algorithms'): (

        ('type', science.Algorithm),


        ('cardinality', "0.N"),



    ),

    (science.Process, 'implementation_overview'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Process, 'id'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Process, 'sub_processes'): (

        ('type', science.SubProcess),


        ('cardinality', "0.N"),



    ),

    (science.Process, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Process, 'properties'): (

        ('type', science.Detail),


        ('cardinality', "0.N"),



    ),

    (science.Process, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),



    (science.Grid, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Grid, 'grid_extent'): (

        ('type', science.Extent),


        ('cardinality', "0.1"),



    ),

    (science.Grid, 'horizontal_grid_layout'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Grid, 'additional_details'): (

        ('type', science.Detail),


        ('cardinality', "0.N"),



    ),

    (science.Grid, 'vertical_grid_type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Grid, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (science.Grid, 'vertical_grid_layout'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Grid, 'horizontal_grid_type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (designing.OutputTemporalRequirement, 'conformance_is_requested'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (designing.OutputTemporalRequirement, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (designing.OutputTemporalRequirement, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "0.0"),



    ),

    (designing.OutputTemporalRequirement, 'continuous_subset'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.N"),



    ),

    (designing.OutputTemporalRequirement, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (designing.OutputTemporalRequirement, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.OutputTemporalRequirement, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.OutputTemporalRequirement, 'sliced_subset'): (

        ('type', shared.TimesliceList),


        ('cardinality', "0.1"),



    ),

    (designing.OutputTemporalRequirement, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.OutputTemporalRequirement, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (designing.OutputTemporalRequirement, 'throughout'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (designing.OutputTemporalRequirement, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (designing.OutputTemporalRequirement, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.0"),



    ),

    (designing.OutputTemporalRequirement, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.OutputTemporalRequirement, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (science.Extent, 'southern_boundary'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (science.Extent, 'is_global'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (science.Extent, 'western_boundary'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (science.Extent, 'northern_boundary'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (science.Extent, 'bottom_vertical_level'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (science.Extent, 'region_known_as'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (science.Extent, 'z_units'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Extent, 'eastern_boundary'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (science.Extent, 'top_vertical_level'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),



    (shared.DatetimeSet, 'length'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),



    (designing.DomainProperties, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.DomainProperties, 'conformance_is_requested'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (designing.DomainProperties, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (designing.DomainProperties, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (designing.DomainProperties, 'required_extent'): (

        ('type', science.Extent),


        ('cardinality', "0.1"),



    ),

    (designing.DomainProperties, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (designing.DomainProperties, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.DomainProperties, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "0.0"),



    ),

    (designing.DomainProperties, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.DomainProperties, 'required_resolution'): (

        ('type', science.Resolution),


        ('cardinality', "0.1"),



    ),

    (designing.DomainProperties, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (designing.DomainProperties, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.0"),



    ),

    (designing.DomainProperties, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.DomainProperties, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (science.Model, 'model_default_properties'): (

        ('type', science.KeyProperties),


        ('cardinality', "0.1"),



    ),

    (science.Model, 'documentation'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (science.Model, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Model, 'id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Model, 'repository'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.1"),



    ),

    (science.Model, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Model, 'development_history'): (

        ('type', software.DevelopmentPath),


        ('cardinality', "0.1"),



    ),

    (science.Model, 'internal_software_components'): (

        ('type', software.SoftwareComponent),


        ('cardinality', "0.N"),



    ),

    (science.Model, 'category'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Model, 'simulates'): (

        ('type', science.ScientificDomain),


        ('cardinality', "0.N"),



    ),

    (science.Model, 'coupled_components'): (

        ('type', science.Model),


        ('cardinality', "0.N"),



    ),

    (science.Model, 'version'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Model, 'release_date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (science.Model, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Model, 'coupler'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Model, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),



    (shared.DateTime, 'offset'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (shared.DateTime, 'value'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (shared.NumberArray, 'values'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (shared.Party, 'organisation'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (shared.Party, 'orcid_id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Party, 'address'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Party, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Party, 'url'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.1"),



    ),

    (shared.Party, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (shared.Party, 'email'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (activity.UberEnsemble, 'supported'): (

        ('type', designing.NumericalExperiment),


        ('cardinality', "1.N"),



    ),

    (activity.UberEnsemble, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.UberEnsemble, 'has_ensemble_axes'): (

        ('type', activity.EnsembleAxis),


        ('cardinality', "1.N"),



    ),

    (activity.UberEnsemble, 'common_conformances'): (

        ('type', activity.Conformance),


        ('cardinality', "0.0"),



    ),

    (activity.UberEnsemble, 'child_ensembles'): (

        ('type', activity.Ensemble),


        ('cardinality', "1.N"),



    ),

    (activity.UberEnsemble, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.UberEnsemble, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.0"),



    ),

    (activity.UberEnsemble, 'documentation'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.N"),



    ),

    (activity.UberEnsemble, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.0"),



    ),

    (activity.UberEnsemble, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (activity.UberEnsemble, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (activity.UberEnsemble, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.0"),



    ),

    (activity.UberEnsemble, 'part_of'): (

        ('type', activity.UberEnsemble),


        ('cardinality', "0.N"),



    ),

    (activity.UberEnsemble, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.UberEnsemble, 'members'): (

        ('type', activity.EnsembleMember),


        ('cardinality', "0.0"),



    ),

    (activity.UberEnsemble, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.0"),



    ),

    (activity.UberEnsemble, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),



    (science.ConservationProperties, 'corrected_conserved_prognostic_variables'): (

        ('type', data.VariableCollection),


        ('cardinality', "0.1"),



    ),

    (science.ConservationProperties, 'correction_methodology'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.ConservationProperties, 'flux_correction_was_used'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),



    (platform.Partition, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (platform.Partition, 'model_number'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.Partition, 'online_documentation'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.N"),



    ),

    (platform.Partition, 'institution'): (

        ('type', shared.Party),


        ('cardinality', "1.1"),



    ),

    (platform.Partition, 'when_used'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.1"),



    ),

    (platform.Partition, 'partition'): (

        ('type', platform.Partition),


        ('cardinality', "0.N"),



    ),

    (platform.Partition, 'vendor'): (

        ('type', shared.Party),


        ('cardinality', "0.1"),



    ),

    (platform.Partition, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.Partition, 'storage_pools'): (

        ('type', platform.StoragePool),


        ('cardinality', "0.N"),



    ),

    (platform.Partition, 'compute_pools'): (

        ('type', platform.ComputePool),


        ('cardinality', "1.N"),



    ),



    (activity.AxisMember, 'extra_detail'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.AxisMember, 'value'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (activity.AxisMember, 'index'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (activity.AxisMember, 'description'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (software.DevelopmentPath, 'funding_sources'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (software.DevelopmentPath, 'developed_in_house'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (software.DevelopmentPath, 'creators'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (software.DevelopmentPath, 'previous_version'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.DevelopmentPath, 'consortium_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (shared.TimesliceList, 'members'): (

        ('type', shared.NumberArray),


        ('cardinality', "1.1"),



    ),

    (shared.TimesliceList, 'units'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (platform.ComputePool, 'compute_cores_per_node'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'cpu_type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'operating_system'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'accelerators_per_node'): (

        ('type', int),


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

    (platform.ComputePool, 'model_number'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'interconnect'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'memory_per_node'): (

        ('type', platform.StorageVolume),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'accelerator_type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (designing.TemporalConstraint, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (designing.TemporalConstraint, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.TemporalConstraint, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.TemporalConstraint, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "0.0"),



    ),

    (designing.TemporalConstraint, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.TemporalConstraint, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (designing.TemporalConstraint, 'conformance_is_requested'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (designing.TemporalConstraint, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.TemporalConstraint, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.TemporalConstraint, 'required_calendar'): (

        ('type', shared.Calendar),


        ('cardinality', "0.1"),



    ),

    (designing.TemporalConstraint, 'required_duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.1"),



    ),

    (designing.TemporalConstraint, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.0"),



    ),

    (designing.TemporalConstraint, 'start_date'): (

        ('type', shared.DateTime),


        ('cardinality', "0.1"),



    ),

    (designing.TemporalConstraint, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (designing.TemporalConstraint, 'start_flexibility'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.1"),



    ),

    (designing.TemporalConstraint, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),



    (science.Resolution, 'number_of_xy_gridpoints'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (science.Resolution, 'typical_y_degrees'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (science.Resolution, 'is_adaptive_grid'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (science.Resolution, 'typical_x_degrees'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (science.Resolution, 'number_of_levels'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (science.Resolution, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Resolution, 'equivalent_resolution_km'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),



    (activity.ParentSimulation, 'branch_time_in_parent'): (

        ('type', shared.DateTime),


        ('cardinality', "0.1"),



    ),

    (activity.ParentSimulation, 'parent'): (

        ('type', data.Simulation),


        ('cardinality', "1.1"),



    ),

    (activity.ParentSimulation, 'branch_time_in_child'): (

        ('type', shared.DateTime),


        ('cardinality', "0.1"),



    ),



    (shared.DocMetaInfo, 'drs_path'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'drs_keys'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (shared.DocMetaInfo, 'source_key'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'external_ids'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (shared.DocMetaInfo, 'type_display_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'id'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'institute'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'type_sort_key'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'version'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'update_date'): (

        ('type', datetime.datetime),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'create_date'): (

        ('type', datetime.datetime),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'author'): (

        ('type', shared.Party),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'sort_key'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'project'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'source'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'language'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (designing.SimulationPlan, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.SimulationPlan, 'expected_platform'): (

        ('type', platform.Machine),


        ('cardinality', "0.1"),



    ),

    (designing.SimulationPlan, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "1.1"),



    ),

    (designing.SimulationPlan, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.SimulationPlan, 'will_support_experiments'): (

        ('type', designing.NumericalExperiment),


        ('cardinality', "1.N"),



    ),

    (designing.SimulationPlan, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (designing.SimulationPlan, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (designing.SimulationPlan, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.SimulationPlan, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.SimulationPlan, 'expected_model'): (

        ('type', science.Model),


        ('cardinality', "1.1"),



    ),

    (designing.SimulationPlan, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (designing.SimulationPlan, 'expected_performance_sypd'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (designing.SimulationPlan, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.SimulationPlan, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),



    (drs.DrsPublicationDataset, 'frequency'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (drs.DrsPublicationDataset, 'realm'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (drs.DrsPublicationDataset, 'institute'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsPublicationDataset, 'product'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsPublicationDataset, 'version_number'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (drs.DrsPublicationDataset, 'model'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsPublicationDataset, 'experiment'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsPublicationDataset, 'activity'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (data.Dataset, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (data.Dataset, 'availability'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.N"),



    ),

    (data.Dataset, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (data.Dataset, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.Dataset, 'produced_by'): (

        ('type', data.Simulation),


        ('cardinality', "0.1"),



    ),

    (data.Dataset, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (data.Dataset, 'related_to_dataset'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.N"),



    ),

    (data.Dataset, 'drs_datasets'): (

        ('type', drs.DrsPublicationDataset),


        ('cardinality', "0.N"),



    ),

    (data.Dataset, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (designing.MultiEnsemble, 'conformance_is_requested'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (designing.MultiEnsemble, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (designing.MultiEnsemble, 'ensemble_axis'): (

        ('type', designing.EnsembleRequirement),


        ('cardinality', "1.N"),



    ),

    (designing.MultiEnsemble, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.MultiEnsemble, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.MultiEnsemble, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "0.0"),



    ),

    (designing.MultiEnsemble, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.MultiEnsemble, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (designing.MultiEnsemble, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (designing.MultiEnsemble, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (designing.MultiEnsemble, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.0"),



    ),

    (designing.MultiEnsemble, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.MultiEnsemble, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (science.SubProcess, 'implementation_overview'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.SubProcess, 'context'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.SubProcess, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.SubProcess, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (science.SubProcess, 'properties'): (

        ('type', science.Detail),


        ('cardinality', "0.N"),



    ),

    (science.SubProcess, 'id'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (activity.Conformance, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.0"),



    ),

    (activity.Conformance, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.0"),



    ),

    (activity.Conformance, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Conformance, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (activity.Conformance, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.0"),



    ),

    (activity.Conformance, 'target_requirement'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "1.1"),



    ),

    (activity.Conformance, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (activity.Conformance, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (activity.Conformance, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.0"),



    ),

    (activity.Conformance, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.Conformance, 'description'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (shared.Reference, 'context'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Reference, 'document'): (

        ('type', shared.ExternalDocument),


        ('cardinality', "1.1"),



    ),



    (software.SoftwareComponent, 'language'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.SoftwareComponent, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (software.SoftwareComponent, 'repository'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.1"),



    ),

    (software.SoftwareComponent, 'documentation'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (software.SoftwareComponent, 'coupling_framework'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.SoftwareComponent, 'development_history'): (

        ('type', software.DevelopmentPath),


        ('cardinality', "0.1"),



    ),

    (software.SoftwareComponent, 'license'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.SoftwareComponent, 'dependencies'): (

        ('type', software.EntryPoint),


        ('cardinality', "0.N"),



    ),

    (software.SoftwareComponent, 'release_date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (software.SoftwareComponent, 'version'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.SoftwareComponent, 'composition'): (

        ('type', software.Composition),


        ('cardinality', "0.1"),



    ),

    (software.SoftwareComponent, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.SoftwareComponent, 'grid'): (

        ('type', software.Gridspec),


        ('cardinality', "0.1"),



    ),

    (software.SoftwareComponent, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.SoftwareComponent, 'connection_points'): (

        ('type', software.Variable),


        ('cardinality', "0.N"),



    ),

    (software.SoftwareComponent, 'sub_components'): (

        ('type', software.SoftwareComponent),


        ('cardinality', "0.N"),



    ),



    (platform.StoragePool, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.StoragePool, 'volume_available'): (

        ('type', platform.StorageVolume),


        ('cardinality', "1.1"),



    ),

    (platform.StoragePool, 'vendor'): (

        ('type', shared.Party),


        ('cardinality', "0.1"),



    ),

    (platform.StoragePool, 'type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.StoragePool, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (platform.Performance, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'total_nodes_used'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'compiler'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'io_load'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (platform.Performance, 'asypd'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'subcomponent_performance'): (

        ('type', platform.ComponentPerformance),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'memory_bloat'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'platform'): (

        ('type', platform.Machine),


        ('cardinality', "1.1"),



    ),

    (platform.Performance, 'model'): (

        ('type', science.Model),


        ('cardinality', "1.1"),



    ),

    (platform.Performance, 'sypd'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'load_imbalance'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'chsy'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'coupler_load'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),



    (activity.Activity, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.Activity, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (activity.Activity, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Activity, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Activity, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Activity, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (activity.Activity, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (activity.Activity, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.1"),



    ),

    (activity.Activity, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.Activity, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (designing.Project, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.1"),



    ),

    (designing.Project, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (designing.Project, 'requires_experiments'): (

        ('type', designing.NumericalExperiment),


        ('cardinality', "0.N"),



    ),

    (designing.Project, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.Project, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (designing.Project, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.Project, 'description'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.Project, 'sub_projects'): (

        ('type', designing.Project),


        ('cardinality', "0.N"),



    ),

    (designing.Project, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (designing.Project, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.Project, 'previous_projects'): (

        ('type', designing.Project),


        ('cardinality', "0.N"),



    ),

    (designing.Project, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.Project, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),



    (shared.Cimtext, 'content'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.Cimtext, 'content_type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (shared.QualityReview, 'quality_status'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.QualityReview, 'quality_description'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.QualityReview, 'metadata_reviewer'): (

        ('type', shared.Party),


        ('cardinality', "1.1"),



    ),

    (shared.QualityReview, 'date'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (activity.EnsembleMember, 'ran_on'): (

        ('type', platform.Machine),


        ('cardinality', "0.1"),



    ),

    (activity.EnsembleMember, 'errata'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.1"),



    ),

    (activity.EnsembleMember, 'variant_id'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.EnsembleMember, 'had_performance'): (

        ('type', platform.Performance),


        ('cardinality', "0.1"),



    ),

    (activity.EnsembleMember, 'simulation'): (

        ('type', data.Simulation),


        ('cardinality', "1.1"),



    ),



    (software.Variable, 'prognostic'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (software.Variable, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (software.Variable, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (data.VariableCollection, 'collection_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.VariableCollection, 'variables'): (

        ('type', unicode),


        ('cardinality', "1.N"),



    ),


}