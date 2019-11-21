"""
.. module:: data_data_object.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.data.data_object document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def get_extenders():
    """Returns set of extension functions.

    """
    return (
        _set_display_name,
        _set_summary_fields
        )


def _set_display_name(ctx):
    """Sets document display name.

    """
    ctx.ext.display_name = ctx.doc.acronym


def _set_summary_fields(ctx):
    """Sets document summary fields.

    """
    ctx.ext.summary_fields += (
        ctx.doc.acronym,
        ctx.doc.description
    )
