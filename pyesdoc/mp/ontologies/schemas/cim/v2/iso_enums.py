# -*- coding: utf-8 -*-

"""
.. module:: iso_enums.py
   :synopsis: Set of CIM v2 ontology type definitions.
   for ISO Enumerations.

"""


def ds_initiative_typecode():
    """Classifier of initiative, to inform ISO19115 metadata.

    Formally a DS_InitiativeTypeCode, from ISO19115_2011.

    """
    # Do not modify or extend these definitions unless using a later version
    # of ISO19115
    return {
        "type": "enum",
        "is_open": False,
        "members": [
            ("campaign", "series of organized planned actions"),
            (
                "collection",
                "accumulation of datasets assembled for a specific purpose",
            ),
            (
                "exercise",
                "specific performance of a function or group of functions",
            ),
            (
                "experiment",
                "process designed to find if something is effective or valid",
            ),
            ("investigation", "search or systematic inquiry"),
            ("mission", "specific operation of a data collection system"),
            (
                "sensor",
                "device or piece of equipment which detects or records",
            ),
            ("operation", "action that is part of a series of actions"),
            ("platform", "vehicle or other support base that holds a sensor"),
            (
                "process",
                " method of doing something involving a number of steps",
            ),
            ("program", "specific planned activity"),
            ("project", "organized undertaking, research, or development"),
            ("study", "examination or investigation"),
            ("task", "piece of work"),
            (
                "trial",
                "process of testing to discover or demonstrate something",
            ),
        ],
    }


def md_cellgeometry_code():
    """Classifier of cells.

    Whether a grid point is point or area.

    """
    return {
        "type": "enum",
        "is_open": False,
        "members": [
            ("point", "each cell represents a point"),
            ("area", "each cell represents an area"),
        ],
    }


def md_progress_code():
    """Classifier of project or dataset progress."""
    return {
        "type": "enum",
        "is_open": False,
        "members": [
            ("completed", "production of the data has been completed"),
            (
                "historicalArchive",
                "data has been stored in an offline storage facility",
            ),
            ("obsolete", "data is no longer relevant"),
            ("onGoing", "data is continually being updated"),
            (
                "planned",
                "fixed date has been established upon or by which the data "
                "will be created or updated",
            ),
            ("required", "updated"),
            (
                "underDevelopment",
                "data is currently in the process of being created",
            ),
        ],
    }


def dq_evaluation_result_type():
    """Classifier of evaluation results."""
    return {
        "type": "enum",
        "is_open": False,
        "members": [
            (
                "plot",
                "Diagnostic plot, use mime-type to identify what kind of "
                "image format is used",
            ),
            (
                "document",
                "Document of some form, use mime-type to identify if PDF etc",
            ),
            (
                "dataset",
                "Expect a binary target, accessible via a landing page or "
                "directly",
            ),
        ],
    }
