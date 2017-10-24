# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.utils.runtime.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Runtime utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def assert_doc(doc):
    """Asserts thay passed variable is a pyesdoc object instance.

    :param object doc: A pyesdoc object instance.

    """
    if doc is None or not isinstance(doc, object):
        raise TypeError("Document type is unrecognized")
    if not hasattr(doc, 'meta'):
        raise ValueError('Document has no meta attribute')


def invoke(ctx, actions, error_actions):
    """Invokes a set of actions.

    :param object ctx: Processing context information.
    :param iterable actions: Set of actions to perform.
    :param iterable error_actions: Set of error actions to perform.

    """
    try:
        for action in actions:
            action(ctx)
    except Exception as exc:
        ctx.error = exc
        for action in error_actions:
            action(ctx)


def first(collection, name, value, value_formatter=None):
    """Returns first item in collection filtered by attribute name/value.

    :param iterable collection: A collection of items for filtering.
    :param str name: Name of an attribute acting as filter target.
    :param object value: Value to filter by.
    :param function formatter: Value formatting function.

    :returns: First item in collection filtered by attribute name/value.
    :rtype: object | None

    """
    filtered = all(collection, name, value, value_formatter)

    return filtered[0] if len(filtered) else None


def all(collection, name, value, formatter=None):
    """Returns collection filtered by attribute name/value.

    :param iterable collection: A collection of items for filtering.
    :param str name: Name of an attribute acting as filter target.
    :param object value: Value to filter by.
    :param function formatter: Value formatting function.

    :returns: Collection filtered by attribute name/value.
    :rtype: iterable

    """
    if formatter:
        value = formatter(value)

    def predicate(i):
        if hasattr(i, name):
            v = getattr(i, name)
            if formatter:
                v = formatter(v)

            return v == value
        else:
            return False

    return filter(predicate, collection)
