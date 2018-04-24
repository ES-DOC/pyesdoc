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
DESCRIPTION = 'Land surface vegetation'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Key properties of the land surface vegetation',
    'properties': [
        ('time_step', 'int', '1.1',
             'Time step of vegetation scheme in seconds'),                
        ('dynamic_vegetation', 'bool', '1.1',
             'Is there dynamic evolution of vegetation?'),
        ('tiling', 'l-str', '0.1',
             'Describe the vegetation tiling, if any.'),
        ('vegetation_representation', 'ENUM:vegetation_representation_types', '1.1',
             'Vegetation classification used'),
        ('vegetation_types', 'ENUM:vegetation_types', '0.N',
             'List of vegetation types in the classification, if any'),
        ('biome_types', 'ENUM:biome_types', '0.N',
             'List of biome types in the classification, if any'),
        ('vegetation_time_variation', 'ENUM:vegetation_time_variation', '1.1',
             'How the vegetation fractions in each tile are varying with time'),
        ('vegetation_map', 'str', '0.1',
             'If vegetation fractions are not dynamically updated , describe the vegetation map used (common name and reference, if possible)'),
        ('interception', 'bool', '1.1',
             'Is vegetation interception of rainwater represented?'),
        ('phenology', 'ENUM:phenology_methods', '1.1',
             'Treatment of vegetation phenology'),
        ('phenology_description', 'l-str', '0.1',
             'General description of the treatment of vegetation phenology'),
        ('leaf_area_index', 'ENUM:leaf_area_index_methods', '1.1',
             'Treatment of vegetation leaf area index'),
        ('leaf_area_index_description', 'l-str', '0.1',
             'General description of the treatment of leaf area index'),
        ('biomass', 'ENUM:biomass_methods', '1.1',
             'Treatment of vegetation biomass '),
        ('biomass_description', 'l-str', '0.1',
             'General description of the treatment of vegetation biomass'),
        ('biogeography', 'ENUM:biogeography_methods', '1.1',
             'Treatment of vegetation biogeography'),
        ('biogeography_description', 'l-str', '0.1',
             'General description of the treatment of vegetation biogeography'),
        ('stomatal_resistance', 'ENUM:stomatal_resistance_methods', '1.N',
             'Specify what the vegetation stomatal resistance depends on'),
        ('stomatal_resistance_description', 'l-str', '0.1',
             'General description of the treatment of vegetation stomatal resistance'),
        ('prognostic_variables', 'cs-str', '1.1',
             'List the prognostic variables of the vegetation scheme'),

    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['phenology_methods'] = {
    'description': 'Treatment of vegetation phenology',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic (vegetation map)', None),
        ]
    }

ENUMERATIONS['leaf_area_index_methods'] = {
    'description': 'Treatment of vegetation leaf area index',
    'is_open': True,
    'members': [
        ('prescribed', None),
        ('prognostic', None),
        ('diagnostic', None),
        ]
    }

ENUMERATIONS['biomass_methods'] = {
    'description': 'Treatment of vegetation biomass',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
        ]
    }

ENUMERATIONS['biogeography_methods'] = {
    'description': 'Treatment of vegetation biogeography',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
        ]
    }

ENUMERATIONS['stomatal_resistance_methods'] = {
    'description': 'Dependancies of vegetation stomatal resistance',
    'is_open': True,
    'members': [
        ('light', None),
        ('temperature', None),
        ('water availability', None),
        ('CO2', None),
        ('O3', None),
        ]
    }

ENUMERATIONS['biome_types'] = {
    'description': 'Biome type in the classification',
    'is_open': True,
    'members': [
        ('evergreen needleleaf forest', None),
        ('evergreen broadleaf forest', None),
        ('deciduous needleleaf forest', None),
        ('deciduous broadleaf forest', None),
        ('mixed forest', None),
        ('woodland', None),
        ('wooded grassland', None),
        ('closed shrubland', None),
        ('opne shrubland', None),
        ('grassland', None),
        ('cropland', None),
        ('wetlands', None),
        ]
    }

ENUMERATIONS['vegetation_types'] = {
    'description': 'Vegetation type in the classification',
    'is_open': True,
    'members': [
        ('broadleaf tree', None),
        ('needleleaf tree', None),
        ('C3 grass', None),
        ('C4 grass', None),
        ('vegetated', None),
        ]
    }

ENUMERATIONS['vegetation_representation_types'] = {
    'description': 'Vegetation classification used',
    'is_open': True,
    'members': [
        ('vegetation types', None),
        ('biome types', None),
        ]
    }

ENUMERATIONS['vegetation_time_variation'] = {
    'description': 'How the vegetation fraction in each tile are varying with time',
    'is_open': True,
    'members': [
        ('fixed (not varying)', None),
        ('prescribed (varying from files)', None),
        ('dynamical (varying from simulation)', None),
    ]
}
