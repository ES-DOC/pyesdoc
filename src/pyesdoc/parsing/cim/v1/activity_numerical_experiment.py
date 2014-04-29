"""
.. module:: activity_numerical_experiment.py
   :platform: Unix, Windows
   :synopsis: Parses a cim.v1.activity.numerical_experiment document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def _set_type_display_name(ctx):
    """Sets document type display name."""
    ctx.meta.type_display_name = ctx.ext.type_display_name = "Experiment"


# Set of parsing functions.
PARSERS = (
    _set_type_display_name,
    )
