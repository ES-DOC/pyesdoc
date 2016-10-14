# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.decoder_for_data_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 2 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from decoder_xml_utils import set_attributes
from decoder_for_activity_package import *
from decoder_for_designing_package import *
from decoder_for_drs_package import *
from decoder_for_science_package import *
from decoder_for_shared_package import *
from decoder_for_time_package import *
import typeset



def decode_dataset(xml, nsmap):
    """Decodes an instance of the following type: dataset.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.data.Dataset

    """
    decodings = [
    ]

    return set_attributes(typeset.data.Dataset(), xml, nsmap, decodings)


def decode_downscaling(xml, nsmap):
    """Decodes an instance of the following type: downscaling.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.data.Downscaling

    """
    decodings = [
    ]

    return set_attributes(typeset.data.Downscaling(), xml, nsmap, decodings)


def decode_input_dataset(xml, nsmap):
    """Decodes an instance of the following type: input dataset.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.data.InputDataset

    """
    decodings = [
    ]

    return set_attributes(typeset.data.InputDataset(), xml, nsmap, decodings)


def decode_simulation(xml, nsmap):
    """Decodes an instance of the following type: simulation.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.data.Simulation

    """
    decodings = [
    ]

    return set_attributes(typeset.data.Simulation(), xml, nsmap, decodings)


def decode_variable_collection(xml, nsmap):
    """Decodes an instance of the following type: variable collection.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.data.VariableCollection

    """
    decodings = [
    ]

    return set_attributes(typeset.data.VariableCollection(), xml, nsmap, decodings)


