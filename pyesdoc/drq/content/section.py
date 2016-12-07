# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.drq.content.section.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Wraps a section defined within dreq.xml.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.drq import _utils as utils



class Section(object):
    """Wraps a section defined within dreq.xml.

    """
    def __init__(self, cfg, elem):
        """Instance constructor.

        :param dreq.config.Table cfg: Associated config info.
        :param xml.etree.ElementTree elem: Content section xml element.

        """
        utils.init_from_xml(self, elem, elem.keys())

        self._iter_idx = None
        self.cfg = cfg
        self.elem = elem
        self.items = []
        self.label = cfg.label
        self.label_pythonic = cfg.label_pythonic


    def __repr__(self):
        """Instance representation.

        """
        return self.label


    def __len__(self):
        """Returns number of items in managed collection.

        """
        return len(self.items)


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(self.items)


    def __getitem__(self, key):
        """Returns a child section item.

        """
        try:
            int(key)
        except ValueError:
            key = str(key).strip().lower()
            for item in self.items:
                if item.label.lower() == key:
                    return item
        else:
            return self.items[key]


    def get_item(self, name):
        """Returns a item.

        """
        for item in self.items:
            if item.label == name:
                return item
