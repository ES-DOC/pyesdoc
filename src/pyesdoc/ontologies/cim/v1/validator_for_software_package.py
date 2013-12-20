"""
.. module:: cim.v1.validator_for_software_package.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of validators over the cim.v1.software package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2013-12-16 16:41:48.355083.

"""
# Module imports.
from validator_for_activity_package import *
from validator_for_data_package import *
from validator_for_grids_package import *
from validator_for_shared_package import *
import typeset



def validate_component(instance):
    """Validates an instance of the following type: cim.v1.types.software.Component.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.Component

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_component_language(instance):
    """Validates an instance of the following type: cim.v1.types.software.ComponentLanguage.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.ComponentLanguage

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_component_language_property(instance):
    """Validates an instance of the following type: cim.v1.types.software.ComponentLanguageProperty.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.ComponentLanguageProperty

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_component_property(instance):
    """Validates an instance of the following type: cim.v1.types.software.ComponentProperty.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.ComponentProperty

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_composition(instance):
    """Validates an instance of the following type: cim.v1.types.software.Composition.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.Composition

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_connection(instance):
    """Validates an instance of the following type: cim.v1.types.software.Connection.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.Connection

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_connection_endpoint(instance):
    """Validates an instance of the following type: cim.v1.types.software.ConnectionEndpoint.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.ConnectionEndpoint

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_connection_property(instance):
    """Validates an instance of the following type: cim.v1.types.software.ConnectionProperty.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.ConnectionProperty

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_coupling(instance):
    """Validates an instance of the following type: cim.v1.types.software.Coupling.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.Coupling

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_coupling_endpoint(instance):
    """Validates an instance of the following type: cim.v1.types.software.CouplingEndpoint.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.CouplingEndpoint

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_coupling_property(instance):
    """Validates an instance of the following type: cim.v1.types.software.CouplingProperty.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.CouplingProperty

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_deployment(instance):
    """Validates an instance of the following type: cim.v1.types.software.Deployment.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.Deployment

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_entry_point(instance):
    """Validates an instance of the following type: cim.v1.types.software.EntryPoint.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.EntryPoint

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_model_component(instance):
    """Validates an instance of the following type: cim.v1.types.software.ModelComponent.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.ModelComponent

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_parallelisation(instance):
    """Validates an instance of the following type: cim.v1.types.software.Parallelisation.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.Parallelisation

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_processor_component(instance):
    """Validates an instance of the following type: cim.v1.types.software.ProcessorComponent.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.ProcessorComponent

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_rank(instance):
    """Validates an instance of the following type: cim.v1.types.software.Rank.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.Rank

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_spatial_regridding(instance):
    """Validates an instance of the following type: cim.v1.types.software.SpatialRegridding.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.SpatialRegridding

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_spatial_regridding_property(instance):
    """Validates an instance of the following type: cim.v1.types.software.SpatialRegriddingProperty.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.SpatialRegriddingProperty

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_spatial_regridding_user_method(instance):
    """Validates an instance of the following type: cim.v1.types.software.SpatialRegriddingUserMethod.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.SpatialRegriddingUserMethod

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_statistical_model_component(instance):
    """Validates an instance of the following type: cim.v1.types.software.StatisticalModelComponent.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.StatisticalModelComponent

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_time_lag(instance):
    """Validates an instance of the following type: cim.v1.types.software.TimeLag.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.TimeLag

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_time_transformation(instance):
    """Validates an instance of the following type: cim.v1.types.software.TimeTransformation.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.TimeTransformation

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


def validate_timing(instance):
    """Validates an instance of the following type: cim.v1.types.software.Timing.

    :param instance: A type instance being validated.
    :type instance: cim.v1.types.software.Timing

    :returns: List of validation errors.
    :rtype: list

    """
    return NotImplementedError()


