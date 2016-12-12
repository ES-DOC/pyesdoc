# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv.model.scope.py
   :copyright: Copyright "December 01, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: A vocabulary scope, e.g. CMIP6.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import uuid

from pyesdoc.cv.model.entity import Entity



class Scope(Entity):
    """A scope managed by an authority.

    """
    def __init__(self):
        """Instance constructor.

        """
        self.authority = None
        self.collections = list()
        self.description = None
        self.idx = None
        self.label = None
        self.name = None
        self.uid = None
        self.url = None


    def __repr__(self):
        """Instance representation.

        """
        return self.namespace


    @property
    def namespace(self):
        """Returns full namespace of the term set.

        """
        return u":".join([self.authority.name, self.name])


    @property
    def full_idx(self):
        """Gets full computed idx.

        """
        return unicode(self.idx)

