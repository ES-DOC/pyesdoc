"""
.. module:: set_external_id.py
   :platform: Unix
   :synopsis: Sets document DRS index.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import sqlalchemy

from .. import (
    models,
    session
    )



def execute(ctx):
    """Creates document index.

    :param object ctx: Document processing context information.

    """
    # Escape if there are no DRS keys defined.
    if not ctx.doc.meta.drs_path:
        return

    # Instantiate.
    idx = models.DocumentDRS()
    idx.Document_ID = ctx.primary.ID
    idx.Path = ctx.doc.meta.drs_path
    idx.Project_ID = ctx.primary.Project_ID

    # Set keys.
    for index, key in enumerate(ctx.doc.meta.drs_keys):
        if index > 7:
            break
        elif key is not None:
            setattr(idx, "Key_0" + str(index + 1), key.upper())

    # Insert.
    try:
        session.insert(idx)
    except sqlalchemy.exc.IntegrityError:
        session.rollback()
