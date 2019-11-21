"""
.. module:: cim.v1.decoder_for_activity_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
from decoder_xml_utils import set_attributes
from decoder_for_data_package import *
from decoder_for_shared_package import *
from decoder_for_software_package import *
import typeset



def decode_activity(xml, nsmap):
    """Decodes an instance of the following type: activity.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.Activity

    """
    decodings = [
        ('funding_sources', True, 'unicode', 'child::cim:fundingSource'),
        ('projects', True, 'unicode', 'child::cim:project/@value'),
        ('rationales', True, 'unicode', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(typeset.activity.Activity(), xml, nsmap, decodings)


def decode_boundary_condition(xml, nsmap):
    """Decodes an instance of the following type: boundary condition.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.BoundaryCondition

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('id', False, 'unicode', 'child::cim:id'),
        ('name', False, 'unicode', 'child::cim:name'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
    ]

    return set_attributes(typeset.activity.BoundaryCondition(), xml, nsmap, decodings)


def decode_conformance(xml, nsmap):
    """Decodes an instance of the following type: conformance.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.Conformance

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('frequency', False, 'unicode', 'child::cim:frequency'),
        ('is_conformant', False, 'bool', '@conformant'),
        ('requirements', True, decode_boundary_condition, 'child::cim:requirement/cim:requirement/cim:boundaryCondition'),
        ('requirements', True, decode_doc_reference, 'child::cim:requirement/cim:reference'),
        ('requirements', True, decode_initial_condition, 'child::cim:requirement/cim:requirement/cim:initialCondition'),
        ('requirements', True, decode_lateral_boundary_condition, 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition'),
        ('requirements', True, decode_output_requirement, 'child::cim:requirement/cim:requirement/cim:outputRequirement'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint'),
        ('sources', True, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('sources', True, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('sources', True, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('sources', True, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('sources', True, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('type', False, 'unicode', '@type'),
    ]

    return set_attributes(typeset.activity.Conformance(), xml, nsmap, decodings)


def decode_downscaling_simulation(xml, nsmap):
    """Decodes an instance of the following type: downscaling simulation.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.DownscalingSimulation

    """
    decodings = [
        ('calendar', False, decode_daily_360, 'child::cim:calendar/cim:daily-360'),
        ('calendar', False, decode_perpetual_period, 'child::cim:calendar/cim:perpetualPeriod'),
        ('calendar', False, decode_real_calendar, 'child::cim:calendar/cim:realCalendar'),
        ('description', False, 'unicode', 'child::cim:description'),
        ('downscaled_from', False, decode_component_property, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:componentProperty'),
        ('downscaled_from', False, decode_data_content, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:dataContent'),
        ('downscaled_from', False, decode_data_object, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:dataObject'),
        ('downscaled_from', False, decode_doc_reference, 'child::cim:downscaledFrom/cim:reference'),
        ('downscaled_from', False, decode_model_component, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:softwareComponent'),
        ('downscaled_from', False, decode_processor_component, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:softwareComponent'),
        ('downscaled_from', False, decode_statistical_model_component, 'child::cim:downscaledFrom/cim:downscaledFrom/cim:softwareComponent'),
        ('downscaling_id', False, 'unicode', 'child::cim:downscalingID'),
        ('downscaling_type', False, 'unicode', 'self::cim:downscalingSimulation/@downscalingType'),
        ('funding_sources', True, 'unicode', 'child::cim:fundingSource'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('long_name', False, 'unicode', 'child::cim:longName'),
        ('meta', False, decode_doc_meta_info, 'self::cim:downscalingSimulation'),
        ('outputs', True, decode_data_object, 'child::cim:output/cim:dataObject'),
        ('outputs', True, decode_doc_reference, 'child::cim:output/cim:reference'),
        ('projects', True, 'unicode', 'child::cim:project/@value'),
        ('rationales', True, 'unicode', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'unicode', 'child::cim:shortName'),
        ('supports', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
    ]

    return set_attributes(typeset.activity.DownscalingSimulation(), xml, nsmap, decodings)


def decode_ensemble(xml, nsmap):
    """Decodes an instance of the following type: ensemble.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.Ensemble

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('funding_sources', True, 'unicode', 'child::cim:fundingSource'),
        ('long_name', False, 'unicode', 'child::cim:longName'),
        ('members', True, decode_ensemble_member, 'child::cim:ensembleMember'),
        ('meta', False, decode_doc_meta_info, 'self::cim:ensemble'),
        ('outputs', True, decode_component_property, 'child::cim:output/cim:output/cim:componentProperty'),
        ('outputs', True, decode_data_content, 'child::cim:output/cim:output/cim:dataContent'),
        ('outputs', True, decode_data_object, 'child::cim:output/cim:output/cim:dataObject'),
        ('outputs', True, decode_doc_reference, 'child::cim:output/cim:reference'),
        ('outputs', True, decode_model_component, 'child::cim:output/cim:output/cim:softwareComponent'),
        ('outputs', True, decode_processor_component, 'child::cim:output/cim:output/cim:softwareComponent'),
        ('outputs', True, decode_statistical_model_component, 'child::cim:output/cim:output/cim:softwareComponent'),
        ('projects', True, 'unicode', 'child::cim:project/@value'),
        ('rationales', True, 'unicode', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'unicode', 'child::cim:shortName'),
        ('supports', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
        ('types', True, 'unicode', 'child::cim:ensembleType/@value'),
    ]

    return set_attributes(typeset.activity.Ensemble(), xml, nsmap, decodings)


