"""
A realm key-properties specialization.
For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Atmosphere key properties'

# --------------------------------------------------------------------
# Top level details.
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': "Top level key properties",
    'properties': [
        ('model_family', 'ENUM:model_family_type', '1.1',
            'Type of atmospheric model.'),
        ('basic_approximations', 'ENUM:basic_approximations_attributes', '1.N',
            'Basic approximations made in the atmosphere.',),
        ]
    }

DETAILS['resolution'] = {
    'description': "Characteristics of the model resolution",
    'properties': [
        ('horizontal_resolution_name', 'str', '1.1',
            'This is a string usually used by the modelling group to describe the resolution of the model grid, '
            'e.g. T42, N48.',),
        ('canonical_horizontal_resolution', 'str', '1.1',
            'Expression quoted for gross comparisons of resolution, e.g. 2.5 x 3.75 degrees lat-lon.'),
        ('range_horizontal_resolution', 'str', '1.1',
             "Range of horizontal resolution with spatial details, eg. 1 deg (Equator) - 0.5 deg"),
        ('number_of_vertical_levels', 'int', '1.1',
             "Number of vertical levels resolved on the computational grid."),
        ('high_top', 'bool', '1.1',
            "Does the atmosphere have a high-top? "
            "High-Top atmospheres have a fully resolved stratosphere with a model top above the stratopause."),
        ]
    }

DETAILS['timestepping'] = {
    'description': "Characteristics of the atmosphere model time stepping",
    'properties': [
        ('timestep_dynamics', 'int', '1.1',
             "Timestep for the dynamics in seconds"),
        ('timestep_shortwave_radiative_transfer', 'int', '0.1',
             "Timestep for the shortwave radiative transfer in seconds."),
        ('timestep_longwave_radiative_transfer', 'int', '0.1',
             "Timestep for the longwave radiative transfer in seconds."),
        ]
    }


DETAILS['orography'] = {
    'description': "Characteristics of the model orography",
    'properties': [
        ('type', 'ENUM:orography_type', '1.1',
            'Type of orographic representation.',),
        ('modified', 'ENUM:orography_changes', '0.N',
            'If the orography type is modified describe the adaptation.'),
        ('time-varying', 'str', '0.1',
            'Describe any time varying orographic change')
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: TUNING APPLIED: Any tuning used to optimise the parameters
# --------------------------------------------------------------------
DETAILS['tuning_applied'] = {
    'description': 'Tuning methodology for atmospheric component',
    'properties': [
        ('description', 'l-str', '1.1',
             "General overview description of tuning: explain and motivate the main targets and metrics retained. &"
             "Document the relative weight given to climate performance metrics versus process oriented metrics, &"
             "and on the possible conflicts with parameterization level tuning. In particular describe any struggle &"
             "with a parameter value that required pushing it to its limits to solve a particular model deficiency."),
        ('global_mean_metrics_used', 'cs-str', '0.1',
             "List set of metrics of the global mean state used in tuning model/component"),
        ('regional_metrics_used', 'cs-str', '0.1',
             "List of regional metrics of mean state used in tuning model/component"),
        ('trend_metrics_used', 'cs-str', '0.1',
             "List observed trend metrics used in tuning model/component"),
        ]
    }

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['model_family_type'] = {
    'description': "Type of atmospheric model",
    'is_open': True,
    'members': [
        ('AGCM', 'Atmospheric General Circulation Model'),
        ('ARCM', 'Atmospheric Regional Climate Model'),
        ]
    }

ENUMERATIONS['basic_approximations_attributes'] = {
    'description': "Basic approximations made in the atmosphere",
    'is_open': True,
    'members': [
        ('primitive equations', None),
        ('non-hydrostatic', None),
        ('anelastic', None),
        ('Boussinesq', None),
        ('hydrostatic', None),
        ('quasi-hydrostatic', None),
        ]
    }


ENUMERATIONS['orography_type'] = {
    'description': "Type of orographic representation",
    'is_open': True,
    'members': [
        ('fixed: present day', None),
        ('fixed: modified', "provide details of modification below"),
        ]
    }

ENUMERATIONS['orography_changes'] = {
    'description': "If the orography type is modified describe the time adaptation changes",
    'is_open': True,
    'members': [
        ('related to ice sheets', None),
        ('related to tectonics', None),
        ('modified mean', None),
        ('modified variance if taken into account in model (cf gravity waves)', None),
        ]
    }
