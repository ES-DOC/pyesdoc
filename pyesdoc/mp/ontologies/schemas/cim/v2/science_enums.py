# -*- coding: utf-8 -*-

"""
.. module:: science_enums.py
   :synopsis: Set of CIM v2 ontology type definitions.
   pertaining to the enumerations necessary for the
   description of the scientific capabilities of models

"""


def model_types():
    """Defines a set of model types relevant to weather, climate, and
    earth system modelling."""
    return {
        "type": "enum",
        "is_open": False,
        "members": [
            ("Atm Only", "Atmosphere Only"),
            ("Ocean Only", "Ocean Only"),
            ("Regional", "Regional Model"),
            (
                "ESM",
                "Earth System Model (Atmosphere, Ocean, Land, carbon cycle)",
            ),
            (
                "GCM",
                "Global Climate Model (Atmosphere, Ocean, no carbon cycle)",
            ),
            ("IGCM", "Intermediate Complexity GCM"),
            ("GCM-MLO", "GCM with mixed layer ocean"),
            ("Mesoscale", "Mesoscale Model"),
            ("ProcessLA", "Limited Area process model"),
            ("DynamicalCore", "Dynamical Core only"),
            ("Statistical", "Derived from statistics"),
            ("ML Inference", "Model is trained from data"),
            (
                "Re-Analysis",
                "Model includes active data-assimilation beyond "
                "initialisation",
            ),
            ("Planetary", "Non-Earth model"),
            ("Process", "Specific process or parameterisation in column mode"),
            ("Other", "A numerical model not covered above"),
        ],
    }
