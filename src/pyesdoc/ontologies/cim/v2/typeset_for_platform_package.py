# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_platform_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.platform package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-03 11:24:48.591640.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class ComponentPerformance(object):
    """A concrete class within the cim v2 type system.

    Describes the simulation rate of a component in seconds per model day.

    """
    def __init__(self):
        """Constructor.

        """
        super(ComponentPerformance, self).__init__()

        self.component = None                             # software.SoftwareComponent
        self.component_name = None                        # str
        self.cores_used = None                            # int
        self.nodes_used = None                            # int
        self.speed = None                                 # float


class ComputePool(object):
    """A concrete class within the cim v2 type system.

    Homogeneous pool of nodes within a computing machine.

    """
    def __init__(self):
        """Constructor.

        """
        super(ComputePool, self).__init__()

        self.CPU_type = None                              # str
        self.accelerator_type = None                      # str
        self.accelerators_per_node = None                 # int
        self.compute_cores_per_node = None                # int
        self.description = None                           # shared.CimText
        self.interconnect = None                          # str
        self.memory_per_node = None                       # platform.StorageVolume
        self.model_number = None                          # str
        self.name = None                                  # str
        self.number_of_nodes = None                       # int
        self.operating_system = None                      # str


class Partition(object):
    """A concrete class within the cim v2 type system.

    A description of a partition in a computing machine.

    """
    def __init__(self):
        """Constructor.

        """
        super(Partition, self).__init__()

        self.compute_pool = []                            # platform.ComputePool
        self.description = None                           # shared.CimText
        self.institution = None                           # linked_to(shared.Party)
        self.model_number = None                          # str
        self.name = None                                  # str
        self.online_documentation = []                    # shared.OnlineResource
        self.partition = []                               # platform.Partition
        self.storage_pool = []                            # platform.StoragePool
        self.vendor = None                                # linked_to(shared.Party)
        self.when_used = None                             # time.TimePeriod


class Performance(object):
    """A concrete class within the cim v2 type system.

    Describes the properties of a performance of a configured model on a machine.

    """
    def __init__(self):
        """Constructor.

        """
        super(Performance, self).__init__()

        self.asypd = None                                 # float
        self.chsy = None                                  # float
        self.compiler = None                              # str
        self.coupler_load = None                          # float
        self.io_load = None                               # float
        self.load_imbalance = None                        # float
        self.memory_bloat = None                          # float
        self.meta = shared.Meta()                         # shared.Meta
        self.model = None                                 # linked_to(software.ConfiguredModel)
        self.name = None                                  # str
        self.platform = None                              # linked_to(platform.Machine)
        self.subcomponent_performance = None              # platform.ComponentPerformance
        self.sypd = None                                  # float
        self.total_nodes_used = None                      # int


class StoragePool(object):
    """A concrete class within the cim v2 type system.

    Homogeneous storage pool on a computing machine.

    """
    def __init__(self):
        """Constructor.

        """
        super(StoragePool, self).__init__()

        self.description = None                           # shared.CimText
        self.name = None                                  # str
        self.type = None                                  # platform.StorageSystems
        self.vendor = None                                # linked_to(shared.Party)
        self.volume_available = None                      # platform.StorageVolume


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


