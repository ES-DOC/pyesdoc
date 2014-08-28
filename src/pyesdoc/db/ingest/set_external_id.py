"""
.. module:: set_external_id.py
   :platform: Unix
   :synopsis: Sets document external id index.

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
    # Escape if there is no external id defined.
    if not len(ctx.doc.meta.external_ids):
    	return

    # Pick up first external id.
    external_id = ctx.doc.meta.external_ids[0]

    # Insert.
    idx = models.DocumentExternalID()
    idx.Project_ID = ctx.primary.Project_ID
    idx.Document_ID = ctx.primary.ID
    idx.ExternalID = external_id.value.upper()

    # Insert.
    try:
        session.insert(idx)
    except sqlalchemy.exc.IntegrityError:
        session.rollback()
