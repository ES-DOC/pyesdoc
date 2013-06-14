"""
.. module:: pyesdoc.serialization.__init__.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package initialisor.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from pyesdoc.ontologies.constants import (
    CIM_ENCODINGS,
    CIM_SCHEMAS
    )
from pyesdoc.serialization.decoder import decode as decoder
from pyesdoc.serialization.encoder import encode as encoder
from pyesdoc.utils.exception import ESDOC_Exception



def decode(representation, schema, encoding):
    """Decodes a pyesdoc document representation.

    :param representation: A document representation (e.g. utf-8).
    :type representation: str

    :param schema: A document schema (e.g. CIM v1).
    :type schema: str

    :param encoding: A document encoding (e.g. json).
    :type encoding: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Defensive programming.
    if representation is None:
        raise ESDOC_Exception('Document instances cannot be decoded from null objects.')
    if schema not in CIM_SCHEMAS:
        raise ESDOC_Exception('{0} is an unsupported schema.'.format(schema))
    if encoding not in CIM_ENCODINGS:
        raise ESDOC_Exception('{0} is an unsupported encoding.'.format(encoding))

    return decoder(representation, schema, encoding)


def encode(instance, schema, encoding):
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
    # Defensive programming.
    if instance is None:
        raise ESDOC_Exception('Cannot encode null objects.')
    if schema not in CIM_SCHEMAS:
        raise ESDOC_Exception('{0} is an unsupported CIM schema.'.format(schema))
    if encoding not in CIM_ENCODINGS:
        raise ESDOC_Exception('{0} is an unsupported CIM encoding.'.format(encoding))

    return encoder(instance, schema, encoding)
