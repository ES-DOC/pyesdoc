# -*- coding: utf-8 -*-

"""
.. module:: designing_numerical_experiment.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v2.designing.numerical_experiment document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def get_extenders():
    """Returns set of extension functions."""
    return (
        _set_type_display_info,
        )


def _set_type_display_info(ctx):
    """Sets document type information."""
    ctx.meta.type_display_name = "Experiment"
    ctx.meta.type_sort_key = "AB"

