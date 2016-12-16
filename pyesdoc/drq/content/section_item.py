# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.drq.content.section_item.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Wraps a section item defined within dreq.xml.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.drq import constants
from pyesdoc.drq import utils
from pyesdoc.drq.definition.table_row_attribute import TableRowAttribute




class SectionItem(object):
    """Wraps a section item defined within dreq.xml.

    """
    def __init__(self, section, elem):
        """Instance constructor.

        :param dreq.content.Section section: Associated section.
        :param xml.etree.ElementTree elem: Section item xml info.

        """
        self._section = section
        self._dfn = section._dfn
        utils.init_from_xml(
            constants.LABEL_MAP, 
            self,
            elem,
            section._dfn.attribute_names,
            section._dfn.attribute_convertors
            )
        self._sort_key = self.label.lower()


    def __repr__(self):
        """Instance representation.

        """
        return self.label or self.uid or str(type(self))


    def __len__(self):
        """Returns number of item attributes.

        """
        return len(self._dfn.attributes)


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter([(i, self[i]) for i in self._dfn])


    def __getitem__(self, key):
        """Returns a child table attribute.

        """
        attr = None
        if isinstance(key, TableRowAttribute):
            attr = key
        elif isinstance(key, int):
            attr = self._dfn[key]
        else:
            key = str(key).strip().lower()
            for attribute in self._dfn:
                if attribute.label.lower() == key:
                    attr = attribute
                    break
        if attr is not None:
            return getattr(self, attr.key)
