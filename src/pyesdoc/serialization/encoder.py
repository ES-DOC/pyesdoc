"""
.. module:: encoder.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Document encoder.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
from .. import constants, ontologies
from .. utils import runtime as rt
from . import (
    encoder_dict,
    encoder_html,
    encoder_json,
    encoder_xml,
    )



# Set of ontology types.
_TYPES = ontologies.get_types()

# Encoders.
_encoders = {
    constants.ESDOC_ENCODING_DICT : encoder_dict,
    constants.ESDOC_ENCODING_JSON : encoder_json,
    constants.ESDOC_ENCODING_XML : encoder_xml,
    constants.ESDOC_ENCODING_HTML : encoder_html,
}


def _assert(doc, encoding):
    """Validates input parameters."""
    if doc is None:
        rt.throw("Cannot encode a null document.")
    if type(doc) not in _TYPES:
        rt.throw("Unsupported document type: {0}.".format(type(doc)))
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
    try:
        iter(doc)
    except ValueError:
        _assert(doc, encoding)
    else:
        for item in doc:
            _assert(item, encoding)

    return _encoders[encoding].encode(doc)
