"""
.. module:: pyesdoc.drq.definition.initializer.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulates definition package initialization.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import pyesdoc
from pyesdoc.drq.definition.wrapper import Wrapper
from pyesdoc.drq.definition.table import Table
from pyesdoc.drq.definition.table_attribute import TableAttribute
from pyesdoc.drq.definition.xml_parser import XMLParser



class _Parser(XMLParser):
    """Initialises library with parsed definition.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(_Parser, self).__init__()
        self.tables = {}


    def on_parse_table_element(self, elem):
        """On table element parse event handler.

        """
        self.tables[elem] = Table(elem)


    def on_parse_table_attribute_element(self, table_elem, elem):
        """On table row attribute element parse event handler.

        """
        table = self.tables[table_elem]
        attribute = TableAttribute(table, elem)
        duplicates = [i for i in table if i.label == attribute.label]
        if not duplicates:
            table.attributes.append(attribute)


    def on_parse_complete(self):
        """On parse complete event handler.

        """
        # Instantiate wrapper.
        wrapper = Wrapper(self.tables.values())

        # Mutate drq.definition from package to wrapper.
        setattr(pyesdoc.drq, "definition", wrapper)


def execute():
    """Execute initialization process.

    """
    parser = _Parser()
    parser.execute()
