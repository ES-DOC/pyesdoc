"""
.. module:: pyesdoc.serialization.serializer_xml.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes document xml serialization functions.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""
# Module imports.
import datetime

import xml.etree.ElementTree as ET

from . import serializer_dict
from .. import utils



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
                if k == 'docTypeKey':
                    xml.attrib["ontologyTypeKey"] = v
                else:
                    _encode_scalar(ET.SubElement(xml, k), v)

    return xml


def _get_xml_tag(doc):
    """Returns document root xml tag."""
    return utils.convert_to_camel_case(doc.__class__.type_key.split('.')[3])


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
    as_dict = utils.convert_dict_keys(as_dict, utils.convert_to_camel_case)

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
    raise NotImplementedError()
