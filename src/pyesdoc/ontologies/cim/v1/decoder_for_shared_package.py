"""
.. module:: cim.v1.decoder_for_shared_package.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-09-12 17:03:09.111357.

"""

# Module imports.
from decoder_xml_utils import set_attributes
import typeset



def decode_calendar(xml, nsmap):
    """Decodes an instance of the following type: calendar.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Calendar

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('length', False, 'int', 'child::cim:length'),
        ('range', False, decode_closed_date_range, 'child::cim:range/cim:closedDateRange'),
        ('range', False, decode_open_date_range, 'child::cim:range/cim:openDateRange'),
    ]

    return set_attributes(typeset.shared.Calendar(), xml, nsmap, decodings)


def decode_change(xml, nsmap):
    """Decodes an instance of the following type: change.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Change

    """
    decodings = [
        ('author', False, decode_responsible_party, 'child::cim:changeAuthor'),
        ('date', False, 'datetime.datetime', 'child::cim:changeDate'),
        ('description', False, 'str', 'child::cim:description'),
        ('details', True, decode_change_property, 'child::cim:detail'),
        ('name', False, 'str', 'child::cim:name'),
        ('type', False, 'str', 'self::cim:change/@type'),
    ]

    return set_attributes(typeset.shared.Change(), xml, nsmap, decodings)


def decode_change_property(xml, nsmap):
    """Decodes an instance of the following type: change property.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.ChangeProperty

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('id', False, 'str', 'child::cim:id'),
        ('name', False, 'str', 'child::cim:name'),
        ('value', False, 'str', 'child::cim:value'),
    ]

    return set_attributes(typeset.shared.ChangeProperty(), xml, nsmap, decodings)


def decode_citation(xml, nsmap):
    """Decodes an instance of the following type: citation.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Citation

    """
    decodings = [
        ('alternative_title', False, 'str', 'child::gmd:alternateTitle/gco:CharacterString'),
        ('collective_title', False, 'str', 'gmd:collectiveTitle/gco:CharacterString'),
        ('date', False, 'datetime.datetime', 'child::gmd:date/gmd:CI_Date/gmd:date/gco:Date'),
        ('date_type', False, 'str', 'child::gmd:date/gmd:CI_Date/gmd:dateType/gmd:CI_DateTypeCode/@codeListValue'),
        ('location', False, 'str', 'child::gmd:otherCitationDetails/gco:CharacterString'),
        ('title', False, 'str', 'child::gmd:title/gco:CharacterString'),
        ('type', False, 'str', 'child::gmd:presentationForm/gmd:CI_PresentationFormCode/@codeListValue'),
    ]

    return set_attributes(typeset.shared.Citation(), xml, nsmap, decodings)


def decode_closed_date_range(xml, nsmap):
    """Decodes an instance of the following type: closed date range.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.ClosedDateRange

    """
    decodings = [
        ('duration', False, 'str', 'child::cim:duration'),
        ('end', False, 'datetime.datetime', 'child::cim:endDate'),
        ('start', False, 'datetime.datetime', 'child::cim:startDate'),
    ]

    return set_attributes(typeset.shared.ClosedDateRange(), xml, nsmap, decodings)


def decode_compiler(xml, nsmap):
    """Decodes an instance of the following type: compiler.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Compiler

    """
    decodings = [
        ('environment_variables', False, 'str', 'child::cim:compilerEnvironmentVariables'),
        ('language', False, 'str', 'child::cim:compilerLanguage'),
        ('name', False, 'str', 'child::cim:compilerName'),
        ('options', False, 'str', 'child::cim:compilerOptions'),
        ('type', False, 'str', 'child::cim:compilerType'),
        ('version', False, 'str', 'child::cim:compilerVersion'),
    ]

    return set_attributes(typeset.shared.Compiler(), xml, nsmap, decodings)


