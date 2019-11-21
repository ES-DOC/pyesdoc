"""
.. module:: pyesdoc.mp.ontologies.core.property
   :platform: Unix, Windows
   :synopsis: Represents an ontological type property definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.mp.ontologies.core.type_ import Type



class Property(object):
    """Represents a property within an ontology.

    """
    def __init__(self, name, type_name, cardinality, doc_string):
        """Instance constructor.

        :param str name: Property name.
        :param str doc_string: Property documentation string.
        :param str type_name: Property type name.
        :param str cardinality: Type of relationship to associated class (i.e. 0.1 | 1.1 | 0.N | 1.N).

        """
        if name.lower() in ("ext", ):
            raise AttributeError("{0} is a reserved property name.".format(name))

        self.cls = None
        self.decodings = []
        self.doc_string = doc_string if doc_string is not None else u""
        self.cardinality = cardinality
        self.is_collection = cardinality.split('.')[1] == 'N'
        self.is_linked_document = (name == 'meta')
        self.is_required = cardinality.split('.')[0] != '0'
        self.max_occurs = cardinality.split('.')[1]
        self.min_occurs = cardinality.split('.')[0]
        self.name = name
        self.type = Type(type_name)


    def __repr__(self):
        """Instance string representation.

        """
        return self.name

