"""
.. module:: xml_metafor_cim_v1.decoder.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Decodes a document from a Metafor cim v1 XML text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from lxml import etree as et


from pyesdoc._codecs.xml_metafor_cim_v1.decoder_utils import load_xml
from pyesdoc._codecs.xml_metafor_cim_v1.decoder_utils import decode_xml
from pyesdoc.ontologies import cim



# Map of decoders to document root tag names.
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


def decode(as_xml):
    """Decodes a pyesdoc document from passed representation.

    :param as_xml: Metafor CIM v1 XML document representation.
    :type as_xml: str | unicode | lxml.etree._ElementTree

    """
    # Defensive programming.
    xml, nsmap = load_xml(as_xml, return_nsmap=True)
    if not isinstance(xml, et._Element):
        raise TypeError('Decoding failure due to invalid Metafor CIM v1 XML.')

    # Validate decoder.
    doc_type = xml.tag.split('}')[1]
    if doc_type not in _decoders:
        raise ValueError("CIM v1 - {0} document type decoding unsupported.".format(doc_type))

    # Decode pyesdoc doc.
    return decode_xml(_decoders[doc_type], xml, nsmap, None)