def decode_daily_360(xml, nsmap):
    """Decodes an instance of the following type: daily 360.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Daily360

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('length', False, 'int', 'child::cim:length'),
        ('range', False, decode_closed_date_range, 'child::cim:range/cim:closedDateRange'),
        ('range', False, decode_open_date_range, 'child::cim:range/cim:openDateRange'),
    ]

    return set_attributes(typeset.shared.Daily360(), xml, nsmap, decodings)


def decode_data_source(xml, nsmap):
    """Decodes an instance of the following type: data source.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.DataSource

    """
    decodings = [
    ]

    return set_attributes(typeset.shared.DataSource(), xml, nsmap, decodings)


def decode_date_range(xml, nsmap):
    """Decodes an instance of the following type: date range.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.DateRange

    """
    decodings = [
        ('duration', False, 'str', 'child::cim:duration'),
    ]

    return set_attributes(typeset.shared.DateRange(), xml, nsmap, decodings)


def decode_doc_genealogy(xml, nsmap):
    """Decodes an instance of the following type: doc genealogy.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.DocGenealogy

    """
    decodings = [
        ('relationships', True, decode_doc_relationship, 'child::cim:relationship/cim:documentRelationship'),
    ]

    return set_attributes(typeset.shared.DocGenealogy(), xml, nsmap, decodings)


def decode_doc_info(xml, nsmap):
    """Decodes an instance of the following type: doc info.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.DocInfo

    """
    decodings = [
        ('author', False, decode_responsible_party, 'child::cim:documentAuthor'),
        ('create_date', False, 'datetime.datetime', 'child::cim:documentCreationDate'),
        ('external_ids', True, decode_standard_name, 'child::cim:externalID'),
        ('genealogy', False, decode_doc_genealogy, 'child::cim:documentGenealogy'),
        ('id', False, 'uuid.UUID', 'child::cim:documentID'),
        ('version', False, 'int', 'child::cim:documentVersion'),
    ]

    return set_attributes(typeset.shared.DocInfo(), xml, nsmap, decodings)


def decode_doc_reference(xml, nsmap):
    """Decodes an instance of the following type: doc reference.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.DocReference

    """
    decodings = [
        ('changes', True, decode_change, 'child::cim:change'),
        ('description', False, 'str', 'child::cim:description'),
        ('external_id', False, 'str', 'child::cim:externalID'),
        ('id', False, 'uuid.UUID', 'child::cim:id'),
        ('name', False, 'str', 'child::cim:name'),
        ('type', False, 'str', 'child::cim:type'),
        ('version', False, 'str', 'child::cim:version'),
    ]

    return set_attributes(typeset.shared.DocReference(), xml, nsmap, decodings)


def decode_doc_relationship(xml, nsmap):
    """Decodes an instance of the following type: doc relationship.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.DocRelationship

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('direction', False, 'str', 'self::cim:documentRelationship/@direction'),
        ('target', False, decode_doc_relationship_target, 'child::cim:target'),
        ('type', False, 'str', 'self::cim:documentRelationship/@type'),
    ]

    return set_attributes(typeset.shared.DocRelationship(), xml, nsmap, decodings)


def decode_doc_relationship_target(xml, nsmap):
    """Decodes an instance of the following type: doc relationship target.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.DocRelationshipTarget

    """
    decodings = [
        ('reference', False, decode_doc_reference, 'child::cim:reference'),
    ]

    return set_attributes(typeset.shared.DocRelationshipTarget(), xml, nsmap, decodings)


def decode_license(xml, nsmap):
    """Decodes an instance of the following type: license.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.License

    """
    decodings = [
    ]

    return set_attributes(typeset.shared.License(), xml, nsmap, decodings)


def decode_machine(xml, nsmap):
    """Decodes an instance of the following type: machine.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Machine

    """
    decodings = [
        ('cores_per_processor', False, 'int', 'child::cim:machineCoresPerProcessor'),
        ('description', False, 'str', 'child::cim:machineDescription'),
        ('interconnect', False, 'str', 'child::cim:machineInterconnect/@value'),
        ('libraries', True, 'str', 'child::cim:machineLibrary'),
        ('location', False, 'str', 'child::cim:machineLocation'),
        ('maximum_processors', False, 'int', 'child::cim:machineMaximumProcessors'),
        ('name', False, 'str', 'child::cim:machineName'),
        ('operating_system', False, 'str', 'child::cim:machineOperatingSystem/@value'),
        ('processor_type', False, 'str', 'child::cim:machineProcessorType/@value'),
        ('system', False, 'str', 'child::cim:machineSystem'),
        ('type', False, 'str', '@machineType'),
        ('vendor', False, 'str', 'child::cim:machineVendor/@value'),
    ]

    return set_attributes(typeset.shared.Machine(), xml, nsmap, decodings)


