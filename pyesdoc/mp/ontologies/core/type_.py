"""
.. module:: pyesdoc.mp.ontologies.core.property
   :platform: Unix, Windows
   :synopsis: Represents an ontological type reference definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.mp.ontologies.core.class_ import Class
from pyesdoc.mp.ontologies.core.enum import Enum
from pyesdoc.mp.ontologies.schemas import utils



class Type(object):
    """Represents a type within an ontology.

    :ivar name: Name of type.

    """

    def __init__(self, name):
        """Instance constructor.

        :param str name: Name of type.

        """
        self.is_class = False
        self.is_complex = len(name.split('.')) > 1
        self.is_simple = not self.is_complex

        if name.startswith("linked_to"):
            self.name, qualifier = utils.parse_type(name)
        else:
            self.name, qualifier = name, None
        self.qualifier_type = Type(qualifier) if qualifier else None

        if self.is_simple:
            self.name_of_package = None
            self.name_of_type = self.name
        else:
            self.name_of_package = self.name.split('.')[0]
            self.name_of_type = self.name.split('.')[1]


    def __repr__(self):
        """Instance string representation.

        """
        return self.name


    @property
    def is_enum(self):
        """Gets flag indicating whether type represents an enumerated type.

        """
        return self.is_complex and not self.is_class
