"""A realm process sepecialization.

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
DESCRIPTION = 'Land surface snow'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Properties of land surface snow scheme',
    'properties': [
        ('tiling', 'l-str', '0.1',
             'Describe the snow tiling, if any.'),        
        ('number_of_snow_layers', 'int', '1.1',
             'The number of snow levels used in the land surface scheme/model'),
        ('density', 'ENUM:snow_density_methods', '1.1',
             'Description of the treatment of snow density'),
        ('water_equivalent', 'ENUM:snow_water_equivalent_methods', '1.1',
             'Description of the treatment of the snow water equivalent'),
        ('heat_content', 'ENUM:snow_heat_content_methods', '1.1',
             'Description of the treatment of the heat content of snow'),
        ('temperature', 'ENUM:snow_temperature_methods', '1.1',
             'Description of the treatment of snow temperature'),
        ('liquid_water_content', 'ENUM:snow_liquid_water_content_methods', '1.1',
             'Description of the treatment of snow liquid water'),
        ('snow_cover_fractions', 'ENUM:snow_cover_fraction_types', '1.N',
             'Specify cover fractions used in the surface snow scheme'),
        ('processes', 'ENUM:snow_processes', '1.N',
             'Snow related processes in the land surface scheme'),
        ('prognostic_variables', 'cs-str', '1.1',
             'List the prognostic variables of the snow scheme'),
    ]
}

DETAILS['snow_albedo'] = {
    'description': 'Snow albedo',
    'properties' : [
        ('type', 'ENUM:snow_albedo_type', '1.1',
            'Describe the treatment of snow-covered land albedo'),
        ('functions', 'ENUM:snow_albedo_function_types', '0.N',
             'Describe the function types if prognostic snow albedo'),
        ]
    }
# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['snow_albedo_type'] = {
    'description': 'Describe the treatment of snow-covered land albedo',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('prescribed', None),        
        ('constant', None),
    ]
}

ENUMERATIONS['snow_albedo_function_types'] = {
    'description': 'Describe the dependancies on snow albedo calculations',
    'is_open': True,
    'members': [
        ('vegetation type', None),
        ('snow age', None),        
        ('snow density', None),
        ('snow grain type', None),
        ('aerosol deposition', None),
    ]
}

ENUMERATIONS['snow_density_methods'] = {
    'description': 'Treatment of snow density',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('constant', None),
    ]
}

ENUMERATIONS['snow_water_equivalent_methods'] = {
    'description': 'Treatment of snow water equivalent',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
    ]
}

ENUMERATIONS['snow_heat_content_methods'] = {
    'description': 'Treatment of snow heat content',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
    ]
}

ENUMERATIONS['snow_temperature_methods'] = {
    'description': 'Treatment of snow temperature',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
    ]
}


ENUMERATIONS['snow_liquid_water_content_methods'] = {
    'description': 'Treatment of snow liquid water',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
    ]
}

ENUMERATIONS['snow_cover_fraction_types'] = {
    'description': 'Snow cover fraction types',
    'is_open': True,
    'members': [
        ('ground snow fraction', None),
        ('vegetation snow fraction', None),
    ]
}

ENUMERATIONS['snow_processes'] = {
    'description': 'Snow-related processes',
    'is_open': True,
    'members': [
        ('snow interception', None),
        ('snow melting', None),
        ('snow freezing', None),
        ('blowing snow', None),
    ]
}

