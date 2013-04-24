"""Exposes set of cim constants.

"""


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

