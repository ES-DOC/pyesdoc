"""
.. module:: pyesdoc.mp.ontologies.core.enum
   :platform: Unix, Windows
   :synopsis: Represents an ontological enumerated type definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

class Enum(object):
    """Represents an enumeration, i.e. a constrained set of values.

    """
    def __init__(self, name, is_open, doc_string, members):
        """Instance constructor.

        :param str name: Enumeration name.
        :param bool is_open: Flag indicating whether members can be added to the enumeration or not.
        :param str doc_string: Enumeration documentation string.
        :param iterable members: Set of associated enumeration members.

        """
        self.name = name
        self.is_open = is_open
        self.doc_string = doc_string if doc_string is not None else ''
        self.members = members
        self.package = None

        self.op_doc_string_name = None
        self.op_file_name = None
        self.op_full_name = None
        self.op_func_name = None
        self.op_import_name = None
        self.op_name = None


    def __repr__(self):
        """Instance string representation.

        """
        try:
            return "{}.{}".format(self.package, self.name)
        except:
            return self.name

