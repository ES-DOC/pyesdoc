# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc._validation.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Validates a document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import re

from pyesdoc.ontologies.graph_parser import GraphParser
from pyesdoc import ontologies
from pyesdoc import constants



# Validation error text.
_ERR_CONSTANT = "constant value has been overwritten"
_ERR_LIST_IS_EMPTY = "is an empty list"
_ERR_LIST_CONTAINS_INVALID_ITEM_TYPES = "list contains item(s) of invalid type"
_ERR_LIST_TYPE = "is of invalid type (actual = {0}, expected=list)"
_ERR_HIDDEN = "hidden property has been assigned"
_ERR_ITEM_IS_NULL = "is null"
_ERR_ITEM_TYPE = "is of invalid type (actual = {0}, expected={1})"
_ERR_ITEM_IS_EMPTY_TEXT = "is zero length"
_ERR_ITEM_IS_LIST = "is a list, expected a complex or ximple type"
_ERR_REGEX = "regular expression validation failed"

# Type of document references.
_DOCUMENT_REFERENCE_TYPE = "DocReference"

# Set of text types.
_TEXT_TYPES = (str, unicode)


def _validate_cardinality(value, expected_cardinality):
    """Cardinality constraint validator.

    """
    if expected_cardinality == constants.CARDINALITY_TYPE_0_0:
        if value not in (None, []):
            return _ERR_HIDDEN

    elif expected_cardinality == constants.CARDINALITY_TYPE_0_1:
        if isinstance(value, list):
            return _ERR_ITEM_IS_LIST

    elif expected_cardinality == constants.CARDINALITY_TYPE_1_1:
        if isinstance(value, list):
            return _ERR_ITEM_IS_LIST
        if value is None:
            return _ERR_ITEM_IS_NULL

    elif expected_cardinality == constants.CARDINALITY_TYPE_1_N:
        if not isinstance(value, list):
            return _ERR_LIST_TYPE.format(type(value))
        if len(value) == 0:
            return _ERR_LIST_IS_EMPTY

    elif expected_cardinality == constants.CARDINALITY_TYPE_0_N:
        if not isinstance(value, list):
            return _ERR_LIST_TYPE.format(type(value))


def _validate_constant(value, expected_constant):
    """Constant constraint validator.

    """
    if not expected_constant:
        return

    elif value != expected_constant:
        return _ERR_CONSTANT


def _validate_regex(value, regex):
    """Regular expression constraint validator.

    """
    if not regex:
        return

    elif not re.match(regex, str(value)):
        return _ERR_REGEX


def _validate_type(value, expected_type):
    """Type constraint validator.

    """
    def _is_type_mismatch(instance):
        """Validates that a complex type matches.

        """
        if isinstance(instance, expected_type):
            return False

        if expected_type in ontologies.type_info.TYPES and \
           type(instance).__name__.split(".")[-1] == _DOCUMENT_REFERENCE_TYPE:
            return False

        return True


    # Escape if unncessary.
    if value in (None, []):
        return

    # Validate collections.
    if isinstance(value, list):
        if [i for i in value if _is_type_mismatch(i)]:
            return _ERR_LIST_CONTAINS_INVALID_ITEM_TYPES

    # Assert non text.
    elif expected_type not in _TEXT_TYPES:
        if _is_type_mismatch(value):
            return _ERR_ITEM_TYPE.format(type(value), expected_type)

    # Assert text.
    elif not isinstance(value, _TEXT_TYPES):
        return _ERR_ITEM_TYPE.format(type(value), expected_type)

    # Assert text length.
    elif len(value.strip()) == 0:
        return _ERR_ITEM_IS_EMPTY_TEXT


# Set of property validators to be executed.
_VALIDATORS = (
    (constants.CONSTRAINT_TYPE_CARDINALITY, _validate_cardinality),
    (constants.CONSTRAINT_TYPE_TYPEOF, _validate_type),
    (constants.CONSTRAINT_TYPE_CONSTANT, _validate_constant),
    (constants.CONSTRAINT_TYPE_REGEX, _validate_regex),
    )


class _GraphParserValidator(GraphParser):
    """A graph parser that performs validation.

    """
    def __init__(self):
        """Instance initializer.

        """
        self.errors = []


    def on_property_parse(self, container, path, name, value):
        """Property parsed event handler.

        """
        for constraint_type, validator in _VALIDATORS:
            error = validator(value, ontologies.get_property_constraint(container, name, constraint_type))
            if error:
                self.errors.append("doc{} --> {}".format(path, error))
                return


def validate(doc):
    """Validates a document.

    :param object doc: A pyesdoc document instance.

    :returns: A list of validation errors.
    :rtype: list

    """
    parser = _GraphParserValidator()
    parser.parse(doc)

    return parser.errors


def is_valid(doc):
    """Returns validation status of a document.

    :param object doc: A pyesdoc document instance.

    :returns: The document's validation state.
    :rtype: bool

    """
    return len(validate(doc)) == 0

