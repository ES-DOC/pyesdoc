"""
.. module:: pyesdoc.drq.definition.table.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Wraps a table defined within dreq2Defn.xml.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.drq import constants
from pyesdoc.drq import utils



# Map of table xml attribute names to value covertors.
_CONVERTORS = {
    'is_label_unique': lambda v: False if v == "No" else True,
    'level': int,
    'max_occurs': int
}



class Table(object):
    """Wraps a table defined within dreq2Defn.xml.

    """
    def __init__(self, elem):
        """Instance constructor.

        :param xml.etree.Element elem: XML element declared within data request definition.

        """
        utils.init_from_xml(self, elem, elem.keys(), _CONVERTORS)
        self.attributes = []
        self.label_drq = self.label
        self.label = utils.get_label(self.label)


    def __repr__(self):
        """Instance representation.

        """
        return self.label


    def __len__(self):
        """Returns number of attributes in managed collection.

        """
        return len(self.attributes)


    def __contains__(self, target):
        """Returns flag indicating whether an attribute of the matching name exists or not.

        """
        return (target in self.attributes) or (self[target] is not None)


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(sorted(self.attributes, key=lambda i: i._sort_key))


    def __getitem__(self, key):
        """Returns a child table attribute.

        """
        if isinstance(key, int):
            return self.attributes[key]
        key = str(key).strip().lower()
        for attribute in self.attributes:
            if attribute.label.lower() == key or \
               attribute.label_drq.lower() == key:
                return attribute
