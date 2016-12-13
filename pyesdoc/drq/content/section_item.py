# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.drq.content.section_item.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Wraps a section item defined within dreq.xml.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.drq import _utils as utils



class SectionItem(object):
    """Wraps a section item defined within dreq.xml.

    """
    def __init__(self, section, elem):
        """Instance constructor.

        :param dreq.content.Section section: Associated section.
        :param xml.etree.ElementTree elem: Section item xml info.

        """
        self.section = section
        self.cfg = section.cfg
        # utils.init_from_xml(self, elem, section.cfg.attribute_names.union(elem.keys()))
        utils.init_from_xml(
          self,
          elem,
          section.cfg.attribute_names,
          section.cfg.attribute_convertors
          )


    def __repr__(self):
        """Instance representation.

        """
        return self.label or self.uid or str(type(self))


    def __len__(self):
        """Returns number of item attributes.

        """
        return len(self.cfg.attributes)


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(self.cfg.attributes)


    def __getitem__(self, key):
        """Returns a child table attribute.

        """
        attr = None
        if isinstance(key, int):
            attr = self.cfg.attributes[key]
        else:
            key = str(key).strip().lower()
            for attribute in self.cfg.attributes:
                if attribute.label.lower() == key:
                    attr = attribute
                    break
        if attr is not None:
            return getattr(self, attr.name)
