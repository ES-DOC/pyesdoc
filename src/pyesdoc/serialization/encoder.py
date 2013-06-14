"""
.. module:: pyesdoc.serialization.encoder.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes functions for encoding document representations.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""

# Module imports.
from pyesdoc.ontologies.constants import (
    ESDOC_ENCODING_JSON,
    ESDOC_ENCODING_XML
    )
from pyesdoc.serialization.encoder_json import encode as encode_to_json
from pyesdoc.serialization.encoder_xml import encode as encode_to_xml



# Set of encoders.
_encoders = {
    ESDOC_ENCODING_JSON : encode_to_json,
    ESDOC_ENCODING_XML : encode_to_xml,
}


def encode(instance, version, encoding):
    """Encodes a pyesdoc document instance.

    :param instance: pyesdoc document instance.
    :type instance: object

    :param schema: A document schema (e.g. CIM v1).
    :type schema: str

    :param encoding: A document encoding (e.g. json).
    :type encoding: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    return _encoders[encoding](instance, version)
