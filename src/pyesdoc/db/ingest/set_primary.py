"""
.. module:: set_primary.py
   :platform: Unix
   :synopsis: Sets document primary index.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import sqlalchemy

from .. import (
    cache,
    models,
    session
    )


def execute(ctx):
    """Creates document index.

    :param object ctx: Document processing context information.

    """
    # Unpack helper vars.
    doc = ctx.doc

    # Instantiate.
    idx = models.Document()
    idx.Institute_ID = cache.get_institute_id(doc.meta.institute)
    idx.Name = doc.ext.display_name
    idx.Project_ID = cache.get_project_id(doc.meta.project)
    idx.Source_Key = doc.meta.source_key
    idx.Type = doc.meta.type
    idx.UID = unicode(doc.meta.id)
    idx.Version = doc.meta.version

    # Insert.
    try:
        session.insert(idx)
    except sqlalchemy.exc.IntegrityError:
        ctx.stop()
        session.rollback()
    finally:
        ctx.primary = idx
