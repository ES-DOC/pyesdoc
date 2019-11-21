"""
.. module:: pyesdoc.drq.definition.wrapper.py
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

        :param list tables: Collection of definition tables.

        """
        self._tables = sorted(tables, key=lambda i: i.label.lower())
        for table in tables:
            setattr(self, str(table), table)


    def __repr__(self):
        """Instance representation.

        """
        return unicode(self._tables)


    def __len__(self):
        """Returns number of attributes in managed collection.

        """
        return len(self._tables)


    def __contains__(self, key):
        """Returns flag indicating whether a certain table exists or not.

        """
        if key in self._tables:
            return True
        return self[key] is not None


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(self._tables)


    def __getitem__(self, key):
        """Returns a child table attribute.

        """
        try:
            int(key)
        except ValueError:
            key = str(key).strip().lower()
            for table in self._tables:
                if table.label.lower() == key or \
                   table.label_drq.lower() == key:
                    return table
        else:
            return self._tables[key]

