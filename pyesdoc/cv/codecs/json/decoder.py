# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv.codecs.json.decoder.py

   :copyright: @2013 Earth System Documentation (https://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Decodes a term from a JSON text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc.cv.codecs.dictionary import decoder as dict_decoder
from pyesdoc.cv.utils import convert



def decode(as_json):
    """Decodes a document from a UTF-8 encoded json text blob.

    :param unicode as_xml: Term JSON representation.

    :returns: A term instance.
    :rtype: pyesdoc.cv.Term

    """
    # Convert to unicode.
    as_json = convert.str_to_unicode(as_json)

    # Convert to dictionary.
    as_dict = convert.json_to_dict(as_json, convert.str_to_underscore_case)

    # Decode from dictionary.
    return dict_decoder.decode(as_dict)
