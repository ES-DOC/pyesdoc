# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_for_data_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.data package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-01 16:50:10.358639.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class DataContent(shared.DataSource):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of data_content class.

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

    Creates and returns instance of data_distribution class.

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

    Creates and returns instance of data_extent class.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataExtent, self).__init__()

        self.geographical = None                          # data.DataExtentGeographical
        self.temporal = None                              # data.DataExtentTemporal


class DataExtentGeographical(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of data_extent_geographical class.

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

    Creates and returns instance of data_extent_temporal class.

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

    Creates and returns instance of data_extent_time_interval class.

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

    Creates and returns instance of data_hierarchy_level class.

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

    Creates and returns instance of data_object class.

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

    Creates and returns instance of data_property class.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataProperty, self).__init__()

        self.description = None                           # str


class DataRestriction(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of data_restriction class.

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

    Creates and returns instance of data_storage class.

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

    Creates and returns instance of data_topic class.

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

    Creates and returns instance of data_storage_db class.

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

    Creates and returns instance of data_storage_file class.

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

    Creates and returns instance of data_storage_ip class.

    """
    def __init__(self):
        """Constructor.

        """
        super(DataStorageIp, self).__init__()

        self.file_name = None                             # str
        self.host = None                                  # str
        self.path = None                                  # str
        self.protocol = None                              # str


class DataHierarchyType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of data_status_type enum.
    """

    pass


class DataStatusType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of data_status_type enum.
    """

    pass


