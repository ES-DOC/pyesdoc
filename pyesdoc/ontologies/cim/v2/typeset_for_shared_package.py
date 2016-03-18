# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_shared_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.shared package.

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
        self.standard_name = None                         # shared.CalendarTypes (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.standard_name)


class Cimtext(object):
    """A concrete class within the cim v2 type system.

    Provides a text class which supports plaintext, html, and
    friends (or will do).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Cimtext, self).__init__()

        self.content = None                               # unicode (1.1)
        self.content_type = None                          # shared.TextCode (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.content)


class CitationTarget(object):
    """A concrete class within the cim v2 type system.

    A real world document, could be a book, a journal article, a manual, a web page ... it might or might
    not be online, although preferably it would be.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(CitationTarget, self).__init__()

        self.citation_detail = None                       # unicode (0.1)
        self.doi = None                                   # unicode (0.1)
        self.meta = DocMetaInfo()                         # shared.DocMetaInfo (1.1)
        self.name = None                                  # unicode (1.1)
        self.online_at = None                             # shared.OnlineResource (0.1)
        self.title = None                                 # unicode (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.name)


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

    Base class for a set of dates or times.
    Note that we assume either a periodic set of dates which can
    be date and/or time, or an irregular set which can only be dates.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Instance constructor.

        """
        super(DatetimeSet, self).__init__()

        self.length = None                                # int (1.1)


class DocMetaInfo(object):
    """A concrete class within the cim v2 type system.

    Encapsulates document meta information used by es-doc machinery. Will not normally be
    populated by humans. May duplicate information held in 'visible' metadata.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DocMetaInfo, self).__init__()

        self.author = None                                # shared.Party (0.1)
        self.create_date = None                           # datetime.datetime (1.1)
        self.drs_keys = []                                # unicode (0.N)
        self.drs_path = None                              # unicode (0.1)
        self.external_ids = []                            # unicode (0.N)
        self.id = None                                    # unicode (1.1)
        self.institute = None                             # unicode (0.1)
        self.language = None                              # unicode (1.1)
        self.project = None                               # unicode (1.1)
        self.sort_key = None                              # unicode (0.1)
        self.source = None                                # unicode (1.1)
        self.source_key = None                            # unicode (0.1)
        self.type = None                                  # unicode (1.1)
        self.type_display_name = None                     # unicode (0.1)
        self.type_sort_key = None                         # unicode (0.1)
        self.update_date = None                           # datetime.datetime (1.1)
        self.version = None                               # int (1.1)


class KeyFloat(object):
    """A concrete class within the cim v2 type system.

    Holds a key and a float value.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(KeyFloat, self).__init__()

        self.key = None                                   # unicode (1.1)
        self.value = None                                 # float (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}: {}".format(self.key, self.value)


class NumberArray(object):
    """A concrete class within the cim v2 type system.

    Provides a class for entering an array of numbers.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(NumberArray, self).__init__()

        self.values = None                                # unicode (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.values)


class OnlineResource(object):
    """A concrete class within the cim v2 type system.

    A minimal approximation of ISO19115 CI_ONLINERESOURCE, provides a link and details
    of how to use that link.

    """
    def __init__(self):
        """Instance constructor.

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
        """Instance constructor.

        """
        super(Party, self).__init__()

        self.address = None                               # unicode (0.1)
        self.email = None                                 # unicode (0.1)
        self.meta = DocMetaInfo()                         # shared.DocMetaInfo (1.1)
        self.name = None                                  # unicode (0.1)
        self.orcid_id = None                              # unicode (0.1)
        self.organisation = None                          # bool (0.1)
        self.url = None                                   # shared.OnlineResource (0.1)


class Pid(object):
    """A concrete class within the cim v2 type system.

    A permanent identifier (with a resolution service).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Pid, self).__init__()

        self.id = None                                    # unicode (1.1)
        self.resolution_service = None                    # shared.OnlineResource (1.1)


class QualityReview(object):
    """A concrete class within the cim v2 type system.

    Assertations as to the completeness and quality of a document.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(QualityReview, self).__init__()

        self.date = None                                  # unicode (1.1)
        self.meta = DocMetaInfo()                         # shared.DocMetaInfo (1.1)
        self.metadata_reviewer = None                     # shared.Party (1.1)
        self.quality_description = None                   # unicode (1.1)
        self.quality_status = None                        # shared.QualityStatus (0.1)
        self.target_document = None                       # shared.DocReference (1.1)


class Reference(object):
    """A concrete class within the cim v2 type system.

    An external citation target which can have a context associated with it.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Reference, self).__init__()

        self.context = None                               # unicode (0.1)
        self.document = None                              # shared.CitationTarget (1.1)


