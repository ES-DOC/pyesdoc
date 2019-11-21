"""
.. module:: pyesdoc.mp.ontologies.core.computed_property
   :platform: Unix, Windows
   :synopsis: Represents an ontological computed property definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

class ComputedProperty(object):
    """Represents a computed property within an ontology.

    """
    def __init__(self, name, computation):
        """Instance constructor.

        :param str name: Property name.
        :param str computation: Computed property derivation.

        """
        if name.lower() in ("ext", ):
            raise AttributeError("{0} is a reserved property name.".format(name))

        self.cls = None
        self.name = name
        self.computation = computation
        self.package = None


    def __repr__(self):
        """Instance string representation.

        """
        return self.name
