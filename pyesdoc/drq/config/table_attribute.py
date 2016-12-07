# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.drq.config.table_attribute.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Wraps a table attribute defined within dreq2Defn.xml.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.drq import _utils as utils



# Map of table xml attribute names to value covertors.
_CONVERTORS = {
    'required': lambda v: True if v == "True" else False,
}

# Map of table attribute type to python type.
_TYPE_MAP = {
    "xs:string": str,
    "xs:integer": int,
    "xs:float": float,
    "xs:boolean": bool,
    "aa:st__integerList": list,
    "aa:st__integerListMonInc": list,
    "aa:st__stringList": list,
    "aa:st__floatList": list,
    "aa:st__uid": str,
}

# Map of table attribute type to default value.
_DEFAULT_VALUE_MAP = {
    "xs:string": None,
    "xs:integer": None,
    "xs:float": None,
    "xs:boolean": None,
    "aa:st__integerList": list(),
    "aa:st__integerListMonInc": list(),
    "aa:st__stringList": list(),
    "aa:st__floatList": list(),
    "aa:st__uid": None,
}


class TableAttribute(object):
    """Wraps a table attribute defined within dreq2Defn.xml.

    """
    def __init__(self, table, elem):
        """Instance constructor.

        :param dreq.config.table.Table table: Associated configuration table.
        :param xml.etree.Element elem: XML element declared within data request configuration.

        """
        utils.init_from_xml(self, elem, elem.keys(), _CONVERTORS)
        self.default_value = _DEFAULT_VALUE_MAP[self.type]
        self.name = self.label
        self.table = table
        self.type_python = _TYPE_MAP[self.type]


    def __repr__(self):
        """Instance representation.

        """
        return "{}".format(self.label)
