"""
.. module:: pyesdoc.__init__.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Package initialisor.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""

# Module imports.
from pyesdoc.serialization import (
    decode as decoder,
    encode as encoder
    )


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
    return encoder(instance, schema, encoding)