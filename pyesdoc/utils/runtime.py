# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.utils.runtime.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Runtime utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Set of logging levels.
LOG_LEVEL_DEBUG = 'DUBUG'
LOG_LEVEL_INFO = 'INFO'
LOG_LEVEL_WARNING = 'WARNING'
LOG_LEVEL_ERROR = 'ERROR'


def assert_doc(doc):
    """Asserts thay passed variable is a pyesdoc object instance.

    :param object doc: A pyesdoc object instance.

    """
    if doc is None or not isinstance(doc, object):
        raise TypeError("Document type is unrecognized")
    if not hasattr(doc, 'meta'):
        raise ValueError('Document has no meta attribute')


def log(msg=None, level=LOG_LEVEL_INFO):
    """Outputs a message to log.

    :param str msg: Message for writing to log.
    :param str level: Logging level.

    """
    # Format.
    if msg:
        msg = "ES-DOC :: pyesdoc :: {0} > {1}".format(level, str(msg).strip())
    else:
        msg = '-----------------------------------------'
        msg += msg

    # TODO output to logs.
    print msg


def log_error(err):
    """Logs a runtime error.

    :param Exception err: Exception to be logged.

    """
    if isinstance(err, basestring):
        msg = "!!! RUNTIME ERROR !!! :: {}.".format(err)
    else:
        msg = "!!! RUNTIME ERROR !!! :: {} :: {}.".format(err.__class__, err)
    log(msg, level=LOG_LEVEL_ERROR)


def log_warning(msg):
    """Logs a runtime warning.

    :param str msg: Message for writing to log.

    """
    log(msg, level=LOG_LEVEL_WARNING)


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
