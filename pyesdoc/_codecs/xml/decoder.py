"""
.. module:: xml.decoder.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Decodes a document from an XML text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import xml.etree.ElementTree as ET

from pyesdoc import ontologies
from pyesdoc.utils import convert



# Set of supported ontology types.
_TYPES = ontologies.get_types()


def _create_doc(elem, doc_type):
    """Creates & returns a document to be hydrated from an xml element.

    """
    type_key = elem.get('ontologyTypeKey')
    if type_key and ontologies.get_type_key(doc_type) != type_key:
        doc_type = ontologies.get_type_from_key(type_key)
    if doc_type is None:
        raise ValueError('Decoding type is unrecognized')

    return doc_type(), ontologies.get_decoder_info(doc_type)


def _decode_simple(elem, typeof, is_iterable):
    """Decodes a simple type value.

    """
    if is_iterable:
        return [convert.text_to_typed_value(i.text, typeof) for i in elem]
    return convert.text_to_typed_value(elem.text, typeof)


def _decode(elem, doc_type, is_iterable):
    """Decodes a complex type value.

    """
    def _do(xml):
        # Set doc.
        doc, doc_type_info = _create_doc(xml, doc_type)

        # Set doc attributes:
        for _name, _type, _is_iterable in doc_type_info:
            # ... set xml element;
            _elem = xml.find(convert.str_to_camel_case(_name))

            # ... skip placeholders;
            if _elem is None:
                continue

            # ... complex types;
            elif _type in _TYPES:
                setattr(doc, _name, _decode(_elem, _type, _is_iterable))

            # ... simple types;
            else:
                setattr(doc, _name, _decode_simple(_elem, _type, _is_iterable))

        return doc

    return [_do(i) for i in elem] if is_iterable else _do(elem)


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

    # Get document type key.
    doc_type_key = as_xml.find('meta/type').text

    # Get document type.
    doc_type = ontologies.get_type_from_key(doc_type_key)
    if doc_type is None:
        raise ValueError('meta.type key cannot be mapped to an ontology type.')

    return _decode(as_xml, doc_type, False)
