"""
.. module:: cim.v1.typeset_for_data_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.data package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class DataContent(shared.DataSource):
    """A concrete class within the cim v1 type system.

    The contents of the data object; like ISO: MD_ContentInformation.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DataContent, self).__init__()

        self.aggregation = None                           # unicode (0.1)
        self.frequency = None                             # unicode (0.1)
        self.topic = None                                 # data.DataTopic (1.1)


class DataDistribution(object):
    """A concrete class within the cim v1 type system.

    Describes how a DataObject is distributed.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DataDistribution, self).__init__()

        self.access = None                                # unicode (0.1)
        self.fee = None                                   # unicode (0.1)
        self.format = None                                # unicode (0.1)
        self.responsible_party = None                     # shared.ResponsibleParty (0.1)


class DataExtent(object):
    """A concrete class within the cim v1 type system.

    A data object extent represents the geographical and temporal coverage associated with a data object.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DataExtent, self).__init__()

        self.geographical = None                          # data.DataExtentGeographical (1.1)
        self.temporal = None                              # data.DataExtentTemporal (1.1)


class DataExtentGeographical(object):
    """A concrete class within the cim v1 type system.

    A data object geographical extent represents the geographical coverage associated with a data object.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DataExtentGeographical, self).__init__()

        self.east = None                                  # float (0.1)
        self.north = None                                 # float (0.1)
        self.south = None                                 # float (0.1)
        self.west = None                                  # float (0.1)


class DataExtentTemporal(object):
    """A concrete class within the cim v1 type system.

    A data object temporal extent represents the temporal coverage associated with a data object.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DataExtentTemporal, self).__init__()

        self.begin = None                                 # datetime.date (0.1)
        self.end = None                                   # datetime.date (0.1)
        self.time_interval = None                         # data.DataExtentTimeInterval (0.1)


class DataExtentTimeInterval(object):
    """A concrete class within the cim v1 type system.

    A data object temporal extent represents the temporal coverage associated with a data object.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DataExtentTimeInterval, self).__init__()

        self.factor = None                                # int (0.1)
        self.radix = None                                 # int (0.1)
        self.unit = None                                  # unicode (0.1)


class DataHierarchyLevel(object):
    """A concrete class within the cim v1 type system.

    The type of data object that is grouped together into a particular hierarchy.  Currently, this is made up of terms describing how the Met Office splits up archived data and how THREDDS categorises variables.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DataHierarchyLevel, self).__init__()

        self.is_open = None                               # bool (0.1)
        self.name = None                                  # data.DataHierarchyType (0.1)
        self.value = None                                 # unicode (0.1)


class DataObject(shared.DataSource):
    """A concrete class within the cim v1 type system.

    A DataObject describes a unit of data.  DataObjects can be grouped hierarchically.  The attributes hierarchyLevelName and hierarchyLevelValue describe how objects are grouped.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DataObject, self).__init__()

        self.acronym = None                               # unicode (0.1)
        self.child_object = []                            # data.DataObject (0.N)
        self.citations = []                               # shared.Citation (0.N)
        self.content = []                                 # data.DataContent (0.N)
        self.data_status = None                           # data.DataStatusType (0.1)
        self.description = None                           # unicode (0.1)
        self.distribution = None                          # data.DataDistribution (0.1)
        self.extent = None                                # data.DataExtent (0.1)
        self.geometry_model = None                        # unicode (0.1)
        self.hierarchy_level = None                       # data.DataHierarchyLevel (0.1)
        self.keyword = None                               # unicode (0.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.parent_object = None                         # data.DataObject (0.1)
        self.properties = []                              # data.DataProperty (0.N)
        self.purpose = None                               # unicode (0.1)
        self.restriction = []                             # data.DataRestriction (0.N)
        self.source_simulation = None                     # unicode (0.1)
        self.storage = []                                 # data.DataStorage (0.N)


class DataProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    A property of a DataObject. Currently this is intended to be used to record CF specific information (like packing, scaling, etc.) for OASIS4.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DataProperty, self).__init__()

        self.description = None                           # unicode (0.1)


class DataRestriction(object):
    """A concrete class within the cim v1 type system.

    An access or use restriction on some element of the DataObject actual data.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DataRestriction, self).__init__()

        self.license = None                               # shared.License (0.1)
        self.restriction = None                           # unicode (0.1)
        self.scope = None                                 # unicode (0.1)


class DataStorage(object):
    """An abstract class within the cim v1 type system.

    Describes the method that the DataObject is stored. An abstract class with specific child classes for each supported method.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Instance constructor.

        """
        super(DataStorage, self).__init__()

        self.format = None                                # unicode (0.1)
        self.location = None                              # unicode (0.1)
        self.modification_date = None                     # datetime.datetime (0.1)
        self.size = None                                  # int (0.1)


class DataTopic(object):
    """A concrete class within the cim v1 type system.

    Describes the content of a data object: the variable name, units, etc.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DataTopic, self).__init__()

        self.description = None                           # unicode (0.1)
        self.name = None                                  # unicode (0.1)
        self.unit = None                                  # unicode (0.1)


class DataStorageDb(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a database file.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DataStorageDb, self).__init__()

        self.access_string = None                         # unicode (0.1)
        self.name = None                                  # unicode (0.1)
        self.owner = None                                 # unicode (0.1)
        self.table = None                                 # unicode (0.1)


class DataStorageFile(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a single file.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DataStorageFile, self).__init__()

        self.file_name = None                             # unicode (0.1)
        self.file_system = None                           # unicode (0.1)
        self.path = None                                  # unicode (0.1)


class DataStorageIp(DataStorage):
    """A concrete class within the cim v1 type system.

    Contains attributes to describe a DataObject stored as a database file.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DataStorageIp, self).__init__()

        self.file_name = None                             # unicode (0.1)
        self.host = None                                  # unicode (0.1)
        self.path = None                                  # unicode (0.1)
        self.protocol = None                              # unicode (0.1)


class DataHierarchyType(object):
    """An enumeration within the cim v1 type system.

    Enumerates the level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.
    """
    is_open = True
    members = []
    descriptions = []


class DataStatusType(object):
    """An enumeration within the cim v1 type system.

    Enumerates status of a data object.
    """
    is_open = False
    members = [
        "complete",
        "metadataOnly",
        "continuouslySupplemented"
        ]
    descriptions = [
        "This DataObject is complete.",
        "This DataObject is incomplete - it is described in metadata but the actual data has not yet been linked to it.",
        "This DataObject's actual data is continuously updated."
        ]


