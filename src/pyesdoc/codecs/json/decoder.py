# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.codecs.json.decoder.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Decodes a document from a JSON text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc.codecs.dictionary import decoder as dict_decoder
from pyesdoc.utils import convert



# Default document encoding.
_UNICODE = "utf-8"



def decode(as_json):
    """Decodes a document from a UTF-8 encoded json text blob.

    :param as_json: Document json representation.
    :type as_json: unicode | str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Convert to dictionary.
    d = convert.json_to_dict(as_json.decode(_UNICODE))

    # Format dictionary keys.
    d = convert.dict_keys(d, convert.str_to_underscore_case)

    # Decode from dictionary.
    return dict_decoder.decode(d)
