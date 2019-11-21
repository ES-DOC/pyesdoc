"""
.. module:: shared_classes.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 shared package class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def change():
    """A description of [a set of] changes applied at a particular time, by a particular party, to a particular unit of metadata.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('author', 'shared.responsible_party', '0.1'),
            ('date', 'datetime', '0.1'),
            ('description', 'str', '0.1'),
            ('details', 'shared.change_property', '1.N'),
            ('name', 'str', '0.1'),
            ('type', 'shared.change_property_type', '0.1'),
        ],
        'doc_strings': {
            'author': 'The person that made the change.',
            'date': 'The date the change was implemented.',
            'name': 'A mnemonic for describing a particular change.',
        },
        'decodings': [
            ('author', 'child::cim:changeAuthor'),
            ('date', 'child::cim:changeDate'),
            ('description', 'child::cim:description'),
            ('details', 'child::cim:detail'),
            ('name', 'child::cim:name'),
            ('type', 'self::cim:change/@type'),
        ]
    }


def change_property():
    """A description of a single change applied to a single target.  Every ChangeProperty has a description, and may also have a name from a controlled vocabulary and a value.

    """
    return {
        'type': 'class',
        'base': 'shared.property',
        'is_abstract': False,
        'properties': [
            ('description', 'str', '0.1'),
            ('id', 'str', '0.1')
        ],
        'doc_strings': {
            'description': 'A text description of the change.  May be used in addition to, or instead of, the more formal description provided by the "value" attribute.',
        },
        'decodings': [
            ('description', 'child::cim:description'),
            ('id', 'child::cim:id'),
        ]
    }


def citation():
    """An academic reference to published work.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('alternative_title', 'str', '0.1'),
            ('collective_title', 'str', '0.1'),
            ('location', 'str', '0.1'),
            ('date', 'datetime', '0.1'),
            ('date_type', 'str', '0.1'),
            ('organisation', 'str', '0.1'),
            ('role', 'str', '0.1'),
            ('title', 'str', '0.1'),
            ('type', 'str', '0.1'),
        ],
        'decodings': [
            ('alternative_title', 'child::gmd:alternateTitle/gco:CharacterString'),
            ('alternative_title', 'child::gmd:alternateTitle'),
            ('collective_title', 'gmd:collectiveTitle/gco:CharacterString'),
            ('collective_title', 'gmd:collectiveTitle'),
            ('date', 'child::gmd:date/gmd:CI_Date/gmd:date/gco:Date'),
            ('date_type', 'child::gmd:date/gmd:CI_Date/gmd:dateType/gmd:CI_DateTypeCode/@codeListValue'),
            ('location', 'child::gmd:otherCitationDetails/gco:CharacterString'),
            ('location', 'child::gmd:otherCitationDetails'),
            ('title', 'child::gmd:title/gco:CharacterString'),
            ('title', 'child::gmd:title'),
            ('type', 'child::gmd:presentationForm/gmd:CI_PresentationFormCode/@codeListValue'),
        ]
    }


def compiler():
    """A description of a compiler used on a particular platform.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('environment_variables', 'str', '0.1'),
            ('language', 'str', '0.1'),
            ('name', 'str', '1.1'),
            ('options', 'str', '0.1'),
            ('type', 'shared.compiler_type', '0.1'),
            ('version', 'str', '1.1'),
        ],
        'doc_strings': {
            'environment_variables': 'The set of environment_variables used during compilation (recorded here as a single string rather than separate elements)',
            'options': 'The set of options used during compilation (recorded here as a single string rather than separate elements)',
        },
        'decodings': [
            ('environment_variables', 'child::cim:compilerEnvironmentVariables'),
            ('language', 'child::cim:compilerLanguage'),
            ('name', 'child::cim:compilerName'),
            ('options', 'child::cim:compilerOptions'),
            ('type', 'child::cim:compilerType'),
            ('version', 'child::cim:compilerVersion'),
        ]
    }


def data_source():
    """A DataSource can be realised by either a DataObject (file), a DataContent (variable), a Component (model), or a ComponentProperty (variable); all of those can supply data.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': True,
        'properties': [
            ('purpose', 'shared.data_purpose', '0.1'),
        ]
    }


def license():
    """A description of a license restricting access to a unit of data or software.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('name', 'str', '0.1'),
            ('contact', 'str', '0.1'),
            ('description', 'str', '0.1'),
            ('is_unrestricted', 'bool', '0.1'),
        ],
        'doc_strings': {
            'name': 'The name that the license goes by (ie: "GPL")',
            'contact': 'The point of contact for access to this artifact; may be either a person or an institution.',
            'description': 'A textual description of the license; might be the full text of the license, more likely to be a brief summary',
            'is_unrestricted': 'If unrestricted="true" then the artifact can be downloaded with no restrictions (ie: there are no administrative steps for the user to deal with; code or data can be downloaded and used directly).',
        }
    }


