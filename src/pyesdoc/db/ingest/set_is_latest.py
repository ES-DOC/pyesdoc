"""
.. module:: set_is_latest.py
   :platform: Unix
   :synopsis: Sets document is latest index.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from .. import (
    dao,
    models,
    session
    )



def execute(ctx):
    """Creates document index.

    :param object ctx: Document processing context information.

    """
    # Get related documents (sorted by version).
    documents = dao.get_document(ctx.primary.Project_ID,
                                 ctx.primary.UID,
                                 models.DOCUMENT_VERSION_ALL)

    # Uodate flag accordingly.
    for index, document in enumerate(documents):
        document.IsLatest = (index == 0)

    # Commit changes.
    session.commit()
