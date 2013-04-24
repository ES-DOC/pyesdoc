"""
.. module:: pyesdoc.serialization.decoder.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes functions for decoding document instances from representations.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""

# Module imports.
from pyesdoc.ontologies.constants import (
    ESDOC_ENCODING_JSON,
    ESDOC_ENCODING_XML
    )
from pyesdoc.serialization.decoder_json import decode as decode_from_json
from pyesdoc.serialization.decoder_xml import decode as decode_from_xml



# Set of decoders.
_decoders = {
    ESDOC_ENCODING_JSON : decode_from_json,
    ESDOC_ENCODING_XML : decode_from_xml,
}


def decode(representation, schema, encoding):
    """Decodes a pyesdoc document representation.

    :param representation: A document representation (e.g. utf-8).
    :type representation: str

    :param schema: A document schema (e.g. CIM 1.5).
    :type schema: str

    :param encoding: A document encoding (e.g. json).
    :type encoding: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    return _decoders[encoding](representation, schema)
