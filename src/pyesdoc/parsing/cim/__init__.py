# Module imports.
from . import v1


# Supported cim versions.
_VERSIONS = [v1]


# Supported parsers keyed by document type.
SUPPORTED = {}
for v in _VERSIONS:
    for doc_type, doc_parser in v.SUPPORTED.iteritems():
        SUPPORTED[doc_type] = doc_parser