def decode_ensemble_member(xml, nsmap):
    """Decodes an instance of the following type: ensemble member.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.EnsembleMember

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('ensemble', False, decode_doc_reference, 'child::cim:ensemble/cim:reference'),
        ('ensemble', False, decode_ensemble, 'child::cim:ensemble/cim:ensemble'),
        ('ensemble_ids', True, decode_standard_name, 'child::cim:ensembleMemberID'),
        ('funding_sources', True, 'unicode', 'child::cim:fundingSource'),
        ('long_name', False, 'unicode', 'child::cim:longName'),
        ('projects', True, 'unicode', 'child::cim:project/@value'),
        ('rationales', True, 'unicode', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'unicode', 'child::cim:shortName'),
        ('simulation', False, decode_doc_reference, 'child::cim:simulation/cim:reference'),
        ('simulation', False, decode_simulation, 'child::cim:ensemble/cim:simulation'),
        ('supports', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
    ]

    return set_attributes(typeset.activity.EnsembleMember(), xml, nsmap, decodings)


def decode_experiment(xml, nsmap):
    """Decodes an instance of the following type: experiment.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.Experiment

    """
    decodings = [
        ('funding_sources', True, 'unicode', 'child::cim:fundingSource'),
        ('projects', True, 'unicode', 'child::cim:project/@value'),
        ('rationales', True, 'unicode', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(typeset.activity.Experiment(), xml, nsmap, decodings)


def decode_experiment_relationship(xml, nsmap):
    """Decodes an instance of the following type: experiment relationship.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.ExperimentRelationship

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.ExperimentRelationship(), xml, nsmap, decodings)


def decode_experiment_relationship_target(xml, nsmap):
    """Decodes an instance of the following type: experiment relationship target.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.ExperimentRelationshipTarget

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.ExperimentRelationshipTarget(), xml, nsmap, decodings)


def decode_initial_condition(xml, nsmap):
    """Decodes an instance of the following type: initial condition.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.InitialCondition

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('id', False, 'unicode', 'child::cim:id'),
        ('name', False, 'unicode', 'child::cim:name'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
    ]

    return set_attributes(typeset.activity.InitialCondition(), xml, nsmap, decodings)


def decode_lateral_boundary_condition(xml, nsmap):
    """Decodes an instance of the following type: lateral boundary condition.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.LateralBoundaryCondition

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('id', False, 'unicode', 'child::cim:id'),
        ('name', False, 'unicode', 'child::cim:name'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
    ]

    return set_attributes(typeset.activity.LateralBoundaryCondition(), xml, nsmap, decodings)


def decode_measurement_campaign(xml, nsmap):
    """Decodes an instance of the following type: measurement campaign.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.MeasurementCampaign

    """
    decodings = [
        ('funding_sources', True, 'unicode', 'child::cim:fundingSource'),
        ('projects', True, 'unicode', 'child::cim:project/@value'),
        ('rationales', True, 'unicode', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(typeset.activity.MeasurementCampaign(), xml, nsmap, decodings)


def decode_numerical_activity(xml, nsmap):
    """Decodes an instance of the following type: numerical activity.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.NumericalActivity

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('funding_sources', True, 'unicode', 'child::cim:fundingSource'),
        ('long_name', False, 'unicode', 'child::cim:longName'),
        ('projects', True, 'unicode', 'child::cim:project/@value'),
        ('rationales', True, 'unicode', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'unicode', 'child::cim:shortName'),
        ('supports', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
    ]

    return set_attributes(typeset.activity.NumericalActivity(), xml, nsmap, decodings)


