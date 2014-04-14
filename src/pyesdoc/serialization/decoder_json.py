"""
.. module:: pyesdoc.utils.decoder_json.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Document decoder from json.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
from . import decoder_dict
from .. utils import convert



def decode(as_json):
    """Decodes a document from a json string.

    :param as_json: Document json representation.
    :type as_json: unicode | str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Convert strings (assume are utf-8 encoded).
    if isinstance(as_json, str):
        as_json = as_json.decode("utf-8")

    # Convert to dictionary.
    d = convert.json_to_dict(as_json)

    # Format dictionary keys.
    d = convert.dict_keys(d, convert.str_to_underscore_case)

    # Decode from dictionary.
    return decoder_dict.decode(d)