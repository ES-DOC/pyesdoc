"""
.. module:: pyesdoc.serialization.__init__.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package initialisor.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from . import (
    serializer_dict,
    serializer_json,
    serializer_xml,
    serializer_xml_metafor_cim_v1
    )
from .. import utils



# Set of supported ESDOC encodings.
ESDOC_ENCODING_DICT = 'dict'
ESDOC_ENCODING_JSON = 'json'
ESDOC_ENCODING_XML = 'xml'
METAFOR_CIM_XML_ENCODING = 'metafor-cim-v1-xml'

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

# Set of supported sesrializers keyed by encoding.
_serializers = {
    ESDOC_ENCODING_DICT : serializer_dict,
    ESDOC_ENCODING_JSON : serializer_json,
    ESDOC_ENCODING_XML : serializer_xml,
    METAFOR_CIM_XML_ENCODING : serializer_xml_metafor_cim_v1,
}


def _assert(encoding):
    """Asserts that the serialization encoding is supported."""
    if not encoding in _serializers:
        raise ValueError('Document encoding is unsupported :: encoding = {0}.'.format(encoding))
    

def decode(representation, encoding):
    """Decodes a pyesdoc document representation.

    :param representation: A document representation (e.g. json).
    :type representation: str

    :param encoding: A document encoding (dict|json|xml|metafor-cim-1-xml).
    :type encoding: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    _assert(encoding)

    return _serializers[encoding].decode(representation)


def encode(doc, encoding):
    """Encodes a pyesdoc document instance.

    :param doc: pyesdoc document instance.
    :type doc: object

    :param encoding: A document encoding (dict|json|xml).
    :type encoding: str

    :returns: A pyesdoc document representation.
    :rtype: unicode | dict

    """
    _assert(encoding)

    return _serializers[encoding].encode(doc)
