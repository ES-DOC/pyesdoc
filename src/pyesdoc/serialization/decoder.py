"""
.. module:: decoder.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Document decoder.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
from .. import constants, parsers
from .. utils import runtime as rt
from . import (
    decoder_dict,
    decoder_json,
    decoder_xml,
    decoder_xml_metafor_cim_v1
    )



# Decoders.
_decoders = {
    constants.ESDOC_ENCODING_DICT : decoder_dict,
    constants.ESDOC_ENCODING_JSON : decoder_json,
    constants.ESDOC_ENCODING_XML : decoder_xml,
    constants.METAFOR_CIM_XML_ENCODING : decoder_xml_metafor_cim_v1,
}


def _assert_encoding(encoding):
    """Asserts that the serialization encoding is supported."""
    if not encoding in _decoders:
        raise NotImplementedError('Document decoding is unsupported :: encoding = {0}.'.format(encoding))


def _assert_representation(doc):
    """Asserts that the representation is decodable."""
    if doc is None:
        rt.throw("Documents cannot be decoded from null objects.")


def decode(doc, encoding):
    """Decodes a pyesdoc document from a representation.

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
    return _decoders[encoding].decode(doc)