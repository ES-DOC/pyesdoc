"""A process specialization.

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
DESCRIPTION = 'Atmospheric chemistry emissions'

# --------------------------------------------------------------------
# SUB-PROCESS: Surface emissions
# --------------------------------------------------------------------
DETAILS['surface_emissions'] = {
    'description': '',
    'properties': [
        ('sources', 'ENUM:surface_source_types', '0.N',
             'Sources of the chemical species emitted at the surface that are taken into account in the emissions scheme'),
        ('method', 'ENUM:emissions_methods', '0.N',
            'Methods used to define chemical species emitted directly into model layers above the surface (several methods allowed because the different species may not use the same method).'),
        ('prescribed_climatology_emitted_species', 'cs-str', '0.1',
             'List of chemical species emitted at the surface and prescribed via a climatology, and the nature of the climatology (E.g. CO (monthly), C2H6 (constant))'),
        ('prescribed_spatially_uniform_emitted_species', 'cs-str', '0.1',
             'List of chemical species emitted at the surface and prescribed as spatially uniform'),
        ('interactive_emitted_species', 'cs-str', '0.1',
             'List of chemical species emitted at the surface and specified via an interactive method'),
        ('other_emitted_species', 'cs-str', '0.1',
             'List of chemical species emitted at the surface and specified via any other method'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Atmospheric emissions
# --------------------------------------------------------------------
DETAILS['atmospheric_emissions'] = {
    'description': 'TO DO',
    'properties': [
        ('sources', 'ENUM:atmospheric_source_types', '0.N',
             'Sources of chemical species emitted in the atmosphere that are taken into account in the emissions scheme.'),
        ('method', 'ENUM:emissions_methods', '0.N',
            'Methods used to define the chemical species emitted in the atmosphere (several methods allowed because the different species may not use the same method).'),
        ('prescribed_climatology_emitted_species', 'cs-str', '0.1',
             'List of chemical species emitted in the atmosphere and prescribed via a climatology (E.g. CO (monthly), C2H6 (constant))'),
        ('prescribed_spatially_uniform_emitted_species', 'cs-str', '0.1',
             'List of chemical species emitted in the atmosphere and prescribed as spatially uniform'),
        ('interactive_emitted_species', 'cs-str', '0.1',
             'List of chemical species emitted in the atmosphere and specified via an interactive method'),
        ('other_emitted_species', 'cs-str', '0.1',
             'List of chemical species emitted in the atmosphere and specified via an "other method"'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Concentrations
# --------------------------------------------------------------------
DETAILS['concentrations'] = {
    'description': 'TO DO',
    'properties': [
        ('prescribed_lower_boundary', 'cs-str', '0.1',
            'List of species prescribed at the lower boundary.'),
        ('prescribed_upper_boundary', 'cs-str', '0.1',
            'List of species prescribed at the upper boundary.'),
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['prescribed_climatology_type'] = {
    'description': 'Specify the climatology type for chemical emissions',
    'is_open': False,
    'members': [
        ('Constant', None),
        ('Interannual', None),
        ('Annual', None),
        ('Monthly', None),
        ('Daily', None),
        ]
    }

ENUMERATIONS['surface_source_types'] = {
    'description':'Sources of the chemical species emitted at the surface that are taken into account in the emissions scheme',
    'is_open': True,
    'members':[
        ('Vegetation', None),
        ('Soil', None),
        ('Sea surface', None),
        ('Anthropogenic', None),
        ('Biomass burning', None),
    ]
}

ENUMERATIONS['atmospheric_source_types'] = {
    'description':'Sources of the chemical species emitted in the atmosphere that are taken into account in the emissions scheme',
    'is_open': True,
    'members':[
        ('Aircraft', None),
        ('Biomass burning', None),
        ('Lightning', None),
        ('Volcanos', None),
    ]
}

ENUMERATIONS['emissions_methods'] = {
    'description': 'Method used to define chemical species emitted (several methods allowed because the different species may not use the same method).',
    'is_open': True,
    'members':[
        ('Climatology', None),
        ('Spatially uniform mixing ratio', None),
        ('Spatially uniform concentration', None),
        ('Interactive', None),
    ]
}
