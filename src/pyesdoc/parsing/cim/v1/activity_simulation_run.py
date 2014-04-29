"""
.. module:: activity_simulation_run.py
   :platform: Unix, Windows
   :synopsis: Parses a cim.v1.activity.simulation_run document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def _set_type_display_name(ctx):
    """Sets document type display name."""
    ctx.meta.type_display_name = ctx.ext.type_display_name = "Simulation"


# Set of parsing functions.
PARSERS = (
    _set_type_display_name,
    )
