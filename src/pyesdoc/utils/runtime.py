"""
.. module:: pyesdoc.utils.runtime.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Runtime utility functions.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""


class PYESDOC_Exception(Exception):
    """Default library exception class.

    """

    def __init__(self, message):
        """Contructor.

        :param message: Exception message.
        :type message: str

        """
        self.message = message


    def __str__(self):
        """Returns a string representation.

        """
        return "ES-DOC PY-CLIENT EXCEPTION : {0}".format(repr(self.message))

