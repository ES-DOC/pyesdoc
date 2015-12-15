# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.validation.graph.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: A document validation graph.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc import ontologies



class _DocumentSerializationNode(object):
    """A node within a serialization graph.

    """
    def __init__(self,
                 value,
                 path,
                 typeof=None,
                 parent=None,
                 root=None,
                 iterable_index=None):
        """Object constructor.

        :param object value: Current node value.
        :param str path: Node path.
        :param class typeof: Type used during type checking.
        :param _DocumentSerializationNode parent: Parent node.
        :param _DocumentSerializationNode root: Root node.

        """
        self.children = []
        self.error = None
        self.iterable_index = iterable_index
        self.parent = parent
        self.path = path
        self.name = path.split(".")[-1]
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
            return "{0} --> {1}".format(self.path, self.value)


    @property
    def _has_children(self):
        """Gets a flag indicating whether node has children or not.

        """
        return \
            self.type in ontologies.TYPES and \
            not isinstance(self.value, list) and \
            self.value is not None and \
            type(self.value) == self.type


    def _set_children(self):
        """Sets collection of child node from type information.

        """
        for type_info in ontologies.get_type_info(self.type):
            # Unpack type info.
            name = type_info[0]
            typeof = type_info[1]

            # Set derived variables.
            path = self.path + "." + name
            value = getattr(self.value, name)

            # Exclude nulls.
            try:
                iter(value)
            except TypeError:
                if value is None:
                    continue
            else:
                if len(value) == 0:
                    continue

            # Create child nodes.
            if isinstance(value, list):
                for idx, item in enumerate([i for i in value if i is not None]):
                    _DocumentSerializationNode(
                        item,
                        "{0}[{1}]".format(path, idx),
                        type(item),
                        self,
                        self.root,
                        idx
                        )
            else:
                _DocumentSerializationNode(
                    value,
                    path,
                    typeof,
                    self,
                    self.root
                    )


class DocumentSerializationGraph(_DocumentSerializationNode):
    """A document serialization graph.

    A set of heirarchical nodes processed by a serializor.

    """
    def __init__(self, doc):
        """Object constructor.

        :param object doc: pyesdoc document.

        """
        self.nodes = []
        super(DocumentSerializationGraph, self).__init__(doc, "doc")


    def __repr__(self):
        """Object representation.

        """
        return reduce(lambda r, n: r + "\n{0}".format(n), self.nodes, self.path)
