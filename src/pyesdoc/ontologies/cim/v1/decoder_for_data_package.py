# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.decoder_for_data_package.py

   :copyright: @2014 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2014-06-06 13:55:48.234213.

"""

# Module imports.
from decoder_xml_utils import set_attributes
from decoder_for_shared_package import *
import typeset



def decode_data_content(xml, nsmap):
    """Decodes an instance of the following type: data content.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataContent

    """
    decodings = [
        ('aggregation', False, 'str', 'child::cim:aggregation'),
        ('frequency', False, 'str', 'child::cim:frequency/@value'),
        ('topic', False, decode_data_topic, 'child::cim:topic'),
    ]

    return set_attributes(typeset.data.DataContent(), xml, nsmap, decodings)


def decode_data_distribution(xml, nsmap):
    """Decodes an instance of the following type: data distribution.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataDistribution

    """
    decodings = [
        ('access', False, 'str', '@distributionAccess'),
        ('format', False, 'str', 'child::cim:distributionFormat/@value'),
        ('responsible_party', False, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(typeset.data.DataDistribution(), xml, nsmap, decodings)


def decode_data_extent(xml, nsmap):
    """Decodes an instance of the following type: data extent.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataExtent

    """
    decodings = [
        ('geographical', False, decode_data_extent_geographical, 'child::gmd:geographicElement'),
        ('temporal', False, decode_data_extent_temporal, 'child::gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod'),
    ]

    return set_attributes(typeset.data.DataExtent(), xml, nsmap, decodings)


def decode_data_extent_geographical(xml, nsmap):
    """Decodes an instance of the following type: data extent geographical.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataExtentGeographical

    """
    decodings = [
        ('east', False, 'float', 'child::gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/gco:Decimal'),
        ('north', False, 'float', 'child::gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/gco:Decimal'),
        ('south', False, 'float', 'child::gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/gco:Decimal'),
        ('west', False, 'float', 'child::gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/gco:Decimal'),
    ]

    return set_attributes(typeset.data.DataExtentGeographical(), xml, nsmap, decodings)


def decode_data_extent_temporal(xml, nsmap):
    """Decodes an instance of the following type: data extent temporal.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataExtentTemporal

    """
    decodings = [
        ('begin', False, 'datetime.date', 'child::gml:beginPosition'),
        ('end', False, 'datetime.date', 'child::gml:endPosition'),
        ('time_interval', False, decode_data_extent_time_interval, 'child::gml:timeInterval'),
    ]

    return set_attributes(typeset.data.DataExtentTemporal(), xml, nsmap, decodings)


def decode_data_extent_time_interval(xml, nsmap):
    """Decodes an instance of the following type: data extent time interval.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataExtentTimeInterval

    """
    decodings = [
        ('factor', False, 'int', '@factor'),
        ('radix', False, 'int', '@radix'),
        ('unit', False, 'str', '@unit'),
    ]

    return set_attributes(typeset.data.DataExtentTimeInterval(), xml, nsmap, decodings)


def decode_data_hierarchy_level(xml, nsmap):
    """Decodes an instance of the following type: data hierarchy level.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataHierarchyLevel

    """
    decodings = [
        ('is_open', False, 'bool', 'child::cim:hierarchyLevelName/@open'),
        ('name', False, 'str', 'child::cim:hierarchyLevelName/@value'),
        ('value', False, 'str', 'child::cim:hierarchyLevelValue'),
    ]

    return set_attributes(typeset.data.DataHierarchyLevel(), xml, nsmap, decodings)


def decode_data_object(xml, nsmap):
    """Decodes an instance of the following type: data object.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataObject

    """
    decodings = [
        ('acronym', False, 'str', 'child::cim:acronym'),
        ('citations', True, decode_citation, '//cim:citation[not(cim:citation)]'),
        ('content', True, decode_data_content, 'child::cim:content'),
        ('data_status', False, 'str', 'self::cim:dataObject/@dataStatus'),
        ('description', False, 'str', 'child::cim:description'),
        ('distribution', False, decode_data_distribution, 'child::cim:distribution'),
        ('extent', False, decode_data_extent, 'child::cim:extent'),
        ('hierarchy_level', False, decode_data_hierarchy_level, 'self::cim:dataObject'),
        ('keyword', False, 'str', 'child::cim:keyword'),
        ('meta', False, decode_doc_meta_info, 'self::cim:dataObject'),
        ('properties', True, decode_data_property, 'child::cim:dataProperty/cim:dataProperty'),
        ('purpose', False, 'str', 'self::cim:dataObject/@purpose'),
        ('purpose', False, 'str', 'self::cim:dataObject/@purpose'),
        ('storage', True, decode_data_storage_ip, 'child::cim:storage/cim:ipStorage'),
    ]

    return set_attributes(typeset.data.DataObject(), xml, nsmap, decodings)


def decode_data_property(xml, nsmap):
    """Decodes an instance of the following type: data property.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataProperty

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('name', False, 'str', 'child::cim:name'),
        ('value', False, 'str', 'child::cim:value'),
    ]

    return set_attributes(typeset.data.DataProperty(), xml, nsmap, decodings)


def decode_data_restriction(xml, nsmap):
    """Decodes an instance of the following type: data restriction.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataRestriction

    """
    decodings = [
    ]

    return set_attributes(typeset.data.DataRestriction(), xml, nsmap, decodings)


def decode_data_storage(xml, nsmap):
    """Decodes an instance of the following type: data storage.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataStorage

    """
    decodings = [
    ]

    return set_attributes(typeset.data.DataStorage(), xml, nsmap, decodings)


def decode_data_storage_db(xml, nsmap):
    """Decodes an instance of the following type: data storage db.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataStorageDb

    """
    decodings = [
    ]

    return set_attributes(typeset.data.DataStorageDb(), xml, nsmap, decodings)


def decode_data_storage_file(xml, nsmap):
    """Decodes an instance of the following type: data storage file.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataStorageFile

    """
    decodings = [
    ]

    return set_attributes(typeset.data.DataStorageFile(), xml, nsmap, decodings)


def decode_data_storage_ip(xml, nsmap):
    """Decodes an instance of the following type: data storage ip.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataStorageIp

    """
    decodings = [
        ('fileName', False, 'str', 'child::cim:fileName'),
        ('format', False, 'str', 'child::cim:dataFormat/@value'),
    ]

    return set_attributes(typeset.data.DataStorageIp(), xml, nsmap, decodings)


def decode_data_topic(xml, nsmap):
    """Decodes an instance of the following type: data topic.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataTopic

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('name', False, 'str', 'child::cim:name'),
        ('unit', False, 'str', 'child::cim:unit/@value'),
    ]

    return set_attributes(typeset.data.DataTopic(), xml, nsmap, decodings)


