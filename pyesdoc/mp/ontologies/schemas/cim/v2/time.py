"""
.. module:: time.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def calendar():
    """Describes the calendar required/used in an experiment/simulation.
    This class is based on the calendar attributes and properties found in the
    CF netCDF conventions.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('{}', ('standard_name',)),
        'properties': [
            ('description', 'str', '0.1',
                "Extra information about the calendar."),
            ('month_lengths', 'int', '0.N',
                "Used for special calendars to provide month lengths."),
            ('name', 'str', '0.1',
                "Can be used to name a special calendar type."),
            ('standard_name', 'time.calendar_types', '1.1',
                "Type of calendar used.")
        ]
    }


def calendar_types():
    """CF calendar types as defined in CF 1.6.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("gregorian", "Mixed Gregorian/Julian calendar as defined by Udunits"),
            ("standard", "Synonym for gregorian: Mixed Gregorian/Julian calendar as defined by Udunits"),
            ("proleptic_gregorian", "A Gregorian calendar extended to dates before 1582-10-15. That is, a year is a leap year if either (i) it is divisible by 4 but not by 100 or (ii) it is divisible by 400."),
            ("noleap", "Gregorian calendar without leap years, i.e., all years are 365 days long."),
            ("365_day", "Synonym for noleap:Gregorian calendar without leap years, i.e., all years are 365 days long."),
            ("all_leap", "Gregorian calendar with every year being a leap year, i.e., all years are 366 days long."),
            ("366_day", "Synonym for all_leap:Gregorian calendar with every year being a leap year, i.e., all years are 366 days long."),
            ("360_day", "All years are 360 days divided into 30 day months."),
            ("julian", "Julian Calendar"),
            ("none", "Perpetual time axis")
        ]
    }


def date_time():
    """A date or time. Either in simulation time with the simulation
    calendar, or with reference to a simulation start, in which
    case the datetime is an interval after the start date.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('{}(offset {})', ('value', 'offset')),
        'properties': [
            ('is_offset', 'bool', '0.1',
                "Date is offset from start of an integration."),
            ('value', 'str', '1.1',
                "Date or time - some of (from left to right): yyyy-mm-dd:hh:mm:ss.")
        ]
    }


def datetime_set():
    """A set of times. This is an abstract class which is specialised into
    a periodic or aperiodic (irregular) list.  Note that we assume either a
    periodic set of dates which can be date and/or time, or an irregular set
    which can only be dates.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': True,
        'alternatives': [
            'time.irregular_dateset',
            'time.regular_timeset'
        ],
        'properties': [
            ('length', 'int', '1.1',
                "Number of times in set.")
        ]
    }


def irregular_dateset():
    """A set of irregularly spaced times, provided as a comma separated string of yyyy-mm-dd in
     the appropriate calendar.

    """
    return {
        'type': 'class',
        'base': 'time.datetime_set',
        'is_abstract': False,
        'properties': [
            ('date_set', 'str', '1.1',
                "Set of dates, comma separated yyyy-mm-dd.")
        ]
    }


def period_date_types():
    """A period date type vocabulary (used by time_period).

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("unused", "Date is not used"),
            ("date is start", "The date defines the start of the period"),
            ("date is end", "The date is the end of the period")
        ]
    }


def regular_timeset():
    """A regularly spaced set of times.

    """
    return {
        'type': 'class',
        'base': 'time.datetime_set',
        'is_abstract': False,
        'pstr': ('{} times from {} at {} intervals', ('length', 'start_date', 'increment')),
        'properties': [
            ('increment', 'time.time_period', '1.1',
                "Interval between members of set."),
            ('length', 'int', '1.1',
                "Number of times in set."),
            ('start_date', 'time.date_time', '1.1',
                "Beginning of time set.")
        ]
    }


def time_period():
    """A time period/interval (aka temporal extent).

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('{} {}', ('length', 'units')),
        'properties': [
            ('calendar', 'time.calendar', '0.1',
                "Calendar, default is standard aka gregorian."),
            ('date', 'time.date_time', '0.1',
                "Optional start/end date of time period."),
            ('date_type', 'time.period_date_types', '1.1',
                "Describes how the date is used to define the period."),
            ('length', 'str', '1.1',
                "Duration of the time period."),
            ('units', 'time.time_units', '1.1',
                "Appropriate time units.")
        ]
    }


def time_units():
    """Appropriate Time units for experiment durations in NWP and Climate Modelling.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("years", "Years in current calendar"),
            ("months", "Months in the current calendar"),
            ("days", "86400 seconds"),
            ("seconds", "Standard metric seconds")
        ]
    }
