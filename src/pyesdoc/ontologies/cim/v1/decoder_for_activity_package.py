# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.decoder_for_activity_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
from decoder_xml_utils import set_attributes
from decoder_for_data_package import *
from decoder_for_shared_package import *
from decoder_for_software_package import *
import typeset



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
        ('id', False, 'str', 'child::cim:id'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('name', False, 'str', 'child::cim:name'),
        ('description', False, 'str', 'child::cim:description'),
        ('source_reference', False, decode_doc_reference, 'child::cim:source/cim:reference'),
    ]

    return set_attributes(typeset.activity.InitialCondition(), xml, nsmap, decodings)


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
        ('id', False, 'str', 'child::cim:id'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('name', False, 'str', 'child::cim:name'),
        ('date_range', False, decode_open_date_range, 'child::cim:requiredDuration/cim:openDateRange'),
        ('date_range', False, decode_closed_date_range, 'child::cim:requiredDuration/cim:closedDateRange'),
        ('source_reference', False, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('spatial_resolution', False, 'str', 'child::cim:spatialResolution'),
        ('description', False, 'str', 'child::cim:description'),
    ]

    return set_attributes(typeset.activity.SpatioTemporalConstraint(), xml, nsmap, decodings)


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
        ('long_name', False, 'str', 'child::cim:longName'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('ensemble_ids', True, decode_standard_name, 'child::cim:ensembleMemberID'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('simulation', False, decode_simulation, 'child::cim:ensemble/cim:simulation'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('ensemble', False, decode_ensemble, 'child::cim:ensemble/cim:ensemble'),
        ('supports_references', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('description', False, 'str', 'child::cim:description'),
        ('ensemble_reference', False, decode_doc_reference, 'child::cim:ensemble/cim:reference'),
        ('simulation_reference', False, decode_doc_reference, 'child::cim:simulation/cim:reference'),
    ]

    return set_attributes(typeset.activity.EnsembleMember(), xml, nsmap, decodings)


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
        ('long_name', False, 'str', 'child::cim:longName'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('description', False, 'str', 'child::cim:description'),
        ('supports_references', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('projects', True, 'str', 'child::cim:project/@value'),
    ]

    return set_attributes(typeset.activity.NumericalActivity(), xml, nsmap, decodings)


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
        ('id', False, 'str', 'child::cim:id'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('name', False, 'str', 'child::cim:name'),
        ('description', False, 'str', 'child::cim:description'),
        ('source_reference', False, decode_doc_reference, 'child::cim:source/cim:reference'),
    ]

    return set_attributes(typeset.activity.LateralBoundaryCondition(), xml, nsmap, decodings)


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
        ('id', False, 'str', 'child::cim:id'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('name', False, 'str', 'child::cim:name'),
        ('description', False, 'str', 'child::cim:description'),
        ('source_reference', False, decode_doc_reference, 'child::cim:source/cim:reference'),
    ]

    return set_attributes(typeset.activity.OutputRequirement(), xml, nsmap, decodings)


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
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('projects', True, 'str', 'child::cim:project/@value'),
    ]

    return set_attributes(typeset.activity.MeasurementCampaign(), xml, nsmap, decodings)


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
        ('id', False, 'str', 'child::cim:id'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('name', False, 'str', 'child::cim:name'),
        ('description', False, 'str', 'child::cim:description'),
        ('source_reference', False, decode_doc_reference, 'child::cim:source/cim:reference'),
    ]

    return set_attributes(typeset.activity.BoundaryCondition(), xml, nsmap, decodings)


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
        ('long_name', False, 'str', 'child::cim:longName'),
        ('meta', False, decode_doc_meta_info, 'self::cim:downscalingSimulation'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('downscaled_from', False, decode_statistical_model_component, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:softwareComponent'),
        ('downscaled_from', False, decode_data_object, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:dataObject'),
        ('downscaled_from', False, decode_data_content, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:dataContent'),
        ('downscaled_from', False, decode_component_property, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:componentProperty'),
        ('downscaled_from', False, decode_model_component, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:softwareComponent'),
        ('downscaled_from', False, decode_processor_component, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:softwareComponent'),
        ('downscaling_type', False, 'str', 'self::cim:downscalingSimulation/@downscalingType'),
        ('description', False, 'str', 'child::cim:description'),
        ('calendar', False, decode_daily_360, 'child::cim:calendar/cim:daily-360'),
        ('calendar', False, decode_perpetual_period, 'child::cim:calendar/cim:perpetualPeriod'),
        ('calendar', False, decode_real_calendar, 'child::cim:calendar/cim:realCalendar'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('supports_references', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('outputs', True, decode_data_object, 'child::cim:output/cim:dataObject'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('downscaling_id', False, 'str', 'child::cim:downscalingID'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('downscaled_from_reference', False, decode_doc_reference, 'child::cim:downscaledFrom/cim:reference'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('rationales', True, 'str', 'child::cim:rationale'),
    ]

    return set_attributes(typeset.activity.DownscalingSimulation(), xml, nsmap, decodings)


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
        ('name', False, 'str', 'child::cim:requirement/cim:requirement/cim:boundaryCondition/cim:name'),
        ('name', False, 'str', 'child::cim:requirement/cim:requirement/cim:initialCondition/cim:name'),
        ('name', False, 'str', 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition/cim:name'),
        ('name', False, 'str', 'child::cim:requirement/cim:requirement/cim:outputRequirement/cim:name'),
        ('name', False, 'str', 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint/cim:name'),
        ('name', False, 'str', 'child::cim:name'),
        ('id', False, 'str', 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint/cim:id'),
        ('id', False, 'str', 'child::cim:id'),
        ('id', False, 'str', 'child::cim:requirement/cim:requirement/cim:boundaryCondition/cim:id'),
        ('id', False, 'str', 'child::cim:requirement/cim:requirement/cim:initialCondition/cim:id'),
        ('id', False, 'str', 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition/cim:id'),
        ('id', False, 'str', 'child::cim:requirement/cim:requirement/cim:outputRequirement/cim:id'),
        ('relationship', False, 'str', 'self::cim:requirementOption/@optionRelationship'),
        ('description', False, 'str', 'child::cim:requirement/cim:requirement/cim:initialCondition/cim:description'),
        ('description', False, 'str', 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition/cim:description'),
        ('description', False, 'str', 'child::cim:requirement/cim:requirement/cim:outputRequirement/cim:description'),
        ('description', False, 'str', 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint/cim:description'),
        ('description', False, 'str', 'child::cim:description'),
        ('description', False, 'str', 'child::cim:requirement/cim:requirement/cim:boundaryCondition/cim:description'),
    ]

    return set_attributes(typeset.activity.NumericalRequirementOption(), xml, nsmap, decodings)


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
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:numericalRequirement/cim:spatioTemporalConstraint'),
        ('requirements', True, decode_initial_condition, 'child::cim:numericalRequirement[@xsi:type="InitialCondition"]'),
        ('requirements', True, decode_boundary_condition, 'child::cim:numericalRequirement[@xsi:type="BoundaryCondition"]'),
        ('requirements', True, decode_lateral_boundary_condition, 'child::cim:numericalRequirement[@xsi:type="LateralBoundaryCondition"]'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:numericalRequirement[@xsi:type="SpatioTemporalConstraint"]'),
        ('requirements', True, decode_output_requirement, 'child::cim:numericalRequirement[@xsi:type="OutputRequirement"]'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('meta', False, decode_doc_meta_info, 'self::cim:numericalExperiment'),
        ('description', False, 'str', 'child::cim:description'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('experiment_id', False, 'str', 'child::cim:experimentID'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
    ]

    return set_attributes(typeset.activity.NumericalExperiment(), xml, nsmap, decodings)


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
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(typeset.activity.Experiment(), xml, nsmap, decodings)


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
        ('sources_references', True, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('requirements', True, decode_boundary_condition, 'child::cim:requirement/cim:requirement/cim:boundaryCondition'),
        ('requirements', True, decode_initial_condition, 'child::cim:requirement/cim:requirement/cim:initialCondition'),
        ('requirements', True, decode_lateral_boundary_condition, 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition'),
        ('requirements', True, decode_output_requirement, 'child::cim:requirement/cim:requirement/cim:outputRequirement'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint'),
        ('frequency', False, 'str', 'child::cim:frequency'),
        ('description', False, 'str', 'child::cim:description'),
        ('requirements_references', True, decode_doc_reference, 'child::cim:requirement/cim:reference'),
        ('sources', True, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('sources', True, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('sources', True, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('type', False, 'str', '@type'),
        ('is_conformant', False, 'bool', '@conformant'),
    ]

    return set_attributes(typeset.activity.PhysicalModification(), xml, nsmap, decodings)


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
        ('id', False, 'str', 'child::cim:id'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('name', False, 'str', 'child::cim:name'),
        ('description', False, 'str', 'child::cim:description'),
        ('source_reference', False, decode_doc_reference, 'child::cim:source/cim:reference'),
    ]

    return set_attributes(typeset.activity.NumericalRequirement(), xml, nsmap, decodings)


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
        ('long_name', False, 'str', 'child::cim:longName'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('members', True, decode_ensemble_member, 'child::cim:ensembleMember'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('types', True, 'str', 'child::cim:ensembleType/@value'),
        ('meta', False, decode_doc_meta_info, 'self::cim:ensemble'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('outputs', True, decode_processor_component, 'child::cim:output/cim:output/cim:softwareComponent'),
        ('outputs', True, decode_statistical_model_component, 'child::cim:output/cim:output/cim:softwareComponent'),
        ('outputs', True, decode_data_object, 'child::cim:output/cim:output/cim:dataObject'),
        ('outputs', True, decode_data_content, 'child::cim:output/cim:output/cim:dataContent'),
        ('outputs', True, decode_component_property, 'child::cim:output/cim:output/cim:componentProperty'),
        ('outputs', True, decode_model_component, 'child::cim:output/cim:output/cim:softwareComponent'),
        ('supports_references', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('description', False, 'str', 'child::cim:description'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('outputs_references', True, decode_doc_reference, 'child::cim:output/cim:reference'),
        ('rationales', True, 'str', 'child::cim:rationale'),
    ]

    return set_attributes(typeset.activity.Ensemble(), xml, nsmap, decodings)


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
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('control_simulation', False, decode_simulation, 'child::cim:controlSimulation/cim:controlSimulation'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('simulation_id', False, 'str', 'child::cim:simulationID'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('authors', False, 'str', 'child::cim:authorsList/cim:list'),
        ('description', False, 'str', 'child::cim:description'),
        ('rank', False, 'int', 'child::cim:rank'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('supports_references', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('deployments', True, decode_deployment, 'child::cim:deployment'),
        ('control_simulation_reference', False, decode_doc_reference, 'child::cim:controlSimulation/cim:reference'),
        ('meta', False, decode_doc_meta_info, 'self::cim:simulationRun'),
        ('child', True, decode_simulation_composite, 'child::cim:child'),
        ('child', True, decode_simulation_run, 'child::cim:child'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('conformances', True, decode_physical_modification, 'child::cim:conformance/cim:physicalModification'),
        ('conformances', True, decode_conformance, 'child::cim:conformance/cim:conformance'),
        ('date_range', False, decode_open_date_range, 'child::cim:dateRange/cim:openDateRange'),
        ('date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('spinup_date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('projects', True, 'str', 'child::cim:project/@value'),
    ]

    return set_attributes(typeset.activity.SimulationComposite(), xml, nsmap, decodings)


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
        ('sources_references', True, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('is_conformant', False, 'bool', '@conformant'),
        ('requirements', True, decode_boundary_condition, 'child::cim:requirement/cim:requirement/cim:boundaryCondition'),
        ('requirements', True, decode_initial_condition, 'child::cim:requirement/cim:requirement/cim:initialCondition'),
        ('requirements', True, decode_lateral_boundary_condition, 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition'),
        ('requirements', True, decode_output_requirement, 'child::cim:requirement/cim:requirement/cim:outputRequirement'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint'),
        ('requirements_references', True, decode_doc_reference, 'child::cim:requirement/cim:reference'),
        ('description', False, 'str', 'child::cim:description'),
        ('frequency', False, 'str', 'child::cim:frequency'),
        ('type', False, 'str', '@type'),
        ('sources', True, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('sources', True, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('sources', True, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
    ]

    return set_attributes(typeset.activity.Conformance(), xml, nsmap, decodings)


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
        ('calendar', False, decode_real_calendar, 'child::cim:calendar/cim:realCalendar'),
        ('calendar', False, decode_perpetual_period, 'child::cim:calendar/cim:perpetualPeriod'),
        ('calendar', False, decode_daily_360, 'child::cim:calendar/cim:daily-360'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('date_range', False, decode_open_date_range, 'child::cim:dateRange/cim:openDateRange'),
        ('date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('simulation_id', False, 'str', 'child::cim:simulationID'),
        ('meta', False, decode_doc_meta_info, 'self::cim:simulationRun'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('spinup_date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('description', False, 'str', 'child::cim:description'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('supports_references', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('deployments', True, decode_deployment, 'child::cim:deployment'),
        ('control_simulation_reference', False, decode_doc_reference, 'child::cim:controlSimulation/cim:reference'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('projects', True, 'str', 'child::cim:project/@value'),
        ('model_reference', False, decode_doc_reference, 'child::cim:model/cim:reference'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('control_simulation', False, decode_simulation, 'child::cim:controlSimulation/cim:controlSimulation'),
        ('conformances', True, decode_physical_modification, 'child::cim:conformance/cim:physicalModification'),
        ('conformances', True, decode_conformance, 'child::cim:conformance/cim:conformance'),
        ('authors', False, 'str', 'child::cim:authorsList/cim:list'),
        ('model', False, decode_model_component, 'child::cim:model/cim:modelComponent'),
    ]

    return set_attributes(typeset.activity.SimulationRun(), xml, nsmap, decodings)


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
        ('calendar', False, decode_daily_360, 'child::cim:calendar/cim:daily-360'),
        ('calendar', False, decode_perpetual_period, 'child::cim:calendar/cim:perpetualPeriod'),
        ('calendar', False, decode_real_calendar, 'child::cim:calendar/cim:realCalendar'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('rationales', True, 'str', 'child::cim:rationale'),
        ('description', False, 'str', 'child::cim:description'),
        ('control_simulation', False, decode_simulation, 'child::cim:controlSimulation/cim:controlSimulation'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('simulation_id', False, 'str', 'child::cim:simulationID'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('authors', False, 'str', 'child::cim:authorsList/cim:list'),
        ('spinup_date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('deployments', True, decode_deployment, 'child::cim:deployment'),
        ('supports_references', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('control_simulation_reference', False, decode_doc_reference, 'child::cim:controlSimulation/cim:reference'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('funding_sources', True, 'str', 'child::cim:fundingSource'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('conformances', True, decode_physical_modification, 'child::cim:conformance/cim:physicalModification'),
        ('conformances', True, decode_conformance, 'child::cim:conformance/cim:conformance'),
        ('projects', True, 'str', 'child::cim:project/@value'),
    ]

    return set_attributes(typeset.activity.Simulation(), xml, nsmap, decodings)


