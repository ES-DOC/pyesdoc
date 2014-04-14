"""
.. module:: pyesdoc.utils.encoder_xml.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: XML encoder from document.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import datetime
import uuid
import xml.etree.ElementTree as ET

from . import encoder_dict
from .. utils import convert



# Default XML document encoding.
_UNICODE = "utf-8"

# Mappings between collection name suffixes and collection item suffixes.
_suffix_maps = (
    ('ies', 'y'),
    ('List', ''),
    ('s', ''),
)


def _get_item_tag(tag):
    "Returns tag name of a collection item."
    for suffix, replacement in _suffix_maps:
        if tag.endswith(suffix):
            return tag[0:len(tag) - len(suffix)] + replacement

    return tag + 'Item'


def _is_encodable_simple(sv):
    """Determines whether a simple value requires encoding."""
    return sv not in (None, str(), int())


def _encode_simple(xml, sv):
    """Encodes a simple value."""
    # Format according to type.
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

    # Assign to xml.
    if sv is not None and len(sv):
        xml.text = unicode(sv.decode(_UNICODE).strip())
    else:
        xml.text = u''


def _encode_list(xml, tag, l):
    """Encodes a list."""
    tag = _get_item_tag(tag)
    for i in l:
        if isinstance(i, dict):
            _encode_complex(ET.SubElement(xml, tag), i)
        else:
            _encode_simple(ET.SubElement(xml, tag), i)


def _encode_complex(xml, d):
    """Encodes a complex type."""
    # Iterate dictionary keys sorted in alphabetical order.
    for k in sorted(d.iterkeys()):
        # Get attribute value.
        v = d[k]

        # Process according to value type.
        # ... iterable
        if isinstance(v, list):
            if len(v):
                elem = ET.SubElement(xml, k)
                _encode_list(elem, k, v)

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
    """Returns document root xml tag."""
    tag = type(doc).type_key.split('.')[3]
    tag = convert.str_to_camel_case(tag)

    return tag


def encode(doc):
    """Encodes a document to an xml str.

    :param doc: Document being encoded.
    :type doc: object

    :returns: An xml representation of a document.
    :rtype: str

    """
    # Convert to dictionary.
    d = encoder_dict.encode(doc)

    # Format dictionary keys.
    d = convert.dict_keys(d, convert.str_to_camel_case)

    # Encode to an etree xml element.
    tag = _get_xml_tag(doc)
    xml = _encode_complex(ET.Element(tag), d)

    return ET.tostring(xml, _UNICODE)
