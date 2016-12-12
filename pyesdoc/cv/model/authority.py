# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv.model.authority.py
   :copyright: Copyright "December 01, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: A vocabulary authority, e.g. WGCM.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.cv.model.entity import Entity



class Authority(Entity):
    """An authority assuming responsibity for governance of vocabularies.

    """
    def __init__(self):
        """Instance constructor.

        """
        self.description = None
        self.label = None
        self.name = None
        self.scopes = list()
        self.url = None


    def __repr__(self):
        """Instance representation.

        """
        return self.namespace


    @property
    def namespace(self):
        """Returns namespace used in I/O scenarios.

        """
        return self.name
