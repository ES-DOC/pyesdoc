# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.decoder_for_science_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 2 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from decoder_xml_utils import set_attributes
from decoder_for_data_package import *
from decoder_for_shared_package import *
from decoder_for_software_package import *
import typeset



def decode_conservation_properties(xml, nsmap):
    """Decodes an instance of the following type: conservation properties.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.science.ConservationProperties

    """
    decodings = [
    ]

    return set_attributes(typeset.science.ConservationProperties(), xml, nsmap, decodings)


def decode_detail(xml, nsmap):
    """Decodes an instance of the following type: detail.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.science.Detail

    """
    decodings = [
    ]

    return set_attributes(typeset.science.Detail(), xml, nsmap, decodings)


def decode_discretisation(xml, nsmap):
    """Decodes an instance of the following type: discretisation.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.science.Discretisation

    """
    decodings = [
    ]

    return set_attributes(typeset.science.Discretisation(), xml, nsmap, decodings)


def decode_extent(xml, nsmap):
    """Decodes an instance of the following type: extent.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.science.Extent

    """
    decodings = [
    ]

    return set_attributes(typeset.science.Extent(), xml, nsmap, decodings)


def decode_grid(xml, nsmap):
    """Decodes an instance of the following type: grid.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.science.Grid

    """
    decodings = [
    ]

    return set_attributes(typeset.science.Grid(), xml, nsmap, decodings)


def decode_iso_extent(xml, nsmap):
    """Decodes an instance of the following type: iso extent.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.science.IsoExtent

    """
    decodings = [
    ]

    return set_attributes(typeset.science.IsoExtent(), xml, nsmap, decodings)


def decode_key_properties(xml, nsmap):
    """Decodes an instance of the following type: key properties.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.science.KeyProperties

    """
    decodings = [
    ]

    return set_attributes(typeset.science.KeyProperties(), xml, nsmap, decodings)


def decode_model(xml, nsmap):
    """Decodes an instance of the following type: model.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.science.Model

    """
    decodings = [
    ]

    return set_attributes(typeset.science.Model(), xml, nsmap, decodings)


def decode_process(xml, nsmap):
    """Decodes an instance of the following type: process.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.science.Process

    """
    decodings = [
    ]

    return set_attributes(typeset.science.Process(), xml, nsmap, decodings)


def decode_resolution(xml, nsmap):
    """Decodes an instance of the following type: resolution.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.science.Resolution

    """
    decodings = [
    ]

    return set_attributes(typeset.science.Resolution(), xml, nsmap, decodings)


def decode_science_context(xml, nsmap):
    """Decodes an instance of the following type: science context.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.science.ScienceContext

    """
    decodings = [
    ]

    return set_attributes(typeset.science.ScienceContext(), xml, nsmap, decodings)


def decode_scientific_realm(xml, nsmap):
    """Decodes an instance of the following type: scientific realm.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.science.ScientificRealm

    """
    decodings = [
    ]

    return set_attributes(typeset.science.ScientificRealm(), xml, nsmap, decodings)


def decode_sub_process(xml, nsmap):
    """Decodes an instance of the following type: sub process.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.science.SubProcess

    """
    decodings = [
    ]

    return set_attributes(typeset.science.SubProcess(), xml, nsmap, decodings)


def decode_tuning(xml, nsmap):
    """Decodes an instance of the following type: tuning.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.science.Tuning

    """
    decodings = [
    ]

    return set_attributes(typeset.science.Tuning(), xml, nsmap, decodings)


