# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.decoder_for_activity_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 2 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from decoder_xml_utils import set_attributes
from decoder_for_data_package import *
from decoder_for_designing_package import *
from decoder_for_platform_package import *
from decoder_for_science_package import *
from decoder_for_shared_package import *
from decoder_for_time_package import *
import typeset



def decode_activity(xml, nsmap):
    """Decodes an instance of the following type: activity.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.activity.Activity

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.Activity(), xml, nsmap, decodings)


def decode_axis_member(xml, nsmap):
    """Decodes an instance of the following type: axis member.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.activity.AxisMember

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.AxisMember(), xml, nsmap, decodings)


def decode_conformance(xml, nsmap):
    """Decodes an instance of the following type: conformance.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.activity.Conformance

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.Conformance(), xml, nsmap, decodings)


def decode_ensemble(xml, nsmap):
    """Decodes an instance of the following type: ensemble.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.activity.Ensemble

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.Ensemble(), xml, nsmap, decodings)


def decode_ensemble_axis(xml, nsmap):
    """Decodes an instance of the following type: ensemble axis.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.activity.EnsembleAxis

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.EnsembleAxis(), xml, nsmap, decodings)


def decode_ensemble_member(xml, nsmap):
    """Decodes an instance of the following type: ensemble member.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.activity.EnsembleMember

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.EnsembleMember(), xml, nsmap, decodings)


def decode_parent_simulation(xml, nsmap):
    """Decodes an instance of the following type: parent simulation.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.activity.ParentSimulation

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.ParentSimulation(), xml, nsmap, decodings)


def decode_uber_ensemble(xml, nsmap):
    """Decodes an instance of the following type: uber ensemble.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.activity.UberEnsemble

    """
    decodings = [
    ]

    return set_attributes(typeset.activity.UberEnsemble(), xml, nsmap, decodings)