def decode_numerical_experiment(xml, nsmap):
    """Decodes an instance of the following type: numerical experiment.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.NumericalExperiment

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('experiment_id', False, 'unicode', 'child::cim:experimentID'),
        ('funding_sources', True, 'unicode', 'child::cim:fundingSource'),
        ('long_name', False, 'unicode', 'child::cim:longName'),
        ('meta', False, decode_doc_meta_info, 'self::cim:numericalExperiment'),
        ('projects', True, 'unicode', 'child::cim:project/@value'),
        ('rationales', True, 'unicode', 'child::cim:rationale'),
        ('requirements', True, decode_boundary_condition, 'child::cim:numericalRequirement/cim:boundaryCondition'),
        ('requirements', True, decode_boundary_condition, 'child::cim:numericalRequirement[@xsi:type="BoundaryCondition"]'),
        ('requirements', True, decode_initial_condition, 'child::cim:numericalRequirement/cim:initialCondition'),
        ('requirements', True, decode_initial_condition, 'child::cim:numericalRequirement[@xsi:type="InitialCondition"]'),
        ('requirements', True, decode_lateral_boundary_condition, 'child::cim:numericalRequirement/cim:lateralBoundaryCondition'),
        ('requirements', True, decode_lateral_boundary_condition, 'child::cim:numericalRequirement[@xsi:type="LateralBoundaryCondition"]'),
        ('requirements', True, decode_output_requirement, 'child::cim:numericalRequirement/cim:outputRequirement'),
        ('requirements', True, decode_output_requirement, 'child::cim:numericalRequirement[@xsi:type="OutputRequirement"]'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:numericalRequirement/cim:spatioTemporalConstraint'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:numericalRequirement[@xsi:type="SpatioTemporalConstraint"]'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'unicode', 'child::cim:shortName'),
    ]

    return set_attributes(typeset.activity.NumericalExperiment(), xml, nsmap, decodings)


def decode_numerical_requirement(xml, nsmap):
    """Decodes an instance of the following type: numerical requirement.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.NumericalRequirement

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('id', False, 'unicode', 'child::cim:id'),
        ('name', False, 'unicode', 'child::cim:name'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
    ]

    return set_attributes(typeset.activity.NumericalRequirement(), xml, nsmap, decodings)


def decode_numerical_requirement_option(xml, nsmap):
    """Decodes an instance of the following type: numerical requirement option.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.NumericalRequirementOption

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('description', False, 'unicode', 'child::cim:requirement/cim:requirement/cim:boundaryCondition/cim:description'),
        ('description', False, 'unicode', 'child::cim:requirement/cim:requirement/cim:initialCondition/cim:description'),
        ('description', False, 'unicode', 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition/cim:description'),
        ('description', False, 'unicode', 'child::cim:requirement/cim:requirement/cim:outputRequirement/cim:description'),
        ('description', False, 'unicode', 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint/cim:description'),
        ('id', False, 'unicode', 'child::cim:id'),
        ('id', False, 'unicode', 'child::cim:requirement/cim:requirement/cim:boundaryCondition/cim:id'),
        ('id', False, 'unicode', 'child::cim:requirement/cim:requirement/cim:initialCondition/cim:id'),
        ('id', False, 'unicode', 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition/cim:id'),
        ('id', False, 'unicode', 'child::cim:requirement/cim:requirement/cim:outputRequirement/cim:id'),
        ('id', False, 'unicode', 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint/cim:id'),
        ('name', False, 'unicode', 'child::cim:name'),
        ('name', False, 'unicode', 'child::cim:requirement/cim:requirement/cim:boundaryCondition/cim:name'),
        ('name', False, 'unicode', 'child::cim:requirement/cim:requirement/cim:initialCondition/cim:name'),
        ('name', False, 'unicode', 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition/cim:name'),
        ('name', False, 'unicode', 'child::cim:requirement/cim:requirement/cim:outputRequirement/cim:name'),
        ('name', False, 'unicode', 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint/cim:name'),
        ('relationship', False, 'unicode', 'self::cim:requirementOption/@optionRelationship'),
    ]

    return set_attributes(typeset.activity.NumericalRequirementOption(), xml, nsmap, decodings)


def decode_output_requirement(xml, nsmap):
    """Decodes an instance of the following type: output requirement.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.OutputRequirement

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('id', False, 'unicode', 'child::cim:id'),
        ('name', False, 'unicode', 'child::cim:name'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
    ]

    return set_attributes(typeset.activity.OutputRequirement(), xml, nsmap, decodings)


