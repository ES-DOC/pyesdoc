"""
.. module:: pyesdoc.drq.content.section.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Wraps a section defined within dreq.xml.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
class Section(object):
    """Wraps a section defined within dreq.xml.

    """
    def __init__(self, table):
        """Instance constructor.

        :param dreq.definition.Table table: Associated definition info.

        """
        self._TABLE = table
        self._items = []


    def __repr__(self):
        """Instance representation.

        """
        return repr(self._TABLE)


    def __len__(self):
        """Returns number of items in managed collection.

        """
        return len(self._items)


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(sorted(self._items, key=lambda i: i._sort_key))


    def __getattr__(self, key):
        """Returns a child section item.

        """
        return self._get_item(key)


    def __getitem__(self, key):
        """Returns a child section item.

        """
        return self._get_item(key)


    def _get_item(self, key):
        """Returns a wrapped keyed value.

        """
        if isinstance(key, (slice, int)):
            return self._items[key]
        key = unicode(key).strip().lower()
        for item in self._items:
            if item.label.lower() == key:
                return item
