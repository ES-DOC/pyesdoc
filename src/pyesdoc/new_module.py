# CIM v1 type names.
CIM_1_TYPE_ASSIMILATION = 'assimilation'
CIM_1_TYPE_DATA_OBJECT = 'dataObject'
CIM_1_TYPE_DATA_PROCESSING = 'dataProcessing'
CIM_1_TYPE_DOCUMENT_SET = 'CIMDocumentSet'
CIM_1_TYPE_ENSEMBLE = 'ensemble'
CIM_1_TYPE_GRID_SPEC = 'gridSpec'
CIM_1_TYPE_MODEL_COMPONENT = 'modelComponent'
CIM_1_TYPE_NUMERICAL_EXPERIMENT = 'numericalExperiment'
CIM_1_TYPE_PLATFORM = 'platform'
CIM_1_TYPE_PROCESSOR_COMPONENT = 'processorComponent'
CIM_1_TYPE_QUALITY = 'cIM_Quality'
CIM_1_TYPE_SIMULATION_COMPOSITE = 'simulationComposite'
CIM_1_TYPE_SIMULATION_RUN = 'simulationRun'
CIM_1_TYPE_STATISTICAL_MODEL_COMPONENT = 'statisticalModelComponent'

# CIM v1 types.
CIM_1_TYPES = (
    (CIM_1_TYPE_ASSIMILATION, None),
    (CIM_1_TYPE_DATA_OBJECT, cim.v1.typeset.DataObject),
    (CIM_1_TYPE_DATA_PROCESSING, None),
    (CIM_1_TYPE_DOCUMENT_SET, None),
    (CIM_1_TYPE_ENSEMBLE, cim.v1.typeset.Ensemble),
    (CIM_1_TYPE_GRID_SPEC, cim.v1.typeset.GridSpec),
    (CIM_1_TYPE_MODEL_COMPONENT, cim.v1.typeset.ModelComponent),
    (CIM_1_TYPE_NUMERICAL_EXPERIMENT, cim.v1.typeset.NumericalExperiment),
    (CIM_1_TYPE_PLATFORM, cim.v1.typeset.Platform),
    (CIM_1_TYPE_PROCESSOR_COMPONENT, cim.v1.typeset.ProcessorComponent),
    (CIM_1_TYPE_QUALITY, cim.v1.typeset.CimQuality),
    (CIM_1_TYPE_SIMULATION_COMPOSITE, cim.v1.typeset.SimulationComposite),
    (CIM_1_TYPE_SIMULATION_RUN, cim.v1.typeset.SimulationRun),
    (CIM_1_TYPE_STATISTICAL_MODEL_COMPONENT, cim.v1.typeset.StatisticalModelComponent),
)

# CIM v1 active typeset.
CIM_1_TYPES_ACTIVE = [
    CIM_1_TYPE_DATA_OBJECT,
    CIM_1_TYPE_ENSEMBLE,
    CIM_1_TYPE_GRID_SPEC,
    CIM_1_TYPE_MODEL_COMPONENT,
    CIM_1_TYPE_NUMERICAL_EXPERIMENT,
    CIM_1_TYPE_PLATFORM,
    CIM_1_TYPE_QUALITY,
    CIM_1_TYPE_SIMULATION_COMPOSITE,
    CIM_1_TYPE_SIMULATION_RUN,
    CIM_1_TYPE_STATISTICAL_MODEL_COMPONENT,
]

# Set of supported ontologies.
ESDOC_ONTOLOGIES = (
    ('cim', '1', CIM_1_TYPES),
)
