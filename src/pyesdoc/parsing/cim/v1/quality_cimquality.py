"""
.. module:: quality_cim_quality.py
   :platform: Unix, Windows
   :synopsis: Parses a cim.v1.quality.cim_quality document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def _set_display_name(ctx):
    """Sets document display name."""
    if len(ctx.doc.reports) and ctx.doc.reports[0].measure is not None:
        ctx.ext.display_name = ctx.doc.reports[0].measure.name


def _set_type_display_name(ctx):
    """Sets document type display name."""
    ctx.ext.type_display_name = ctx.meta.type_display_name = "QC Record"


def _set_description(ctx):
    """Sets document description."""
    if len(ctx.doc.reports) and ctx.doc.reports[0].measure is not None:
        ctx.ext.description = ctx.doc.reports[0].measure.name


def _set_summary_fields(ctx):
    """Sets document summary fields."""
    if len(ctx.meta.external_ids):
        ctx.ext.summary_fields += (
            ctx.meta.external_ids[0].value,
        )


# Set of parsing functions.
PARSERS = (
    _set_display_name,
    _set_type_display_name,
    _set_description,
    _set_summary_fields
    )