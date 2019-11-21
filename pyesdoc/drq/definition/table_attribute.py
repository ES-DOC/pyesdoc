"""
.. module:: pyesdoc.drq.definition.table_attribute.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Wraps a table row attribute defined within dreq2Defn.xml.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.drq import utils



# Map of table xml attribute names to value covertors.
_CONVERTORS = {
    'required': lambda v: True if v == "True" else False,
}

# Map of table row attribute type to python type.
_TYPE_MAP = {
    "xs:string": str,
    "xs:integer": int,
    "xs:float": float,
    "xs:boolean": bool,
    "aa:st__configurationType": str,
    "aa:st__integerList": list,
    "aa:st__integerListMonInc": list,
    "aa:st__stringList": list,
    "aa:st__floatList": list,
    "aa:st__fortranType": str,
    "aa:st__sliceType": list,
    "aa:st__uid": str,
}

# Map of table attribute type to default value.
_DEFAULT_VALUE_MAP = {
    "aa:st__integerList": list(),
    "aa:st__integerListMonInc": list(),
    "aa:st__stringList": list(),
    "aa:st__floatList": list()
}


class TableAttribute(object):
    """Wraps a table attribute defined within dreq2Defn.xml.

    """
    def __init__(self, table, elem):
        """Instance constructor.

        :param dreq.definition.table.Table table: Associated definition table.
        :param xml.etree.Element elem: XML element declared within data request definition.

        """
        # Initialize from XML.
        utils.init_from_xml(self, elem, elem.keys(), _CONVERTORS)

        # Switch to pythonic labels.
        self.label_drq = self.label
        self.label = utils.get_label(self.label)
        self._sort_key = self.label.lower()

        # Map drq types.
        self.default_value = _DEFAULT_VALUE_MAP.get(self.type)
        self.type_python = _TYPE_MAP[self.type]

        # Format use_class field.
        try:
            self.use_class
        except AttributeError:
            self.use_class = None
        else:
            if self.use_class == "":
                self.use_class == None


    def __repr__(self):
        """Instance representation.

        """
        return self.label


    @property
    def is_internal_link(self):
        """Gets flag indicating whether the attribute is an internal link or not.

        """
        return self.use_class == "internalLink"
