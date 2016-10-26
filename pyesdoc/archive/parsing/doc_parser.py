# -*- coding: utf-8 -*-
"""
.. module:: doc_parser.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document parsers.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.archive import config
from pyesdoc.archive.parsing import doc_parser_cmip5_qc
from pyesdoc.archive.parsing import doc_parser_cmip5_q
from pyesdoc.archive.parsing import doc_parser_esdoc_q



# Set of document parsers mapped by encoding, project & source.
_PARSERS = {
    "xml-metafor-cim-v1": {
        "cmip5": {
            "dkrz-qc": doc_parser_cmip5_qc,
            "metafor-q": doc_parser_cmip5_q
        }
    },
    "xml": {
        "esps": {
            "esdoc-q": doc_parser_esdoc_q
        },
        "downscaling-metadata": {
            "esdoc-q": doc_parser_esdoc_q
        }
    }
}


# Document type keys.
_TYPE_KEY_DOCUMENT_SET = 'cim.1.misc.documentset'



def _get_source_description(source):
    """Returns document source description.

    """
    for source_cfg in config.get_sources():
        if source_cfg.name == source:
            return source_cfg.description
    return source


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
    """Sets document meta attributes.

    """
    document.meta.project = unicode(project)
    document.meta.source = _get_source_description(source)
    document.meta.source_key = unicode(source)


def _set_defaults(doc):
    """Set default institute name.

    """
    if doc.meta.institute is None:
        doc.meta.institute = u"--"


def _get_parsers(project, source):
    """Returns set of document parsers to be invoked."""
    result = ()
    mod = _get_parsing_module(project, source)
    if mod:
        try:
            result += mod.get_parsers()
        except TypeError:
            result += (mod.get_parsers(), )
    result += (_set_defaults, )

    return result


def parse(encoding, project, source, document):
    """Parses document according to project & source.

    :param encoding: Original document encoding.
    :param str project: Name of a supported project (e.g. cmip6).
    :param str source: Name of a document source (e.g. esdoc-q).
    :param object document: Document being parsed.

    """
    # Set collection of documents to process.
    docs = [document] + _get_children(document)

    # Set common meta attributes.
    for doc in docs:
        _set_meta_attributes(project, source, doc)

    # Invoke parser.
    try:
        parser = _PARSERS[encoding][project][source]
    except KeyError:
        pass
    else:
        for func in parser.PARSERS:
            for doc in docs:
                func(doc)

    # Set defaults.
    for doc in docs:
        _set_defaults(doc)
