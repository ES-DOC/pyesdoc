"""
.. module:: cim.v1.decoding.decoder_for_software_package.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:07.999045.

"""

# Module imports.
from lxml import etree as et

from pyesdoc.serialization.decoder_xml_utils import *
from pyesdoc.ontologies.cim.v1.serialization.decoder_for_activity_package import *
from pyesdoc.ontologies.cim.v1.serialization.decoder_for_data_package import *
from pyesdoc.ontologies.cim.v1.serialization.decoder_for_grids_package import *
from pyesdoc.ontologies.cim.v1.serialization.decoder_for_shared_package import *
from pyesdoc.ontologies.cim.v1.types.software import *




def decode_component(xml, nsmap):
    """Decodes an instance of the following type: component.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Component

    """
    decodings = [
        ('children', True, decode_model_component, 'child::cim:childComponent/cim:modelComponent'),
        ('children', True, decode_processor_component, 'child::cim:childComponent/cim:processorComponent'),
        ('citation_list', True, decode_citation, 'child::cim:citation'),
        ('citations', True, decode_citation, 'child::cim:citation'),
        ('description', False, 'str', 'child::cim:description'),
        ('language', False, decode_component_language, 'child::cim:componentLanguage'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('properties', True, decode_component_property, 'child::cim:componentProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:scientificProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:numericalProperties/cim:componentProperty'),
        ('property_tree', True, decode_component_property, 'child::cim:componentProperties/cim:componentProperty'),
        ('property_tree', True, decode_component_property, 'child::cim:scientificProperties/cim:componentProperty'),
        ('property_tree', True, decode_component_property, 'child::cim:numericalProperties/cim:componentProperty'),
        ('release_date', False, 'datetime', 'child::cim:releaseDate'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('responsible_party_list', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName'),
    ]

    return set_attributes(Component(), xml, nsmap, decodings)


def decode_component_language(xml, nsmap):
    """Decodes an instance of the following type: component language.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.ComponentLanguage

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
    ]

    return set_attributes(ComponentLanguage(), xml, nsmap, decodings)


def decode_component_language_property(xml, nsmap):
    """Decodes an instance of the following type: component language property.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.ComponentLanguageProperty

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
        ('value', False, 'str', 'child::cim:value'),
    ]

    return set_attributes(ComponentLanguageProperty(), xml, nsmap, decodings)


def decode_component_property(xml, nsmap):
    """Decodes an instance of the following type: component property.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.ComponentProperty

    """
    decodings = [
        ('children', True, decode_component_property, 'child::cim:componentProperty'),
        ('citations', True, decode_citation, 'child::cim:citation'),
        ('description', False, 'str', 'child::cim:description'),
        ('intent', False, 'str', 'self::cim:componentProperty/@intent'),
        ('is_represented', False, 'bool', 'self::cim:componentProperty/@represented'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('standard_names', True, 'str', 'child::cim:standardName/@value'),
        ('units', False, 'str', 'child::cim:units/@value'),
        ('values', True, 'str', 'child::cim:value'),
    ]

    return set_attributes(ComponentProperty(), xml, nsmap, decodings)


def decode_composition(xml, nsmap):
    """Decodes an instance of the following type: composition.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Composition

    """
    decodings = [
    ]

    return set_attributes(Composition(), xml, nsmap, decodings)


def decode_connection(xml, nsmap):
    """Decodes an instance of the following type: connection.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Connection

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('priming', False, decode_data_object, 'child::cim:priming/cim:priming/cim:dataObject'),
        ('priming', False, decode_data_content, 'child::cim:priming/cim:priming/cim:dataContent'),
        ('priming', False, decode_component_property, 'child::cim:priming/cim:priming/cim:componentProperty'),
        ('priming', False, decode_model_component, 'child::cim:priming/cim:priming/cim:softwareComponent'),
        ('priming', False, decode_processor_component, 'child::cim:priming/cim:priming/cim:softwareComponent'),
        ('priming', False, decode_statistical_model_component, 'child::cim:priming/cim:priming/cim:softwareComponent'),
        ('priming_reference', False, decode_cim_reference, 'child::cim:priming/cim:reference'),
        ('properties', True, decode_connection_property, 'child::cim:connectionProperty'),
        ('sources', True, decode_connection_endpoint, 'child::cim:connectionSource'),
        ('spatial_regridding', True, decode_spatial_regridding, 'child::cim:spatialRegridding'),
        ('target', False, decode_connection_endpoint, 'child::cim:connectionTarget'),
        ('time_lag', False, 'str', 'child::cim:timeLag'),
        ('time_profile', False, decode_timing, 'child::cim:timeProfile'),
        ('time_transformation', False, decode_time_transformation, 'child::cim:timeTransformation'),
        ('transformers', True, decode_processor_component, 'child::cim:transformer/cim:processorComponent'),
        ('transformers_references', True, decode_cim_reference, 'child::cim:transformer/cim:reference'),
        ('type', False, 'str', 'child::cim:type/@value'),
    ]

    return set_attributes(Connection(), xml, nsmap, decodings)


def decode_connection_endpoint(xml, nsmap):
    """Decodes an instance of the following type: connection endpoint.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.ConnectionEndpoint

    """
    decodings = [
        ('data_source', False, decode_data_object, 'child::cim:dataSource/cim:dataSource/cim:dataObject'),
        ('data_source', False, decode_data_content, 'child::cim:dataSource/cim:dataSource/cim:dataContent'),
        ('data_source', False, decode_component_property, 'child::cim:dataSource/cim:dataSource/cim:componentProperty'),
        ('data_source', False, decode_model_component, 'child::cim:dataSource/cim:dataSource/cim:softwareComponent'),
        ('data_source', False, decode_processor_component, 'child::cim:dataSource/cim:dataSource/cim:softwareComponent'),
        ('data_source', False, decode_statistical_model_component, 'child::cim:dataSource/cim:dataSource/cim:softwareComponent'),
        ('data_source_reference', False, decode_cim_reference, 'child::cim:dataSource/cim:reference'),
        ('instance_id', False, 'str', 'child::cim:instanceID'),
        ('properties', True, decode_connection_property, 'child::cim:connectionProperty'),
    ]

    return set_attributes(ConnectionEndpoint(), xml, nsmap, decodings)


def decode_connection_property(xml, nsmap):
    """Decodes an instance of the following type: connection property.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.ConnectionProperty

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
        ('value', False, 'str', 'child::cim:value'),
    ]

    return set_attributes(ConnectionProperty(), xml, nsmap, decodings)


def decode_coupling(xml, nsmap):
    """Decodes an instance of the following type: coupling.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Coupling

    """
    decodings = [
        ('connections', True, decode_connection, 'child::cim:connection'),
        ('description', False, 'str', 'child::cim:description'),
        ('is_fully_specified', False, 'bool', '@fullySpecified'),
        ('priming', False, decode_data_object, 'child::cim:priming/cim:priming/cim:dataObject'),
        ('priming', False, decode_data_content, 'child::cim:priming/cim:priming/cim:dataContent'),
        ('priming', False, decode_component_property, 'child::cim:priming/cim:priming/cim:componentProperty'),
        ('priming', False, decode_model_component, 'child::cim:priming/cim:priming/cim:softwareComponent'),
        ('priming', False, decode_processor_component, 'child::cim:priming/cim:priming/cim:softwareComponent'),
        ('priming', False, decode_statistical_model_component, 'child::cim:priming/cim:priming/cim:softwareComponent'),
        ('priming_reference', False, decode_cim_reference, 'child::cim:priming/cim:reference'),
        ('properties', True, decode_coupling_property, 'child::cim:couplingProperty'),
        ('purpose', False, 'str', '@purpose'),
        ('sources', True, decode_coupling_endpoint, 'child::cim:couplingSource'),
        ('spatial_regriddings', True, decode_spatial_regridding, 'child::cim:spatialRegridding'),
        ('target', False, decode_coupling_endpoint, 'child::cim:couplingTarget'),
        ('time_lag', False, decode_time_lag, 'child::cim:timeLag'),
        ('time_profile', False, decode_timing, 'child::cim:timeProfile'),
        ('time_transformation', False, decode_time_transformation, 'child::cim:timeTransformation'),
        ('transformers', True, decode_processor_component, 'child::cim:transformer/cim:processorComponent'),
        ('transformers_references', True, decode_cim_reference, 'child::cim:transformer/cim:reference'),
        ('type', False, 'str', 'child::cim:type/@value'),
    ]

    return set_attributes(Coupling(), xml, nsmap, decodings)


def decode_coupling_endpoint(xml, nsmap):
    """Decodes an instance of the following type: coupling endpoint.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.CouplingEndpoint

    """
    decodings = [
        ('data_source', False, decode_data_object, 'child::cim:dataSource/cim:dataSource/cim:dataObject'),
        ('data_source', False, decode_data_content, 'child::cim:dataSource/cim:dataSource/cim:dataContent'),
        ('data_source', False, decode_component_property, 'child::cim:dataSource/cim:dataSource/cim:componentProperty'),
        ('data_source', False, decode_model_component, 'child::cim:dataSource/cim:dataSource/cim:softwareComponent'),
        ('data_source', False, decode_processor_component, 'child::cim:dataSource/cim:dataSource/cim:softwareComponent'),
        ('data_source', False, decode_statistical_model_component, 'child::cim:dataSource/cim:dataSource/cim:softwareComponent'),
        ('data_source_reference', False, decode_cim_reference, 'child::cim:dataSource/cim:reference'),
        ('instance_id', False, 'str', 'child::cim:instanceID'),
        ('properties', True, decode_coupling_property, 'child::cim:couplingProperty'),
    ]

    return set_attributes(CouplingEndpoint(), xml, nsmap, decodings)


def decode_coupling_property(xml, nsmap):
    """Decodes an instance of the following type: coupling property.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.CouplingProperty

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
        ('value', False, 'str', 'child::cim:value'),
    ]

    return set_attributes(CouplingProperty(), xml, nsmap, decodings)


def decode_deployment(xml, nsmap):
    """Decodes an instance of the following type: deployment.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Deployment

    """
    decodings = [
        ('deployment_date', False, 'datetime', 'child::cim:deploymentDate'),
        ('description', False, 'str', 'child::cim:description'),
        ('executable_arguments', True, 'str', 'child::cim:executableArgument'),
        ('executable_name', False, 'str', 'child::cim:executableName'),
        ('parallelisation', False, decode_parallelisation, 'child::cim:parallelisation'),
        ('platform', False, decode_platform, 'child::cim:platform/cim:platform'),
        ('platform_reference', False, decode_cim_reference, 'child::cim:platform/cim:reference'),
    ]

    return set_attributes(Deployment(), xml, nsmap, decodings)


def decode_entry_point(xml, nsmap):
    """Decodes an instance of the following type: entry point.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.EntryPoint

    """
    decodings = [
    ]

    return set_attributes(EntryPoint(), xml, nsmap, decodings)


def decode_model_component(xml, nsmap):
    """Decodes an instance of the following type: model component.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.ModelComponent

    """
    decodings = [
        ('children', True, decode_model_component, 'child::cim:childComponent/cim:modelComponent'),
        ('children', True, decode_processor_component, 'child::cim:childComponent/cim:processorComponent'),
        ('cim_info', False, decode_cim_info, 'self::cim:modelComponent'),
        ('citation_list', True, decode_citation, 'child::cim:citation'),
        ('citations', True, decode_citation, 'child::cim:citation'),
        ('description', False, 'str', 'child::cim:description'),
        ('language', False, decode_component_language, 'child::cim:componentLanguage'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('properties', True, decode_component_property, 'child::cim:componentProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:scientificProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:numericalProperties/cim:componentProperty'),
        ('property_tree', True, decode_component_property, 'child::cim:componentProperties/cim:componentProperty'),
        ('property_tree', True, decode_component_property, 'child::cim:scientificProperties/cim:componentProperty'),
        ('property_tree', True, decode_component_property, 'child::cim:numericalProperties/cim:componentProperty'),
        ('release_date', False, 'datetime', 'child::cim:releaseDate'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('responsible_party_list', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('timing', False, decode_timing, 'child::cim:timing'),
        ('type', False, 'str', 'child::cim:type[1]/@value'),
        ('types', True, 'str', 'child::cim:type/@value'),
    ]

    return set_attributes(ModelComponent(), xml, nsmap, decodings)


def decode_parallelisation(xml, nsmap):
    """Decodes an instance of the following type: parallelisation.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Parallelisation

    """
    decodings = [
        ('processes', False, 'int', 'child::cim:processes'),
        ('ranks', True, decode_rank, 'child::cim:rank'),
    ]

    return set_attributes(Parallelisation(), xml, nsmap, decodings)


def decode_processor_component(xml, nsmap):
    """Decodes an instance of the following type: processor component.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.ProcessorComponent

    """
    decodings = [
        ('children', True, decode_model_component, 'child::cim:childComponent/cim:modelComponent'),
        ('children', True, decode_processor_component, 'child::cim:childComponent/cim:processorComponent'),
        ('cim_info', False, decode_cim_info, 'self::cim:modelComponent'),
        ('citation_list', True, decode_citation, 'child::cim:citation'),
        ('citations', True, decode_citation, 'child::cim:citation'),
        ('description', False, 'str', 'child::cim:description'),
        ('language', False, decode_component_language, 'child::cim:componentLanguage'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('properties', True, decode_component_property, 'child::cim:componentProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:scientificProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:numericalProperties/cim:componentProperty'),
        ('property_tree', True, decode_component_property, 'child::cim:componentProperties/cim:componentProperty'),
        ('property_tree', True, decode_component_property, 'child::cim:scientificProperties/cim:componentProperty'),
        ('property_tree', True, decode_component_property, 'child::cim:numericalProperties/cim:componentProperty'),
        ('release_date', False, 'datetime', 'child::cim:releaseDate'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('responsible_party_list', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName'),
    ]

    return set_attributes(ProcessorComponent(), xml, nsmap, decodings)


def decode_rank(xml, nsmap):
    """Decodes an instance of the following type: rank.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Rank

    """
    decodings = [
        ('increment', False, 'int', 'child::cim:rankIncrement'),
        ('max', False, 'int', 'child::cim:rankMax'),
        ('min', False, 'int', 'child::cim:rankMin'),
        ('value', False, 'int', 'child::cim:rankValue'),
    ]

    return set_attributes(Rank(), xml, nsmap, decodings)


def decode_spatial_regridding(xml, nsmap):
    """Decodes an instance of the following type: spatial regridding.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.SpatialRegridding

    """
    decodings = [
        ('dimension', False, 'str', 'child::cim:spatialRegriddingDimension'),
        ('properties', True, decode_spatial_regridding_property, 'child::cim:spatialRegriddingProperty'),
        ('standard_method', False, 'str', 'child::cim:spatialRegriddingStandardMethod'),
        ('user_method', False, decode_spatial_regridding_user_method, 'child::cim:spatialRegriddingUserMethod'),
    ]

    return set_attributes(SpatialRegridding(), xml, nsmap, decodings)


def decode_spatial_regridding_property(xml, nsmap):
    """Decodes an instance of the following type: spatial regridding property.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.SpatialRegriddingProperty

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
        ('value', False, 'str', 'child::cim:value'),
    ]

    return set_attributes(SpatialRegriddingProperty(), xml, nsmap, decodings)


def decode_spatial_regridding_user_method(xml, nsmap):
    """Decodes an instance of the following type: spatial regridding user method.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.SpatialRegriddingUserMethod

    """
    decodings = [
        ('file', False, decode_data_object, 'child::cim:file/cim:dataObject'),
        ('file_reference', False, decode_cim_reference, 'child::cim:file/cim:reference'),
        ('name', False, 'str', 'child::cim:name'),
    ]

    return set_attributes(SpatialRegriddingUserMethod(), xml, nsmap, decodings)


def decode_statistical_model_component(xml, nsmap):
    """Decodes an instance of the following type: statistical model component.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.StatisticalModelComponent

    """
    decodings = [
        ('children', True, decode_model_component, 'child::cim:childComponent/cim:modelComponent'),
        ('children', True, decode_processor_component, 'child::cim:childComponent/cim:processorComponent'),
        ('cim_info', False, decode_cim_info, 'self::cim:statisticalModelComponent'),
        ('citation_list', True, decode_citation, 'child::cim:citation'),
        ('citations', True, decode_citation, 'child::cim:citation'),
        ('description', False, 'str', 'child::cim:description'),
        ('language', False, decode_component_language, 'child::cim:componentLanguage'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('properties', True, decode_component_property, 'child::cim:componentProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:scientificProperties/cim:componentProperty'),
        ('properties', True, decode_component_property, 'child::cim:numericalProperties/cim:componentProperty'),
        ('property_tree', True, decode_component_property, 'child::cim:componentProperties/cim:componentProperty'),
        ('property_tree', True, decode_component_property, 'child::cim:scientificProperties/cim:componentProperty'),
        ('property_tree', True, decode_component_property, 'child::cim:numericalProperties/cim:componentProperty'),
        ('release_date', False, 'datetime', 'child::cim:releaseDate'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('responsible_party_list', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('timing', False, decode_timing, 'child::cim:timing'),
        ('type', False, 'str', 'child::cim:type[1]/@value'),
        ('types', True, 'str', 'child::cim:type/@value'),
    ]

    return set_attributes(StatisticalModelComponent(), xml, nsmap, decodings)


def decode_time_lag(xml, nsmap):
    """Decodes an instance of the following type: time lag.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.TimeLag

    """
    decodings = [
        ('units', False, 'str', '@units'),
        ('value', False, 'int', 'child::cim:value'),
    ]

    return set_attributes(TimeLag(), xml, nsmap, decodings)


def decode_time_transformation(xml, nsmap):
    """Decodes an instance of the following type: time transformation.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.TimeTransformation

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('mapping_type', False, 'str', 'child::cim:mappingType/@value'),
    ]

    return set_attributes(TimeTransformation(), xml, nsmap, decodings)


def decode_timing(xml, nsmap):
    """Decodes an instance of the following type: timing.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Timing

    """
    decodings = [
        ('end', False, 'datetime', 'child::cim:end'),
        ('is_variable_rate', False, 'bool', '@variableRate'),
        ('rate', False, 'int', 'child::cim:rate'),
        ('start', False, 'datetime', 'child::cim:start'),
        ('units', False, 'str', '@units'),
    ]

    return set_attributes(Timing(), xml, nsmap, decodings)


