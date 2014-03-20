"""
.. module:: pyesdoc.serialization.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document serialization functions.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from .. import parsers
from .. utils import runtime as rt
from . import (
    constants,
    serializer_dict,
    serializer_html,
    serializer_json,
    serializer_xml,
    serializer_xml_metafor_cim_v1
    )


# Serializers.
_serializers = {
    constants.ESDOC_ENCODING_DICT : serializer_dict,
    constants.ESDOC_ENCODING_JSON : serializer_json,
    constants.ESDOC_ENCODING_XML : serializer_xml,
    constants.ESDOC_ENCODING_HTML : serializer_html,
    constants.METAFOR_CIM_XML_ENCODING : serializer_xml_metafor_cim_v1,
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


def decode(doc, encoding):
    """Decodes a pyesdoc document representation.

    :param doc: A document representation (e.g. json).
    :type doc: str | unicode

    :param encoding: A document encoding (dict|json|xml|metafor-cim-1-xml).
    :type encoding: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Defensive programming.
    _assert_representation(doc)
    _assert_encoding(encoding)

    # Decode.
    doc = _serializers[encoding].decode(doc)

    if doc:
        # Parse.
        parsers.parse(doc)

        # Set supported encodings.
        doc._encodings = doc.doc_info.encodings = list(get_file_encodings(doc))

    return doc


def encode(doc, encoding):
    """Encodes a pyesdoc document instance.

    :param decoded: pyesdoc document instance.
    :type decoded: object

    :param encoding: A document encoding (dict|json|xml).
    :type encoding: str

    :returns: A pyesdoc document representation.
    :rtype: unicode | dict

    """
    _assert_doc(doc)
    _assert_encoding(encoding)

    return _serializers[encoding].encode(doc)


def convert(doc, encoding_from, encoding_to):
    """Converts one encoding to another.

    :param doc: A document representation (e.g. json).
    :type doc: str

    :param encoding_from: A document encoding (dict|json|xml).
    :type encoding_from: str

    :param encoding_to: A document encoding (dict|json|xml).
    :type encoding_to: str

    :returns: A pyesdoc document representation.
    :rtype: str

    """
    # Defensive programming.
    _assert_representation(doc)
    _assert_encoding(encoding_from)
    _assert_encoding(encoding_to)

    return encode(decode(doc, encoding_from), encoding_to)


def get_file_encodings(doc):
    """Returns set of file encodings for the passed document.

    :param object doc: A document for which the set of supported file encodings is to be returned.

    :returns: Set of supported file encodings.
    :rtype: set

    """
    # Defensive programming.
    _assert_doc(doc)

    result = constants.ESDOC_ENCODINGS_FILE
    if doc.doc_info.type.startswith("cim.1"):
        result = result + (constants.METAFOR_CIM_XML_ENCODING,)

    return result