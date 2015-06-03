# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_shared_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.shared package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-03 11:24:48.594059.

"""
import abc
import datetime
import uuid




class Calendar(object):
    """A concrete class within the cim v2 type system.

    Describes the calendar required/used in an experiment/simulation. This class is based on the
    calendar attributes and properties found in the CF netCDF conventions.

    """
    def __init__(self):
        """Constructor.

        """
        super(Calendar, self).__init__()

        self.cal_type = None                              # time.CalendarTypes
        self.description = None                           # str
        self.month_lengths = []                           # int
        self.name = None                                  # str


class CimText(object):
    """A concrete class within the cim v2 type system.

    A text class which supports plaintext, html, ...etc.

    """
    def __init__(self):
        """Constructor.

        """
        super(CimText, self).__init__()

        self.content = None                               # str
        self.content_type = None                          # shared.TextCode


class Citation(object):
    """A concrete class within the cim v2 type system.

    A document, book, or academic paper..

    """
    def __init__(self):
        """Constructor.

        """
        super(Citation, self).__init__()

        self.abstract = None                              # str
        self.citation_str = None                          # str
        self.description = None                           # str
        self.doi = None                                   # str
        self.title = None                                 # str
        self.url = None                                   # shared.OnlineResource


class DateTime(object):
    """A concrete class within the cim v2 type system.

    A date or time. Either in simulation time with the simulation
       calendar, or with reference to a simulation start, in which
       case the datetime is an interval after the start date.

    """
    def __init__(self):
        """Constructor.

        """
        super(DateTime, self).__init__()

        self.offset = None                                # bool
        self.value = None                                 # str


class DatetimeSet(object):
    """An abstract class within the cim v2 type system.

    Provides a set of dates which are displaced by a regular interval.

    Note that we assume either a periodic set of dates which can
    be date and/or time, or an irregular set which can only be dates.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(DatetimeSet, self).__init__()

        self.length = None                                # int


class Meta(object):
    """A concrete class within the cim v2 type system.

    Metadata for all documents.

    """
    def __init__(self):
        """Constructor.

        """
        super(Meta, self).__init__()

        self.author = None                                # linked_to(shared.Party)
        self.completeness = None                          # str
        self.create_date = None                           # datetime.datetime
        self.quality = None                               # str
        self.uid = None                                   # uuid.UUID
        self.update_date = None                           # datetime.datetime
        self.version = None                               # int


class NumberArray(object):
    """A concrete class within the cim v2 type system.

    An array of numbers as a space separated list.

    """
    def __init__(self):
        """Constructor.

        """
        super(NumberArray, self).__init__()

        self.values = None                                # str


class OnlineResource(object):
    """A concrete class within the cim v2 type system.

    An approximation of ISO19115 CI_ONLINERESOURCE.

    """
    def __init__(self):
        """Constructor.

        """
        super(OnlineResource, self).__init__()

        self.description = None                           # str
        self.linkage = None                               # str
        self.name = None                                  # str
        self.protocol = None                              # str


class Party(object):
    """A concrete class within the cim v2 type system.

    A person or organisation.

    NOTE: Implements minimal material for an ISO19115-1 (2014) compliant party.
    For our purposes this is a much better animal than the previous responsibleParty
    which munged roles together with people. Note we have collapsed CI_Contact,
    CI_Individual and CI_Organisation as well as the abstract CI_Party.

    """
    def __init__(self):
        """Constructor.

        """
        super(Party, self).__init__()

        self.address = None                               # str
        self.email = None                                 # str
        self.meta = Meta()                                # shared.Meta
        self.name = None                                  # str
        self.organisation = None                          # bool
        self.url = None                                   # shared.OnlineResource


class Responsibility(object):
    """A concrete class within the cim v2 type system.

    Identifies a person or organisation and their role in doing something.

    NOTE: Implements the ISO19115-1 (2014) CI_Responsibility (which replaces responsibleParty).

    """
    def __init__(self):
        """Constructor.

        """
        super(Responsibility, self).__init__()

        self.party = []                                   # linked_to(shared.Party)
        self.role = None                                  # shared.RoleCode
        self.when = None                                  # time.TimePeriod


class TimePeriod(object):
    """A concrete class within the cim v2 type system.

    Provides a time interval description.

    """
    def __init__(self):
        """Constructor.

        """
        super(TimePeriod, self).__init__()

        self.calendar = None                              # time.Calendar
        self.date = None                                  # time.DateTime
        self.date_type = None                             # time.PeriodDateTypes
        self.length = None                                # int
        self.units = None                                 # time.TimeUnits


class TimesliceList(object):
    """A concrete class within the cim v2 type system.

    A list of timeslices either as months in  year, or as days in a month:
        yearlist: 1,4,5 refers to jan,april,may,
        monthlist: 1,5,6 refers to the 1st, 5th and 6th of the month

    """
    def __init__(self):
        """Constructor.

        """
        super(TimesliceList, self).__init__()

        self.members = None                               # shared.NumberArray
        self.units = None                                 # time.SlicetimeUnits


class VocabMember(object):
    """A concrete class within the cim v2 type system.

    A term in an external (to the CIM) controlled vocabulary (CV).

    """
    def __init__(self):
        """Constructor.

        """
        super(VocabMember, self).__init__()

        self.uri = None                                   # str
        self.value = None                                 # str
        self.vocab = None                                 # shared.Citation


class CimLink(OnlineResource):
    """A concrete class within the cim v2 type system.

    Specialisation of online resource for link between documents.

    """
    def __init__(self):
        """Constructor.

        """
        super(CimLink, self).__init__()

        self.remote_type = None                           # str


class IrregularDateSet(DatetimeSet):
    """A concrete class within the cim v2 type system.

    Provides a set of dates as a list of dates.

    """
    def __init__(self):
        """Constructor.

        """
        super(IrregularDateSet, self).__init__()

        self.date_set = None                              # str


class RegularTimeSet(DatetimeSet):
    """A concrete class within the cim v2 type system.

    Provides a set of dates which are displaced by a regular interval.

    """
    def __init__(self):
        """Constructor.

        """
        super(RegularTimeSet, self).__init__()

        self.increment = None                             # time.TimePeriod
        self.length = None                                # int
        self.start_date = None                            # time.DateTime


class CalendarTypes(object):
    """An enumeration within the cim v2 type system.

    CF calendar types as defined in CF 1.6.
    """

    pass


class PeriodDateTypes(object):
    """An enumeration within the cim v2 type system.

    Create and return a period date type enum (used by time_period).
    """

    pass


class RoleCode(object):
    """An enumeration within the cim v2 type system.

    Roles that a party may play in delivering a responsibility.

    Definitions sourced from: https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115_and_19115-2_CodeList_Dictionaries#CI_RoleCode
    """

    pass


class SlicetimeUnits(object):
    """An enumeration within the cim v2 type system.

    Units for integers in a timeslice.
    """

    pass


class TextCode(object):
    """An enumeration within the cim v2 type system.

    Types of text understood by the CIM notebook.
    """

    pass


class TimeUnits(object):
    """An enumeration within the cim v2 type system.

    Appropriate Time units for experiment durations in NWP and Climate Modelling.
    """

    pass


