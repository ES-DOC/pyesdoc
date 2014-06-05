"""
.. module:: shared_platform.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.shared.platform document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def _set_type_display_info(ctx):
    """Sets document type information."""
    ctx.meta.type_sort_key = "BA"


# Set of extension functions.
EXTENDERS = (
    _set_type_display_info,
    )
