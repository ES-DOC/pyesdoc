# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.drq.content.xml_parser.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulates parsing over the data request content XML file.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import pyesdoc
from pyesdoc.drq import constants
from pyesdoc.drq import utils



class XMLParser(object):
    """Event driven data request content XML file parser.

    """
    def execute(self):
        """Execute the parse.

        """
        self.on_parse_begin()

        # Load xml to be parsed.
        xml = utils.load_xml(constants.CONTENT_FPATH)

        # Iterate config tables & parse content sections.
        for table in pyesdoc.drq.definition.tables:
            section_elem = xml.find('./main/{}'.format(table.label))
            self.on_parse_section(table, section_elem)
            for item_elem in section_elem.findall('./item'):
                self.on_parse_section_item(section_elem, item_elem)

        self.on_parse_complete()


    def on_parse_begin(self):
        """On parse begin event handler.

        """
        # Sub-class will handle.
        pass


    def on_parse_section(self, cfg, elem):
        """On section element parse event handler.

        """
        # Sub-class will handle.
        pass


    def on_parse_section_item(self, section_elem, elem):
        """On table section item element parse event handler.

        """
        # Sub-class will handle.
        pass


    def on_parse_complete(self):
        """On parse complete event handler.

        """
        # Sub-class will handle.
        pass
