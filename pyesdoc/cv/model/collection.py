# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv.model.collection.py
   :copyright: Copyright "December 01, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: A vocabulary collection, e.g. institute-id.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import uuid

import pyesdoc
from pyesdoc.cv import constants
from pyesdoc.cv.model.entity import Entity



class Collection(Entity):
    """A vocabulary term collection.

    """
    def __init__(self):
        """Instance constructor.

        """
        self.create_date = None
        self.description = None
        self.idx = None
        self.label = None
        self.name = None
        self.scope = None
        self.terms = list()
        self.uid = None
        self.url = None


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
        """Gets namespace.

        """
        return ":".join([
            self.scope.namespace,
            self.name,
            ])


    @property
    def full_idx(self):
        """Gets full computed idx.

        """
        return u"{}.{}".format(
            self.scope.idx,
            self.idx
            )


    @property
    def partition(self):
        """Returns associated partition.

        """
        return pyesdoc.cv.get_partition(self.namespace)
