"""
.. module:: designing_numerical_experiment.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.designing.numerical_experiment document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc import constants



def get_extenders():
    """Returns set of extension functions.

    """
    return (
        _set_summary_fields,
        )


def _set_summary_fields(ctx):
    """Sets related experiment viewer urls.

    """
    ctx.ext.summary_fields = (
        ctx.doc.canonical_id.upper(),
        ctx.doc.long_name
    )
