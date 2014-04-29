"""
.. module:: activity_ensemble.py
   :platform: Unix, Windows
   :synopsis: Parses a cim.v1.activity.ensemble document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def _set_member_short_name(ctx):
    """Sets ensemble member short names."""
    for member in ctx.doc.members:
    	if not member.short_name and len(member.ensemble_ids):
    		member.short_name = member.ensemble_ids[0].value


# Set of parsing functions.
PARSERS = (
    _set_member_short_name,
    )
