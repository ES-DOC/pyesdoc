# -*- coding: utf-8 -*-

"""
.. module:: platform_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.
   applying to the description of computers and the
   performance of code running on those computers.
"""


def compute_pool():
    """Homogeneous pool of nodes within a computing machine."""
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "pstr": ("{} [{}]", ("name", "number_of_nodes")),
        "properties": [
            ("accelerator_type", "str", "0.1", "Type of accelerator."),
            (
                "accelerators_per_node",
                "int",
                "0.1",
                "Number of accelerator units on a node.",
            ),
            (
                "clock_cycle_concurrency",
                "int",
                "0.1",
                "The number of operations which can be carried out concurrently in a single clock cycle of a single core. E.g. 4.",
            ),
            (
                "clock_speed",
                "shared.numeric",
                "0.1",
                "The clock speed of a single core, in units of GHz. E.g. 3.6.",
            ),
            (
                "compute_cores_per_node",
                "int",
                "0.1",
                "Number of CPU cores per node.",
            ),
            ("cpu_type", "str", "0.1", "CPU type."),
            ("description", "str", "0.1", "Textural description of pool."),
            ("memory_per_node", "shared.numeric", "0.1", "Memory per node."),
            ("model_number", "str", "0.1", "Model/Board number/type."),
            ("name", "str", "0.1", "Name of compute pool within a machine."),
            ("number_of_nodes", "int", "0.1", "Number of nodes."),
            (
                "vendor",
                "linked_to(shared.party)",
                "0.1",
                "Supplier of compute hardware in this pool",
            ),
            (
                "network_cards_per_node",
                "platform.nic",
                "0.N",
                "Available network interfaces on node",
            ),
        ],
        "derived": [
            ("total_cores", "compute_cores_per_node * number_of_nodes"),
            ("total_memory", "memory_per_node * number_of_nodes"),
        ],
    }


def interconnect():
    """The interconnect used within a machine to join nodes together."""
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "pstr": ("{}", ("name",)),
        "properties": [
            ("name", "str", "0.1", "Name of interconnnect."),
            ("topology", "str", "0.1", "Interconnect topology"),
            (
                "description",
                "str",
                "0.1",
                "Technical description of interconnect layout",
            ),
            (
                "vendor",
                "linked_to(shared.party)",
                "0.1",
                "Supplier of the interconnect",
            ),
        ],
    }


def nic():
    """Network Interface Card."""
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "pstr": ("{}", ("name",)),
        "properties": [
            ("name", "str", "1.1", "Name of interface card"),
            (
                "vendor",
                "linked_to(shared.party)",
                "0.1",
                "Vendor of network card",
            ),
            ("bandwidth", "shared.numeric", "1.1", "Bandwidth to network"),
        ],
    }


def machine():
    """A computer/system/platform/machine which is used for
    simulation."""
    return {
        "type": "class",
        "base": "platform.partition",
        "is_abstract": False,
        "pstr": ("{}", ("name",)),
        "is_document": True,
        "properties": [
            (
                "peak_performance",
                "shared.numeric",
                "0.1",
                "Total peak performance (RPeak in Top500 lingo)",
            ),
            (
                "linpack_performance",
                "shared.numeric",
                "0.1",
                "Linpack performance (RMax in Top500 lingo)",
            ),
        ],
    }


def partition():
    """A major partition (component) of a computing system (aka
    machine)."""
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "pstr": ("{}", ("name",)),
        "properties": [
            (
                "compute_pools",
                "platform.compute_pool",
                "1.N",
                "Layout of compute nodes.",
            ),
            (
                "interconnect",
                "platform.interconnect",
                "0.1",
                "Interconnect used.",
            ),
            ("description", "str", "0.1", "Textural description of machine."),
            (
                "institution",
                "linked_to(shared.party)",
                "1.1",
                "Institutional location.",
            ),
            (
                "model_number",
                "str",
                "0.1",
                "Vendor's model number/name - if it exists.",
            ),
            ("name", "str", "1.1", "Name of partition (or machine)."),
            (
                "online_documentation",
                "shared.online_resource",
                "0.N",
                "Links to documentation.",
            ),
            ("operating_system", "str", "0.1", "Operating system."),
            (
                "partition",
                "platform.partition",
                "0.N",
                "If machine is partitioned, treat subpartitions as machines.",
            ),
            (
                "storage_pools",
                "platform.storage_pool",
                "0.N",
                "Storage resource available.",
            ),
            (
                "vendor",
                "linked_to(shared.party)",
                "0.1",
                "The system integrator or vendor.",
            ),
            (
                "when_available",
                "time.time_period",
                "0.1",
                "If no longer in use, the time period it was in use.",
            ),
        ],
    }


