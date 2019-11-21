"""
.. module:: pyesdoc.mp.ontologies.core.enum_member
   :platform: Unix, Windows
   :synopsis: Represents an ontological enumerated type member definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

class EnumMember(object):
    """Represents an enumeration member, i.e. a constrained value associated with an enumeration.

    """
    def __init__(self, name, doc_string):
        """Instance constructor.

        :param str name: Enumeration member name.
        :param str doc_string: Enumeration member documentation string.

        """
        self.enum = None
        self.name = name
        self.doc_string = doc_string


    def __repr__(self):
        """Instance string representation.

        """
        return self.name


    @property
    def key(self):
        """Returns enum member key.

        """
        return self.name.strip().lower().replace(" ", "_")
