"""
.. module:: encoder.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Document encoder.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
from .. import constants
from .. utils import runtime as rt
from . import (
    encoder_dict,
    encoder_html,
    encoder_json,
    encoder_xml,
    )


# Encoders.
_encoders = {
    constants.ESDOC_ENCODING_DICT : encoder_dict,
    constants.ESDOC_ENCODING_JSON : encoder_json,
    constants.ESDOC_ENCODING_XML : encoder_xml,
    constants.ESDOC_ENCODING_HTML : encoder_html,
}


def _assert_doc(doc):
    """Asserts that document is encodable."""    
    rt.assert_doc('doc', doc, "Cannot encode a null document")
    

def _assert_encoding(encoding):
    """Asserts that encoding is supported."""
    if not encoding in _encoders:
        raise NotImplementedError('Document encoding is unsupported :: encoding = {0}.'.format(encoding))


def encode(doc, encoding):
    """Encodes a pyesdoc document instance.

    :param doc: pyesdoc document instance.
    :type doc: object

    :param encoding: A document encoding.
    :type encoding: str

    :returns: A formatted representation of a pyesdoc document.
    :rtype: object

    """
    # Defensive programming.
    _assert_doc(doc)
    _assert_encoding(encoding)

    return _encoders[encoding].encode(doc)
