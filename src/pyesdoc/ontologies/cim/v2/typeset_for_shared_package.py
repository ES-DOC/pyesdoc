# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_shared_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.shared package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-07-24 23:58:29.562877.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class OnlineResource(object):
    """A concrete class within the cim v2 type system.

    An approximation of ISO19115 CI_ONLINERESOURCE

    """
    def __init__(self):
        """Constructor.

        """
        super(OnlineResource, self).__init__()

        self.protocol = None                              # str
        self.name = None                                  # str
        self.description = None                           # str
        self.linkage = None                               # str


class KeyFloat(object):
    """A concrete class within the cim v2 type system.

    Holds a key and a float value

    """
    def __init__(self):
        """Constructor.

        """
        super(KeyFloat, self).__init__()

        self.key = None                                   # str
        self.value = None                                 # float


class StandaloneDocument(object):
    """An abstract class within the cim v2 type system.

    Raw base class for documents which are created standalone in a workflow

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(StandaloneDocument, self).__init__()

        self.responsible_parties = []                     # shared.Responsibility
        self.references = []                              # shared.Citation
        self.name = None                                  # str
        self.long_name = None                             # str
        self.meta = Meta()                                # shared.Meta


class Cimtext(object):
    """A concrete class within the cim v2 type system.

    Provides a text class which supports plaintext, html, and
    friends (or will do).

    """
    def __init__(self):
        """Constructor.

        """
        super(Cimtext, self).__init__()

        self.content = None                               # str
        self.content_type = None                          # shared.TextCode


class Citation(object):
    """A concrete class within the cim v2 type system.

    Create and return an instance of the citation class

    """
    def __init__(self):
        """Constructor.

        """
        super(Citation, self).__init__()

        self.context = None                               # shared.Cimtext
        self.citation_str = None                          # shared.Cimtext
        self.title = None                                 # str
        self.url = None                                   # shared.OnlineResource
        self.abstract = None                              # str
        self.doi = None                                   # str


class TimesliceList(object):
    """A concrete class within the cim v2 type system.

    A list of referential dates, 
        e.g. yearlist, 1,4,5 would refer to jan,april,may,
             monthlist, 1,5,6 would refer to the 1st, 5th and 6th of the month

    """
    def __init__(self):
        """Constructor.

        """
        super(TimesliceList, self).__init__()

        self.members = None                               # shared.NumberArray
        self.units = None                                 # shared.SlicetimeUnits


class Responsibility(object):
    """A concrete class within the cim v2 type system.

    Implements the ISO19115-1 (2014) CI_Responsibility (which replaces
    responsibleParty).

    """
    def __init__(self):
        """Constructor.

        """
        super(Responsibility, self).__init__()

        self.when = None                                  # shared.TimePeriod
        self.party = []                                   # shared.Party
        self.role = None                                  # shared.RoleCode


class Party(object):
    """A concrete class within the cim v2 type system.

    Implements minimal material for an ISO19115-1 (2014) compliant party. 
    For our purposes this is a much better animal than the previous responsibleParty 
    which munged roles together with people. Note we have collapsed CI_Contact,
    CI_Individual and CI_Organisation as well as the abstract CI_Party.

    """
    def __init__(self):
        """Constructor.

        """
        super(Party, self).__init__()

        self.address = None                               # str
        self.name = None                                  # str
        self.email = None                                 # str
        self.url = None                                   # shared.OnlineResource
        self.meta = MinimalMeta()                         # shared.MinimalMeta
        self.organisation = None                          # bool


class Calendar(object):
    """A concrete class within the cim v2 type system.

    Creates and returns instance of calendar class. This class is based on the
    calendar attributes and properties found in the CF netCDF conventions.

    """
    def __init__(self):
        """Constructor.

        """
        super(Calendar, self).__init__()

        self.cal_type = None                              # shared.CalendarTypes
        self.name = None                                  # str
        self.month_lengths = []                           # int
        self.description = None                           # str


class TimePeriod(object):
    """A concrete class within the cim v2 type system.

    Creates a time period class aka a temporal extent

    """
    def __init__(self):
        """Constructor.

        """
        super(TimePeriod, self).__init__()

        self.length = None                                # int
        self.date_type = None                             # shared.PeriodDateTypes
        self.units = None                                 # shared.TimeUnits
        self.calendar = None                              # shared.Calendar
        self.date = None                                  # shared.DateTime


class DatetimeSet(object):
    """An abstract class within the cim v2 type system.

    Base class for a set of dates or times.
    Note that we assume either a periodic set of dates which can
    be date and/or time, or an irregular set which can only be dates

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(DatetimeSet, self).__init__()

        self.length = None                                # int


