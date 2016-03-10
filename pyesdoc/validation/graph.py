# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.validation.graph.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: A document validation graph.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc import ontologies
from pyesdoc import constants



class _ValidationNode(object):
    """A node within a validation graph.

    """
    def __init__(self, parent, value, name, idx=None, constraints=[]):
        """Object constructor.

        :param _ValidationNode parent: Parent node within graph.
        :param object value: Current node value.
        :param str path: Node path.
        :param class typeof: Type used during type checking.
        :param _ValidationNode parent: Parent node.

        """
        self.children = []
        self.constraints = constraints
        self.error = None
        self.idx = idx
        self.name = name
        self.value = value
        self.value_type = type(value)
        self.parent = parent
        self.root = self if parent is None else parent.root

        # Set information derived from constraints.
        self.expected_cardinality = \
            self._get_constraint(constants.CONSTRAINT_TYPE_CARDINALITY)
        self.expected_type = \
            self._get_constraint(constants.CONSTRAINT_TYPE_TYPEOF)
        self.expected_constant = \
            self._get_constraint(constants.CONSTRAINT_TYPE_CONSTANT)
        self.regex = \
            self._get_constraint(constants.CONSTRAINT_TYPE_REGEX)

        # Set path used for reporting purposes.
        if parent is None:
            self.path = name
        else:
            self.path = "{}.{}".format(parent.path, name)
        if idx is not None:
            self.path = "{}[{}]".format(self.path, idx)

        # Append node to parent/root.
        if parent is not None:
            self.root.nodes.append(self)
            parent.children.append(self)

        # Set child nodes.
        if self.value is not None and not \
           isinstance(self.value, list) and \
           self.value_type in ontologies.TYPES:
            self._set_children()


    def __repr__(self):
        """Object representation.

        """
        if self.error:
            return "{0} --> {1}".format(self.path, self.error)
        else:
            return self.path


    @property
    def is_invalid(self):
        """Gets a flag indicating whether node is valid.

        """
        return self.error is not None


    def _get_constraint(self, constraint_type):
        """Returns an associated node constraint.

        """
        for typeof, value in self.constraints:
            if typeof == constraint_type:
                return value


    def _set_children(self):
        """Sets collection of child node from type information.

        """
        for name in ontologies.CLASS_PROPERTIES[self.value_type]:
            val = getattr(self.value, name)
            _ValidationNode(self, val, name,
                constraints=ontologies.CONSTRAINTS[(self.value_type, name)]
                )

            # Create child nodes for collections.
            if isinstance(val, list):
                for idx, item in enumerate([i for i in val if i is not None]):
                    _ValidationNode(self, item, name, idx)


class ValidationGraph(_ValidationNode):
    """A document validation graph.

    A set of heirarchical nodes processed by a validator.

    """
    def __init__(self, doc):
        """Object constructor.

        :param object doc: pyesdoc document.

        """
        self.nodes = []
        super(ValidationGraph, self).__init__(None, doc, "doc")


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

