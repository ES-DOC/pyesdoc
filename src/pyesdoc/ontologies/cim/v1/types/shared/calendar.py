"""
.. module:: cim.v1.types.shared.calendar.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.194158.

"""

# Module imports.
import abc
from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.date_range import DateRange




class Calendar(object):
    """An abstract class within the cim v1 type system.

    Describes a method of calculating a span of dates.
    """
    # Abstract Base Class module.
    # N.B. - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(Calendar, self).__init__()
        self.description = str()                     # type = str
        self.length = int()                          # type = int
        self.range = None                            # type = shared.DateRange


    def as_dict(self):
        """Returns a deep dictionary representation.

        """
        def append(d, key, value, is_iterative, is_primitive, is_enum):
            if value is None:
                if is_iterative:
                    value = []
            elif is_primitive == False and is_enum == False:
                if is_iterative:
                    value = map(lambda i : i.as_dict(), value)
                else:
                    value = value.as_dict()
            d[key] = value

        # Populate a deep dictionary.
        d = dict()
        append(d, 'description', self.description, False, True, False)
        append(d, 'length', self.length, False, True, False)
        append(d, 'range', self.range, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

