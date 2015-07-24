# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.decoder_for_software_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-07-24 23:33:18.128589.

"""
from decoder_xml_utils import set_attributes
from decoder_for_activity_package import *
from decoder_for_data_package import *
from decoder_for_grids_package import *
from decoder_for_shared_package import *
import typeset



def decode_component_property(xml, nsmap):
    """Decodes an instance of the following type: component property.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.ComponentProperty

    """
    decodings = [
        ('long_name', False, 'str', 'child::cim:longName'),
        ('is_represented', False, 'bool', 'self::cim:componentProperty/@represented'),
        ('description', False, 'str', 'child::cim:description'),
        ('sub_properties', True, decode_component_property, 'child::cim:componentProperty'),
        ('units', False, 'str', 'child::cim:units/@value'),
        ('standard_names', True, 'str', 'child::cim:standardName/@value'),
        ('citations', True, decode_citation, 'child::cim:citation'),
        ('values', True, 'str', 'child::cim:value'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('intent', False, 'str', 'self::cim:componentProperty/@intent'),
    ]

    return set_attributes(typeset.software.ComponentProperty(), xml, nsmap, decodings)


def decode_statistical_model_component(xml, nsmap):
    """Decodes an instance of the following type: statistical model component.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.StatisticalModelComponent

    """
    decodings = [
        ('properties', True, decode_component_property, 'child::cim:componentProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:scientificProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:numericalProperties/cim:componentProperty'),
        ('meta', False, decode_doc_meta_info, 'self::cim:statisticalModelComponent'),
        ('language', False, decode_component_language, 'child::cim:componentLanguage'),
        ('type', False, 'str', 'child::cim:type[1]/@value'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('types', True, 'str', 'child::cim:type/@value'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('timing', False, decode_timing, 'child::cim:timing'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('description', False, 'str', 'child::cim:description'),
        ('sub_components', True, decode_model_component, 'child::cim:childComponent/cim:modelComponent'),
        ('sub_components', True, decode_processor_component, 'child::cim:childComponent/cim:processorComponent'),
        ('release_date', False, 'datetime.datetime', 'child::cim:releaseDate'),
        ('citations', True, decode_citation, 'child::cim:citation'),
    ]

    return set_attributes(typeset.software.StatisticalModelComponent(), xml, nsmap, decodings)


def decode_connection_property(xml, nsmap):
    """Decodes an instance of the following type: connection property.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.ConnectionProperty

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
        ('value', False, 'str', 'child::cim:value'),
    ]

    return set_attributes(typeset.software.ConnectionProperty(), xml, nsmap, decodings)


