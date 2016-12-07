# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv.codecs.dict.encoder.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encodes a term to a python dictionary.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.cv.exceptions import EncodingError
from pyesdoc.cv.term import Term
from pyesdoc.cv.term_collection import TermCollection



def encode(data):
    """Encodes a term as a dictionary.

    :param pyesdoc.cv.Term term: Term to be encoded.

    :returns: Dictionary encoded term.
    :rtype: dict

    """
    if isinstance(data, Term):
        return _encode_term(data)
    elif isinstance(data, TermCollection):
        return _encode_termset(data)

    raise EncodingError(data)


def _encode_termset(termset):
    """Encodes a termset as a dictionary.

    """
    return {
        "create_date": termset.create_date,
        "domain": termset.domain,
        "type": termset.kind,
        "uid": termset.uid,
        "description": termset.description
    }


def _encode_term(term):
    """Encodes a term as a dictionary.

    """
    return {
        "labels": term.labels,
        "meta": {
            "create_date": term.create_date,
            "domain": term.domain,
            "idx": term.idx,
            "status": term.status,
            "type": term.kind,
            "uid": term.uid
        },
        "names": {
            "aliases": sorted(term.aliases),
            "alternative": term.alternative_name,
            "preferred": term.name
        },
        "other": {
            "alternativeURL": term.alternative_url,
            "description": term.description,
            "url": term.url
        },
        "relations": {
            "associations": sorted(term.associations),
            "parent": term.parent
        }
    }
