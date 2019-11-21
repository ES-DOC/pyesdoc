"""
.. module:: cim.v1.decoder_for_shared_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
from decoder_xml_utils import set_attributes
import typeset



def decode_calendar(xml, nsmap):
    """Decodes an instance of the following type: calendar.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Calendar

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('length', False, 'int', 'child::cim:length'),
        ('range', False, decode_closed_date_range, 'child::cim:range/cim:closedDateRange'),
        ('range', False, decode_open_date_range, 'child::cim:range/cim:openDateRange'),
    ]

    return set_attributes(typeset.shared.Calendar(), xml, nsmap, decodings)


def decode_change(xml, nsmap):
    """Decodes an instance of the following type: change.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Change

    """
    decodings = [
        ('author', False, decode_responsible_party, 'child::cim:changeAuthor'),
        ('date', False, 'datetime.datetime', 'child::cim:changeDate'),
        ('description', False, 'unicode', 'child::cim:description'),
        ('details', True, decode_change_property, 'child::cim:detail'),
        ('name', False, 'unicode', 'child::cim:name'),
        ('type', False, 'unicode', 'self::cim:change/@type'),
    ]

    return set_attributes(typeset.shared.Change(), xml, nsmap, decodings)


def decode_change_property(xml, nsmap):
    """Decodes an instance of the following type: change property.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.ChangeProperty

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('id', False, 'unicode', 'child::cim:id'),
        ('name', False, 'unicode', 'child::cim:name'),
        ('value', False, 'unicode', 'child::cim:value'),
    ]

    return set_attributes(typeset.shared.ChangeProperty(), xml, nsmap, decodings)


def decode_citation(xml, nsmap):
    """Decodes an instance of the following type: citation.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Citation

    """
    decodings = [
        ('alternative_title', False, 'unicode', 'child::gmd:alternateTitle'),
        ('alternative_title', False, 'unicode', 'child::gmd:alternateTitle/gco:CharacterString'),
        ('collective_title', False, 'unicode', 'gmd:collectiveTitle'),
        ('collective_title', False, 'unicode', 'gmd:collectiveTitle/gco:CharacterString'),
        ('date', False, 'datetime.datetime', 'child::gmd:date/gmd:CI_Date/gmd:date/gco:Date'),
        ('date_type', False, 'unicode', 'child::gmd:date/gmd:CI_Date/gmd:dateType/gmd:CI_DateTypeCode/@codeListValue'),
        ('location', False, 'unicode', 'child::gmd:otherCitationDetails'),
        ('location', False, 'unicode', 'child::gmd:otherCitationDetails/gco:CharacterString'),
        ('title', False, 'unicode', 'child::gmd:title'),
        ('title', False, 'unicode', 'child::gmd:title/gco:CharacterString'),
        ('type', False, 'unicode', 'child::gmd:presentationForm/gmd:CI_PresentationFormCode/@codeListValue'),
    ]

    return set_attributes(typeset.shared.Citation(), xml, nsmap, decodings)


def decode_closed_date_range(xml, nsmap):
    """Decodes an instance of the following type: closed date range.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.ClosedDateRange

    """
    decodings = [
        ('duration', False, 'unicode', 'child::cim:duration'),
        ('end', False, 'datetime.datetime', 'child::cim:endDate'),
        ('start', False, 'datetime.datetime', 'child::cim:startDate'),
    ]

    return set_attributes(typeset.shared.ClosedDateRange(), xml, nsmap, decodings)


def decode_compiler(xml, nsmap):
    """Decodes an instance of the following type: compiler.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Compiler

    """
    decodings = [
        ('environment_variables', False, 'unicode', 'child::cim:compilerEnvironmentVariables'),
        ('language', False, 'unicode', 'child::cim:compilerLanguage'),
        ('name', False, 'unicode', 'child::cim:compilerName'),
        ('options', False, 'unicode', 'child::cim:compilerOptions'),
        ('type', False, 'unicode', 'child::cim:compilerType'),
        ('version', False, 'unicode', 'child::cim:compilerVersion'),
    ]

    return set_attributes(typeset.shared.Compiler(), xml, nsmap, decodings)


def decode_daily_360(xml, nsmap):
    """Decodes an instance of the following type: daily 360.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Daily360

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('length', False, 'int', 'child::cim:length'),
        ('range', False, decode_closed_date_range, 'child::cim:range/cim:closedDateRange'),
        ('range', False, decode_open_date_range, 'child::cim:range/cim:openDateRange'),
    ]

    return set_attributes(typeset.shared.Daily360(), xml, nsmap, decodings)


