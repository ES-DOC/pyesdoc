# -*- coding: utf-8 -*-

"""
.. module:: designing_project.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.designing.project document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.constants import VIEWER_URL_BY_ID
from pyesdoc.ontologies import cim



def get_extenders():
    """Returns set of extension functions.

    """
    return (
        _set_viewer_urls,
        _set_summary_fields
        )


def _set_viewer_urls(ctx):
    """Sets viewer urls.

    """
    for exp in ctx.doc.requires_experiments:
        if isinstance(exp, cim.v2.designing.NumericalExperiment):
            exp.viewer_url = VIEWER_URL_BY_ID.format(ctx.meta.project, exp.meta.id, exp.meta.version)
        elif isinstance(exp, cim.v2.shared.DocReference):
            exp.viewer_url = VIEWER_URL_BY_ID.format(ctx.meta.project, exp.id, exp.version)


def _set_summary_fields(ctx):
    """Sets related experiment viewer urls.

    """
    ctx.ext.summary_fields += (
        ctx.doc.canonical_name,
        ctx.doc.name,
        ctx.doc.long_name
    )

