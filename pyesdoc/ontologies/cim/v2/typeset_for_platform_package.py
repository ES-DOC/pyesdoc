"""
.. module:: cim.v2.typeset_for_platform_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.platform package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class ComputePool(object):
    """A concrete class within the cim v2 type system.

    Homogeneous pool of nodes within a computing machine.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ComputePool, self).__init__()

        self.accelerator_type = None                      # unicode (0.1)
        self.accelerators_per_node = None                 # int (0.1)
        self.clock_cycle_concurrency = None               # int (0.1)
        self.clock_speed = None                           # shared.Numeric (0.1)
        self.compute_cores_per_node = None                # int (0.1)
        self.cpu_type = None                              # unicode (0.1)
        self.description = None                           # unicode (0.1)
        self.memory_per_node = None                       # shared.Numeric (0.1)
        self.model_number = None                          # unicode (0.1)
        self.name = None                                  # unicode (0.1)
        self.network_cards_per_node = []                  # platform.Nic (0.N)
        self.number_of_nodes = None                       # int (0.1)
        self.vendor = None                                # shared.Party (0.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{} [{}]".format(self.name, self.number_of_nodes)


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


class Interconnect(object):
    """A concrete class within the cim v2 type system.

    The interconnect used within a machine to join nodes together.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Interconnect, self).__init__()

        self.description = None                           # unicode (0.1)
        self.name = None                                  # unicode (0.1)
        self.topology = None                              # unicode (0.1)
        self.vendor = None                                # shared.Party (0.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.name)


class Nic(object):
    """A concrete class within the cim v2 type system.

    Network Interface Card.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Nic, self).__init__()

        self.bandwidth = None                             # shared.Numeric (1.1)
        self.name = None                                  # unicode (1.1)
        self.vendor = None                                # shared.Party (0.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.name)


class Partition(object):
    """A concrete class within the cim v2 type system.

    A major partition (component) of a computing system (aka
    machine).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Partition, self).__init__()

        self.compute_pools = []                           # platform.ComputePool (1.N)
        self.description = None                           # unicode (0.1)
        self.institution = None                           # shared.Party (1.1)
        self.interconnect = None                          # platform.Interconnect (0.1)
        self.model_number = None                          # unicode (0.1)
        self.name = None                                  # unicode (1.1)
        self.online_documentation = []                    # shared.OnlineResource (0.N)
        self.operating_system = None                      # unicode (0.1)
        self.partition = []                               # platform.Partition (0.N)
        self.storage_pools = []                           # platform.StoragePool (0.N)
        self.vendor = None                                # shared.Party (0.1)
        self.when_available = None                        # time.TimePeriod (0.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.name)


class Performance(object):
    """A concrete class within the cim v2 type system.

    Describes the properties of a performance of a configured model
    on a particular system/machine.

    Based on "CPMIP: Measurements of Real Computational Performance of
    Earth System Models" (Balaji et. al. 2016,
    doi:10.5194/gmd-2016-197).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Performance, self).__init__()

        self.actual_simulated_years_per_day = None        # float (0.1)
        self.compiler = None                              # unicode (0.1)
        self.complexity = None                            # int (0.1)
        self.core_hours_per_simulated_year = None         # float (0.1)
        self.further_detail = None                        # platform.PerformanceDetail (0.1)
        self.joules_per_simulated_year = None             # float (0.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.model = None                                 # science.Model (1.1)
        self.name = None                                  # unicode (0.1)
        self.parallelisation = None                       # float (0.1)
        self.platform = None                              # platform.Machine (1.1)
        self.resolution = None                            # int (0.1)
        self.simulated_years_per_day = None               # float (0.1)
        self.subcomponent_performance = []                # platform.Performance (0.N)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{} (sypd:{})".format(self.name, self.simulated_years_per_day)


class PerformanceDetail(object):
    """A concrete class within the cim v2 type system.

    Information about how the various components of performance were
    related.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(PerformanceDetail, self).__init__()

        self.coupling_cost = None                         # float (0.1)
        self.data_intensity = None                        # float (0.1)
        self.data_output_cost = None                      # float (0.1)
        self.memory_bloat = None                          # float (0.1)


class ProjectCost(object):
    """A concrete class within the cim v2 type system.

    Cost of an experiment or project on a particular platform.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ProjectCost, self).__init__()

        self.activity = None                              # activity.Activity (1.1)
        self.actual_years = None                          # int (0.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.peak_data = None                             # shared.Numeric (0.1)
        self.platform = None                              # platform.Machine (1.1)
        self.total_core_hours = None                      # int (0.1)
        self.total_energy_cost = None                     # float (0.1)
        self.useful_core_hours = None                     # int (0.1)
        self.useful_data = None                           # shared.Numeric (0.1)
        self.useful_years = None                          # int (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "Production: {}Y, {}".format(self.useful_years, self.useful_data)


class StoragePool(object):
    """A concrete class within the cim v2 type system.

    Homogeneous storage pool on a computing machine.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(StoragePool, self).__init__()

        self.description = None                           # unicode (0.1)
        self.file_system_sizes = []                       # shared.Numeric (1.N)
        self.name = None                                  # unicode (1.1)
        self.type = None                                  # platform.StorageSystems (0.1)
        self.vendor = None                                # shared.Party (0.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{} {}".format(self.name, self.file_system_sizes)


class Machine(Partition):
    """A concrete class within the cim v2 type system.

    A computer/system/platform/machine which is used for
    simulation.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Machine, self).__init__()

        self.linpack_performance = None                   # shared.Numeric (0.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.peak_performance = None                      # shared.Numeric (0.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.name)


class StorageSystems(object):
    """An enumeration within the cim v2 type system.

    Controlled vocabulary for storage types (including
    filesystems).
    """
    is_open = True
    members = [
        "Lustre",
        "GPFS",
        "isilon",
        "NFS",
        "S3",
        "PanFS",
        "Other Disk",
        "Tape - MARS",
        "Tape - MASS",
        "Tape - Castor",
        "Tape - Other"
        ]
    descriptions = [
        "Lustre parallel file system",
        "IBM GPFS (also known as IBM Spectral Scale",
        "The EMC scaleout NAS solution",
        "Generic Network File System",
        "Object file system exposing the AWS S3 interface",
        "Panasas Parallel File system",
        "Other disk based file system",
        "Tape storage system using ECMWF MARS",
        "Tape storage system using Met Office MASS",
        "Tape storage sytsem using CERN Castor",
        "Other tape based system"
        ]


