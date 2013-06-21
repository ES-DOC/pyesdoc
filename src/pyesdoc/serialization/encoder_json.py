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


def encode(ctx):
    """Encodes an json representation of passed pyesdoc document instance.

    :param ctx: Serialization context info.
    :type ctx: namedtuple

    """
    # Get dictionary representation of instance.
    d = ctx.instance.as_dict()

    # Honour json object attribute naming conventions.
    d = convert_dict_keys(d, convert_to_pascal_case)

    # Encode to json.
    ctx.representation = JSONEncoder().encode(d)
