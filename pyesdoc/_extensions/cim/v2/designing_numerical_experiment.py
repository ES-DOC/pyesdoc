"""
.. module:: designing_numerical_experiment.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.designing.numerical_experiment document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc import constants



def get_extenders():
    """Returns set of extension functions.

    """
    return (
        _set_viewer_urls,
        _set_summary_fields,
        _set_full_display_name
        )


def _set_viewer_urls(ctx):
    """Sets related experiment viewer urls.

    """
    for i in ctx.doc.related_experiments + ctx.doc.related_mips:
        try:
            i.meta
        except AttributeError:
            i.viewer_url = constants.VIEWER_URL_BY_ID.format(ctx.meta.project, i.id, i.version)
        else:
            i.viewer_url = constants.VIEWER_URL_BY_ID.format(ctx.meta.project, i.meta.id, i.meta.version)


def _set_summary_fields(ctx):
    """Sets related experiment viewer urls.

    """
    ctx.ext.summary_fields += (
        ctx.doc.canonical_name,
        ctx.doc.name,
        ctx.doc.long_name
    )


def _set_full_display_name(ctx):
    """Sets document full display name.

    """
    ctx.ext.full_display_name = "{} Tier {} Experiment: {}".format(
        ctx.meta.project.upper(),
        ctx.doc.tier,
        ctx.ext.display_name
        ).strip()
