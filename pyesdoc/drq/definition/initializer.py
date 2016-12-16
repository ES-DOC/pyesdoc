# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.drq.definition.initializer.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulates config package initialization.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import pyesdoc
from pyesdoc.drq.definition.wrapper import Wrapper
from pyesdoc.drq.definition.table import Table
from pyesdoc.drq.definition.table_row_attribute import TableRowAttribute
from pyesdoc.drq.definition.xml_parser import XMLParser



class _Parser(XMLParser):
    """Initialises library with parsed configuration.

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


    def on_parse_table_row_attribute_element(self, table_elem, elem):
        """On table row attribute element parse event handler.

        """
        t = self.tables[table_elem]
        tra = TableRowAttribute(t, elem)
        duplicates = [i for i in t if i.key == tra.key]
        if not duplicates:
            t.attributes.append(tra)


    def on_parse_complete(self):
        """On parse complete event handler.

        """
        setattr(pyesdoc.drq, "definition", Wrapper(self.tables.values()))


def execute():
    """Execute initialization process.

    """
    parser = _Parser()
    parser.execute()
