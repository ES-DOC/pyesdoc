"""
.. module:: cim.v1.typeset_for_shared_package.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.shared package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-09-06 15:59:51.497346.

"""
# Module imports.
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

        self.description = str()                     # type = str
        self.length = int()                          # type = int
        self.range = None                            # type = shared.DateRange


class Change(object):
    """A concrete class within the cim v1 type system.

    A description of [a set of] changes applied at a particular time, by a particular party, to a particular unit of metadata.
    """
    def __init__(self):
        """Constructor.

        """
        super(Change, self).__init__()

        self.author = None                           # type = shared.ResponsibleParty
        self.date = datetime.datetime.now()          # type = datetime.datetime
        self.description = str()                     # type = str
        self.details = []                            # type = shared.ChangeProperty
        self.name = str()                            # type = str
        self.type = ''                               # type = shared.ChangePropertyType


class CimDocumentRelationshipTarget(object):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(CimDocumentRelationshipTarget, self).__init__()

        self.document = ''                           # type = shared.CimDocumentType
        self.reference = None                        # type = shared.CimReference


class CimGenealogy(object):
    """A concrete class within the cim v1 type system.

    A record of a document's history. A genealogy element contains a textual description and a set of relationships. Each relationship has a type and a reference to some target. There are different relationships for different document types.
    """
    def __init__(self):
        """Constructor.

        """
        super(CimGenealogy, self).__init__()

        self.relationships = []                      # type = shared.CimRelationship


class CimInfo(object):
    """A concrete class within the cim v1 type system.

    Encapsulates common cim information.
    """
    def __init__(self):
        """Constructor.

        """
        super(CimInfo, self).__init__()

        self.author = None                           # type = shared.ResponsibleParty
        self.create_date = datetime.datetime.now()   # type = datetime.datetime
        self.external_ids = []                       # type = shared.StandardName
        self.genealogy = None                        # type = shared.CimGenealogy
        self.id = uuid.uuid4()                       # type = uuid.UUID
        self.language = str()                        # type = str
        self.metadata_id = str()                     # type = str
        self.metadata_version = str()                # type = str
        self.project = str()                         # type = str
        self.source = str()                          # type = str
        self.status = ''                             # type = shared.DocumentStatusType
        self.version = str()                         # type = str


class CimReference(object):
    """A concrete class within the cim v1 type system.

    A reference to another cim entity
    """
    def __init__(self):
        """Constructor.

        """
        super(CimReference, self).__init__()

        self.changes = []                            # type = shared.Change
        self.description = str()                     # type = str
        self.external_id = str()                     # type = str
        self.id = uuid.uuid4()                       # type = uuid.UUID
        self.name = str()                            # type = str
        self.type = str()                            # type = str
        self.version = str()                         # type = str


class CimRelationship(object):
    """An abstract class within the cim v1 type system.

    A record of a relationship between one document and another. This class is abstract; specific document types must specialise this class for their relationshipTypes to be included in a document's genealogy.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(CimRelationship, self).__init__()

        self.description = str()                     # type = str
        self.direction = ''                          # type = shared.CimRelationshipDirectionType


class Citation(object):
    """A concrete class within the cim v1 type system.

    An academic reference to published work.
    """
    def __init__(self):
        """Constructor.

        """
        super(Citation, self).__init__()

        self.alternative_title = str()               # type = str
        self.collective_title = str()                # type = str
        self.date = datetime.datetime.now()          # type = datetime.datetime
        self.date_type = str()                       # type = str
        self.location = str()                        # type = str
        self.organisation = str()                    # type = str
        self.reference = None                        # type = shared.CimReference
        self.role = str()                            # type = str
        self.title = str()                           # type = str
        self.type = str()                            # type = str


class Compiler(object):
    """A concrete class within the cim v1 type system.

    A description of a compiler used on a particular platform.
    """
    def __init__(self):
        """Constructor.

        """
        super(Compiler, self).__init__()

        self.environment_variables = str()           # type = str
        self.language = str()                        # type = str
        self.name = str()                            # type = str
        self.options = str()                         # type = str
        self.type = ''                               # type = shared.CompilerType
        self.version = str()                         # type = str


class DataSource(object):
    """An abstract class within the cim v1 type system.

    A DataSource can be realised by either a DataObject (file), a DataContent (variable), a Component (model), or a ComponentProperty (variable); all of those can supply data.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(DataSource, self).__init__()

        self.purpose = ''                            # type = shared.DataPurpose


