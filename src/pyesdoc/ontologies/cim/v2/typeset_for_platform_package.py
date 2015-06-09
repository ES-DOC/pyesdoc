# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_platform_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.platform package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-05 14:48:44.254779.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class StoragePool(object):
    """A concrete class within the cim v2 type system.

    Homogeneous storage pool on a computing machine.

    """
    def __init__(self):
        """Constructor.

        """
        super(StoragePool, self).__init__()

        self.vendor = None                                # linked_to(shared.Party)
        self.type = None                                  # platform.StorageSystems
        self.description = None                           # shared.CimText
        self.volume_available = None                      # platform.StorageVolume
        self.name = None                                  # str


class ComputePool(object):
    """A concrete class within the cim v2 type system.

    Homogeneous pool of nodes within a computing machine.

    """
    def __init__(self):
        """Constructor.

        """
        super(ComputePool, self).__init__()

        self.operating_system = None                      # str
        self.accelerators_per_node = None                 # int
        self.name = None                                  # str
        self.model_number = None                          # str
        self.interconnect = None                          # str
        self.accelerator_type = None                      # str
        self.compute_cores_per_node = None                # int
        self.number_of_nodes = None                       # int
        self.memory_per_node = None                       # platform.StorageVolume
        self.CPU_type = None                              # str
        self.description = None                           # shared.CimText


class Performance(object):
    """A concrete class within the cim v2 type system.

    Describes the properties of a performance of a configured model on a machine.

    """
    def __init__(self):
        """Constructor.

        """
        super(Performance, self).__init__()

        self.coupler_load = None                          # float
        self.subcomponent_performance = None              # platform.ComponentPerformance
        self.name = None                                  # str
        self.io_load = None                               # float
        self.compiler = None                              # str
        self.model = None                                 # linked_to(software.ConfiguredModel)
        self.asypd = None                                 # float
        self.platform = None                              # linked_to(platform.Machine)
        self.meta = shared.Meta()                         # shared.Meta
        self.sypd = None                                  # float
        self.chsy = None                                  # float
        self.load_imbalance = None                        # float
        self.memory_bloat = None                          # float
        self.total_nodes_used = None                      # int


class Partition(object):
    """A concrete class within the cim v2 type system.

    A description of a partition in a computing machine.

    """
    def __init__(self):
        """Constructor.

        """
        super(Partition, self).__init__()

        self.storage_pool = []                            # platform.StoragePool
        self.institution = None                           # linked_to(shared.Party)
        self.name = None                                  # str
        self.model_number = None                          # str
        self.when_used = None                             # time.TimePeriod
        self.partition = []                               # platform.Partition
        self.compute_pool = []                            # platform.ComputePool
        self.description = None                           # shared.CimText
        self.online_documentation = []                    # shared.OnlineResource
        self.vendor = None                                # linked_to(shared.Party)


class ComponentPerformance(object):
    """A concrete class within the cim v2 type system.

    Describes the simulation rate of a component in seconds per model day.

    """
    def __init__(self):
        """Constructor.

        """
        super(ComponentPerformance, self).__init__()

        self.cores_used = None                            # int
        self.speed = None                                 # float
        self.nodes_used = None                            # int
        self.component = None                             # software.SoftwareComponent
        self.component_name = None                        # str


class StorageVolume(object):
    """A concrete class within the cim v2 type system.

    Volume and units.

    """
    def __init__(self):
        """Constructor.

        """
        super(StorageVolume, self).__init__()

        self.units = None                                 # platform.VolumeUnits
        self.volume = None                                # int


class Machine(Partition):
    """A concrete class within the cim v2 type system.

    A description of an independent computing machine.

    """
    def __init__(self):
        """Constructor.

        """
        super(Machine, self).__init__()

        self.meta = shared.Meta()                         # shared.Meta


class StorageSystems(object):
    """An enumeration within the cim v2 type system.

    Controlled vocabulary for storage  types (including filesystems).
    """

    pass


class VolumeUnits(object):
    """An enumeration within the cim v2 type system.

    Appropriate storage volume units.
    """

    pass


