# -*- coding: utf-8 -*-

from pyesdoc.extensions.cim import v1
from pyesdoc.extensions.cim import v2


# Supported cim versions.
_VERSIONS = [v1, v2]


# Supported extenders keyed by document type.
SUPPORTED = {}
for v in _VERSIONS:
    for doc_type, doc_extender in v.SUPPORTED.iteritems():
        SUPPORTED[doc_type] = doc_extender
