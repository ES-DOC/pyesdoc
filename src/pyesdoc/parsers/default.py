# -*- coding: utf-8 -*-

"""
.. module:: default.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Default document parser.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from .. import defaults


def _set_type(doc):
    """Sets document type information."""
    doc._type = doc.doc_info.type = doc.__class__.type_key


def _set_type_display_name(doc):
    """Sets document type display name."""
    doc._type_display_name = doc.doc_info.type_display_name = doc.doc_info.type.split(".")[-1]  


def _set_language(doc):
    """Sets document language."""
    if doc.doc_info.language is None or not len(doc.doc_info.language):
        doc.doc_info.language = defaults.ESDOC_DEFAULT_LANGUAGE
    doc._language = doc.doc_info.language


def _set_summary_fields(doc):
    """Sets document summary fields."""
    fields = ()
    if hasattr(doc, "short_name"):
        fields = fields + (doc.short_name, )
    if hasattr(doc, "long_name"):
        fields = fields + (doc.long_name, )
    doc._summary_fields = fields


def _set_display_name(doc):
    """Sets document display name."""
    if hasattr(doc, "short_name"):
        doc._display_name = doc.short_name
    else:
        doc._display_name = None


def _set_description(doc):
    """Sets document description."""
    if hasattr(doc, "description"):
        doc._description = None if doc.description is None else doc.description[:1023]
    else:
        doc._description = None


def _set_full_display_name(doc):
    """Sets document full display name."""
    name = ""
    if doc.doc_info.project:
        name += doc.doc_info.project
    name += " "
    name += doc._type_display_name
    name += " : "
    if doc.doc_info.institute:
        name += doc.doc_info.institute
        name += " - "
    if doc._display_name:
        name += doc._display_name
        name += " "

    doc._full_display_name = name.strip()


# Set of pre-parsers.
_pre_parsers = (
    _set_type,
    _set_type_display_name, 
    _set_language,
    _set_display_name, 
    _set_description,
    _set_summary_fields,
    )


# Set of post-parsers.
_post_parsers = (
    _set_full_display_name, 
    )


def pre_parse(doc):
    """Performs default document pre-parsing.

    :param object doc: A document to be parsed.

    """
    for parser in _pre_parsers:
        parser(doc)


def post_parse(doc):
    """Performs default document pre-parsing.

    :param object doc: A document to be parsed.

    """
    for parser in _post_parsers:
        parser(doc)
