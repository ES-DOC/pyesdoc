# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.codecs.dictionary.decoder.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Decodes a document from a python dictionary.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import datetime
import uuid

from pyesdoc import ontologies
from pyesdoc.utils import convert
from pyesdoc.utils import runtime as rt



def _get_doc(obj, doc_type):
    """Returns document.

    """
    if doc_type.type_key != obj['ontology_type_key']:
        doc_type = ontologies.get_type_from_key(obj['ontology_type_key'])
    if doc_type is None:
        raise ValueError('Decoding type is unrecognized')

    return doc_type(), ontologies.get_type_info(doc_type)


def _decode_simple(value, target_type, iterable):
    """Decodes a simple value.

    """
    if iterable:
        return [convert.text_to_typed_value(i, target_type) for i in value]
    return convert.text_to_typed_value(value, target_type)


def _decode(value, doc_type, iterable):
    """Decodes a dictionary.

    """
    def _do(obj):
        # Create doc.
        doc, doc_type_info = _get_doc(obj, doc_type)

        # Set doc attributes.
        for _name, _type, _required, _iterable in doc_type_info:
            # ... set placeholders
            if _name not in obj:
                continue
            # ... set nulls
            elif obj[_name] is None:
                setattr(doc, _name, [] if _iterable else None)
            # ... set simple / complex types
            else:
                decoder = _decode if _type in ontologies.get_types() else _decode_simple
                setattr(doc, _name, decoder(obj[_name], _type, _iterable))

        return doc

    return _do(value) if not iterable else [_do(i) for i in value]


def decode(as_dict):
    """Decodes a document from a dictionary.

    :param dict as_dict: A document in dictionary format.

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Format keys.
    as_dict = convert.dict_keys(as_dict, convert.str_to_underscore_case)
    if 'ontology_type_key' not in as_dict:
        raise KeyError('ontology_type_key is unspecified and therefore the document cannot be decoded.')

    # Get document type.
    doc_type_key = as_dict['ontology_type_key']
    doc_type = ontologies.get_type_from_key(doc_type_key)

    return _decode(as_dict, doc_type, False)
