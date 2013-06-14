"""
.. module:: cim.v1.types.software.timing.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:08.104327.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.software.timing_units import TimingUnits


class Timing(object):
    """A concrete class within the cim v1 type system.

    Provides information about the rate of couplings and connections and/or the timing characteristics of individual components - for example, the start and stop times that the component was run for or the units of time that a component is able to model (in a single timestep).
    """

    def __init__(self):
        """Constructor"""
        super(Timing, self).__init__()
        self.end = datetime.datetime.now()           # type = datetime.datetime
        self.is_variable_rate = bool()               # type = bool
        self.rate = int()                            # type = int
        self.start = datetime.datetime.now()         # type = datetime.datetime
        self.units = ''                              # type = software.TimingUnits


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
        append(d, 'end', self.end, False, True, False)
        append(d, 'is_variable_rate', self.is_variable_rate, False, True, False)
        append(d, 'rate', self.rate, False, True, False)
        append(d, 'start', self.start, False, True, False)
        append(d, 'units', self.units, False, False, True)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

