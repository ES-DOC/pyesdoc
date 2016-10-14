# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.decoder_for_drs_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 2 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from decoder_xml_utils import set_attributes
from decoder_for_designing_package import *
import typeset



def decode_drs_atomic_dataset(xml, nsmap):
    """Decodes an instance of the following type: drs atomic dataset.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.drs.DrsAtomicDataset

    """
    decodings = [
    ]

    return set_attributes(typeset.drs.DrsAtomicDataset(), xml, nsmap, decodings)


def decode_drs_ensemble_identifier(xml, nsmap):
    """Decodes an instance of the following type: drs ensemble identifier.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.drs.DrsEnsembleIdentifier

    """
    decodings = [
    ]

    return set_attributes(typeset.drs.DrsEnsembleIdentifier(), xml, nsmap, decodings)


def decode_drs_experiment(xml, nsmap):
    """Decodes an instance of the following type: drs experiment.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.drs.DrsExperiment

    """
    decodings = [
    ]

    return set_attributes(typeset.drs.DrsExperiment(), xml, nsmap, decodings)


def decode_drs_geographical_indicator(xml, nsmap):
    """Decodes an instance of the following type: drs geographical indicator.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.drs.DrsGeographicalIndicator

    """
    decodings = [
    ]

    return set_attributes(typeset.drs.DrsGeographicalIndicator(), xml, nsmap, decodings)


def decode_drs_publication_dataset(xml, nsmap):
    """Decodes an instance of the following type: drs publication dataset.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.drs.DrsPublicationDataset

    """
    decodings = [
    ]

    return set_attributes(typeset.drs.DrsPublicationDataset(), xml, nsmap, decodings)


def decode_drs_simulation_identifier(xml, nsmap):
    """Decodes an instance of the following type: drs simulation identifier.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.drs.DrsSimulationIdentifier

    """
    decodings = [
    ]

    return set_attributes(typeset.drs.DrsSimulationIdentifier(), xml, nsmap, decodings)


def decode_drs_temporal_identifier(xml, nsmap):
    """Decodes an instance of the following type: drs temporal identifier.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.drs.DrsTemporalIdentifier

    """
    decodings = [
    ]

    return set_attributes(typeset.drs.DrsTemporalIdentifier(), xml, nsmap, decodings)


