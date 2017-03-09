"""A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""

from collections import OrderedDict
DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()


# --------------------------------------------------------------------
# CONTACT
#
# Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# AUTHORS
#
# Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = ''

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Top of atmosphere solar insolation characteristics'

# --------------------------------------------------------------------
# SUB-PROCESS: solar_forcing_pathways
# --------------------------------------------------------------------
DETAILS['solar_pathways'] = {
    'description': "Pathways for solar forcing of the atmosphere",
    'properties': [
        ('pathways', 'ENUM:solar_forcing_pathways', '1.N',
            'Pathways for the solar forcing of the atmosphere model domain'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: solar_constant
# --------------------------------------------------------------------
DETAILS['solar_constant'] = {
    'description': "Solar constant and top of atmosphere insolation characteristics",
    'properties': [
        ('type', 'ENUM:top_insolation_solar_constant_type', '1.1',
             'Time adaptation of the solar constant.'),
        ('fixed_value', 'float', '0.1',
             'If the solar constant is fixed, enter the value of the solar constant (W m-2).'),
        ('transient_characteristics', 'str', '1.1',
             'solar constant transient characteristics (W m-2)'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: orbital_parameters
# --------------------------------------------------------------------
DETAILS['orbital_parameters'] = {
    'description': "Orbital parameters and top of atmosphere insolation characteristics",
    'properties': [
        ('type', 'ENUM:top_insolation_orbital_parameters_type', '1.1',
            'Time adaptation of orbital parameters'),
        ('fixed_reference_date', 'int', '1.1',
            'Reference date for fixed orbital parameters (yyyy)'),
        ('solar_constant_transient_characteristics', 'str', '1.1',
            'Characteristics of transient orbital parameters'),
        ('computation_method', 'ENUM:top_insolation_orbital_parameters_computation_method', '1.1',
            'Method used for computing orbital parameters.')
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: insolation_ozone
# --------------------------------------------------------------------
DETAILS['insolation_ozone'] = {
    'description': "Impact of solar insolation on stratospheric ozone",
    'properties': [
        ('solar_ozone_impact', 'bool', '1.1',
            'Does top of atmosphere insolation impact on stratospheric ozone?'),
        ]
    }

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------

ENUMERATIONS['solar_forcing_pathways'] = {
    'description': "Pathways for solar forcing of the atmosphere",
    'is_open': True,
    'members': [
        ('SW radiation', 'Shortwave solar spectral irradiance.'),
        ('precipitating energetic particles', 'Precipitating energetic particles from the sun (predominantly protons) '
                            'and the magnetosphere (predominantly electrons) affect the ionization levels in the polar '
                            'middle and upper atmosphere, leading to significant changes of the chemical composition'),
        ('cosmic rays', 'Cosmic rays are the main source of ionization in the troposphere and lower stratosphere.')
    ]
}

ENUMERATIONS['top_insolation_solar_constant_type'] = {
    'description': "Time adaptation of the solar constant",
    'is_open': False,
    'members': [
        ('fixed', None),
        ('transient', None),
        ]
    }

ENUMERATIONS['top_insolation_orbital_parameters_type'] = {
    'description': "Time adaptation of orbital parameters",
    'is_open': False,
    'members': [
        ('fixed', None),
        ('transient', None),
        ]
    }

ENUMERATIONS['top_insolation_orbital_parameters_computation_method'] = {
    'description': "Method used for computing orbital parameters",
    'is_open': True,
    'members': [
        ('Berger 1978', None),
        ('Laskar 2004', None),
        ]
    }

