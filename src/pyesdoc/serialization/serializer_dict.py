"""
.. module:: pyesdoc.serialization.serializer_dict.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes document dictionary serialization functions.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""
# Module imports.
import datetime
import uuid

from dateutil import parser as date_parser

from .. import (
    ontologies,
    utils
    )


# Set of ontology types.
_TYPES = ontologies.get_types()

cim = ontologies.cim


def _is_encodable(obj):
    """Returns flag indicating whether an object is encodable or not."""
    return obj.__class__ in _TYPES


def _encode(obj):
    """Encodes an onbject to a deep dictionary."""
    result = {
        'doc_type_key' : obj.__class__.type_key
    }

    for k, v in obj.__dict__.items():
        try:
            iter(v)
        except TypeError:
            result[k] = _encode(v) if _is_encodable(v) else v
        else:
            if v.__class__ in (str,):
                result[k] = v
            else:
                result[k] = map(lambda i : _encode(i) if _is_encodable(i) else i, v)

    return result


def _decode_scalar(v, type, iterable):
    """Decodes a scalar value."""
    def _do(s):
        s = s.encode('utf-8') if isinstance(s, unicode) else str(s)
            
        if type in (datetime.datetime, datetime.date, datetime.time):
            return date_parser.parse(s)
        elif type is uuid.UUID:
            return uuid.UUID(s)
        elif type is bool:
            if s.lower() in ("yes", "true", "t", "1", "y"):
                return True
            return False
        else:
            try:
                return type(s)
            except Error as e:
                print "Scalar decoding error", s, type, iterable

    return map(lambda i : _do(i), v) if iterable else _do(v)


def _decode(v, type, iterable):
    """Decodes a dictionary value."""
        
    def _do(d):
        # Set doc type.
        doc_type = type
        if type.type_key != d['doc_type_key']:
            doc_type = ontologies.get_type_from_key(d['doc_type_key'])
        if doc_type is None:
            utils.runtime.raise_error('Decoding type is unrecognized')
    
        # Create doc.
        doc = doc_type()

        # Set doc attributes.
        for _name, _type, _required, _iterable in ontologies.get_type_info(doc_type):
            if _name not in d:
                continue
            elif d[_name] is None:
                setattr(doc, _name, [] if _iterable else None)
            elif _type in _TYPES:
                setattr(doc, _name, _decode(d[_name], _type, _iterable))
            else:
                setattr(doc, _name, _decode_scalar(d[_name], _type, _iterable))

        return doc

    return _do(v) if not iterable else map(lambda i : _do(i), v)


def encode(doc):
    """Encodes a document to a dictionary.

    :param doc: Document being encoded.
    :type doc: object.

    :returns: A dictionary representation of a document.
    :rtype: dict

    """
    return _encode(doc)


def decode(repr):
    """Decodes a document from a dictionary.

    :param as_dict: Document dictionary representation.
    :type as_dict: dict

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Format dictionary keys.
    as_dict = utils.convert_dict_keys(repr, utils.convert_to_underscore_case)

    # Get target type.
    o, v, p, t = as_dict['doc_type_key'].split('.')
    type = ontologies.get_type(o, v, p, t)

    return _decode(as_dict, type, False)
