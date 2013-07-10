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
from pyesdoc.utils.exception import PYESDOC_Exception

from pyesdoc.ontologies.cim.v1.types.shared.cim_type_info import CimTypeInfo




class _State(object):
    """Encpasulates mutable module state.

    """
    # Type information injected into decoded objects.
    # TODO replace with values from repo.
    type_info = None

    # Set of supported decoders.
    decoders = None


def _get_decoder(ctx):
    """Returns a decoder.

    :param ctx: Serialization context info.
    :type ctx: namedtuple

    """
    def load_decoders():
        import pyesdoc.ontologies.cim.v1.serialization as v1_decoders

        # Set of supported decoders.
        _State.decoders = {
            'cim' : {
                '1' : {
                    'cIM_Quality' : v1_decoders.decode_cim_quality,
                    'dataObject' : v1_decoders.decode_data_object,
                    'ensemble' : v1_decoders.decode_ensemble,
                    'gridSpec' : v1_decoders.decode_grid_spec,
                    'modelComponent' : v1_decoders.decode_model_component,
                    'numericalExperiment' : v1_decoders.decode_numerical_experiment,
                    'platform' : v1_decoders.decode_platform,
                    'simulationRun' : v1_decoders.decode_simulation_run,
                    'simulationComposite' : v1_decoders.decode_simulation_composite,
                    'statisticalModelComponent' : v1_decoders.decode_statistical_model_component,
                }
            },
        }

    # JIT load.
    if _State.decoders is None:
        load_decoders()

    # Defensive programming.
    decoders = _State.decoders
    if ctx.ontology_name not in decoders or \
       ctx.ontology_version not in decoders[ctx.ontology_name] or \
       ctx.type not in decoders[ctx.ontology_name][ctx.ontology_version]:
        err = "{0} v{1} {2} decoder not found."
        err = err.format(ctx.ontology_name, ctx.ontology_version, ctx.type)
        raise PYESDOC_Exception(err)

    return decoders[ctx.ontology_name][ctx.ontology_version][ctx.type]


def _set_type_info(ctx):
    """Injects type information into pyesdoc object.

    :param ctx: Serialization context info.
    :type ctx: namedtuple

    """
    def load_type_info():
        import pyesdoc.ontologies.cim.v1.serialization as v1_decoders

        # Type information injected into decoded objects.
        _State.type_info = {
            'cim' : {
                '1' : {
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
            },
        }

    # JIT load.
    if _State.type_info is None:
        load_type_info()

    # Defensive programming.
    type_info = _State.type_info
    if ctx.ontology_name in type_info and \
       ctx.ontology_version in type_info[ctx.ontology_name] and \
       ctx.type in type_info[ctx.ontology_name][ctx.ontology_version]:
        info = type_info[ctx.ontology_name][ctx.ontology_version][ctx.type]
        ctx.instance.cim_info.type_info = CimTypeInfo()
        ctx.instance.cim_info.type_info.package = info[0]
        ctx.instance.cim_info.type_info.ontology_name = ctx.ontology_name
        ctx.instance.cim_info.type_info.ontology_version = ctx.ontology_version
        ctx.instance.cim_info.type_info.type = ctx.type
        ctx.instance.cim_info.type_info.type_display_name = info[1]
    else:
        print "WARNING :: pyesdoc type information is underivable", ctx.ontology_name, ctx.ontology_version, ctx.type


def decode(ctx):
    """Decodes a pyesdoc document from an xml representation.

    :param ctx: Serialization context info.
    :type ctx: namedtuple

    """
    # Load xml & associated namespaces.
    xml, nsmap = load_xml(ctx.representation, return_nsmap=True)

    # Validate xml.
    if _can_decode_from_xml(xml) == False:
        raise PYESDOC_Exception('Representation failed XML validation.')

    # Set document type.
    ctx.type = xml.tag.split('}')[1]

    # Set decoder.
    decoder = _get_decoder(ctx)

    # Decode pyesdoc obj.
    ctx.instance = decode_xml(decoder, xml, nsmap, None)

    # Assign type info.
    _set_type_info(ctx)


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
