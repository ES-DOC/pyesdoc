"""
.. module:: software_enums.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 software package enum definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def component_property_intent_type():
    """The direction that the associated component property is intended to be coupled: in, out, or inout.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('in', None),
            ('out', None),
            ('inout', None),
        ],
    }


def connection_type():
    """The ConnectionType enumeration describes the mechanism of transport for a connection.

    """
    return {
        'type': 'enum',
        'is_open': True
    }


def coupling_framework_type():
    """Creates and returns instance of coupling_framework_type enum.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('BFG', None),
            ('ESMF', None),
            ('OASIS', None),
        ],
    }


def model_component_type():
    """An enumeration of types of ModelComponent. This includes things like atmosphere & ocean models, radiation schemes, etc. CIM best-practice is to describe every component for which there is a named ComponentType as a separate component, even if it is not a separate unit of software (ie: even if it is embedded), instead of as a (set of) ModelParameters. This codelist is synonomous with "realm" for the purposes of CMIP5.

    """
    return {
        'type': 'enum',
        'is_open': True
    }


def spatial_regridding_dimension_type():
    """Creates and returns instance of spatial_regridding_dimension_type enum.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('1D', None),
            ('2D', None),
            ('3D', None),
        ],
    }


def spatial_regridding_standard_method_type():
    """Creates and returns instance of spatial_regridding_standard_method_type enum.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('linear', None),
            ('near-neighbour', None),
            ('cubic', None),
            ('conservative-first-order', None),
            ('conservative-second-order', None),
            ('conservative', None),
            ('non-conservative', None),
        ],
    }


def statistical_model_component_type():
    """An enumeration of types of ProcessorComponent.  This includes things like transformers and post-processors.

    """
    return {
        'type': 'enum',
        'is_open': True
    }


def time_mapping_type():
    """Enumerates the different ways that time can be mapped when transforming from one field to another.

    """
    return {
        'type': 'enum',
        'is_open': True
    }


def timing_units():
    """Creates and returns instance of timing_units enum.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('seconds', None),
            ('minutes', None),
            ('hours', None),
            ('days', None),
            ('months', None),
            ('years', None),
            ('decades', None),
            ('centuries', None),
        ],
    }
