# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.codecs.dictionary.encoder.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Enocdes a document as a python dictionary.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc import ontologies



def _is_encodable(obj):
    """Returns flag indicating whether an object is encodable or not.

    """
    return type(obj) in ontologies.get_types()


def _is_encodable_attribute(name):
    """Returns flag indicating whether an attribute is encodable.

    """
    if name.startswith("_") or name.startswith("__"):
        return False
    if name == "ext":
        return False
    return True


def _encode(doc):
    """Encodes an object to a deep dictionary.

    """
    # Initialise result (note - type key is necessary to decode).
    d = {
        'ontology_type_key' : type(doc).type_key
    }

    for k, v in doc.__dict__.items():
        if not _is_encodable_attribute(k):
            continue
        try:
            iter(v)
        except TypeError:
            if _is_encodable(v):
                d[k] = _encode(v)
            elif v is not None:
                d[k] = v
        else:
            if len(v) == 0:
                pass
            elif type(v) in (str, unicode,):
                d[k] = v
            else:
                d[k] = map(lambda i : _encode(i) if _is_encodable(i) else i, v)

    return d


def encode(doc):
    """Encodes a document.

    :param doc: Document being encoded.
    :type doc: object

    :returns: An encoded document representation.
    :rtype: dict

    """
    return _encode(doc)
