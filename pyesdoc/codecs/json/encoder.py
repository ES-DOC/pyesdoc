# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.codecs.json.encoder.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encodes a document as a JSON text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc.codecs.dictionary import encoder as dict_encoder
from pyesdoc.utils import convert



def encode(doc):
    """Encodes a document.

    :param doc: Document being encoded.
    :type doc: object

    :returns: An encoded document representation.
    :rtype: unicode

    """
    # Encode as dictionary.
    d = dict_encoder.encode(doc)

    # Convert dictionary to json.
    return convert.dict_to_json(d, convert.str_to_camel_case)
