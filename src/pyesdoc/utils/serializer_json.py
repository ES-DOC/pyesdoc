"""
.. module:: pyesdoc.utils.serializer_json.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes document json serialization functions.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""
# Module imports.
import datetime
import json
import uuid

from . import serializer_dict
from . convertors import (
    convert_dict_keys,
    convert_to_camel_case
    )



class _JSONEncoder(json.JSONEncoder):
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
            raise TypeError(repr(obj) + " is not JSON serializable")


def encode(doc):
    """Encodes a document to a json str.

    :param doc: Document being encoded.
    :type doc: object

    :returns: A json representation of a document.
    :rtype: str

    """
    # Convert to dictionary.
    as_dict = serializer_dict.encode(doc)

    # Format dictionary keys.
    as_dict = convert_dict_keys(as_dict, convert_to_camel_case)

    # Return json encoded string.
    return _JSONEncoder().encode(as_dict)


def decode(repr):
    """Decodes a document from a json string.

    :param repr: Document json representation.
    :type repr: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Convert to dictionary.
    as_dict = json.loads(repr)

    # Decode from dictionary.
    return serializer_dict.decode(as_dict)