def decode_physical_modification(xml, nsmap):
    """Decodes an instance of the following type: physical modification.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.PhysicalModification

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('frequency', False, 'unicode', 'child::cim:frequency'),
        ('is_conformant', False, 'bool', '@conformant'),
        ('requirements', True, decode_boundary_condition, 'child::cim:requirement/cim:requirement/cim:boundaryCondition'),
        ('requirements', True, decode_doc_reference, 'child::cim:requirement/cim:reference'),
        ('requirements', True, decode_initial_condition, 'child::cim:requirement/cim:requirement/cim:initialCondition'),
        ('requirements', True, decode_lateral_boundary_condition, 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition'),
        ('requirements', True, decode_output_requirement, 'child::cim:requirement/cim:requirement/cim:outputRequirement'),
        ('requirements', True, decode_spatio_temporal_constraint, 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint'),
        ('sources', True, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('sources', True, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('sources', True, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('sources', True, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('sources', True, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('sources', True, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('type', False, 'unicode', '@type'),
    ]

    return set_attributes(typeset.activity.PhysicalModification(), xml, nsmap, decodings)


def decode_simulation(xml, nsmap):
    """Decodes an instance of the following type: simulation.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.Simulation

    """
    decodings = [
        ('authors', False, 'unicode', 'child::cim:authorsList/cim:list'),
        ('calendar', False, decode_daily_360, 'child::cim:calendar/cim:daily-360'),
        ('calendar', False, decode_perpetual_period, 'child::cim:calendar/cim:perpetualPeriod'),
        ('calendar', False, decode_real_calendar, 'child::cim:calendar/cim:realCalendar'),
        ('conformances', True, decode_conformance, 'child::cim:conformance/cim:conformance'),
        ('conformances', True, decode_physical_modification, 'child::cim:conformance/cim:physicalModification'),
        ('control_simulation', False, decode_doc_reference, 'child::cim:controlSimulation/cim:reference'),
        ('control_simulation', False, decode_simulation, 'child::cim:controlSimulation/cim:controlSimulation'),
        ('deployments', True, decode_deployment, 'child::cim:deployment'),
        ('description', False, 'unicode', 'child::cim:description'),
        ('funding_sources', True, 'unicode', 'child::cim:fundingSource'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('long_name', False, 'unicode', 'child::cim:longName'),
        ('projects', True, 'unicode', 'child::cim:project/@value'),
        ('rationales', True, 'unicode', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'unicode', 'child::cim:shortName'),
        ('simulation_id', False, 'unicode', 'child::cim:simulationID'),
        ('spinup_date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('supports', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
    ]

    return set_attributes(typeset.activity.Simulation(), xml, nsmap, decodings)


def decode_simulation_composite(xml, nsmap):
    """Decodes an instance of the following type: simulation composite.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.SimulationComposite

    """
    decodings = [
        ('authors', False, 'unicode', 'child::cim:authorsList/cim:list'),
        ('calendar', False, decode_daily_360, 'child::cim:calendar/cim:daily-360'),
        ('calendar', False, decode_perpetual_period, 'child::cim:calendar/cim:perpetualPeriod'),
        ('calendar', False, decode_real_calendar, 'child::cim:calendar/cim:realCalendar'),
        ('child', True, decode_simulation_composite, 'child::cim:child'),
        ('child', True, decode_simulation_run, 'child::cim:child'),
        ('conformances', True, decode_conformance, 'child::cim:conformance/cim:conformance'),
        ('conformances', True, decode_physical_modification, 'child::cim:conformance/cim:physicalModification'),
        ('control_simulation', False, decode_doc_reference, 'child::cim:controlSimulation/cim:reference'),
        ('control_simulation', False, decode_simulation, 'child::cim:controlSimulation/cim:controlSimulation'),
        ('date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('date_range', False, decode_open_date_range, 'child::cim:dateRange/cim:openDateRange'),
        ('deployments', True, decode_deployment, 'child::cim:deployment'),
        ('description', False, 'unicode', 'child::cim:description'),
        ('funding_sources', True, 'unicode', 'child::cim:fundingSource'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('long_name', False, 'unicode', 'child::cim:longName'),
        ('meta', False, decode_doc_meta_info, 'self::cim:simulationRun'),
        ('projects', True, 'unicode', 'child::cim:project/@value'),
        ('rank', False, 'int', 'child::cim:rank'),
        ('rationales', True, 'unicode', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'unicode', 'child::cim:shortName'),
        ('simulation_id', False, 'unicode', 'child::cim:simulationID'),
        ('spinup_date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('supports', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
    ]

    return set_attributes(typeset.activity.SimulationComposite(), xml, nsmap, decodings)


def decode_simulation_relationship(xml, nsmap):
    """Decodes an instance of the following type: simulation relationship.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.SimulationRelationship

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.SimulationRelationship(), xml, nsmap, decodings)


