"""
.. module:: set_summary.py
   :platform: Unix
   :synopsis: Sets document summary index.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import sqlalchemy

from .. import (
    cache,
    models,
    session
    )
from ... import constants


def execute(ctx):
    """Creates document index.

    :param object ctx: Document processing context information.

    """
    # Initialise.
    idx = models.DocumentSummary()
    idx.Description = ctx.doc.ext.description
    idx.Document_ID = ctx.primary.ID
    idx.Language_ID = cache.get_id(models.DocumentLanguage,
                                   constants.ESDOC_DEFAULT_LANGUAGE)

    # Set fields.
    fields = [f for f in ctx.doc.ext.summary_fields if f is not None]
    for index, field in enumerate(fields):
        if index == 0:
            idx.ShortName = field
        elif index == 1:
            idx.LongName = field
        else:
            setattr(idx, 'Field_0' + str(index - 1), field)

    # Insert.
    try:
        session.insert(idx)
    except sqlalchemy.exc.IntegrityError:
        session.rollback()
