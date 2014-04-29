"""
.. module:: pyesdoc.validation.graph.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: A document validation graph.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from .. import ontologies



class _DocumentValidationNode(object):
    """A node within a validation graph.

    """
    def __init__(self,
                 value,
                 path,
                 typeof=None,
                 is_required=False,
                 parent=None,
                 root=None):
        """Constructor.

        :param object value: Current node value.
        :param str path: Node path.
        :param class typeof: Type used during type checking.
        :param bool is_required: Indicates whether a value is required.
        :param _DocumentValidationNode parent: Parent node.

        """
        self.children = []
        self.error = None
        self.is_required = is_required
        self.parent = parent
        self.path = path
        self.root = self if root is None else root
        self.type = type(value) if typeof is None else typeof
        self.value = value
        if parent is not None:
            parent.children.append(self)
        if root is not None:
            root.nodes.append(self)

        # Set children if necessary.
        if self._has_children:
            self._set_children()


    def __repr__(self):
        """Returns string representation."""
        if self.error:
            return "{0} --> {1}".format(self.path, self.error)
        else:
            return self.path


    @property
    def is_valid(self):
        """Gets a flag indicating whether node is valid."""
        return self.error is None


    @property
    def is_invalid(self):
        """Gets a flag indicating whether node is valid."""
        return not self.is_valid


    @property
    def _has_children(self):
        return \
            self.type in ontologies.TYPES and \
            not isinstance(self.value, list) and \
            self.value is not None and \
            type(self.value) == self.type


    def _set_children(self):
        """Sets collection of child node from type information."""
        for type_info in ontologies.get_type_info(self.type):
            # Unpack type info.
            is_required = type_info[2]
            name = type_info[0]
            typeof = type_info[1]

            # Set derived variables.
            path = self.path + "." + name
            value = getattr(self.value, name)

            # Create child node.
            _DocumentValidationNode(
                value,
                path,
                typeof,
                is_required,
                self,
                self.root
                )

            # Create child nodes for list items.
            if isinstance(value, list):
                for idx, item in enumerate([i for i in value if i is not None]):
                    _DocumentValidationNode(
                        item,
                        "{0}[{1}]".format(path, idx),
                        type(item),
                        False,
                        self,
                        self.root
                        )


class DocumentValidationGraph(_DocumentValidationNode):
    """A document validation graph.

    A set of heirarchical nodes processed by a validator.

    """
    def __init__(self, doc):
        """Constructor.

        :param object doc: pyesdoc document.

        """
        self.nodes = []
        super(DocumentValidationGraph, self).__init__(doc, "doc")


    def __repr__(self):
        """Returns string representation."""
        return reduce(lambda r, n: r + "\n{0}".format(n), self.nodes, self.path)


    @property
    def invalid_nodes(self):
        """Get set of invalid nodes."""
        return [n for n in self.nodes if n.is_invalid]
