"""
.. module:: pyesdoc.utils.ontologies.py
   :copyright: Copyright "Jun 14, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Ontology utility functions.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""

# Set of supported ontologies.
_supported = {
    'CIM' : ['1']
}


def is_supported(name, version):
    """Returns a flag indicating whether the schema is supported.

    :param name: Schema name.
    :type name: str

    :param version: Schema version.
    :type version: str

    :returns: True if the schema is supported, false otherwise.
    :rtype: bool

    """
    name = str(name).upper()
    version = str(version).upper()

    return name in _supported and version in _supported[name]



CIM_V1_5 = {
    'version' : '1.5',
    'encodings' : [
        'json',
        'xml',
        'metafor-xml'
    ],
    'media_types' : [
        'application/json',
        'application/xml',
        'application/vnd.metafor.cim-v15'
    ],
    'defaults' : {
        'encoding' : 'json',
        'language' : 'en',
        'media_type' : 'application/json'
    }
}


# Set of supported CIM schemas.
CIM_SCHEMA_1_5 = '1.5'
CIM_SCHEMAS = [CIM_SCHEMA_1_5]

# Set of supported ESDOC encodings.
ESDOC_ENCODING_JSON = 'json'
ESDOC_ENCODING_XML = 'xml'
CIM_ENCODING_METAFOR_XML = 'metafor-xml'

CIM_ENCODINGS = [
    ESDOC_ENCODING_JSON,
    ESDOC_ENCODING_XML,
    CIM_ENCODING_METAFOR_XML,
]

# Default encoding, language, schema.
CIM_DEFAULT_ENCODING = ESDOC_ENCODING_XML
CIM_DEFAULT_LANGUAGE = 'en'
CIM_DEFAULT_SCHEMA = CIM_SCHEMA_1_5



def get_cim_media_type(version, encoding):
    """
    Derives cim media type from passed version / encoding.

    Keyword Arguments:
    version - version of cim schema.
    encoding - cim document encoding.
    """
    version = version.replace('.', '')
    mt = 'application/vnd.metafor.cim-v{0}+{1}'
    mt = mt.format(version, encoding)

    return mt




"""Exposes set of cim constants.

"""


# Set of supported CIM schemas.
CIM_SCHEMA_1_5 = '1.5'
CIM_SCHEMAS = [
    CIM_SCHEMA_1_5
]

# Supported CIM xml schemas.
CIM_XML_1_5_SCHEMA = 'http://www.purl.org/org/esmetadata/cim/1.5/schemas'
CIM_XML_1_5_XSD = 'http://www.purl.org/org/esmetadata/cim/1.5/schemas/cim.xsd'

# Set of supported CIM encodings.
CIM_ENCODING_JSON = 'json'
CIM_ENCODING_XML = 'xml'
CIM_ENCODINGS = [
    CIM_ENCODING_JSON,
    CIM_ENCODING_XML,
]

# Set of standard representations to be decoded automatically.
CIM_STANDARD_REPRESENTATIONS = [
    (CIM_SCHEMA_1_5, CIM_ENCODING_JSON)
]

# Default encoding, language, schema.
CIM_DEFAULT_ENCODING = CIM_ENCODING_JSON
CIM_DEFAULT_LANGUAGE = 'en'
CIM_DEFAULT_SCHEMA = CIM_SCHEMA_1_5

# Set of supported CIM media types.
CIM_MEDIA_TYPE = "application/vnd.metafor.cim"
CIM_MEDIA_TYPE_V15 = CIM_MEDIA_TYPE + "-v15"
CIM_MEDIA_TYPE_V15_JSON = CIM_MEDIA_TYPE_V15 + "+json"
CIM_MEDIA_TYPE_V15_XML = CIM_MEDIA_TYPE_V15 + "+xml"
CIM_MEDIA_TYPES = [
    CIM_MEDIA_TYPE_V15_JSON,
    CIM_MEDIA_TYPE_V15_XML,
]

METAFOR_MEDIA_TYPE_CIM_V15 = "application/vnd.esdoc.cim-v1.5"
METAFOR_MEDIA_TYPE_CIM_V15_XML = METAFOR_MEDIA_TYPE_CIM_V15 + '+xml'

ESDOC_MEDIA_TYPE_CIM_V15 = "application/vnd.esdoc.cim-v1.5"
ESDOC_MEDIA_TYPE_CIM_V15_XML = ESDOC_MEDIA_TYPE_CIM_V15 + "+xml"
ESDOC_MEDIA_TYPE_CIM_V15_JSON = ESDOC_MEDIA_TYPE_CIM_V15 + "+json"


# Token for latest version of a document.
CIM_DOC_VERSION_LATEST = 'latest'

# Default xml encoding.
CIM_UNICODE = 'utf-8'




