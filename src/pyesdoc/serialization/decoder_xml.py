"""
.. module:: pyesdoc.serialization.decoder_xml.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes functions for decoding document instances from xml representations.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""

# Module imports.
from lxml import etree as et

from pyesdoc.serialization.decoder_xml_utils import (
    load_xml,
    decode_xml
    )
from pyesdoc.utils.exception import ESDOC_Exception

from pyesdoc.ontologies.cim.v1_5.types.shared.cim_type_info import CimTypeInfo
import pyesdoc.ontologies.cim.v1_5.serialization as v1_5_decoders



# Set of decoders grouped by cim version.
_decoders = {
    '1.5' : {
        'cIM_Quality' : v1_5_decoders.decode_cim_quality,
        'dataObject' : v1_5_decoders.decode_data_object,
        'ensemble' : v1_5_decoders.decode_ensemble,
        'gridSpec' : v1_5_decoders.decode_grid_spec,
        'modelComponent' : v1_5_decoders.decode_model_component,
        'numericalExperiment' : v1_5_decoders.decode_numerical_experiment,
        'platform' : v1_5_decoders.decode_platform,
        'simulationRun' : v1_5_decoders.decode_simulation_run,
        'simulationComposite' : v1_5_decoders.decode_simulation_composite,
    }
}

# Set of type information injected into decoded objects.
_type_info = {
    '1.5' : {
        'cIM_Quality' : ('quality', 'QC Record'),
        'dataObject' : ('data', 'Data Object'),
        'ensemble' : ('activity', 'Ensemble'),
        'gridSpec' : ('grids', 'Grid'),
        'modelComponent' : ('software', 'Model'),
        'numericalExperiment' : ('activity', 'Experiment'),
        'platform' : ('activity', 'Platform'),
        'simulationRun' : ('activity', 'Simulation'),
        'simulationComposite' : ('activity', 'Simulation'),
    }
}


def decode(representation, schema):
    """Decodes a pyesdoc document from an xml representation.

    :param representation: A document xml representation.
    :type representation: str

    :param schema: A document schema (e.g. CIM 1.5).
    :type schema: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Load xml & associated namespaces.
    xml, nsmap = load_xml(representation, return_nsmap=True)

    # Validate xml.
    if _can_decode_from_xml(xml) == False:
        raise ESDOC_Exception('Representation failed XML validation.')

    # Get document type.
    type = xml.tag.split('}')[1]
    
    # Get decoder.
    if type not in _decoders[schema]:
        raise ESDOC_Exception('No decoder exists for the following CIM type :: {0}.'.format(type))
    decoder = _decoders[schema][type]

    # Decode pyesdoc obj.
    obj = decode_xml(decoder, xml, nsmap, None)

    # Assign type info.
    _set_cim_type_info(obj, schema, type)

    return obj


def _set_cim_type_info(obj, schema, type):
    """Injects type information into pyesdoc object.

    :param obj: pyesdoc document instance.
    :type obj: object

    :param schema: A document schema (e.g. CIM 1.5).
    :type schema: str

    :param type: Document type (e.g. 'model').
    :type schema: str


    """
    if schema in _type_info and type in _type_info[schema]:
        info = _type_info[schema][type]
        obj.cim_info.type_info = CimTypeInfo()
        obj.cim_info.type_info.package = info[0]
        obj.cim_info.type_info.schema = schema
        obj.cim_info.type_info.type = type
        obj.cim_info.type_info.type_display_name = info[1]
    else:
        print "WARNING :: object type information is underivable", schema, type


def _can_decode_from_xml(xml):
    """Determines a priori whether xml is decodeable.

    :param xml: An xml representation (i.e. string, url ...etc.).
    :type xml: str
    
    """
    # Load (if necessary).
    if isinstance(xml, et._Element) == False:
        xml = load_xml(xml)

    # False if representation is not of correct type.
    if isinstance(xml, et._Element) == False:
        return False

    # False if representation is an invalid xml instance.
    # TODO - implement via call to validator component.

    # All tests have passed therefore return true.
    return True
