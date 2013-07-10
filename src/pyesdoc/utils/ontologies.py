"""
.. module:: pyesdoc.utils.ontologies.py
   :copyright: Copyright "Jun 14, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Ontology utility functions.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""

# ESDOC json encoding.
ESDOC_ENCODING_JSON = 'json'

# ESDOC xml encoding.
ESDOC_ENCODING_XML = 'xml'

# Metafor CIM xml encoding.
METAFOR_CIM_XML_ENCODING = 'metafor-xml'

# Set of supported ESDOC encodings.
ESDOC_ENCODINGS = [
    ESDOC_ENCODING_JSON,
    ESDOC_ENCODING_XML,
    METAFOR_CIM_XML_ENCODING,
]

# Default encoding, language.
ESDOC_DEFAULT_ENCODING = ESDOC_ENCODING_JSON
ESDOC_DEFAULT_LANGUAGE = 'en'

# Token for latest version of a document.
ESDOC_VERSION_LATEST = 'latest'

# Default xml encoding.
ESDOC_UNICODE = 'utf-8'

# Set of supported cim v1 types.
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


# Collection of active cim v1 types.
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

# Collection of all cim v1 types.
CIM_1_TYPES = [
    CIM_1_TYPE_ASSIMILATION,
    CIM_1_TYPE_DATA_OBJECT,
    CIM_1_TYPE_DATA_PROCESSING,
    CIM_1_TYPE_DOCUMENT_SET,
    CIM_1_TYPE_ENSEMBLE,
    CIM_1_TYPE_GRID_SPEC,
    CIM_1_TYPE_MODEL_COMPONENT,
    CIM_1_TYPE_NUMERICAL_EXPERIMENT,
    CIM_1_TYPE_PLATFORM,
    CIM_1_TYPE_PROCESSOR_COMPONENT,
    CIM_1_TYPE_QUALITY,
    CIM_1_TYPE_SIMULATION_COMPOSITE,
    CIM_1_TYPE_SIMULATION_RUN,
    CIM_1_TYPE_STATISTICAL_MODEL_COMPONENT,
]

# Set of supported ontologies.
ESDOC_ONTOLOGIES = {
    'cim' : {
        '1' : {
            'types' : CIM_1_TYPES
        }
    }
}


def is_supported(name, version):
    """Returns a flag indicating whether the schema is supported.

    :param name: Schema name.
    :type name: str

    :param version: Schema version.
    :type version: str

    :returns: True if the schema is supported, false otherwise.
    :rtype: bool

    """
    name = str(name).lower()
    version = str(version).upper()

    return name in ESDOC_ONTOLOGIES and version in ESDOC_ONTOLOGIES[name]


