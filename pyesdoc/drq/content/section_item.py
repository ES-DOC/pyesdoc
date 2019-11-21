"""
.. module:: pyesdoc.drq.content.section_item.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Wraps a section item defined within dreq.xml.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.drq import utils
from pyesdoc.drq.definition.table_attribute import TableAttribute



class SectionItem(object):
    """Wraps a section item defined within dreq.xml.

    """
    def __init__(self, table, elem):
        """Instance constructor.

        :param dreq.definition.Table table: Associated definition table.
        :param xml.etree.ElementTree elem: Section item xml info.

        """
        self._TABLE = table
        utils.init_from_xml(
            self,
            elem,
            sorted([i.label for i in table]),
            {i.label: i.type_python for i in table if i.type_python != list}
            )
        self._sort_key = self.label.lower()
        self.links = SectionItemLinks(self)


    def __repr__(self):
        """Instance representation.

        """
        return self.label or self.uid or str(type(self))


    def __len__(self):
        """Returns number of item attributes.

        """
        return len(self._TABLE.attributes)


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter([(i, self[i]) for i in self._TABLE])


    def __getitem__(self, key):
        """Returns a child table attribute.

        """
        attr = None
        if isinstance(key, TableAttribute):
            attr = key
        elif isinstance(key, int):
            attr = self._TABLE[key]
        else:
            key = str(key).strip().lower()
            for attribute in self._TABLE:
                if attribute.label.lower() == key:
                    attr = attribute
                    break
        if attr is not None:
            return getattr(self, attr.label)


class SectionItemLinks(object):
    """Wraps the collection of linked data request sections.

    """
    def __init__(self, item):
        """Instance constructor.

        :param dreq.content.SectionItem item: Associated section item.

        """
        for attr in [i for i in item._TABLE if i.is_internal_link]:
            short_name, long_name = utils.get_link_labels(attr.label)
            if short_name is not None:
                setattr(self, short_name, None)
            if short_name != long_name and long_name is not None:
                setattr(self, long_name, None)
