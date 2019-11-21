"""
.. module:: pyesdoc.drq.content.wrapper.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Wraps dreq.xml.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
class Wrapper(object):
    """Wraps dreq.xml.

    """
    def __init__(self, sections):
        """Instance constructor.

        :param list sections: Collection of content sections.

        """
        self._sections = sorted(sections, key=lambda i: i._TABLE.label.lower())
        for section in sections:
            setattr(self, str(section), section)


    def __repr__(self):
        """Instance representation.

        """
        return unicode(self._sections)


    def __len__(self):
        """Returns number of sections in managed collection.

        """
        return len(self._sections)


    def __contains__(self, key):
        """Returns flag indicating whether a certain section exists or not.

        """
        if key in self._sections:
            return True
        return self[key] is not None


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(self._sections)


    def __getattr__(self, key):
        """Returns a section.

        """
        return self._get_section(key)


    def __getitem__(self, key):
        """Returns a section.

        """
        return self._get_section(key)


    def _get_section(self, key):
        """Returns a section.

        """
        if isinstance(key, (slice, int)):
            return self._sections[key]
        key = unicode(key).strip().lower()
        for section in self._sections:
            if section._TABLE.label.lower() == key or \
               section._TABLE.label_drq.lower() == key:
                return section
