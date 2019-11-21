"""
.. module:: pyesdoc.drq.content.initializer.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulates content initialization.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import pyesdoc
from pyesdoc.drq import utils
from pyesdoc.drq.content import cache
from pyesdoc.drq.content.section import Section
from pyesdoc.drq.content.section_item import SectionItem
from pyesdoc.drq.content.wrapper import Wrapper
from pyesdoc.drq.content.xml_parser import XMLParser



class _Parser(XMLParser):
    """Initialises library with parsed content.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(_Parser, self).__init__()
        self.parsed = {}


    def on_parse_section(self, table, elem):
        """On table element parse event handler.

        """
        section = Section(table)
        self.parsed[elem] = section
        self.parsed[section] = table
        cache.DATA[section.uid] = section


    def on_parse_section_item(self, section_elem, item_elem):
        """On table section item element parse event handler.

        """
        section = self.parsed[section_elem]
        table = self.parsed[section]
        item = SectionItem(table, item_elem)
        setattr(section, item.label, item)
        section._items.append(item)
        cache.DATA[item.uid] = item


    def on_parse_complete(self):
        """On parse complete event handler.

        """
        # Instantiate wrapper.
        wrapper = Wrapper([i for i in self.parsed.values() if isinstance(i, Section)])

        # Set internal links.
        _set_internal_links(wrapper)

        # Mutate drq.content from package to wrapper.
        setattr(pyesdoc.drq, "content", wrapper)


def _set_internal_links(wrapper):
    for section in wrapper:
        for item in section:
            for attr, value in item:
                if attr.is_internal_link and value in cache.DATA:
                    short_name, long_name = utils.get_link_labels(attr.label)
                    if short_name is not None:
                        setattr(item.links, short_name, cache.DATA[value])
                    if short_name != long_name and long_name is not None:
                        setattr(item.links, long_name, cache.DATA[value])

    # Set relation: mip --> objective
    for mip in wrapper.mip:
        mip.objectives = [o for o in wrapper['objective'] if o.mip == mip.label]


def execute():
    """Execute initialization process.

    """
    parser = _Parser()
    parser.execute()