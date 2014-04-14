"""
.. module:: data_data_object.py
   :platform: Unix, Windows
   :synopsis: Parses a cim.v1.data.data_object document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def _set_display_name(ctx):
    """Sets document display name."""
    ctx.ext.display_name = ctx.doc.acronym


def _set_type_display_name(ctx):
    """Sets document type display name."""
    ctx.ext.type_display_name = ctx.meta.type_display_name = "Data Object"


def _set_summary_fields(ctx):
    """Sets document summary fields."""
    ctx.ext.summary_fields += (
        ctx.doc.acronym,
        ctx.doc.description
    )


# Set of parsing functions.
PARSERS = (
    _set_display_name,
    _set_type_display_name,
    _set_summary_fields
    )
