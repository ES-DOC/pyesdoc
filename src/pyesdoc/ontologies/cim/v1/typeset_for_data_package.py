"""
.. module:: cim.v1.typeset_for_data_package.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.data package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-09-06 15:59:51.490486.

"""
# Module imports.
import abc
import datetime
import uuid

import typeset_for_shared_package as shared




class DataContent(shared.DataSource):
    """A concrete class within the cim v1 type system.

    The contents of the data object; like ISO: MD_ContentInformation.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataContent, self).__init__()

        self.aggregation = str()                     # type = str
        self.frequency = str()                       # type = str
        self.topic = None                            # type = data.DataTopic


class DataDistribution(object):
    """A concrete class within the cim v1 type system.

    Describes how a DataObject is distributed.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataDistribution, self).__init__()

        self.access = str()                          # type = str
        self.fee = str()                             # type = str
        self.format = str()                          # type = str
        self.responsible_party = None                # type = shared.ResponsibleParty


class DataExtent(object):
    """A concrete class within the cim v1 type system.

    A data object extent represents the geographical and temporal coverage associated with a data object.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtent, self).__init__()

        self.geographical = None                     # type = data.DataExtentGeographical
        self.temporal = None                         # type = data.DataExtentTemporal


class DataExtentGeographical(object):
    """A concrete class within the cim v1 type system.

    A data object geographical extent represents the geographical coverage associated with a data object.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtentGeographical, self).__init__()

        self.east = float()                          # type = float
        self.north = float()                         # type = float
        self.south = float()                         # type = float
        self.west = float()                          # type = float


class DataExtentTemporal(object):
    """A concrete class within the cim v1 type system.

    A data object temporal extent represents the temporal coverage associated with a data object.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtentTemporal, self).__init__()

        self.begin = datetime.date(1900, 1, 1)       # type = datetime.date
        self.end = datetime.date(1900, 1, 1)         # type = datetime.date
        self.time_interval = None                    # type = data.DataExtentTimeInterval


class DataExtentTimeInterval(object):
    """A concrete class within the cim v1 type system.

    A data object temporal extent represents the temporal coverage associated with a data object.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtentTimeInterval, self).__init__()

        self.factor = int()                          # type = int
        self.radix = int()                           # type = int
        self.unit = str()                            # type = str


class DataHierarchyLevel(object):
    """A concrete class within the cim v1 type system.

    The type of data object that is grouped together into a particular hierarchy.  Currently, this is made up of terms describing how the Met Office splits up archived data and how THREDDS categorises variables.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataHierarchyLevel, self).__init__()

        self.is_open = bool()                        # type = bool
        self.name = ''                               # type = data.DataHierarchyType
        self.value = str()                           # type = str


class DataObject(shared.DataSource):
    """A concrete class within the cim v1 type system.

    A DataObject describes a unit of data.  DataObjects can be grouped hierarchically.  The attributes hierarchyLevelName and hierarchyLevelValue describe how objects are grouped.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataObject, self).__init__()

        self.acronym = str()                         # type = str
        self.child_object = []                       # type = data.DataObject
        self.cim_info = None                         # type = shared.CimInfo
        self.citations = []                          # type = shared.Citation
        self.content = []                            # type = data.DataContent
        self.data_property = []                      # type = data.DataProperty
        self.data_status = ''                        # type = data.DataStatusType
        self.description = str()                     # type = str
        self.distribution = None                     # type = data.DataDistribution
        self.extent = None                           # type = data.DataExtent
        self.geometry_model = str()                  # type = str
        self.hierarchy_level = None                  # type = data.DataHierarchyLevel
        self.keyword = str()                         # type = str
        self.parent_object = None                    # type = data.DataObject
        self.parent_object_reference = None          # type = shared.CimReference
        self.restriction = []                        # type = data.DataRestriction
        self.source_simulation = str()               # type = str
        self.storage = []                            # type = data.DataStorage


class DataProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    A property of a DataObject. Currently this is intended to be used to record CF specific information (like packing, scaling, etc.) for OASIS4.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataProperty, self).__init__()

        self.description = str()                     # type = str


class DataRestriction(object):
    """A concrete class within the cim v1 type system.

    An access or use restriction on some element of the DataObject's actual data.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataRestriction, self).__init__()

        self.license = None                          # type = shared.License
        self.restriction = str()                     # type = str
        self.scope = str()                           # type = str


class DataStorage(object):
    """An abstract class within the cim v1 type system.

    Describes the method that the DataObject is stored. An abstract class with specific child classes for each supported method.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(DataStorage, self).__init__()

        self.format = str()                          # type = str
        self.location = str()                        # type = str
        self.modification_date = datetime.datetime.now()# type = datetime.datetime
        self.size = int()                            # type = int


class DataTopic(object):
    """A concrete class within the cim v1 type system.

    Describes the content  of a data object; the variable's name, units, etc.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataTopic, self).__init__()

        self.description = str()                     # type = str
        self.name = str()                            # type = str
        self.unit = str()                            # type = str


class DataStorageDb(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a database file.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataStorageDb, self).__init__()

        self.access_string = str()                   # type = str
        self.name = str()                            # type = str
        self.owner = str()                           # type = str
        self.table = str()                           # type = str


class DataStorageFile(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a single file.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataStorageFile, self).__init__()

        self.file_name = str()                       # type = str
        self.file_system = str()                     # type = str
        self.path = str()                            # type = str


class DataStorageIp(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a database file.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataStorageIp, self).__init__()

        self.file_name = str()                       # type = str
        self.host = str()                            # type = str
        self.path = str()                            # type = str
        self.protocol = str()                        # type = str


class DataHierarchyType(object):
    """An enumeration within the cim v1 type system.

    What level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.
    """

    pass


class DataStatusType(object):
    """An enumeration within the cim v1 type system.

    Status of the data.
    """

    pass


