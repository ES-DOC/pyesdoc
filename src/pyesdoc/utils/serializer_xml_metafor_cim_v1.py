"""
.. module:: pyesdoc.utils.serializer_xml_metafor_cim_v1.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
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
from .. utils import runtime as rt



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


def decode(repr):
    """Decodes a pyesdoc document from passed representation.

    :param repr: Metafor CIM v1 XML document representation.
    :type repr: lxml.etree._ElementTree

    """
    # Load xml & associated namespaces.
    xml, nsmap = load_xml(repr, return_nsmap=True)
    if not isinstance(xml, et._Element):
        raise rt.PYESDOC_Exception('Decoding failure due to invalid Metafor CIM v1 XML XML.')

    # Validate decoder.
    doc_type = xml.tag.split('}')[1]
    if doc_type not in _decoders:
        raise rt.PYESDOC_Exception("CIM v1 - {0} document type decoding unsupported.".format(doc_type))

    # Decode pyesdoc doc.
    return decode_xml(_decoders[doc_type], xml, nsmap, None)


def encode(doc):
    """Encodes a document to an xml string.

    :param doc: Document being encoded.
    :type doc: object

    :returns: An xml representation of a document.
    :rtype: str

    """
    raise NotImplementedError()
