"""
.. module:: pyesdoc.utils.serializer_json.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes document json serialization functions.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
from .. utils import (
    convert,
    serializer_dict
    )



def encode(doc):
    """Encodes a document to a json str.

    :param doc: Document being encoded.
    :type doc: object

    :returns: A json representation of a document.
    :rtype: str

    """
    # Encode as dictionary.
    as_dict = serializer_dict.encode(doc)

    # Format dictionary keys.
    as_dict = convert.dict_keys(as_dict, convert.str_to_camel_case)

    # Convert dictionary to json.
    return convert.dict_to_json(as_dict)


def decode(repr):
    """Decodes a document from a json string.

    :param repr: Document json representation.
    :type repr: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Convert to dictionary.
    as_dict = convert.json_to_dict(repr)

    # Format dictionary keys.
    as_dict = convert.dict_keys(as_dict, convert.str_to_underscore_case)

    # Decode from dictionary.
    return serializer_dict.decode(as_dict)
