# -*- coding: utf-8 -*-

"""
.. module:: designing_numerical_experiment.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.designing.numerical_experiment document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.constants import ESDOC_VIEWER_URL



def get_extenders():
    """Returns set of extension functions.

    """
    return (
        _set_related_experiment_viewer_urls,
        )


def _set_related_experiment_viewer_urls(ctx):
    """Sets related experiment viewer urls.

    """
    for ref in ctx.doc.related_experiments_references:
        ref.viewer_url = ESDOC_VIEWER_URL.format(ctx.meta.project, ref.id, ref.version)

