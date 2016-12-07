# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.drq.config.initializer.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulates config package initialization.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import pyesdoc
from pyesdoc.drq.config.wrapper import Wrapper
from pyesdoc.drq.config.table import Table
from pyesdoc.drq.config.table_attribute import TableAttribute
from pyesdoc.drq.config.xml_parser import XMLParser



class Initializer(XMLParser):
    """Initialises library with parsed configuration.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Initializer, self).__init__()
        self.tables = {}
        self.execute()


    def on_parse_table_element(self, elem):
        """On table element parse event handler.

        """
        self.tables[elem] = Table(elem)


    def on_parse_table_attribute_element(self, table_elem, elem):
        """On table attribute element parse event handler.

        """
        table = self.tables[table_elem]
        table.attributes.append(TableAttribute(table, elem))


    def on_parse_complete(self):
        """On parse complete event handler.

        """
        setattr(pyesdoc.drq, "config", Wrapper(self.tables.values()))
