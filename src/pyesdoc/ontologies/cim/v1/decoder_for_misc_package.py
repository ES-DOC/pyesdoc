# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.decoder_for_misc_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-05 15:44:25.772771.

"""
from decoder_xml_utils import set_attributes
from decoder_for_activity_package import *
from decoder_for_data_package import *
from decoder_for_grids_package import *
from decoder_for_shared_package import *
from decoder_for_software_package import *
import typeset



def decode_document_set(xml, nsmap):
    """Decodes an instance of the following type: document set.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.misc.DocumentSet

    """
    decodings = [
        ('platform', False, decode_platform, 'child::cim:platform'),
        ('ensembles', True, decode_ensemble, 'child::cim:ensemble'),
        ('grids', True, decode_grid_spec, 'child::cim:gridSpec'),
        ('model', False, decode_model_component, 'child::cim:modelComponent'),
        ('data', True, decode_data_object, 'child::cim:dataObject'),
        ('experiment', False, decode_numerical_experiment, 'child::cim:numericalExperiment'),
        ('simulation', False, decode_simulation_run, 'child::cim:simulationRun'),
    ]

    return set_attributes(typeset.misc.DocumentSet(), xml, nsmap, decodings)


