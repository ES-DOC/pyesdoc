# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv.model.entity.py
   :copyright: Copyright "December 01, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: An entity within the pyesdoc.cv domain model.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import pyesdoc
from pyesdoc.cv.constants import ENCODING_DICT
from pyesdoc.cv.constants import ENCODING_JSON



class Entity(object):
    """An entity within the pyesdoc.cv domain model.

    """
    def validate(self):
        """Validates instance.

        :returns: Set of validation errrors.
        :rtype: set

        """
        # N.B. just-in-time import to avaoid circular references.
        from pyesdoc.cv import validation as v

        return v.validate(self)


    @property
    def errors(self):
        """Returns set of validation errors.

        """
        return sorted(list(self.validate()))


    @property
    def is_valid(self):
        """Gets flag indicating validity status.

        """
        return len(self.validate()) == 0


    @property
    def as_dict(self):
        """Returns dictionary representation of term.

        """
        return pyesdoc.cv.encode(self, ENCODING_DICT)


    @property
    def as_json(self):
        """Returns json representation of term.

        """
        return pyesdoc.cv.encode(self, ENCODING_JSON)


    @classmethod
    def from_json(cls, encoded):
        """Returns json representation of term.

        """
        return pyesdoc.cv.decode(encoded, ENCODING_JSON)
