"""CIM json encoding functions.

"""

# Module imports.
try:
    import simplejson as json
except ImportError:
    import json

import datetime
import uuid

from pyesdoc.utils.convertors import (
    convert_dict_keys,
    convert_to_pascal_case
    )


class JSONEncoder(json.JSONEncoder):
    """Extends json encoder so as to handle extended types.
    
    """
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat().replace('T', ' ')
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.time):
            return obj.isoformat()
        elif isinstance(obj, uuid.UUID):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


def encode(instance, schema):
    """Encodes an json representation of passed pyesdoc document instance.

    :param instance: pyesdoc document instance.
    :type instance: object

    :param schema: A document schema (e.g. CIM 1.5).
    :type schema: str

    :returns: A json representation of document instance.
    :rtype: str

    """
    # Get dictionary representation of instance.
    d = instance.as_dict()

    # Honour json object attribute naming conventions.
    d = convert_dict_keys(d, convert_to_pascal_case)

    # Encode to json.
    return JSONEncoder().encode(d)

