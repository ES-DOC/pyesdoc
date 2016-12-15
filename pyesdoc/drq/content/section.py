# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.drq.content.section.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Wraps a section defined within dreq.xml.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.drq import utils
from pyesdoc.drq import constants



class Section(object):
    """Wraps a section defined within dreq.xml.

    """
    def __init__(self, cfg, elem):
        """Instance constructor.

        :param dreq.definition.Table cfg: Associated config info.
        :param xml.etree.ElementTree elem: Content section xml element.

        """
        utils.init_from_xml(constants.LABEL_MAP, self, elem, elem.keys())

        self._dfn = cfg
        self._sort_key = cfg.label.lower()
        self.items = []
        self.label = cfg.label
        self.label_pythonic = cfg.label_pythonic


    def __repr__(self):
        """Instance representation.

        """
        return self.label_pythonic


    def __len__(self):
        """Returns number of items in managed collection.

        """
        return len(self.items)


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(sorted(self.items, key=lambda i: i._sort_key))


    def __getitem__(self, key):
        """Returns a child section item.

        """
        if isinstance(key, slice):
            return self.items[key]
        elif isinstance(key, int):
            return self.items[key]
        key = str(key).strip().lower()
        for item in self.items:
            if item.label.lower() == key:
                return item


    def get_item(self, name):
        """Returns a item.

        """
        for item in self.items:
            if item.label == name:
                return item