def decode_simulation_relationship_target(xml, nsmap):
    """Decodes an instance of the following type: simulation relationship target.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.SimulationRelationshipTarget

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.SimulationRelationshipTarget(), xml, nsmap, decodings)


def decode_simulation_run(xml, nsmap):
    """Decodes an instance of the following type: simulation run.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.SimulationRun

    """
    decodings = [
        ('authors', False, 'unicode', 'child::cim:authorsList/cim:list'),
        ('calendar', False, decode_daily_360, 'child::cim:calendar/cim:daily-360'),
        ('calendar', False, decode_perpetual_period, 'child::cim:calendar/cim:perpetualPeriod'),
        ('calendar', False, decode_real_calendar, 'child::cim:calendar/cim:realCalendar'),
        ('conformances', True, decode_conformance, 'child::cim:conformance/cim:conformance'),
        ('conformances', True, decode_physical_modification, 'child::cim:conformance/cim:physicalModification'),
        ('control_simulation', False, decode_doc_reference, 'child::cim:controlSimulation/cim:reference'),
        ('control_simulation', False, decode_simulation, 'child::cim:controlSimulation/cim:controlSimulation'),
        ('date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('date_range', False, decode_open_date_range, 'child::cim:dateRange/cim:openDateRange'),
        ('deployments', True, decode_deployment, 'child::cim:deployment'),
        ('description', False, 'unicode', 'child::cim:description'),
        ('funding_sources', True, 'unicode', 'child::cim:fundingSource'),
        ('inputs', True, decode_coupling, 'child::cim:input'),
        ('long_name', False, 'unicode', 'child::cim:longName'),
        ('meta', False, decode_doc_meta_info, 'self::cim:simulationRun'),
        ('model', False, decode_doc_reference, 'child::cim:model/cim:reference'),
        ('model', False, decode_model_component, 'child::cim:model/cim:modelComponent'),
        ('projects', True, 'unicode', 'child::cim:project/@value'),
        ('rationales', True, 'unicode', 'child::cim:rationale'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'unicode', 'child::cim:shortName'),
        ('simulation_id', False, 'unicode', 'child::cim:simulationID'),
        ('spinup_date_range', False, decode_closed_date_range, 'child::cim:dateRange/cim:closedDateRange'),
        ('supports', True, decode_doc_reference, 'child::cim:supports/cim:reference'),
        ('supports', True, decode_experiment, 'child::cim:supports/cim:experiment'),
    ]

    return set_attributes(typeset.activity.SimulationRun(), xml, nsmap, decodings)


def decode_spatio_temporal_constraint(xml, nsmap):
    """Decodes an instance of the following type: spatio temporal constraint.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.activity.SpatioTemporalConstraint

    """
    decodings = [
        ('date_range', False, decode_closed_date_range, 'child::cim:requiredDuration/cim:closedDateRange'),
        ('date_range', False, decode_open_date_range, 'child::cim:requiredDuration/cim:openDateRange'),
        ('description', False, 'unicode', 'child::cim:description'),
        ('id', False, 'unicode', 'child::cim:id'),
        ('name', False, 'unicode', 'child::cim:name'),
        ('options', True, decode_numerical_requirement_option, 'child::cim:requirementOption'),
        ('source', False, decode_component_property, 'child::cim:source/cim:source/cim:componentProperty'),
        ('source', False, decode_data_content, 'child::cim:source/cim:source/cim:dataContent'),
        ('source', False, decode_data_object, 'child::cim:source/cim:source/cim:dataObject'),
        ('source', False, decode_doc_reference, 'child::cim:source/cim:reference'),
        ('source', False, decode_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_processor_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('source', False, decode_statistical_model_component, 'child::cim:source/cim:source/cim:softwareComponent'),
        ('spatial_resolution', False, 'unicode', 'child::cim:spatialResolution'),
    ]

    return set_attributes(typeset.activity.SpatioTemporalConstraint(), xml, nsmap, decodings)


