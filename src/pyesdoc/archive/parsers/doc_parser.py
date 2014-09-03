"""
.. module:: doc_parser.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document parsers.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from . import (
    doc_parser_cmip5_dkrz_qc as cmip5_dkrz_qc,
    doc_parser_cmip5_metafor_q as cmip5_metafor_q,
    doc_parser_esdoc_q as esdoc_q
    )
from .. import io



# Set of document post-decoding handlers.
_PARSERS = {
    "cmip5": {
        "dkrz-qc": cmip5_dkrz_qc.PARSERS,
        "metafor-q": cmip5_metafor_q.PARSERS
    },
    "esdoc-q": esdoc_q.PARSERS
}


def _get_source_description(source_key):
    """Returns document source description."""
    for source in io.config.sources:
        if source.name == source_key:
            return source.description
    return source_key


def _get_parsers(project, source):
    """Returns parsers to be invoked."""
    try:
        return _PARSERS[project][source]
    except KeyError:
        try:
            return _PARSERS[source]
        except KeyError:
            return ()


def _set_meta_attributes(project, source, document):
    """Sets document meta attributes."""
    document.meta.project = unicode(project)
    document.meta.source = _get_source_description(source)
    document.meta.source_key = unicode(source)


def parse(project, source, document):
    """Parses document according to project & source.

    :param str project: Name of a project.
    :param str source: Document source.
    :param str document: Document being parsed.

    """
    _set_meta_attributes(project, source, document)
    for parser in _get_parsers(project, source):
        parser(document)