def decode_component(xml, nsmap):
    """Decodes an instance of the following type: component.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.Component

    """
    decodings = [
        ('properties', True, decode_component_property, 'child::cim:componentProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:scientificProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:numericalProperties/cim:componentProperty'),
        ('citations', True, decode_citation, 'child::cim:citation'),
        ('language', False, decode_component_language, 'child::cim:componentLanguage'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('sub_components', True, decode_model_component, 'child::cim:childComponent/cim:modelComponent'),
        ('sub_components', True, decode_processor_component, 'child::cim:childComponent/cim:processorComponent'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('description', False, 'str', 'child::cim:description'),
        ('release_date', False, 'datetime.datetime', 'child::cim:releaseDate'),
    ]

    return set_attributes(typeset.software.Component(), xml, nsmap, decodings)


def decode_parallelisation(xml, nsmap):
    """Decodes an instance of the following type: parallelisation.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.Parallelisation

    """
    decodings = [
        ('processes', False, 'int', 'child::cim:processes'),
        ('ranks', True, decode_rank, 'child::cim:rank'),
    ]

    return set_attributes(typeset.software.Parallelisation(), xml, nsmap, decodings)


def decode_spatial_regridding(xml, nsmap):
    """Decodes an instance of the following type: spatial regridding.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.SpatialRegridding

    """
    decodings = [
        ('standard_method', False, 'str', 'child::cim:spatialRegriddingStandardMethod'),
        ('properties', True, decode_spatial_regridding_property, 'child::cim:spatialRegriddingProperty'),
        ('dimension', False, 'str', 'child::cim:spatialRegriddingDimension'),
        ('user_method', False, decode_spatial_regridding_user_method, 'child::cim:spatialRegriddingUserMethod'),
    ]

    return set_attributes(typeset.software.SpatialRegridding(), xml, nsmap, decodings)


def decode_model_component(xml, nsmap):
    """Decodes an instance of the following type: model component.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.ModelComponent

    """
    decodings = [
        ('properties', True, decode_component_property, 'child::cim:componentProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:scientificProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:numericalProperties/cim:componentProperty'),
        ('meta', False, decode_doc_meta_info, 'self::cim:modelComponent'),
        ('description', False, 'str', 'child::cim:description'),
        ('type', False, 'str', 'child::cim:type[1]/@value'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('sub_components', True, decode_model_component, 'child::cim:childComponent/cim:modelComponent'),
        ('sub_components', True, decode_processor_component, 'child::cim:childComponent/cim:processorComponent'),
        ('types', True, 'str', 'child::cim:type/@value'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('language', False, decode_component_language, 'child::cim:componentLanguage'),
        ('timing', False, decode_timing, 'child::cim:timing'),
        ('release_date', False, 'datetime.datetime', 'child::cim:releaseDate'),
        ('citations', True, decode_citation, 'child::cim:citation'),
    ]

    return set_attributes(typeset.software.ModelComponent(), xml, nsmap, decodings)


def decode_entry_point(xml, nsmap):
    """Decodes an instance of the following type: entry point.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.EntryPoint

    """
    decodings = [
    ]

    return set_attributes(typeset.software.EntryPoint(), xml, nsmap, decodings)


def decode_timing(xml, nsmap):
    """Decodes an instance of the following type: timing.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.Timing

    """
    decodings = [
        ('rate', False, 'int', 'child::cim:rate'),
        ('is_variable_rate', False, 'bool', '@variableRate'),
        ('start', False, 'datetime.datetime', 'child::cim:start'),
        ('end', False, 'datetime.datetime', 'child::cim:end'),
        ('units', False, 'str', '@units'),
    ]

    return set_attributes(typeset.software.Timing(), xml, nsmap, decodings)


def decode_processor_component(xml, nsmap):
    """Decodes an instance of the following type: processor component.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.ProcessorComponent

    """
    decodings = [
        ('properties', True, decode_component_property, 'child::cim:componentProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:scientificProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:numericalProperties/cim:componentProperty'),
        ('language', False, decode_component_language, 'child::cim:componentLanguage'),
        ('meta', False, decode_doc_meta_info, 'self::cim:modelComponent'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('description', False, 'str', 'child::cim:description'),
        ('sub_components', True, decode_model_component, 'child::cim:childComponent/cim:modelComponent'),
        ('sub_components', True, decode_processor_component, 'child::cim:childComponent/cim:processorComponent'),
        ('release_date', False, 'datetime.datetime', 'child::cim:releaseDate'),
        ('citations', True, decode_citation, 'child::cim:citation'),
    ]

    return set_attributes(typeset.software.ProcessorComponent(), xml, nsmap, decodings)


def decode_time_lag(xml, nsmap):
    """Decodes an instance of the following type: time lag.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.TimeLag

    """
    decodings = [
        ('units', False, 'str', '@units'),
        ('value', False, 'int', 'child::cim:value'),
    ]

    return set_attributes(typeset.software.TimeLag(), xml, nsmap, decodings)


def decode_connection(xml, nsmap):
    """Decodes an instance of the following type: connection.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.Connection

    """
    decodings = [
        ('priming_reference', False, decode_doc_reference, 'child::cim:priming/cim:reference'),
        ('time_profile', False, decode_timing, 'child::cim:timeProfile'),
        ('sources', True, decode_connection_endpoint, 'child::cim:connectionSource'),
        ('transformers', True, decode_processor_component, 'child::cim:transformer/cim:processorComponent'),
        ('description', False, 'str', 'child::cim:description'),
        ('time_transformation', False, decode_time_transformation, 'child::cim:timeTransformation'),
        ('time_lag', False, 'str', 'child::cim:timeLag'),
        ('spatial_regridding', True, decode_spatial_regridding, 'child::cim:spatialRegridding'),
        ('transformers_references', True, decode_doc_reference, 'child::cim:transformer/cim:reference'),
        ('type', False, 'str', 'child::cim:type/@value'),
        ('properties', True, decode_connection_property, 'child::cim:connectionProperty'),
        ('priming', False, decode_processor_component, 'child::cim:priming/cim:priming/cim:softwareComponent'),
        ('priming', False, decode_statistical_model_component, 'child::cim:priming/cim:priming/cim:softwareComponent'),
        ('priming', False, decode_data_object, 'child::cim:priming/cim:priming/cim:dataObject'),
        ('priming', False, decode_data_content, 'child::cim:priming/cim:priming/cim:dataContent'),
        ('priming', False, decode_component_property, 'child::cim:priming/cim:priming/cim:componentProperty'),
        ('priming', False, decode_model_component, 'child::cim:priming/cim:priming/cim:softwareComponent'),
        ('target', False, decode_connection_endpoint, 'child::cim:connectionTarget'),
    ]

    return set_attributes(typeset.software.Connection(), xml, nsmap, decodings)


def decode_coupling_property(xml, nsmap):
    """Decodes an instance of the following type: coupling property.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.CouplingProperty

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
        ('value', False, 'str', 'child::cim:value'),
    ]

    return set_attributes(typeset.software.CouplingProperty(), xml, nsmap, decodings)


def decode_rank(xml, nsmap):
    """Decodes an instance of the following type: rank.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.Rank

    """
    decodings = [
        ('max', False, 'int', 'child::cim:rankMax'),
        ('value', False, 'int', 'child::cim:rankValue'),
        ('min', False, 'int', 'child::cim:rankMin'),
        ('increment', False, 'int', 'child::cim:rankIncrement'),
    ]

    return set_attributes(typeset.software.Rank(), xml, nsmap, decodings)


def decode_deployment(xml, nsmap):
    """Decodes an instance of the following type: deployment.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.Deployment

    """
    decodings = [
        ('executable_arguments', True, 'str', 'child::cim:executableArgument'),
        ('platform', False, decode_platform, 'child::cim:platform/cim:platform'),
        ('executable_name', False, 'str', 'child::cim:executableName'),
        ('description', False, 'str', 'child::cim:description'),
        ('deployment_date', False, 'datetime.datetime', 'child::cim:deploymentDate'),
        ('parallelisation', False, decode_parallelisation, 'child::cim:parallelisation'),
        ('platform_reference', False, decode_doc_reference, 'child::cim:platform/cim:reference'),
    ]

    return set_attributes(typeset.software.Deployment(), xml, nsmap, decodings)


def decode_time_transformation(xml, nsmap):
    """Decodes an instance of the following type: time transformation.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.TimeTransformation

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('mapping_type', False, 'str', 'child::cim:mappingType/@value'),
    ]

    return set_attributes(typeset.software.TimeTransformation(), xml, nsmap, decodings)


def decode_coupling_endpoint(xml, nsmap):
    """Decodes an instance of the following type: coupling endpoint.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.CouplingEndpoint

    """
    decodings = [
        ('data_source_reference', False, decode_doc_reference, 'child::cim:dataSource/cim:reference'),
        ('instance_id', False, 'str', 'child::cim:instanceID'),
        ('properties', True, decode_coupling_property, 'child::cim:couplingProperty'),
        ('data_source', False, decode_processor_component, 'child::cim:dataSource/cim:dataSource/cim:softwareComponent'),
        ('data_source', False, decode_statistical_model_component, 'child::cim:dataSource/cim:dataSource/cim:softwareComponent'),
        ('data_source', False, decode_data_object, 'child::cim:dataSource/cim:dataSource/cim:dataObject'),
        ('data_source', False, decode_data_content, 'child::cim:dataSource/cim:dataSource/cim:dataContent'),
        ('data_source', False, decode_component_property, 'child::cim:dataSource/cim:dataSource/cim:componentProperty'),
        ('data_source', False, decode_model_component, 'child::cim:dataSource/cim:dataSource/cim:softwareComponent'),
    ]

    return set_attributes(typeset.software.CouplingEndpoint(), xml, nsmap, decodings)


def decode_component_language(xml, nsmap):
    """Decodes an instance of the following type: component language.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.ComponentLanguage

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
    ]

    return set_attributes(typeset.software.ComponentLanguage(), xml, nsmap, decodings)


def decode_spatial_regridding_user_method(xml, nsmap):
    """Decodes an instance of the following type: spatial regridding user method.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.SpatialRegriddingUserMethod

    """
    decodings = [
        ('file_reference', False, decode_doc_reference, 'child::cim:file/cim:reference'),
        ('name', False, 'str', 'child::cim:name'),
        ('file', False, decode_data_object, 'child::cim:file/cim:dataObject'),
    ]

    return set_attributes(typeset.software.SpatialRegriddingUserMethod(), xml, nsmap, decodings)


def decode_coupling(xml, nsmap):
    """Decodes an instance of the following type: coupling.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.Coupling

    """
    decodings = [
        ('time_profile', False, decode_timing, 'child::cim:timeProfile'),
        ('priming', False, decode_data_object, 'child::cim:priming/cim:priming/cim:dataObject'),
        ('priming', False, decode_data_content, 'child::cim:priming/cim:priming/cim:dataContent'),
        ('priming', False, decode_component_property, 'child::cim:priming/cim:priming/cim:componentProperty'),
        ('priming', False, decode_model_component, 'child::cim:priming/cim:priming/cim:softwareComponent'),
        ('priming', False, decode_processor_component, 'child::cim:priming/cim:priming/cim:softwareComponent'),
        ('priming', False, decode_statistical_model_component, 'child::cim:priming/cim:priming/cim:softwareComponent'),
        ('transformers_references', True, decode_doc_reference, 'child::cim:transformer/cim:reference'),
        ('target', False, decode_coupling_endpoint, 'child::cim:couplingTarget'),
        ('description', False, 'str', 'child::cim:description'),
        ('is_fully_specified', False, 'bool', '@fullySpecified'),
        ('transformers', True, decode_processor_component, 'child::cim:transformer/cim:processorComponent'),
        ('purpose', False, 'str', '@purpose'),
        ('time_transformation', False, decode_time_transformation, 'child::cim:timeTransformation'),
        ('type', False, 'str', 'child::cim:type/@value'),
        ('connections', True, decode_connection, 'child::cim:connection'),
        ('priming_reference', False, decode_doc_reference, 'child::cim:priming/cim:reference'),
        ('properties', True, decode_coupling_property, 'child::cim:couplingProperty'),
        ('time_lag', False, decode_time_lag, 'child::cim:timeLag'),
        ('spatial_regriddings', True, decode_spatial_regridding, 'child::cim:spatialRegridding'),
        ('sources', True, decode_coupling_endpoint, 'child::cim:couplingSource'),
    ]

    return set_attributes(typeset.software.Coupling(), xml, nsmap, decodings)


def decode_spatial_regridding_property(xml, nsmap):
    """Decodes an instance of the following type: spatial regridding property.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.SpatialRegriddingProperty

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
        ('value', False, 'str', 'child::cim:value'),
    ]

    return set_attributes(typeset.software.SpatialRegriddingProperty(), xml, nsmap, decodings)


def decode_connection_endpoint(xml, nsmap):
    """Decodes an instance of the following type: connection endpoint.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.ConnectionEndpoint

    """
    decodings = [
        ('data_source', False, decode_data_object, 'child::cim:dataSource/cim:dataSource/cim:dataObject'),
        ('data_source', False, decode_data_content, 'child::cim:dataSource/cim:dataSource/cim:dataContent'),
        ('data_source', False, decode_component_property, 'child::cim:dataSource/cim:dataSource/cim:componentProperty'),
        ('data_source', False, decode_model_component, 'child::cim:dataSource/cim:dataSource/cim:softwareComponent'),
        ('data_source', False, decode_processor_component, 'child::cim:dataSource/cim:dataSource/cim:softwareComponent'),
        ('data_source', False, decode_statistical_model_component, 'child::cim:dataSource/cim:dataSource/cim:softwareComponent'),
        ('data_source_reference', False, decode_doc_reference, 'child::cim:dataSource/cim:reference'),
        ('instance_id', False, 'str', 'child::cim:instanceID'),
        ('properties', True, decode_connection_property, 'child::cim:connectionProperty'),
    ]

    return set_attributes(typeset.software.ConnectionEndpoint(), xml, nsmap, decodings)


def decode_component_language_property(xml, nsmap):
    """Decodes an instance of the following type: component language property.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.ComponentLanguageProperty

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
        ('value', False, 'str', 'child::cim:value'),
    ]

    return set_attributes(typeset.software.ComponentLanguageProperty(), xml, nsmap, decodings)


def decode_composition(xml, nsmap):
    """Decodes an instance of the following type: composition.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.software.Composition

    """
    decodings = [
    ]

    return set_attributes(typeset.software.Composition(), xml, nsmap, decodings)


