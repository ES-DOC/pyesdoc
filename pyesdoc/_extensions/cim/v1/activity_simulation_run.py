"""
.. module:: activity_simulation_run.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.activity.simulation_run document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def get_extenders():
    """Returns set of extension functions.

    """
    return (
        _set_experiment_conformances,
        _set_responsible_parties
        )


def _set_experiment_conformances(ctx):
    """Sets conformance links.

    """
    ctx.ext.conformances = []
    for conformance in ctx.doc.conformances:
    	if len(conformance.requirements):
    		for requirement in conformance.requirements:
    			ctx.ext.conformances.append(requirement.name)
    ctx.ext.conformances = ", ".join(sorted(ctx.ext.conformances))


def _set_responsible_parties(ctx):
    """Sets sorted contacts list.

    """
    ctx.doc.responsible_parties = \
        sorted(ctx.doc.responsible_parties, key=lambda rp: rp.role)

