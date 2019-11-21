"""
.. module:: pyesdoc._serialization.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encpasulates transformations of documents from one format to another.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from lxml.etree import _ElementTree as et
from lxml.etree import _Element as ete
import xml.etree.ElementTree as ET

from pyesdoc import constants
from pyesdoc import ontologies
from pyesdoc import _codecs



# Codecs mapped by encoding.
_CODECS = {
	constants.ENCODING_DICT: _codecs.dictionary,
	constants.ENCODING_HTML: _codecs.html,
	constants.ENCODING_JSON: _codecs.json,
	constants.ENCODING_XML: _codecs.xml,
	constants.METAFOR_CIM_XML_ENCODING: _codecs.xml_metafor_cim_v1
}

# Map of formats to allowed input types when decoding.
_DECODE_TYPE_WHITELIST = {
    constants.ENCODING_DICT : (dict, ),
    constants.ENCODING_JSON : (str, unicode),
    constants.ENCODING_XML : (str, unicode, ET.Element),
    constants.METAFOR_CIM_XML_ENCODING : (str, unicode, ET.Element, et, ete),
}


def decode(target, encoding=constants.ENCODING_JSON):
    """Decodes a document from a text blob.

    :param target: A document representation (e.g. json).
    :type target: utf-8 encoded str | unicode
    :param str encoding: A document encoding (dict|json|xml|metafor-cim-1-xml).

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    _assert_decode(target, encoding)

    return _CODECS[encoding].decode(target)


def encode(target, encoding=constants.ENCODING_JSON):
    """Encodes a document.

    :param object target: pyesdoc document instance.
    :param str encoding: A document encoding.

    :returns: A formatted representation of a pyesdoc document.
    :rtype: object

    """
    try:
        iter(target)
    except TypeError:
        pass
    else:
        return [i for i in [encode(d, encoding) for d in target] if i]

    _assert_encode(target, encoding)
    encoded = _CODECS[encoding].encode(target)
    try:
        encoded = encoded.strip()
    except AttributeError:
        pass

    return encoded


def convert(doc, encoding_from, encoding_to):
    """Converts a document.

    :param unicode doc: A document representation (e.g. json).
    :param str encoding_from: A document encoding (dict|json|xml).
    :param str encoding_to: A document encoding (dict|json|xml).

    :returns: A pyesdoc document representation.
    :rtype: unicode | dict

    """
    return encode(decode(doc, encoding_from), encoding_to)


def _assert_decode(target, encoding):
    """Asserts decode input parameters.

    """
    if target is None:
        raise ValueError("Documents cannot be decoded from null objects.")

    if not encoding in _CODECS:
        raise NotImplementedError('Document decoding is unsupported :: encoding = {0}.'.format(encoding))

    if type(target) not in _DECODE_TYPE_WHITELIST[encoding]:
        err = "Document representation type ({0}) is unsupported, it must be one of {1}."
        err = err.format(type(target), _DECODE_TYPE_WHITELIST[encoding])
        raise TypeError(err)


def _assert_encode(target, encoding):
    """Asserts encode input parameters.

    """
    if target is None:
        raise ValueError("Cannot encode a null document.")

    if type(target) not in ontologies.get_types():
        raise TypeError("Unsupported document type: {0}.".format(type(target)))

    if not encoding in _CODECS:
        raise NotImplementedError('Unsupported document encoding :: {0}.'.format(encoding))
