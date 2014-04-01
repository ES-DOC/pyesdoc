"""
.. module:: pyesdoc.utils.decoder_xml.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Document decoder from metafor cim v1 xml.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
from lxml import etree as et

from . decoder_xml_utils import (
    load_xml,
    decode_xml
    )
from .. ontologies import cim
from .. utils import runtime as rt



# CIM v1 decoders.
_decoders = {
    'cIM_Quality' : cim.v1.decoder.decode_cim_quality,
    'numericalExperiment' : cim.v1.decoder.decode_numerical_experiment,
    'CIMDocumentSet' : cim.v1.decoder.decode_document_set,
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


def decode(repr):
    """Decodes a pyesdoc document from passed representation.

    :param repr: Metafor CIM v1 XML document representation.
    :type repr: lxml.etree._ElementTree

    """
    # Defensive programming.
    xml, nsmap = load_xml(repr, return_nsmap=True)
    if not isinstance(xml, et._Element):
        rt.raise_error('Decoding failure due to invalid Metafor CIM v1 XML.')

    # Validate decoder.
    doc_type = xml.tag.split('}')[1]
    if doc_type not in _decoders:
        rt.raise_error("CIM v1 - {0} document type decoding unsupported.".format(doc_type))
    
    # Decode pyesdoc doc.
    return decode_xml(_decoders[doc_type], xml, nsmap, None)
