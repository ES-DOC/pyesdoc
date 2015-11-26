# -*- coding: utf-8 -*-

"""
.. module:: activity_ensemble.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.activity.ensemble document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def get_extenders():
    """Returns set of extension functions."""
    return (
        _set_member_short_name,
        _set_has_changes
        )


def _set_member_short_name(ctx):
    """Sets ensemble member short names."""
    for member in ctx.doc.members:
    	if not member.short_name and len(member.ensemble_ids):
    		member.short_name = member.ensemble_ids[0].value


def _set_has_changes(ctx):
    """Sets a flag indicating whether ensemble has member level changes."""
    ctx.ext.has_changes = False
    for member in ctx.doc.members:
        if member.simulation_reference.changes:
            ctx.ext.has_changes = True
            return
