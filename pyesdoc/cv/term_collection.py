# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv.term_collection.py
   :copyright: Copyright "December 01, 2014", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: A vocabulary term collection.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import uuid

import pyesdoc
from pyesdoc.cv import constants



class TermCollection(object):
    """A vocabulary term collection.

    """
    def __init__(self):
        """Instance constructor.

        """
        self.create_date = None
        self.description = None
        self.terms = list()
        self.label = None
        self.idx = None
        self.name = None
        self.scope = None
        self.uid = None


    def __repr__(self):
        """Instance representation.

        """
        return self.namespace


    def __len__(self):
        """Returns number of terms in managed collection.

        """
        return len(self.terms)


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(self.terms)


    def __getitem__(self, key):
        """Returns a child section item.

        """
        if isinstance(key, int):
            return self.terms[key]
        key = unicode(key).strip().lower()
        try:
            uuid.UUID(key)
        except ValueError:
            get_key = lambda i: i.name
        else:
            get_key = lambda i: i.uid
        for item in self.terms:
            if key == get_key(item).lower():
                return item


    @property
    def authority(self):
        """Gets associated governing authority.

        """
        return self.scope.authority


    @property
    def namespace(self):
        """Returns full namespace of the term set.

        """
        return ":".join([self.authority.name, self.scope.name, self.name])


    @property
    def partition(self):
        """Returns associated partition.

        """
        return pyesdoc.cv.get_partition(self.namespace)


    def as_dict(self):
        """Returns dictionary representation of term.

        """
        return pyesdoc.cv.encode(self, constants.ENCODING_DICT)


    def as_json(self):
        """Returns json representation of term.

        """
        return pyesdoc.cv.encode(self, constants.ENCODING_JSON)
