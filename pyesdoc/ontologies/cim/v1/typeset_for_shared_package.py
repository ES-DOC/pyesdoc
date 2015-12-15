# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_for_shared_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.shared package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
import abc
import datetime
import uuid




class Calendar(object):
    """An abstract class within the cim v1 type system.

    Describes a method of calculating a span of dates.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(Calendar, self).__init__()

        self.description = None                           # unicode
        self.length = None                                # int
        self.range = None                                 # shared.DateRange


class Change(object):
    """A concrete class within the cim v1 type system.

    A description of [a set of] changes applied at a particular time, by a particular party, to a particular unit of metadata.

    """
    def __init__(self):
        """Constructor.

        """
        super(Change, self).__init__()

        self.author = None                                # shared.ResponsibleParty
        self.date = None                                  # datetime.datetime
        self.description = None                           # unicode
        self.details = []                                 # shared.ChangeProperty
        self.name = None                                  # unicode
        self.type = None                                  # shared.ChangePropertyType


class Citation(object):
    """A concrete class within the cim v1 type system.

    An academic reference to published work.

    """
    def __init__(self):
        """Constructor.

        """
        super(Citation, self).__init__()

        self.alternative_title = None                     # unicode
        self.collective_title = None                      # unicode
        self.date = None                                  # datetime.datetime
        self.date_type = None                             # unicode
        self.location = None                              # unicode
        self.organisation = None                          # unicode
        self.reference = None                             # shared.DocReference
        self.role = None                                  # unicode
        self.title = None                                 # unicode
        self.type = None                                  # unicode


class Compiler(object):
    """A concrete class within the cim v1 type system.

    A description of a compiler used on a particular platform.

    """
    def __init__(self):
        """Constructor.

        """
        super(Compiler, self).__init__()

        self.environment_variables = None                 # unicode
        self.language = None                              # unicode
        self.name = None                                  # unicode
        self.options = None                               # unicode
        self.type = None                                  # shared.CompilerType
        self.version = None                               # unicode


class DataSource(object):
    """An abstract class within the cim v1 type system.

    A DataSource can be realised by either a DataObject (file), a DataContent (variable), a Component (model), or a ComponentProperty (variable); all of those can supply data.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(DataSource, self).__init__()

        self.purpose = None                               # shared.DataPurpose


class DateRange(object):
    """An abstract class within the cim v1 type system.

    Creates and returns instance of date_range class.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(DateRange, self).__init__()

        self.duration = None                              # unicode


class DocGenealogy(object):
    """A concrete class within the cim v1 type system.

    A record of a document's history. A genealogy element contains a textual description and a set of relationships. Each relationship has a type and a reference to some target. There are different relationships for different document types.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocGenealogy, self).__init__()

        self.relationships = []                           # shared.DocRelationship


class DocMetaInfo(object):
    """A concrete class within the cim v1 type system.

    Encapsulates document meta information.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocMetaInfo, self).__init__()

        self.author = None                                # shared.ResponsibleParty
        self.create_date = None                           # datetime.datetime
        self.drs_keys = []                                # unicode
        self.drs_path = None                              # unicode
        self.external_ids = []                            # shared.StandardName
        self.genealogy = None                             # shared.DocGenealogy
        self.id = None                                    # uuid.UUID
        self.institute = None                             # unicode
        self.language = None                              # unicode
        self.project = None                               # unicode
        self.sort_key = None                              # unicode
        self.source = None                                # unicode
        self.source_key = None                            # unicode
        self.status = None                                # shared.DocStatusType
        self.type = None                                  # unicode
        self.type_display_name = None                     # unicode
        self.type_sort_key = None                         # unicode
        self.update_date = None                           # datetime.datetime
        self.version = None                               # int
        self.source = unicode("scripts")


class DocReference(object):
    """A concrete class within the cim v1 type system.

    A reference to another cim entity.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocReference, self).__init__()

        self.changes = []                                 # shared.Change
        self.description = None                           # unicode
        self.external_id = None                           # unicode
        self.id = None                                    # uuid.UUID
        self.name = None                                  # unicode
        self.type = None                                  # unicode
        self.url = None                                   # unicode
        self.version = None                               # int


class DocRelationshipTarget(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of doc_relationship_target class.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocRelationshipTarget, self).__init__()

        self.document = None                              # shared.DocType
        self.reference = None                             # shared.DocReference


class License(object):
    """A concrete class within the cim v1 type system.

    A description of a license restricting access to a unit of data or software.

    """
    def __init__(self):
        """Constructor.

        """
        super(License, self).__init__()

        self.contact = None                               # unicode
        self.description = None                           # unicode
        self.is_unrestricted = None                       # bool
        self.name = None                                  # unicode


class Machine(object):
    """A concrete class within the cim v1 type system.

    A description of a machine used by a particular platform.

    """
    def __init__(self):
        """Constructor.

        """
        super(Machine, self).__init__()

        self.cores_per_processor = None                   # int
        self.description = None                           # unicode
        self.interconnect = None                          # shared.InterconnectType
        self.libraries = []                               # unicode
        self.location = None                              # unicode
        self.maximum_processors = None                    # int
        self.name = None                                  # unicode
        self.operating_system = None                      # shared.OperatingSystemType
        self.processor_type = None                        # shared.ProcessorType
        self.system = None                                # unicode
        self.type = None                                  # shared.MachineType
        self.vendor = None                                # shared.MachineVendorType


