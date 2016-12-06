# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv.codecs.__init__.py
   :copyright: Copyright "Sep 4, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encpasulates transformations of terms from one format to another.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.cv import constants
from pyesdoc.cv.codecs import dictionary
from pyesdoc.cv.codecs import json



# Codecs mapped by encoding.
_CODECS = {
	constants.ENCODING_DICT: dictionary,
	constants.ENCODING_JSON: json
}

# Map of encodings to allowed input types when decoding.
_DECODE_TYPE_WHITELIST = {
    constants.ENCODING_DICT : (dict, ),
    constants.ENCODING_JSON : (str, unicode)
}


def _assert_decode(target, encoding):
    """Asserts decode input parameters.

    """
    if target is None:
        raise ValueError("Cannot decode a null pointer.")
    if not encoding in _CODECS:
        raise NotImplementedError('Unsupported term encoding :: {0}.'.format(encoding))

    if type(target) not in _DECODE_TYPE_WHITELIST[encoding]:
        err = "Term representation type ({0}) is unsupported, it must be one of {1}."
        err = err.format(type(target), _DECODE_TYPE_WHITELIST[encoding])
        raise TypeError(err)


def decode(target, encoding):
    """Returns a decoded pyesdoc document.

    :param target: A document representation (e.g. json).
    :type target: utf-8 encoded str | unicode
    :param str encoding: A document encoding (dict|json|xml|metafor-cim-1-xml).

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    _assert_decode(target, encoding)

    return _CODECS[encoding].decode(target)


def _assert_encode(target, encoding):
    """Asserts encode input parameters.

    """
    if target is None:
        raise ValueError("Cannot encode a null pointer.")
    if not encoding in _CODECS:
        raise NotImplementedError('Unsupported term encoding :: {0}.'.format(encoding))


def encode(target, encoding):
    """Returns an encoded term instance.

    :param object target: Term instance.
    :param str encoding: A document encoding.

    :returns: A formatted representation of a term.
    :rtype: object

    """
    try:
        iter(target)
    except TypeError:
        _assert_encode(target, encoding)
        encoded = _CODECS[encoding].encode(target)
        return encoded.strip() if isinstance(encoded, basestring) else encoded
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

