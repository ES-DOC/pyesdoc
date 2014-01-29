"""
.. module:: pyesdoc.utils.serializer_xml.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes document xml serialization functions.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import datetime
import uuid
import xml.etree.ElementTree as ET

from dateutil import parser as date_parser

from .. import ontologies
from . import runtime as rt
from . import serializer_dict
from . convertors import (
    convert_dict_keys,
    convert_to_camel_case
    )



# Default XML document encoding.
_UNICODE = "utf-8"

# Mappings between collection name suffixes and collection item suffixes.
_suffix_maps = (
    ('ies', 'y'),
    ('List', ''),
    ('s', ''),
)

# Set of ontology types.
_TYPES = ontologies.get_types()



def _get_item_tag(tag):
    "Returns tag name of a collection item."
    for suffix, replacement in _suffix_maps:
        if tag.endswith(suffix):
            return tag[0:len(tag) - len(suffix)] + replacement
        
    return tag + 'Item'


def _decode_scalar(sv, type, iterable):
    """Decodes a scalar value."""
    def _do(s):
        # None if empty value.
        if not len(s):
            return None

        # Encode.
        s = s.encode('utf-8') if isinstance(s, unicode) else str(s)

        # Decode according to type:
        # ... date
        if type in (datetime.datetime, datetime.date, datetime.time):
            return date_parser.parse(s)
        # ... uuid
        elif type is uuid.UUID:
            return uuid.UUID(s)
        # ... boolean
        elif type is bool:
            if s.lower() in ("yes", "true", "t", "1", "y"):
                return True
            return False
        # ... other
        else:
            try:
                return type(s)
            except Error as e:
                print "Scalar decoding error", s, type, iterable

    return map(lambda i : _do(i.text), sv) if iterable else _do(sv.text)


def _decode(repr, typeof, iterable):
    """Decodes an xml element."""        
    def _do(xml):
        # Set doc type.
        doc_type = typeof
        if typeof.type_key != xml.get('ontologyTypeKey'):
            doc_type = ontologies.get_type_from_key(xml.get('ontologyTypeKey'))
        if doc_type is None:
            rt.raise_error('Decoding type is unrecognized')
    
        # Set doc.
        doc = doc_type()

        # Set doc attributes.
        for _name, _type, _required, _iterable in ontologies.get_type_info(doc_type):            
            elem = xml.find(convert_to_camel_case(_name))
            if elem is not None:
                decoder = _decode if _type in _TYPES else _decode_scalar
                setattr(doc, _name, decoder(elem, _type, _iterable))

        return doc

    return map(lambda i : _do(i), repr) if iterable else _do(repr)


def _is_encodable_scalar(sv):
    """Predicate returning flag indicating whether a scalar value requires encoding."""
    return sv not in (None, str(), int())


def _encode_scalar(xml, sv):
    """Encodes a scalar value."""
    if sv in (None, 'None'):
        return ''
    elif isinstance(sv, datetime.datetime):
        sv = sv.isoformat().replace('T', ' ')
    elif isinstance(sv, datetime.date):
        sv = sv.isoformat()
    elif isinstance(sv, datetime.time):
        sv = sv.isoformat()
    else:
        sv = str(sv)
    
    xml.text = sv


def _encode_list(xml, tag, l):
    """Encodes a list."""
    tag = _get_item_tag(tag)
    for i in l:
        if isinstance(i, dict):
            _encode_dict(ET.SubElement(xml, tag), i)
        else:
            _encode_scalar(ET.SubElement(xml, tag), i)


def _encode_dict(xml, d):
    """Encodes a dictionary."""
    for k in sorted(d.iterkeys()):
        v = d[k]
        if isinstance(v, dict):
            _encode_dict(ET.SubElement(xml, k), v)
        elif isinstance(v, list):
            if len(v) > 0:
                _encode_list(ET.SubElement(xml, k), k, v)
        else:
            if _is_encodable_scalar(v):
                if k in ('ontologyTypeKey'):
                    xml.attrib[k] = v
                else:
                    _encode_scalar(ET.SubElement(xml, k), v)

    return xml


def _get_xml_tag(doc):
    """Returns document root xml tag."""
    return convert_to_camel_case(doc.__class__.type_key.split('.')[3])


def encode(doc):
    """Encodes a document to an xml string.

    :param doc: Document being encoded.
    :type doc: object

    :returns: An xml representation of a document.
    :rtype: str

    """
    # Convert to dictionary.
    as_dict = serializer_dict.encode(doc)

    # Format dictionary keys.    
    as_dict = convert_dict_keys(as_dict, convert_to_camel_case)

    # Encode to an xml element.
    as_xml = _encode_dict(ET.Element(_get_xml_tag(doc)), as_dict)

    # Return xml encoded string.
    return ET.tostring(as_xml, _UNICODE)


def decode(repr):
    """Decodes a document from an xml string.

    :param repr: Document xml representation.
    :type repr: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """  
    # Convert to etree.
    xml = repr if type(repr) == ET else ET.fromstring(repr)

    # Get target type.
    o, v, p, t = xml.get("ontologyTypeKey").split('.')
    doc_type = ontologies.get_type(o, v, p, t)

    return _decode(xml, doc_type, False)
