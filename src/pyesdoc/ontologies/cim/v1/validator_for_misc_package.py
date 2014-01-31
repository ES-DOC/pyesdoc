"""
.. module:: cim.v1.validator_for_misc_package.py

   :copyright: @2014 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of validators over the cim.v1.misc package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2014-01-31 14:14:51.544489.

"""
# Module imports.
from validator_for_activity_package import *
from validator_for_grids_package import *
from validator_for_shared_package import *
from validator_for_software_package import *
import typeset



def validate_document_set(instance):
    """Validates an instance of the following type: cim.v1.types.misc.DocumentSet.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.misc.DocumentSet

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


