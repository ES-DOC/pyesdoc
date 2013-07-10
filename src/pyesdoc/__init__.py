"""
.. module:: pyesdoc.__init__.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Package initialisor.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""

# Module imports.
from pyesdoc.serialization import (
    decode as decoder,
    encode as encoder
    )
from pyesdoc.utils.ontologies import *


from pyesdoc.utils.ontologies import (
    ESDOC_ONTOLOGIES,
    ESDOC_ENCODINGS,
    ESDOC_ENCODING_JSON,
    ESDOC_ENCODING_XML,
    METAFOR_CIM_XML_ENCODING,
    ESDOC_DEFAULT_ENCODING,
    ESDOC_DEFAULT_LANGUAGE,
    ESDOC_VERSION_LATEST,
    ESDOC_UNICODE,
    CIM_1_TYPES,
    CIM_1_TYPES_ACTIVE,
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
    CIM_1_TYPE_STATISTICAL_MODEL_COMPONENT
    )


def decode(representation, ontology_name, ontology_version, encoding):
    """Decodes a pyesdoc document representation.

    :param representation: A document representation (e.g. utf-8).
    :type representation: str

    :param ontology_name: Name of ontology from which representation is derived (e.g. CIM).
    :type ontology_name: str

    :param ontology_version: Version of ontology from which representation is derived (e.g. v1).
    :type ontology_version: str

    :param encoding: A document encoding (e.g. json).
    :type encoding: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    return decoder(representation, ontology_name, ontology_version, encoding)


def encode(instance, ontology_name, ontology_version, encoding):
    """Encodes a pyesdoc document instance.

    :param instance: pyesdoc document instance.
    :type instance: object

    :param ontology_name: Name of ontology from which representation is derived (e.g. CIM).
    :type ontology_name: str

    :param ontology_version: Version of ontology from which representation is derived (e.g. v1).
    :type ontology_version: str

    :param encoding: A document encoding (e.g. json).
    :type encoding: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    return encoder(instance, ontology_name, ontology_version, encoding)
