# -*- coding: utf-8 -*-

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
        self.sections = sections
        for section in sections:
            setattr(self, section.label_pythonic or section.label, section)


    def __repr__(self):
        """Instance representation.

        """
        return unicode(self.sections)


    def __len__(self):
        """Returns number of sections in managed collection.

        """
        return len(self.sections)


    def __contains__(self, key):
        """Returns flag indicating whether a certain section exists or not.

        """
        if key in self.sections:
            return True
        return self[key] is not None


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(sorted(self.sections, key=lambda i: i._sort_key))


    def __getitem__(self, key):
        """Returns a child section.

        """
        if isinstance(key, int):
            return self.sections[key]
        key = str(key).strip().lower()
        for section in self.sections:
            if section.label.lower() == key or \
               section.label_pythonic.lower() == key:
                return section
