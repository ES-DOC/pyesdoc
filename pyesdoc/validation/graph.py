# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.validation.graph.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: A document validation graph.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc import ontologies



class _ValidationNode(object):
    """A node within a validation graph.

    """
    def __init__(self,
                 value,
                 path,
                 typeof=None,
                 is_required=False,
                 parent=None,
                 root=None):
        """Object constructor.

        :param object value: Current node value.
        :param str path: Node path.
        :param class typeof: Type used during type checking.
        :param bool is_required: Indicates whether a value is required.
        :param _ValidationNode parent: Parent node.

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
        """Object representation.

        """
        if self.error:
            return "{0} --> {1}".format(self.path, self.error)
        else:
            return self.path


    @property
    def is_valid(self):
        """Gets a flag indicating whether node is valid.

        """
        return self.error is None


    @property
    def is_invalid(self):
        """Gets a flag indicating whether node is valid.

        """
        return not self.is_valid


    @property
    def _has_children(self):
        """Gets a flag indicating whether node has children or not.

        """
        if self.type in ontologies.TYPES and \
           not isinstance(self.value, list) and \
           self.value is not None and \
           type(self.value) == self.type:
           return True


    def _set_children(self):
        """Sets collection of child node from type information.

        """
        for name, constraints in ontologies.get_validation_info(self.type):
            val = getattr(self.value, name)
            path = self.path + "." + name
            # Create child node.
            _ValidationNode(
                val,
                path,
                self,
                self.root,
                constraints
                )

            # Continue if not processing a collection.
            if not isinstance(val, list):
                continue

            # Create child nodes for collections.
            for idx, item in enumerate([i for i in val if i is not None]):
                _ValidationNode(
                    item,
                    "{0}[{1}]".format(path, idx),
                    type(item),
                    False,
                    self,
                    self.root
                    )

                _ValidationNode(
                    item,
                    "{0}[{1}]".format(path, idx),
                    self,
                    self.root,
                    constraints
                    )

    def __init__(self,
                 value,
                 path,
                 typeof=None,
                 is_required=False,
                 parent=None,
                 root=None):


        for type_info in ontologies.get_type_info(self.type):
            # Unpack type info.
            is_required = type_info[2]
            name = type_info[0]
            typeof = type_info[1]

            # Set derived variables.
            path = self.path + "." + name
            value = getattr(self.value, name)

            # Create child node.
            _ValidationNode(
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
                    _ValidationNode(
                        item,
                        "{0}[{1}]".format(path, idx),
                        type(item),
                        False,
                        self,
                        self.root
                        )


class ValidationGraph(_ValidationNode):
    """A document validation graph.

    A set of heirarchical nodes processed by a validator.

    """
    def __init__(self, doc):
        """Object constructor.

        :param object doc: pyesdoc document.

        """
        self.nodes = []
        super(ValidationGraph, self).__init__(doc, "doc")


    def __repr__(self):
        """Object representation.

        """
        return reduce(lambda r, n: r + "\n{0}".format(n), self.nodes, self.path)


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(self.nodes)


    @property
    def invalid_nodes(self):
        """Get set of invalid nodes.

        """
        return [n for n in self.nodes if n.is_invalid]

