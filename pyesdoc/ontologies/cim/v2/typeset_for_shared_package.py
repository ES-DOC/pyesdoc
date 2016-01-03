# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_shared_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.shared package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

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
        """Constructor.

        """
        super(Calendar, self).__init__()

        self.description = None                           # unicode (0.1)
        self.month_lengths = []                           # int (0.N)
        self.name = None                                  # unicode (0.1)
        self.standard_name = None                         # shared.CalendarTypes (1.1)


class Cimtext(object):
    """A concrete class within the cim v2 type system.

    Provides a text class which supports plaintext, html, and
    friends (or will do).

    """
    def __init__(self):
        """Constructor.

        """
        super(Cimtext, self).__init__()

        self.content = None                               # unicode (1.1)
        self.content_type = None                          # shared.TextCode (1.1)


class Citation(object):
    """A concrete class within the cim v2 type system.

    Description of material suitable for citation - in the academic sense, i.e. for a journal bibliography.

    """
    def __init__(self):
        """Constructor.

        """
        super(Citation, self).__init__()

        self.abstract = None                              # unicode (0.1)
        self.citation_str = None                          # unicode (1.1)
        self.context = None                               # unicode (0.1)
        self.doi = None                                   # unicode (0.1)
        self.short_cite = None                            # unicode (0.1)
        self.title = None                                 # unicode (0.1)
        self.url = None                                   # shared.OnlineResource (0.1)


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

        self.offset = None                                # bool (0.1)
        self.value = None                                 # unicode (1.1)


class DatetimeSet(object):
    """An abstract class within the cim v2 type system.

    Base class for a set of dates or times.
    Note that we assume either a periodic set of dates which can
    be date and/or time, or an irregular set which can only be dates.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(DatetimeSet, self).__init__()

        self.length = None                                # int (1.1)


class DocMetaInfo(object):
    """A concrete class within the cim v2 type system.

    Encapsulates document meta information.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocMetaInfo, self).__init__()

        self.author = None                                # shared.Party (0.1)
        self.create_date = None                           # datetime.datetime (1.1)
        self.drs_keys = []                                # unicode (0.N)
        self.drs_path = None                              # unicode (0.1)
        self.external_ids = []                            # unicode (0.N)
        self.id = None                                    # uuid.UUID (1.1)
        self.institute = None                             # unicode (0.1)
        self.language = None                              # unicode (1.1)
        self.project = None                               # unicode (1.1)
        self.reviews = []                                 # shared.DocQualityReview (0.N)
        self.sort_key = None                              # unicode (0.1)
        self.source = None                                # unicode (1.1)
        self.source_key = None                            # unicode (0.1)
        self.type = None                                  # unicode (1.1)
        self.type_display_name = None                     # unicode (0.1)
        self.type_sort_key = None                         # unicode (0.1)
        self.update_date = None                           # datetime.datetime (1.1)
        self.version = None                               # int (1.1)


class DocQualityReview(object):
    """A concrete class within the cim v2 type system.

    A review of a documents quality.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocQualityReview, self).__init__()

        self.completeness = None                          # unicode (1.1)
        self.date = None                                  # unicode (1.1)
        self.quality = None                               # unicode (1.1)
        self.reviewer = None                              # shared.Party (1.1)


class DocReference(object):
    """A concrete class within the cim v2 type system.

    A reference to another cim entity.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocReference, self).__init__()

        self.description = None                           # unicode (0.1)
        self.id = None                                    # uuid.UUID (0.1)
        self.name = None                                  # unicode (0.1)
        self.type = None                                  # unicode (0.1)
        self.url = None                                   # unicode (0.1)
        self.version = None                               # int (0.1)


class KeyFloat(object):
    """A concrete class within the cim v2 type system.

    Holds a key and a float value.

    """
    def __init__(self):
        """Constructor.

        """
        super(KeyFloat, self).__init__()

        self.key = None                                   # unicode (1.1)
        self.value = None                                 # float (1.1)


class NumberArray(object):
    """A concrete class within the cim v2 type system.

    Provides a class for entering an array of numbers.

    """
    def __init__(self):
        """Constructor.

        """
        super(NumberArray, self).__init__()

        self.values = None                                # unicode (1.1)


class OnlineResource(object):
    """A concrete class within the cim v2 type system.

    An approximation of ISO19115 CI_ONLINERESOURCE.

    """
    def __init__(self):
        """Constructor.

        """
        super(OnlineResource, self).__init__()

        self.description = None                           # unicode (0.1)
        self.linkage = None                               # unicode (1.1)
        self.name = None                                  # unicode (1.1)
        self.protocol = None                              # unicode (0.1)


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

        self.address = None                               # unicode (0.1)
        self.email = None                                 # unicode (0.1)
        self.meta = DocMetaInfo()                         # shared.DocMetaInfo (1.1)
        self.name = None                                  # unicode (0.1)
        self.organisation = None                          # bool (0.1)
        self.url = None                                   # shared.OnlineResource (0.1)


