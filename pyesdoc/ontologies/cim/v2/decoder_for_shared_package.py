# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.decoder_for_shared_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 2 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from decoder_xml_utils import set_attributes
from decoder_for_time_package import *
import typeset



def decode_cimtext(xml, nsmap):
    """Decodes an instance of the following type: cimtext.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.shared.Cimtext

    """
    decodings = [
    ]

    return set_attributes(typeset.shared.Cimtext(), xml, nsmap, decodings)


def decode_citation(xml, nsmap):
    """Decodes an instance of the following type: citation.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.shared.Citation

    """
    decodings = [
    ]

    return set_attributes(typeset.shared.Citation(), xml, nsmap, decodings)


def decode_doc_meta_info(xml, nsmap):
    """Decodes an instance of the following type: doc meta info.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.shared.DocMetaInfo

    """
    decodings = [
        ('author', False, decode_party, 'child::cim:documentAuthor'),
        ('create_date', False, 'datetime.datetime', 'child::cim:documentCreationDate'),
        ('external_ids', True, 'unicode', 'child::cim:externalID'),
        ('id', False, 'unicode', 'child::cim:documentID'),
        ('update_date', False, 'datetime.datetime', 'child::cim:documentCreationDate'),
        ('version', False, 'int', 'child::cim:documentVersion'),
        ('version', False, 'int', 'self::cim:numericalExperiment/@documentVersion'),
    ]

    return set_attributes(typeset.shared.DocMetaInfo(), xml, nsmap, decodings)


def decode_doc_reference(xml, nsmap):
    """Decodes an instance of the following type: doc reference.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.shared.DocReference

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('external_id', False, 'unicode', 'child::cim:externalID'),
        ('id', False, 'unicode', 'child::cim:id'),
        ('name', False, 'unicode', 'child::cim:name'),
        ('type', False, 'unicode', 'child::cim:type'),
        ('version', False, 'int', 'child::cim:version'),
    ]

    return set_attributes(typeset.shared.DocReference(), xml, nsmap, decodings)


def decode_extra_attribute(xml, nsmap):
    """Decodes an instance of the following type: extra attribute.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.shared.ExtraAttribute

    """
    decodings = [
    ]

    return set_attributes(typeset.shared.ExtraAttribute(), xml, nsmap, decodings)


def decode_online_resource(xml, nsmap):
    """Decodes an instance of the following type: online resource.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.shared.OnlineResource

    """
    decodings = [
    ]

    return set_attributes(typeset.shared.OnlineResource(), xml, nsmap, decodings)


def decode_party(xml, nsmap):
    """Decodes an instance of the following type: party.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.shared.Party

    """
    decodings = [
    ]

    return set_attributes(typeset.shared.Party(), xml, nsmap, decodings)


def decode_quality_review(xml, nsmap):
    """Decodes an instance of the following type: quality review.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.shared.QualityReview

    """
    decodings = [
    ]

    return set_attributes(typeset.shared.QualityReview(), xml, nsmap, decodings)


def decode_responsibility(xml, nsmap):
    """Decodes an instance of the following type: responsibility.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.shared.Responsibility

    """
    decodings = [
    ]

    return set_attributes(typeset.shared.Responsibility(), xml, nsmap, decodings)