def machine():
    """A description of a machine used by a particular platform.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('cores_per_processor', 'int', '0.1'),
            ('description', 'str', '0.1'),
            ('interconnect', 'shared.interconnect_type', '0.1'),
            ('name', 'str', '1.1'),
            ('libraries', 'str', '0.N'),
            ('location', 'str', '0.1'),
            ('maximum_processors', 'int', '0.1'),
            ('operating_system', 'shared.operating_system_type', '0.1'),
            ('system', 'str', '0.1'),
            ('type', 'shared.machine_type', '0.1'),
            ('vendor', 'shared.machine_vendor_type', '0.1'),
            ('processor_type', 'shared.processor_type', '0.1'),
        ],
        'doc_strings': {
            'libraries': 'The libraries residing on this machine.',
        },
        'decodings': [
            ('cores_per_processor', 'child::cim:machineCoresPerProcessor'),
            ('description', 'child::cim:machineDescription'),
            ('interconnect', 'child::cim:machineInterconnect/@value'),
            ('name', 'child::cim:machineName'),
            ('libraries', 'child::cim:machineLibrary'),
            ('location', 'child::cim:machineLocation'),
            ('maximum_processors', 'child::cim:machineMaximumProcessors'),
            ('operating_system', 'child::cim:machineOperatingSystem/@value'),
            ('system', 'child::cim:machineSystem'),
            ('type', '@machineType'),
            ('vendor', 'child::cim:machineVendor/@value'),
            ('processor_type', 'child::cim:machineProcessorType/@value'),
        ]
    }


def machine_compiler_unit():
    """Associates a machine with a [set of] compilers.  This is a separate class in case a platform needs to specify more than one machine/compiler pair.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('compilers', 'shared.compiler', '0.N'),
            ('machine', 'shared.machine', '1.1'),
        ],
        'decodings': [
            ('compilers', 'child::cim:compiler'),
            ('machine', 'child::cim:machine'),
        ]
    }


def platform():
    """A platform is a description of resources used to deploy a component/simulation.  A platform pairs a machine with a (set of) compilers.  There is also a point of contact for the platform.

    """
    return {
        'type': 'class',
        'name': 'platform',
        'base': None,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('contacts', 'shared.responsible_party', '0.N'),
            ('description', 'str', '0.1'),
            ('long_name', 'str', '0.1'),
            ('short_name', 'str', '1.1'),
            ('units', 'shared.machine_compiler_unit', '1.N'),
        ],
        'decodings': [
            ('meta', 'self::cim:platform'),
            ('contacts', 'child::cim:contact'),
            ('description', 'child::cim:description'),
            ('long_name', 'child::cim:longName'),
            ('short_name', 'child::cim:shortName'),
            ('units', 'child::cim:unit'),
        ]
    }


def property():
    """A simple name/value pair representing a property of some entity or other.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('name', 'str', '0.1'),
            ('value', 'str', '0.1'),
        ],
        'decodings': [
            ('name', 'child::cim:name'),
            ('value', 'child::cim:value'),
        ]
    }


def relationship():
    """A record of a relationship between one document and another. This class is abstract; specific document types must specialise this class for their relationshipTypes to be included in a document\'s genealogy.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': True,
        'properties': [
            ('description', 'str', '0.1')
        ]
    }


def responsible_party():
    """A person/organsiation responsible for some aspect of a climate science artefact.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('abbreviation', 'str', '0.1'),
            ('address', 'str', '0.1'),
            ('email', 'str', '0.1'),
            ('individual_name', 'str', '0.1'),
            ('organisation_name', 'str', '0.1'),
            ('role', 'str', '0.1'),
            ('url', 'str', '0.1'),
        ],
        'decodings': [
            ('abbreviation', 'child::cim:abbreviation'),
            ('address', 'child::gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint/gco:CharacterString'),
            ('address', 'child::gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:deliveryPoint'),
            ('email', 'child::gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress/gco:CharacterString'),
            ('email', 'child::gmd:contactInfo/gmd:CI_Contact/gmd:address/gmd:CI_Address/gmd:electronicMailAddress'),
            ('individual_name', 'child::gmd:individualName/gco:CharacterString'),
            ('individual_name', 'child::gmd:individualName'),
            ('organisation_name', 'child::gmd:organisationName/gco:CharacterString'),
            ('organisation_name', 'child::gmd:organisationName'),
            ('role', 'gmd:role/gmd:CI_RoleCode/@codeListValue'),
            ('url', 'child::gmd:contactInfo/gmd:CI_Contact/gmd:onlineResource/gmd:CI_OnlineResource/gmd:linkage/gmd:URL'),
        ]
    }


def standard():
    """Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('name', 'str', '1.1'),
            ('version', 'str', '0.1'),
            ('description', 'str', '0.1'),
        ],
        'doc_strings': {
            'name': 'The name of the standard',
            'version': 'The version of the standard',
            'description': 'The version of the standard'
        },
        'decodings': [
            ('name', 'child::cim:name'),
            ('version', 'child::cim:version'),
            ('description', 'child::cim:description'),
        ]
    }


def standard_name():
    """Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('is_open', 'bool', '1.1'),
            ('value', 'str', '1.1'),
            ('standards', 'shared.standard', '0.N'),
        ],
        'doc_strings': {
            'standards': 'Details of the standard being used.'
        },
        'decodings': [
            ('is_open', '@open'),
            ('value', '@value'),
            ('standards', 'child::cim:standard'),
        ]
    }


