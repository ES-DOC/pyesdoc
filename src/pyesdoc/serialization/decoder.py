"""
.. module:: decoder.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Document decoder.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
from lxml.etree import (
    _ElementTree as et,
    _Element as ete
    )
import xml.etree.ElementTree as ET

from .. import constants
from .. utils import runtime as rt
from . import (
    decoder_dict,
    decoder_json,
    decoder_xml,
    decoder_xml_metafor_cim_v1
    )



# Map of encodings to decoders.
_decoders = {
    constants.ESDOC_ENCODING_DICT : decoder_dict,
    constants.ESDOC_ENCODING_JSON : decoder_json,
    constants.ESDOC_ENCODING_XML : decoder_xml,
    constants.METAFOR_CIM_XML_ENCODING : decoder_xml_metafor_cim_v1,
}

# Map of encodings to allowed input types.
_input_types = {
    constants.ESDOC_ENCODING_DICT : (dict, ),
    constants.ESDOC_ENCODING_JSON : (str, unicode),
    constants.ESDOC_ENCODING_XML : (str, unicode, ET.Element),
    constants.METAFOR_CIM_XML_ENCODING : (str, unicode, ET.Element, et, ete),
}


def _assert(doc, encoding):
    """Validates input parameters."""
    if doc is None:
        rt.throw("Documents cannot be decoded from null objects.")
    if not encoding in _decoders:
        raise NotImplementedError('Document decoding is unsupported :: encoding = {0}.'.format(encoding))
    if type(doc) not in _input_types[encoding]:
        err = "Document representation type ({0}) is unsupported, it must be one of {1}."
        err = err.format(type(doc), _input_types[encoding])
        rt.throw(err)


def decode(doc, encoding):
    """Decodes a pyesdoc document from a representation.

    :param doc: A document representation (e.g. json).
    :type doc: utf-8 encoded str | unicode

    :param encoding: A document encoding (dict|json|xml|metafor-cim-1-xml).
    :type encoding: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Defensive programming.
    _assert(doc, encoding)

    # Decode.
    return _decoders[encoding].decode(doc)