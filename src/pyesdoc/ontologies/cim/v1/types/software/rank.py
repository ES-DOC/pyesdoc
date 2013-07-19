"""
.. module:: cim.v1.types.software.rank.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.221267.

"""

# Module imports.
import datetime
import types
import uuid



class Rank(object):
    """A concrete class within the cim v1 type system.

    
    """

    def __init__(self):
        """Constructor"""
        super(Rank, self).__init__()
        self.increment = int()                       # type = int
        self.max = int()                             # type = int
        self.min = int()                             # type = int
        self.value = int()                           # type = int


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
        append(d, 'increment', self.increment, False, True, False)
        append(d, 'max', self.max, False, True, False)
        append(d, 'min', self.min, False, True, False)
        append(d, 'value', self.value, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

