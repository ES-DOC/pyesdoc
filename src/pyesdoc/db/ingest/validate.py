"""
.. module:: validate.py
   :platform: Unix
   :synopsis: Sets Performs pre-ingest document validation.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import uuid

from .. import cache
from ... import ontologies



# Set of document types that do not need to be associated with an institute.
_INSTITUTE_VALIDATION_EXCEPIONS = (
    ontologies.cim.v1.NumericalExperiment,
    )


def _validate_id(ctx):
    """Validates document id."""
    # Is mandatory.
    if not ctx.doc.meta.id:
        ctx.stop("ID is mandatory")

    # Is a UUID.
    if not type(ctx.doc.meta.id) == uuid.UUID:
        try:
            ctx.doc.meta.id = uuid.UUID(ctx.doc.meta.id)
        except (ValueError, TypeError):
            msg = "ID must be a universally unique identifer (UUID): {0}"
            msg = msg.format(ctx.doc)
            ctx.stop(msg)


def _validate_version(ctx):
    """Validates document version."""
    # Is mandatory.
    if not ctx.doc.meta.version:
        ctx.stop("Version is mandatory: {0}".format(type(ctx.doc)))

    # Is an integer.
    if not type(ctx.doc.meta.version) == int:
        try:
            ctx.doc.meta.version = int(ctx.doc.meta.version)
        except TypeError:
            ctx.stop("Version must be an integer")

    # Is a positive integer.
    if not ctx.doc.meta.version > 0:
        ctx.stop("Version must be a positive integer")


def _validate_project(ctx):
    """Validates project code."""
    # Is mandatory.
    if not ctx.doc.meta.project:
        ctx.stop("Project code is mandatory")

    # Is controlled vocabulary.
    if not cache.get_project(ctx.doc.meta.project):
        err = "Project code is unsupported: {0}"
        ctx.stop(err.format(ctx.doc.meta.project))


def _validate_institute(ctx):
    """Validates institute code."""
    # Is sometimes mandatory.
    if not ctx.doc.meta.institute:
        if type(ctx.doc) not in _INSTITUTE_VALIDATION_EXCEPIONS:
            ctx.stop("Institute code is mandatory")
        else:
            return

    # Is controlled vocabulary.
    if not cache.get_institute(ctx.doc.meta.institute):
        err = "Institute code is unsupported: {0}"
        ctx.stop(err.format(ctx.doc.meta.institute))


def _validate_name(ctx):
    """Validates name."""
    # Is mandatory.
    if not ctx.doc.ext.display_name:
        ctx.stop("Name is mandatory")


# Set of validators to apply.
_VALIDATORS = (
    _validate_id,
    _validate_version,
    _validate_institute,
    _validate_project,
    _validate_name
    )


def execute(ctx):
    """Validates document prior to ingestion.

    :param object ctx: Document processing context information.

    """
    # Validate
    for func in _VALIDATORS:
        func(ctx)