class VocabMember(object):
    """A concrete class within the cim v2 type system.

    A term in an external (to the CIM) controlled vocabulary (CV)

    """
    def __init__(self):
        """Constructor.

        """
        super(VocabMember, self).__init__()

        self.vocab = None                                 # shared.Citation
        self.uri = None                                   # str
        self.value = None                                 # str


class Pid(object):
    """A concrete class within the cim v2 type system.

    A permanent identifier (with a resolution service).

    """
    def __init__(self):
        """Constructor.

        """
        super(Pid, self).__init__()

        self.id = None                                    # str
        self.resolution_service = None                    # shared.OnlineResource


class MinimalMeta(object):
    """A concrete class within the cim v2 type system.

    Provides a base class for minimal metadata, used for document classes which
    are basically lists of external entities such as people, as opposed to documents
    which are the main business of the CIM. The presence of an attribute of this
    class (or any subclases) on another class indicates that the latter class carries
    the <<document>> stereotype.

    """
    def __init__(self):
        """Constructor.

        """
        super(MinimalMeta, self).__init__()

        self.document_version = None                      # int
        self.uid = None                                   # str
        self.metadata_last_updated = None                 # datetime.datetime


class NumberArray(object):
    """A concrete class within the cim v2 type system.

    Provides a class for entering an array of numbers

    """
    def __init__(self):
        """Constructor.

        """
        super(NumberArray, self).__init__()

        self.values = None                                # str


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


class Reference(Citation):
    """A concrete class within the cim v2 type system.

    A citation which is forced to have a context provided

    """
    def __init__(self):
        """Constructor.

        """
        super(Reference, self).__init__()



class CimLink(OnlineResource):
    """A concrete class within the cim v2 type system.

    Specialisation of online resource for link between CIM documents

    """
    def __init__(self):
        """Constructor.

        """
        super(CimLink, self).__init__()

        self.remote_type = None                           # str


class Meta(MinimalMeta):
    """A concrete class within the cim v2 type system.

    Metadata for all documents, describing who created it, and last updated etc.

    """
    def __init__(self):
        """Constructor.

        """
        super(Meta, self).__init__()

        self.metadata_author = None                       # shared.Party
        self.metadata_quality = None                      # str
        self.metadata_reviewer = None                     # shared.Party
        self.metadata_completeness = None                 # str


class RegularTimeset(DatetimeSet):
    """A concrete class within the cim v2 type system.

    Creates a regularly spaced set of times

    """
    def __init__(self):
        """Constructor.

        """
        super(RegularTimeset, self).__init__()

        self.increment = None                             # shared.TimePeriod
        self.length = None                                # int
        self.start_date = None                            # shared.DateTime


class IrregularDateset(DatetimeSet):
    """A concrete class within the cim v2 type system.

    Creates a set of irregularly spaced times

    """
    def __init__(self):
        """Constructor.

        """
        super(IrregularDateset, self).__init__()

        self.date_set = None                              # str


class TextCode(object):
    """An enumeration within the cim v2 type system.

    Types of text understood by the CIM notebook. Currently only
    plaintext, but we expect safe HTML to be supported as soon as practicable.
    """

    pass


class PeriodDateTypes(object):
    """An enumeration within the cim v2 type system.

    Create and return a period date type enum (used by time_period)
    """

    pass


class CalendarTypes(object):
    """An enumeration within the cim v2 type system.

    Create and return a calendar type enum
    """

    pass


class TimeUnits(object):
    """An enumeration within the cim v2 type system.

    Create and return a time unit enum
    """

    pass


class SlicetimeUnits(object):
    """An enumeration within the cim v2 type system.

    Create and return a time unit enum for just years and months
    """

    pass


class RoleCode(object):
    """An enumeration within the cim v2 type system.

    Responsibility role codes
    """

    pass


