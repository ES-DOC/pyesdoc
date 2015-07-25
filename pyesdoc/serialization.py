# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.serialization.py
   :copyright: Copyright "Sep 4, 2013", Earth System Documentation
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
from pyesdoc.codecs import dictionary
from pyesdoc.codecs import html
from pyesdoc.codecs import json
from pyesdoc.codecs import xml
from pyesdoc.codecs import xml_metafor_cim_v1
from pyesdoc.utils import runtime as rt



# Codecs mapped by encoding.
_CODECS = {
	constants.ESDOC_ENCODING_DICT: dictionary,
	constants.ESDOC_ENCODING_HTML: html,
	constants.ESDOC_ENCODING_JSON: json,
	constants.ESDOC_ENCODING_XML: xml,
	constants.METAFOR_CIM_XML_ENCODING: xml_metafor_cim_v1
}

# Map of formats to allowed input types when decoding.
_DECODE_TYPE_WHITELIST = {
    constants.ESDOC_ENCODING_DICT : (dict, ),
    constants.ESDOC_ENCODING_JSON : (str, unicode),
    constants.ESDOC_ENCODING_XML : (str, unicode, ET.Element),
    constants.METAFOR_CIM_XML_ENCODING : (str, unicode, ET.Element, et, ete),
}


def _assert_decode(target, encoding):
    """Asserts decode input parameters.

    """
    if target is None:
        rt.throw("Documents cannot be decoded from null objects.")
    if not encoding in _CODECS:
        raise NotImplementedError('Document decoding is unsupported :: encoding = {0}.'.format(encoding))
    if type(target) not in _DECODE_TYPE_WHITELIST[encoding]:
        err = "Document representation type ({0}) is unsupported, it must be one of {1}."
        err = err.format(type(target), _DECODE_TYPE_WHITELIST[encoding])
        rt.throw(err)


def decode(target, encoding):
    """Returns a decoded pyesdoc document.

    :param target: A document representation (e.g. json).
    :type target: utf-8 encoded str | unicode
    :param str encoding: A document encoding (dict|json|xml|metafor-cim-1-xml).

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    _assert_decode(target, encoding)
    document = _CODECS[encoding].decode(target)
    if document:
        document.meta.type == type(document).type_key
    return document


def _assert_encode(target, encoding):
    """Asserts encode input parameters.

    """
    if target is None:
        rt.throw("Cannot encode a null document.")
    if type(target) not in ontologies.get_types():
        rt.throw("Unsupported document type: {0}.".format(type(target)))
    if not encoding in _CODECS:
        raise NotImplementedError('Unsupported document encoding :: {0}.'.format(encoding))


def encode(target, encoding):
    """Returns an encoded pyesdoc document instance.

    :param object target: pyesdoc document instance.
    :param str encoding: A document encoding.

    :returns: A formatted representation of a pyesdoc document.
    :rtype: object

    """
    try:
        iter(target)
    except TypeError:
        _assert_encode(target, encoding)
        return _CODECS[encoding].encode(target)
    else:
        return [encode(d, encoding) for d in target]


def convert(doc, encoding_from, encoding_to):
    """Converts one encoding to another.

    :param unicode doc: A document representation (e.g. json).
    :param str encoding_from: A document encoding (dict|json|xml).
    :param str encoding_to: A document encoding (dict|json|xml).

    :returns: A pyesdoc document representation.
    :rtype: unicode | dict

    """
    return encode(decode(doc, encoding_from), encoding_to)

