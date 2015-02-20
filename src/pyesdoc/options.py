# -*- coding: utf-8 -*-

"""
.. module:: TODO - write module name
   :copyright: Copyright "Sep 4, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: TODO - write synopsis

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from .utils import runtime as rt



# Set of supported options.
_OPTIONS = {
    'api_url' : "http://test.api.es-doc.org",
    'institute': "UNKNOWN",
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
        rt.throw("pyesdoc option {0} is unsupported".format(name))

    _OPTIONS[name] = str(value)


def get_option(name):
    """Returns an option value.

    :param str name: Option name.

    :returns: A library option.
    :rtype: str

    """
    if name not in _OPTIONS:
        rt.throw("pyesdoc option {0} is unsupported".format(name))

    return _OPTIONS[name]
