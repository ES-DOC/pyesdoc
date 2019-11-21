"""
.. module:: activity_numerical_experiment.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.activity.numerical_experiment document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def get_extenders():
    """Returns set of extension functions.

    """
    return (
        _set_full_experiment_name,
        )


def _set_full_experiment_name(ctx):
    """Sets full experiment name.

    """
    name = ""
    if ctx.doc.experiment_id is not None:
    	name += ctx.doc.experiment_id
    	name += " "
    name += ctx.doc.short_name

    ctx.ext.full_experiment_name = name

