"""
.. module:: pyesdoc.serializer.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes functions for decoding/encoding document instances.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""

# Module imports.
from pyesdoc.ontologies.constants import (
    CIM_ENCODINGS,
    CIM_SCHEMAS
    )
from pyesdoc.serialization import (
    decode as decoder,
    encode as encoder
    )
from pyesdoc.utils.exception import PYESDOC_Exception


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
    # Defensive programming.
    if representation is None:
        raise PYESDOC_Exception('Document instances cannot be decoded from null objects.')
    if schema not in CIM_SCHEMAS:
        raise PYESDOC_Exception('{0} is an unsupported schema.'.format(schema))
    if encoding not in CIM_ENCODINGS:
        raise PYESDOC_Exception('{0} is an unsupported encoding.'.format(encoding))

    return decoder(representation, schema, encoding)


def encode(instance, schema, encoding):
    """Encodes a pyesdoc document instance.
    
    :param instance: pyesdoc document instance.
    :type instance: object

    :param schema: A document schema (e.g. CIM 1.5).
    :type schema: str

    :param encoding: A document encoding (e.g. json).
    :type encoding: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Defensive programming.
    if instance is None:
        raise PYESDOC_Exception('Cannot encode null objects.')
    if schema not in CIM_SCHEMAS:
        raise PYESDOC_Exception('{0} is an unsupported CIM schema.'.format(schema))
    if encoding not in CIM_ENCODINGS:
        raise PYESDOC_Exception('{0} is an unsupported CIM encoding.'.format(encoding))

    return encoder(instance, schema, encoding)
