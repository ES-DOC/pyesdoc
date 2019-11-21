"""
.. module:: pyesdoc.mp.utils
   :platform: Unix, Windows
   :synopsis: Runtime utilty functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

class ESDOC_MP_Exception(Exception):
    """Default library exception class.

    """

    def __init__(self, message):
        """Contructor.

        :param str message: Exception message.

        """
        self.message = unicode(message)


    def __str__(self):
        """Returns a string representation.

        """
        return "ES-DOC MP :: !!! EXCEPTION !!! : {0}".format(repr(self.message))


def raise_error(msg, type_=ESDOC_MP_Exception):
    """Helper function to raise a runtime error.

    :param str msg: Error message.
    :param class type_: Error type.

    """
    raise type_(msg)


def log(msg):
    """Outputs a message to log.

    :param str msg: Logging message.

    """
    if msg.startswith('-'):
        print(msg)
    else:
        print("ES-DOC-MP :: {}".format(msg))


def str_to_camel_case(target, separator='_'):
    """Converts passed name to camel case.

    :param target: A string to be converted.
    :type target: str

    :param separator: A separator used to split target string into constituent parts.
    :type separator: str

    :returns: The target string converted to camel case.
    :rtype: str

    """
    r = ''
    if target is not None and len(target):
        # Convert to pascal case.
        s = str_to_pascal_case(target, separator)

        # Preserve initial separator
        if s[0:len(separator)] == separator:
            r += separator
            s = s[len(separator):]

        # Lower case abbreviations.
        if s.lower() in _ABBREVIATIONS:
            r += s.lower()

        # Lower case initial character.
        elif len(s):
            r += s[0].lower()
            r += s[1:]

    return r