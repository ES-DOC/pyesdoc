# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.validation.validator.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Validates a document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import re

from pyesdoc.validation.graph import ValidationGraph
from pyesdoc import ontologies
from pyesdoc import constants



# Validation error text.
_ERR_LIST_IS_EMPTY = "is an empty list"
_ERR_LIST_CONTAINS_INVALID_ITEM_TYPES = "list contains item(s) of invalid type"
_ERR_LIST_TYPE = "is of invalid type (actual = {0}, expected=list)"
_ERR_ITEM_IS_NULL = "is null"
_ERR_ITEM_TYPE = "is of invalid type (actual = {0}, expected={1})"
_ERR_ITEM_IS_EMPTY_TEXT = "is zero length"
_ERR_ITEM_IS_LIST = "is a list, expected a complex or ximple type"
_ERR_HIDDEN = "Hidden attribute has been assigned"

# Type of document references.
_DOCUMENT_REFERENCE_TYPE = "DocReference"

# Set of text types.
_TEXT_TYPES = {str, unicode}


def _validate_cardinality(node):
    """Cardinality constraint validator.

    """
    if node.expected_cardinality == constants.CARDINALITY_TYPE_0_0:
        if node.value not in (None, []):
            _ERR_HIDDEN

    elif node.expected_cardinality == constants.CARDINALITY_TYPE_0_1:
        if node.value_type == list:
            return _ERR_ITEM_IS_LIST

    elif node.expected_cardinality == constants.CARDINALITY_TYPE_1_1:
        if node.value_type == list:
            return _ERR_ITEM_IS_LIST
        if node.value is None:
            return _ERR_ITEM_IS_NULL

    elif node.expected_cardinality == constants.CARDINALITY_TYPE_1_N:
        if node.value_type != list:
            return _ERR_LIST_TYPE.format(node.value_type)
        if len(node.value) == 0:
            return _ERR_LIST_IS_EMPTY

    elif node.expected_cardinality == constants.CARDINALITY_TYPE_0_N:
        if node.value_type != list:
            return _ERR_LIST_TYPE.format(node.value_type)


def _validate_constant(node):
    """Constant constraint validator.

    """
    if not node.expected_constant:
        return

    elif node.value != node.expected_constant:
        return "Constant value has been overwritten"


def _validate_regex(node):
    """Regular expression constraint validator.

    """
    if not node.regex:
        return

    print "TODO: validate regex"


def _validate_type(node):
    """Type constraint validator.

    """
    # Escape if unncessary.
    if node.value in (None, []):
        return

    # Validate collections.
    if node.value_type == list:
        if [i for i in node.value if _is_type_mismatch(i, node.expected_type)]:
            return _ERR_LIST_CONTAINS_INVALID_ITEM_TYPES

    # Assert non text.
    elif node.expected_type not in _TEXT_TYPES:
        if _is_type_mismatch(node.value, node.expected_type):
            return _ERR_ITEM_TYPE.format(node.value_type, node.expected_type)

    # Assert text.
    elif node.value_type not in _TEXT_TYPES:
        return _ERR_ITEM_TYPE.format(node.value_type, node.expected_type)

    # Assert text length.
    elif len(node.value.strip()) == 0:
        return _ERR_ITEM_IS_EMPTY_TEXT


# Set of node validators.
_VALIDATORS = (
    _validate_cardinality,
    _validate_type,
    _validate_constant,
    _validate_regex,
)


def _is_type_mismatch(instance, expected_type):
    """Validates that a complex type matches.

    """
    if isinstance(instance, expected_type):
        return False

    if expected_type in ontologies.TYPES and \
       type(instance).__name__.split(".")[-1] == _DOCUMENT_REFERENCE_TYPE:
        return False

    return True


def _validate_node(node):
    """Validates a node within a validation graph.

    """
    # Reset error state.
    node.error = None

    # Escape if parent node is invalid.
    if node.parent and node.parent.is_invalid:
        return

    # Execute validators.
    for validator in _VALIDATORS:
        node.error = validator(node)
        if node.error:
            break


def validate(doc):
    """Validates a document.

    :param doc: A pyesdoc document instance.
    :type doc: object

    :returns: A list of validation errors.
    :rtype: list

    """
    graph = ValidationGraph(doc)
    for node in [n for n in graph.nodes if n.constraints]:
        _validate_node(node)

    return graph.invalid_nodes


def is_valid(doc):
    """Returns validation status of a document.

    :param doc: A pyesdoc document instance.
    :type doc: object

    :returns: The document's validation state.
    :rtype: bool

    """
    return len(validate(doc)) == 0
