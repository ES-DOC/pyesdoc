# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv.term.py
   :copyright: Copyright "December 01, 2014", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: A vocabulary term.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import uuid

import arrow

import pyesdoc.cv
from pyesdoc.cv import constants



class Termset(object):
    """A vocabulary termset.

    """
    def __init__(self, domain, kind):
        """Instance constructor.

        """
        self.create_date = arrow.utcnow().datetime
        self.domain = domain
        self.kind = kind
        self.description = None
        self.uid = unicode(uuid.uuid4())
        self.items = []


    def __repr__(self):
        """Instance representation.

        """
        return self.namespace


    def __len__(self):
        """Returns number of items in managed collection.

        """
        return len(self.items)


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(self.items)


    def __getitem__(self, key):
        """Returns a child section item.

        """
        try:
            int(key)
        except ValueError:
            key = str(key).strip().lower()
            for item in self.items:
                if item.name.lower() == key:
                    return item
        else:
            return self.items[key]


    @property
    def namespace(self):
        """Returns full namespace of the term set.

        """
        return ":".join([self.domain, self.kind])


    @property
    def partition(self):
        """Returns associated partition.

        """
        return pyesdoc.cv.get_partition(self.domain)


    def as_dict(self):
        """Returns dictionary representation of term.

        """
        return pyesdoc.cv.encode(self, constants.ENCODING_DICT)


    def as_json(self):
        """Returns json representation of term.

        """
        return pyesdoc.cv.encode(self, constants.ENCODING_JSON)
