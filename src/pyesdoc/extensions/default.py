# -*- coding: utf-8 -*-

"""
.. module:: default.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Default document extender.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from .. import constants



def _set_full_id(ctx):
    """Sets full document identifier."""
    ctx.ext.full_id = "{0}-{1}-{2}".format(
        ctx.meta.project, ctx.meta.id, ctx.meta.version)


def _set_type(ctx):
    """Sets document type information."""
    ctx.meta.type = ctx.ext.type = ctx.doc.__class__.type_key


def _set_type_display_info(ctx):
    """Sets document type display name."""
    ctx.meta.type_display_name = \
        ctx.ext.type_display_name = \
            ctx.meta.type.split(".")[-1]
    ctx.meta.type_sortkey = "ZZ"


def _set_language(ctx):
    """Sets document language."""
    if not ctx.meta.language:
        ctx.meta.language = constants.ESDOC_DEFAULT_LANGUAGE
    ctx.ext.language = ctx.meta.language


def _set_summary_fields(ctx):
    """Sets document summary fields."""
    fields = ()
    if hasattr(ctx.doc, "short_name"):
        fields = fields + (ctx.doc.short_name, )
    if hasattr(ctx.doc, "long_name"):
        fields = fields + (ctx.doc.long_name, )
    ctx.ext.summary_fields = fields


def _set_display_name(ctx):
    """Sets document display name."""
    ctx.ext.display_name = None
    if hasattr(ctx.doc, "short_name") and ctx.doc.short_name:
        ctx.ext.display_name = ctx.doc.short_name


def _set_description(ctx):
    """Sets document description."""
    ctx.ext.description = None
    if hasattr(ctx.doc, "description") and ctx.doc.description:
        ctx.ext.description = ctx.doc.description[:1023]
    elif hasattr(ctx.doc, "long_name") and ctx.doc.long_name:
        ctx.ext.description = ctx.doc.long_name[:1023]


def _set_full_display_name(ctx):
    """Sets document full display name."""
    name = ""
    if ctx.meta.project:
        name += ctx.meta.project
    name += " "
    name += ctx.meta.type_display_name
    name += " : "
    if ctx.meta.institute:
        name += ctx.meta.institute
        name += " - "
    if ctx.ext.display_name:
        name += ctx.ext.display_name
        name += " "

    ctx.ext.full_display_name = name.strip()


def _set_encodings(ctx):
    """Returns set of file encodings for the passed document."""
    encodings = constants.ESDOC_ENCODINGS_FILE
    if ctx.meta.type.startswith("cim.1"):
        encodings = encodings + (constants.METAFOR_CIM_XML_ENCODING,)

    ctx.ext.encodings = ctx.meta.encodings = list(encodings)


# Set of pre-extenders.
PRE_EXTENDERS = (
    _set_full_id,
    _set_type,
    _set_type_display_info,
    _set_language,
    _set_display_name,
    _set_description,
    _set_summary_fields,
    _set_encodings,
    )


# Set of post-extenders.
POST_EXTENDERS = (
    _set_full_display_name,
    )

