"""
.. module:: pyesdoc.serialization.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document serialization functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from . import (
    decoder,
    encoder
    )



def decode(doc, encoding):
    """Returns a decoded pyesdoc document.

    :param unicode doc: A document representation (e.g. json).
    :param str encoding: A document encoding (dict|json|xml|metafor-cim-1-xml).
    :param func post_processing_handlers: Callback(s) to invoke after processing.

    :rtype: object

    """
    return decoder.decode(doc, encoding)


def encode(doc, encoding):
    """Returns an encoded pyesdoc document instance.

    :param object doc: pyesdoc document instance.
    :param str encoding: A document encoding.

    :rtype: unicode | dict

    """
    return encoder.encode(doc, encoding)


def convert(doc, encoding_from, encoding_to):
    """Converts one encoding to another.

    :param unicode doc: A document representation (e.g. json).
    :param str encoding_from: A document encoding (dict|json|xml).
    :param str encoding_to: A document encoding (dict|json|xml).

    :returns: A pyesdoc document representation.
    :rtype: unicode | dict

    """
    return encode(decode(doc, encoding_from), encoding_to)
