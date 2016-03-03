# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.validation.validator.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Validates a document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.validation.graph import ValidationGraph



# Validation error text.
_ERR_LIST_IS_EMPTY = "is an empty list"
_ERR_LIST_CONTAINS_INVALID_ITEM_TYPES = "list contains item(s) of invalid type"
_ERR_ITEM_IS_NULL = "is null"
_ERR_ITEM_TYPE = "is of invalid type (actual = {0}, expected={1})"
_ERR_ITEM_IS_EMPTY_TEXT = "is zero length"

# Type of document references.
_DOCUMENT_REFERENCE_TYPE = "DocReference"


def __validate_cardinality():
    pass


def __validate_type():
    pass


def __validate_regex():
    pass


def __validate_constant():
    pass


def _is_type_mismatch(instance, expected_type):
    """Validates that a complex type matches.

    """
    if isinstance(instance, expected_type):
        return False

    if type(instance).__name__.split(".")[-1] == _DOCUMENT_REFERENCE_TYPE:
        return False

    return True


def _validate_list_node(node):
    """Validates a node that represents a list.

    """
    if node.is_required and len(node.value) == 0:
        node.error = _ERR_LIST_IS_EMPTY
    else:
        for i in node.value:
            if _is_type_mismatch(i, node.type):
                node.error = _ERR_LIST_CONTAINS_INVALID_ITEM_TYPES


def _validate_item_node(node):
    """Validates a node that represents an item.

    """
    # Escape if unncessary.
    if not node.is_required and node.value is None:
        return

    # Assert required.
    if node.is_required and node.value is None:
        node.error = _ERR_ITEM_IS_NULL
        return

    # Assert valid type (non text).
    if node.type not in (str, unicode):
        if _is_type_mismatch(node.value, node.type):
            node.error = _ERR_ITEM_TYPE.format(type(node.value), node.type)
        return

    # Assert valid type (text).
    if not isinstance(node.value, (str, unicode)):
        node.error = _ERR_ITEM_TYPE.format(type(node.value), node.type)
        return

    # Assert valid text length.
    if len(node.value) == 0:
        node.error = _ERR_ITEM_IS_EMPTY_TEXT


def _validate_node(node):
    """Validates a node within a validation graph.

    """
    # Reset error state.
    node.error = None

    # Escape if parent node is invalid.
    if node.parent and node.parent.is_invalid:
        return

    # Validate according to type.
    if isinstance(node.value, list):
        _validate_list_node(node)
    else:
        _validate_item_node(node)


def validate(doc):
    """Validates a document.

    :param doc: A pyesdoc document instance.
    :type doc: object

    :returns: A list of validation errors.
    :rtype: list

    """
    graph = ValidationGraph(doc)
    for node in graph.nodes:
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
