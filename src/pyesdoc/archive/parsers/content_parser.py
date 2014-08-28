"""
.. module:: content_parser.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document content parsers.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from . import (
    content_parser_cmip5_metafor_q as cmip5_metafor_q,
    content_parser_esdoc_q as esdoc_q
    )



# Set of document content parsers.
_PARSERS = {
    "cmip5": {
        "metafor-q": cmip5_metafor_q.PARSERS
    },
    "esdoc-q": esdoc_q.PARSERS,
}


def _get_parsers(project, source):
    """Returns parsers to be invoked."""
    try:
        return _PARSERS[project][source]
    except KeyError:
        try:
            return _PARSERS[source]
        except KeyError:
            return ()


def parse(project, source, content):
    """Parses document content according to project & source.

    :param str project: Name of a project.
    :param str source: Document source.
    :param str content: Document content.

    """
    for parser in _get_parsers(project, source):
        content = parser(content) or content

    return content
