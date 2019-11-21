"""
.. module:: pyesdoc.mp.ontologies.core.computed_property
   :platform: Unix, Windows
   :synopsis: Represents an ontological computed property definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

class ClassConstraint(object):
    """Represents a class constraint defined within an ontology.

    """
    def __init__(self, property_name, typeof, value):
        """Instance constructor.

        :param str property_name: Property name.
        :param str typeof: Constraint type.
        :param str value: Constrained value.

        """
        if property_name.lower() in ("ext", ):
            raise AttributeError("{0} is a reserved property name.".format(property_name))

        self.cls = None
        self.property_name = property_name
        self.typeof = typeof
        self.value = value
        self.package = None


    def __repr__(self):
        """Instance string representation.

        """
        return "class constraint; {}::{}::{}".format(self.property_name, self.typeof, self.value)


    @property
    def key(self):
        """Returns a key for disambiguating amongst a set of constraints.

        """
        return "{}-{}".format(self.property_name, self.typeof)
