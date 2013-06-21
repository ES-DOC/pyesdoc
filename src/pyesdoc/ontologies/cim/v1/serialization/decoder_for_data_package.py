"""
.. module:: cim.v1.decoding.decoder_for_data_package.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-21 14:34:23.212721.

"""

# Module imports.
from lxml import etree as et

from pyesdoc.serialization.decoder_xml_utils import *
from pyesdoc.ontologies.cim.v1.serialization.decoder_for_shared_package import *
from pyesdoc.ontologies.cim.v1.types.data import *




def decode_data_content(xml, nsmap):
    """Decodes an instance of the following type: data content.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DataContent

    """
    decodings = [
        ('aggregation', False, 'str', 'child::cim:aggregation'),
        ('frequency', False, 'str', 'child::cim:frequency/@value'),
        ('topic', False, decode_data_topic, 'child::cim:topic'),
    ]

    return set_attributes(DataContent(), xml, nsmap, decodings)


def decode_data_distribution(xml, nsmap):
    """Decodes an instance of the following type: data distribution.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DataDistribution

    """
    decodings = [
        ('access', False, 'str', '@distributionAccess'),
        ('format', False, 'str', 'child::cim:distributionFormat/@value'),
        ('responsible_party', False, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(DataDistribution(), xml, nsmap, decodings)


def decode_data_extent(xml, nsmap):
    """Decodes an instance of the following type: data extent.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DataExtent

    """
    decodings = [
        ('geographical', False, decode_data_extent_geographical, 'child::gmd:geographicElement'),
        ('temporal', False, decode_data_extent_temporal, 'child::gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod'),
    ]

    return set_attributes(DataExtent(), xml, nsmap, decodings)


def decode_data_extent_geographical(xml, nsmap):
    """Decodes an instance of the following type: data extent geographical.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DataExtentGeographical

    """
    decodings = [
        ('east', False, 'float', 'child::gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/gco:Decimal'),
        ('north', False, 'float', 'child::gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/gco:Decimal'),
        ('south', False, 'float', 'child::gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/gco:Decimal'),
        ('west', False, 'float', 'child::gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/gco:Decimal'),
    ]

    return set_attributes(DataExtentGeographical(), xml, nsmap, decodings)


def decode_data_extent_temporal(xml, nsmap):
    """Decodes an instance of the following type: data extent temporal.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DataExtentTemporal

    """
    decodings = [
        ('begin', False, 'date', 'child::gml:beginPosition'),
        ('end', False, 'date', 'child::gml:endPosition'),
        ('time_interval', False, decode_data_extent_time_interval, 'child::gml:timeInterval'),
    ]

    return set_attributes(DataExtentTemporal(), xml, nsmap, decodings)


def decode_data_extent_time_interval(xml, nsmap):
    """Decodes an instance of the following type: data extent time interval.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DataExtentTimeInterval

    """
    decodings = [
        ('factor', False, 'int', '@factor'),
        ('radix', False, 'int', '@radix'),
        ('unit', False, 'str', '@unit'),
    ]

    return set_attributes(DataExtentTimeInterval(), xml, nsmap, decodings)


def decode_data_hierarchy_level(xml, nsmap):
    """Decodes an instance of the following type: data hierarchy level.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DataHierarchyLevel

    """
    decodings = [
        ('is_open', False, 'bool', 'child::cim:hierarchyLevelName/@open'),
        ('name', False, 'str', 'child::cim:hierarchyLevelName/@value'),
        ('value', False, 'str', 'child::cim:hierarchyLevelValue'),
    ]

    return set_attributes(DataHierarchyLevel(), xml, nsmap, decodings)


def decode_data_object(xml, nsmap):
    """Decodes an instance of the following type: data object.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DataObject

    """
    decodings = [
        ('acronym', False, 'str', 'child::cim:acronym'),
        ('cim_info', False, decode_cim_info, 'self::cim:dataObject'),
        ('citations', True, decode_citation, '//cim:citation[not(cim:citation)]'),
        ('content', True, decode_data_content, 'child::cim:content'),
        ('data_property', True, decode_data_property, 'child::cim:dataProperty/cim:dataProperty'),
        ('data_status', False, 'str', 'self::cim:dataObject/@dataStatus'),
        ('description', False, 'str', 'child::cim:description'),
        ('distribution', False, decode_data_distribution, 'child::cim:distribution'),
        ('extent', False, decode_data_extent, 'child::cim:extent'),
        ('hierarchy_level', False, decode_data_hierarchy_level, 'self::cim:dataObject'),
        ('keyword', False, 'str', 'child::cim:keyword'),
        ('purpose', False, 'str', 'self::cim:dataObject/@purpose'),
    ]

    return set_attributes(DataObject(), xml, nsmap, decodings)


def decode_data_property(xml, nsmap):
    """Decodes an instance of the following type: data property.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DataProperty

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('name', False, 'str', 'child::cim:name'),
        ('value', False, 'str', 'child::cim:value'),
    ]

    return set_attributes(DataProperty(), xml, nsmap, decodings)


def decode_data_restriction(xml, nsmap):
    """Decodes an instance of the following type: data restriction.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DataRestriction

    """
    decodings = [
    ]

    return set_attributes(DataRestriction(), xml, nsmap, decodings)


def decode_data_storage(xml, nsmap):
    """Decodes an instance of the following type: data storage.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DataStorage

    """
    decodings = [
    ]

    return set_attributes(DataStorage(), xml, nsmap, decodings)


def decode_data_storage_db(xml, nsmap):
    """Decodes an instance of the following type: data storage db.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DataStorageDb

    """
    decodings = [
    ]

    return set_attributes(DataStorageDb(), xml, nsmap, decodings)


def decode_data_storage_file(xml, nsmap):
    """Decodes an instance of the following type: data storage file.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DataStorageFile

    """
    decodings = [
    ]

    return set_attributes(DataStorageFile(), xml, nsmap, decodings)


def decode_data_storage_ip(xml, nsmap):
    """Decodes an instance of the following type: data storage ip.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DataStorageIp

    """
    decodings = [
    ]

    return set_attributes(DataStorageIp(), xml, nsmap, decodings)


def decode_data_topic(xml, nsmap):
    """Decodes an instance of the following type: data topic.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.DataTopic

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('name', False, 'str', 'child::cim:name'),
        ('unit', False, 'str', 'child::cim:unit/@value'),
    ]

    return set_attributes(DataTopic(), xml, nsmap, decodings)


