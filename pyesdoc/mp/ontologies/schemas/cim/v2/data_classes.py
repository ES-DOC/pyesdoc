# -*- coding: utf-8 -*-

"""
.. module:: data_classes.py
   :synopsis: Set of CIM v2 ontology type definitions
   which are related to describing data.

"""


def dataset():
    """Dataset discovery information.

    This may be further enhanced for ISO (or any other) compliance via
    the extra attributes or project specific sub-classing.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "is_document": True,
        "pstr": ("{}", ("name",)),
        "properties": [
            (
                "citations",
                "linked_to(shared.citation)",
                "0.N",
                "Set of pertinent citations.",
            ),
            (
                "responsible_parties",
                "shared.responsibility",
                "0.N",
                "Individuals and organisations responsible for the data.",
            ),
            ("name", "str", "1.1", "Name of dataset."),
            ("description", "str", "0.1", "Textural description of dataset."),
            (
                "type",
                "data.dataset_type",
                "1.N",
                "Dataset discovery classifier",
            ),
            (
                "availability",
                "shared.online_resource",
                "0.N",
                "Where the data is located, and how it is accessed.",
            ),
            (
                "related_to_dataset",
                "shared.formal_association",
                "0.N",
                "Related dataset.",
            ),
            (
                "contains",
                "data.variable_collection",
                "0.N",
                "Contents in terms of variables.",
            ),
            (
                "progress",
                "iso.md_progress_code",
                "0.1",
                "State of the dataset",
            ),
            (
                "keywords",
                "str",
                "0.N",
                "Set of additional keywords to aid discovery/classification",
            ),
            (
                "further_attributes",
                "shared.extra_attribute",
                "0.N",
                "Additional attributes as necessary.",
            ),
            (
                "lineage",
                "linked_to(iso.lineage)",
                "0.1",
                "Provenance of the dataset",
            ),
        ],
    }


def variable_collection():
    """A collection of variables within the scope of a code or process
    element."""
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            (
                "collection_name",
                "str",
                "0.1",
                "Name for this variable collection.",
            ),
            ("variables", "str", "1.N", "Set of variable names."),
            (
                "geometry",
                "iso.md_cellgeometry_code",
                "0.1",
                "Defines whether or not all variables in collection are point "
                "or area based",
            ),
        ],
    }


def dataset_type():
    """Classifier of dataset type, to inform discovery metadata.

    Informed by Bedia et al,
    https://doi.org/10.1016/j.envsoft.2019.07.005, but adjusted for more
    generality.

    """
    return {
        "type": "enum",
        "is_open": False,
        "members": [
            (
                "reanalysis",
                "Hindcast which includes observations via data assimilation",
            ),
            ("analysis", "Product of manipulation of multiple input datasets"),
            (
                "forecast",
                "Representation of a future real time predicted from a "
                "specific initial condition ",
            ),
            (
                "hindcast",
                "Representation of a past real time predicted from a specific "
                "initial condition",
            ),
            (
                "projection",
                "Representation a possible future given initial conditions "
                "and assumptions",
            ),
            ("representation", "Simulation of a particular object or process"),
            (
                "observation",
                "Constructed from observations or measurements alone",
            ),
            (
                "dump",
                "Raw computer output intended for re-use within or by "
                "originating software",
            ),
            (
                "modified",
                "Modified representation of another dataset (e.g. regridded)",
            ),
            (
                "unphysical",
                "Not intended for comparison with the real world (e.g. as "
                "part of a sensitivity study)",
            ),
            (
                "downscaled",
                "Dataset was downscaled by embedded simulation within driving "
                "data at larger scale",
            ),
        ],
    }