def performance():
    """Describes the properties of a performance of a configured model
    on a particular system/machine.

    Based on "CPMIP: Measurements of Real Computational Performance of
    Earth System Models" (Balaji et. al. 2016,
    doi:10.5194/gmd-2016-197).

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "pstr": ("{} (sypd:{})", ("name", "simulated_years_per_day")),
        "is_document": True,
        "properties": [
            (
                "name",
                "str",
                "0.1",
                "Name for performance (experiment/test/whatever).",
            ),
            # CPMIP model and platform
            (
                "model",
                "linked_to(science.model)",
                "1.1",
                "Model for which performance was tested.",
            ),
            (
                "resolution",
                "int",
                "0.1",
                "Resolution measured as the number of gridpoints (or more generally, spatial degrees of freedom) NX x NY x NZ per component with an independent discretization.",
            ),
            (
                "complexity",
                "int",
                "0.1",
                "Complexity measured as the number of prognostic variables per component with an independent discretization.",
            ),
            (
                "platform",
                "linked_to(platform.machine)",
                "1.1",
                "Platform on which performance was tested.",
            ),
            ("compiler", "str", "0.1", "Compiler used for performance test."),
            # CPMIP computational cost
            (
                "simulated_years_per_day",
                "float",
                "0.1",
                "Simulated years per day (SYPD) in a 24h period on the given platform.",
            ),
            (
                "actual_simulated_years_per_day",
                "float",
                "0.1",
                "Actual simulated years per day (ASYPD) in a 24h period on the given platform obtained from a typical long-running simulation with the model. Inclusive of system interruptions, queue wait time, or issues with the model workflow, etc.",
            ),
            (
                "core_hours_per_simulated_year",
                "float",
                "0.1",
                "Core-hours per simulated year (CHSY). This is measured as the product of the model runtime for 1 SY, and the numbers of cores allocated. Note that if allocations are done on a node basis then all cores on a node are charged against the allocation, regardless of whether or not they are used.",
            ),
            (
                "joules_per_simulated_year",
                "float",
                "0.1",
                "The energy cost of a simulation, measured in joules per simulated year (JPSY). Given the energy E in joules consumed over a budgeting interval T (generally 1 month or 1 year, in units of hours), JPSY=CHSY*E*T/NP.",
            ),
            (
                "parallelisation",
                "float",
                "0.1",
                "Total number of cores (NP) allocated for the run, regardless of whether or not all cores were used all of the time.",
            ),
            (
                "further_detail",
                "platform.performance_detail",
                "0.1",
                "Set of additional information related to coupling, memory "
                "and I/O.",
            ),
            # Subcomponent performance
            (
                "subcomponent_performance",
                "linked_to(platform.performance)",
                "0.N",
                "Describes the performance of each subcomponent.",
            ),
        ],
    }


def performance_detail():
    """Information about how the various components of performance were
    related."""
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "is_document": False,
        "properties": [
            # CPMIP coupling, memory, I/O
            (
                "coupling_cost",
                "float",
                "0.1",
                "Coupling cost measures the overhead caused by coupling. This can include the cost of the coupling algorithm itself (which may involve grid interpolation and computation of transfer coefficients for conservative coupling) as well as load imbalance. It is the normalized difference between the time-processor integral for the whole model versus the sum of individual concurrent components.",
            ),
            (
                "memory_bloat",
                "float",
                "0.1",
                "Memory bloat is the ratio of the actual memory size, defined as M minus NP  multiplied by X where M is the measured runtime memory usage and X the size of the executable files, to the ideal memory size Mi, the size of the complete model state, which in theory is all you need to hold in memory.",
            ),
            (
                "data_output_cost",
                "float",
                "0.1",
                "Data output cost is the cost of performing I/O, and is the ratio of CHSY with and without I/O.",
            ),
            (
                "data_intensity",
                "float",
                "0.1",
                "Data intensity is the amount of data produced per compute-hour, in units GB per compute-hour.",
            ),
        ],
    }


def project_cost():
    """Cost of an experiment or project on a particular platform."""
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "is_document": True,
        "pstr": ("Production: {}Y, {}", ("useful_years", "useful_data")),
        "properties": [
            (
                "activity",
                "linked_to(activity.activity)",
                "1.1",
                "Project or Experiment of interest",
            ),
            (
                "platform",
                "linked_to(platform.machine)",
                "1.1",
                "Machine used for project",
            ),
            (
                "useful_years",
                "int",
                "1.1",
                "Number of useful years simulated (or to be simulated) during "
                "this project",
            ),
            (
                "useful_data",
                "shared.numeric",
                "0.1",
                "Volume of useful data to be analysed",
            ),
            (
                "useful_core_hours",
                "int",
                "0.1",
                "Number of core-hours used for useful simulations within "
                "the project",
            ),
            (
                "actual_years",
                "int",
                "0.1",
                "Number of actual years simulated, including spin-up tuning "
                "etc.",
            ),
            (
                "peak_data",
                "shared.numeric",
                "0.1",
                "Maximum volume of data held during project",
            ),
            (
                "total_core_hours",
                "int",
                "0.1",
                "Total number of core hours needed for all aspects of the "
                "project",
            ),
            (
                "total_energy_cost",
                "float",
                "0.1",
                "Total cost of project in Joules, if known",
            ),
        ],
    }


def storage_pool():
    """Homogeneous storage pool on a computing machine."""
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "pstr": ("{} {}", ("name", "file_system_sizes")),
        "properties": [
            (
                "description",
                "str",
                "0.1",
                "Description of the technology used.",
            ),
            ("name", "str", "1.1", "Name of storage pool."),
            ("type", "platform.storage_systems", "0.1", "Type of storage."),
            (
                "vendor",
                "linked_to(shared.party)",
                "0.1",
                "Vendor of storage hardware.",
            ),
            (
                "file_system_sizes",
                "shared.numeric",
                "1.N",
                "Sizes of constituent File Systems",
            ),
        ],
    }


def storage_systems():
    """Controlled vocabulary for storage types (including
    filesystems)."""
    return {
        "type": "enum",
        "is_open": True,
        "members": [
            ("Lustre", "Lustre parallel file system"),
            ("GPFS", "IBM GPFS (also known as IBM Spectral Scale"),
            ("isilon", "The EMC scaleout NAS solution"),
            ("NFS", "Generic Network File System"),
            ("S3", "Object file system exposing the AWS S3 interface"),
            ("PanFS", "Panasas Parallel File system"),
            ("Other Disk", "Other disk based file system"),
            ("Tape - MARS", "Tape storage system using ECMWF MARS"),
            ("Tape - MASS", "Tape storage system using Met Office MASS"),
            ("Tape - Castor", "Tape storage sytsem using CERN Castor"),
            ("Tape - Other", "Other tape based system"),
        ],
    }
