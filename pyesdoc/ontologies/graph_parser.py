# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.ontologies.utils_graph.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Graph utilities.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.ontologies.type_info import CLASSES
from pyesdoc.ontologies.type_info import CLASS_PROPERTIES



class GraphParser(object):
    """Encapsulates object graph parsing.

    """
    def parse(self, container, path=''):
        """Performs a parse over a container raising events as it does so.

        """
        # Get properties.
        try:
            properties = CLASS_PROPERTIES[type(container)]
        except KeyError:
            raise ValueError("Container is an unsupported ontology class.")

        # Raise container parse event.
        self.on_container_parse(container, path)

        # Parse container properties.
        for p_name in properties:
            # Raise property parse event.
            p_value = getattr(container, p_name)
            p_path = "{}.{}".format(path, p_name)
            self.on_property_parse(container, p_path, p_name, p_value)

            # Parse list values.
            if isinstance(p_value, list):
                for idx, item in enumerate(p_value):
                    item_path = "{}.{}".format(p_path, idx)
                    self.on_list_item_parse(p_value, item_path, idx, item)
                    if isinstance(item, CLASSES):
                        self.parse(item, item_path)

            # Parse sub-containers.
            elif isinstance(p_value, CLASSES):
                self.parse(p_value, p_path)

        # Raise container parsed event.
        self.on_container_parsed(container)


    def on_container_parse(self, container, path):
        """Container parse event handler.

        """
        # Allow sub-classes to handle.
        pass


    def on_container_parsed(self, container):
        """Container parsed event handler.

        """
        # Allow sub-classes to handle.
        pass


    def on_property_parse(self, container, path, name, value):
        """Property parse event handler.

        """
        # Allow sub-classes to handle.
        pass


    def on_list_item_parse(self, container, path, idx, value):
        """List item parse event handler.

        """
        # Allow sub-classes to handle.
        pass
