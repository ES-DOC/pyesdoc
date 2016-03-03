# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.codecs.xml.decoder.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Decodes a document from an XML text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import xml.etree.ElementTree as ET

from pyesdoc import ontologies
from pyesdoc.utils import convert
from pyesdoc.utils import runtime as rt



# Set of supported ontology types.
_TYPES = ontologies.get_types()


def _get_doc(xml, doc_type):
    """Returns document.

    """
    type_key = xml.get('ontologyTypeKey')
    if type_key and ontologies.get_type_key(doc_type) != type_key:
        doc_type = ontologies.get_type_from_key(type_key)
    if doc_type is None:
        raise ValueError('Decoding type is unrecognized')

    return doc_type(), ontologies.get_decoder_info(doc_type)


def _decode_simple(v, type, iterable):
    """Decodes a simple type value.

    """
    if iterable:
        return [convert.text_to_typed_value(i.text, type) for i in v]
    else:
        return convert.text_to_typed_value(v.text, type)


def _decode_complex(val, doc_type, iterable):
    """Decodes a complex type value.

    """
    def _decode(xml):
        # Set doc.
        doc, doc_type_info = _get_doc(xml, doc_type)

        # Set doc attributes.
        for _name, _type, _iterable in doc_type_info:
            # ... get xml element
            elem = xml.find(convert.str_to_camel_case(_name))

            # ... set attribute
            if elem is not None:
                decoder = _decode_complex if _type in _TYPES else _decode_simple
                setattr(doc, _name, decoder(elem, _type, _iterable))

        return doc

    return [_decode(i) for i in val] if iterable else _decode(val)


def decode(as_xml):
    """Decodes a document from an xml string.

    :param as_xml: Document xml representation.
    :type as_xml: unicode | str | ET.Element

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Convert to etree.
    if isinstance(as_xml, unicode):
        as_xml = ET.fromstring(convert.unicode_to_str(as_xml))
    elif isinstance(as_xml, str):
        as_xml = ET.fromstring(as_xml)
    if not isinstance(as_xml, ET.Element):
        raise TypeError("Cannot decode non xml documents")

    # Get document type.
    doc_type_key = as_xml.get("ontologyTypeKey")

    # Get target type.
    doc_type = ontologies.get_type_from_key(doc_type_key)
    if doc_type is None:
        raise ValueError('ontology_type_key cannot be mapped to a supported ontology type.')

    return  _decode_complex(as_xml, doc_type, False)
