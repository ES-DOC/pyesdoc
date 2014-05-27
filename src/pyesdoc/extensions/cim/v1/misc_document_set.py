"""
.. module:: misc_document_set.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.misc.document_set document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def _set_meta_info(ctx):
    """Sets document meta information."""
    if ctx.doc.simulation:
        ctx.meta.create_date = ctx.doc.simulation.meta.create_date
        ctx.meta.id = ctx.doc.simulation.meta.id
        ctx.meta.version = ctx.doc.simulation.meta.version


def _set_display_name(ctx):
    """Sets document display name."""
    pass


def _set_type_display_info(ctx):
    """Sets document type display name."""
    pass


def _set_summary_fields(ctx):
    """Sets document summary fields."""
    pass


# Set of extension functions.
EXTENDERS = (
    _set_meta_info,
    _set_display_name,
    _set_type_display_info,
    _set_summary_fields
    )
