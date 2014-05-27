# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_for_data_package.py

   :copyright: @2014 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.data package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2014-05-27 15:15:32.836242.

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

        self.aggregation = None                           # str
        self.frequency = None                             # str
        self.topic = None                                 # data.DataTopic


class DataDistribution(object):
    """A concrete class within the cim v1 type system.

    Describes how a DataObject is distributed.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataDistribution, self).__init__()

        self.access = None                                # str
        self.fee = None                                   # str
        self.format = None                                # str
        self.responsible_party = None                     # shared.ResponsibleParty


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


class DataExtentGeographical(object):
    """A concrete class within the cim v1 type system.

    A data object geographical extent represents the geographical coverage associated with a data object.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtentGeographical, self).__init__()

        self.east = None                                  # float
        self.north = None                                 # float
        self.south = None                                 # float
        self.west = None                                  # float


class DataExtentTemporal(object):
    """A concrete class within the cim v1 type system.

    A data object temporal extent represents the temporal coverage associated with a data object.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtentTemporal, self).__init__()

        self.begin = None                                 # datetime.date
        self.end = None                                   # datetime.date
        self.time_interval = None                         # data.DataExtentTimeInterval


class DataExtentTimeInterval(object):
    """A concrete class within the cim v1 type system.

    A data object temporal extent represents the temporal coverage associated with a data object.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtentTimeInterval, self).__init__()

        self.factor = None                                # int
        self.radix = None                                 # int
        self.unit = None                                  # str


class DataHierarchyLevel(object):
    """A concrete class within the cim v1 type system.

    The type of data object that is grouped together into a particular hierarchy.  Currently, this is made up of terms describing how the Met Office splits up archived data and how THREDDS categorises variables.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataHierarchyLevel, self).__init__()

        self.is_open = None                               # bool
        self.name = None                                  # data.DataHierarchyType
        self.value = None                                 # str


class DataObject(shared.DataSource):
    """A concrete class within the cim v1 type system.

    A DataObject describes a unit of data.  DataObjects can be grouped hierarchically.  The attributes hierarchyLevelName and hierarchyLevelValue describe how objects are grouped.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataObject, self).__init__()

        self.acronym = None                               # str
        self.child_object = []                            # data.DataObject
        self.citations = []                               # shared.Citation
        self.content = []                                 # data.DataContent
        self.data_status = None                           # data.DataStatusType
        self.description = None                           # str
        self.distribution = None                          # data.DataDistribution
        self.extent = None                                # data.DataExtent
        self.geometry_model = None                        # str
        self.hierarchy_level = None                       # data.DataHierarchyLevel
        self.keyword = None                               # str
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.parent_object = None                         # data.DataObject
        self.parent_object_reference = None               # shared.DocReference
        self.properties = []                              # data.DataProperty
        self.purpose = None                               # str
        self.restriction = []                             # data.DataRestriction
        self.source_simulation = None                     # str
        self.storage = []                                 # data.DataStorage


class DataProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    A property of a DataObject. Currently this is intended to be used to record CF specific information (like packing, scaling, etc.) for OASIS4.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataProperty, self).__init__()

        self.description = None                           # str


class DataRestriction(object):
    """A concrete class within the cim v1 type system.

    An access or use restriction on some element of the DataObject's actual data.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataRestriction, self).__init__()

        self.license = None                               # shared.License
        self.restriction = None                           # str
        self.scope = None                                 # str


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
        self.location = None                              # str
        self.modification_date = None                     # datetime.datetime
        self.size = None                                  # int


class DataTopic(object):
    """A concrete class within the cim v1 type system.

    Describes the content  of a data object; the variable's name, units, etc.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataTopic, self).__init__()

        self.description = None                           # str
        self.name = None                                  # str
        self.unit = None                                  # str


class DataStorageDb(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a database file.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataStorageDb, self).__init__()

        self.access_string = None                         # str
        self.name = None                                  # str
        self.owner = None                                 # str
        self.table = None                                 # str


class DataStorageFile(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a single file.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataStorageFile, self).__init__()

        self.file_name = None                             # str
        self.file_system = None                           # str
        self.path = None                                  # str


class DataStorageIp(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a database file.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataStorageIp, self).__init__()

        self.fileName = None                              # str
        self.host = None                                  # str
        self.path = None                                  # str
        self.protocol = None                              # str


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


