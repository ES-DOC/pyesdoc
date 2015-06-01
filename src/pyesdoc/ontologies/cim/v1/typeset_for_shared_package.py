# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_for_shared_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.shared package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-01 16:50:10.364320.

"""
import abc
import datetime
import uuid




class Calendar(object):
    """An abstract class within the cim v1 type system.

    Creates and returns instance of calendar class.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(Calendar, self).__init__()

        self.description = None                           # str
        self.length = None                                # int
        self.range = None                                 # shared.DateRange


class Change(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of change class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Change, self).__init__()

        self.author = None                                # shared.ResponsibleParty
        self.date = None                                  # datetime.datetime
        self.description = None                           # str
        self.details = []                                 # shared.ChangeProperty
        self.name = None                                  # str
        self.type = None                                  # shared.ChangePropertyType


class Citation(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of citation class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Citation, self).__init__()

        self.alternative_title = None                     # str
        self.collective_title = None                      # str
        self.date = None                                  # datetime.datetime
        self.date_type = None                             # str
        self.location = None                              # str
        self.organisation = None                          # str
        self.reference = None                             # shared.DocReference
        self.role = None                                  # str
        self.title = None                                 # str
        self.type = None                                  # str


class Compiler(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of compiler class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Compiler, self).__init__()

        self.environment_variables = None                 # str
        self.language = None                              # str
        self.name = None                                  # str
        self.options = None                               # str
        self.type = None                                  # shared.CompilerType
        self.version = None                               # str


class DataSource(object):
    """An abstract class within the cim v1 type system.

    Creates and returns instance of data_source class.

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

        self.duration = None                              # str


class DocGenealogy(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of doc_genealogy class.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocGenealogy, self).__init__()

        self.relationships = []                           # shared.DocRelationship


class DocMetaInfo(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of doc_meta_info class.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocMetaInfo, self).__init__()

        self.author = None                                # shared.ResponsibleParty
        self.create_date = None                           # datetime.datetime
        self.drs_keys = []                                # str
        self.drs_path = None                              # str
        self.encodings = []                               # str
        self.external_ids = []                            # shared.StandardName
        self.genealogy = None                             # shared.DocGenealogy
        self.id = None                                    # uuid.UUID
        self.institute = None                             # str
        self.language = None                              # str
        self.metadata_id = None                           # str
        self.metadata_version = None                      # str
        self.project = None                               # str
        self.sort_key = None                              # str
        self.source = None                                # str
        self.source_key = None                            # str
        self.status = None                                # shared.DocStatusType
        self.type = None                                  # str
        self.type_display_name = None                     # str
        self.type_sort_key = None                         # str
        self.version = None                               # int


class DocReference(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of reference class.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocReference, self).__init__()

        self.changes = []                                 # shared.Change
        self.description = None                           # str
        self.external_id = None                           # str
        self.id = None                                    # uuid.UUID
        self.name = None                                  # str
        self.type = None                                  # str
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

    Creates and returns instance of license class.

    """
    def __init__(self):
        """Constructor.

        """
        super(License, self).__init__()

        self.contact = None                               # str
        self.description = None                           # str
        self.is_unrestricted = None                       # str
        self.name = None                                  # str


class Machine(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of machine class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Machine, self).__init__()

        self.cores_per_processor = None                   # int
        self.description = None                           # str
        self.interconnect = None                          # shared.InterconnectType
        self.libraries = []                               # str
        self.location = None                              # str
        self.maximum_processors = None                    # int
        self.name = None                                  # str
        self.operating_system = None                      # shared.OperatingSystemType
        self.processor_type = None                        # shared.ProcessorType
        self.system = None                                # str
        self.type = None                                  # shared.MachineType
        self.vendor = None                                # shared.MachineVendorType


class MachineCompilerUnit(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of machine_compiler_unit class.

    """
    def __init__(self):
        """Constructor.

        """
        super(MachineCompilerUnit, self).__init__()

        self.compilers = []                               # shared.Compiler
        self.machine = None                               # shared.Machine


class Platform(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of platform class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Platform, self).__init__()

        self.contacts = []                                # shared.ResponsibleParty
        self.description = None                           # str
        self.long_name = None                             # str
        self.meta = DocMetaInfo()                         # shared.DocMetaInfo
        self.short_name = None                            # str
        self.units = []                                   # shared.MachineCompilerUnit


class Property(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of property class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Property, self).__init__()

        self.name = None                                  # str
        self.value = None                                 # str


class Relationship(object):
    """An abstract class within the cim v1 type system.

    Creates and returns instance of relationship class.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(Relationship, self).__init__()

        self.description = None                           # str
        self.direction = None                             # shared.DocRelationshipDirectionType


class ResponsibleParty(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of responsible_party class.

    """
    def __init__(self):
        """Constructor.

        """
        super(ResponsibleParty, self).__init__()

        self.abbreviation = None                          # str
        self.address = None                               # str
        self.email = None                                 # str
        self.individual_name = None                       # str
        self.organisation_name = None                     # str
        self.role = None                                  # str
        self.url = None                                   # str


class Standard(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of standard class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Standard, self).__init__()

        self.description = None                           # str
        self.name = None                                  # str
        self.version = None                               # str


class StandardName(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of standard_name class.

    """
    def __init__(self):
        """Constructor.

        """
        super(StandardName, self).__init__()

        self.is_open = None                               # bool
        self.standards = []                               # shared.Standard
        self.value = None                                 # str


class ChangeProperty(Property):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of change class.

    """
    def __init__(self):
        """Constructor.

        """
        super(ChangeProperty, self).__init__()

        self.description = None                           # str
        self.id = None                                    # str


class ClosedDateRange(DateRange):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of closed_date_range class.

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

    Creates and returns instance of doc_relationship class.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocRelationship, self).__init__()

        self.target = None                                # shared.DocRelationshipTarget
        self.type = None                                  # shared.DocRelationshipType


class OpenDateRange(DateRange):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of open_date_range class.

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

    Creates and returns instance of data_purpose enum.
    """

    pass


class InterconnectType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of interconnect_type enum.
    """

    pass


class MachineType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of machine_type enum.
    """

    pass


class MachineVendorType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of machine_vendor_type enum.
    """

    pass


class OperatingSystemType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of operating_system_type enum.
    """

    pass


class ProcessorType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of processor_type enum.
    """

    pass


class UnitType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of unit_type enum.
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

    Creates and returns instance of doc_status_type enum.
    """

    pass


class DocType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of doc_type enum.
    """

    pass


