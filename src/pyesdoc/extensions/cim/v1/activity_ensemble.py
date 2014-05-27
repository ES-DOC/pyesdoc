"""
.. module:: activity_ensemble.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.activity.ensemble document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def _set_type_display_info(ctx):
    """Sets document type information."""
    ctx.ext.type_sortkey = ctx.meta.type_sortkey = "BC"


def _set_member_short_name(ctx):
    """Sets ensemble member short names."""
    for member in ctx.doc.members:
    	if not member.short_name and len(member.ensemble_ids):
    		member.short_name = member.ensemble_ids[0].value


# Set of extension functions.
EXTENDERS = (
	_set_type_display_info,
    _set_member_short_name,
    )
