"""
.. module:: grids_grid_spec.py
   :platform: Unix, Windows
   :synopsis: Parses a cim.v1.grids.grid_spec document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def _set_display_name(ctx):
    """Sets document display name."""
    if len(ctx.doc.esm_model_grids):
        ctx.ext.display_name = ctx.doc.esm_model_grids[0].short_name
    elif len(ctx.doc.esm_exchange_grids):
        ctx.ext.display_name = ctx.doc.esm_exchange_grids[0].short_name


def _set_type_display_name(ctx):
    """Sets document type display name."""
    ctx.ext.type_display_name = ctx.meta.type_display_name = "Grid Spec"


def _set_description(ctx):
    """Sets document description."""
    if len(ctx.doc.esm_model_grids):
        ctx.ext.description = ctx.doc.esm_model_grids[0].long_name
    elif len(ctx.doc.esm_exchange_grids):
        ctx.ext.description = ctx.doc.esm_exchange_grids[0].long_name


def _set_ids(ctx):
    """Sets document id."""
    for grid in ctx.doc.esm_model_grids + ctx.doc.esm_exchange_grids:
        if not grid.id:
            grid.id = grid.short_name


def _set_summary_fields(ctx):
    """Sets document summary fields."""
    if len(ctx.doc.esm_model_grids):
    	ctx.ext.summary_fields += (
            ctx.doc.esm_model_grids[0].short_name,
            ctx.doc.esm_model_grids[0].long_name
        )
    elif len(ctx.doc.esm_exchange_grids):
    	ctx.ext.summary_fields += (
            ctx.doc.esm_exchange_grids[0].short_name,
            ctx.doc.esm_exchange_grids[0].long_name
        )


# Set of parsing functions.
PARSERS = (
    _set_display_name,
    _set_type_display_name,
    _set_description,
    _set_ids,
    _set_summary_fields,
    )
