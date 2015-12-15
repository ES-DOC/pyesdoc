# -*- coding: utf-8 -*-
"""
.. module:: content_parser.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document content parsers.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.archive.parsing import content_parser_cmip5_metafor_q



# Set of content parsers mapped by encoding, project & source.
_PARSERS = {
    "xml-metafor-cim-v1": {
        "cmip5": {
            "metafor-q": content_parser_cmip5_metafor_q
        }
    }
}


def parse(encoding, project, source, content):
    """Parses document content according to project & source.

    :param encoding: Original content encoding.
    :param str project: Name of a supported project (e.g. cmip6).
    :param str source: Name of a document source (e.g. esdoc-q).
    :param unicode content: Document content.

    """
    try:
        parser = _PARSERS[encoding][project][source]
    except KeyError:
        pass
    else:
        for func in parser.PARSERS:
            content = func(content) or content

    return content
