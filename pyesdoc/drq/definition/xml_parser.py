# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.drq.definition.xml_parser.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulates parsing over the data request configuration XML file.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.drq import constants
from pyesdoc.drq import utils



class XMLParser(object):
    """Event driven data request configuration XML file parser.

    """
    def execute(self):
        """Execute the parse.

        """
        self.on_parse_begin()
        xml = utils.load_xml(constants.DEFINITION_FPATH)
        for t_elem in xml.findall('./table'):
            self.on_parse_table_element(t_elem)
            for tra_elem in t_elem.findall('./rowAttribute'):
                self.on_parse_table_row_attribute_element(t_elem, tra_elem)
        self.on_parse_complete()


    def on_parse_begin(self):
        """On parse begin event handler.

        """
        # Sub-class will handle.
        pass


    def on_parse_table_element(self, elem):
        """On table element parse event handler.

        """
        # Sub-class will handle.
        pass


    def on_parse_table_row_attribute_element(self, table_elem, elem):
        """On table attribute row element parse event handler.

        """
        # Sub-class will handle.
        pass


    def on_parse_complete(self):
        """On parse complete event handler.

        """
        # Sub-class will handle.
        pass

