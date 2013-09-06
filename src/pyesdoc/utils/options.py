"""
.. module:: TODO - write module name
   :copyright: Copyright "Sep 4, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: TODO - write synopsis

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Set of supported options.
_OPTIONS = {
    'api_url' : "http://127.0.0.1:5000"
}



def set_option(name, value):
    """Sets a library option.

    :param name: Option name.
    :type name: str

    :param value: Option value.
    :type value: str

    """
    if name not in _OPTIONS:
        pass

    _OPTIONS[name] = str(value)


def get_option(name):
    """Returns a library option.

    :param name: Option name.
    :type name: str

    :returns: A library option.
    :rtype: str

    """
    if name not in _OPTIONS:
        pass

    return _OPTIONS[name]