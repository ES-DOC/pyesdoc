"""
.. module:: constants.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package constants.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Supported ESDOC encodings.
ENCODING_DICT = 'dict'
ENCODING_JSON = 'json'
ENCODING_XML = 'xml'
ENCODING_HTML = 'html'
METAFOR_CIM_XML_ENCODING = 'xml-metafor-cim-v1'

# Standard ESDOC encodings.
ENCODINGS = (
    ENCODING_DICT,
    ENCODING_HTML,
    ENCODING_JSON,
    ENCODING_XML,
)

# Standard ESDOC file encodings.
ENCODINGS_FILE = (
    ENCODING_JSON,
    ENCODING_XML,
    ENCODING_HTML,
)

# Standard ESDOC http encodings.
ENCODINGS_HTTP = (
    ENCODING_JSON,
    ENCODING_XML,
    ENCODING_HTML,
)

# Custom ESDOC encodings.
ENCODINGS_CUSTOM = (
    METAFOR_CIM_XML_ENCODING,
)

# Custom ESDOC file encodings.
ENCODINGS_FILE_CUSTOM = (
    METAFOR_CIM_XML_ENCODING,
)

# All ESDOC encodings.
ENCODINGS_ALL = set(ENCODINGS + ENCODINGS_CUSTOM)

# Map of standard ESDOC encodings to MIME types.
ENCODING_HTTP_MEDIA_TYPES = {
    ENCODING_JSON : "application/json",
    ENCODING_XML : "application/xml",
    ENCODING_HTML : "text/html"
}

# Latest document version label.
DOC_VERSION_LATEST = 'latest'

# All document versions label.
DOC_VERSION_ALL = 'all'

# Default document encoding.
DEFAULT_ENCODING = 'json'

# Default document project.
DEFAULT_PROJECT = u'--'

# Default document institute.
DEFAULT_INSTITUTE = u'--'

# Default document source.
DEFAULT_SOURCE = u'scripts'

# Document viewer url.
VIEWER_URL_BY_ID = u"index.html?renderMethod=id&project={0}&id={1}&version={2}"

# Cardinality constraint.
CONSTRAINT_TYPE_CARDINALITY = 'cardinality'

# Constant constraint.
CONSTRAINT_TYPE_CONSTANT = 'constant'

# Type constraint.
CONSTRAINT_TYPE_TYPEOF = 'type'

# Regular expression constraint.
CONSTRAINT_TYPE_REGEX = 'regex'

# Set of supported constraint types.
CONSTRAINT_TYPES = {
    CONSTRAINT_TYPE_CARDINALITY,
    CONSTRAINT_TYPE_CONSTANT,
    CONSTRAINT_TYPE_REGEX,
    CONSTRAINT_TYPE_TYPEOF
}

# Cardinality constraint ... 0.0.
CARDINALITY_TYPE_0_0 = '0.0'

# Cardinality constraint ... 0.1.
CARDINALITY_TYPE_0_1 = '0.1'

# Cardinality constraint ... 1.1.
CARDINALITY_TYPE_1_1 = '1.1'

# Cardinality constraint ... 0.N.
CARDINALITY_TYPE_0_N = '0.N'

# Cardinality constraint ... 1.N.
CARDINALITY_TYPE_1_N = '1.N'

# Set of supported cardinality types.
CARDINALITY_TYPES = {
    CARDINALITY_TYPE_0_0,
    CARDINALITY_TYPE_0_1,
    CARDINALITY_TYPE_1_1,
    CARDINALITY_TYPE_0_N,
    CARDINALITY_TYPE_1_N
}
