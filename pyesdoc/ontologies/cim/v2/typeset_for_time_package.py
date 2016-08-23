# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_time_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.time package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import abc
import datetime
import uuid




class Calendar(object):
    """A concrete class within the cim v2 type system.

    Describes the calendar required/used in an experiment/simulation.
    This class is based on the calendar attributes and properties found in the
    CF netCDF conventions.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Calendar, self).__init__()

        self.description = None                           # unicode (0.1)
        self.month_lengths = []                           # int (0.N)
        self.name = None                                  # unicode (0.1)
        self.standard_name = None                         # time.CalendarTypes (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.standard_name)


class DateTime(object):
    """A concrete class within the cim v2 type system.

    A date or time. Either in simulation time with the simulation
    calendar, or with reference to a simulation start, in which
    case the datetime is an interval after the start date.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DateTime, self).__init__()

        self.offset = None                                # bool (0.1)
        self.value = None                                 # unicode (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}(offset {})".format(self.value, self.offset)


class DatetimeSet(object):
    """An abstract class within the cim v2 type system.

    A set of times. This is an abstract class which is specialised into
    a periodic or aperiodic (irregular) list.  Note that we assume either a
    periodic set of dates which can be date and/or time, or an irregular set
    which can only be dates.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Instance constructor.

        """
        super(DatetimeSet, self).__init__()

        self.length = None                                # int (1.1)


class TimePeriod(object):
    """A concrete class within the cim v2 type system.

    A time period/interval (aka temporal extent).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(TimePeriod, self).__init__()

        self.calendar = None                              # time.Calendar (0.1)
        self.date = None                                  # time.DateTime (0.1)
        self.date_type = None                             # time.PeriodDateTypes (1.1)
        self.length = None                                # unicode (1.1)
        self.units = None                                 # time.TimeUnits (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{} {}".format(self.length, self.units)


class IrregularDateset(DatetimeSet):
    """A concrete class within the cim v2 type system.

    A set of irregularly spaced times, provided as a comma separated string of yyyy-mm-dd in
     the appropriate calendar.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(IrregularDateset, self).__init__()

        self.date_set = None                              # unicode (1.1)


class RegularTimeset(DatetimeSet):
    """A concrete class within the cim v2 type system.

    A regularly spaced set of times.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(RegularTimeset, self).__init__()

        self.increment = None                             # time.TimePeriod (1.1)
        self.length = None                                # int (1.1)
        self.start_date = None                            # time.DateTime (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{} times from {} at {} intervals".format(self.length, self.start_date, self.increment)


class CalendarTypes(object):
    """An enumeration within the cim v2 type system.

    CF calendar types as defined in CF 1.6.
    """
    is_open = False
    members = [
        "360_day",
        "365_day",
        "366_day",
        "all_leap",
        "gregorian",
        "julian",
        "noleap",
        "none",
        "proleptic_gregorian",
        "standard"
        ]


class PeriodDateTypes(object):
    """An enumeration within the cim v2 type system.

    A period date type vocabulary (used by time_period).
    """
    is_open = False
    members = [
        "date is end",
        "date is start",
        "unused"
        ]


class TimeUnits(object):
    """An enumeration within the cim v2 type system.

    Appropriate Time units for experiment durations in NWP and Climate Modelling.
    """
    is_open = False
    members = [
        "days",
        "months",
        "seconds",
        "years"
        ]