def decode_data_source(xml, nsmap):
    """Decodes an instance of the following type: data source.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.DataSource

    """
    decodings = [
    ]

    return set_attributes(typeset.shared.DataSource(), xml, nsmap, decodings)


def decode_date_range(xml, nsmap):
    """Decodes an instance of the following type: date range.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.DateRange

    """
    decodings = [
        ('duration', False, 'unicode', 'child::cim:duration'),
    ]

    return set_attributes(typeset.shared.DateRange(), xml, nsmap, decodings)


def decode_doc_meta_info(xml, nsmap):
    """Decodes an instance of the following type: doc meta info.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.DocMetaInfo

    """
    decodings = [
        ('author', False, decode_responsible_party, 'child::cim:documentAuthor'),
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
    :rtype: cim.v1.typeset.shared.DocReference

    """
    decodings = [
        ('changes', True, decode_change, 'child::cim:change'),
        ('description', False, 'unicode', 'child::cim:description'),
        ('external_id', False, 'unicode', 'child::cim:externalID'),
        ('id', False, 'unicode', 'child::cim:id'),
        ('name', False, 'unicode', 'child::cim:name'),
        ('type', False, 'unicode', 'child::cim:type'),
        ('version', False, 'int', 'child::cim:version'),
    ]

    return set_attributes(typeset.shared.DocReference(), xml, nsmap, decodings)


def decode_license(xml, nsmap):
    """Decodes an instance of the following type: license.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.License

    """
    decodings = [
    ]

    return set_attributes(typeset.shared.License(), xml, nsmap, decodings)


def decode_machine(xml, nsmap):
    """Decodes an instance of the following type: machine.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Machine

    """
    decodings = [
        ('cores_per_processor', False, 'int', 'child::cim:machineCoresPerProcessor'),
        ('description', False, 'unicode', 'child::cim:machineDescription'),
        ('interconnect', False, 'unicode', 'child::cim:machineInterconnect/@value'),
        ('libraries', True, 'unicode', 'child::cim:machineLibrary'),
        ('location', False, 'unicode', 'child::cim:machineLocation'),
        ('maximum_processors', False, 'int', 'child::cim:machineMaximumProcessors'),
        ('name', False, 'unicode', 'child::cim:machineName'),
        ('operating_system', False, 'unicode', 'child::cim:machineOperatingSystem/@value'),
        ('processor_type', False, 'unicode', 'child::cim:machineProcessorType/@value'),
        ('system', False, 'unicode', 'child::cim:machineSystem'),
        ('type', False, 'unicode', '@machineType'),
        ('vendor', False, 'unicode', 'child::cim:machineVendor/@value'),
    ]

    return set_attributes(typeset.shared.Machine(), xml, nsmap, decodings)


def decode_machine_compiler_unit(xml, nsmap):
    """Decodes an instance of the following type: machine compiler unit.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.MachineCompilerUnit

    """
    decodings = [
        ('compilers', True, decode_compiler, 'child::cim:compiler'),
        ('machine', False, decode_machine, 'child::cim:machine'),
    ]

    return set_attributes(typeset.shared.MachineCompilerUnit(), xml, nsmap, decodings)


def decode_open_date_range(xml, nsmap):
    """Decodes an instance of the following type: open date range.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.OpenDateRange

    """
    decodings = [
        ('duration', False, 'unicode', 'child::cim:duration'),
        ('end', False, 'datetime.datetime', 'child::cim:endDate'),
        ('start', False, 'datetime.datetime', 'child::cim:startDate'),
    ]

    return set_attributes(typeset.shared.OpenDateRange(), xml, nsmap, decodings)


def decode_perpetual_period(xml, nsmap):
    """Decodes an instance of the following type: perpetual period.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.PerpetualPeriod

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('length', False, 'int', 'child::cim:length'),
        ('range', False, decode_closed_date_range, 'child::cim:range/cim:closedDateRange'),
        ('range', False, decode_open_date_range, 'child::cim:range/cim:openDateRange'),
    ]

    return set_attributes(typeset.shared.PerpetualPeriod(), xml, nsmap, decodings)


