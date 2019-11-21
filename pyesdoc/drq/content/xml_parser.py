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

        # Load content xml file.
        fpath = utils.get_fpath(constants.CONTENT_FNAME, "content")
        xml = utils.load_xml(fpath)

        # Parse.
        for table in pyesdoc.drq.definition:
            elem = xml.find('./main/{}'.format(table.label_drq))
            self.on_parse_section(table, elem)
            for sub_elem in elem.findall('./item'):
                self.on_parse_section_item(elem, sub_elem)

        self.on_parse_complete()


    def on_parse_begin(self):
        """On parse begin event handler.

        """
        # Sub-class will handle.
        pass


    def on_parse_section(self, table, elem):
        """On section element parse event handler.

        """
        # Sub-class will handle.
        pass


    def on_parse_section_item(self, section_elem, elem):
        """On section item element parse event handler.

        """
        # Sub-class will handle.
        pass


    def on_parse_complete(self):
        """On parse complete event handler.

        """
        # Sub-class will handle.
        pass
