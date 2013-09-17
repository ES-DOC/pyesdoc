"""
.. module:: cim.v1.typeset_for_data_package.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.data package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-09-17 11:53:50.232944.

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

        self.aggregation = str()                          # str
        self.frequency = str()                            # str
        self.topic = DataTopic()                          # data.DataTopic


class DataDistribution(object):
    """A concrete class within the cim v1 type system.

    Describes how a DataObject is distributed.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataDistribution, self).__init__()

        self.access = str()                               # str
        self.fee = str()                                  # str
        self.format = str()                               # str
        self.responsible_party = None                     # shared.ResponsibleParty


class DataExtent(object):
    """A concrete class within the cim v1 type system.

    A data object extent represents the geographical and temporal coverage associated with a data object.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtent, self).__init__()

        self.geographical = DataExtentGeographical()      # data.DataExtentGeographical
        self.temporal = DataExtentTemporal()              # data.DataExtentTemporal


class DataExtentGeographical(object):
    """A concrete class within the cim v1 type system.

    A data object geographical extent represents the geographical coverage associated with a data object.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtentGeographical, self).__init__()

        self.east = float()                               # float
        self.north = float()                              # float
        self.south = float()                              # float
        self.west = float()                               # float


class DataExtentTemporal(object):
    """A concrete class within the cim v1 type system.

    A data object temporal extent represents the temporal coverage associated with a data object.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtentTemporal, self).__init__()

        self.begin = datetime.date(1900, 1, 1)            # datetime.date
        self.end = datetime.date(1900, 1, 1)              # datetime.date
        self.time_interval = None                         # data.DataExtentTimeInterval


class DataExtentTimeInterval(object):
    """A concrete class within the cim v1 type system.

    A data object temporal extent represents the temporal coverage associated with a data object.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtentTimeInterval, self).__init__()

        self.factor = int()                               # int
        self.radix = int()                                # int
        self.unit = str()                                 # str


class DataHierarchyLevel(object):
    """A concrete class within the cim v1 type system.

    The type of data object that is grouped together into a particular hierarchy.  Currently, this is made up of terms describing how the Met Office splits up archived data and how THREDDS categorises variables.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataHierarchyLevel, self).__init__()

        self.is_open = bool()                             # bool
        self.name = ''                                    # data.DataHierarchyType
        self.value = str()                                # str


class DataObject(shared.DataSource):
    """A concrete class within the cim v1 type system.

    A DataObject describes a unit of data.  DataObjects can be grouped hierarchically.  The attributes hierarchyLevelName and hierarchyLevelValue describe how objects are grouped.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataObject, self).__init__()

        self.acronym = str()                              # str
        self.child_object = []                            # data.DataObject
        self.citations = []                               # shared.Citation
        self.content = []                                 # data.DataContent
        self.data_property = []                           # data.DataProperty
        self.data_status = ''                             # data.DataStatusType
        self.description = str()                          # str
        self.distribution = None                          # data.DataDistribution
        self.doc_info = shared.DocInfo()                  # shared.DocInfo
        self.extent = None                                # data.DataExtent
        self.geometry_model = str()                       # str
        self.hierarchy_level = None                       # data.DataHierarchyLevel
        self.keyword = str()                              # str
        self.parent_object = None                         # data.DataObject
        self.parent_object_reference = None               # shared.DocReference
        self.restriction = []                             # data.DataRestriction
        self.source_simulation = str()                    # str
        self.storage = []                                 # data.DataStorage


class DataProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    A property of a DataObject. Currently this is intended to be used to record CF specific information (like packing, scaling, etc.) for OASIS4.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataProperty, self).__init__()

        self.description = str()                          # str


class DataRestriction(object):
    """A concrete class within the cim v1 type system.

    An access or use restriction on some element of the DataObject's actual data.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataRestriction, self).__init__()

        self.license = None                               # shared.License
        self.restriction = str()                          # str
        self.scope = str()                                # str


class DataStorage(object):
    """An abstract class within the cim v1 type system.

    Describes the method that the DataObject is stored. An abstract class with specific child classes for each supported method.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(DataStorage, self).__init__()

        self.format = str()                               # str
        self.location = str()                             # str
        self.modification_date = datetime.datetime.now()  # datetime.datetime
        self.size = int()                                 # int


class DataTopic(object):
    """A concrete class within the cim v1 type system.

    Describes the content  of a data object; the variable's name, units, etc.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataTopic, self).__init__()

        self.description = str()                          # str
        self.name = str()                                 # str
        self.unit = str()                                 # str


class DataStorageDb(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a database file.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataStorageDb, self).__init__()

        self.access_string = str()                        # str
        self.name = str()                                 # str
        self.owner = str()                                # str
        self.table = str()                                # str


class DataStorageFile(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a single file.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataStorageFile, self).__init__()

        self.file_name = str()                            # str
        self.file_system = str()                          # str
        self.path = str()                                 # str


class DataStorageIp(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a database file.
    """
    def __init__(self):
        """Constructor.

        """
        super(DataStorageIp, self).__init__()

        self.file_name = str()                            # str
        self.host = str()                                 # str
        self.path = str()                                 # str
        self.protocol = str()                             # str


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


