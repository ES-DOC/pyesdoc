"""
.. module:: pyesdoc.drq.definition.xml_parser.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulates parsing over the data request definition XML file.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.drq import constants
from pyesdoc.drq import utils



class XMLParser(object):
    """Event driven data request definition XML file parser.

    """
    def execute(self):
        """Execute the parse.

        """
        self.on_parse_begin()

        # Load definition xml file.
        fpath = utils.get_fpath(constants.DEFINITION_FNAME, "definition")
        xml = utils.load_xml(fpath)

        # Parse.
        for elem in xml.findall('./table'):
            self.on_parse_table_element(elem)
            for sub_elem in elem.findall('./rowAttribute'):
                self.on_parse_table_attribute_element(elem, sub_elem)

        self.on_parse_complete()


    def on_parse_begin(self):
        """On parse begin event handler.

        """
        pass


    def on_parse_table_element(self, elem):
        """On table element parse event handler.

        """
        pass


    def on_parse_table_attribute_element(self, table_elem, elem):
        """On table attribute row element parse event handler.

        """
        pass


    def on_parse_complete(self):
        """On parse complete event handler.

        """
        pass
