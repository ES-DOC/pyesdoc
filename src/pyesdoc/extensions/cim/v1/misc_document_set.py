"""
.. module:: misc_document_set.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.misc.document_set document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def _extend_children(ctx):
    """Extends child documents."""
    # Note : JIT extension.
    from ...extender import extend as extend_doc

    children = []
    # children = children + ctx.doc.data
    children = children + ctx.doc.ensembles
    children = children + ctx.doc.grids
    children.append(ctx.doc.experiment)
    children.append(ctx.doc.model)
    children.append(ctx.doc.platform)
    children.append(ctx.doc.simulation)

    for child in children:
        if not child.meta.institute:
            child.meta.institute = ctx.doc.meta.institute
        extend_doc(child)


def _set_meta_info(ctx):
    """Sets document meta information."""
    simulation = ctx.doc.simulation
    if simulation:
        ctx.meta.create_date = simulation.meta.create_date
        ctx.meta.external_ids = simulation.meta.external_ids
        ctx.meta.id = simulation.meta.id
        ctx.meta.version = simulation.meta.version
    ctx.meta.type_display_name = "Simulation"
    ctx.meta.type_sort_key = "AC"


def _set_ext_info(ctx):
    """Sets document extension information."""
    simulation = ctx.doc.simulation
    if simulation:
        ctx.ext = ctx.doc.ext = simulation.ext
        ctx.ext.type = ctx.meta.type


# Set of extension functions.
EXTENDERS = (
    _extend_children,
    _set_meta_info,
    _set_ext_info,
    )
