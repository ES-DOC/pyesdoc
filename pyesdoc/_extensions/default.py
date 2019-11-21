"""
.. module:: default.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Default document extender.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc import constants
from pyesdoc.ontologies import cim



def _set_full_id(ctx):
    """Sets full document identifier.

    """
    ctx.ext.full_id = "{}-{}".format(ctx.meta.id, ctx.meta.version)


def _set_type_info(ctx):
    """Sets document type information.

    """
    ctx.meta.type = ctx.ext.type = ctx.doc.__class__.type_key
    ctx.ext.css_class = ctx.ext.type.lower().replace(".", "-")
    ctx.meta.type_display_name = cim.constants.DISPLAY_NAMES.get(type(ctx.doc), ctx.meta.type.split(".")[-1])
    ctx.meta.type_sort_key = cim.constants.SORT_KEYS.get(type(ctx.doc), u"ZZ")


def _set_institute(ctx):
    """Sets document institute field.

    """
    if ctx.meta.institute:
        ctx.meta.institute = ctx.meta.institute.upper()
    else:
        ctx.meta.institute = constants.DEFAULT_INSTITUTE


def _set_project(ctx):
    """Sets document project field.

    """
    if ctx.meta.project:
        ctx.meta.project = ctx.meta.project.lower()
    else:
        ctx.meta.institute = constants.DEFAULT_PROJECT


def _set_summary_fields(ctx):
    """Sets document summary fields.

    """
    fields = ()
    if hasattr(ctx.doc, "short_name"):
        fields = fields + (ctx.doc.short_name, )
    elif hasattr(ctx.doc, "canonical_name"):
        fields = fields + (ctx.doc.canonical_name, )
    if hasattr(ctx.doc, "long_name"):
        fields = fields + (ctx.doc.long_name, )
    ctx.ext.summary_fields = fields


def _set_display_name(ctx):
    """Sets document display name.

    """
    ctx.ext.display_name = None
    if hasattr(ctx.doc, "short_name") and ctx.doc.short_name:
        ctx.ext.display_name = ctx.doc.short_name
    elif hasattr(ctx.doc, "name") and ctx.doc.name:
        ctx.ext.display_name = ctx.doc.name
    elif hasattr(ctx.doc, "title") and ctx.doc.title:
        ctx.ext.display_name = ctx.doc.title


def _set_description(ctx):
    """Sets document description.

    """
    ctx.ext.description = None
    if hasattr(ctx.doc, "description") and ctx.doc.description:
        ctx.ext.description = ctx.doc.description[:1023]
    elif hasattr(ctx.doc, "long_name") and ctx.doc.long_name:
        ctx.ext.description = ctx.doc.long_name[:1023]


def _set_viewer_url(ctx):
    """Sets document viewer URL.

    """
    ctx.ext.viewer_url = constants.VIEWER_URL_BY_ID.format(ctx.meta.project,
                                                           ctx.meta.id,
                                                           ctx.meta.version)

def _set_full_display_name(ctx):
    """Sets document full display name.

    """
    # Escape if already assigned.
    if ctx.ext.full_display_name:
        return

    name = u""
    if ctx.meta.project:
        name += ctx.meta.project.upper()
        name += u" "
    name += ctx.meta.type_display_name
    name += u" : "
    if ctx.meta.institute and ctx.meta.institute != u"--":
        name += ctx.meta.institute.upper()
        name += u" - "
    if ctx.ext.display_name:
        name += ctx.ext.display_name
        name += u" "

    ctx.ext.full_display_name = name.strip()


def _set_sort_key(ctx):
    """Sets document full display name.

    """
    ctx.meta.sort_key = u"{0}{1}".format(
        ctx.meta.type_sort_key, ctx.ext.display_name or unicode())
    ctx.meta.sort_key = ctx.meta.sort_key.upper()


# Set of pre-extenders.
PRE_EXTENDERS = (
    _set_full_id,
    _set_type_info,
    _set_institute,
    _set_project,
    _set_display_name,
    _set_description,
    _set_summary_fields,
    _set_viewer_url,
    )


# Set of post-extenders.
POST_EXTENDERS = (
    _set_full_display_name,
    _set_sort_key
    )