def decode_platform(xml, nsmap):
    """Decodes an instance of the following type: platform.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Platform

    """
    decodings = [
        ('contacts', True, decode_responsible_party, 'child::cim:contact'),
        ('description', False, 'unicode', 'child::cim:description'),
        ('long_name', False, 'unicode', 'child::cim:longName'),
        ('meta', False, decode_doc_meta_info, 'self::cim:platform'),
        ('short_name', False, 'unicode', 'child::cim:shortName'),
        ('units', True, decode_machine_compiler_unit, 'child::cim:unit'),
    ]

    return set_attributes(typeset.shared.Platform(), xml, nsmap, decodings)


def decode_property(xml, nsmap):
    """Decodes an instance of the following type: property.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Property

    """
    decodings = [
        ('name', False, 'unicode', 'child::cim:name'),
        ('value', False, 'unicode', 'child::cim:value'),
    ]

    return set_attributes(typeset.shared.Property(), xml, nsmap, decodings)


def decode_real_calendar(xml, nsmap):
    """Decodes an instance of the following type: real calendar.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.RealCalendar

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('length', False, 'int', 'child::cim:length'),
        ('range', False, decode_closed_date_range, 'child::cim:range/cim:closedDateRange'),
        ('range', False, decode_open_date_range, 'child::cim:range/cim:openDateRange'),
    ]

    return set_attributes(typeset.shared.RealCalendar(), xml, nsmap, decodings)


def decode_relationship(xml, nsmap):
    """Decodes an instance of the following type: relationship.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Relationship

    """
    decodings = [
    ]

    return set_attributes(typeset.shared.Relationship(), xml, nsmap, decodings)


def decode_responsible_party(xml, nsmap):
    """Decodes an instance of the following type: responsible party.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.ResponsibleParty

    """
    decodings = [
        ('abbreviation', False, 'unicode', 'child::cim:abbreviation'),
        ('address', False, 'unicode', 'child::gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint'),
        ('address', False, 'unicode', 'child::gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString'),
        ('email', False, 'unicode', 'child::gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress'),
        ('email', False, 'unicode', 'child::gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString'),
        ('individual_name', False, 'unicode', 'child::gmd:individualName'),
        ('individual_name', False, 'unicode', 'child::gmd:individualName/gco:CharacterString'),
        ('organisation_name', False, 'unicode', 'child::gmd:organisationName'),
        ('organisation_name', False, 'unicode', 'child::gmd:organisationName/gco:CharacterString'),
        ('role', False, 'unicode', 'gmd:role/gmd:CI_RoleCode/@codeListValue'),
        ('url', False, 'unicode', 'child::gmd:contactInfo/gmd:CI_Contact/gmd:onlineResource/gmd:CI_OnlineResource/gmd:linkage/gmd:URL'),
    ]

    return set_attributes(typeset.shared.ResponsibleParty(), xml, nsmap, decodings)


def decode_standard(xml, nsmap):
    """Decodes an instance of the following type: standard.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Standard

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('name', False, 'unicode', 'child::cim:name'),
        ('version', False, 'unicode', 'child::cim:version'),
    ]

    return set_attributes(typeset.shared.Standard(), xml, nsmap, decodings)


def decode_standard_name(xml, nsmap):
    """Decodes an instance of the following type: standard name.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.StandardName

    """
    decodings = [
        ('is_open', False, 'bool', '@open'),
        ('standards', True, decode_standard, 'child::cim:standard'),
        ('value', False, 'unicode', '@value'),
    ]

    return set_attributes(typeset.shared.StandardName(), xml, nsmap, decodings)


