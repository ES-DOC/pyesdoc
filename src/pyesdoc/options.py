"""
.. module:: TODO - write module name
   :copyright: Copyright "Sep 4, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: TODO - write synopsis

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from .utils import runtime as rt



# Set of supported options.
_OPTIONS = {
    'api_url' : "http://127.0.0.1:5000"
}


def list():
    """List library options.

    """
    opts = []
    for k, v in _OPTIONS.items():
        opts.append((k, v))

    return tuple(opts)


def set(name, value):
    """Sets a library option.

    :param name: Option name.
    :type name: str

    :param value: Option value.
    :type value: str

    """
    if name not in _OPTIONS:
        rt.throw("pyesdoc option {0} is unsupported".format(name))

    _OPTIONS[name] = str(value)


def get(name):
    """Returns a library option.

    :param name: Option name.
    :type name: str

    :returns: A library option.
    :rtype: str

    """
    if name not in _OPTIONS:
        rt.throw("pyesdoc option {0} is unsupported".format(name))

    return _OPTIONS[name]