"""
.. module:: cim.v1.decoder_for_data_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
from decoder_xml_utils import set_attributes
from decoder_for_shared_package import *
import typeset



def decode_data_content(xml, nsmap):
    """Decodes an instance of the following type: data content.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataContent

    """
    decodings = [
        ('aggregation', False, 'unicode', 'child::cim:aggregation'),
        ('frequency', False, 'unicode', 'child::cim:frequency/@value'),
        ('topic', False, decode_data_topic, 'child::cim:topic'),
    ]

    return set_attributes(typeset.data.DataContent(), xml, nsmap, decodings)


def decode_data_distribution(xml, nsmap):
    """Decodes an instance of the following type: data distribution.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataDistribution

    """
    decodings = [
        ('access', False, 'unicode', '@distributionAccess'),
        ('format', False, 'unicode', 'child::cim:distributionFormat/@value'),
        ('responsible_party', False, decode_responsible_party, 'child::cim:responsibleParty'),
    ]

    return set_attributes(typeset.data.DataDistribution(), xml, nsmap, decodings)


def decode_data_extent(xml, nsmap):
    """Decodes an instance of the following type: data extent.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

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

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

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

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

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

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataExtentTimeInterval

    """
    decodings = [
        ('factor', False, 'int', '@factor'),
        ('radix', False, 'int', '@radix'),
        ('unit', False, 'unicode', '@unit'),
    ]

    return set_attributes(typeset.data.DataExtentTimeInterval(), xml, nsmap, decodings)


def decode_data_hierarchy_level(xml, nsmap):
    """Decodes an instance of the following type: data hierarchy level.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataHierarchyLevel

    """
    decodings = [
        ('is_open', False, 'bool', 'child::cim:hierarchyLevelName/@open'),
        ('name', False, 'unicode', 'child::cim:hierarchyLevelName/@value'),
        ('value', False, 'unicode', 'child::cim:hierarchyLevelValue'),
    ]

    return set_attributes(typeset.data.DataHierarchyLevel(), xml, nsmap, decodings)


def decode_data_object(xml, nsmap):
    """Decodes an instance of the following type: data object.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataObject

    """
    decodings = [
        ('acronym', False, 'unicode', 'child::cim:acronym'),
        ('citations', True, decode_citation, '//cim:citation[not(cim:citation)]'),
        ('content', True, decode_data_content, 'child::cim:content'),
        ('data_status', False, 'unicode', 'self::cim:dataObject/@dataStatus'),
        ('description', False, 'unicode', 'child::cim:description'),
        ('distribution', False, decode_data_distribution, 'child::cim:distribution'),
        ('extent', False, decode_data_extent, 'child::cim:extent'),
        ('hierarchy_level', False, decode_data_hierarchy_level, 'self::cim:dataObject'),
        ('keyword', False, 'unicode', 'child::cim:keyword'),
        ('meta', False, decode_doc_meta_info, 'self::cim:dataObject'),
        ('properties', True, decode_data_property, 'child::cim:dataProperty/cim:dataProperty'),
        ('purpose', False, 'unicode', 'self::cim:dataObject/@purpose'),
        ('purpose', False, 'unicode', 'self::cim:dataObject/@purpose'),
        ('storage', True, decode_data_storage_ip, 'child::cim:storage/cim:ipStorage'),
    ]

    return set_attributes(typeset.data.DataObject(), xml, nsmap, decodings)


def decode_data_property(xml, nsmap):
    """Decodes an instance of the following type: data property.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataProperty

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('name', False, 'unicode', 'child::cim:name'),
        ('value', False, 'unicode', 'child::cim:value'),
    ]

    return set_attributes(typeset.data.DataProperty(), xml, nsmap, decodings)


def decode_data_restriction(xml, nsmap):
    """Decodes an instance of the following type: data restriction.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataRestriction

    """
    decodings = [
    ]

    return set_attributes(typeset.data.DataRestriction(), xml, nsmap, decodings)


def decode_data_storage(xml, nsmap):
    """Decodes an instance of the following type: data storage.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataStorage

    """
    decodings = [
    ]

    return set_attributes(typeset.data.DataStorage(), xml, nsmap, decodings)


def decode_data_storage_db(xml, nsmap):
    """Decodes an instance of the following type: data storage db.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataStorageDb

    """
    decodings = [
    ]

    return set_attributes(typeset.data.DataStorageDb(), xml, nsmap, decodings)


def decode_data_storage_file(xml, nsmap):
    """Decodes an instance of the following type: data storage file.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataStorageFile

    """
    decodings = [
    ]

    return set_attributes(typeset.data.DataStorageFile(), xml, nsmap, decodings)


def decode_data_storage_ip(xml, nsmap):
    """Decodes an instance of the following type: data storage ip.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataStorageIp

    """
    decodings = [
        ('file_name', False, 'unicode', 'child::cim:fileName'),
        ('format', False, 'unicode', 'child::cim:dataFormat/@value'),
    ]

    return set_attributes(typeset.data.DataStorageIp(), xml, nsmap, decodings)


def decode_data_topic(xml, nsmap):
    """Decodes an instance of the following type: data topic.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.data.DataTopic

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('name', False, 'unicode', 'child::cim:name'),
        ('unit', False, 'unicode', 'child::cim:unit/@value'),
    ]

    return set_attributes(typeset.data.DataTopic(), xml, nsmap, decodings)


