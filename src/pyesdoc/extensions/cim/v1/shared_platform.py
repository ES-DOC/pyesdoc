"""
.. module:: shared_platform.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.shared.platform document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def get_extenders():
    """Returns set of extension functions."""
    return (
        _set_type_display_info,
        )


def _set_type_display_info(ctx):
    """Sets document type information."""
    ctx.meta.type_sort_key = "BA"

