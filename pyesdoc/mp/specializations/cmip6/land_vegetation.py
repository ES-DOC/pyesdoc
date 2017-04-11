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
DESCRIPTION = 'Land surface soil'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Key properties of the land surface vegetation',
    'properties': [
        ('tiling', 'str', '0.1',
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
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Soil map
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'TODO',
    'properties': [
        ('description', 'str', '1.1',
             'General description of soil map'),
        ('structure', 'str', '1.1',
             'Describe the soil map structure'),
        ('texture', 'str', '1.1',
             'Describe the soil map texture'),
        ('albedo', 'str', '1.1',
             'Describe the soil map albedo'),
        ('water_table', 'str', '1.1',
             'Describe the soil map water_table'),
        ('soil_depth', 'str', '1.1',
             'Describe the soil map total soil depth'),
    ],
    'detail_sets': [
        'methods',
    ],
}

DETAILS['toplevel:methods'] = {
    'description': 'TODO',
    'properties': [
        ('phenology', 'ENUM:phenology_methods', '1.1',
             'Treatment of vegetation phenology'),
        ('phenology_description', 'str', '0.1',
             'General description of the treatment of vegetation phenology'),
        ('leaf_area_index', 'ENUM:leaf_area_index_methods', '1.1',
             'Treatment of vegetation leaf area index'),
        ('leaf_area_index_description', 'str', '0.1',
             'General description of the treatment of leaf area index'),
        ('biomass', 'ENUM:biomass_methods', '1.1',
             'Treatment of vegetation biomass '),
        ('biomass_description', 'str', '0.1',
             'General description of the treatment of vegetation biomass'),
        ('biogeography', 'ENUM:biogeography_methods', '1.1',
             'Treatment of vegetation biogeography'),
        ('biogeography_description', 'str', '0.1',
             'General description of the treatment of vegetation biogeography'),
        ('stomatal_resistance', 'ENUM:stomatal_resistance_methods', '1.N',
             'Specify the dependancies on vegetation stomatal resistance'),
        ('stomatal_resistance_description', 'str', '0.1',
             'General description of the treatment of vegetation stomatal resistance'),
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
    'description': 'Dependancies on vegetation stomatal resistance',
    'is_open': True,
    'members': [
        ('light', None),
        ('temperature', None),
        ('water availability', None),
        ('CO2', None),
        ('O3', None),
        ]
    }
