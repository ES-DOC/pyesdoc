"""
.. module:: pyesdoc.serialization.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document serialization functions.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from .utils import (
    runtime as rt,
    serializer_dict,
    serializer_json,
    serializer_xml,
    serializer_xml_metafor_cim_v1
    )



# Supported ESDOC encodings.
ESDOC_ENCODING_DICT = 'dict'
ESDOC_ENCODING_JSON = 'json'
ESDOC_ENCODING_XML = 'xml'
METAFOR_CIM_XML_ENCODING = 'xml-metafor-cim-v1'

# Standard ESDOC encodings.
ESDOC_ENCODINGS = (
    ESDOC_ENCODING_DICT,
    ESDOC_ENCODING_JSON,
    ESDOC_ENCODING_XML
)

# Custom ESDOC encodings.
ESDOC_ENCODINGS_CUSTOM = (
    METAFOR_CIM_XML_ENCODING,
)

# Map of standard ESDOC encodings to MIME types.
ESDOC_ENCODING_HTTP_MEDIA_TYPES = {
    ESDOC_ENCODING_JSON : "application/json",
    ESDOC_ENCODING_XML : "application/xml"
}

# Map of encodings to serializers.
_serializers = {
    ESDOC_ENCODING_DICT : serializer_dict,
    ESDOC_ENCODING_JSON : serializer_json,
    ESDOC_ENCODING_XML : serializer_xml,
    METAFOR_CIM_XML_ENCODING : serializer_xml_metafor_cim_v1,
}


def _assert_encoding(encoding):
    """Asserts that the serialization encoding is supported."""
    if not encoding in _serializers:
        raise ValueError('Document encoding is unsupported :: encoding = {0}.'.format(encoding))


def _assert_doc(doc):
    """Asserts that the document is encodable."""    
    rt.assert_doc('doc', doc, "Cannot encode a null document")
    

def _assert_representation(repr):
    """Asserts that the representation is decodable."""
    if repr is None:
        rt.throw("Documents cannot be decoded from null objects.")


def decode(repr, encoding):
    """Decodes a pyesdoc document representation.

    :param repr: A document representation (e.g. json).
    :type repr: str

    :param encoding: A document encoding (dict|json|xml|metafor-cim-1-xml).
    :type encoding: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    def set_attributes(doc):
        if doc is not None:
            doc.doc_info.type = doc.__class__.type_key

        return doc

    _assert_representation(repr)
    _assert_encoding(encoding)

    return set_attributes(_serializers[encoding].decode(repr))


def encode(doc, encoding):
    """Encodes a pyesdoc document instance.

    :param doc: pyesdoc document instance.
    :type doc: object

    :param encoding: A document encoding (dict|json|xml).
    :type encoding: str

    :returns: A pyesdoc document representation.
    :rtype: unicode | dict

    """
    _assert_doc(doc)
    _assert_encoding(encoding)

    return _serializers[encoding].encode(doc)


def convert(repr, encoding_from, encoding_to):
    """Converts one encoding to another.

    :param repr: A document representation (e.g. json).
    :type repr: str

    :param encoding_from: A document encoding (dict|json|xml).
    :type encoding_from: str

    :param encoding_to: A document encoding (dict|json|xml).
    :type encoding_to: str

    :returns: A pyesdoc document representation.
    :rtype: str

    """
    return encode(decode(repr, encoding_from), encoding_to)