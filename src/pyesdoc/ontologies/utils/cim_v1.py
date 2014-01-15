"""
.. module:: pyesdoc.ontologies.utils.cim_v1.py
   :copyright: Copyright "Sep 5, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of cim v1 utility constants / functions.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# CIM v1 type keys.
TYPE_KEY_DATA_OBJECT = 'cim.1.data.DataObject'
TYPE_KEY_DOCUMENT_SET = 'cim.1.misc.DocumentSet'
TYPE_KEY_ENSEMBLE = 'cim.1.activity.Ensemble'
TYPE_KEY_GRID_SPEC = 'cim.1.grids.GridSpec'
TYPE_KEY_MODEL_COMPONENT = 'cim.1.software.ModelComponent'
TYPE_KEY_NUMERICAL_EXPERIMENT = 'cim.1.activity.NumericalExperiment'
TYPE_KEY_PLATFORM = 'cim.1.shared.Platform'
TYPE_KEY_QUALITY = 'cim.1.quality.CimQuality'
TYPE_KEY_SIMULATION_COMPOSITE = 'cim.1.activity.SimulationComposite'
TYPE_KEY_SIMULATION_RUN = 'cim.1.activity.SimulationRun'
TYPE_KEY_STATISTICAL_MODEL_COMPONENT = 'cim.1.software.StatisticalModelComponent'

# CIM v1 active typeset.
ACTIVE_TYPES = [
    TYPE_KEY_DATA_OBJECT,
    TYPE_KEY_DOCUMENT_SET,
    TYPE_KEY_ENSEMBLE,
    TYPE_KEY_GRID_SPEC,
    TYPE_KEY_MODEL_COMPONENT,
    TYPE_KEY_NUMERICAL_EXPERIMENT,
    TYPE_KEY_PLATFORM,
    TYPE_KEY_QUALITY,
    TYPE_KEY_SIMULATION_COMPOSITE,
    TYPE_KEY_SIMULATION_RUN,
    TYPE_KEY_STATISTICAL_MODEL_COMPONENT
]

# XML tag names.
XML_TAG_ASSIMILATION = 'assimilation'
XML_TAG_DATA_OBJECT = 'dataObject'
XML_TAG_DATA_PROCESSING = 'dataProcessing'
XML_TAG_DOCUMENT_SET = 'CIMDocumentSet'
XML_TAG_ENSEMBLE = 'ensemble'
XML_TAG_GRID_SPEC = 'gridSpec'
XML_TAG_MODEL_COMPONENT = 'modelComponent'
XML_TAG_NUMERICAL_EXPERIMENT = 'numericalExperiment'
XML_TAG_PLATFORM = 'platform'
XML_TAG_PROCESSOR_COMPONENT = 'processorComponent'
XML_TAG_QUALITY = 'cIM_Quality'
XML_TAG_SIMULATION_COMPOSITE = 'simulationComposite'
XML_TAG_SIMULATION_RUN = 'simulationRun'
XML_TAG_STATISTICAL_MODEL_COMPONENT = 'statisticalModelComponent'

# Display names.
DISPLAY_NAMES = {
    TYPE_KEY_DATA_OBJECT : "Data",
    TYPE_KEY_DOCUMENT_SET : "Documents",
    TYPE_KEY_ENSEMBLE : "Ensemble",
    TYPE_KEY_GRID_SPEC : "Grid Spec",
    TYPE_KEY_MODEL_COMPONENT : "Model",
    TYPE_KEY_NUMERICAL_EXPERIMENT : "Experiment",
    TYPE_KEY_PLATFORM : "Platform",
    TYPE_KEY_QUALITY : "Quailty",
    TYPE_KEY_SIMULATION_COMPOSITE : "Simulation",
    TYPE_KEY_SIMULATION_RUN : "Simulation",
    TYPE_KEY_STATISTICAL_MODEL_COMPONENT : "Statistical Model",
}

