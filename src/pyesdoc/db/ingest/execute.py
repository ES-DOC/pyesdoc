"""
.. module:: execute.py
   :platform: Unix
   :synopsis: Executes ingestion process from document archive.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from . import (
    set_drs,
    set_external_id,
    set_is_latest,
    set_primary,
    set_summary,
    validate
    )
from ... import archive



# Set of document handlers (N.B. order matters).
_DOC_HANDLERS = (
    validate,
    set_primary,
    set_is_latest,
    set_summary,
    set_drs,
    set_external_id,
    )


class _DocumentProcessingInfo(object):
    """Encapsulates document processing information."""
    def __init__(self, document):
        """Constructor."""
        self.abort = False
        self.doc = document


    def stop(self, msg=None):
        """Stops processing.

        :param str msg: Halt reason message.

        """
        self.abort = True
        self.abort_reason = msg


def do(throttle=0, type_filter=None):
    """Creates document index.

    :param int throttle: Limits the number of documents to process.
    :param str type_filter: Limits the type of documents to process.

    """
    # Iterate yielded documents.
    processed = 0
    for document in archive.yield_organized_documents(type_filter):
        print "PROCESSING DOC: ", document.meta.id, document.meta.version
        # Execute document handlers.
        ctx = _DocumentProcessingInfo(document)
        for handler in _DOC_HANDLERS:
            handler.execute(ctx)
            if ctx.abort:
                break

        # Perform post processing tasks.
        processed = processed + 1
        if ctx.abort and ctx.abort_reason:
            print "TODO: log ingest error: {0}".format(ctx.abort_reason)
        if throttle:
            if throttle == processed:
                break
