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
# CONTACT: Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Land surface albedo'

# --------------------------------------------------------------------
# ALBEDO: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'General properties in land surface albedo',
    'properties': [
        ('tiling', 'str', '0.1',
             'Describe the albedo tiling, if any.'),
    ],
}

DETAILS['snow_free_albedo'] = {
    'description': 'TODO',
    'properties' : [
        ('prognostic', 'bool', '1.1',
             'Is snow free albedo prognostic?'),
        ('functions', 'ENUM:snow_free_albedo_function_types', '0.N',
             'If prognostic, describe the dependancies on snow free albedo calculations'),
        ('direct_diffuse', 'ENUM:direct_diffuse_types', '0.1',
             'If prognostic, describe the distinction between direct and diffuse albedo'),
        ('number_of_wavelength_bands', 'int', '0.1',
             'If prognostic, enter the number of wavelength bands used'),
        ]
    }

DETAILS['snow_albedo'] = {
    'description': 'TODO',
    'properties' : [
        ('type', 'ENUM:snow_albedo_type', '1.1',
            'Describe the treatment of snow-covered land albedo'),
        ('functions', 'ENUM:snow_albedo_function_types', '0.N',
             'If prognostic, '),
        ]
    }

DETAILS['method'] = {
    'description': 'TODO',
    'properties':[
        ('phenology','ENUM:phenology_types', '1.1',
            'Description of the treatment of vegetation phenolo]gy'),
        ('leaf_area_index','ENUM:leaf_area_index_types', '1.1',
            'Describe the treatment of the leaf area index'),
        ('biomass','ENUM:biomass_types', '1.1',
            'Describe the treatment of vegetation biomass'),
        ('biogeography','ENUM:biogeography_types', '1.1',
            'Describe the treatment of vegatation biogeography'),
        ('stomatal_resistance','ENUM:stomatal_resistance_types', '1.N',
            'Specify the dependancies on vegetation stomatal resistance'),
    ]
}

# --------------------------------------------------------------------
# ALBEDO: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['snow_free_albedo_function_types'] = {
    'description': 'Describe the dependancies on snow free albedo calculations',
    'is_open': True,
    'members': [
        ('vegetation type', None),
        ('soil humidity', None),
        ('vegatation state', None),        
        ]
    }

ENUMERATIONS['direct_diffuse_types'] = {
    'description': 'Describe the distinction between direct and diffuse albedo',
    'is_open': True,
    'members': [
        ('distinction between direct and diffuse albedo', None),
        ('no distinction between direct and diffuse albedo', None),        
    ]
}

ENUMERATIONS['snow_albedo_type'] = {
    'description': 'Describe the treatment of snow-covered land albedo',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('prescribed', None),        
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

ENUMERATIONS['phenology_types'] = {
    'description': 'Description of the treatment of vegetation phenolo]gy',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic (vegetation map)', None),
        ]
}

ENUMERATIONS['leaf_area_index_types'] = {
    'description': 'Describe the treatment of the leaf area index',
    'is_open': True,
    'members': [
        ('prescribed', None),
        ('prognostic', None),
        ('diagnostic', None),
        ]
    }

ENUMERATIONS['biomass_types'] = {
    'description': 'Describe the treatment of vegetation biomass',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
        ]
    }

ENUMERATIONS['biogeography_types'] = {
    'description': 'Describe the treatment of vegatation biogeography',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
        ]
    }

ENUMERATIONS['stomatal_resistance_types'] = {
    'description': 'Specify the dependancies on vegetation stomatal resistance',
    'is_open': True,
    'members': [
        ('light', None),
        ('temperature', None),
        ('water availability', None),
        ('CO2', None),
        ('O3', None),
    ]
}
