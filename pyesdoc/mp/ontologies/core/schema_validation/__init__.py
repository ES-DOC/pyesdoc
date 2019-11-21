"""
.. module:: pyesdoc.mp.ontologies.core.schema_validation.__init__.py
   :platform: Unix, Windows
   :synopsis: Validates an ontology schema definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import inspect
import re

from pyesdoc.mp.ontologies.core.schema_validation.context import ValidationContext
from pyesdoc.mp.ontologies.core.schema_validation import class_validator
from pyesdoc.mp.ontologies.core.schema_validation import enum_validator
from pyesdoc.mp.ontologies.core.schema_validation import package_validator
from pyesdoc.mp.ontologies.core.schema_validation import schema_validator
from pyesdoc.mp.ontologies.core.schema_validation import type_validator



def validate(schema):
    """Validates ontology schema.

    :param module schema: Ontology schema definition.

    :returns: Set of validation errors (if any).
    :rtype: set

    """
    ctx = ValidationContext(schema)
    for validator in (
        schema_validator,
        package_validator,
        type_validator
        ):
        validator.validate(ctx)
        if ctx.report:
            break

    return ctx.report


def is_valid(schema):
    """Returns flag indicating whether the passed schema is deemed to be valid or not.

    :param module schema: An ontology schema definition.

    :returns: True if valid false otherwise.
    :rtype: bool

    """
    return len(validate(schema)) == 0
