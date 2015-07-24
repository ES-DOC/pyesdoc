# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_platform_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.platform package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-07-24 23:58:29.533156.

"""
import abc
import datetime
import uuid

import typeset_for_software_package as software
import typeset_for_shared_package as shared
import typeset_for_platform_package as platform



class ComponentPerformance(object):
    """A concrete class within the cim v2 type system.

    Describes the simulation rate of a component in seconds per model day

    """
    def __init__(self):
        """Constructor.

        """
        super(ComponentPerformance, self).__init__()

        self.cores_used = None                            # int
        self.speed = None                                 # float
        self.component = None                             # software.SoftwareComponent
        self.nodes_used = None                            # int
        self.component_name = None                        # str


class Partition(object):
    """A concrete class within the cim v2 type system.

    A major partition (component) of a computing system (aka machine)

    """
    def __init__(self):
        """Constructor.

        """
        super(Partition, self).__init__()

        self.vendor = None                                # shared.Party
        self.storage_pools = []                           # platform.StoragePool
        self.name = None                                  # str
        self.online_documentation = []                    # shared.OnlineResource
        self.institution = None                           # shared.Party
        self.compute_pools = []                           # platform.ComputePool
        self.description = None                           # shared.Cimtext
        self.when_used = None                             # shared.TimePeriod
        self.model_number = None                          # str
        self.partition = []                               # platform.Partition


class ComputePool(object):
    """A concrete class within the cim v2 type system.

    Homogeneous pool of nodes within a computing machine.

    """
    def __init__(self):
        """Constructor.

        """
        super(ComputePool, self).__init__()

        self.operating_system = None                      # str
        self.model_number = None                          # str
        self.accelerators_per_node = None                 # int
        self.memory_per_node = None                       # platform.StorageVolume
        self.compute_cores_per_node = None                # int
        self.description = None                           # shared.Cimtext
        self.number_of_nodes = None                       # int
        self.accelerator_type = None                      # str
        self.interconnect = None                          # str
        self.cpu_type = None                              # str
        self.name = None                                  # str


class StorageVolume(object):
    """A concrete class within the cim v2 type system.

    Volume and units

    """
    def __init__(self):
        """Constructor.

        """
        super(StorageVolume, self).__init__()

        self.units = None                                 # platform.VolumeUnits
        self.volume = None                                # int


class StoragePool(object):
    """A concrete class within the cim v2 type system.

    Homogeneous storage pool on a computing machine

    """
    def __init__(self):
        """Constructor.

        """
        super(StoragePool, self).__init__()

        self.description = None                           # shared.Cimtext
        self.volume_available = None                      # platform.StorageVolume
        self.vendor = None                                # shared.Party
        self.name = None                                  # str
        self.type = None                                  # platform.StorageSystems


class Performance(object):
    """A concrete class within the cim v2 type system.

    Describes the properties of a performance of a configured model on a particular system/machine

    """
    def __init__(self):
        """Constructor.

        """
        super(Performance, self).__init__()

        self.meta = shared.Meta()                         # shared.Meta
        self.chsy = None                                  # float
        self.compiler = None                              # str
        self.memory_bloat = None                          # float
        self.asypd = None                                 # float
        self.model = None                                 # software.Model
        self.sypd = None                                  # float
        self.subcomponent_performance = None              # platform.ComponentPerformance
        self.load_imbalance = None                        # float
        self.platform = None                              # platform.Machine
        self.coupler_load = None                          # float
        self.io_load = None                               # float
        self.total_nodes_used = None                      # int
        self.name = None                                  # str


class Machine(Partition):
    """A concrete class within the cim v2 type system.

    A computer/system/platform/machine which is used for simulation.

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