class Pid(object):
    """A concrete class within the cim v2 type system.

    A permanent identifier (with a resolution service).

    """
    def __init__(self):
        """Constructor.

        """
        super(Pid, self).__init__()

        self.id = None                                    # unicode (1.1)
        self.resolution_service = None                    # shared.OnlineResource (1.1)


class Responsibility(object):
    """A concrete class within the cim v2 type system.

    Implements the ISO19115-1 (2014) CI_Responsibility (which replaces
    responsibleParty).

    """
    def __init__(self):
        """Constructor.

        """
        super(Responsibility, self).__init__()

        self.party = []                                   # shared.Party (1.N)
        self.role = None                                  # shared.RoleCode (1.1)
        self.when = None                                  # shared.TimePeriod (0.1)


class StandaloneDocument(object):
    """An abstract class within the cim v2 type system.

    Raw base class for documents which are created standalone in a workflow.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(StandaloneDocument, self).__init__()

        self.long_name = None                             # unicode (0.1)
        self.meta = DocMetaInfo()                         # shared.DocMetaInfo (1.1)
        self.name = None                                  # unicode (1.1)
        self.references = []                              # shared.Citation (0.N)
        self.responsible_parties = []                     # shared.Responsibility (0.N)


class TimePeriod(object):
    """A concrete class within the cim v2 type system.

    A time period class aka a temporal extent.

    """
    def __init__(self):
        """Constructor.

        """
        super(TimePeriod, self).__init__()

        self.calendar = None                              # shared.Calendar (0.1)
        self.date = None                                  # shared.DateTime (0.1)
        self.date_type = None                             # shared.PeriodDateTypes (1.1)
        self.length = None                                # int (1.1)
        self.units = None                                 # shared.TimeUnits (1.1)


class TimesliceList(object):
    """A concrete class within the cim v2 type system.

    A list of referential dates, 
        e.g. yearlist, 1,4,5 would refer to jan,april,may,
             monthlist, 1,5,6 would refer to the 1st, 5th and 6th of the month.

    """
    def __init__(self):
        """Constructor.

        """
        super(TimesliceList, self).__init__()

        self.members = None                               # shared.NumberArray (1.1)
        self.units = None                                 # shared.SlicetimeUnits (1.1)


class VocabMember(object):
    """A concrete class within the cim v2 type system.

    A term in an external (to the CIM) controlled vocabulary (CV).

    """
    def __init__(self):
        """Constructor.

        """
        super(VocabMember, self).__init__()

        self.uri = None                                   # unicode (0.1)
        self.value = None                                 # unicode (1.1)
        self.vocab = None                                 # shared.Citation (0.1)


class CimLink(OnlineResource):
    """A concrete class within the cim v2 type system.

    Specialisation of online resource for link between CIM documents.

    """
    def __init__(self):
        """Constructor.

        """
        super(CimLink, self).__init__()

        self.remote_type = None                           # unicode (1.1)


class IrregularDateset(DatetimeSet):
    """A concrete class within the cim v2 type system.

    A set of irregularly spaced times.

    """
    def __init__(self):
        """Constructor.

        """
        super(IrregularDateset, self).__init__()

        self.date_set = None                              # unicode (1.1)


class Reference(Citation):
    """A concrete class within the cim v2 type system.

    A citation which is forced to have a context provided.

    """
    def __init__(self):
        """Constructor.

        """
        super(Reference, self).__init__()



class RegularTimeset(DatetimeSet):
    """A concrete class within the cim v2 type system.

    A regularly spaced set of times.

    """
    def __init__(self):
        """Constructor.

        """
        super(RegularTimeset, self).__init__()

        self.increment = None                             # shared.TimePeriod (1.1)
        self.length = None                                # int (1.1)
        self.start_date = None                            # shared.DateTime (1.1)


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

    A period date type enum (used by time_period).
    """
    is_open = False
    members = [
        "date is end",
        "date is start",
        "unused"
        ]


class RoleCode(object):
    """An enumeration within the cim v2 type system.

    Responsibility role codes.
    """
    is_open = False
    members = [
        "Principal Investigator",
        "author",
        "collaborator",
        "custodian",
        "distributor",
        "originator",
        "owner",
        "point of contact",
        "processor",
        "publisher",
        "resource provider",
        "sponsor",
        "user"
        ]


class SlicetimeUnits(object):
    """An enumeration within the cim v2 type system.

    Units for integers in a timeslice.
    """
    is_open = False
    members = [
        "monthly",
        "yearly"
        ]


class TextCode(object):
    """An enumeration within the cim v2 type system.

    Types of text understood by the CIM notebook. Currently only
    plaintext, but we expect safe HTML to be supported as soon as practicable.
    """
    is_open = False
    members = [
        "plaintext"
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


