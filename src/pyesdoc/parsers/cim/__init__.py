# Module imports.
from . import v1


# Supported cim versions.
_versions = [v1]


# Supported parsers keyed by document type.
supported = reduce(lambda x, v: dict(x.items() + v.supported.items()), _versions, {})