# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.decoder_for_designing_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 2 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from decoder_xml_utils import set_attributes
from decoder_for_data_package import *
from decoder_for_platform_package import *
from decoder_for_science_package import *
from decoder_for_shared_package import *
from decoder_for_time_package import *
import typeset



def decode_axis_member(xml, nsmap):
    """Decodes an instance of the following type: axis member.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.designing.AxisMember

    """
    decodings = [
    ]

    return set_attributes(typeset.designing.AxisMember(), xml, nsmap, decodings)


def decode_domain_requirements(xml, nsmap):
    """Decodes an instance of the following type: domain requirements.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.designing.DomainRequirements

    """
    decodings = [
    ]

    return set_attributes(typeset.designing.DomainRequirements(), xml, nsmap, decodings)


def decode_ensemble_requirement(xml, nsmap):
    """Decodes an instance of the following type: ensemble requirement.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.designing.EnsembleRequirement

    """
    decodings = [
    ]

    return set_attributes(typeset.designing.EnsembleRequirement(), xml, nsmap, decodings)


def decode_forcing_constraint(xml, nsmap):
    """Decodes an instance of the following type: forcing constraint.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.designing.ForcingConstraint

    """
    decodings = [
    ]

    return set_attributes(typeset.designing.ForcingConstraint(), xml, nsmap, decodings)


def decode_initialisation_requirement(xml, nsmap):
    """Decodes an instance of the following type: initialisation requirement.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.designing.InitialisationRequirement

    """
    decodings = [
    ]

    return set_attributes(typeset.designing.InitialisationRequirement(), xml, nsmap, decodings)


def decode_multi_ensemble(xml, nsmap):
    """Decodes an instance of the following type: multi ensemble.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.designing.MultiEnsemble

    """
    decodings = [
    ]

    return set_attributes(typeset.designing.MultiEnsemble(), xml, nsmap, decodings)


def decode_numerical_experiment(xml, nsmap):
    """Decodes an instance of the following type: numerical experiment.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.designing.NumericalExperiment

    """
    decodings = [
    ]

    return set_attributes(typeset.designing.NumericalExperiment(), xml, nsmap, decodings)


def decode_numerical_requirement(xml, nsmap):
    """Decodes an instance of the following type: numerical requirement.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.designing.NumericalRequirement

    """
    decodings = [
    ]

    return set_attributes(typeset.designing.NumericalRequirement(), xml, nsmap, decodings)


def decode_output_requirement(xml, nsmap):
    """Decodes an instance of the following type: output requirement.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.designing.OutputRequirement

    """
    decodings = [
    ]

    return set_attributes(typeset.designing.OutputRequirement(), xml, nsmap, decodings)


def decode_project(xml, nsmap):
    """Decodes an instance of the following type: project.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.designing.Project

    """
    decodings = [
    ]

    return set_attributes(typeset.designing.Project(), xml, nsmap, decodings)


def decode_simulation_plan(xml, nsmap):
    """Decodes an instance of the following type: simulation plan.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.designing.SimulationPlan

    """
    decodings = [
    ]

    return set_attributes(typeset.designing.SimulationPlan(), xml, nsmap, decodings)


def decode_start_date_ensemble(xml, nsmap):
    """Decodes an instance of the following type: start date ensemble.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.designing.StartDateEnsemble

    """
    decodings = [
    ]

    return set_attributes(typeset.designing.StartDateEnsemble(), xml, nsmap, decodings)


def decode_temporal_constraint(xml, nsmap):
    """Decodes an instance of the following type: temporal constraint.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.designing.TemporalConstraint

    """
    decodings = [
    ]

    return set_attributes(typeset.designing.TemporalConstraint(), xml, nsmap, decodings)


