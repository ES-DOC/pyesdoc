# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.validation.validator.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Validates a document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.validation.graph import DocumentValidationGraph



# Validation error text.
_ERR_LIST_IS_EMPTY = "is an empty list"
_ERR_LIST_CONTAINS_INVALID_ITEM_TYPES = "list contains item(s) of invalid type"
_ERR_ITEM_IS_NULL = "is null"
_ERR_ITEM_TYPE = "is of invalid type (actual = {0}, expected={1})"
_ERR_ITEM_IS_EMPTY_TEXT = "is zero length"


def _validate_list_node(node):
    """Validates a node that represents a list.

    """
    if node.is_required and len(node.value) == 0:
        node.error = _ERR_LIST_IS_EMPTY
    else:
        for i in node.value:
            if not isinstance(i, node.type):
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

    # Validate type (non text).
    if node.type not in (str, unicode) and not isinstance(node.value, node.type):
        node.error = _ERR_ITEM_TYPE.format(type(node.value), node.type)
        return

    # Validate type.
    if node.type in (str, unicode):
        if not isinstance(node.value, (str, unicode)):
            node.error = _ERR_ITEM_TYPE.format(type(node.value), node.type)
            return
    elif not isinstance(node.value, node.type):
        node.error = _ERR_ITEM_TYPE.format(type(node.value), node.type)
        return

    # Validate length of text types.
    if node.type in (str, unicode) and len(node.value) == 0:
        node.error = _ERR_ITEM_IS_EMPTY_TEXT
        return


def _validate_node(node):
    """Validates a node within a validation graph."""
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
    # Instantiate validation graph.
    graph = DocumentValidationGraph(doc)

    # Validate nodes.
    for node in graph.nodes:
        _validate_node(node)

    # Return invalid nodes.
    return graph.invalid_nodes


def is_valid(doc):
    """Returns validation status of a document.

    :param doc: A pyesdoc document instance.
    :type doc: object

    :returns: The document's validation state.
    :rtype: bool

    """
    return len(validate(doc)) == 0
