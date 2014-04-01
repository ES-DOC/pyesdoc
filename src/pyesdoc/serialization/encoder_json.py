"""
.. module:: pyesdoc.utils.encoder_json.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: JSON encoder from document.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
from . import encoder_dict
from .. utils import convert



def encode(doc):
    """Encodes a document to a json str.

    :param doc: Document being encoded.
    :type doc: object

    :returns: A json representation of a document.
    :rtype: str

    """
    # Encode as dictionary.
    d = encoder_dict.encode(doc)

    # Format dictionary keys.
    d = convert.dict_keys(d, convert.str_to_camel_case)

    # Convert dictionary to json.
    return convert.dict_to_json(d)