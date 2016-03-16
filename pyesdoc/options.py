# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.options.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulates library options that can be overridden at runtime.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import pyesdoc



# Set of supported options.
_OPTIONS = {
    'api_url' : "http://test.api.es-doc.org",
    'output_dir': ''
}


def list_options():
    """List library options.

    """
    opts = []
    for name, value in _OPTIONS.items():
        opts.append((name, value))

    return tuple(opts)


def set_option(name, value):
    """Sets an option value.

    :param str name: Option name.
    :param str value: Option value.

    """
    if name not in _OPTIONS:
        raise pyesdoc.InvalidOptionException(name)

    _OPTIONS[name] = str(value)


def get_option(name):
    """Returns an option value.

    :param str name: Option name.

    :returns: A library option.
    :rtype: str

    """
    if name not in _OPTIONS:
        raise ValueError("pyesdoc option {0} is unsupported".format(name))

    return _OPTIONS[name]
