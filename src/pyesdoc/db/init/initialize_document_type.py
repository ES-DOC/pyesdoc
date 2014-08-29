"""
.. module:: initialize_document_type.py
   :platform: Unix
   :synopsis: Initializes collection of supported document types.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# -*- coding: iso-8859-15 -*-

# Module imports.
from .. import (
    dao,
    models, 
    session
    )
from ...utils import runtime as rt



# CIM v1 type keys.
_TYPE_KEY_DATA_OBJECT = 'cim.1.data.DataObject'
_TYPE_KEY_DOCUMENT_SET = 'cim.1.misc.DocumentSet'
_TYPE_KEY_ENSEMBLE = 'cim.1.activity.Ensemble'
_TYPE_KEY_GRID_SPEC = 'cim.1.grids.GridSpec'
_TYPE_KEY_MODEL_COMPONENT = 'cim.1.software.ModelComponent'
_TYPE_KEY_NUMERICAL_EXPERIMENT = 'cim.1.activity.NumericalExperiment'
_TYPE_KEY_PLATFORM = 'cim.1.shared.Platform'
_TYPE_KEY_QUALITY = 'cim.1.quality.CimQuality'
_TYPE_KEY_SIMULATION_COMPOSITE = 'cim.1.activity.SimulationComposite'
_TYPE_KEY_SIMULATION_RUN = 'cim.1.activity.SimulationRun'
_TYPE_KEY_STATISTICAL_MODEL_COMPONENT = 'cim.1.software.StatisticalModelComponent'

# Active typeset.
_ACTIVE_TYPES = [
    _TYPE_KEY_DATA_OBJECT,
    _TYPE_KEY_DOCUMENT_SET,
    _TYPE_KEY_ENSEMBLE,
    _TYPE_KEY_GRID_SPEC,
    _TYPE_KEY_MODEL_COMPONENT,
    _TYPE_KEY_NUMERICAL_EXPERIMENT,
    _TYPE_KEY_PLATFORM,
    _TYPE_KEY_QUALITY,
    _TYPE_KEY_SIMULATION_COMPOSITE,
    _TYPE_KEY_SIMULATION_RUN,
    _TYPE_KEY_STATISTICAL_MODEL_COMPONENT
]

# Search target typeset.
_SEARCH_TYPES = [
    _TYPE_KEY_DOCUMENT_SET,
    _TYPE_KEY_GRID_SPEC,
    _TYPE_KEY_MODEL_COMPONENT,
    _TYPE_KEY_NUMERICAL_EXPERIMENT,
    _TYPE_KEY_PLATFORM,
]

# Display names.
_DISPLAY_NAMES = {
    _TYPE_KEY_DATA_OBJECT: "Data",
    _TYPE_KEY_DOCUMENT_SET: "Simulation",
    _TYPE_KEY_ENSEMBLE: "Ensemble",
    _TYPE_KEY_GRID_SPEC: "Grid Spec",
    _TYPE_KEY_MODEL_COMPONENT: "Model",
    _TYPE_KEY_NUMERICAL_EXPERIMENT: "Experiment",
    _TYPE_KEY_PLATFORM: "Platform",
    _TYPE_KEY_QUALITY: "Quailty",
    _TYPE_KEY_SIMULATION_COMPOSITE: "Simulation",
    _TYPE_KEY_SIMULATION_RUN: "Simulation",
    _TYPE_KEY_STATISTICAL_MODEL_COMPONENT: "Statistical Model",
}


def execute():
    """Initializes collection of cim document schema types.

    """
    ontologies = {}

    for type_key in _ACTIVE_TYPES:
        # Unpack type info.
        ontology, version, package, typeof = type_key.split(".")
        ontology = ontology + "." + version

        # Cache.
        if ontology not in ontologies:
            ontologies[ontology] = dao.get_doc_ontology(ontology)

        # Create.
        i = models.DocumentType()
        i.Ontology_ID = ontologies[ontology].ID
        i.Key = type_key
        i.DisplayName = _DISPLAY_NAMES[type_key]
        i.SearchTarget = type_key in _SEARCH_TYPES

        # Persist.
        session.insert(i)
