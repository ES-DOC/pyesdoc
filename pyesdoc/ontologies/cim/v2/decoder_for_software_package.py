# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.decoder_for_software_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 2 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from decoder_xml_utils import set_attributes
from decoder_for_shared_package import *
import typeset



def decode_component_base(xml, nsmap):
    """Decodes an instance of the following type: component base.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.software.ComponentBase

    """
    decodings = [
    ]

    return set_attributes(typeset.software.ComponentBase(), xml, nsmap, decodings)


def decode_composition(xml, nsmap):
    """Decodes an instance of the following type: composition.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.software.Composition

    """
    decodings = [
    ]

    return set_attributes(typeset.software.Composition(), xml, nsmap, decodings)


def decode_development_path(xml, nsmap):
    """Decodes an instance of the following type: development path.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.software.DevelopmentPath

    """
    decodings = [
    ]

    return set_attributes(typeset.software.DevelopmentPath(), xml, nsmap, decodings)


def decode_entry_point(xml, nsmap):
    """Decodes an instance of the following type: entry point.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.software.EntryPoint

    """
    decodings = [
    ]

    return set_attributes(typeset.software.EntryPoint(), xml, nsmap, decodings)


def decode_gridspec(xml, nsmap):
    """Decodes an instance of the following type: gridspec.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.software.Gridspec

    """
    decodings = [
    ]

    return set_attributes(typeset.software.Gridspec(), xml, nsmap, decodings)


def decode_software_component(xml, nsmap):
    """Decodes an instance of the following type: software component.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.software.SoftwareComponent

    """
    decodings = [
    ]

    return set_attributes(typeset.software.SoftwareComponent(), xml, nsmap, decodings)


def decode_variable(xml, nsmap):
    """Decodes an instance of the following type: variable.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.software.Variable

    """
    decodings = [
    ]

    return set_attributes(typeset.software.Variable(), xml, nsmap, decodings)


