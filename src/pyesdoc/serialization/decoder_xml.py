"""
.. module:: pyesdoc.utils.decoder_xml.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Document decoder from xml.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import xml.etree.ElementTree as ET

from .. import ontologies
from .. utils import (
    convert,
    runtime as rt
    )



# Set of supported ontology types.
_TYPES = ontologies.get_types()


def _get_doc(xml, doc_type):
    """Returns document."""
    type_key = xml.get('ontologyTypeKey')
    if type_key and doc_type.type_key != type_key:
        doc_type = ontologies.get_type_from_key(xml.get('ontologyTypeKey'))
    if doc_type is None:
        rt.raise_error('Decoding type is unrecognized')

    return doc_type(), ontologies.get_type_info(doc_type)


def _decode_simple(v, type, iterable):
    """Decodes a simple value."""
    if iterable:
        return map(lambda i : convert.str_to_typed_value(i.text, type), v)
    else:
        return convert.str_to_typed_value(v.text, type)


def _decode_complex(v, doc_type, iterable):
    """Decodes a complex type."""
    def _do(xml):
        # Set doc.
        doc, doc_type_info = _get_doc(xml, doc_type)

        # Set doc attributes.
        for _name, _type, _required, _iterable in doc_type_info:
            # ... get xml element
            elem = xml.find(convert.str_to_camel_case(_name))

            # ... set attribute
            if elem is not None:
                decoder = _decode_complex if _type in _TYPES else _decode_simple
                setattr(doc, _name, decoder(elem, _type, _iterable))

        return doc

    return map(lambda i : _do(i), v) if iterable else _do(v)


def decode(as_xml):
    """Decodes a document from an xml string.

    :param as_xml: Document xml representation.
    :type as_xml: unicode | str | ET.Element

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Convert to etree.
    if isinstance(as_xml, unicode):
        as_xml = ET.fromstring(as_xml.encode('utf-8'))
    elif isinstance(as_xml, str):
        as_xml = ET.fromstring(as_xml)

    # Verify etree.
    if not isinstance(as_xml, ET.Element):
        rt.throw("Cannot decode non xml documents")

    # Get target type.
    doc_type_key = as_xml.get("ontologyTypeKey")
    doc_type = ontologies.get_type_from_key(doc_type_key)

    return  _decode_complex(as_xml, doc_type, False)