class MachineCompilerUnit(object):
    """A concrete class within the cim v1 type system.

    Associates a machine with a [set of] compilers.  This is a separate class in case a platform needs to specify more than one machine/compiler pair.

    """
    def __init__(self):
        """Constructor.

        """
        super(MachineCompilerUnit, self).__init__()

        self.compilers = []                               # shared.Compiler
        self.machine = None                               # shared.Machine


class Platform(object):
    """A concrete class within the cim v1 type system.

    A platform is a description of resources used to deploy a component/simulation.  A platform pairs a machine with a (set of) compilers.  There is also a point of contact for the platform.

    """
    def __init__(self):
        """Constructor.

        """
        super(Platform, self).__init__()

        self.contacts = []                                # shared.ResponsibleParty
        self.description = None                           # unicode
        self.long_name = None                             # unicode
        self.meta = DocMetaInfo()                         # shared.DocMetaInfo
        self.short_name = None                            # unicode
        self.units = []                                   # shared.MachineCompilerUnit


class Property(object):
    """A concrete class within the cim v1 type system.

    A simple name/value pair representing a property of some entity or other.

    """
    def __init__(self):
        """Constructor.

        """
        super(Property, self).__init__()

        self.name = None                                  # unicode
        self.value = None                                 # unicode


class Relationship(object):
    """An abstract class within the cim v1 type system.

    A record of a relationship between one document and another. This class is abstract; specific document types must specialise this class for their relationshipTypes to be included in a document's genealogy.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(Relationship, self).__init__()

        self.description = None                           # unicode
        self.direction = None                             # shared.DocRelationshipDirectionType


class ResponsibleParty(object):
    """A concrete class within the cim v1 type system.

    A person/organsiation responsible for some aspect of a climate science artefact.

    """
    def __init__(self):
        """Constructor.

        """
        super(ResponsibleParty, self).__init__()

        self.abbreviation = None                          # unicode
        self.address = None                               # unicode
        self.email = None                                 # unicode
        self.individual_name = None                       # unicode
        self.organisation_name = None                     # unicode
        self.role = None                                  # unicode
        self.url = None                                   # unicode


class Standard(object):
    """A concrete class within the cim v1 type system.

    Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

    """
    def __init__(self):
        """Constructor.

        """
        super(Standard, self).__init__()

        self.description = None                           # unicode
        self.name = None                                  # unicode
        self.version = None                               # unicode


class StandardName(object):
    """A concrete class within the cim v1 type system.

    Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

    """
    def __init__(self):
        """Constructor.

        """
        super(StandardName, self).__init__()

        self.is_open = None                               # bool
        self.standards = []                               # shared.Standard
        self.value = None                                 # unicode


class ChangeProperty(Property):
    """A concrete class within the cim v1 type system.

    A description of a single change applied to a single target.  Every ChangeProperty has a description, and may also have a name from a controlled vocabulary and a value.

    """
    def __init__(self):
        """Constructor.

        """
        super(ChangeProperty, self).__init__()

        self.description = None                           # unicode
        self.id = None                                    # unicode


class ClosedDateRange(DateRange):
    """A concrete class within the cim v1 type system.

    A date range with specified start and end points.

    """
    def __init__(self):
        """Constructor.

        """
        super(ClosedDateRange, self).__init__()

        self.end = None                                   # datetime.datetime
        self.start = None                                 # datetime.datetime


class Daily360(Calendar):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of daily_360 class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Daily360, self).__init__()



class DocRelationship(Relationship):
    """A concrete class within the cim v1 type system.

    Contains the set of relationships supported by a Document.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocRelationship, self).__init__()

        self.target = None                                # shared.DocRelationshipTarget
        self.type = None                                  # shared.DocRelationshipType


class OpenDateRange(DateRange):
    """A concrete class within the cim v1 type system.

    A date range without a specified start and/or end point.

    """
    def __init__(self):
        """Constructor.

        """
        super(OpenDateRange, self).__init__()

        self.end = None                                   # datetime.datetime
        self.start = None                                 # datetime.datetime


class PerpetualPeriod(Calendar):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of perpetual_period class.

    """
    def __init__(self):
        """Constructor.

        """
        super(PerpetualPeriod, self).__init__()



class RealCalendar(Calendar):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of real_calendar class.

    """
    def __init__(self):
        """Constructor.

        """
        super(RealCalendar, self).__init__()



class ChangePropertyType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of change_property_type enum.
    """

    pass


class CompilerType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of compiler_type enum.
    """

    pass


class DataPurpose(object):
    """An enumeration within the cim v1 type system.

    Purpose of the data - i.e. ancillaryFile, boundaryCondition or initialCondition.
    """

    pass


class DocRelationshipDirectionType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of relationship_direction_type enum.
    """

    pass


class DocRelationshipType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of document_relationship_type enum.
    """

    pass


class DocStatusType(object):
    """An enumeration within the cim v1 type system.

    Status of cim document.
    """

    pass


class DocType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of doc_type enum.
    """

    pass


class InterconnectType(object):
    """An enumeration within the cim v1 type system.

    A list of connectors between machines.
    """

    pass


class MachineType(object):
    """An enumeration within the cim v1 type system.

    A list of known machines.
    """

    pass


class MachineVendorType(object):
    """An enumeration within the cim v1 type system.

    A list of organisations that create machines.
    """

    pass


class OperatingSystemType(object):
    """An enumeration within the cim v1 type system.

    A list of common operating systems.
    """

    pass


class ProcessorType(object):
    """An enumeration within the cim v1 type system.

    A list of known cpu's.
    """

    pass


class UnitType(object):
    """An enumeration within the cim v1 type system.

    A list of scientific units.
    """

    pass


