# -*- coding: utf-8 -*-
"""
.. module:: doc_parser.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document parsers.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from . import (
    doc_parser_cmip5_qc as cmip5_qc,
    doc_parser_cmip5_q as cmip5_q,
    doc_parser_esdoc_q
    )
from .. import io



# Set of document post-decoding handlers.
_PARSERS = {
    "cmip5": {
        "dkrz-qc": cmip5_qc,
        "metafor-q": cmip5_q
    },
    "esps": doc_parser_esdoc_q,
    "test": cmip5_qc
}

# Document type keys.
_TYPE_KEY_DOCUMENT_SET = 'cim.1.misc.documentset'



def _get_source_description(source):
    """Returns document source description."""
    for source_cfg in io.config.sources:
        if source_cfg.name == source:
            return source_cfg.description
    return source


def _get_parsing_module(project, source):
    """Returns parsing module that will handle parsing."""
    for index, getter in enumerate((
        lambda: _PARSERS[project][source],
        lambda: _PARSERS[source][project],
        lambda: _PARSERS[project],
        lambda: _PARSERS[source]
        )):
        try:
            return getter()
        except (TypeError, KeyError):
            pass


def _get_children(doc):
    """Unpacks child documents contained within document being processed.

    :param object doc: Document being processed.

    :returns: Collection of documents being processed.
    :rtype: list

    """
    children = []
    if doc.type_key.lower() == _TYPE_KEY_DOCUMENT_SET:
        children += [
            doc.experiment,
            doc.model,
            doc.platform,
            doc.simulation
            ]
        children += doc.data
        children += doc.ensembles
        children += doc.grids

    return [c for c in children if c]


def _set_meta_attributes(project, source, document):
    """Sets document meta attributes."""
    document.meta.project = unicode(project)
    document.meta.source = _get_source_description(source)
    document.meta.source_key = unicode(source)


def _set_default_institute(doc):
    """Set default institute name."""
    if doc.meta.institute is None:
        doc.meta.institute = "--"


def _set_default_language(doc):
    """Set default language code."""
    if doc.meta.language is None:
        doc.meta.language = "en"


def _get_default_parsers():
    """Factory function: returns default parsers."""
    return (
        _set_default_institute,
        _set_default_language
        )


def _get_parsers(project, source):
    """Returns set of document parsers to be invoked."""
    result = ()
    mod = _get_parsing_module(project, source)
    if mod:
        try:
            result += mod.get_parsers()
        except TypeError:
            result += (mod.get_parsers(), )
    result += _get_default_parsers()

    return result


def parse(project, source, document):
    """Parses document according to project & source.

    :param str project: Name of a project.
    :param str source: Document source.
    :param str document: Document being parsed.

    """
    # Set collection of documents to process.
    docs = [document] + _get_children(document)

    # Set common meta attributes.
    for doc in docs:
        _set_meta_attributes(project, source, doc)

    # Invoke parsers.
    for parser in _get_parsers(project, source):
        for doc in docs:
            parser(doc)
