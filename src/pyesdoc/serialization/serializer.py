"""
.. module:: pyesdoc.serialization.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document serialization functions.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from . import (
    decoder, 
    encoder
    )
from .. import parsers
from .. utils import runtime as rt



def decode(doc, encoding):
    """Decodes a pyesdoc document from a representation.

    :param doc: A document representation (e.g. json).
    :type doc: str | unicode

    :param encoding: A document encoding (dict|json|xml|metafor-cim-1-xml).
    :type encoding: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Decode.
    doc = decoder.decode(doc, encoding)

    # Parse.
    if doc:
        parsers.parse(doc)

    return doc


def encode(doc, encoding):
    """Encodes a pyesdoc document instance.

    :param doc: pyesdoc document instance.
    :type doc: object

    :param encoding: A document encoding.
    :type encoding: str

    :returns: A formatted representation of a pyesdoc document.
    :rtype: object

    """
    return encoder.encode(doc, encoding)


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
    return encode(decode(doc, encoding_from), encoding_to)