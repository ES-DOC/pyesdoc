
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.constraints.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The ontology constraint set.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import datetime
import uuid

import typeset_for_data_package as data
import typeset_for_software_package as software
import typeset_for_shared_package as shared
import typeset_for_grids_package as grids
import typeset_for_quality_package as quality
import typeset_for_misc_package as misc
import typeset_for_activity_package as activity




# Map of ontology types to constraints.
CONSTRAINTS = {
    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    shared.DocReference: (

        ('description', 'type', unicode),

        ('url', 'type', unicode),

        ('type', 'type', unicode),

        ('version', 'type', int),

        ('changes', 'type', shared.Change),

        ('external_id', 'type', unicode),

        ('id', 'type', uuid.UUID),

        ('name', 'type', unicode),


        ('description', 'cardinality', "0.1"),

        ('url', 'cardinality', "0.1"),

        ('type', 'cardinality', "0.1"),

        ('version', 'cardinality', "0.1"),

        ('changes', 'cardinality', "0.N"),

        ('external_id', 'cardinality', "0.1"),

        ('id', 'cardinality', "0.1"),

        ('name', 'cardinality', "0.1"),



    ),

    data.DataContent: (

        ('topic', 'type', data.DataTopic),

        ('frequency', 'type', unicode),

        ('purpose', 'type', unicode),

        ('aggregation', 'type', unicode),


        ('topic', 'cardinality', "1.1"),

        ('frequency', 'cardinality', "0.1"),

        ('purpose', 'cardinality', "0.1"),

        ('aggregation', 'cardinality', "0.1"),



    ),

    shared.PerpetualPeriod: (

        ('length', 'type', int),

        ('range', 'type', shared.DateRange),

        ('description', 'type', unicode),


        ('length', 'cardinality', "0.1"),

        ('range', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



    ),

    shared.OpenDateRange: (

        ('duration', 'type', unicode),

        ('start', 'type', datetime.datetime),

        ('end', 'type', datetime.datetime),


        ('duration', 'cardinality', "0.1"),

        ('start', 'cardinality', "0.1"),

        ('end', 'cardinality', "0.1"),



    ),

    shared.Relationship: (

        ('direction', 'type', unicode),

        ('description', 'type', unicode),


        ('direction', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),



    ),

    data.DataStorage: (

        ('format', 'type', unicode),

        ('location', 'type', unicode),

        ('modification_date', 'type', datetime.datetime),

        ('size', 'type', int),


        ('format', 'cardinality', "0.1"),

        ('location', 'cardinality', "0.1"),

        ('modification_date', 'cardinality', "0.1"),

        ('size', 'cardinality', "0.1"),



    ),

    shared.Citation: (

        ('title', 'type', unicode),

        ('organisation', 'type', unicode),

        ('collective_title', 'type', unicode),

        ('role', 'type', unicode),

        ('location', 'type', unicode),

        ('date', 'type', datetime.datetime),

        ('type', 'type', unicode),

        ('date_type', 'type', unicode),

        ('alternative_title', 'type', unicode),


        ('title', 'cardinality', "0.1"),

        ('organisation', 'cardinality', "0.1"),

        ('collective_title', 'cardinality', "0.1"),

        ('role', 'cardinality', "0.1"),

        ('location', 'cardinality', "0.1"),

        ('date', 'cardinality', "0.1"),

        ('type', 'cardinality', "0.1"),

        ('date_type', 'cardinality', "0.1"),

        ('alternative_title', 'cardinality', "0.1"),



    ),

    software.Parallelisation: (

        ('ranks', 'type', software.Rank),

        ('processes', 'type', int),


        ('ranks', 'cardinality', "0.N"),

        ('processes', 'cardinality', "1.1"),



    ),

    grids.GridTile: (

        ('mnemonic', 'type', unicode),

        ('refinement_scheme', 'type', unicode),

        ('is_regular', 'type', bool),

        ('long_name', 'type', unicode),

        ('horizontal_crs', 'type', unicode),

        ('cell_array', 'type', unicode),

        ('id', 'type', unicode),

        ('cell_ref_array', 'type', unicode),

        ('area', 'type', unicode),

        ('simple_grid_geom', 'type', grids.SimpleGridGeometry),

        ('vertical_crs', 'type', unicode),

        ('nx', 'type', int),

        ('ny', 'type', int),

        ('nz', 'type', int),

        ('vertical_resolution', 'type', grids.GridTileResolutionType),

        ('discretization_type', 'type', unicode),

        ('coordinate_pole', 'type', unicode),

        ('description', 'type', unicode),

        ('short_name', 'type', unicode),

        ('extent', 'type', grids.GridExtent),

        ('zcoords', 'type', grids.VerticalCoordinateList),

        ('is_conformal', 'type', bool),

        ('is_uniform', 'type', bool),

        ('coord_file', 'type', unicode),

        ('geometry_type', 'type', unicode),

        ('grid_north_pole', 'type', unicode),

        ('horizontal_resolution', 'type', grids.GridTileResolutionType),

        ('is_terrain_following', 'type', bool),


        ('mnemonic', 'cardinality', "0.1"),

        ('refinement_scheme', 'cardinality', "0.1"),

        ('is_regular', 'cardinality', "0.1"),

        ('long_name', 'cardinality', "0.1"),

        ('horizontal_crs', 'cardinality', "0.1"),

        ('cell_array', 'cardinality', "0.1"),

        ('id', 'cardinality', "0.1"),

        ('cell_ref_array', 'cardinality', "0.1"),

        ('area', 'cardinality', "0.1"),

        ('simple_grid_geom', 'cardinality', "0.1"),

        ('vertical_crs', 'cardinality', "0.1"),

        ('nx', 'cardinality', "0.1"),

        ('ny', 'cardinality', "0.1"),

        ('nz', 'cardinality', "0.1"),

        ('vertical_resolution', 'cardinality', "0.1"),

        ('discretization_type', 'cardinality', "0.1"),

        ('coordinate_pole', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('short_name', 'cardinality', "0.1"),

        ('extent', 'cardinality', "0.1"),

        ('zcoords', 'cardinality', "0.1"),

        ('is_conformal', 'cardinality', "0.1"),

        ('is_uniform', 'cardinality', "0.1"),

        ('coord_file', 'cardinality', "0.1"),

        ('geometry_type', 'cardinality', "0.1"),

        ('grid_north_pole', 'cardinality', "0.1"),

        ('horizontal_resolution', 'cardinality', "0.1"),

        ('is_terrain_following', 'cardinality', "0.1"),



    ),

    software.ModelComponent: (

        ('funding_sources', 'type', unicode),

        ('version', 'type', unicode),

        ('long_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('is_embedded', 'type', bool),

        ('short_name', 'type', unicode),

        ('previous_version', 'type', unicode),

        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('deployments', 'type', software.Deployment),

        ('citations', 'type', shared.Citation),

        ('type', 'type', unicode),

        ('composition', 'type', software.Composition),

        ('coupling_framework', 'type', unicode),

        ('description', 'type', unicode),

        ('parent', 'type', software.Component),

        ('sub_components', 'type', software.Component),

        ('dependencies', 'type', software.EntryPoint),

        ('grid', 'type', grids.GridSpec),

        ('purpose', 'type', unicode),

        ('online_resource', 'type', unicode),

        ('timing', 'type', software.Timing),

        ('properties', 'type', software.ComponentProperty),

        ('types', 'type', unicode),

        ('language', 'type', software.ComponentLanguage),

        ('license', 'type', shared.License),

        ('release_date', 'type', datetime.datetime),

        ('code_access', 'type', unicode),

        ('activity', 'type', activity.Activity),


        ('funding_sources', 'cardinality', "0.N"),

        ('version', 'cardinality', "0.1"),

        ('long_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('is_embedded', 'cardinality', "0.1"),

        ('short_name', 'cardinality', "1.1"),

        ('previous_version', 'cardinality', "0.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('deployments', 'cardinality', "0.N"),

        ('citations', 'cardinality', "0.N"),

        ('type', 'cardinality', "0.1"),

        ('composition', 'cardinality', "0.1"),

        ('coupling_framework', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('parent', 'cardinality', "0.1"),

        ('sub_components', 'cardinality', "0.N"),

        ('dependencies', 'cardinality', "0.N"),

        ('grid', 'cardinality', "0.1"),

        ('purpose', 'cardinality', "0.1"),

        ('online_resource', 'cardinality', "0.1"),

        ('timing', 'cardinality', "0.1"),

        ('properties', 'cardinality', "0.N"),

        ('types', 'cardinality', "1.N"),

        ('language', 'cardinality', "0.1"),

        ('license', 'cardinality', "0.1"),

        ('release_date', 'cardinality', "0.1"),

        ('code_access', 'cardinality', "0.1"),

        ('activity', 'cardinality', "0.1"),



    ),

    activity.Conformance: (

        ('requirements', 'type', activity.NumericalRequirement),

        ('description', 'type', unicode),

        ('sources', 'type', shared.DataSource),

        ('frequency', 'type', unicode),

        ('is_conformant', 'type', bool),

        ('type', 'type', unicode),


        ('requirements', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('sources', 'cardinality', "0.N"),

        ('frequency', 'cardinality', "0.1"),

        ('is_conformant', 'cardinality', "1.1"),

        ('type', 'cardinality', "0.1"),



    ),

    quality.Report: (

        ('date', 'type', datetime.datetime),

        ('evaluator', 'type', shared.ResponsibleParty),

        ('evaluation', 'type', quality.Evaluation),

        ('measure', 'type', quality.Measure),


        ('date', 'cardinality', "0.1"),

        ('evaluator', 'cardinality', "0.1"),

        ('evaluation', 'cardinality', "1.1"),

        ('measure', 'cardinality', "1.1"),



    ),

    software.ProcessorComponent: (

        ('funding_sources', 'type', unicode),

        ('version', 'type', unicode),

        ('long_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('is_embedded', 'type', bool),

        ('short_name', 'type', unicode),

        ('previous_version', 'type', unicode),

        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('deployments', 'type', software.Deployment),

        ('citations', 'type', shared.Citation),

        ('composition', 'type', software.Composition),

        ('coupling_framework', 'type', unicode),

        ('description', 'type', unicode),

        ('parent', 'type', software.Component),

        ('sub_components', 'type', software.Component),

        ('dependencies', 'type', software.EntryPoint),

        ('grid', 'type', grids.GridSpec),

        ('purpose', 'type', unicode),

        ('online_resource', 'type', unicode),

        ('properties', 'type', software.ComponentProperty),

        ('language', 'type', software.ComponentLanguage),

        ('license', 'type', shared.License),

        ('release_date', 'type', datetime.datetime),

        ('code_access', 'type', unicode),


        ('funding_sources', 'cardinality', "0.N"),

        ('version', 'cardinality', "0.1"),

        ('long_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('is_embedded', 'cardinality', "0.1"),

        ('short_name', 'cardinality', "1.1"),

        ('previous_version', 'cardinality', "0.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('deployments', 'cardinality', "0.N"),

        ('citations', 'cardinality', "0.N"),

        ('composition', 'cardinality', "0.1"),

        ('coupling_framework', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('parent', 'cardinality', "0.1"),

        ('sub_components', 'cardinality', "0.N"),

        ('dependencies', 'cardinality', "0.N"),

        ('grid', 'cardinality', "0.1"),

        ('purpose', 'cardinality', "0.1"),

        ('online_resource', 'cardinality', "0.1"),

        ('properties', 'cardinality', "0.N"),

        ('language', 'cardinality', "0.1"),

        ('license', 'cardinality', "0.1"),

        ('release_date', 'cardinality', "0.1"),

        ('code_access', 'cardinality', "0.1"),



    ),

    shared.DocMetaInfo: (

        ('drs_keys', 'type', unicode),

        ('drs_path', 'type', unicode),

        ('create_date', 'type', datetime.datetime),

        ('language', 'type', unicode),

        ('genealogy', 'type', shared.DocGenealogy),

        ('update_date', 'type', datetime.datetime),

        ('sort_key', 'type', unicode),

        ('author', 'type', shared.ResponsibleParty),

        ('source_key', 'type', unicode),

        ('project', 'type', unicode),

        ('institute', 'type', unicode),

        ('version', 'type', int),

        ('status', 'type', unicode),

        ('source', 'type', unicode),

        ('type_sort_key', 'type', unicode),

        ('external_ids', 'type', shared.StandardName),

        ('type', 'type', unicode),

        ('id', 'type', uuid.UUID),

        ('type_display_name', 'type', unicode),


        ('drs_keys', 'cardinality', "0.N"),

        ('drs_path', 'cardinality', "0.1"),

        ('create_date', 'cardinality', "1.1"),

        ('language', 'cardinality', "1.1"),

        ('genealogy', 'cardinality', "0.1"),

        ('update_date', 'cardinality', "1.1"),

        ('sort_key', 'cardinality', "0.1"),

        ('author', 'cardinality', "0.1"),

        ('source_key', 'cardinality', "0.1"),

        ('project', 'cardinality', "1.1"),

        ('institute', 'cardinality', "0.1"),

        ('version', 'cardinality', "1.1"),

        ('status', 'cardinality', "0.1"),

        ('source', 'cardinality', "1.1"),

        ('type_sort_key', 'cardinality', "0.1"),

        ('external_ids', 'cardinality', "0.N"),

        ('type', 'cardinality', "1.1"),

        ('id', 'cardinality', "1.1"),

        ('type_display_name', 'cardinality', "0.1"),


        ('source', 'constant', "scripts"),


    ),

    software.ComponentLanguage: (

        ('name', 'type', unicode),

        ('properties', 'type', software.ComponentLanguageProperty),


        ('name', 'cardinality', "1.1"),

        ('properties', 'cardinality', "0.N"),



    ),

    activity.NumericalActivity: (

        ('funding_sources', 'type', unicode),

        ('rationales', 'type', unicode),

        ('description', 'type', unicode),

        ('short_name', 'type', unicode),

        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('long_name', 'type', unicode),

        ('supports', 'type', activity.Experiment),

        ('projects', 'type', unicode),


        ('funding_sources', 'cardinality', "0.N"),

        ('rationales', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('short_name', 'cardinality', "1.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('supports', 'cardinality', "0.N"),

        ('projects', 'cardinality', "0.N"),



    ),

    activity.Activity: (

        ('funding_sources', 'type', unicode),

        ('rationales', 'type', unicode),

        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('projects', 'type', unicode),


        ('funding_sources', 'cardinality', "0.N"),

        ('rationales', 'cardinality', "0.N"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('projects', 'cardinality', "0.N"),



    ),

    software.CouplingProperty: (

        ('name', 'type', unicode),

        ('value', 'type', unicode),


        ('name', 'cardinality', "0.1"),

        ('value', 'cardinality', "0.1"),



    ),

    software.SpatialRegridding: (

        ('user_method', 'type', software.SpatialRegriddingUserMethod),

        ('properties', 'type', software.SpatialRegriddingProperty),

        ('standard_method', 'type', unicode),

        ('dimension', 'type', unicode),


        ('user_method', 'cardinality', "0.1"),

        ('properties', 'cardinality', "0.N"),

        ('standard_method', 'cardinality', "0.1"),

        ('dimension', 'cardinality', "0.1"),



    ),

    shared.DocGenealogy: (

        ('relationships', 'type', shared.DocRelationship),


        ('relationships', 'cardinality', "0.N"),



    ),

    shared.Calendar: (

        ('length', 'type', int),

        ('range', 'type', shared.DateRange),

        ('description', 'type', unicode),


        ('length', 'cardinality', "0.1"),

        ('range', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



    ),

    activity.PhysicalModification: (

        ('requirements', 'type', activity.NumericalRequirement),

        ('description', 'type', unicode),

        ('sources', 'type', shared.DataSource),

        ('frequency', 'type', unicode),

        ('is_conformant', 'type', bool),

        ('type', 'type', unicode),


        ('requirements', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('sources', 'cardinality', "0.N"),

        ('frequency', 'cardinality', "0.1"),

        ('is_conformant', 'cardinality', "1.1"),

        ('type', 'cardinality', "0.1"),



    ),

    shared.DocRelationship: (

        ('direction', 'type', unicode),

        ('type', 'type', unicode),

        ('description', 'type', unicode),

        ('target', 'type', shared.DocRelationshipTarget),


        ('direction', 'cardinality', "1.1"),

        ('type', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),

        ('target', 'cardinality', "1.1"),



    ),

    shared.ClosedDateRange: (

        ('duration', 'type', unicode),

        ('start', 'type', datetime.datetime),

        ('end', 'type', datetime.datetime),


        ('duration', 'cardinality', "0.1"),

        ('start', 'cardinality', "1.1"),

        ('end', 'cardinality', "0.1"),



    ),

    activity.ExperimentRelationship: (

        ('direction', 'type', unicode),

        ('type', 'type', unicode),

        ('description', 'type', unicode),

        ('target', 'type', activity.ExperimentRelationshipTarget),


        ('direction', 'cardinality', "1.1"),

        ('type', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),

        ('target', 'cardinality', "1.1"),



    ),

    shared.RealCalendar: (

        ('length', 'type', int),

        ('range', 'type', shared.DateRange),

        ('description', 'type', unicode),


        ('length', 'cardinality', "0.1"),

        ('range', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



    ),

    data.DataHierarchyLevel: (

        ('is_open', 'type', bool),

        ('name', 'type', unicode),

        ('value', 'type', unicode),


        ('is_open', 'cardinality', "0.1"),

        ('name', 'cardinality', "0.1"),

        ('value', 'cardinality', "0.1"),



    ),

    shared.Change: (

        ('name', 'type', unicode),

        ('author', 'type', shared.ResponsibleParty),

        ('details', 'type', shared.ChangeProperty),

        ('date', 'type', datetime.datetime),

        ('type', 'type', unicode),

        ('description', 'type', unicode),


        ('name', 'cardinality', "0.1"),

        ('author', 'cardinality', "0.1"),

        ('details', 'cardinality', "1.N"),

        ('date', 'cardinality', "0.1"),

        ('type', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



    ),

    software.SpatialRegriddingProperty: (

        ('name', 'type', unicode),

        ('value', 'type', unicode),


        ('name', 'cardinality', "0.1"),

        ('value', 'cardinality', "0.1"),



    ),

    activity.SimulationRun: (

        ('funding_sources', 'type', unicode),

        ('long_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('calendar', 'type', shared.Calendar),

        ('conformances', 'type', activity.Conformance),

        ('rationales', 'type', unicode),

        ('control_simulation', 'type', activity.Simulation),

        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('deployments', 'type', software.Deployment),

        ('restarts', 'type', data.DataObject),

        ('supports', 'type', activity.Experiment),

        ('inputs', 'type', software.Coupling),

        ('simulation_id', 'type', unicode),

        ('description', 'type', unicode),

        ('short_name', 'type', unicode),

        ('outputs', 'type', data.DataObject),

        ('spinup_date_range', 'type', shared.ClosedDateRange),

        ('date_range', 'type', shared.DateRange),

        ('authors', 'type', unicode),

        ('projects', 'type', unicode),

        ('spinup_simulation', 'type', activity.Simulation),

        ('model', 'type', software.ModelComponent),


        ('funding_sources', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('calendar', 'cardinality', "1.1"),

        ('conformances', 'cardinality', "0.N"),

        ('rationales', 'cardinality', "0.N"),

        ('control_simulation', 'cardinality', "0.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('deployments', 'cardinality', "0.N"),

        ('restarts', 'cardinality', "0.N"),

        ('supports', 'cardinality', "0.N"),

        ('inputs', 'cardinality', "0.N"),

        ('simulation_id', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('short_name', 'cardinality', "1.1"),

        ('outputs', 'cardinality', "0.N"),

        ('spinup_date_range', 'cardinality', "0.1"),

        ('date_range', 'cardinality', "1.1"),

        ('authors', 'cardinality', "0.1"),

        ('projects', 'cardinality', "0.N"),

        ('spinup_simulation', 'cardinality', "0.1"),

        ('model', 'cardinality', "0.1"),



    ),

    quality.Evaluation: (

        ('description', 'type', unicode),

        ('type_hyperlink', 'type', unicode),

        ('explanation', 'type', unicode),

        ('specification_hyperlink', 'type', unicode),

        ('did_pass', 'type', bool),

        ('date', 'type', datetime.datetime),

        ('title', 'type', unicode),

        ('type', 'type', unicode),

        ('specification', 'type', unicode),


        ('description', 'cardinality', "0.1"),

        ('type_hyperlink', 'cardinality', "0.1"),

        ('explanation', 'cardinality', "0.1"),

        ('specification_hyperlink', 'cardinality', "0.1"),

        ('did_pass', 'cardinality', "0.1"),

        ('date', 'cardinality', "0.1"),

        ('title', 'cardinality', "0.1"),

        ('type', 'cardinality', "0.1"),

        ('specification', 'cardinality', "0.1"),



    ),

    activity.SimulationRelationshipTarget: (

        ('target', 'type', unicode),

        ('simulation', 'type', shared.DocReference),


        ('target', 'cardinality', "0.1"),

        ('simulation', 'cardinality', "0.1"),



    ),

    data.DataObject: (

        ('hierarchy_level', 'type', data.DataHierarchyLevel),

        ('source_simulation', 'type', unicode),

        ('description', 'type', unicode),

        ('keyword', 'type', unicode),

        ('restriction', 'type', data.DataRestriction),

        ('acronym', 'type', unicode),

        ('citations', 'type', shared.Citation),

        ('storage', 'type', data.DataStorage),

        ('child_object', 'type', data.DataObject),

        ('content', 'type', data.DataContent),

        ('geometry_model', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('purpose', 'type', unicode),

        ('extent', 'type', data.DataExtent),

        ('distribution', 'type', data.DataDistribution),

        ('parent_object', 'type', data.DataObject),

        ('properties', 'type', data.DataProperty),

        ('data_status', 'type', unicode),


        ('hierarchy_level', 'cardinality', "0.1"),

        ('source_simulation', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('keyword', 'cardinality', "0.1"),

        ('restriction', 'cardinality', "0.N"),

        ('acronym', 'cardinality', "0.1"),

        ('citations', 'cardinality', "0.N"),

        ('storage', 'cardinality', "0.N"),

        ('child_object', 'cardinality', "0.N"),

        ('content', 'cardinality', "0.N"),

        ('geometry_model', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('purpose', 'cardinality', "0.1"),

        ('extent', 'cardinality', "0.1"),

        ('distribution', 'cardinality', "0.1"),

        ('parent_object', 'cardinality', "0.1"),

        ('properties', 'cardinality', "0.N"),

        ('data_status', 'cardinality', "0.1"),



    ),

    data.DataTopic: (

        ('name', 'type', unicode),

        ('unit', 'type', unicode),

        ('description', 'type', unicode),


        ('name', 'cardinality', "0.1"),

        ('unit', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



    ),

    grids.GridExtent: (

        ('units', 'type', unicode),

        ('maximum_latitude', 'type', unicode),

        ('minimum_latitude', 'type', unicode),

        ('maximum_longitude', 'type', unicode),

        ('minimum_longitude', 'type', unicode),


        ('units', 'cardinality', "0.1"),

        ('maximum_latitude', 'cardinality', "1.1"),

        ('minimum_latitude', 'cardinality', "1.1"),

        ('maximum_longitude', 'cardinality', "1.1"),

        ('minimum_longitude', 'cardinality', "1.1"),



    ),

    software.Timing: (

        ('units', 'type', unicode),

        ('start', 'type', datetime.datetime),

        ('rate', 'type', int),

        ('end', 'type', datetime.datetime),

        ('is_variable_rate', 'type', bool),


        ('units', 'cardinality', "0.1"),

        ('start', 'cardinality', "0.1"),

        ('rate', 'cardinality', "0.1"),

        ('end', 'cardinality', "0.1"),

        ('is_variable_rate', 'cardinality', "0.1"),



    ),

    activity.NumericalRequirement: (

        ('description', 'type', unicode),

        ('options', 'type', activity.NumericalRequirementOption),

        ('source', 'type', shared.DataSource),

        ('requirement_type', 'type', unicode),

        ('id', 'type', unicode),

        ('name', 'type', unicode),


        ('description', 'cardinality', "0.1"),

        ('options', 'cardinality', "0.N"),

        ('source', 'cardinality', "0.1"),

        ('requirement_type', 'cardinality', "1.1"),

        ('id', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),



    ),

    grids.SimpleGridGeometry: (

        ('dim_order', 'type', unicode),

        ('num_dims', 'type', int),

        ('xcoords', 'type', grids.CoordinateList),

        ('is_mesh', 'type', bool),

        ('ycoords', 'type', grids.CoordinateList),

        ('zcoords', 'type', grids.CoordinateList),


        ('dim_order', 'cardinality', "0.1"),

        ('num_dims', 'cardinality', "1.1"),

        ('xcoords', 'cardinality', "1.1"),

        ('is_mesh', 'cardinality', "0.1"),

        ('ycoords', 'cardinality', "1.1"),

        ('zcoords', 'cardinality', "0.1"),



    ),

    activity.InitialCondition: (

        ('description', 'type', unicode),

        ('options', 'type', activity.NumericalRequirementOption),

        ('source', 'type', shared.DataSource),

        ('requirement_type', 'type', unicode),

        ('id', 'type', unicode),

        ('name', 'type', unicode),


        ('description', 'cardinality', "0.1"),

        ('options', 'cardinality', "0.N"),

        ('source', 'cardinality', "0.1"),

        ('requirement_type', 'cardinality', "1.1"),

        ('id', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),


        ('requirement_type', 'constant', "initialCondition"),


    ),

    activity.SpatioTemporalConstraint: (

        ('description', 'type', unicode),

        ('options', 'type', activity.NumericalRequirementOption),

        ('date_range', 'type', shared.DateRange),

        ('source', 'type', shared.DataSource),

        ('spatial_resolution', 'type', unicode),

        ('requirement_type', 'type', unicode),

        ('id', 'type', unicode),

        ('name', 'type', unicode),


        ('description', 'cardinality', "0.1"),

        ('options', 'cardinality', "0.N"),

        ('date_range', 'cardinality', "0.1"),

        ('source', 'cardinality', "0.1"),

        ('spatial_resolution', 'cardinality', "0.1"),

        ('requirement_type', 'cardinality', "1.1"),

        ('id', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),


        ('requirement_type', 'constant', "spatioTemporalConstraint"),


    ),

    data.DataExtent: (

        ('temporal', 'type', data.DataExtentTemporal),

        ('geographical', 'type', data.DataExtentGeographical),


        ('temporal', 'cardinality', "1.1"),

        ('geographical', 'cardinality', "1.1"),



    ),

    data.DataStorageFile: (

        ('modification_date', 'type', datetime.datetime),

        ('format', 'type', unicode),

        ('file_name', 'type', unicode),

        ('location', 'type', unicode),

        ('path', 'type', unicode),

        ('file_system', 'type', unicode),

        ('size', 'type', int),


        ('modification_date', 'cardinality', "0.1"),

        ('format', 'cardinality', "0.1"),

        ('file_name', 'cardinality', "0.1"),

        ('location', 'cardinality', "0.1"),

        ('path', 'cardinality', "0.1"),

        ('file_system', 'cardinality', "0.1"),

        ('size', 'cardinality', "0.1"),



    ),

    activity.DownscalingSimulation: (

        ('inputs', 'type', software.Coupling),

        ('funding_sources', 'type', unicode),

        ('rationales', 'type', unicode),

        ('description', 'type', unicode),

        ('short_name', 'type', unicode),

        ('outputs', 'type', data.DataObject),

        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('long_name', 'type', unicode),

        ('downscaled_from', 'type', shared.DataSource),

        ('downscaling_id', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('downscaling_type', 'type', unicode),

        ('calendar', 'type', shared.Calendar),

        ('supports', 'type', activity.Experiment),

        ('projects', 'type', unicode),


        ('inputs', 'cardinality', "0.N"),

        ('funding_sources', 'cardinality', "0.N"),

        ('rationales', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('short_name', 'cardinality', "1.1"),

        ('outputs', 'cardinality', "0.N"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('downscaled_from', 'cardinality', "1.1"),

        ('downscaling_id', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('downscaling_type', 'cardinality', "0.1"),

        ('calendar', 'cardinality', "1.1"),

        ('supports', 'cardinality', "0.N"),

        ('projects', 'cardinality', "0.N"),



    ),

    shared.Daily360: (

        ('length', 'type', int),

        ('range', 'type', shared.DateRange),

        ('description', 'type', unicode),


        ('length', 'cardinality', "0.1"),

        ('range', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



    ),

    activity.SimulationComposite: (

        ('funding_sources', 'type', unicode),

        ('child', 'type', activity.Simulation),

        ('rank', 'type', int),

        ('long_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('calendar', 'type', shared.Calendar),

        ('conformances', 'type', activity.Conformance),

        ('rationales', 'type', unicode),

        ('control_simulation', 'type', activity.Simulation),

        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('deployments', 'type', software.Deployment),

        ('restarts', 'type', data.DataObject),

        ('supports', 'type', activity.Experiment),

        ('inputs', 'type', software.Coupling),

        ('simulation_id', 'type', unicode),

        ('description', 'type', unicode),

        ('short_name', 'type', unicode),

        ('outputs', 'type', data.DataObject),

        ('spinup_date_range', 'type', shared.ClosedDateRange),

        ('date_range', 'type', shared.DateRange),

        ('authors', 'type', unicode),

        ('projects', 'type', unicode),

        ('spinup_simulation', 'type', activity.Simulation),


        ('funding_sources', 'cardinality', "0.N"),

        ('child', 'cardinality', "0.N"),

        ('rank', 'cardinality', "1.1"),

        ('long_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('calendar', 'cardinality', "1.1"),

        ('conformances', 'cardinality', "0.N"),

        ('rationales', 'cardinality', "0.N"),

        ('control_simulation', 'cardinality', "0.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('deployments', 'cardinality', "0.N"),

        ('restarts', 'cardinality', "0.N"),

        ('supports', 'cardinality', "0.N"),

        ('inputs', 'cardinality', "0.N"),

        ('simulation_id', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('short_name', 'cardinality', "1.1"),

        ('outputs', 'cardinality', "0.N"),

        ('spinup_date_range', 'cardinality', "0.1"),

        ('date_range', 'cardinality', "1.1"),

        ('authors', 'cardinality', "0.1"),

        ('projects', 'cardinality', "0.N"),

        ('spinup_simulation', 'cardinality', "0.1"),



    ),

    software.SpatialRegriddingUserMethod: (

        ('name', 'type', unicode),

        ('file', 'type', data.DataObject),


        ('name', 'cardinality', "1.1"),

        ('file', 'cardinality', "0.1"),



    ),

    software.Deployment: (

        ('executable_arguments', 'type', unicode),

        ('description', 'type', unicode),

        ('parallelisation', 'type', software.Parallelisation),

        ('deployment_date', 'type', datetime.datetime),

        ('platform', 'type', shared.Platform),

        ('executable_name', 'type', unicode),


        ('executable_arguments', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('parallelisation', 'cardinality', "0.1"),

        ('deployment_date', 'cardinality', "0.1"),

        ('platform', 'cardinality', "0.1"),

        ('executable_name', 'cardinality', "0.1"),



    ),

    data.DataProperty: (

        ('name', 'type', unicode),

        ('value', 'type', unicode),

        ('description', 'type', unicode),


        ('name', 'cardinality', "0.1"),

        ('value', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



    ),

    data.DataStorageIp: (

        ('protocol', 'type', unicode),

        ('modification_date', 'type', datetime.datetime),

        ('format', 'type', unicode),

        ('file_name', 'type', unicode),

        ('host', 'type', unicode),

        ('location', 'type', unicode),

        ('path', 'type', unicode),

        ('size', 'type', int),


        ('protocol', 'cardinality', "0.1"),

        ('modification_date', 'cardinality', "0.1"),

        ('format', 'cardinality', "0.1"),

        ('file_name', 'cardinality', "0.1"),

        ('host', 'cardinality', "0.1"),

        ('location', 'cardinality', "0.1"),

        ('path', 'cardinality', "0.1"),

        ('size', 'cardinality', "0.1"),



    ),

    grids.GridSpec: (

        ('meta', 'type', shared.DocMetaInfo),

        ('esm_exchange_grids', 'type', grids.GridMosaic),

        ('esm_model_grids', 'type', grids.GridMosaic),


        ('meta', 'cardinality', "1.1"),

        ('esm_exchange_grids', 'cardinality', "0.N"),

        ('esm_model_grids', 'cardinality', "0.N"),



    ),

    software.ComponentLanguageProperty: (

        ('name', 'type', unicode),

        ('value', 'type', unicode),


        ('name', 'cardinality', "0.1"),

        ('value', 'cardinality', "0.1"),



    ),

    software.Composition: (

        ('couplings', 'type', unicode),

        ('description', 'type', unicode),


        ('couplings', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),



    ),

    shared.ResponsibleParty: (

        ('url', 'type', unicode),

        ('organisation_name', 'type', unicode),

        ('abbreviation', 'type', unicode),

        ('individual_name', 'type', unicode),

        ('role', 'type', unicode),

        ('address', 'type', unicode),

        ('email', 'type', unicode),


        ('url', 'cardinality', "0.1"),

        ('organisation_name', 'cardinality', "0.1"),

        ('abbreviation', 'cardinality', "0.1"),

        ('individual_name', 'cardinality', "0.1"),

        ('role', 'cardinality', "0.1"),

        ('address', 'cardinality', "0.1"),

        ('email', 'cardinality', "0.1"),



    ),

    data.DataExtentTemporal: (

        ('time_interval', 'type', data.DataExtentTimeInterval),

        ('begin', 'type', datetime.date),

        ('end', 'type', datetime.date),


        ('time_interval', 'cardinality', "0.1"),

        ('begin', 'cardinality', "0.1"),

        ('end', 'cardinality', "0.1"),



    ),

    activity.Experiment: (

        ('funding_sources', 'type', unicode),

        ('rationales', 'type', unicode),

        ('generates', 'type', unicode),

        ('supports', 'type', unicode),

        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('measurement_campaigns', 'type', activity.MeasurementCampaign),

        ('requires', 'type', activity.NumericalActivity),

        ('projects', 'type', unicode),


        ('funding_sources', 'cardinality', "0.N"),

        ('rationales', 'cardinality', "0.N"),

        ('generates', 'cardinality', "0.N"),

        ('supports', 'cardinality', "0.N"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('measurement_campaigns', 'cardinality', "0.N"),

        ('requires', 'cardinality', "0.N"),

        ('projects', 'cardinality', "0.N"),



    ),

    grids.GridProperty: (

        ('name', 'type', unicode),

        ('value', 'type', unicode),


        ('name', 'cardinality', "0.1"),

        ('value', 'cardinality', "0.1"),



    ),

    grids.VerticalCoordinateList: (

        ('has_constant_offset', 'type', bool),

        ('form', 'type', unicode),

        ('length', 'type', int),

        ('type', 'type', unicode),

        ('properties', 'type', grids.GridProperty),

        ('uom', 'type', unicode),


        ('has_constant_offset', 'cardinality', "0.1"),

        ('form', 'cardinality', "0.1"),

        ('length', 'cardinality', "0.1"),

        ('type', 'cardinality', "0.1"),

        ('properties', 'cardinality', "0.N"),

        ('uom', 'cardinality', "0.1"),



    ),

    activity.NumericalRequirementOption: (

        ('sub_options', 'type', activity.NumericalRequirementOption),

        ('description', 'type', unicode),

        ('name', 'type', unicode),

        ('relationship', 'type', unicode),

        ('id', 'type', unicode),


        ('sub_options', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

        ('relationship', 'cardinality', "0.1"),

        ('id', 'cardinality', "0.1"),



    ),

    shared.ChangeProperty: (

        ('id', 'type', unicode),

        ('name', 'type', unicode),

        ('value', 'type', unicode),

        ('description', 'type', unicode),


        ('id', 'cardinality', "0.1"),

        ('name', 'cardinality', "0.1"),

        ('value', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



    ),

    grids.GridTileResolutionType: (

        ('description', 'type', unicode),

        ('properties', 'type', grids.GridProperty),


        ('description', 'cardinality', "0.1"),

        ('properties', 'cardinality', "0.N"),



    ),

    activity.EnsembleMember: (

        ('ensemble_ids', 'type', shared.StandardName),

        ('funding_sources', 'type', unicode),

        ('rationales', 'type', unicode),

        ('description', 'type', unicode),

        ('short_name', 'type', unicode),

        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('simulation', 'type', activity.Simulation),

        ('long_name', 'type', unicode),

        ('supports', 'type', activity.Experiment),

        ('ensemble', 'type', activity.Ensemble),

        ('projects', 'type', unicode),


        ('ensemble_ids', 'cardinality', "0.N"),

        ('funding_sources', 'cardinality', "0.N"),

        ('rationales', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('short_name', 'cardinality', "1.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('simulation', 'cardinality', "0.1"),

        ('long_name', 'cardinality', "0.1"),

        ('supports', 'cardinality', "0.N"),

        ('ensemble', 'cardinality', "0.1"),

        ('projects', 'cardinality', "0.N"),



    ),

    software.TimeLag: (

        ('units', 'type', unicode),

        ('value', 'type', int),


        ('units', 'cardinality', "0.1"),

        ('value', 'cardinality', "0.1"),



    ),

    software.StatisticalModelComponent: (

        ('funding_sources', 'type', unicode),

        ('version', 'type', unicode),

        ('long_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('is_embedded', 'type', bool),

        ('short_name', 'type', unicode),

        ('previous_version', 'type', unicode),

        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('deployments', 'type', software.Deployment),

        ('citations', 'type', shared.Citation),

        ('type', 'type', unicode),

        ('composition', 'type', software.Composition),

        ('coupling_framework', 'type', unicode),

        ('description', 'type', unicode),

        ('parent', 'type', software.Component),

        ('sub_components', 'type', software.Component),

        ('dependencies', 'type', software.EntryPoint),

        ('grid', 'type', grids.GridSpec),

        ('purpose', 'type', unicode),

        ('online_resource', 'type', unicode),

        ('timing', 'type', software.Timing),

        ('properties', 'type', software.ComponentProperty),

        ('types', 'type', unicode),

        ('language', 'type', software.ComponentLanguage),

        ('license', 'type', shared.License),

        ('release_date', 'type', datetime.datetime),

        ('code_access', 'type', unicode),


        ('funding_sources', 'cardinality', "0.N"),

        ('version', 'cardinality', "0.1"),

        ('long_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('is_embedded', 'cardinality', "0.1"),

        ('short_name', 'cardinality', "1.1"),

        ('previous_version', 'cardinality', "0.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('deployments', 'cardinality', "0.N"),

        ('citations', 'cardinality', "0.N"),

        ('type', 'cardinality', "0.1"),

        ('composition', 'cardinality', "0.1"),

        ('coupling_framework', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('parent', 'cardinality', "0.1"),

        ('sub_components', 'cardinality', "0.N"),

        ('dependencies', 'cardinality', "0.N"),

        ('grid', 'cardinality', "0.1"),

        ('purpose', 'cardinality', "0.1"),

        ('online_resource', 'cardinality', "0.1"),

        ('timing', 'cardinality', "0.1"),

        ('properties', 'cardinality', "0.N"),

        ('types', 'cardinality', "1.N"),

        ('language', 'cardinality', "0.1"),

        ('license', 'cardinality', "0.1"),

        ('release_date', 'cardinality', "0.1"),

        ('code_access', 'cardinality', "0.1"),



    ),

    data.DataDistribution: (

        ('access', 'type', unicode),

        ('fee', 'type', unicode),

        ('responsible_party', 'type', shared.ResponsibleParty),

        ('format', 'type', unicode),


        ('access', 'cardinality', "0.1"),

        ('fee', 'cardinality', "0.1"),

        ('responsible_party', 'cardinality', "0.1"),

        ('format', 'cardinality', "0.1"),



    ),

    quality.CimQuality: (

        ('meta', 'type', shared.DocMetaInfo),

        ('reports', 'type', quality.Report),


        ('meta', 'cardinality', "1.1"),

        ('reports', 'cardinality', "0.N"),



    ),

    data.DataRestriction: (

        ('restriction', 'type', unicode),

        ('license', 'type', shared.License),

        ('scope', 'type', unicode),


        ('restriction', 'cardinality', "0.1"),

        ('license', 'cardinality', "0.1"),

        ('scope', 'cardinality', "0.1"),



    ),

    software.CouplingEndpoint: (

        ('instance_id', 'type', unicode),

        ('data_source', 'type', shared.DataSource),

        ('properties', 'type', software.CouplingProperty),


        ('instance_id', 'cardinality', "0.1"),

        ('data_source', 'cardinality', "0.1"),

        ('properties', 'cardinality', "0.N"),



    ),

    shared.Property: (

        ('name', 'type', unicode),

        ('value', 'type', unicode),


        ('name', 'cardinality', "0.1"),

        ('value', 'cardinality', "0.1"),



    ),

    shared.Platform: (

        ('description', 'type', unicode),

        ('short_name', 'type', unicode),

        ('contacts', 'type', shared.ResponsibleParty),

        ('long_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('units', 'type', shared.MachineCompilerUnit),


        ('description', 'cardinality', "0.1"),

        ('short_name', 'cardinality', "1.1"),

        ('contacts', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('units', 'cardinality', "1.N"),



    ),

    shared.DataSource: (

        ('purpose', 'type', unicode),


        ('purpose', 'cardinality', "0.1"),



    ),

    grids.GridMosaic: (

        ('is_leaf', 'type', bool),

        ('mnemonic', 'type', unicode),

        ('tiles', 'type', grids.GridTile),

        ('description', 'type', unicode),

        ('short_name', 'type', unicode),

        ('mosaic_count', 'type', int),

        ('type', 'type', unicode),

        ('long_name', 'type', unicode),

        ('tile_count', 'type', int),

        ('citations', 'type', shared.Citation),

        ('extent', 'type', grids.GridExtent),

        ('has_congruent_tiles', 'type', bool),

        ('mosaics', 'type', grids.GridMosaic),

        ('id', 'type', unicode),


        ('is_leaf', 'cardinality', "1.1"),

        ('mnemonic', 'cardinality', "0.1"),

        ('tiles', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('short_name', 'cardinality', "1.1"),

        ('mosaic_count', 'cardinality', "0.1"),

        ('type', 'cardinality', "1.1"),

        ('long_name', 'cardinality', "0.1"),

        ('tile_count', 'cardinality', "0.1"),

        ('citations', 'cardinality', "0.N"),

        ('extent', 'cardinality', "0.1"),

        ('has_congruent_tiles', 'cardinality', "0.1"),

        ('mosaics', 'cardinality', "0.N"),

        ('id', 'cardinality', "1.1"),



    ),

    software.TimeTransformation: (

        ('description', 'type', unicode),

        ('mapping_type', 'type', unicode),


        ('description', 'cardinality', "0.1"),

        ('mapping_type', 'cardinality', "1.1"),



    ),

    activity.LateralBoundaryCondition: (

        ('description', 'type', unicode),

        ('options', 'type', activity.NumericalRequirementOption),

        ('source', 'type', shared.DataSource),

        ('requirement_type', 'type', unicode),

        ('id', 'type', unicode),

        ('name', 'type', unicode),


        ('description', 'cardinality', "0.1"),

        ('options', 'cardinality', "0.N"),

        ('source', 'cardinality', "0.1"),

        ('requirement_type', 'cardinality', "1.1"),

        ('id', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),


        ('requirement_type', 'constant', "lateralBoundaryCondition"),


    ),

    shared.License: (

        ('contact', 'type', unicode),

        ('description', 'type', unicode),

        ('is_unrestricted', 'type', bool),

        ('name', 'type', unicode),


        ('contact', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('is_unrestricted', 'cardinality', "0.1"),

        ('name', 'cardinality', "0.1"),



    ),

    activity.ExperimentRelationshipTarget: (

        ('numerical_experiment', 'type', activity.NumericalExperiment),


        ('numerical_experiment', 'cardinality', "0.1"),



    ),

    data.DataStorageDb: (

        ('name', 'type', unicode),

        ('modification_date', 'type', datetime.datetime),

        ('format', 'type', unicode),

        ('location', 'type', unicode),

        ('owner', 'type', unicode),

        ('table', 'type', unicode),

        ('access_string', 'type', unicode),

        ('size', 'type', int),


        ('name', 'cardinality', "0.1"),

        ('modification_date', 'cardinality', "0.1"),

        ('format', 'cardinality', "0.1"),

        ('location', 'cardinality', "0.1"),

        ('owner', 'cardinality', "0.1"),

        ('table', 'cardinality', "0.1"),

        ('access_string', 'cardinality', "0.1"),

        ('size', 'cardinality', "0.1"),



    ),

    software.Component: (

        ('funding_sources', 'type', unicode),

        ('version', 'type', unicode),

        ('long_name', 'type', unicode),

        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('short_name', 'type', unicode),

        ('previous_version', 'type', unicode),

        ('is_embedded', 'type', bool),

        ('deployments', 'type', software.Deployment),

        ('citations', 'type', shared.Citation),

        ('composition', 'type', software.Composition),

        ('coupling_framework', 'type', unicode),

        ('description', 'type', unicode),

        ('parent', 'type', software.Component),

        ('sub_components', 'type', software.Component),

        ('dependencies', 'type', software.EntryPoint),

        ('grid', 'type', grids.GridSpec),

        ('purpose', 'type', unicode),

        ('online_resource', 'type', unicode),

        ('properties', 'type', software.ComponentProperty),

        ('language', 'type', software.ComponentLanguage),

        ('license', 'type', shared.License),

        ('release_date', 'type', datetime.datetime),

        ('code_access', 'type', unicode),


        ('funding_sources', 'cardinality', "0.N"),

        ('version', 'cardinality', "0.1"),

        ('long_name', 'cardinality', "0.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('short_name', 'cardinality', "1.1"),

        ('previous_version', 'cardinality', "0.1"),

        ('is_embedded', 'cardinality', "0.1"),

        ('deployments', 'cardinality', "0.N"),

        ('citations', 'cardinality', "0.N"),

        ('composition', 'cardinality', "0.1"),

        ('coupling_framework', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('parent', 'cardinality', "0.1"),

        ('sub_components', 'cardinality', "0.N"),

        ('dependencies', 'cardinality', "0.N"),

        ('grid', 'cardinality', "0.1"),

        ('purpose', 'cardinality', "0.1"),

        ('online_resource', 'cardinality', "0.1"),

        ('properties', 'cardinality', "0.N"),

        ('language', 'cardinality', "0.1"),

        ('license', 'cardinality', "0.1"),

        ('release_date', 'cardinality', "0.1"),

        ('code_access', 'cardinality', "0.1"),



    ),

    shared.Standard: (

        ('version', 'type', unicode),

        ('name', 'type', unicode),

        ('description', 'type', unicode),


        ('version', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),



    ),

    data.DataExtentTimeInterval: (

        ('radix', 'type', int),

        ('unit', 'type', unicode),

        ('factor', 'type', int),


        ('radix', 'cardinality', "0.1"),

        ('unit', 'cardinality', "0.1"),

        ('factor', 'cardinality', "0.1"),



    ),

    activity.NumericalExperiment: (

        ('funding_sources', 'type', unicode),

        ('rationales', 'type', unicode),

        ('generates', 'type', unicode),

        ('short_name', 'type', unicode),

        ('long_name', 'type', unicode),

        ('requires', 'type', activity.NumericalActivity),

        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('measurement_campaigns', 'type', activity.MeasurementCampaign),

        ('meta', 'type', shared.DocMetaInfo),

        ('experiment_id', 'type', unicode),

        ('requirements', 'type', activity.NumericalRequirement),

        ('supports', 'type', unicode),

        ('projects', 'type', unicode),

        ('description', 'type', unicode),


        ('funding_sources', 'cardinality', "0.N"),

        ('rationales', 'cardinality', "0.N"),

        ('generates', 'cardinality', "0.N"),

        ('short_name', 'cardinality', "1.1"),

        ('long_name', 'cardinality', "0.1"),

        ('requires', 'cardinality', "0.N"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('measurement_campaigns', 'cardinality', "0.N"),

        ('meta', 'cardinality', "1.1"),

        ('experiment_id', 'cardinality', "0.1"),

        ('requirements', 'cardinality', "0.N"),

        ('supports', 'cardinality', "0.N"),

        ('projects', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),



    ),

    activity.MeasurementCampaign: (

        ('duration', 'type', int),

        ('funding_sources', 'type', unicode),

        ('rationales', 'type', unicode),

        ('projects', 'type', unicode),

        ('responsible_parties', 'type', shared.ResponsibleParty),


        ('duration', 'cardinality', "1.1"),

        ('funding_sources', 'cardinality', "0.N"),

        ('rationales', 'cardinality', "0.N"),

        ('projects', 'cardinality', "0.N"),

        ('responsible_parties', 'cardinality', "0.N"),



    ),

    activity.BoundaryCondition: (

        ('description', 'type', unicode),

        ('options', 'type', activity.NumericalRequirementOption),

        ('source', 'type', shared.DataSource),

        ('requirement_type', 'type', unicode),

        ('id', 'type', unicode),

        ('name', 'type', unicode),


        ('description', 'cardinality', "0.1"),

        ('options', 'cardinality', "0.N"),

        ('source', 'cardinality', "0.1"),

        ('requirement_type', 'cardinality', "1.1"),

        ('id', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),


        ('requirement_type', 'constant', "boundaryCondition"),


    ),

    software.EntryPoint: (

        ('name', 'type', unicode),


        ('name', 'cardinality', "0.1"),



    ),

    software.Connection: (

        ('transformers', 'type', software.ProcessorComponent),

        ('target', 'type', software.ConnectionEndpoint),

        ('time_transformation', 'type', software.TimeTransformation),

        ('description', 'type', unicode),

        ('spatial_regridding', 'type', software.SpatialRegridding),

        ('sources', 'type', software.ConnectionEndpoint),

        ('time_profile', 'type', software.Timing),

        ('type', 'type', unicode),

        ('properties', 'type', software.ConnectionProperty),

        ('time_lag', 'type', unicode),

        ('priming', 'type', shared.DataSource),


        ('transformers', 'cardinality', "0.N"),

        ('target', 'cardinality', "0.1"),

        ('time_transformation', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('spatial_regridding', 'cardinality', "0.N"),

        ('sources', 'cardinality', "0.N"),

        ('time_profile', 'cardinality', "0.1"),

        ('type', 'cardinality', "0.1"),

        ('properties', 'cardinality', "0.N"),

        ('time_lag', 'cardinality', "0.1"),

        ('priming', 'cardinality', "0.1"),



    ),

    shared.Compiler: (

        ('name', 'type', unicode),

        ('language', 'type', unicode),

        ('version', 'type', unicode),

        ('environment_variables', 'type', unicode),

        ('type', 'type', unicode),

        ('options', 'type', unicode),


        ('name', 'cardinality', "1.1"),

        ('language', 'cardinality', "0.1"),

        ('version', 'cardinality', "1.1"),

        ('environment_variables', 'cardinality', "0.1"),

        ('type', 'cardinality', "0.1"),

        ('options', 'cardinality', "0.1"),



    ),

    activity.Ensemble: (

        ('funding_sources', 'type', unicode),

        ('rationales', 'type', unicode),

        ('description', 'type', unicode),

        ('short_name', 'type', unicode),

        ('outputs', 'type', shared.DataSource),

        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('long_name', 'type', unicode),

        ('meta', 'type', shared.DocMetaInfo),

        ('types', 'type', unicode),

        ('members', 'type', activity.EnsembleMember),

        ('supports', 'type', activity.Experiment),

        ('projects', 'type', unicode),


        ('funding_sources', 'cardinality', "0.N"),

        ('rationales', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('short_name', 'cardinality', "1.1"),

        ('outputs', 'cardinality', "0.N"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('types', 'cardinality', "1.N"),

        ('members', 'cardinality', "1.N"),

        ('supports', 'cardinality', "0.N"),

        ('projects', 'cardinality', "0.N"),



    ),

    activity.OutputRequirement: (

        ('description', 'type', unicode),

        ('options', 'type', activity.NumericalRequirementOption),

        ('source', 'type', shared.DataSource),

        ('requirement_type', 'type', unicode),

        ('id', 'type', unicode),

        ('name', 'type', unicode),


        ('description', 'cardinality', "0.1"),

        ('options', 'cardinality', "0.N"),

        ('source', 'cardinality', "0.1"),

        ('requirement_type', 'cardinality', "1.1"),

        ('id', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),


        ('requirement_type', 'constant', "outputRequirement"),


    ),

    shared.StandardName: (

        ('is_open', 'type', bool),

        ('value', 'type', unicode),

        ('standards', 'type', shared.Standard),


        ('is_open', 'cardinality', "1.1"),

        ('value', 'cardinality', "1.1"),

        ('standards', 'cardinality', "0.N"),



    ),

    shared.DocRelationshipTarget: (

        ('reference', 'type', shared.DocReference),


        ('reference', 'cardinality', "0.1"),



    ),

    shared.MachineCompilerUnit: (

        ('machine', 'type', shared.Machine),

        ('compilers', 'type', shared.Compiler),


        ('machine', 'cardinality', "1.1"),

        ('compilers', 'cardinality', "0.N"),



    ),

    quality.Measure: (

        ('identification', 'type', unicode),

        ('name', 'type', unicode),

        ('description', 'type', unicode),


        ('identification', 'cardinality', "0.1"),

        ('name', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),



    ),

    software.Rank: (

        ('max', 'type', int),

        ('value', 'type', int),

        ('increment', 'type', int),

        ('min', 'type', int),


        ('max', 'cardinality', "0.1"),

        ('value', 'cardinality', "0.1"),

        ('increment', 'cardinality', "0.1"),

        ('min', 'cardinality', "0.1"),



    ),

    activity.SimulationRelationship: (

        ('direction', 'type', unicode),

        ('type', 'type', unicode),

        ('description', 'type', unicode),

        ('target', 'type', activity.SimulationRelationshipTarget),


        ('direction', 'cardinality', "1.1"),

        ('type', 'cardinality', "1.1"),

        ('description', 'cardinality', "0.1"),

        ('target', 'cardinality', "1.1"),



    ),

    software.ConnectionEndpoint: (

        ('instance_id', 'type', unicode),

        ('data_source', 'type', shared.DataSource),

        ('properties', 'type', software.ConnectionProperty),


        ('instance_id', 'cardinality', "0.1"),

        ('data_source', 'cardinality', "0.1"),

        ('properties', 'cardinality', "0.N"),



    ),

    data.DataExtentGeographical: (

        ('west', 'type', float),

        ('east', 'type', float),

        ('north', 'type', float),

        ('south', 'type', float),


        ('west', 'cardinality', "0.1"),

        ('east', 'cardinality', "0.1"),

        ('north', 'cardinality', "0.1"),

        ('south', 'cardinality', "0.1"),



    ),

    grids.CoordinateList: (

        ('has_constant_offset', 'type', bool),

        ('length', 'type', int),

        ('uom', 'type', unicode),


        ('has_constant_offset', 'cardinality', "0.1"),

        ('length', 'cardinality', "0.1"),

        ('uom', 'cardinality', "0.1"),



    ),

    misc.DocumentSet: (

        ('ensembles', 'type', activity.Ensemble),

        ('grids', 'type', grids.GridSpec),

        ('experiment', 'type', activity.NumericalExperiment),

        ('simulation', 'type', activity.SimulationRun),

        ('platform', 'type', shared.Platform),

        ('meta', 'type', shared.DocMetaInfo),

        ('model', 'type', software.ModelComponent),

        ('data', 'type', data.DataObject),


        ('ensembles', 'cardinality', "0.N"),

        ('grids', 'cardinality', "0.N"),

        ('experiment', 'cardinality', "0.1"),

        ('simulation', 'cardinality', "0.1"),

        ('platform', 'cardinality', "0.1"),

        ('meta', 'cardinality', "1.1"),

        ('model', 'cardinality', "0.1"),

        ('data', 'cardinality', "0.N"),



    ),

    activity.Simulation: (

        ('inputs', 'type', software.Coupling),

        ('simulation_id', 'type', unicode),

        ('funding_sources', 'type', unicode),

        ('rationales', 'type', unicode),

        ('description', 'type', unicode),

        ('short_name', 'type', unicode),

        ('outputs', 'type', data.DataObject),

        ('spinup_simulation', 'type', activity.Simulation),

        ('spinup_date_range', 'type', shared.ClosedDateRange),

        ('responsible_parties', 'type', shared.ResponsibleParty),

        ('deployments', 'type', software.Deployment),

        ('restarts', 'type', data.DataObject),

        ('long_name', 'type', unicode),

        ('control_simulation', 'type', activity.Simulation),

        ('authors', 'type', unicode),

        ('calendar', 'type', shared.Calendar),

        ('supports', 'type', activity.Experiment),

        ('conformances', 'type', activity.Conformance),

        ('projects', 'type', unicode),


        ('inputs', 'cardinality', "0.N"),

        ('simulation_id', 'cardinality', "0.1"),

        ('funding_sources', 'cardinality', "0.N"),

        ('rationales', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('short_name', 'cardinality', "1.1"),

        ('outputs', 'cardinality', "0.N"),

        ('spinup_simulation', 'cardinality', "0.1"),

        ('spinup_date_range', 'cardinality', "0.1"),

        ('responsible_parties', 'cardinality', "0.N"),

        ('deployments', 'cardinality', "0.N"),

        ('restarts', 'cardinality', "0.N"),

        ('long_name', 'cardinality', "0.1"),

        ('control_simulation', 'cardinality', "0.1"),

        ('authors', 'cardinality', "0.1"),

        ('calendar', 'cardinality', "1.1"),

        ('supports', 'cardinality', "0.N"),

        ('conformances', 'cardinality', "0.N"),

        ('projects', 'cardinality', "0.N"),



    ),

    software.ComponentProperty: (

        ('standard_names', 'type', unicode),

        ('sub_properties', 'type', software.ComponentProperty),

        ('description', 'type', unicode),

        ('short_name', 'type', unicode),

        ('is_represented', 'type', bool),

        ('long_name', 'type', unicode),

        ('citations', 'type', shared.Citation),

        ('grid', 'type', unicode),

        ('purpose', 'type', unicode),

        ('units', 'type', unicode),

        ('values', 'type', unicode),

        ('intent', 'type', unicode),


        ('standard_names', 'cardinality', "0.N"),

        ('sub_properties', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('short_name', 'cardinality', "1.1"),

        ('is_represented', 'cardinality', "1.1"),

        ('long_name', 'cardinality', "0.1"),

        ('citations', 'cardinality', "0.N"),

        ('grid', 'cardinality', "0.1"),

        ('purpose', 'cardinality', "0.1"),

        ('units', 'cardinality', "0.1"),

        ('values', 'cardinality', "0.N"),

        ('intent', 'cardinality', "0.1"),



    ),

    software.ConnectionProperty: (

        ('name', 'type', unicode),

        ('value', 'type', unicode),


        ('name', 'cardinality', "0.1"),

        ('value', 'cardinality', "0.1"),



    ),

    software.Coupling: (

        ('transformers', 'type', software.ProcessorComponent),

        ('description', 'type', unicode),

        ('type', 'type', unicode),

        ('time_transformation', 'type', software.TimeTransformation),

        ('connections', 'type', software.Connection),

        ('sources', 'type', software.CouplingEndpoint),

        ('spatial_regriddings', 'type', software.SpatialRegridding),

        ('purpose', 'type', unicode),

        ('time_profile', 'type', software.Timing),

        ('priming', 'type', shared.DataSource),

        ('is_fully_specified', 'type', bool),

        ('properties', 'type', software.CouplingProperty),

        ('time_lag', 'type', software.TimeLag),

        ('target', 'type', software.CouplingEndpoint),


        ('transformers', 'cardinality', "0.N"),

        ('description', 'cardinality', "0.1"),

        ('type', 'cardinality', "0.1"),

        ('time_transformation', 'cardinality', "0.1"),

        ('connections', 'cardinality', "0.N"),

        ('sources', 'cardinality', "1.N"),

        ('spatial_regriddings', 'cardinality', "0.N"),

        ('purpose', 'cardinality', "1.1"),

        ('time_profile', 'cardinality', "0.1"),

        ('priming', 'cardinality', "0.1"),

        ('is_fully_specified', 'cardinality', "1.1"),

        ('properties', 'cardinality', "0.N"),

        ('time_lag', 'cardinality', "0.1"),

        ('target', 'cardinality', "1.1"),



    ),

    shared.DateRange: (

        ('duration', 'type', unicode),


        ('duration', 'cardinality', "0.1"),



    ),

    shared.Machine: (

        ('operating_system', 'type', unicode),

        ('vendor', 'type', unicode),

        ('description', 'type', unicode),

        ('cores_per_processor', 'type', int),

        ('interconnect', 'type', unicode),

        ('system', 'type', unicode),

        ('name', 'type', unicode),

        ('libraries', 'type', unicode),

        ('location', 'type', unicode),

        ('maximum_processors', 'type', int),

        ('type', 'type', unicode),

        ('processor_type', 'type', unicode),


        ('operating_system', 'cardinality', "0.1"),

        ('vendor', 'cardinality', "0.1"),

        ('description', 'cardinality', "0.1"),

        ('cores_per_processor', 'cardinality', "0.1"),

        ('interconnect', 'cardinality', "0.1"),

        ('system', 'cardinality', "0.1"),

        ('name', 'cardinality', "1.1"),

        ('libraries', 'cardinality', "0.N"),

        ('location', 'cardinality', "0.1"),

        ('maximum_processors', 'cardinality', "0.1"),

        ('type', 'cardinality', "0.1"),

        ('processor_type', 'cardinality', "0.1"),



    ),

    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------


    (shared.DocReference, 'type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'external_id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'url'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'version'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocReference, 'changes'): (

        ('type', shared.Change),


        ('cardinality', "0.N"),



    ),

    (shared.DocReference, 'id'): (

        ('type', uuid.UUID),


        ('cardinality', "0.1"),



    ),



    (data.DataContent, 'aggregation'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataContent, 'topic'): (

        ('type', data.DataTopic),


        ('cardinality', "1.1"),



    ),

    (data.DataContent, 'purpose'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataContent, 'frequency'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (shared.PerpetualPeriod, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.PerpetualPeriod, 'length'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (shared.PerpetualPeriod, 'range'): (

        ('type', shared.DateRange),


        ('cardinality', "0.1"),



    ),



    (shared.OpenDateRange, 'duration'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.OpenDateRange, 'end'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (shared.OpenDateRange, 'start'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),



    (shared.Relationship, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Relationship, 'direction'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (data.DataStorage, 'location'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorage, 'size'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (data.DataStorage, 'modification_date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (data.DataStorage, 'format'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (shared.Citation, 'location'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Citation, 'type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Citation, 'date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (shared.Citation, 'organisation'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Citation, 'date_type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Citation, 'title'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Citation, 'collective_title'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Citation, 'alternative_title'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Citation, 'role'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (software.Parallelisation, 'processes'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (software.Parallelisation, 'ranks'): (

        ('type', software.Rank),


        ('cardinality', "0.N"),



    ),



    (grids.GridTile, 'mnemonic'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'nz'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'horizontal_resolution'): (

        ('type', grids.GridTileResolutionType),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'horizontal_crs'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'grid_north_pole'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'simple_grid_geom'): (

        ('type', grids.SimpleGridGeometry),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'discretization_type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'ny'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'is_conformal'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'area'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'vertical_crs'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'zcoords'): (

        ('type', grids.VerticalCoordinateList),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'cell_array'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'coord_file'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'is_terrain_following'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'cell_ref_array'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'short_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'geometry_type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'is_uniform'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'refinement_scheme'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'vertical_resolution'): (

        ('type', grids.GridTileResolutionType),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'is_regular'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'nx'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'coordinate_pole'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTile, 'extent'): (

        ('type', grids.GridExtent),


        ('cardinality', "0.1"),



    ),



    (software.ModelComponent, 'online_resource'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'release_date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'activity'): (

        ('type', activity.Activity),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'purpose'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'funding_sources'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (software.ModelComponent, 'previous_version'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'properties'): (

        ('type', software.ComponentProperty),


        ('cardinality', "0.N"),



    ),

    (software.ModelComponent, 'version'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'grid'): (

        ('type', grids.GridSpec),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'code_access'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (software.ModelComponent, 'composition'): (

        ('type', software.Composition),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'parent'): (

        ('type', software.Component),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'license'): (

        ('type', shared.License),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'short_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (software.ModelComponent, 'language'): (

        ('type', software.ComponentLanguage),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'citations'): (

        ('type', shared.Citation),


        ('cardinality', "0.N"),



    ),

    (software.ModelComponent, 'deployments'): (

        ('type', software.Deployment),


        ('cardinality', "0.N"),



    ),

    (software.ModelComponent, 'types'): (

        ('type', unicode),


        ('cardinality', "1.N"),



    ),

    (software.ModelComponent, 'is_embedded'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),

    (software.ModelComponent, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'sub_components'): (

        ('type', software.Component),


        ('cardinality', "0.N"),



    ),

    (software.ModelComponent, 'coupling_framework'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'timing'): (

        ('type', software.Timing),


        ('cardinality', "0.1"),



    ),

    (software.ModelComponent, 'dependencies'): (

        ('type', software.EntryPoint),


        ('cardinality', "0.N"),



    ),



    (activity.Conformance, 'sources'): (

        ('type', shared.DataSource),


        ('cardinality', "0.N"),



    ),

    (activity.Conformance, 'frequency'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Conformance, 'type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Conformance, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Conformance, 'is_conformant'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (activity.Conformance, 'requirements'): (

        ('type', activity.NumericalRequirement),


        ('cardinality', "0.N"),



    ),



    (quality.Report, 'date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (quality.Report, 'evaluation'): (

        ('type', quality.Evaluation),


        ('cardinality', "1.1"),



    ),

    (quality.Report, 'evaluator'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.1"),



    ),

    (quality.Report, 'measure'): (

        ('type', quality.Measure),


        ('cardinality', "1.1"),



    ),



    (software.ProcessorComponent, 'online_resource'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ProcessorComponent, 'release_date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (software.ProcessorComponent, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ProcessorComponent, 'purpose'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ProcessorComponent, 'funding_sources'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (software.ProcessorComponent, 'properties'): (

        ('type', software.ComponentProperty),


        ('cardinality', "0.N"),



    ),

    (software.ProcessorComponent, 'version'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ProcessorComponent, 'grid'): (

        ('type', grids.GridSpec),


        ('cardinality', "0.1"),



    ),

    (software.ProcessorComponent, 'code_access'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ProcessorComponent, 'composition'): (

        ('type', software.Composition),


        ('cardinality', "0.1"),



    ),

    (software.ProcessorComponent, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (software.ProcessorComponent, 'previous_version'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ProcessorComponent, 'short_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (software.ProcessorComponent, 'language'): (

        ('type', software.ComponentLanguage),


        ('cardinality', "0.1"),



    ),

    (software.ProcessorComponent, 'citations'): (

        ('type', shared.Citation),


        ('cardinality', "0.N"),



    ),

    (software.ProcessorComponent, 'license'): (

        ('type', shared.License),


        ('cardinality', "0.1"),



    ),

    (software.ProcessorComponent, 'is_embedded'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (software.ProcessorComponent, 'parent'): (

        ('type', software.Component),


        ('cardinality', "0.1"),



    ),

    (software.ProcessorComponent, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),

    (software.ProcessorComponent, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ProcessorComponent, 'sub_components'): (

        ('type', software.Component),


        ('cardinality', "0.N"),



    ),

    (software.ProcessorComponent, 'coupling_framework'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ProcessorComponent, 'deployments'): (

        ('type', software.Deployment),


        ('cardinality', "0.N"),



    ),

    (software.ProcessorComponent, 'dependencies'): (

        ('type', software.EntryPoint),


        ('cardinality', "0.N"),



    ),



    (shared.DocMetaInfo, 'drs_keys'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (shared.DocMetaInfo, 'drs_path'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'type_display_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'source_key'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'status'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'update_date'): (

        ('type', datetime.datetime),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'genealogy'): (

        ('type', shared.DocGenealogy),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'sort_key'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'id'): (

        ('type', uuid.UUID),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'language'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'institute'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'external_ids'): (

        ('type', shared.StandardName),


        ('cardinality', "0.N"),



    ),

    (shared.DocMetaInfo, 'create_date'): (

        ('type', datetime.datetime),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'type_sort_key'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'project'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocMetaInfo, 'author'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.1"),



    ),

    (shared.DocMetaInfo, 'source'): (

        ('type', unicode),


        ('cardinality', "1.1"),


        ('constant', "scripts"),


    ),

    (shared.DocMetaInfo, 'version'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),



    (software.ComponentLanguage, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (software.ComponentLanguage, 'properties'): (

        ('type', software.ComponentLanguageProperty),


        ('cardinality', "0.N"),



    ),



    (activity.NumericalActivity, 'rationales'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.NumericalActivity, 'supports'): (

        ('type', activity.Experiment),


        ('cardinality', "0.N"),



    ),

    (activity.NumericalActivity, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.NumericalActivity, 'funding_sources'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.NumericalActivity, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),

    (activity.NumericalActivity, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.NumericalActivity, 'short_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.NumericalActivity, 'projects'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),



    (activity.Activity, 'funding_sources'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.Activity, 'projects'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.Activity, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),

    (activity.Activity, 'rationales'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),



    (software.CouplingProperty, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.CouplingProperty, 'value'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (software.SpatialRegridding, 'standard_method'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.SpatialRegridding, 'properties'): (

        ('type', software.SpatialRegriddingProperty),


        ('cardinality', "0.N"),



    ),

    (software.SpatialRegridding, 'dimension'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.SpatialRegridding, 'user_method'): (

        ('type', software.SpatialRegriddingUserMethod),


        ('cardinality', "0.1"),



    ),



    (shared.DocGenealogy, 'relationships'): (

        ('type', shared.DocRelationship),


        ('cardinality', "0.N"),



    ),



    (shared.Calendar, 'length'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (shared.Calendar, 'range'): (

        ('type', shared.DateRange),


        ('cardinality', "0.1"),



    ),

    (shared.Calendar, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (activity.PhysicalModification, 'sources'): (

        ('type', shared.DataSource),


        ('cardinality', "0.N"),



    ),

    (activity.PhysicalModification, 'frequency'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.PhysicalModification, 'type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.PhysicalModification, 'requirements'): (

        ('type', activity.NumericalRequirement),


        ('cardinality', "0.N"),



    ),

    (activity.PhysicalModification, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.PhysicalModification, 'is_conformant'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),



    (shared.DocRelationship, 'target'): (

        ('type', shared.DocRelationshipTarget),


        ('cardinality', "1.1"),



    ),

    (shared.DocRelationship, 'direction'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocRelationship, 'type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.DocRelationship, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (shared.ClosedDateRange, 'duration'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ClosedDateRange, 'end'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (shared.ClosedDateRange, 'start'): (

        ('type', datetime.datetime),


        ('cardinality', "1.1"),



    ),



    (activity.ExperimentRelationship, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.ExperimentRelationship, 'direction'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.ExperimentRelationship, 'target'): (

        ('type', activity.ExperimentRelationshipTarget),


        ('cardinality', "1.1"),



    ),

    (activity.ExperimentRelationship, 'type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (shared.RealCalendar, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.RealCalendar, 'length'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (shared.RealCalendar, 'range'): (

        ('type', shared.DateRange),


        ('cardinality', "0.1"),



    ),



    (data.DataHierarchyLevel, 'is_open'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (data.DataHierarchyLevel, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataHierarchyLevel, 'value'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (shared.Change, 'date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (shared.Change, 'details'): (

        ('type', shared.ChangeProperty),


        ('cardinality', "1.N"),



    ),

    (shared.Change, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Change, 'type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Change, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Change, 'author'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.1"),



    ),



    (software.SpatialRegriddingProperty, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.SpatialRegriddingProperty, 'value'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (activity.SimulationRun, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationRun, 'authors'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationRun, 'spinup_simulation'): (

        ('type', activity.Simulation),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationRun, 'calendar'): (

        ('type', shared.Calendar),


        ('cardinality', "1.1"),



    ),

    (activity.SimulationRun, 'inputs'): (

        ('type', software.Coupling),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationRun, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (activity.SimulationRun, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationRun, 'projects'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationRun, 'control_simulation'): (

        ('type', activity.Simulation),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationRun, 'spinup_date_range'): (

        ('type', shared.ClosedDateRange),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationRun, 'date_range'): (

        ('type', shared.DateRange),


        ('cardinality', "1.1"),



    ),

    (activity.SimulationRun, 'funding_sources'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationRun, 'supports'): (

        ('type', activity.Experiment),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationRun, 'simulation_id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationRun, 'model'): (

        ('type', software.ModelComponent),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationRun, 'deployments'): (

        ('type', software.Deployment),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationRun, 'rationales'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationRun, 'restarts'): (

        ('type', data.DataObject),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationRun, 'outputs'): (

        ('type', data.DataObject),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationRun, 'conformances'): (

        ('type', activity.Conformance),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationRun, 'short_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.SimulationRun, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),



    (quality.Evaluation, 'did_pass'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (quality.Evaluation, 'specification_hyperlink'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (quality.Evaluation, 'type_hyperlink'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (quality.Evaluation, 'explanation'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (quality.Evaluation, 'specification'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (quality.Evaluation, 'date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (quality.Evaluation, 'title'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (quality.Evaluation, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (quality.Evaluation, 'type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (activity.SimulationRelationshipTarget, 'simulation'): (

        ('type', shared.DocReference),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationRelationshipTarget, 'target'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (data.DataObject, 'parent_object'): (

        ('type', data.DataObject),


        ('cardinality', "0.1"),



    ),

    (data.DataObject, 'purpose'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataObject, 'distribution'): (

        ('type', data.DataDistribution),


        ('cardinality', "0.1"),



    ),

    (data.DataObject, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (data.DataObject, 'keyword'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataObject, 'extent'): (

        ('type', data.DataExtent),


        ('cardinality', "0.1"),



    ),

    (data.DataObject, 'acronym'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataObject, 'geometry_model'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataObject, 'child_object'): (

        ('type', data.DataObject),


        ('cardinality', "0.N"),



    ),

    (data.DataObject, 'hierarchy_level'): (

        ('type', data.DataHierarchyLevel),


        ('cardinality', "0.1"),



    ),

    (data.DataObject, 'citations'): (

        ('type', shared.Citation),


        ('cardinality', "0.N"),



    ),

    (data.DataObject, 'purpose'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataObject, 'content'): (

        ('type', data.DataContent),


        ('cardinality', "0.N"),



    ),

    (data.DataObject, 'storage'): (

        ('type', data.DataStorage),


        ('cardinality', "0.N"),



    ),

    (data.DataObject, 'properties'): (

        ('type', data.DataProperty),


        ('cardinality', "0.N"),



    ),

    (data.DataObject, 'data_status'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataObject, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataObject, 'restriction'): (

        ('type', data.DataRestriction),


        ('cardinality', "0.N"),



    ),

    (data.DataObject, 'source_simulation'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (data.DataTopic, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataTopic, 'unit'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataTopic, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (grids.GridExtent, 'units'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridExtent, 'minimum_latitude'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (grids.GridExtent, 'maximum_longitude'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (grids.GridExtent, 'minimum_longitude'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (grids.GridExtent, 'maximum_latitude'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (software.Timing, 'units'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Timing, 'start'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (software.Timing, 'is_variable_rate'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (software.Timing, 'rate'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (software.Timing, 'end'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),



    (activity.NumericalRequirement, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.NumericalRequirement, 'requirement_type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.NumericalRequirement, 'options'): (

        ('type', activity.NumericalRequirementOption),


        ('cardinality', "0.N"),



    ),

    (activity.NumericalRequirement, 'source'): (

        ('type', shared.DataSource),


        ('cardinality', "0.1"),



    ),

    (activity.NumericalRequirement, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.NumericalRequirement, 'id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (grids.SimpleGridGeometry, 'xcoords'): (

        ('type', grids.CoordinateList),


        ('cardinality', "1.1"),



    ),

    (grids.SimpleGridGeometry, 'num_dims'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (grids.SimpleGridGeometry, 'is_mesh'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (grids.SimpleGridGeometry, 'zcoords'): (

        ('type', grids.CoordinateList),


        ('cardinality', "0.1"),



    ),

    (grids.SimpleGridGeometry, 'dim_order'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.SimpleGridGeometry, 'ycoords'): (

        ('type', grids.CoordinateList),


        ('cardinality', "1.1"),



    ),



    (activity.InitialCondition, 'source'): (

        ('type', shared.DataSource),


        ('cardinality', "0.1"),



    ),

    (activity.InitialCondition, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.InitialCondition, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.InitialCondition, 'id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.InitialCondition, 'options'): (

        ('type', activity.NumericalRequirementOption),


        ('cardinality', "0.N"),



    ),

    (activity.InitialCondition, 'requirement_type'): (

        ('type', unicode),


        ('cardinality', "1.1"),


        ('constant', "initialCondition"),


    ),



    (activity.SpatioTemporalConstraint, 'id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.SpatioTemporalConstraint, 'requirement_type'): (

        ('type', unicode),


        ('cardinality', "1.1"),


        ('constant', "spatioTemporalConstraint"),


    ),

    (activity.SpatioTemporalConstraint, 'date_range'): (

        ('type', shared.DateRange),


        ('cardinality', "0.1"),



    ),

    (activity.SpatioTemporalConstraint, 'source'): (

        ('type', shared.DataSource),


        ('cardinality', "0.1"),



    ),

    (activity.SpatioTemporalConstraint, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.SpatioTemporalConstraint, 'spatial_resolution'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.SpatioTemporalConstraint, 'options'): (

        ('type', activity.NumericalRequirementOption),


        ('cardinality', "0.N"),



    ),

    (activity.SpatioTemporalConstraint, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (data.DataExtent, 'geographical'): (

        ('type', data.DataExtentGeographical),


        ('cardinality', "1.1"),



    ),

    (data.DataExtent, 'temporal'): (

        ('type', data.DataExtentTemporal),


        ('cardinality', "1.1"),



    ),



    (data.DataStorageFile, 'modification_date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageFile, 'path'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageFile, 'size'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageFile, 'file_system'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageFile, 'format'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageFile, 'file_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageFile, 'location'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (activity.DownscalingSimulation, 'downscaling_id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.DownscalingSimulation, 'supports'): (

        ('type', activity.Experiment),


        ('cardinality', "0.N"),



    ),

    (activity.DownscalingSimulation, 'inputs'): (

        ('type', software.Coupling),


        ('cardinality', "0.N"),



    ),

    (activity.DownscalingSimulation, 'downscaled_from'): (

        ('type', shared.DataSource),


        ('cardinality', "1.1"),



    ),

    (activity.DownscalingSimulation, 'rationales'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.DownscalingSimulation, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.DownscalingSimulation, 'downscaling_type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.DownscalingSimulation, 'short_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.DownscalingSimulation, 'projects'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.DownscalingSimulation, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),

    (activity.DownscalingSimulation, 'calendar'): (

        ('type', shared.Calendar),


        ('cardinality', "1.1"),



    ),

    (activity.DownscalingSimulation, 'outputs'): (

        ('type', data.DataObject),


        ('cardinality', "0.N"),



    ),

    (activity.DownscalingSimulation, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (activity.DownscalingSimulation, 'funding_sources'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.DownscalingSimulation, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (shared.Daily360, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Daily360, 'length'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (shared.Daily360, 'range'): (

        ('type', shared.DateRange),


        ('cardinality', "0.1"),



    ),



    (activity.SimulationComposite, 'child'): (

        ('type', activity.Simulation),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationComposite, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationComposite, 'authors'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationComposite, 'spinup_simulation'): (

        ('type', activity.Simulation),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationComposite, 'date_range'): (

        ('type', shared.DateRange),


        ('cardinality', "1.1"),



    ),

    (activity.SimulationComposite, 'calendar'): (

        ('type', shared.Calendar),


        ('cardinality', "1.1"),



    ),

    (activity.SimulationComposite, 'inputs'): (

        ('type', software.Coupling),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationComposite, 'rank'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (activity.SimulationComposite, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationComposite, 'projects'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationComposite, 'control_simulation'): (

        ('type', activity.Simulation),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationComposite, 'spinup_date_range'): (

        ('type', shared.ClosedDateRange),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationComposite, 'funding_sources'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationComposite, 'supports'): (

        ('type', activity.Experiment),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationComposite, 'simulation_id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationComposite, 'deployments'): (

        ('type', software.Deployment),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationComposite, 'rationales'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationComposite, 'restarts'): (

        ('type', data.DataObject),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationComposite, 'outputs'): (

        ('type', data.DataObject),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationComposite, 'conformances'): (

        ('type', activity.Conformance),


        ('cardinality', "0.N"),



    ),

    (activity.SimulationComposite, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (activity.SimulationComposite, 'short_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.SimulationComposite, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),



    (software.SpatialRegriddingUserMethod, 'file'): (

        ('type', data.DataObject),


        ('cardinality', "0.1"),



    ),

    (software.SpatialRegriddingUserMethod, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (software.Deployment, 'deployment_date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (software.Deployment, 'executable_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Deployment, 'parallelisation'): (

        ('type', software.Parallelisation),


        ('cardinality', "0.1"),



    ),

    (software.Deployment, 'executable_arguments'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (software.Deployment, 'platform'): (

        ('type', shared.Platform),


        ('cardinality', "0.1"),



    ),

    (software.Deployment, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (data.DataProperty, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataProperty, 'value'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataProperty, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (data.DataStorageIp, 'protocol'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageIp, 'modification_date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageIp, 'host'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageIp, 'location'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageIp, 'path'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageIp, 'format'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageIp, 'file_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageIp, 'size'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),



    (grids.GridSpec, 'esm_model_grids'): (

        ('type', grids.GridMosaic),


        ('cardinality', "0.N"),



    ),

    (grids.GridSpec, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (grids.GridSpec, 'esm_exchange_grids'): (

        ('type', grids.GridMosaic),


        ('cardinality', "0.N"),



    ),



    (software.ComponentLanguageProperty, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ComponentLanguageProperty, 'value'): (

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



    (shared.ResponsibleParty, 'abbreviation'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ResponsibleParty, 'role'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ResponsibleParty, 'email'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ResponsibleParty, 'url'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ResponsibleParty, 'address'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ResponsibleParty, 'individual_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ResponsibleParty, 'organisation_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (data.DataExtentTemporal, 'begin'): (

        ('type', datetime.date),


        ('cardinality', "0.1"),



    ),

    (data.DataExtentTemporal, 'end'): (

        ('type', datetime.date),


        ('cardinality', "0.1"),



    ),

    (data.DataExtentTemporal, 'time_interval'): (

        ('type', data.DataExtentTimeInterval),


        ('cardinality', "0.1"),



    ),



    (activity.Experiment, 'requires'): (

        ('type', activity.NumericalActivity),


        ('cardinality', "0.N"),



    ),

    (activity.Experiment, 'generates'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.Experiment, 'rationales'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.Experiment, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),

    (activity.Experiment, 'supports'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.Experiment, 'measurement_campaigns'): (

        ('type', activity.MeasurementCampaign),


        ('cardinality', "0.N"),



    ),

    (activity.Experiment, 'funding_sources'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.Experiment, 'projects'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),



    (grids.GridProperty, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridProperty, 'value'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (grids.VerticalCoordinateList, 'length'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (grids.VerticalCoordinateList, 'properties'): (

        ('type', grids.GridProperty),


        ('cardinality', "0.N"),



    ),

    (grids.VerticalCoordinateList, 'has_constant_offset'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (grids.VerticalCoordinateList, 'uom'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.VerticalCoordinateList, 'form'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.VerticalCoordinateList, 'type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (activity.NumericalRequirementOption, 'sub_options'): (

        ('type', activity.NumericalRequirementOption),


        ('cardinality', "0.N"),



    ),

    (activity.NumericalRequirementOption, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.NumericalRequirementOption, 'relationship'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.NumericalRequirementOption, 'id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.NumericalRequirementOption, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (shared.ChangeProperty, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ChangeProperty, 'value'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ChangeProperty, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.ChangeProperty, 'id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (grids.GridTileResolutionType, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridTileResolutionType, 'properties'): (

        ('type', grids.GridProperty),


        ('cardinality', "0.N"),



    ),



    (activity.EnsembleMember, 'supports'): (

        ('type', activity.Experiment),


        ('cardinality', "0.N"),



    ),

    (activity.EnsembleMember, 'ensemble'): (

        ('type', activity.Ensemble),


        ('cardinality', "0.1"),



    ),

    (activity.EnsembleMember, 'rationales'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.EnsembleMember, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.EnsembleMember, 'ensemble_ids'): (

        ('type', shared.StandardName),


        ('cardinality', "0.N"),



    ),

    (activity.EnsembleMember, 'short_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.EnsembleMember, 'projects'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.EnsembleMember, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),

    (activity.EnsembleMember, 'simulation'): (

        ('type', activity.Simulation),


        ('cardinality', "0.1"),



    ),

    (activity.EnsembleMember, 'funding_sources'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.EnsembleMember, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (software.TimeLag, 'units'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.TimeLag, 'value'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),



    (software.StatisticalModelComponent, 'timing'): (

        ('type', software.Timing),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'properties'): (

        ('type', software.ComponentProperty),


        ('cardinality', "0.N"),



    ),

    (software.StatisticalModelComponent, 'online_resource'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'purpose'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'funding_sources'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (software.StatisticalModelComponent, 'previous_version'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'version'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'grid'): (

        ('type', grids.GridSpec),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'code_access'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'composition'): (

        ('type', software.Composition),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'language'): (

        ('type', software.ComponentLanguage),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'parent'): (

        ('type', software.Component),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'license'): (

        ('type', shared.License),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'short_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (software.StatisticalModelComponent, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (software.StatisticalModelComponent, 'citations'): (

        ('type', shared.Citation),


        ('cardinality', "0.N"),



    ),

    (software.StatisticalModelComponent, 'type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'is_embedded'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'release_date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),

    (software.StatisticalModelComponent, 'types'): (

        ('type', unicode),


        ('cardinality', "1.N"),



    ),

    (software.StatisticalModelComponent, 'sub_components'): (

        ('type', software.Component),


        ('cardinality', "0.N"),



    ),

    (software.StatisticalModelComponent, 'coupling_framework'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.StatisticalModelComponent, 'deployments'): (

        ('type', software.Deployment),


        ('cardinality', "0.N"),



    ),

    (software.StatisticalModelComponent, 'dependencies'): (

        ('type', software.EntryPoint),


        ('cardinality', "0.N"),



    ),



    (data.DataDistribution, 'fee'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataDistribution, 'responsible_party'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.1"),



    ),

    (data.DataDistribution, 'access'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataDistribution, 'format'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (quality.CimQuality, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (quality.CimQuality, 'reports'): (

        ('type', quality.Report),


        ('cardinality', "0.N"),



    ),



    (data.DataRestriction, 'license'): (

        ('type', shared.License),


        ('cardinality', "0.1"),



    ),

    (data.DataRestriction, 'restriction'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataRestriction, 'scope'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (software.CouplingEndpoint, 'instance_id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.CouplingEndpoint, 'properties'): (

        ('type', software.CouplingProperty),


        ('cardinality', "0.N"),



    ),

    (software.CouplingEndpoint, 'data_source'): (

        ('type', shared.DataSource),


        ('cardinality', "0.1"),



    ),



    (shared.Property, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Property, 'value'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (shared.Platform, 'contacts'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),

    (shared.Platform, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Platform, 'units'): (

        ('type', shared.MachineCompilerUnit),


        ('cardinality', "1.N"),



    ),

    (shared.Platform, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Platform, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (shared.Platform, 'short_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (shared.DataSource, 'purpose'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (grids.GridMosaic, 'tiles'): (

        ('type', grids.GridTile),


        ('cardinality', "0.N"),



    ),

    (grids.GridMosaic, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridMosaic, 'is_leaf'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (grids.GridMosaic, 'mosaics'): (

        ('type', grids.GridMosaic),


        ('cardinality', "0.N"),



    ),

    (grids.GridMosaic, 'extent'): (

        ('type', grids.GridExtent),


        ('cardinality', "0.1"),



    ),

    (grids.GridMosaic, 'citations'): (

        ('type', shared.Citation),


        ('cardinality', "0.N"),



    ),

    (grids.GridMosaic, 'short_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (grids.GridMosaic, 'id'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (grids.GridMosaic, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridMosaic, 'mnemonic'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.GridMosaic, 'type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (grids.GridMosaic, 'tile_count'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (grids.GridMosaic, 'mosaic_count'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (grids.GridMosaic, 'has_congruent_tiles'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),



    (software.TimeTransformation, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.TimeTransformation, 'mapping_type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (activity.LateralBoundaryCondition, 'source'): (

        ('type', shared.DataSource),


        ('cardinality', "0.1"),



    ),

    (activity.LateralBoundaryCondition, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.LateralBoundaryCondition, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.LateralBoundaryCondition, 'id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.LateralBoundaryCondition, 'options'): (

        ('type', activity.NumericalRequirementOption),


        ('cardinality', "0.N"),



    ),

    (activity.LateralBoundaryCondition, 'requirement_type'): (

        ('type', unicode),


        ('cardinality', "1.1"),


        ('constant', "lateralBoundaryCondition"),


    ),



    (shared.License, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.License, 'is_unrestricted'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (shared.License, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.License, 'contact'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (activity.ExperimentRelationshipTarget, 'numerical_experiment'): (

        ('type', activity.NumericalExperiment),


        ('cardinality', "0.1"),



    ),



    (data.DataStorageDb, 'table'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageDb, 'size'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageDb, 'access_string'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageDb, 'format'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageDb, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageDb, 'modification_date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageDb, 'owner'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataStorageDb, 'location'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (software.Component, 'online_resource'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Component, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Component, 'composition'): (

        ('type', software.Composition),


        ('cardinality', "0.1"),



    ),

    (software.Component, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Component, 'purpose'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Component, 'funding_sources'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (software.Component, 'license'): (

        ('type', shared.License),


        ('cardinality', "0.1"),



    ),

    (software.Component, 'grid'): (

        ('type', grids.GridSpec),


        ('cardinality', "0.1"),



    ),

    (software.Component, 'properties'): (

        ('type', software.ComponentProperty),


        ('cardinality', "0.N"),



    ),

    (software.Component, 'code_access'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Component, 'release_date'): (

        ('type', datetime.datetime),


        ('cardinality', "0.1"),



    ),

    (software.Component, 'previous_version'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Component, 'language'): (

        ('type', software.ComponentLanguage),


        ('cardinality', "0.1"),



    ),

    (software.Component, 'citations'): (

        ('type', shared.Citation),


        ('cardinality', "0.N"),



    ),

    (software.Component, 'short_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (software.Component, 'is_embedded'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),

    (software.Component, 'parent'): (

        ('type', software.Component),


        ('cardinality', "0.1"),



    ),

    (software.Component, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),

    (software.Component, 'version'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Component, 'sub_components'): (

        ('type', software.Component),


        ('cardinality', "0.N"),



    ),

    (software.Component, 'coupling_framework'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Component, 'deployments'): (

        ('type', software.Deployment),


        ('cardinality', "0.N"),



    ),

    (software.Component, 'dependencies'): (

        ('type', software.EntryPoint),


        ('cardinality', "0.N"),



    ),



    (shared.Standard, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.Standard, 'version'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Standard, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (data.DataExtentTimeInterval, 'radix'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (data.DataExtentTimeInterval, 'unit'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (data.DataExtentTimeInterval, 'factor'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),



    (activity.NumericalExperiment, 'experiment_id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.NumericalExperiment, 'funding_sources'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.NumericalExperiment, 'requires'): (

        ('type', activity.NumericalActivity),


        ('cardinality', "0.N"),



    ),

    (activity.NumericalExperiment, 'requirements'): (

        ('type', activity.NumericalRequirement),


        ('cardinality', "0.N"),



    ),

    (activity.NumericalExperiment, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.NumericalExperiment, 'generates'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.NumericalExperiment, 'rationales'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.NumericalExperiment, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (activity.NumericalExperiment, 'projects'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.NumericalExperiment, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),

    (activity.NumericalExperiment, 'measurement_campaigns'): (

        ('type', activity.MeasurementCampaign),


        ('cardinality', "0.N"),



    ),

    (activity.NumericalExperiment, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.NumericalExperiment, 'short_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.NumericalExperiment, 'supports'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),



    (activity.MeasurementCampaign, 'duration'): (

        ('type', int),


        ('cardinality', "1.1"),



    ),

    (activity.MeasurementCampaign, 'rationales'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.MeasurementCampaign, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),

    (activity.MeasurementCampaign, 'funding_sources'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.MeasurementCampaign, 'projects'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),



    (activity.BoundaryCondition, 'source'): (

        ('type', shared.DataSource),


        ('cardinality', "0.1"),



    ),

    (activity.BoundaryCondition, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.BoundaryCondition, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.BoundaryCondition, 'id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.BoundaryCondition, 'options'): (

        ('type', activity.NumericalRequirementOption),


        ('cardinality', "0.N"),



    ),

    (activity.BoundaryCondition, 'requirement_type'): (

        ('type', unicode),


        ('cardinality', "1.1"),


        ('constant', "boundaryCondition"),


    ),



    (software.EntryPoint, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (software.Connection, 'properties'): (

        ('type', software.ConnectionProperty),


        ('cardinality', "0.N"),



    ),

    (software.Connection, 'time_transformation'): (

        ('type', software.TimeTransformation),


        ('cardinality', "0.1"),



    ),

    (software.Connection, 'priming'): (

        ('type', shared.DataSource),


        ('cardinality', "0.1"),



    ),

    (software.Connection, 'spatial_regridding'): (

        ('type', software.SpatialRegridding),


        ('cardinality', "0.N"),



    ),

    (software.Connection, 'target'): (

        ('type', software.ConnectionEndpoint),


        ('cardinality', "0.1"),



    ),

    (software.Connection, 'transformers'): (

        ('type', software.ProcessorComponent),


        ('cardinality', "0.N"),



    ),

    (software.Connection, 'time_lag'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Connection, 'type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Connection, 'sources'): (

        ('type', software.ConnectionEndpoint),


        ('cardinality', "0.N"),



    ),

    (software.Connection, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Connection, 'time_profile'): (

        ('type', software.Timing),


        ('cardinality', "0.1"),



    ),



    (shared.Compiler, 'type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Compiler, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.Compiler, 'language'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Compiler, 'options'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Compiler, 'version'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (shared.Compiler, 'environment_variables'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (activity.Ensemble, 'funding_sources'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.Ensemble, 'members'): (

        ('type', activity.EnsembleMember),


        ('cardinality', "1.N"),



    ),

    (activity.Ensemble, 'projects'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.Ensemble, 'short_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.Ensemble, 'types'): (

        ('type', unicode),


        ('cardinality', "1.N"),



    ),

    (activity.Ensemble, 'rationales'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.Ensemble, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Ensemble, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),

    (activity.Ensemble, 'outputs'): (

        ('type', shared.DataSource),


        ('cardinality', "0.N"),



    ),

    (activity.Ensemble, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Ensemble, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (activity.Ensemble, 'supports'): (

        ('type', activity.Experiment),


        ('cardinality', "0.N"),



    ),



    (activity.OutputRequirement, 'source'): (

        ('type', shared.DataSource),


        ('cardinality', "0.1"),



    ),

    (activity.OutputRequirement, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.OutputRequirement, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.OutputRequirement, 'id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.OutputRequirement, 'options'): (

        ('type', activity.NumericalRequirementOption),


        ('cardinality', "0.N"),



    ),

    (activity.OutputRequirement, 'requirement_type'): (

        ('type', unicode),


        ('cardinality', "1.1"),


        ('constant', "outputRequirement"),


    ),



    (shared.StandardName, 'is_open'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (shared.StandardName, 'standards'): (

        ('type', shared.Standard),


        ('cardinality', "0.N"),



    ),

    (shared.StandardName, 'value'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (shared.DocRelationshipTarget, 'reference'): (

        ('type', shared.DocReference),


        ('cardinality', "0.1"),



    ),



    (shared.MachineCompilerUnit, 'compilers'): (

        ('type', shared.Compiler),


        ('cardinality', "0.N"),



    ),

    (shared.MachineCompilerUnit, 'machine'): (

        ('type', shared.Machine),


        ('cardinality', "1.1"),



    ),



    (quality.Measure, 'identification'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (quality.Measure, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (quality.Measure, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (software.Rank, 'increment'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (software.Rank, 'min'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (software.Rank, 'value'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (software.Rank, 'max'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),



    (activity.SimulationRelationship, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.SimulationRelationship, 'direction'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.SimulationRelationship, 'target'): (

        ('type', activity.SimulationRelationshipTarget),


        ('cardinality', "1.1"),



    ),

    (activity.SimulationRelationship, 'type'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),



    (software.ConnectionEndpoint, 'instance_id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ConnectionEndpoint, 'data_source'): (

        ('type', shared.DataSource),


        ('cardinality', "0.1"),



    ),

    (software.ConnectionEndpoint, 'properties'): (

        ('type', software.ConnectionProperty),


        ('cardinality', "0.N"),



    ),



    (data.DataExtentGeographical, 'east'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (data.DataExtentGeographical, 'north'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (data.DataExtentGeographical, 'south'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),

    (data.DataExtentGeographical, 'west'): (

        ('type', float),


        ('cardinality', "0.1"),



    ),



    (grids.CoordinateList, 'length'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (grids.CoordinateList, 'uom'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (grids.CoordinateList, 'has_constant_offset'): (

        ('type', bool),


        ('cardinality', "0.1"),



    ),



    (misc.DocumentSet, 'meta'): (

        ('type', shared.DocMetaInfo),


        ('cardinality', "1.1"),



    ),

    (misc.DocumentSet, 'grids'): (

        ('type', grids.GridSpec),


        ('cardinality', "0.N"),



    ),

    (misc.DocumentSet, 'data'): (

        ('type', data.DataObject),


        ('cardinality', "0.N"),



    ),

    (misc.DocumentSet, 'model'): (

        ('type', software.ModelComponent),


        ('cardinality', "0.1"),



    ),

    (misc.DocumentSet, 'ensembles'): (

        ('type', activity.Ensemble),


        ('cardinality', "0.N"),



    ),

    (misc.DocumentSet, 'platform'): (

        ('type', shared.Platform),


        ('cardinality', "0.1"),



    ),

    (misc.DocumentSet, 'experiment'): (

        ('type', activity.NumericalExperiment),


        ('cardinality', "0.1"),



    ),

    (misc.DocumentSet, 'simulation'): (

        ('type', activity.SimulationRun),


        ('cardinality', "0.1"),



    ),



    (activity.Simulation, 'funding_sources'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.Simulation, 'rationales'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.Simulation, 'deployments'): (

        ('type', software.Deployment),


        ('cardinality', "0.N"),



    ),

    (activity.Simulation, 'authors'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Simulation, 'outputs'): (

        ('type', data.DataObject),


        ('cardinality', "0.N"),



    ),

    (activity.Simulation, 'simulation_id'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Simulation, 'projects'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (activity.Simulation, 'short_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (activity.Simulation, 'inputs'): (

        ('type', software.Coupling),


        ('cardinality', "0.N"),



    ),

    (activity.Simulation, 'calendar'): (

        ('type', shared.Calendar),


        ('cardinality', "1.1"),



    ),

    (activity.Simulation, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Simulation, 'responsible_parties'): (

        ('type', shared.ResponsibleParty),


        ('cardinality', "0.N"),



    ),

    (activity.Simulation, 'control_simulation'): (

        ('type', activity.Simulation),


        ('cardinality', "0.1"),



    ),

    (activity.Simulation, 'restarts'): (

        ('type', data.DataObject),


        ('cardinality', "0.N"),



    ),

    (activity.Simulation, 'spinup_date_range'): (

        ('type', shared.ClosedDateRange),


        ('cardinality', "0.1"),



    ),

    (activity.Simulation, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (activity.Simulation, 'conformances'): (

        ('type', activity.Conformance),


        ('cardinality', "0.N"),



    ),

    (activity.Simulation, 'supports'): (

        ('type', activity.Experiment),


        ('cardinality', "0.N"),



    ),

    (activity.Simulation, 'spinup_simulation'): (

        ('type', activity.Simulation),


        ('cardinality', "0.1"),



    ),



    (software.ComponentProperty, 'is_represented'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (software.ComponentProperty, 'short_name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (software.ComponentProperty, 'units'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ComponentProperty, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ComponentProperty, 'purpose'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ComponentProperty, 'grid'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ComponentProperty, 'standard_names'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (software.ComponentProperty, 'values'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (software.ComponentProperty, 'long_name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ComponentProperty, 'intent'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ComponentProperty, 'citations'): (

        ('type', shared.Citation),


        ('cardinality', "0.N"),



    ),

    (software.ComponentProperty, 'sub_properties'): (

        ('type', software.ComponentProperty),


        ('cardinality', "0.N"),



    ),



    (software.ConnectionProperty, 'name'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.ConnectionProperty, 'value'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (software.Coupling, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Coupling, 'purpose'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),

    (software.Coupling, 'spatial_regriddings'): (

        ('type', software.SpatialRegridding),


        ('cardinality', "0.N"),



    ),

    (software.Coupling, 'transformers'): (

        ('type', software.ProcessorComponent),


        ('cardinality', "0.N"),



    ),

    (software.Coupling, 'properties'): (

        ('type', software.CouplingProperty),


        ('cardinality', "0.N"),



    ),

    (software.Coupling, 'connections'): (

        ('type', software.Connection),


        ('cardinality', "0.N"),



    ),

    (software.Coupling, 'sources'): (

        ('type', software.CouplingEndpoint),


        ('cardinality', "1.N"),



    ),

    (software.Coupling, 'time_lag'): (

        ('type', software.TimeLag),


        ('cardinality', "0.1"),



    ),

    (software.Coupling, 'target'): (

        ('type', software.CouplingEndpoint),


        ('cardinality', "1.1"),



    ),

    (software.Coupling, 'is_fully_specified'): (

        ('type', bool),


        ('cardinality', "1.1"),



    ),

    (software.Coupling, 'time_profile'): (

        ('type', software.Timing),


        ('cardinality', "0.1"),



    ),

    (software.Coupling, 'type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (software.Coupling, 'time_transformation'): (

        ('type', software.TimeTransformation),


        ('cardinality', "0.1"),



    ),

    (software.Coupling, 'priming'): (

        ('type', shared.DataSource),


        ('cardinality', "0.1"),



    ),



    (shared.DateRange, 'duration'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),



    (shared.Machine, 'location'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Machine, 'type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Machine, 'description'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Machine, 'maximum_processors'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (shared.Machine, 'vendor'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Machine, 'cores_per_processor'): (

        ('type', int),


        ('cardinality', "0.1"),



    ),

    (shared.Machine, 'operating_system'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Machine, 'processor_type'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Machine, 'interconnect'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Machine, 'libraries'): (

        ('type', unicode),


        ('cardinality', "0.N"),



    ),

    (shared.Machine, 'system'): (

        ('type', unicode),


        ('cardinality', "0.1"),



    ),

    (shared.Machine, 'name'): (

        ('type', unicode),


        ('cardinality', "1.1"),



    ),


}