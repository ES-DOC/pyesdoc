"""
.. module:: pyesdoc.utils.decoder_dict.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Document decoder from dictionary.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import datetime
import uuid

from dateutil import parser as date_parser

from .. import ontologies
from .. utils import (
    convert,
    runtime as rt
    )



# Set of ontology types.
_TYPES = ontologies.get_types()


def _get_doc(d, doc_type):
    """Returns document."""
    if doc_type.type_key != d['ontology_type_key']:
        doc_type = ontologies.get_type_from_key(d['ontology_type_key'])
    if doc_type is None:
        rt.raise_error('Decoding type is unrecognized')

    return doc_type(), ontologies.get_type_info(doc_type)


def _decode_simple(v, type, iterable):
    """Decodes a simple value."""
    if iterable:
        return map(lambda i : convert.str_to_typed_value(i, type), v)
    else:
        return convert.str_to_typed_value(v, type)


def _decode(v, type, iterable):
    """Decodes a dictionary."""        
    def _do(d):
        # Create doc.
        doc, doc_type_info = _get_doc(d, type)

        # Set doc attributes.
        for _name, _type, _required, _iterable in doc_type_info:
            # ... set placeholders
            if _name not in d:
                continue
            # ... set nulls
            elif d[_name] is None:
                setattr(doc, _name, [] if _iterable else None)
            # ... set simple / complex types
            else:
                decoder = _decode if _type in _TYPES else _decode_simple
                setattr(doc, _name, decoder(d[_name], _type, _iterable))

        return doc

    return _do(v) if not iterable else map(lambda i : _do(i), v)


def decode(d):
    """Decodes a document from a dictionary.

    :param d: A document in dictionary format.
    :type d: dict

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Defensive programming.
    if not isinstance(d, dict):
        rt.raise_error('Dictionary is unspecified and therefore the document cannot be decoded.')

    # Format keys.
    d = convert.dict_keys(d, convert.str_to_underscore_case)
    if 'ontology_type_key' not in d:
        rt.raise_error('Ontology type key is unspecified and therefore the document cannot be decoded.')

    # Get document type.
    o, v, p, t = d['ontology_type_key'].split('.')
    doc_type = ontologies.get_type(o, v, p, t)

    return _decode(d, doc_type, False)
    