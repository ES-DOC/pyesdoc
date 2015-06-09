# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.decoder_for_activity_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-05 15:44:25.785464.

"""
from decoder_xml_utils import set_attributes
from decoder_for_data_package import *
from decoder_for_shared_package import *
from decoder_for_software_package import *
import typeset



def decode_boundary_condition(xml, nsmap):
    """Decodes an instance of the following type: boundary condition.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.BoundaryCondition

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('description', False, 'str', 'child::cim:description'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source_reference', False, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('id', False, 'str', 'child::cim:id'),
    ]

    return set_attributes(typeset.activity.BoundaryCondition(), xml, nsmap, decodings)


def decode_experiment_relationship(xml, nsmap):
    """Decodes an instance of the following type: experiment relationship.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.ExperimentRelationship

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.ExperimentRelationship(), xml, nsmap, decodings)


def decode_lateral_boundary_condition(xml, nsmap):
    """Decodes an instance of the following type: lateral boundary condition.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.LateralBoundaryCondition

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('description', False, 'str', 'child::cim:description'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source_reference', False, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('id', False, 'str', 'child::cim:id'),
    ]

    return set_attributes(typeset.activity.LateralBoundaryCondition(), xml, nsmap, decodings)


def decode_physical_modification(xml, nsmap):
    """Decodes an instance of the following type: physical modification.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.PhysicalModification

    """
    decodings = [
        ('requirements', True, decode_initial_condition, 'child::cim:requirement/cim:requirement/cim:initialCondition'),
        ('requirements', True, decode_lateral_boundary_condition, 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint'),
        ('requirements', True, decode_boundary_condition, 'child::cim:requirement/cim:requirement/cim:boundaryCondition'),
        ('requirements', True, decode_output_requirement, 'child::cim:requirement/cim:requirement/cim:outputRequirement'),
        ('type', False, 'str', '@type'),
        ('description', False, 'str', 'child::cim:description'),
        ('requirements_references', True, decode_doc_reference, 'child::cim:requirement/cim:reference'),
        ('frequency', False, 'str', 'child::cim:frequency'),
        ('sources', True, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('sources', True, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('sources', True, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('sources', True, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('is_conformant', False, 'bool', '@conformant'),
        ('sources_references', True, decode_doc_reference, 'child::cim:source/cim:reference'),
    ]

    return set_attributes(typeset.activity.PhysicalModification(), xml, nsmap, decodings)


def decode_activity(xml, nsmap):
    """Decodes an instance of the following type: activity.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.Activity

    """
    decodings = [
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('rationales', True, 'str', 'child::cim:rationale'),
    ]

    return set_attributes(typeset.activity.Activity(), xml, nsmap, decodings)


def decode_simulation_relationship_target(xml, nsmap):
    """Decodes an instance of the following type: simulation relationship target.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.SimulationRelationshipTarget

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.SimulationRelationshipTarget(), xml, nsmap, decodings)


def decode_initial_condition(xml, nsmap):
    """Decodes an instance of the following type: initial condition.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.InitialCondition

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('description', False, 'str', 'child::cim:description'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source_reference', False, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('id', False, 'str', 'child::cim:id'),
    ]

    return set_attributes(typeset.activity.InitialCondition(), xml, nsmap, decodings)


def decode_experiment_relationship_target(xml, nsmap):
    """Decodes an instance of the following type: experiment relationship target.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.ExperimentRelationshipTarget

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.ExperimentRelationshipTarget(), xml, nsmap, decodings)


def decode_simulation(xml, nsmap):
    """Decodes an instance of the following type: simulation.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.Simulation

    """
    decodings = [
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('supports_references', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('control_simulation_reference', False, decode_doc_reference, 'child::cim:controlSimulation/cim:reference'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('simulation_id', False, 'str', 'child::cim:simulationID'),
        ('conformances', True, decode_conformance, 'child::cim:conformance/cim:conformance'),
        ('conformances', True, decode_physical_modification, 'child::cim:conformance/cim:physicalModification'),
        ('authors', False, 'str', 'child::cim:authorsList/cim:list'),
        ('spinup_date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('deployments', True, decode_deployment, 'child::cim:deployment'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('description', False, 'str', 'child::cim:description'),
        ('control_simulation', False, decode_simulation, 'child::cim:controlSimulation/cim:controlSimulation'),
        ('calendar', False, decode_daily_360, 'child::cim:calendar/cim:daily-360'),
        ('calendar', False, decode_perpetual_period, 'child::cim:calendar/cim:perpetualPeriod'),
        ('calendar', False, decode_real_calendar, 'child::cim:calendar/cim:realCalendar'),
    ]

    return set_attributes(typeset.activity.Simulation(), xml, nsmap, decodings)


def decode_simulation_relationship(xml, nsmap):
    """Decodes an instance of the following type: simulation relationship.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.SimulationRelationship

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.SimulationRelationship(), xml, nsmap, decodings)


def decode_downscaling_simulation(xml, nsmap):
    """Decodes an instance of the following type: downscaling simulation.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.DownscalingSimulation

    """
    decodings = [
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('meta', False, decode_doc_meta_info, 'self::cim:downscalingSimulation'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('downscaling_id', False, 'str', 'child::cim:downscalingID'),
        ('supports_references', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('downscaled_from', False, decode_data_object, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:dataObject'),
        ('downscaled_from', False, decode_data_content, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:dataContent'),
        ('downscaled_from', False, decode_component_property, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:componentProperty'),
        ('downscaled_from', False, decode_model_component, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:softwareComponent'),
        ('downscaled_from', False, decode_processor_component, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:softwareComponent'),
        ('downscaled_from', False, decode_statistical_model_component, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:softwareComponent'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('downscaled_from_reference', False, decode_doc_reference, 'child::cim:downscaledFrom/cim:reference'),
        ('outputs', True, decode_data_object, 'child::cim:output/cim:dataObject'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('description', False, 'str', 'child::cim:description'),
        ('downscaling_type', False, 'str', 'self::cim:downscalingSimulation/@downscalingType'),
        ('calendar', False, decode_daily_360, 'child::cim:calendar/cim:daily-360'),
        ('calendar', False, decode_perpetual_period, 'child::cim:calendar/cim:perpetualPeriod'),
        ('calendar', False, decode_real_calendar, 'child::cim:calendar/cim:realCalendar'),
    ]

    return set_attributes(typeset.activity.DownscalingSimulation(), xml, nsmap, decodings)


def decode_simulation_run(xml, nsmap):
    """Decodes an instance of the following type: simulation run.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.SimulationRun

    """
    decodings = [
        ('calendar', False, decode_daily_360, 'child::cim:calendar/cim:daily-360'),
        ('calendar', False, decode_perpetual_period, 'child::cim:calendar/cim:perpetualPeriod'),
        ('calendar', False, decode_real_calendar, 'child::cim:calendar/cim:realCalendar'),
        ('meta', False, decode_doc_meta_info, 'self::cim:simulationRun'),
        ('control_simulation_reference', False, decode_doc_reference, 'child::cim:controlSimulation/cim:reference'),
        ('control_simulation', False, decode_simulation, 'child::cim:controlSimulation/cim:controlSimulation'),
        ('date_range', False, decode_open_date_range, 'child::cim:dateRange/cim:openDateRange'),
        ('date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('conformances', True, decode_conformance, 'child::cim:conformance/cim:conformance'),
        ('conformances', True, decode_physical_modification, 'child::cim:conformance/cim:physicalModification'),
        ('authors', False, 'str', 'child::cim:authorsList/cim:list'),
        ('model', False, decode_model_component, 'child::cim:model/cim:modelComponent'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('model_reference', False, decode_doc_reference, 'child::cim:model/cim:reference'),
        ('supports_references', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('spinup_date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('simulation_id', False, 'str', 'child::cim:simulationID'),
        ('description', False, 'str', 'child::cim:description'),
        ('deployments', True, decode_deployment, 'child::cim:deployment'),
    ]

    return set_attributes(typeset.activity.SimulationRun(), xml, nsmap, decodings)


def decode_spatio_temporal_constraint(xml, nsmap):
    """Decodes an instance of the following type: spatio temporal constraint.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.SpatioTemporalConstraint

    """
    decodings = [
        ('spatial_resolution', False, 'str', 'child::cim:spatialResolution'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source_reference', False, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('name', False, 'str', 'child::cim:name'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('description', False, 'str', 'child::cim:description'),
        ('date_range', False, decode_closed_date_range, 'child::cim:requiredDuration/cim:closedDateRange'),
        ('date_range', False, decode_open_date_range, 'child::cim:requiredDuration/cim:openDateRange'),
        ('id', False, 'str', 'child::cim:id'),
    ]

    return set_attributes(typeset.activity.SpatioTemporalConstraint(), xml, nsmap, decodings)


def decode_simulation_composite(xml, nsmap):
    """Decodes an instance of the following type: simulation composite.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.SimulationComposite

    """
    decodings = [
        ('calendar', False, decode_daily_360, 'child::cim:calendar/cim:daily-360'),
        ('calendar', False, decode_perpetual_period, 'child::cim:calendar/cim:perpetualPeriod'),
        ('calendar', False, decode_real_calendar, 'child::cim:calendar/cim:realCalendar'),
        ('control_simulation', False, decode_simulation, 'child::cim:controlSimulation/cim:controlSimulation'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('meta', False, decode_doc_meta_info, 'self::cim:simulationRun'),
        ('simulation_id', False, 'str', 'child::cim:simulationID'),
        ('child', True, decode_simulation_run, 'child::cim:child'),
        ('child', True, decode_simulation_composite, 'child::cim:child'),
        ('conformances', True, decode_conformance, 'child::cim:conformance/cim:conformance'),
        ('conformances', True, decode_physical_modification, 'child::cim:conformance/cim:physicalModification'),
        ('spinup_date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('deployments', True, decode_deployment, 'child::cim:deployment'),
        ('date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('date_range', False, decode_open_date_range, 'child::cim:dateRange/cim:openDateRange'),
        ('rank', False, 'int', 'child::cim:rank'),
        ('control_simulation_reference', False, decode_doc_reference, 'child::cim:controlSimulation/cim:reference'),
        ('authors', False, 'str', 'child::cim:authorsList/cim:list'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('supports_references', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('description', False, 'str', 'child::cim:description'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
    ]

    return set_attributes(typeset.activity.SimulationComposite(), xml, nsmap, decodings)


def decode_ensemble_member(xml, nsmap):
    """Decodes an instance of the following type: ensemble member.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.EnsembleMember

    """
    decodings = [
        ('simulation', False, decode_simulation, 'child::cim:ensemble/cim:simulation'),
        ('supports_references', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('ensemble', False, decode_ensemble, 'child::cim:ensemble/cim:ensemble'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('ensemble_reference', False, decode_doc_reference, 'child::cim:ensemble/cim:reference'),
        ('description', False, 'str', 'child::cim:description'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('simulation_reference', False, decode_doc_reference, 'child::cim:simulation/cim:reference'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('ensemble_ids', True, decode_standard_name, 'child::cim:ensembleMemberID'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
    ]

    return set_attributes(typeset.activity.EnsembleMember(), xml, nsmap, decodings)


def decode_ensemble(xml, nsmap):
    """Decodes an instance of the following type: ensemble.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.Ensemble

    """
    decodings = [
        ('members', True, decode_ensemble_member, 'child::cim:ensembleMember'),
        ('supports_references', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('types', True, 'str', 'child::cim:ensembleType/@value'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('outputs', True, decode_statistical_model_component, 'child::cim:output/cim:output/cim:softwareComponent'),
        ('outputs', True, decode_data_object, 'child::cim:output/cim:output/cim:dataObject'),
        ('outputs', True, decode_data_content, 'child::cim:output/cim:output/cim:dataContent'),
        ('outputs', True, decode_component_property, 'child::cim:output/cim:output/cim:componentProperty'),
        ('outputs', True, decode_model_component, 'child::cim:output/cim:output/cim:softwareComponent'),
        ('outputs', True, decode_processor_component, 'child::cim:output/cim:output/cim:softwareComponent'),
        ('description', False, 'str', 'child::cim:description'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('meta', False, decode_doc_meta_info, 'self::cim:ensemble'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('outputs_references', True, decode_doc_reference, 'child::cim:output/cim:reference'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
    ]

    return set_attributes(typeset.activity.Ensemble(), xml, nsmap, decodings)


def decode_measurement_campaign(xml, nsmap):
    """Decodes an instance of the following type: measurement campaign.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.MeasurementCampaign

    """
    decodings = [
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
    ]

    return set_attributes(typeset.activity.MeasurementCampaign(), xml, nsmap, decodings)


def decode_numerical_experiment(xml, nsmap):
    """Decodes an instance of the following type: numerical experiment.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.NumericalExperiment

    """
    decodings = [
        ('requirements', True, decode_initial_condition, 'child::cim:numericalRequirement/cim:initialCondition'),
        ('requirements', True, decode_boundary_condition, 'child::cim:numericalRequirement/cim:boundaryCondition'),
        ('requirements', True, decode_output_requirement, 'child::cim:numericalRequirement/cim:outputRequirement'),
        ('requirements', True, decode_lateral_boundary_condition, 'child::cim:numericalRequirement/cim:lateralBoundaryCondition'),
        ('requirements', True, decode_initial_condition, 'child::cim:numericalRequirement[@xsi:type="InitialCondition"]'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:numericalRequirement/cim:spatioTemporalConstraint'),
        ('requirements', True, decode_boundary_condition, 'child::cim:numericalRequirement[@xsi:type="BoundaryCondition"]'),
        ('requirements', True, decode_lateral_boundary_condition, 'child::cim:numericalRequirement[@xsi:type="LateralBoundaryCondition"]'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:numericalRequirement[@xsi:type="SpatioTemporalConstraint"]'),
        ('requirements', True, decode_output_requirement, 'child::cim:numericalRequirement[@xsi:type="OutputRequirement"]'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('meta', False, decode_doc_meta_info, 'self::cim:numericalExperiment'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('description', False, 'str', 'child::cim:description'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('experiment_id', False, 'str', 'child::cim:experimentID'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('long_name', False, 'str', 'child::cim:longName'),
    ]

    return set_attributes(typeset.activity.NumericalExperiment(), xml, nsmap, decodings)


def decode_conformance(xml, nsmap):
    """Decodes an instance of the following type: conformance.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.Conformance

    """
    decodings = [
        ('requirements', True, decode_initial_condition, 'child::cim:requirement/cim:requirement/cim:initialCondition'),
        ('requirements', True, decode_lateral_boundary_condition, 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint'),
        ('requirements', True, decode_boundary_condition, 'child::cim:requirement/cim:requirement/cim:boundaryCondition'),
        ('requirements', True, decode_output_requirement, 'child::cim:requirement/cim:requirement/cim:outputRequirement'),
        ('type', False, 'str', '@type'),
        ('description', False, 'str', 'child::cim:description'),
        ('requirements_references', True, decode_doc_reference, 'child::cim:requirement/cim:reference'),
        ('frequency', False, 'str', 'child::cim:frequency'),
        ('sources', True, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('sources', True, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('sources', True, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('sources', True, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('is_conformant', False, 'bool', '@conformant'),
        ('sources_references', True, decode_doc_reference, 'child::cim:source/cim:reference'),
    ]

    return set_attributes(typeset.activity.Conformance(), xml, nsmap, decodings)


def decode_output_requirement(xml, nsmap):
    """Decodes an instance of the following type: output requirement.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.OutputRequirement

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('description', False, 'str', 'child::cim:description'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source_reference', False, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('id', False, 'str', 'child::cim:id'),
    ]

    return set_attributes(typeset.activity.OutputRequirement(), xml, nsmap, decodings)


def decode_numerical_activity(xml, nsmap):
    """Decodes an instance of the following type: numerical activity.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.NumericalActivity

    """
    decodings = [
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('description', False, 'str', 'child::cim:description'),
        ('supports_references', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('projects', True, 'str', 'child::cim:project/@value'),
    ]

    return set_attributes(typeset.activity.NumericalActivity(), xml, nsmap, decodings)


def decode_experiment(xml, nsmap):
    """Decodes an instance of the following type: experiment.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.Experiment

    """
    decodings = [
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
    ]

    return set_attributes(typeset.activity.Experiment(), xml, nsmap, decodings)


def decode_numerical_requirement_option(xml, nsmap):
    """Decodes an instance of the following type: numerical requirement option.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.NumericalRequirementOption

    """
    decodings = [
        ('id', False, 'str', 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint/cim:id'),
        ('id', False, 'str', 'child::cim:id'),
        ('id', False, 'str', 'child::cim:requirement/cim:requirement/cim:boundaryCondition/cim:id'),
        ('id', False, 'str', 'child::cim:requirement/cim:requirement/cim:initialCondition/cim:id'),
        ('id', False, 'str', 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition/cim:id'),
        ('id', False, 'str', 'child::cim:requirement/cim:requirement/cim:outputRequirement/cim:id'),
        ('description', False, 'str', 'child::cim:requirement/cim:requirement/cim:initialCondition/cim:description'),
        ('description', False, 'str', 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition/cim:description'),
        ('description', False, 'str', 'child::cim:requirement/cim:requirement/cim:outputRequirement/cim:description'),
        ('description', False, 'str', 'child::cim:description'),
        ('description', False, 'str', 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint/cim:description'),
        ('description', False, 'str', 'child::cim:requirement/cim:requirement/cim:boundaryCondition/cim:description'),
        ('name', False, 'str', 'child::cim:requirement/cim:requirement/cim:boundaryCondition/cim:name'),
        ('name', False, 'str', 'child::cim:requirement/cim:requirement/cim:initialCondition/cim:name'),
        ('name', False, 'str', 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition/cim:name'),
        ('name', False, 'str', 'child::cim:requirement/cim:requirement/cim:outputRequirement/cim:name'),
        ('name', False, 'str', 'child::cim:name'),
        ('name', False, 'str', 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint/cim:name'),
        ('relationship', False, 'str', 'self::cim:requirementOption/@optionRelationship'),
    ]

    return set_attributes(typeset.activity.NumericalRequirementOption(), xml, nsmap, decodings)


def decode_numerical_requirement(xml, nsmap):
    """Decodes an instance of the following type: numerical requirement.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.NumericalRequirement

    """
    decodings = [
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('id', False, 'str', 'child::cim:id'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source_reference', False, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('name', False, 'str', 'child::cim:name'),
        ('description', False, 'str', 'child::cim:description'),
    ]

    return set_attributes(typeset.activity.NumericalRequirement(), xml, nsmap, decodings)