class DateRange(object):
    """An abstract class within the cim v1 type system.

    
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(DateRange, self).__init__()

        self.duration = str()                        # type = str


class License(object):
    """A concrete class within the cim v1 type system.

    A description of a license restricting access to a unit of data or software
    """
    def __init__(self):
        """Constructor.

        """
        super(License, self).__init__()

        self.contact = str()                         # type = str
        self.description = str()                     # type = str
        self.is_unrestricted = str()                 # type = str
        self.name = str()                            # type = str


class Machine(object):
    """A concrete class within the cim v1 type system.

    A description of a machine used by a particular platform
    """
    def __init__(self):
        """Constructor.

        """
        super(Machine, self).__init__()

        self.cores_per_processor = int()             # type = int
        self.description = str()                     # type = str
        self.interconnect = ''                       # type = shared.InterconnectType
        self.libraries = []                          # type = str
        self.location = str()                        # type = str
        self.maximum_processors = int()              # type = int
        self.name = str()                            # type = str
        self.operating_system = ''                   # type = shared.OperatingSystemType
        self.processor_type = ''                     # type = shared.ProcessorType
        self.system = str()                          # type = str
        self.type = ''                               # type = shared.MachineType
        self.vendor = ''                             # type = shared.MachineVendorType


class MachineCompilerUnit(object):
    """A concrete class within the cim v1 type system.

    Associates a machine with a [set of] compilers.  This is a separate class in case a platform needs to specify more than one machine/compiler pair.
    """
    def __init__(self):
        """Constructor.

        """
        super(MachineCompilerUnit, self).__init__()

        self.compilers = []                          # type = shared.Compiler
        self.machine = None                          # type = shared.Machine


class Platform(object):
    """A concrete class within the cim v1 type system.

    A platform is a description of resources used to deploy a component/simulation.  A platform pairs a machine with a (set of) compilers.  There is also a point of contact for the platform.
    """
    def __init__(self):
        """Constructor.

        """
        super(Platform, self).__init__()

        self.cim_info = None                         # type = shared.CimInfo
        self.contacts = []                           # type = shared.ResponsibleParty
        self.description = str()                     # type = str
        self.long_name = str()                       # type = str
        self.short_name = str()                      # type = str
        self.units = []                              # type = shared.MachineCompilerUnit


class Property(object):
    """A concrete class within the cim v1 type system.

    A simple name/value pair representing a property of some entity or other
    """
    def __init__(self):
        """Constructor.

        """
        super(Property, self).__init__()

        self.name = str()                            # type = str
        self.value = str()                           # type = str


class ResponsibleParty(object):
    """A concrete class within the cim v1 type system.

    A person/organsiation responsible for some aspect of a climate science artefact
    """
    def __init__(self):
        """Constructor.

        """
        super(ResponsibleParty, self).__init__()

        self.abbreviation = str()                    # type = str
        self.contact_info = None                     # type = shared.ResponsiblePartyContactInfo
        self.individual_name = str()                 # type = str
        self.organisation_name = str()               # type = str
        self.role = str()                            # type = str


class ResponsiblePartyContactInfo(object):
    """A concrete class within the cim v1 type system.

    Maps gmd:contactInfo element.
    """
    def __init__(self):
        """Constructor.

        """
        super(ResponsiblePartyContactInfo, self).__init__()

        self.address = str()                         # type = str
        self.email = str()                           # type = str
        self.url = str()                             # type = str


class Standard(object):
    """A concrete class within the cim v1 type system.

    Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.
    """
    def __init__(self):
        """Constructor.

        """
        super(Standard, self).__init__()

        self.description = str()                     # type = str
        self.name = str()                            # type = str
        self.version = str()                         # type = str


class StandardName(object):
    """A concrete class within the cim v1 type system.

    Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.
    """
    def __init__(self):
        """Constructor.

        """
        super(StandardName, self).__init__()

        self.is_open = bool()                        # type = bool
        self.standards = []                          # type = shared.Standard
        self.value = str()                           # type = str


class ChangeProperty(Property):
    """A concrete class within the cim v1 type system.

    A description of a single change applied to a single target.  Every ChangeProperty has a description, and may also have a name from a controlled vocabulary and a value.
    """
    def __init__(self):
        """Constructor.

        """
        super(ChangeProperty, self).__init__()

        self.description = str()                     # type = str
        self.id = str()                              # type = str


class CimDocumentRelationship(CimRelationship):
    """A concrete class within the cim v1 type system.

    Contains the set of relationships supported by a Document.
    """
    def __init__(self):
        """Constructor.

        """
        super(CimDocumentRelationship, self).__init__()

        self.target = None                           # type = shared.CimDocumentRelationshipTarget
        self.type = ''                               # type = shared.CimDocumentRelationshipType


class ClosedDateRange(DateRange):
    """A concrete class within the cim v1 type system.

    A date range with specified start and end points.
    """
    def __init__(self):
        """Constructor.

        """
        super(ClosedDateRange, self).__init__()

        self.end = datetime.datetime.now()           # type = datetime.datetime
        self.start = datetime.datetime.now()         # type = datetime.datetime


class Daily360(Calendar):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(Daily360, self).__init__()



class OpenDateRange(DateRange):
    """A concrete class within the cim v1 type system.

    A date range without a specified start and/or end point.
    """
    def __init__(self):
        """Constructor.

        """
        super(OpenDateRange, self).__init__()

        self.end = datetime.datetime.now()           # type = datetime.datetime
        self.start = datetime.datetime.now()         # type = datetime.datetime


class PerpetualPeriod(Calendar):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(PerpetualPeriod, self).__init__()



class RealCalendar(Calendar):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(RealCalendar, self).__init__()



class ChangePropertyType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class CimDocumentRelationshipType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class CimDocumentType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class CimRelationshipDirectionType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class CompilerType(object):
    """An enumeration within the cim v1 type system.

    A list of known compilers.
    """

    pass


class DataPurpose(object):
    """An enumeration within the cim v1 type system.

    Purpose of the data - i.e. ancillaryFile, boundaryCondition or initialCondition.
    """

    pass


class DocumentStatusType(object):
    """An enumeration within the cim v1 type system.

    Status of cim document.
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