class Responsibility(object):
    """A concrete class within the cim v2 type system.

    Implements the ISO19115-1 (2014) CI_Responsibility (which replaces
    responsibleParty). Combines a person and their role in doing something.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Responsibility, self).__init__()

        self.party = []                                   # shared.Party (1.N)
        self.role = None                                  # shared.RoleCode (1.1)
        self.when = None                                  # shared.TimePeriod (0.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}:{}".format(self.role, self.party)


class TimePeriod(object):
    """A concrete class within the cim v2 type system.

    A time period class aka a temporal extent.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(TimePeriod, self).__init__()

        self.calendar = None                              # shared.Calendar (0.1)
        self.date = None                                  # shared.DateTime (0.1)
        self.date_type = None                             # shared.PeriodDateTypes (1.1)
        self.length = None                                # int (1.1)
        self.units = None                                 # shared.TimeUnits (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{} {}".format(self.length, self.units)


class TimesliceList(object):
    """A concrete class within the cim v2 type system.

    A list of referential dates, 
        e.g. yearlist, 1,4,5 would refer to jan,april,may,
             monthlist, 1,5,6 would refer to the 1st, 5th and 6th of the month.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(TimesliceList, self).__init__()

        self.members = None                               # shared.NumberArray (1.1)
        self.units = None                                 # shared.SlicetimeUnits (1.1)


class DocReference(OnlineResource):
    """A concrete class within the cim v2 type system.

    Specialisation of online resource for link between CIM documents, whether the
    remote document exists when complete, or not.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DocReference, self).__init__()

        self.constraint_vocabulary = None                 # unicode (0.1)
        self.context = None                               # unicode (0.1)
        self.id = None                                    # unicode (0.1)
        self.relationship = None                          # unicode (0.1)
        self.type = None                                  # unicode (1.1)
        self.version = None                               # int (0.1)


class IrregularDateset(DatetimeSet):
    """A concrete class within the cim v2 type system.

    A set of irregularly spaced times.

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

        self.increment = None                             # shared.TimePeriod (1.1)
        self.length = None                                # int (1.1)
        self.start_date = None                            # shared.DateTime (1.1)


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


class DocumentTypes(object):
    """An enumeration within the cim v2 type system.

    The complete set of CIM document types, that is, all classes which carry the
    document metadata attributes.
    """
    is_open = False
    members = [
        "Conformance",
        "Dataset",
        "DomainProperties",
        "Downscaling",
        "Ensemble",
        "EnsembleRequirement",
        "ExternalDocument",
        "ForcingConstraint",
        "Grid",
        "Machine",
        "Model",
        "MultiEnsemble",
        "MultiTimeEnsemble",
        "NumericalExperiment",
        "NumericalRequirement",
        "OutputTemporalRequirement",
        "Party",
        "Performance",
        "Project",
        "QualityReview",
        "ScientificDomain",
        "Simulation",
        "SimulationPlan",
        "TemporalConstraint",
        "UberEnsemble"
        ]


class NilReason(object):
    """An enumeration within the cim v2 type system.

    Provides an enumeration of possible reasons why a property has not been defined
    Based on GML nilReason as discussed here: https://www.seegrid.csiro.au/wiki/AppSchemas/NilValues.
    """
    is_open = False
    members = [
        "nil:inapplicable",
        "nil:missing",
        "nil:template",
        "nil:unknown",
        "nil:withheld"
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


class QualityStatus(object):
    """An enumeration within the cim v2 type system.

    Assertion as to the review status of document.
    """
    is_open = False
    members = [
        "finalised",
        "incomplete",
        "reviewed",
        "under_review"
        ]


class RoleCode(object):
    """An enumeration within the cim v2 type system.

    Responsibility role codes: roles that a party may play in delivering a responsibility.
    """
    is_open = False
    members = [
        "Principal Investigator",
        "author",
        "collaborator",
        "custodian",
        "distributor",
        "metadata_author",
        "metadata_reviewer",
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


