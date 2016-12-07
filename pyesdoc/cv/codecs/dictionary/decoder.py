# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.codecs.dict.decoder.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Decodes a term from a python dictionary.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import arrow

from pyesdoc.cv.term import Term
from pyesdoc.cv.term_collection import TermCollection



def decode(obj):
    """Decodes a term from a dictionary.

    :param dict obj: Dictionary to be decoded.

    :returns: Decoded term.
    :rtype: pyesdoc.cv.Term

    """
    if 'meta' in obj:
        return _decode_term(obj)
    else:
        return _decode_termset(obj)


def _decode_term(obj):
    """Decodes a term from a dictionary.

    """
    term = Term(
        obj["meta"]["domain"],
        obj["meta"]["type"],
        obj["names"]["preferred"],
        obj["meta"]["status"]
        )
    term.aliases = obj["names"]["aliases"]
    term.alternative_name = obj["names"]["alternative"]
    term.alternative_url = obj["other"].get('alternativeURL')
    term.associations = obj["relations"]["associations"]
    term.create_date = arrow.get(obj["meta"]["create_date"]).datetime
    term.description = obj["other"].get('description')
    term.idx = obj["meta"]["idx"]
    term.labels = obj["labels"]
    term.parent = obj["relations"]["parent"]
    term.status = obj["meta"]["status"]
    term.uid = obj["meta"]["uid"]
    term.url = obj["other"].get('url')

    return term


def _decode_termset(obj):
    """Decodes a termset from a dictionary.

    """
    termset = TermCollection()
    termset.create_date = arrow.get(obj["create_date"]).datetime
    termset.domain = obj["domain"]
    termset.kind = obj["type"]
    termset.description = obj.get("description")
    termset.uid = obj["uid"]

    return termset
