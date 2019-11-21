"""
.. module:: cim.v1.decoder_for_misc_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

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

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.misc.DocumentSet

    """
    decodings = [
        ('data', True, decode_data_object, 'child::cim:dataObject'),
        ('ensembles', True, decode_ensemble, 'child::cim:ensemble'),
        ('experiment', False, decode_numerical_experiment, 'child::cim:numericalExperiment'),
        ('grids', True, decode_grid_spec, 'child::cim:gridSpec'),
        ('model', False, decode_model_component, 'child::cim:modelComponent'),
        ('platform', False, decode_platform, 'child::cim:platform'),
        ('simulation', False, decode_simulation_run, 'child::cim:simulationRun'),
    ]

    return set_attributes(typeset.misc.DocumentSet(), xml, nsmap, decodings)


