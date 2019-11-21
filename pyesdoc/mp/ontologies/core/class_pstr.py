"""
.. module:: pyesdoc.mp.ontologies.core.class_pstr.py
   :platform: Unix, Windows
   :synopsis: Represents an ontological class print string.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

class ClassPrintString(object):
    """Represents a class's print string.

    """
    def __init__(self, text, fields):
        """Instance constructor.

        :param str text: Pstr text (unformatted).
        :param str fields: Fields to be pushed into text at point of formatting.

        """
        self.text = text
        self.fields = fields

