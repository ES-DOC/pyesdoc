"""
.. module:: activity_simulation_run.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.activity.simulation_run document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def _set_type_display_info(ctx):
    """Sets document type information."""
    ctx.meta.type_display_name = "Simulation"
    ctx.meta.type_sort_key = "AC"


def _set_experiment_conformances(ctx):
    """Sets conformance links."""
    ctx.ext.conformances = []
    for conformance in ctx.doc.conformances:
    	if len(conformance.requirements_references):
    		for requirement_reference in conformance.requirements_references:
    			ctx.ext.conformances.append(requirement_reference.name)
    ctx.ext.conformances = ", ".join(ctx.ext.conformances)


# Set of extension functions.
EXTENDERS = (
    _set_type_display_info,
    _set_experiment_conformances,
    )
