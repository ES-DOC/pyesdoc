"""
.. module:: constants.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package constants.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Supported ESDOC encodings.
ESDOC_ENCODING_DICT = 'dict'
ESDOC_ENCODING_JSON = 'json'
ESDOC_ENCODING_XML = 'xml'
ESDOC_ENCODING_HTML = 'html'
METAFOR_CIM_XML_ENCODING = 'xml-metafor-cim-v1'

# Standard ESDOC encodings.
ESDOC_ENCODINGS = (
    ESDOC_ENCODING_DICT,
    ESDOC_ENCODING_JSON,
    ESDOC_ENCODING_XML,
    ESDOC_ENCODING_HTML,
)

# Standard ESDOC file encodings.
ESDOC_ENCODINGS_FILE = (
    ESDOC_ENCODING_JSON,
    ESDOC_ENCODING_XML,
    ESDOC_ENCODING_HTML,
)

# Custom ESDOC encodings.
ESDOC_ENCODINGS_CUSTOM = (
    METAFOR_CIM_XML_ENCODING,
)

# Custom ESDOC file encodings.
ESDOC_ENCODINGS_FILE_CUSTOM = (
    METAFOR_CIM_XML_ENCODING,
)

# Map of standard ESDOC encodings to MIME types.
ESDOC_ENCODING_HTTP_MEDIA_TYPES = {
    ESDOC_ENCODING_JSON : "application/json",
    ESDOC_ENCODING_XML : "application/xml",
    ESDOC_ENCODING_HTML : "text/html",
}

# Latest document version label.
ESDOC_DOC_VERSION_LATEST = 'latest'

# All document versions label.
ESDOC_DOC_VERSION_ALL = 'all'

# Default language.
ESDOC_DEFAULT_LANGUAGE = 'en'

# Default encoding.
ESDOC_DEFAULT_ENCODING = 'json'