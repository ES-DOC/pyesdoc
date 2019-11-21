"""
.. module:: pyesdoc.mp.ontologies.core.package
   :platform: Unix, Windows
   :synopsis: Represents an ontological package definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from operator import add



class Package(object):
    """Represents a package within an ontology.

    :ivar name: Package name.
    :ivar doc_string: Package documentation string.
    :ivar classes: Set of associated classes.
    :ivar enums: Set of associated enums.

    """

    def __init__(self, name, doc_string, classes, enums):
        """Instance constructor.

        :param str name: Package name.
        :param str doc_string: Package documentation string.
        :param iterable classes: Set of associated classes.
        :param iterable enums: Set of associated enums.

        """
        self.abstract_classes = _get_sorted(classes, lambda c: c.is_abstract)
        self.associated = []
        self.associated_for_import = []
        self.concrete_classes = _get_sorted(classes, lambda c: not c.is_abstract)
        self.classes = _get_sorted(classes)
        self.decodings = reduce(add, [c.decodings for c in classes])
        self.doc_string = doc_string
        self.entities = []
        self.enums = _get_sorted(enums)
        self.external_types = []
        self.name = name
        self.op_name = None
        self.properties = reduce(add, [c.properties for c in classes])
        self.sub_classed = tuple()
        self.types = _get_sorted(classes + enums)


    def __repr__(self):
        """Instance string representation.

        """
        return self.name


def _get_sorted(collection, predicate=None, sort_key=None):
    """Returns a sorted collection.

    """
    if predicate:
        collection = [i for i in collection if predicate(i)]
    if sort_key is None:
        sort_key = lambda i: i.name

    return sorted(collection, key=sort_key)
