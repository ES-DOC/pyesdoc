"""
.. module:: activity_numerical_experiment.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.activity.numerical_experiment document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def _set_type_display_info(ctx):
    """Sets document type information."""
    ctx.meta.type_display_name = ctx.ext.type_display_name = "Experiment"
    ctx.ext.type_sortkey = ctx.meta.type_sortkey = "AB"


def _set_full_experiment_name(ctx):
    """Sets full experiment name."""
    name = ""
    if ctx.doc.experiment_id is not None:
    	name += ctx.doc.experiment_id
    	name += " "
    name += ctx.doc.short_name

    ctx.ext.full_experiment_name = name


# Set of extension functions.
EXTENDERS = (
    _set_type_display_info,
    _set_full_experiment_name,
    )
