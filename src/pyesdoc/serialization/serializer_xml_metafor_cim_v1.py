"""
.. module:: pyesdoc.serialization.serializer_xml_metafor_cim_v1.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes functions for decoding document instances from Metafor CIM v1 xml representations.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""

# Module imports.
from lxml import etree as et

from . decoder_xml_utils import (
    load_xml,
    decode_xml
    )
from .. ontologies import cim
import pyesdoc.utils.runtime as rt



# CIM v1 decoders.
_decoders = {
    'cIM_Quality' : cim.v1.decoder.decode_cim_quality,
    'dataObject' : cim.v1.decoder.decode_data_object,
    'ensemble' : cim.v1.decoder.decode_ensemble,
    'gridSpec' : cim.v1.decoder.decode_grid_spec,
    'modelComponent' : cim.v1.decoder.decode_model_component,
    'numericalExperiment' : cim.v1.decoder.decode_numerical_experiment,
    'platform' : cim.v1.decoder.decode_platform,
    'simulationRun' : cim.v1.decoder.decode_simulation_run,
    'simulationComposite' : cim.v1.decoder.decode_simulation_composite,
    'statisticalModelComponent' : cim.v1.decoder.decode_statistical_model_component,
}

# CIM v1 type information.
_type_info = {
    'cIM_Quality' : ('quality', 'QC Record'),
    'dataObject' : ('data', 'Data Object'),
    'ensemble' : ('activity', 'Ensemble'),
    'gridSpec' : ('grids', 'Grid'),
    'modelComponent' : ('software', 'Model'),
    'numericalExperiment' : ('activity', 'Experiment'),
    'platform' : ('activity', 'Platform'),
    'simulationRun' : ('activity', 'Simulation'),
    'simulationComposite' : ('activity', 'Simulation'),
    'statisticalModelComponent' : ('software', 'Statistical Model'),
}



def _set_type_info(doc, doc_type):
    """Injects type information into pyesdoc object."""
    doc.cim_info.type_info = cim.v1.typeset.CimTypeInfo()
    doc.cim_info.type_info.ontology_name = cim.NAME
    doc.cim_info.type_info.ontology_version = cim.v1.ID
    doc.cim_info.type_info.type = doc_type
    doc.cim_info.type_info.package = _type_info[doc_type][0]
    doc.cim_info.type_info.type_display_name = _type_info[doc_type][1]


def decode(as_xml):
    """Decodes a pyesdoc document from passed representation.

    :param as_xml: Metafor CIM v1 XML document representation.
    :type as_xml: lxml.etree._ElementTree

    """
    # Load xml & associated namespaces.
    xml, nsmap = load_xml(as_xml, return_nsmap=True)
    if not isinstance(xml, et._Element):
        raise rt.PYESDOC_Exception('Decoding failure due to invalid Metafor CIM v1 XML XML.')

    # Validate decoder.
    doc_type = xml.tag.split('}')[1]
    if doc_type not in _decoders:
        raise rt.PYESDOC_Exception("CIM v1 - {0} document type decoding unsupported.".format(doc_type))

    # Decode pyesdoc obj.
    doc = decode_xml(_decoders[doc_type], xml, nsmap, None)

    # Assign type info.
    _set_type_info(doc, doc_type)

    return doc



def encode(doc):
    """Encodes a document to an xml string.

    :param doc: Document being encoded.
    :type doc: object

    :returns: An xml representation of a document.
    :rtype: str

    """
    raise NotImplementedError()
