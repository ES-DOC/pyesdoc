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



def _encode(obj):
    """Encodes an onbject to a deep dictionary."""
    def is_encodable(i):
        return i.__class__ in _TYPES

    d = obj.__dict__

    for k, v in d.items():
        try:
            iter(v)
        except TypeError:
            d[k] = _encode(v) if is_encodable(v) else v
        else:
            if v.__class__ in (str,):
                d[k] = v
            else:
                d[k] = map(lambda i : _encode(i) if is_encodable(i) else i, v)

    return d


def encode(doc):
    """Encodes a document to a dictionary.

    :param doc: Document being encoded.
    :type doc: object.

    :returns: A dictionary representation of a document.
    :rtype: dict

    """
    # Get object dictionary.
    d = _encode(doc)

    # Inject type info for use when decoding.
    d['esdoc'] = doc.__class__.type_key

    return d


def _decode_scalar(v, type, iterable):
    """Decodes a scalar value."""
    def _decode(sv):
        sv = sv.encode('utf-8') if isinstance(sv, unicode) else str(sv)
            
        if type in (datetime.datetime, datetime.date, datetime.time):
            return date_parser.parse(sv)
        elif type is uuid.UUID:
            return uuid.UUID(sv)
        else:
            try:
                return type(sv)
            except Error as e:
                print "Scalar decoding error", sv, type, iterable

    return map(lambda i : _decode(i), v) if iterable else _decode(v)


def _decode_dict(v, type, iterable=False):
    """Decodes a dictionary value."""
    def _decode(dv):
        doc = type()

        for _name, _type, _is_required, _is_iterable in ontologies.get_type_info(type):
            if _name not in dv:
                continue
            elif dv[_name] is None:
                setattr(doc, _name, [] if iterable else None)
            elif _type in _TYPES:
                setattr(doc, _name, _decode_dict(dv[_name], _type, _is_iterable))
            else:
                setattr(doc, _name, _decode_scalar(dv[_name], _type, _is_iterable))
        
        return doc

    return _decode(v) if not iterable else map(lambda i : _decode(i), v)


def decode(as_dict):
    """Decodes a document from a dictionary.

    :param as_dict: Document dictionary representation.
    :type as_dict: dict

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Format dictionary keys.
    as_dict = utils.convert_dict_keys(as_dict, utils.convert_to_underscore_case)

    # Get target type.
    o, v, p, t = as_dict['esdoc'].split('.')
    type = ontologies.get_type(o, v, p, t)

    return _decode_dict(as_dict, type)
