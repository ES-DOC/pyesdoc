"""
.. module:: misc_document_set.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.misc.document_set document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def get_extenders():
    """Returns set of extension functions.

    """
    return (
        _propogate_institute,
        _propogate_meta_info,
        _propogate_ext_info,
        )


def unpack_children(ctx):
    """Unpacks child documents.

    """
    children = [
        ctx.doc.experiment,
        ctx.doc.model,
        ctx.doc.platform,
        ctx.doc.simulation
        ]
    children += ctx.doc.data
    children += ctx.doc.ensembles
    children += ctx.doc.grids

    ctx.ext.children = [c for c in children if c]


def _propogate_meta_info(ctx):
    """Propogates document meta information.

    """
    if ctx.doc.simulation:
        simulation = ctx.doc.simulation
        ctx.meta.create_date = simulation.meta.create_date
        ctx.meta.external_ids = simulation.meta.external_ids
        ctx.meta.id = simulation.meta.id
        ctx.meta.version = simulation.meta.version


def _propogate_ext_info(ctx):
    """Propogates document extension information.

    """
    if ctx.doc.simulation:
        simulation = ctx.doc.simulation
        for field in (
            'display_name',
            'description',
            'summary_fields',
            'full_display_name'
            ):
            setattr(ctx.ext, field, getattr(simulation.ext, field))


def _propogate_institute(ctx):
    """Propogates institute code.

    """
    for child in ctx.ext.children:
        if not child.meta.institute:
            child.meta.institute = ctx.doc.meta.institute
