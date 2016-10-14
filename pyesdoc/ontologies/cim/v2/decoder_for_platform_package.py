# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.decoder_for_platform_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 2 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from decoder_xml_utils import set_attributes
from decoder_for_science_package import *
from decoder_for_shared_package import *
from decoder_for_software_package import *
from decoder_for_time_package import *
import typeset



def decode_component_performance(xml, nsmap):
    """Decodes an instance of the following type: component performance.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.platform.ComponentPerformance

    """
    decodings = [
    ]

    return set_attributes(typeset.platform.ComponentPerformance(), xml, nsmap, decodings)


def decode_compute_pool(xml, nsmap):
    """Decodes an instance of the following type: compute pool.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.platform.ComputePool

    """
    decodings = [
    ]

    return set_attributes(typeset.platform.ComputePool(), xml, nsmap, decodings)


def decode_machine(xml, nsmap):
    """Decodes an instance of the following type: machine.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.platform.Machine

    """
    decodings = [
    ]

    return set_attributes(typeset.platform.Machine(), xml, nsmap, decodings)


def decode_partition(xml, nsmap):
    """Decodes an instance of the following type: partition.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.platform.Partition

    """
    decodings = [
    ]

    return set_attributes(typeset.platform.Partition(), xml, nsmap, decodings)


def decode_performance(xml, nsmap):
    """Decodes an instance of the following type: performance.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.platform.Performance

    """
    decodings = [
    ]

    return set_attributes(typeset.platform.Performance(), xml, nsmap, decodings)


def decode_storage_pool(xml, nsmap):
    """Decodes an instance of the following type: storage pool.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.platform.StoragePool

    """
    decodings = [
    ]

    return set_attributes(typeset.platform.StoragePool(), xml, nsmap, decodings)


def decode_storage_volume(xml, nsmap):
    """Decodes an instance of the following type: storage volume.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.platform.StorageVolume

    """
    decodings = [
    ]

    return set_attributes(typeset.platform.StorageVolume(), xml, nsmap, decodings)


