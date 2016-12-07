# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.drq.config.wrapper.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Wraps dreq2Defn.xml.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
class Wrapper(object):
    """Wraps dreq2Defn.xml.

    """
    def __init__(self, tables):
        """Instance constructor.

        :param list tables: Collection of configuration tables.

        """
        self.tables = sorted(tables, key=lambda i: i.label.lower())
        for table in tables:
            setattr(self, table.label, table)
            setattr(self, table.label_pythonic, table)


    def __len__(self):
        """Returns number of attributes in managed collection.

        """
        return len(self.tables)


    def __contains__(self, key):
        """Returns flag indicating whether a certain table exists or not.

        """
        if key in self.tables:
            return True
        return self[key] is not None


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(self.tables)


    def __getitem__(self, key):
        """Returns a child table attribute.

        """
        try:
            int(key)
        except ValueError:
            key = str(key).strip().lower()
            for table in self.tables:
                if table.label.lower() == key or table.label_pythonic.lower() == key:
                    return table
        else:
            return self.tables[key]

