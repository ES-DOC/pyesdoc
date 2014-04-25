# -*- coding: utf-8 -*-

"""
.. module:: functional.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of functional programming utilities for working with collections.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def invoke(collection, func):
    """Invokes a function over each member of a collection.

    :param iterable collection: A collection of items.
    :param function func: A function to be applied to each collection member.

    :returns: Tuple of function results.
    :rtype: tuple

    """
    return (func(i) for i in collection)


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
