"""
.. module:: cim.v1.types.software.parallelisation.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-21 14:34:23.300159.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.software.rank import Rank


class Parallelisation(object):
    """A concrete class within the cim v1 type system.

    Describes how a deployment has been parallelised across a computing platform.
    """

    def __init__(self):
        """Constructor"""
        super(Parallelisation, self).__init__()
        self.processes = int()                       # type = int
        self.ranks = []                              # type = software.Rank


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
        append(d, 'processes', self.processes, False, True, False)
        append(d, 'ranks', self.ranks, True, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

