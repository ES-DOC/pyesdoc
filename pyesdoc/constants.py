# -*- coding: utf-8 -*-

"""
.. module:: constants.py
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
ESDOC_ENCODING_PDF = 'pdf'
METAFOR_CIM_XML_ENCODING = 'xml-metafor-cim-v1'

# Standard ESDOC encodings.
ESDOC_ENCODINGS = (
    ESDOC_ENCODING_DICT,
    ESDOC_ENCODING_HTML,
    ESDOC_ENCODING_JSON,
    ESDOC_ENCODING_PDF,
    ESDOC_ENCODING_XML,
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
    ESDOC_ENCODING_PDF : "application/pdf"
}

# Latest document version label.
ESDOC_DOC_VERSION_LATEST = 'latest'

# All document versions label.
ESDOC_DOC_VERSION_ALL = 'all'

# Default document encoding.
ESDOC_DEFAULT_ENCODING = 'json'

# Default document language.
ESDOC_DEFAULT_LANGUAGE = u'en'

# Default document project.
ESDOC_DEFAULT_PROJECT = u'--'

# Default document institute.
ESDOC_DEFAULT_INSTITUTE = u'--'

# Default document source.
ESDOC_DEFAULT_SOURCE = u'scripts'

# Document viewer url.
ESDOC_VIEWER_URL = u"index.html?renderMethod=id&project={0}&id={1}&version={2}"

