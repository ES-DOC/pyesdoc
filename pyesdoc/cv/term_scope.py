# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv.term_scope.py
   :copyright: Copyright "December 01, 2014", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: A vocabulary scope, e.g. CMIP6.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
class TermScope(object):
    """A scope managed by an authority.

    """
    def __init__(self):
        """Instance constructor.

        """
        self.authority = None
        self.collections = list()
        self.description = None
        self.homepage = None
        self.idx = None
        self.label = None
        self.name = None
        self.uid = None


    def __repr__(self):
        """Instance representation.

        """
        return self.namespace


    @property
    def namespace(self):
        """Returns full namespace of the term set.

        """
        return ":".join([self.authority.name, self.name])
