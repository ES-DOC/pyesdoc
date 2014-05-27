"""
.. module:: data_data_object.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.data.data_object document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def _set_display_name(ctx):
    """Sets document display name."""
    ctx.ext.display_name = ctx.doc.acronym


def _set_type_display_info(ctx):
    """Sets document type information."""
    ctx.ext.type_display_name = ctx.meta.type_display_name = "Data Object"
    ctx.ext.type_sortkey = ctx.meta.type_sortkey = "CA"


def _set_summary_fields(ctx):
    """Sets document summary fields."""
    ctx.ext.summary_fields += (
        ctx.doc.acronym,
        ctx.doc.description
    )


# Set of extension functions.
EXTENDERS = (
    _set_display_name,
    _set_type_display_info,
    _set_summary_fields
    )
