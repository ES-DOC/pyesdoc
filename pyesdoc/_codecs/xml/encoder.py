"""
.. module:: xml.encoder.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encodes a document as an XML text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import datetime
import uuid
import xml.etree.ElementTree as ET

from pyesdoc._codecs.dictionary import encoder as dict_encoder
from pyesdoc.utils import convert



# Default XML document encoding.
_UNICODE = "utf-8"

# Mappings between collection name suffixes and collection item suffixes.
_suffix_maps = (
    ('ies', 'y'),
    ('List', ''),
    ('s', ''),
)


def _get_item_tag(tag):
    """Returns tag name of a collection item.

    """
    for suffix, replacement in _suffix_maps:
        if tag.endswith(suffix):
            return tag[0:len(tag) - len(suffix)] + replacement

    return tag + 'Item'


def _is_encodable_simple(val):
    """Determines whether a simple value requires encoding.

    """
    return val not in (None, str(), int())


def _encode_simple(xml, val):
    """Encodes a simple value.

    """
    # Format according to type.
    if val in (None, 'None'):
        return u''
    elif isinstance(val, datetime.datetime):
        val = val.isoformat().replace('T', ' ')
    elif isinstance(val, datetime.date):
        val = val.isoformat()
    elif isinstance(val, datetime.time):
        val = val.isoformat()
    else:
        val = convert.str_to_unicode(val)
    if val is None or len(val) == 0:
        val = u''

    # Assign to xml.
    xml.text = val.strip()


def _encode_collection(xml, tag, collection):
    """Encodes a collection.

    """
    tag = _get_item_tag(tag)
    for item in collection:
        if isinstance(item, dict):
            _encode_complex(ET.SubElement(xml, tag), item)
        else:
            _encode_simple(ET.SubElement(xml, tag), item)


def _encode_complex(xml, d):
    """Encodes a complex type.

    """
    # Iterate dictionary keys sorted in alphabetical order.
    for k in sorted(d.iterkeys()):
        # Get attribute value.
        v = d[k]

        # Process according to value type.
        # ... iterable
        if isinstance(v, list):
            if len(v):
                elem = ET.SubElement(xml, k)
                _encode_collection(elem, k, v)

        # ... complex
        elif isinstance(v, dict):
            if len(v.keys()):
                elem = ET.SubElement(xml, k)
                _encode_complex(elem, v)

        # ... simple
        elif _is_encodable_simple(v):
            # ... type key is assigned as an attribute
            if k in ('ontologyTypeKey',):
                xml.attrib[k] = v
            else:
                elem = ET.SubElement(xml, k)
                _encode_simple(elem, v)

    return xml


def _get_xml_tag(doc):
    """Returns document root xml tag.

    """
    tag = type(doc).type_key.split('.')[3]
    tag = convert.str_to_camel_case(tag)

    return tag


def encode(doc):
    """Encodes a document.

    :param doc: Document being encoded.
    :type doc: object

    :returns: An encoded document representation.
    :rtype: unicode

    """
    # Encode as a dictionary.
    as_dict = dict_encoder.encode(doc)

    # Format dictionary keys.
    as_dict = convert.dict_keys(as_dict, convert.str_to_camel_case)

    # Encode to an etree xml element.
    tag = _get_xml_tag(doc)
    xml = _encode_complex(ET.Element(tag), as_dict)

    return ET.tostring(xml, _UNICODE)
