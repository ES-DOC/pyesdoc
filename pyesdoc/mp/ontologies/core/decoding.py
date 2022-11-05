"""
.. module:: pyesdoc.mp.ontologies.core.decoding
   :platform: Unix, Windows
   :synopsis: Represents an ontological decoding definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

class Decoding(object):
    """Represents information used for decoding from a non-standard representation, e.g. Metafor CIM XML.

    """

    def __init__(self, property_name, decoding, type):
        """Instance constructor.

        :param property_name: Name of property with which decoding is associated.
        :param decoding: Decoding information (e.g. an xpath expression).
        :param|None type: Target type to be decoded (either a class or enum).

        """
        self.property_name = property_name
        self.decoding = decoding
        self.type = type
