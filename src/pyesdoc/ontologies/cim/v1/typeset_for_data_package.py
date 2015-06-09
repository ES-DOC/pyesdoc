# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_for_data_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.data package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-05 15:44:25.801759.

"""
import abc
import datetime
import uuid

import typeset_for_data_package as data
import typeset_for_shared_package as shared



class DataExtent(object):
    """A concrete class within the cim v1 type system.

    A data object extent represents the geographical and temporal coverage associated with a data object.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtent, self).__init__()

        self.geographical = None                          # data.DataExtentGeographical
        self.temporal = None                              # data.DataExtentTemporal


class DataRestriction(object):
    """A concrete class within the cim v1 type system.

    An access or use restriction on some element of the DataObject actual data.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataRestriction, self).__init__()

        self.scope = None                                 # str
        self.license = None                               # shared.License
        self.restriction = None                           # str


class DataExtentGeographical(object):
    """A concrete class within the cim v1 type system.

    A data object geographical extent represents the geographical coverage associated with a data object.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtentGeographical, self).__init__()

        self.west = None                                  # float
        self.south = None                                 # float
        self.east = None                                  # float
        self.north = None                                 # float


class DataExtentTimeInterval(object):
    """A concrete class within the cim v1 type system.

    A data object temporal extent represents the temporal coverage associated with a data object.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtentTimeInterval, self).__init__()

        self.unit = None                                  # str
        self.factor = None                                # int
        self.radix = None                                 # int


class DataExtentTemporal(object):
    """A concrete class within the cim v1 type system.

    A data object temporal extent represents the temporal coverage associated with a data object.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtentTemporal, self).__init__()

        self.begin = None                                 # datetime.date
        self.time_interval = None                         # data.DataExtentTimeInterval
        self.end = None                                   # datetime.date


class DataObject(shared.DataSource):
    """A concrete class within the cim v1 type system.

    A DataObject describes a unit of data.  DataObjects can be grouped hierarchically.  The attributes hierarchyLevelName and hierarchyLevelValue describe how objects are grouped.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataObject, self).__init__()

        self.hierarchy_level = None                       # data.DataHierarchyLevel
        self.keyword = None                               # str
        self.child_object = []                            # data.DataObject
        self.properties = []                              # data.DataProperty
        self.storage = []                                 # data.DataStorage
        self.description = None                           # str
        self.purpose = None                               # str
        self.citations = []                               # shared.Citation
        self.source_simulation = None                     # str
        self.acronym = None                               # str
        self.distribution = None                          # data.DataDistribution
        self.restriction = []                             # data.DataRestriction
        self.content = []                                 # data.DataContent
        self.parent_object_reference = None               # shared.DocReference
        self.parent_object = None                         # data.DataObject
        self.extent = None                                # data.DataExtent
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.data_status = None                           # data.DataStatusType
        self.geometry_model = None                        # str


class DataProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    A property of a DataObject. Currently this is intended to be used to record CF specific information (like packing, scaling, etc.) for OASIS4.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataProperty, self).__init__()

        self.description = None                           # str


class DataDistribution(object):
    """A concrete class within the cim v1 type system.

    Describes how a DataObject is distributed.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataDistribution, self).__init__()

        self.access = None                                # str
        self.format = None                                # str
        self.responsible_party = None                     # shared.ResponsibleParty
        self.fee = None                                   # str


class DataHierarchyLevel(object):
    """A concrete class within the cim v1 type system.

    The type of data object that is grouped together into a particular hierarchy.  Currently, this is made up of terms describing how the Met Office splits up archived data and how THREDDS categorises variables.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataHierarchyLevel, self).__init__()

        self.is_open = None                               # bool
        self.value = None                                 # str
        self.name = None                                  # data.DataHierarchyType


class DataTopic(object):
    """A concrete class within the cim v1 type system.

    Describes the content of a data object: the variable name, units, etc.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataTopic, self).__init__()

        self.unit = None                                  # str
        self.description = None                           # str
        self.name = None                                  # str


class DataContent(shared.DataSource):
    """A concrete class within the cim v1 type system.

    The contents of the data object; like ISO: MD_ContentInformation.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataContent, self).__init__()

        self.aggregation = None                           # str
        self.topic = None                                 # data.DataTopic
        self.frequency = None                             # str


class DataStorage(object):
    """An abstract class within the cim v1 type system.

    Describes the method that the DataObject is stored. An abstract class with specific child classes for each supported method.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(DataStorage, self).__init__()

        self.format = None                                # str
        self.size = None                                  # int
        self.modification_date = None                     # datetime.datetime
        self.location = None                              # str


class DataStorageIp(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a database file.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataStorageIp, self).__init__()

        self.host = None                                  # str
        self.protocol = None                              # str
        self.file_name = None                             # str
        self.path = None                                  # str


class DataStorageFile(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a single file.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataStorageFile, self).__init__()

        self.file_name = None                             # str
        self.path = None                                  # str
        self.file_system = None                           # str


class DataStorageDb(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a database file.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataStorageDb, self).__init__()

        self.access_string = None                         # str
        self.owner = None                                 # str
        self.table = None                                 # str
        self.name = None                                  # str


class DataHierarchyType(object):
    """An enumeration within the cim v1 type system.

    Enumerates the level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.
    """

    pass


class DataStatusType(object):
    """An enumeration within the cim v1 type system.

    Enumerates status of a data object.
    """

    pass


