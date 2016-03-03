
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

import typeset_for_shared_package as shared
import typeset_for_platform_package as platform
import typeset_for_data_package as data
import typeset_for_activity_package as activity
import typeset_for_drs_package as drs
import typeset_for_software_package as software
import typeset_for_science_package as science
import typeset_for_designing_package as designing




# Map of ontology types to constraints.
CONSTRAINTS = {
    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------


    shared.IrregularDateset: (

        ('length', 'type', int),

        ('date_set', 'type', unicode),


        ('length', 'cardinality', "1.1"),

        ('date_set', 'cardinality', "1.1"),



    ),

    shared.Calendar: (

        ('standard_name', 'type', unicode),

        ('month_lengths', 'type', int),

        ('name', 'type', unicode),

        ('description', 'type', unicode),


        ('standard_name', 'cardinality', "1.1"),

        ('month_lengths', 'cardinality', "0.N"),

        ('name', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



    ),

    shared.DatetimeSet: (

        ('length', 'type', int),


        ('length', 'cardinality', "1.1"),



    ),

    shared.TimesliceList: (

        ('units', 'type', unicode),

        ('members', 'type', shared.NumberArray),


        ('units', 'cardinality', "1.1"),

        ('members', 'cardinality', "1.1"),



    ),

    shared.Cimtext: (

        ('content', 'type', unicode),

        ('content_type', 'type', unicode),


        ('content', 'cardinality', "1.1"),

        ('content_type', 'cardinality', "1.1"),



    ),

    shared.RegularTimeset: (

        ('length', 'type', int),

        ('start_date', 'type', shared.DateTime),

        ('increment', 'type', shared.TimePeriod),


        ('length', 'cardinality', "1.1"),

        ('start_date', 'cardinality', "1.1"),

        ('increment', 'cardinality', "1.1"),



    ),

    shared.DocMetaInfo: (

        ('drs_keys', 'type', unicode),

        ('drs_path', 'type', unicode),

        ('create_date', 'type', datetime.datetime),

        ('language', 'type', unicode),

        ('author', 'type', shared.Party),

        ('institute', 'type', unicode),

        ('source_key', 'type', unicode),

        ('id', 'type', unicode),

        ('project', 'type', unicode),

        ('sort_key', 'type', unicode),

        ('version', 'type', int),

        ('source', 'type', unicode),

        ('type_sort_key', 'type', unicode),

        ('external_ids', 'type', unicode),

        ('type', 'type', unicode),

        ('update_date', 'type', datetime.datetime),

        ('type_display_name', 'type', unicode),


        ('drs_keys', 'cardinality', "0.N"),

        ('drs_path', 'cardinality', "0.1"),

        ('create_date', 'cardinality', "1.1"),

        ('language', 'cardinality', "1.1"),

        ('author', 'cardinality', "0.1"),

        ('institute', 'cardinality', "0.1"),

        ('source_key', 'cardinality', "0.1"),

        ('id', 'cardinality', "1.1"),

        ('project', 'cardinality', "1.1"),

        ('sort_key', 'cardinality', "0.1"),

        ('version', 'cardinality', "1.1"),

        ('source', 'cardinality', "1.1"),

        ('type_sort_key', 'cardinality', "0.1"),

        ('external_ids', 'cardinality', "0.N"),

        ('type', 'cardinality', "1.1"),

        ('update_date', 'cardinality', "1.1"),

        ('type_display_name', 'cardinality', "0.1"),



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

    shared.DocReference: (

        ('constraint_vocabulary', 'type', unicode),

        ('protocol', 'type', unicode),

        ('name', 'type', unicode),

        ('relationship', 'type', unicode),

        ('version', 'type', int),

        ('context', 'type', unicode),

        ('type', 'type', unicode),

        ('id', 'type', unicode),

        ('linkage', 'type', unicode),

        ('description', 'type', unicode),


        ('constraint_vocabulary', 'cardinality', "0.1"),

        ('protocol', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

        ('relationship', 'cardinality', "0.1"),

        ('version', 'cardinality', "0.1"),

        ('context', 'cardinality', "0.1"),

        ('type', 'cardinality', "1.1"),

        ('id', 'cardinality', "0.1"),

        ('linkage', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),



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

    shared.TimePeriod: (

        ('date', 'type', shared.DateTime),

        ('units', 'type', unicode),

        ('date_type', 'type', unicode),

        ('length', 'type', int),

        ('calendar', 'type', shared.Calendar),


        ('date', 'cardinality', "0.1"),

        ('units', 'cardinality', "1.1"),

        ('date_type', 'cardinality', "1.1"),

        ('length', 'cardinality', "1.1"),

        ('calendar', 'cardinality', "0.1"),



    ),

    shared.DateTime: (

        ('value', 'type', unicode),

        ('offset', 'type', bool),


        ('value', 'cardinality', "1.1"),

        ('offset', 'cardinality', "0.1"),



    ),

    shared.Responsibility: (

        ('party', 'type', shared.Party),

        ('when', 'type', shared.TimePeriod),

        ('role', 'type', unicode),


        ('party', 'cardinality', "1.N"),

        ('when', 'cardinality', "0.1"),

        ('role', 'cardinality', "1.1"),



    ),

    shared.QualityReview: (

        ('date', 'type', unicode),

        ('metadata_reviewer', 'type', shared.Party),

        ('quality_status', 'type', unicode),

        ('quality_description', 'type', unicode),


        ('date', 'cardinality', "1.1"),

        ('metadata_reviewer', 'cardinality', "1.1"),

        ('quality_status', 'cardinality', "0.1"),

        ('quality_description', 'cardinality', "1.1"),



    ),

    shared.Pid: (

        ('resolution_service', 'type', shared.OnlineResource),

        ('id', 'type', unicode),


        ('resolution_service', 'cardinality', "1.1"),

        ('id', 'cardinality', "1.1"),



    ),

    shared.KeyFloat: (

        ('value', 'type', float),

        ('key', 'type', unicode),


        ('value', 'cardinality', "1.1"),

        ('key', 'cardinality', "1.1"),



    ),

    shared.NumberArray: (

        ('values', 'type', unicode),


        ('values', 'cardinality', "1.1"),



    ),

    shared.Reference: (

        ('document', 'type', shared.ExternalDocument),

        ('context', 'type', unicode),


        ('document', 'cardinality', "1.1"),

        ('context', 'cardinality', "0.1"),



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

    platform.StorageVolume: (

        ('units', 'type', unicode),

        ('volume', 'type', int),


        ('units', 'cardinality', "1.1"),

        ('volume', 'cardinality', "1.1"),



    ),

    platform.ComponentPerformance: (

        ('speed', 'type', float),

        ('nodes_used', 'type', int),

        ('component', 'type', software.SoftwareComponent),

        ('cores_used', 'type', int),

        ('component_name', 'type', unicode),


        ('speed', 'cardinality', "1.1"),

        ('nodes_used', 'cardinality', "0.1"),

        ('component', 'cardinality', "0.1"),

        ('cores_used', 'cardinality', "0.1"),

        ('component_name', 'cardinality', "1.1"),



    ),

    platform.Performance: (

        ('io_load', 'type', float),

        ('asypd', 'type', float),

        ('memory_bloat', 'type', float),

        ('name', 'type', unicode),

        ('subcomponent_performance', 'type', platform.ComponentPerformance),

        ('load_imbalance', 'type', float),

        ('total_nodes_used', 'type', int),

        ('chsy', 'type', float),

        ('sypd', 'type', float),

        ('platform', 'type', platform.Machine),

        ('meta', 'type', shared.DocMetaInfo),

        ('coupler_load', 'type', float),

        ('model', 'type', science.Model),

        ('compiler', 'type', unicode),


        ('io_load', 'cardinality', "0.1"),

        ('asypd', 'cardinality', "0.1"),

        ('memory_bloat', 'cardinality', "0.1"),

        ('name', 'cardinality', "0.1"),

        ('subcomponent_performance', 'cardinality', "0.1"),

        ('load_imbalance', 'cardinality', "0.1"),

        ('total_nodes_used', 'cardinality', "0.1"),

        ('chsy', 'cardinality', "0.1"),

        ('sypd', 'cardinality', "0.1"),

        ('platform', 'cardinality', "1.1"),

        ('meta', 'cardinality', "1.1"),

        ('coupler_load', 'cardinality', "0.1"),

        ('model', 'cardinality', "1.1"),

        ('compiler', 'cardinality', "0.1"),



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

    platform.ComputePool: (

        ('operating_system', 'type', unicode),

        ('number_of_nodes', 'type', int),

        ('description', 'type', unicode),

        ('memory_per_node', 'type', platform.StorageVolume),

        ('model_number', 'type', unicode),

        ('compute_cores_per_node', 'type', int),

        ('accelerator_type', 'type', unicode),

        ('cpu_type', 'type', unicode),

        ('interconnect', 'type', unicode),

        ('accelerators_per_node', 'type', int),

        ('name', 'type', unicode),


        ('operating_system', 'cardinality', "0.1"),

        ('number_of_nodes', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('memory_per_node', 'cardinality', "0.1"),

        ('model_number', 'cardinality', "0.1"),

        ('compute_cores_per_node', 'cardinality', "0.1"),

        ('accelerator_type', 'cardinality', "0.1"),

        ('cpu_type', 'cardinality', "0.1"),

        ('interconnect', 'cardinality', "0.1"),

        ('accelerators_per_node', 'cardinality', "0.1"),

        ('name', 'cardinality', "0.1"),



    ),



    data.Downscaling: (

        ('ensemble_identifier', 'type', unicode),

        ('used', 'type', science.Model),

        ('name', 'type', unicode),

        ('part_of_project', 'type', designing.Project),

        ('duration', 'type', shared.TimePeriod),

        ('parent_simulation', 'type', activity.ParentSimulation),

        ('primary_ensemble', 'type', activity.Ensemble),

        ('canonical_name', 'type', unicode),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('downscaled_from', 'type', data.Simulation),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('ran_for_experiments', 'type', designing.NumericalExperiment),

        ('rationale', 'type', unicode),

        ('keywords', 'type', unicode),

        ('calendar', 'type', shared.Calendar),

        ('description', 'type', unicode),


        ('ensemble_identifier', 'cardinality', "1.1"),

        ('used', 'cardinality', "1.1"),

        ('name', 'cardinality', "1.1"),

        ('part_of_project', 'cardinality', "1.N"),

        ('duration', 'cardinality', "0.1"),

        ('parent_simulation', 'cardinality', "0.0"),

        ('primary_ensemble', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('downscaled_from', 'cardinality', "1.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('ran_for_experiments', 'cardinality', "1.N"),

        ('rationale', 'cardinality', "0.0"),

        ('keywords', 'cardinality', "0.N"),

        ('calendar', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



    ),

    data.Dataset: (

        ('related_to_dataset', 'type', shared.OnlineResource),

        ('name', 'type', unicode),

        ('produced_by', 'type', data.Simulation),

        ('drs_datasets', 'type', drs.DrsPublicationDataset),

        ('responsible_parties', 'type', shared.Responsibility),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('availability', 'type', shared.OnlineResource),

        ('description', 'type', unicode),


        ('related_to_dataset', 'cardinality', "0.N"),

        ('name', 'cardinality', "1.1"),

        ('produced_by', 'cardinality', "0.1"),

        ('drs_datasets', 'cardinality', "0.N"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('availability', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),



    ),

    data.VariableCollection: (

        ('collection_name', 'type', unicode),

        ('variables', 'type', unicode),


        ('collection_name', 'cardinality', "0.1"),

        ('variables', 'cardinality', "1.N"),



    ),

    data.Simulation: (

        ('ensemble_identifier', 'type', unicode),

        ('used', 'type', science.Model),

        ('name', 'type', unicode),

        ('part_of_project', 'type', designing.Project),

        ('parent_simulation', 'type', activity.ParentSimulation),

        ('primary_ensemble', 'type', activity.Ensemble),

        ('responsible_parties', 'type', shared.Responsibility),

        ('keywords', 'type', unicode),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('ran_for_experiments', 'type', designing.NumericalExperiment),

        ('rationale', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('calendar', 'type', shared.Calendar),

        ('description', 'type', unicode),


        ('ensemble_identifier', 'cardinality', "1.1"),

        ('used', 'cardinality', "1.1"),

        ('name', 'cardinality', "1.1"),

        ('part_of_project', 'cardinality', "1.N"),

        ('parent_simulation', 'cardinality', "0.1"),

        ('primary_ensemble', 'cardinality', "0.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('keywords', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('ran_for_experiments', 'cardinality', "1.N"),

        ('rationale', 'cardinality', "0.0"),

        ('duration', 'cardinality', "0.1"),

        ('calendar', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



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

    activity.ParentSimulation: (

        ('branch_time_in_parent', 'type', shared.DateTime),

        ('branch_time_in_child', 'type', shared.DateTime),

        ('parent', 'type', data.Simulation),


        ('branch_time_in_parent', 'cardinality', "0.1"),

        ('branch_time_in_child', 'cardinality', "0.1"),

        ('parent', 'cardinality', "1.1"),



    ),

    activity.EnsembleMember: (

        ('variant_id', 'type', unicode),

        ('simulation', 'type', data.Simulation),

        ('ran_on', 'type', platform.Machine),

        ('errata', 'type', shared.OnlineResource),

        ('had_performance', 'type', platform.Performance),


        ('variant_id', 'cardinality', "1.1"),

        ('simulation', 'cardinality', "1.1"),

        ('ran_on', 'cardinality', "0.1"),

        ('errata', 'cardinality', "0.1"),

        ('had_performance', 'cardinality', "0.1"),



    ),

    activity.Activity: (

        ('name', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('keywords', 'type', unicode),

        ('description', 'type', unicode),


        ('name', 'cardinality', "1.1"),

        ('duration', 'cardinality', "0.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('rationale', 'cardinality', "0.1"),

        ('keywords', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),



    ),

    activity.Conformance: (

        ('name', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('description', 'type', unicode),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('keywords', 'type', unicode),

        ('target_requirement', 'type', designing.NumericalRequirement),


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

    activity.Ensemble: (

        ('part_of', 'type', activity.UberEnsemble),

        ('common_conformances', 'type', activity.Conformance),

        ('name', 'type', unicode),

        ('description', 'type', unicode),

        ('supported', 'type', designing.NumericalExperiment),

        ('responsible_parties', 'type', shared.Responsibility),

        ('keywords', 'type', unicode),

        ('members', 'type', activity.EnsembleMember),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('has_ensemble_axes', 'type', activity.EnsembleAxis),

        ('documentation', 'type', shared.OnlineResource),


        ('part_of', 'cardinality', "0.N"),

        ('common_conformances', 'cardinality', "0.N"),

        ('name', 'cardinality', "1.1"),

        ('long_name', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

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

        ('documentation', 'cardinality', "0.N"),



    ),

    activity.UberEnsemble: (

        ('child_ensembles', 'type', activity.Ensemble),

        ('part_of', 'type', activity.UberEnsemble),

        ('common_conformances', 'type', activity.Conformance),

        ('name', 'type', unicode),

        ('description', 'type', unicode),

        ('supported', 'type', designing.NumericalExperiment),

        ('responsible_parties', 'type', shared.Responsibility),

        ('members', 'type', activity.EnsembleMember),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('keywords', 'type', unicode),

        ('has_ensemble_axes', 'type', activity.EnsembleAxis),

        ('duration', 'type', shared.TimePeriod),

        ('documentation', 'type', shared.OnlineResource),


        ('child_ensembles', 'cardinality', "1.N"),

        ('part_of', 'cardinality', "0.N"),

        ('common_conformances', 'cardinality', "0.0"),

        ('rationale', 'cardinality', "0.0"),

        ('long_name', 'cardinality', "0.1"),

        ('documentation', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('supported', 'cardinality', "1.N"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('keywords', 'cardinality', "0.0"),

        ('canonical_name', 'cardinality', "0.0"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('members', 'cardinality', "0.0"),

        ('duration', 'cardinality', "0.0"),

        ('has_ensemble_axes', 'cardinality', "1.N"),

        ('name', 'cardinality', "1.1"),



    ),



    drs.DrsPublicationDataset: (

        ('product', 'type', unicode),

        ('realm', 'type', unicode),

        ('institute', 'type', unicode),

        ('version_number', 'type', int),

        ('experiment', 'type', unicode),

        ('frequency', 'type', unicode),

        ('activity', 'type', unicode),

        ('model', 'type', unicode),


        ('product', 'cardinality', "1.1"),

        ('realm', 'cardinality', "0.1"),

        ('institute', 'cardinality', "1.1"),

        ('version_number', 'cardinality', "0.1"),

        ('experiment', 'cardinality', "1.1"),

        ('frequency', 'cardinality', "0.1"),

        ('activity', 'cardinality', "1.1"),

        ('model', 'cardinality', "1.1"),



    ),

    drs.DrsEnsembleIdentifier: (

        ('perturbation_number', 'type', int),

        ('initialisation_method_number', 'type', int),

        ('realisation_number', 'type', int),


        ('perturbation_number', 'cardinality', "1.1"),

        ('initialisation_method_number', 'cardinality', "1.1"),

        ('realisation_number', 'cardinality', "1.1"),



    ),

    drs.DrsTemporalIdentifier: (

        ('start', 'type', unicode),

        ('end', 'type', unicode),

        ('suffix', 'type', unicode),


        ('start', 'cardinality', "1.1"),

        ('end', 'cardinality', "0.1"),

        ('suffix', 'cardinality', "0.1"),



    ),

    drs.DrsAtomicDataset: (

        ('product', 'type', unicode),

        ('realm', 'type', unicode),

        ('institute', 'type', unicode),

        ('geographical_constraint', 'type', drs.DrsGeographicalIndicator),

        ('version_number', 'type', int),

        ('mip_table', 'type', unicode),

        ('variable_name', 'type', unicode),

        ('experiment', 'type', unicode),

        ('frequency', 'type', unicode),

        ('activity', 'type', unicode),

        ('ensemble_member', 'type', drs.DrsEnsembleIdentifier),

        ('model', 'type', unicode),

        ('temporal_constraint', 'type', drs.DrsTemporalIdentifier),


        ('version_number', 'cardinality', "1.1"),

        ('realm', 'cardinality', "1.1"),

        ('experiment', 'cardinality', "1.1"),

        ('institute', 'cardinality', "1.1"),

        ('activity', 'cardinality', "1.1"),

        ('product', 'cardinality', "1.1"),

        ('mip_table', 'cardinality', "1.1"),

        ('variable_name', 'cardinality', "1.1"),

        ('frequency', 'cardinality', "1.1"),

        ('geographical_constraint', 'cardinality', "0.1"),

        ('ensemble_member', 'cardinality', "1.1"),

        ('model', 'cardinality', "1.1"),

        ('temporal_constraint', 'cardinality', "0.1"),



    ),

    drs.DrsGeographicalIndicator: (

        ('operator', 'type', unicode),

        ('bounding_box', 'type', unicode),

        ('spatial_domain', 'type', unicode),


        ('operator', 'cardinality', "0.1"),

        ('bounding_box', 'cardinality', "0.1"),

        ('spatial_domain', 'cardinality', "0.1"),



    ),



    software.Gridspec: (

        ('description', 'type', unicode),


        ('description', 'cardinality', "1.1"),



    ),

    software.DevelopmentPath: (

        ('consortium_name', 'type', unicode),

        ('funding_sources', 'type', shared.Responsibility),

        ('creators', 'type', shared.Responsibility),

        ('developed_in_house', 'type', bool),

        ('previous_version', 'type', unicode),


        ('consortium_name', 'cardinality', "0.1"),

        ('funding_sources', 'cardinality', "0.N"),

        ('creators', 'cardinality', "0.N"),

        ('developed_in_house', 'cardinality', "1.1"),

        ('previous_version', 'cardinality', "0.1"),



    ),

    software.ComponentBase: (

        ('description', 'type', unicode),

        ('repository', 'type', shared.OnlineResource),

        ('release_date', 'type', datetime.datetime),

        ('documentation', 'type', shared.Reference),

        ('development_history', 'type', software.DevelopmentPath),

        ('long_name', 'type', unicode),

        ('version', 'type', unicode),

        ('name', 'type', unicode),


        ('description', 'cardinality', "0.1"),

        ('repository', 'cardinality', "0.1"),

        ('release_date', 'cardinality', "0.1"),

        ('documentation', 'cardinality', "0.N"),

        ('development_history', 'cardinality', "0.1"),

        ('long_name', 'cardinality', "0.1"),

        ('version', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),



    ),

    software.SoftwareComponent: (

        ('license', 'type', unicode),

        ('coupling_framework', 'type', unicode),

        ('description', 'type', unicode),

        ('language', 'type', unicode),

        ('release_date', 'type', datetime.datetime),

        ('documentation', 'type', shared.Reference),

        ('development_history', 'type', software.DevelopmentPath),

        ('sub_components', 'type', software.SoftwareComponent),

        ('repository', 'type', shared.OnlineResource),

        ('long_name', 'type', unicode),

        ('connection_points', 'type', software.Variable),

        ('grid', 'type', software.Gridspec),

        ('version', 'type', unicode),

        ('dependencies', 'type', software.EntryPoint),

        ('composition', 'type', software.Composition),

        ('name', 'type', unicode),


        ('license', 'cardinality', "0.1"),

        ('coupling_framework', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('language', 'cardinality', "0.1"),

        ('release_date', 'cardinality', "0.1"),

        ('documentation', 'cardinality', "0.N"),

        ('development_history', 'cardinality', "0.1"),

        ('sub_components', 'cardinality', "0.N"),

        ('repository', 'cardinality', "0.1"),

        ('long_name', 'cardinality', "0.1"),

        ('connection_points', 'cardinality', "0.N"),

        ('grid', 'cardinality', "0.1"),

        ('version', 'cardinality', "0.1"),

        ('dependencies', 'cardinality', "0.N"),

        ('composition', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),



    ),

    software.EntryPoint: (

        ('name', 'type', unicode),


        ('name', 'cardinality', "0.1"),



    ),

    software.Composition: (

        ('couplings', 'type', unicode),

        ('description', 'type', unicode),


        ('couplings', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),



    ),

    software.Variable: (

        ('description', 'type', unicode),

        ('prognostic', 'type', bool),

        ('name', 'type', unicode),


        ('description', 'cardinality', "0.1"),

        ('prognostic', 'cardinality', "1.1"),

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

    science.ScientificDomain: (

        ('simulates', 'type', science.Process),

        ('realm', 'type', unicode),

        ('name', 'type', unicode),

        ('overview', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('differing_key_properties', 'type', science.KeyProperties),

        ('id', 'type', unicode),


        ('simulates', 'cardinality', "1.N"),

        ('realm', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

        ('overview', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('differing_key_properties', 'cardinality', "0.1"),

        ('id', 'cardinality', "0.1"),



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

    science.ScienceContext: (

        ('id', 'type', unicode),

        ('context', 'type', unicode),

        ('name', 'type', unicode),


        ('id', 'cardinality', "1.1"),

        ('context', 'cardinality', "1.1"),

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

    science.Model: (

        ('category', 'type', unicode),

        ('simulates', 'type', science.ScientificDomain),

        ('model_default_properties', 'type', science.KeyProperties),

        ('name', 'type', unicode),

        ('repository', 'type', shared.OnlineResource),

        ('long_name', 'type', unicode),

        ('coupled_components', 'type', science.Model),

        ('release_date', 'type', datetime.datetime),

        ('documentation', 'type', shared.Reference),

        ('internal_software_components', 'type', software.SoftwareComponent),

        ('development_history', 'type', software.DevelopmentPath),

        ('coupler', 'type', unicode),

        ('version', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('id', 'type', unicode),

        ('description', 'type', unicode),


        ('category', 'cardinality', "1.1"),

        ('simulates', 'cardinality', "0.N"),

        ('model_default_properties', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

        ('repository', 'cardinality', "0.1"),

        ('long_name', 'cardinality', "0.1"),

        ('coupled_components', 'cardinality', "0.N"),

        ('release_date', 'cardinality', "0.1"),

        ('documentation', 'cardinality', "0.N"),

        ('internal_software_components', 'cardinality', "0.N"),

        ('development_history', 'cardinality', "0.1"),

        ('coupler', 'cardinality', "0.1"),

        ('version', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('id', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



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



    designing.NumericalExperiment: (

        ('requirements', 'type', designing.NumericalRequirement),

        ('name', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('rationale', 'type', unicode),

        ('related_experiments', 'type', designing.NumericalExperiment),

        ('keywords', 'type', unicode),

        ('description', 'type', unicode),


        ('rationale', 'cardinality', "1.1"),

        ('requirements', 'cardinality', "0.N"),

        ('name', 'cardinality', "1.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('keywords', 'cardinality', "0.N"),

        ('related_experiments', 'cardinality', "0.N"),

        ('duration', 'cardinality', "0.0"),

        ('description', 'cardinality', "0.1"),



    ),

    designing.NumericalRequirement: (

        ('name', 'type', unicode),

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

        ('description', 'type', unicode),


        ('rationale', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

        ('additional_requirements', 'cardinality', "0.N"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('keywords', 'cardinality', "0.N"),

        ('duration', 'cardinality', "0.0"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),



    ),

    designing.TemporalConstraint: (

        ('name', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('required_duration', 'type', shared.TimePeriod),

        ('start_flexibility', 'type', shared.TimePeriod),

        ('responsible_parties', 'type', shared.Responsibility),

        ('additional_requirements', 'type', designing.NumericalRequirement),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('start_date', 'type', shared.DateTime),

        ('rationale', 'type', unicode),

        ('keywords', 'type', unicode),

        ('conformance_is_requested', 'type', bool),

        ('required_calendar', 'type', shared.Calendar),

        ('description', 'type', unicode),


        ('name', 'cardinality', "1.1"),

        ('long_name', 'cardinality', "0.1"),

        ('required_duration', 'cardinality', "0.1"),

        ('additional_requirements', 'cardinality', "0.0"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('start_flexibility', 'cardinality', "0.1"),

        ('keywords', 'cardinality', "0.N"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('start_date', 'cardinality', "0.1"),

        ('rationale', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.0"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('required_calendar', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



    ),

    designing.MultiTimeEnsemble: (

        ('ensemble_members', 'type', shared.DatetimeSet),

        ('name', 'type', unicode),

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

        ('description', 'type', unicode),


        ('ensemble_members', 'cardinality', "1.1"),

        ('name', 'cardinality', "1.1"),

        ('long_name', 'cardinality', "0.1"),

        ('additional_requirements', 'cardinality', "0.0"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('keywords', 'cardinality', "0.N"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('rationale', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.0"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),



    ),

    designing.EnsembleRequirement: (

        ('minimum_size', 'type', int),

        ('name', 'type', unicode),

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

        ('description', 'type', unicode),


        ('minimum_size', 'cardinality', "1.1"),

        ('name', 'cardinality', "1.1"),

        ('long_name', 'cardinality', "0.1"),

        ('additional_requirements', 'cardinality', "0.0"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('keywords', 'cardinality', "0.N"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('ensemble_type', 'cardinality', "1.1"),

        ('rationale', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.0"),

        ('ensemble_member', 'cardinality', "0.N"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),



    ),

    designing.DomainProperties: (

        ('required_resolution', 'type', science.Resolution),

        ('name', 'type', unicode),

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

        ('description', 'type', unicode),


        ('required_resolution', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

        ('keywords', 'cardinality', "0.N"),

        ('additional_requirements', 'cardinality', "0.0"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('required_extent', 'cardinality', "0.1"),

        ('rationale', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.0"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),



    ),

    designing.ForcingConstraint: (

        ('origin', 'type', shared.Reference),

        ('category', 'type', unicode),

        ('code', 'type', unicode),

        ('group', 'type', unicode),

        ('name', 'type', unicode),

        ('additional_constraint', 'type', unicode),

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

        ('data_link', 'type', shared.OnlineResource),

        ('duration', 'type', shared.TimePeriod),

        ('description', 'type', unicode),


        ('origin', 'cardinality', "0.1"),

        ('category', 'cardinality', "0.1"),

        ('code', 'cardinality', "0.1"),

        ('group', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

        ('long_name', 'cardinality', "0.1"),

        ('additional_constraint', 'cardinality', "0.1"),

        ('additional_requirements', 'cardinality', "0.0"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('forcing_type', 'cardinality', "1.1"),

        ('keywords', 'cardinality', "0.N"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('rationale', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.0"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('data_link', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



    ),

    designing.SimulationPlan: (

        ('expected_performance_sypd', 'type', float),

        ('name', 'type', unicode),

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

        ('will_support_experiments', 'type', designing.NumericalExperiment),

        ('expected_platform', 'type', platform.Machine),


        ('expected_performance_sypd', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

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

        ('will_support_experiments', 'cardinality', "1.N"),

        ('expected_platform', 'cardinality', "0.1"),



    ),

    designing.MultiEnsemble: (

        ('rationale', 'type', unicode),

        ('name', 'type', unicode),

        ('duration', 'type', shared.TimePeriod),

        ('additional_requirements', 'type', designing.NumericalRequirement),

        ('responsible_parties', 'type', shared.Responsibility),

        ('long_name', 'type', unicode),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('ensemble_axis', 'type', designing.EnsembleRequirement),

        ('keywords', 'type', unicode),

        ('conformance_is_requested', 'type', bool),

        ('description', 'type', unicode),


        ('rationale', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

        ('long_name', 'cardinality', "0.1"),

        ('additional_requirements', 'cardinality', "0.0"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('keywords', 'cardinality', "0.N"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('ensemble_axis', 'cardinality', "1.N"),

        ('duration', 'cardinality', "0.0"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),



    ),

    designing.OutputTemporalRequirement: (

        ('throughout', 'type', bool),

        ('name', 'type', unicode),

        ('long_name', 'type', unicode),

        ('continuous_subset', 'type', shared.TimePeriod),

        ('additional_requirements', 'type', designing.NumericalRequirement),

        ('sliced_subset', 'type', shared.TimesliceList),

        ('duration', 'type', shared.TimePeriod),

        ('canonical_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('references', 'type', shared.Reference),

        ('responsible_parties', 'type', shared.Responsibility),

        ('rationale', 'type', unicode),

        ('keywords', 'type', unicode),

        ('conformance_is_requested', 'type', bool),

        ('description', 'type', unicode),


        ('throughout', 'cardinality', "1.1"),

        ('name', 'cardinality', "1.1"),

        ('long_name', 'cardinality', "0.1"),

        ('continuous_subset', 'cardinality', "0.N"),

        ('additional_requirements', 'cardinality', "0.0"),

        ('sliced_subset', 'cardinality', "0.1"),

        ('keywords', 'cardinality', "0.N"),

        ('canonical_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('references', 'cardinality', "0.N"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('rationale', 'cardinality', "0.1"),

        ('duration', 'cardinality', "0.0"),

        ('conformance_is_requested', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),



    ),

    designing.Project: (

        ('requires_experiments', 'type', designing.NumericalExperiment),

        ('name', 'type', unicode),

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

        ('description', 'type', unicode),


        ('requires_experiments', 'cardinality', "0.N"),

        ('name', 'cardinality', "1.1"),

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

        ('description', 'cardinality', "1.1"),



    ),


    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------



    (shared.IrregularDateset, 'date_set'): (

        ('type', unicode),


        ('cardinality', "1.1"),



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

    (shared.Calendar, 'month_lengths'): (

        ('type', int),


        ('cardinality', "0.N"),



    ),



    (shared.DatetimeSet, 'length'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),



    (shared.TimesliceList, 'members'): (

        ('type', shared.NumberArray),


        ('cardinality', "1.1"),



    ),

    (shared.TimesliceList, 'units'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (shared.Cimtext, 'content'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.Cimtext, 'content_type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (shared.RegularTimeset, 'start_date'): (

        ('type', shared.DateTime),


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



    (shared.DocMetaInfo, 'sort_key'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'drs_path'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'institute'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'project'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'version'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'external_ids'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (shared.DocMetaInfo, 'type_display_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'author'): (

        ('type', shared.Party),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'source'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'id'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'type_sort_key'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'language'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'source_key'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'update_date'): (

        ('type', datetime.datetime),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'drs_keys'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (shared.DocMetaInfo, 'create_date'): (

        ('type', datetime.datetime),


        ('cardinality', "1.1"),



    ),



    (shared.OnlineResource, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.OnlineResource, 'protocol'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.OnlineResource, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.OnlineResource, 'linkage'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (shared.DocReference, 'version'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'relationship'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'constraint_vocabulary'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocReference, 'context'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (shared.Party, 'organisation'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (shared.Party, 'email'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Party, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (shared.Party, 'name'): (

        ('type', unicode),


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

    (shared.Party, 'url'): (

        ('type', shared.OnlineResource),


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

    (shared.TimePeriod, 'calendar'): (

        ('type', shared.Calendar),


        ('cardinality', "0.1"),



    ),

    (shared.TimePeriod, 'units'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.TimePeriod, 'date_type'): (

        ('type', unicode),


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



    (shared.Responsibility, 'party'): (

        ('type', shared.Party),


        ('cardinality', "1.N"),



    ),

    (shared.Responsibility, 'when'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.1"),



    ),

    (shared.Responsibility, 'role'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (shared.QualityReview, 'quality_description'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.QualityReview, 'date'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.QualityReview, 'quality_status'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.QualityReview, 'metadata_reviewer'): (

        ('type', shared.Party),


        ('cardinality', "1.1"),



    ),



    (shared.Pid, 'id'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.Pid, 'resolution_service'): (

        ('type', shared.OnlineResource),


        ('cardinality', "1.1"),



    ),



    (shared.KeyFloat, 'key'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.KeyFloat, 'value'): (

        ('type', float),


        ('cardinality', "1.1"),



    ),



    (shared.NumberArray, 'values'): (

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



    (shared.ExternalDocument, 'authorship'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ExternalDocument, 'publication_detail'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ExternalDocument, 'date'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ExternalDocument, 'online_at'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.1"),



    ),

    (shared.ExternalDocument, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (shared.ExternalDocument, 'title'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.ExternalDocument, 'doi'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ExternalDocument, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),





    (platform.Machine, 'meta'): (

        ('type', shared.DocMetaInfo),


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



    (platform.ComponentPerformance, 'component'): (

        ('type', software.SoftwareComponent),


        ('cardinality', "0.1"),



    ),

    (platform.ComponentPerformance, 'speed'): (

        ('type', float),


        ('cardinality', "1.1"),



    ),

    (platform.ComponentPerformance, 'nodes_used'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (platform.ComponentPerformance, 'cores_used'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (platform.ComponentPerformance, 'component_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (platform.Performance, 'load_imbalance'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'total_nodes_used'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'chsy'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'compiler'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'subcomponent_performance'): (

        ('type', platform.ComponentPerformance),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (platform.Performance, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'coupler_load'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'model'): (

        ('type', science.Model),


        ('cardinality', "1.1"),



    ),

    (platform.Performance, 'io_load'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'asypd'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (platform.Performance, 'sypd'): (

        ('type', float),


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



    (platform.StoragePool, 'type'): (

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

    (platform.StoragePool, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.StoragePool, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (platform.Partition, 'compute_pools'): (

        ('type', platform.ComputePool),


        ('cardinality', "1.N"),



    ),

    (platform.Partition, 'vendor'): (

        ('type', shared.Party),


        ('cardinality', "0.1"),



    ),

    (platform.Partition, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (platform.Partition, 'online_documentation'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.N"),



    ),

    (platform.Partition, 'storage_pools'): (

        ('type', platform.StoragePool),


        ('cardinality', "0.N"),



    ),

    (platform.Partition, 'when_used'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.1"),



    ),

    (platform.Partition, 'institution'): (

        ('type', shared.Party),


        ('cardinality', "1.1"),



    ),

    (platform.Partition, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.Partition, 'model_number'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.Partition, 'partition'): (

        ('type', platform.Partition),


        ('cardinality', "0.N"),



    ),



    (platform.ComputePool, 'number_of_nodes'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'cpu_type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'accelerator_type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'accelerators_per_node'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'operating_system'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'interconnect'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'compute_cores_per_node'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'memory_per_node'): (

        ('type', platform.StorageVolume),


        ('cardinality', "0.1"),



    ),

    (platform.ComputePool, 'model_number'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),





    (data.Downscaling, 'downscaled_from'): (

        ('type', data.Simulation),


        ('cardinality', "1.1"),



    ),



    (data.Dataset, 'drs_datasets'): (

        ('type', drs.DrsPublicationDataset),


        ('cardinality', "0.N"),



    ),

    (data.Dataset, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (data.Dataset, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (data.Dataset, 'related_to_dataset'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.N"),



    ),

    (data.Dataset, 'availability'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.N"),



    ),

    (data.Dataset, 'name'): (

        ('type', unicode),


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



    (data.VariableCollection, 'collection_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.VariableCollection, 'variables'): (

        ('type', unicode),


        ('cardinality', "1.N"),



    ),



    (data.Simulation, 'part_of_project'): (

        ('type', designing.Project),


        ('cardinality', "1.N"),



    ),

    (data.Simulation, 'ensemble_identifier'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (data.Simulation, 'calendar'): (

        ('type', shared.Calendar),


        ('cardinality', "0.1"),



    ),

    (data.Simulation, 'ran_for_experiments'): (

        ('type', designing.NumericalExperiment),


        ('cardinality', "1.N"),



    ),

    (data.Simulation, 'primary_ensemble'): (

        ('type', activity.Ensemble),


        ('cardinality', "0.1"),



    ),

    (data.Simulation, 'parent_simulation'): (

        ('type', activity.ParentSimulation),


        ('cardinality', "0.1"),



    ),

    (data.Simulation, 'used'): (

        ('type', science.Model),


        ('cardinality', "1.1"),



    ),





    (activity.EnsembleAxis, 'short_identifier'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.EnsembleAxis, 'extra_detail'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.EnsembleAxis, 'target_requirement'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "1.1"),



    ),

    (activity.EnsembleAxis, 'member'): (

        ('type', activity.AxisMember),


        ('cardinality', "1.N"),



    ),



    (activity.AxisMember, 'index'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (activity.AxisMember, 'value'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (activity.AxisMember, 'description'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.AxisMember, 'extra_detail'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (activity.ParentSimulation, 'branch_time_in_child'): (

        ('type', shared.DateTime),


        ('cardinality', "0.1"),



    ),

    (activity.ParentSimulation, 'parent'): (

        ('type', data.Simulation),


        ('cardinality', "1.1"),



    ),

    (activity.ParentSimulation, 'branch_time_in_parent'): (

        ('type', shared.DateTime),


        ('cardinality', "0.1"),



    ),



    (activity.EnsembleMember, 'had_performance'): (

        ('type', platform.Performance),


        ('cardinality', "0.1"),



    ),

    (activity.EnsembleMember, 'variant_id'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.EnsembleMember, 'errata'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.1"),



    ),

    (activity.EnsembleMember, 'simulation'): (

        ('type', data.Simulation),


        ('cardinality', "1.1"),



    ),

    (activity.EnsembleMember, 'ran_on'): (

        ('type', platform.Machine),


        ('cardinality', "0.1"),



    ),



    (activity.Activity, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.Activity, 'responsible_parties'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),

    (activity.Activity, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (activity.Activity, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.Activity, 'canonical_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Activity, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Activity, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Activity, 'rationale'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Activity, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (activity.Activity, 'duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.1"),



    ),



    (activity.Conformance, 'target_requirement'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "1.1"),



    ),



    (activity.Ensemble, 'part_of'): (

        ('type', activity.UberEnsemble),


        ('cardinality', "0.N"),



    ),

    (activity.Ensemble, 'documentation'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.N"),



    ),

    (activity.Ensemble, 'supported'): (

        ('type', designing.NumericalExperiment),


        ('cardinality', "1.N"),



    ),

    (activity.Ensemble, 'has_ensemble_axes'): (

        ('type', activity.EnsembleAxis),


        ('cardinality', "0.N"),



    ),

    (activity.Ensemble, 'members'): (

        ('type', activity.EnsembleMember),


        ('cardinality', "1.N"),



    ),

    (activity.Ensemble, 'common_conformances'): (

        ('type', activity.Conformance),


        ('cardinality', "0.N"),



    ),



    (activity.UberEnsemble, 'child_ensembles'): (

        ('type', activity.Ensemble),


        ('cardinality', "1.N"),



    ),





    (drs.DrsPublicationDataset, 'product'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsPublicationDataset, 'experiment'): (

        ('type', unicode),


        ('cardinality', "1.1"),



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

    (drs.DrsPublicationDataset, 'model'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsPublicationDataset, 'activity'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsPublicationDataset, 'version_number'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),



    (drs.DrsEnsembleIdentifier, 'realisation_number'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (drs.DrsEnsembleIdentifier, 'initialisation_method_number'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (drs.DrsEnsembleIdentifier, 'perturbation_number'): (

        ('type', int),


        ('cardinality', "1.1"),



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



    (drs.DrsAtomicDataset, 'ensemble_member'): (

        ('type', drs.DrsEnsembleIdentifier),


        ('cardinality', "1.1"),



    ),

    (drs.DrsAtomicDataset, 'variable_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (drs.DrsAtomicDataset, 'geographical_constraint'): (

        ('type', drs.DrsGeographicalIndicator),


        ('cardinality', "0.1"),



    ),

    (drs.DrsAtomicDataset, 'temporal_constraint'): (

        ('type', drs.DrsTemporalIdentifier),


        ('cardinality', "0.1"),



    ),

    (drs.DrsAtomicDataset, 'mip_table'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (drs.DrsGeographicalIndicator, 'bounding_box'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (drs.DrsGeographicalIndicator, 'spatial_domain'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (drs.DrsGeographicalIndicator, 'operator'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),





    (software.Gridspec, 'description'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (software.DevelopmentPath, 'funding_sources'): (

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

    (software.DevelopmentPath, 'developed_in_house'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (software.DevelopmentPath, 'creators'): (

        ('type', shared.Responsibility),


        ('cardinality', "0.N"),



    ),



    (software.ComponentBase, 'documentation'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (software.ComponentBase, 'version'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ComponentBase, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ComponentBase, 'development_history'): (

        ('type', software.DevelopmentPath),


        ('cardinality', "0.1"),



    ),

    (software.ComponentBase, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (software.ComponentBase, 'repository'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.1"),



    ),

    (software.ComponentBase, 'release_date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (software.ComponentBase, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (software.SoftwareComponent, 'language'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.SoftwareComponent, 'connection_points'): (

        ('type', software.Variable),


        ('cardinality', "0.N"),



    ),

    (software.SoftwareComponent, 'coupling_framework'): (

        ('type', unicode),


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

    (software.SoftwareComponent, 'sub_components'): (

        ('type', software.SoftwareComponent),


        ('cardinality', "0.N"),



    ),

    (software.SoftwareComponent, 'grid'): (

        ('type', software.Gridspec),


        ('cardinality', "0.1"),



    ),

    (software.SoftwareComponent, 'composition'): (

        ('type', software.Composition),


        ('cardinality', "0.1"),



    ),



    (software.EntryPoint, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (software.Composition, 'couplings'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (software.Composition, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (software.Variable, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Variable, 'prognostic'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (software.Variable, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),





    (science.ConservationProperties, 'flux_correction_was_used'): (

        ('type', bool),


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



    (science.ScientificDomain, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.ScientificDomain, 'differing_key_properties'): (

        ('type', science.KeyProperties),


        ('cardinality', "0.1"),



    ),

    (science.ScientificDomain, 'overview'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.ScientificDomain, 'id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.ScientificDomain, 'realm'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.ScientificDomain, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (science.ScientificDomain, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (science.ScientificDomain, 'simulates'): (

        ('type', science.Process),


        ('cardinality', "1.N"),



    ),



    (science.Process, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (science.Process, 'sub_processes'): (

        ('type', science.SubProcess),


        ('cardinality', "0.N"),



    ),

    (science.Process, 'implementation_overview'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Process, 'keywords'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Process, 'properties'): (

        ('type', science.Detail),


        ('cardinality', "0.N"),



    ),

    (science.Process, 'algorithms'): (

        ('type', science.Algorithm),


        ('cardinality', "0.N"),



    ),



    (science.Tuning, 'description'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Tuning, 'trend_metrics_used'): (

        ('type', data.VariableCollection),


        ('cardinality', "0.1"),



    ),

    (science.Tuning, 'regional_metrics_used'): (

        ('type', data.VariableCollection),


        ('cardinality', "0.1"),



    ),

    (science.Tuning, 'global_mean_metrics_used'): (

        ('type', data.VariableCollection),


        ('cardinality', "0.1"),



    ),



    (science.ScienceContext, 'name'): (

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



    (science.Detail, 'select'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Detail, 'content'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Detail, 'from_vocab'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Detail, 'with_cardinality'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Detail, 'detail_selection'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),



    (science.Model, 'coupler'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Model, 'internal_software_components'): (

        ('type', software.SoftwareComponent),


        ('cardinality', "0.N"),



    ),

    (science.Model, 'id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Model, 'model_default_properties'): (

        ('type', science.KeyProperties),


        ('cardinality', "0.1"),



    ),

    (science.Model, 'category'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Model, 'coupled_components'): (

        ('type', science.Model),


        ('cardinality', "0.N"),



    ),

    (science.Model, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (science.Model, 'simulates'): (

        ('type', science.ScientificDomain),


        ('cardinality', "0.N"),



    ),



    (science.Resolution, 'equivalent_resolution_km'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (science.Resolution, 'number_of_xy_gridpoints'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (science.Resolution, 'typical_x_degrees'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (science.Resolution, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Resolution, 'typical_y_degrees'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (science.Resolution, 'is_adaptive_grid'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (science.Resolution, 'number_of_levels'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),



    (science.SubProcess, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (science.SubProcess, 'implementation_overview'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.SubProcess, 'properties'): (

        ('type', science.Detail),


        ('cardinality', "0.N"),



    ),



    (science.Extent, 'southern_boundary'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (science.Extent, 'top_vertical_level'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (science.Extent, 'eastern_boundary'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (science.Extent, 'is_global'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (science.Extent, 'northern_boundary'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (science.Extent, 'z_units'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Extent, 'western_boundary'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (science.Extent, 'region_known_as'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (science.Extent, 'bottom_vertical_level'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),



    (science.Grid, 'grid_extent'): (

        ('type', science.Extent),


        ('cardinality', "0.1"),



    ),

    (science.Grid, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (science.Grid, 'horizontal_grid_layout'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Grid, 'additional_details'): (

        ('type', science.Detail),


        ('cardinality', "0.N"),



    ),

    (science.Grid, 'vertical_grid_layout'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Grid, 'horizontal_grid_type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Grid, 'vertical_grid_type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (science.Grid, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),



    (science.KeyProperties, 'additional_detail'): (

        ('type', science.Detail),


        ('cardinality', "0.N"),



    ),

    (science.KeyProperties, 'time_step'): (

        ('type', float),


        ('cardinality', "1.1"),



    ),

    (science.KeyProperties, 'extra_conservation_properties'): (

        ('type', science.ConservationProperties),


        ('cardinality', "0.1"),



    ),

    (science.KeyProperties, 'tuning_applied'): (

        ('type', science.Tuning),


        ('cardinality', "0.1"),



    ),

    (science.KeyProperties, 'grid'): (

        ('type', science.Grid),


        ('cardinality', "1.1"),



    ),

    (science.KeyProperties, 'resolution'): (

        ('type', science.Resolution),


        ('cardinality', "1.1"),



    ),



    (science.Algorithm, 'diagnostic_variables'): (

        ('type', data.VariableCollection),


        ('cardinality', "0.1"),



    ),

    (science.Algorithm, 'prognostic_variables'): (

        ('type', data.VariableCollection),


        ('cardinality', "0.1"),



    ),

    (science.Algorithm, 'forced_variables'): (

        ('type', data.VariableCollection),


        ('cardinality', "0.1"),



    ),

    (science.Algorithm, 'references'): (

        ('type', shared.Reference),


        ('cardinality', "0.N"),



    ),

    (science.Algorithm, 'implementation_overview'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),





    (designing.NumericalExperiment, 'requirements'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "0.N"),



    ),

    (designing.NumericalExperiment, 'related_experiments'): (

        ('type', designing.NumericalExperiment),


        ('cardinality', "0.N"),



    ),



    (designing.NumericalRequirement, 'additional_requirements'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "0.N"),



    ),

    (designing.NumericalRequirement, 'conformance_is_requested'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),



    (designing.TemporalConstraint, 'required_calendar'): (

        ('type', shared.Calendar),


        ('cardinality', "0.1"),



    ),

    (designing.TemporalConstraint, 'start_flexibility'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.1"),



    ),

    (designing.TemporalConstraint, 'start_date'): (

        ('type', shared.DateTime),


        ('cardinality', "0.1"),



    ),

    (designing.TemporalConstraint, 'required_duration'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.1"),



    ),



    (designing.MultiTimeEnsemble, 'ensemble_members'): (

        ('type', shared.DatetimeSet),


        ('cardinality', "1.1"),



    ),



    (designing.EnsembleRequirement, 'ensemble_type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.EnsembleRequirement, 'ensemble_member'): (

        ('type', designing.NumericalRequirement),


        ('cardinality', "0.N"),



    ),

    (designing.EnsembleRequirement, 'minimum_size'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),



    (designing.DomainProperties, 'required_extent'): (

        ('type', science.Extent),


        ('cardinality', "0.1"),



    ),

    (designing.DomainProperties, 'required_resolution'): (

        ('type', science.Resolution),


        ('cardinality', "0.1"),



    ),



    (designing.ForcingConstraint, 'code'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.ForcingConstraint, 'forcing_type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (designing.ForcingConstraint, 'data_link'): (

        ('type', shared.OnlineResource),


        ('cardinality', "0.1"),



    ),

    (designing.ForcingConstraint, 'additional_constraint'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.ForcingConstraint, 'category'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (designing.ForcingConstraint, 'origin'): (

        ('type', shared.Reference),


        ('cardinality', "0.1"),



    ),

    (designing.ForcingConstraint, 'group'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (designing.SimulationPlan, 'expected_platform'): (

        ('type', platform.Machine),


        ('cardinality', "0.1"),



    ),

    (designing.SimulationPlan, 'will_support_experiments'): (

        ('type', designing.NumericalExperiment),


        ('cardinality', "1.N"),



    ),

    (designing.SimulationPlan, 'expected_model'): (

        ('type', science.Model),


        ('cardinality', "1.1"),



    ),

    (designing.SimulationPlan, 'expected_performance_sypd'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),



    (designing.MultiEnsemble, 'ensemble_axis'): (

        ('type', designing.EnsembleRequirement),


        ('cardinality', "1.N"),



    ),



    (designing.OutputTemporalRequirement, 'throughout'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (designing.OutputTemporalRequirement, 'continuous_subset'): (

        ('type', shared.TimePeriod),


        ('cardinality', "0.N"),



    ),

    (designing.OutputTemporalRequirement, 'sliced_subset'): (

        ('type', shared.TimesliceList),


        ('cardinality', "0.1"),



    ),



    (designing.Project, 'previous_projects'): (

        ('type', designing.Project),


        ('cardinality', "0.N"),



    ),

    (designing.Project, 'sub_projects'): (

        ('type', designing.Project),


        ('cardinality', "0.N"),



    ),

    (designing.Project, 'requires_experiments'): (

        ('type', designing.NumericalExperiment),


        ('cardinality', "0.N"),



    ),



}