"""
.. module:: designing_project.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.designing.project document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import collections

from pyesdoc import constants
from pyesdoc.ontologies import cim



def get_extenders():
    """Returns set of extension functions.

    """
    return (
        _set_viewer_urls,
        _set_summary_fields,
        _set_tiered_experiments,
        _set_other_experiments
        )


def _set_viewer_urls(ctx):
    """Sets viewer urls.

    """
    for exp in ctx.doc.required_experiments + ctx.doc.governed_experiments:
        if isinstance(exp, cim.v2.designing.NumericalExperiment):
            exp.viewer_url = constants.VIEWER_URL_BY_ID.format(ctx.meta.project, exp.meta.id, exp.meta.version)
        elif isinstance(exp, cim.v2.shared.DocReference):
            exp.viewer_url = constants.VIEWER_URL_BY_ID.format(ctx.meta.project, exp.id, exp.version)

    for p in ctx.doc.sub_projects:
        if isinstance(p, cim.v2.designing.Project):
            p.viewer_url = constants.VIEWER_URL_BY_ID.format(ctx.meta.project, p.meta.id, p.meta.version)
        elif isinstance(p, cim.v2.shared.DocReference):
            p.viewer_url = constants.VIEWER_URL_BY_ID.format(ctx.meta.project, p.id, p.version)


def _set_summary_fields(ctx):
    """Sets related experiment viewer urls.

    """
    ctx.ext.summary_fields += (
        ctx.doc.canonical_name,
        ctx.doc.name,
        ctx.doc.long_name
    )


def _set_tiered_experiments(ctx):
    """Groups governed experiments by tier.

    """
    tiered_experiments = collections.defaultdict(list)
    for e in ctx.doc.governed_experiments:
        if e.further_info is not None:
            tiered_experiments[e.further_info].append(e)
    ctx.ext.tiered_experiments = tiered_experiments


def _set_other_experiments(ctx):
    """Sets non-governed experiments.

    """
    governed_experiments = [j.name for j in ctx.doc.governed_experiments]
    ctx.ext.other_experiments = [i for i in ctx.doc.required_experiments
                                 if i.name not in governed_experiments]