def decode_machine_compiler_unit(xml, nsmap):
    """Decodes an instance of the following type: machine compiler unit.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

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

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.OpenDateRange

    """
    decodings = [
        ('duration', False, 'str', 'child::cim:duration'),
        ('end', False, 'datetime.datetime', 'child::cim:endDate'),
        ('start', False, 'datetime.datetime', 'child::cim:startDate'),
    ]

    return set_attributes(typeset.shared.OpenDateRange(), xml, nsmap, decodings)


def decode_perpetual_period(xml, nsmap):
    """Decodes an instance of the following type: perpetual period.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.PerpetualPeriod

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('length', False, 'int', 'child::cim:length'),
        ('range', False, decode_closed_date_range, 'child::cim:range/cim:closedDateRange'),
        ('range', False, decode_open_date_range, 'child::cim:range/cim:openDateRange'),
    ]

    return set_attributes(typeset.shared.PerpetualPeriod(), xml, nsmap, decodings)


def decode_platform(xml, nsmap):
    """Decodes an instance of the following type: platform.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Platform

    """
    decodings = [
        ('contacts', True, decode_responsible_party, 'child::cim:contact'),
        ('description', False, 'str', 'child::cim:description'),
        ('doc_info', False, decode_doc_info, 'self::cim:platform'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('units', True, decode_machine_compiler_unit, 'child::cim:unit'),
    ]

    return set_attributes(typeset.shared.Platform(), xml, nsmap, decodings)


def decode_property(xml, nsmap):
    """Decodes an instance of the following type: property.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Property

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
        ('value', False, 'str', 'child::cim:value'),
    ]

    return set_attributes(typeset.shared.Property(), xml, nsmap, decodings)


def decode_real_calendar(xml, nsmap):
    """Decodes an instance of the following type: real calendar.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.RealCalendar

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('length', False, 'int', 'child::cim:length'),
        ('range', False, decode_closed_date_range, 'child::cim:range/cim:closedDateRange'),
        ('range', False, decode_open_date_range, 'child::cim:range/cim:openDateRange'),
    ]

    return set_attributes(typeset.shared.RealCalendar(), xml, nsmap, decodings)


def decode_relationship(xml, nsmap):
    """Decodes an instance of the following type: relationship.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Relationship

    """
    decodings = [
    ]

    return set_attributes(typeset.shared.Relationship(), xml, nsmap, decodings)


def decode_responsible_party(xml, nsmap):
    """Decodes an instance of the following type: responsible party.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.ResponsibleParty

    """
    decodings = [
        ('abbreviation', False, 'str', 'child::cim:abbreviation'),
        ('contact_info', False, decode_responsible_party_contact_info, 'child::gmd:contactInfo/gmd:CI_Contact'),
        ('individual_name', False, 'str', 'child::gmd:individualName/gco:CharacterString'),
        ('organisation_name', False, 'str', 'child::gmd:organisationName/gco:CharacterString'),
        ('role', False, 'str', 'gmd:role/gmd:CI_RoleCode/@codeListValue'),
    ]

    return set_attributes(typeset.shared.ResponsibleParty(), xml, nsmap, decodings)


def decode_responsible_party_contact_info(xml, nsmap):
    """Decodes an instance of the following type: responsible party contact info.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.ResponsiblePartyContactInfo

    """
    decodings = [
        ('address', False, 'str', 'child::gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString'),
        ('email', False, 'str', 'child::gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString'),
        ('url', False, 'str', 'child::gmd:onlineResource/gmd:CI_OnlineResource/gmd:linkage/gmd:URL'),
    ]

    return set_attributes(typeset.shared.ResponsiblePartyContactInfo(), xml, nsmap, decodings)


def decode_standard(xml, nsmap):
    """Decodes an instance of the following type: standard.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.Standard

    """
    decodings = [
        ('description', False, 'str', 'child::cim:description'),
        ('name', False, 'str', 'child::cim:name'),
        ('version', False, 'str', 'child::cim:version'),
    ]

    return set_attributes(typeset.shared.Standard(), xml, nsmap, decodings)


def decode_standard_name(xml, nsmap):
    """Decodes an instance of the following type: standard name.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.shared.StandardName

    """
    decodings = [
        ('is_open', False, 'bool', '@open'),
        ('standards', True, decode_standard, 'child::cim:standard'),
        ('value', False, 'str', '@value'),
    ]

    return set_attributes(typeset.shared.StandardName(), xml, nsmap, decodings)


