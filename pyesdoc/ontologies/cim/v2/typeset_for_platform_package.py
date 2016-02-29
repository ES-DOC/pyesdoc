# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_platform_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.platform package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

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

        self.component = None                             # software.SoftwareComponent (0.1)
        self.component_name = None                        # unicode (1.1)
        self.cores_used = None                            # int (0.1)
        self.nodes_used = None                            # int (0.1)
        self.speed = None                                 # float (1.1)


class ComputePool(object):
    """A concrete class within the cim v2 type system.

    Homogeneous pool of nodes within a computing machine.

    """
    def __init__(self):
        """Constructor.

        """
        super(ComputePool, self).__init__()

        self.accelerator_type = None                      # unicode (0.1)
        self.accelerators_per_node = None                 # int (0.1)
        self.compute_cores_per_node = None                # int (0.1)
        self.cpu_type = None                              # unicode (0.1)
        self.description = None                           # unicode (0.1)
        self.interconnect = None                          # unicode (0.1)
        self.memory_per_node = None                       # platform.StorageVolume (0.1)
        self.model_number = None                          # unicode (0.1)
        self.name = None                                  # unicode (0.1)
        self.number_of_nodes = None                       # int (0.1)
        self.operating_system = None                      # unicode (0.1)


    @property
    def total_cores(self):
	    """Returns a computed property.

	    """
	    return self.compute_cores_per_node * self.number_of_nodes


    @property
    def total_memory(self):
	    """Returns a computed property.

	    """
	    return self.memory_per_node * self.number_of_nodes


class Partition(object):
    """A concrete class within the cim v2 type system.

    A major partition (component) of a computing system (aka machine).

    """
    def __init__(self):
        """Constructor.

        """
        super(Partition, self).__init__()

        self.compute_pools = []                           # platform.ComputePool (1.N)
        self.description = None                           # unicode (0.1)
        self.institution = None                           # shared.Party (1.1)
        self.model_number = None                          # unicode (0.1)
        self.name = None                                  # unicode (1.1)
        self.online_documentation = []                    # shared.OnlineResource (0.N)
        self.partition = []                               # platform.Partition (0.N)
        self.storage_pools = []                           # platform.StoragePool (0.N)
        self.vendor = None                                # shared.Party (0.1)
        self.when_used = None                             # shared.TimePeriod (0.1)


class Performance(object):
    """A concrete class within the cim v2 type system.

    Describes the properties of a performance of a configured model on a particular system/machine.

    """
    def __init__(self):
        """Constructor.

        """
        super(Performance, self).__init__()

        self.asypd = None                                 # float (0.1)
        self.chsy = None                                  # float (0.1)
        self.compiler = None                              # unicode (0.1)
        self.coupler_load = None                          # float (0.1)
        self.io_load = None                               # float (0.1)
        self.load_imbalance = None                        # float (0.1)
        self.memory_bloat = None                          # float (0.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.model = None                                 # science.Model (1.1)
        self.name = None                                  # unicode (0.1)
        self.platform = None                              # platform.Machine (1.1)
        self.subcomponent_performance = None              # platform.ComponentPerformance (0.1)
        self.sypd = None                                  # float (0.1)
        self.total_nodes_used = None                      # int (0.1)


class StoragePool(object):
    """A concrete class within the cim v2 type system.

    Homogeneous storage pool on a computing machine.

    """
    def __init__(self):
        """Constructor.

        """
        super(StoragePool, self).__init__()

        self.description = None                           # unicode (0.1)
        self.name = None                                  # unicode (1.1)
        self.type = None                                  # platform.StorageSystems (0.1)
        self.vendor = None                                # shared.Party (0.1)
        self.volume_available = None                      # platform.StorageVolume (1.1)


class StorageVolume(object):
    """A concrete class within the cim v2 type system.

    Volume and units.

    """
    def __init__(self):
        """Constructor.

        """
        super(StorageVolume, self).__init__()

        self.units = None                                 # platform.VolumeUnits (1.1)
        self.volume = None                                # int (1.1)


class Machine(Partition):
    """A concrete class within the cim v2 type system.

    A computer/system/platform/machine which is used for simulation.

    """
    def __init__(self):
        """Constructor.

        """
        super(Machine, self).__init__()

        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)


class StorageSystems(object):
    """An enumeration within the cim v2 type system.

    Controlled vocabulary for storage  types (including filesystems).
    """
    is_open = False
    members = [
        "GPFS",
        "Lustre",
        "NFS",
        "Other Disk",
        "Panasas",
        "Tape - Castor",
        "Tape - MARS",
        "Tape - MASS",
        "Tape - Other",
        "Unknown",
        "isilon"
        ]


class VolumeUnits(object):
    """An enumeration within the cim v2 type system.

    Appropriate storage volume units.
    """
    is_open = False
    members = [
        "EB",
        "EiB",
        "GB",
        "PB",
        "PiB",
        "TB",
        "TiB"
        ]


