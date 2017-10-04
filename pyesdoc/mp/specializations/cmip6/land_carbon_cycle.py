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
DESCRIPTION = 'Land surface carbon cycle'

# --------------------------------------------------------------------
# CARBON CYCLE: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Properties of land surface carbon cycle',
    'properties': [
        ('tiling', 'str', '0.1',
             'Describe the carbon cycle tiling, if any.'),
        ('time_step', 'int', '1.1',
             'Time step of carbon cycle in seconds'),
        ('anthropogenic_carbon', 'ENUM:anthropogenic_carbon_methods', '0.N',
             'Describe the treament of the anthropogenic carbon pool'),
        ('prognostic_variables', 'str', '1.1',
             'List the prognostic variables of the carbon scheme'),

    ]
}

# --------------------------------------------------------------------
# CARBON CYCLE: process
# --------------------------------------------------------------------
DETAILS['vegetation'] = {
    'description': 'TODO',
    'properties' : [ 
        ('number_of_carbon_pools', 'int', '1.1',
             'Enter the number of carbon pools used'),
        ('carbon_pools', 'str', '0.1',
             'List the carbon pools used'),
        ('forest_stand_dynamics', 'str', '0.1',
             'Describe the treatment of forest stand dyanmics'),
    ],
    'detail_sets': [
        'photosynthesis',
        'autotrophic_respiration',
        'allocation',
        'phenology',
        'mortality',
    ]
}

DETAILS['vegetation:photosynthesis'] = {
    'description': 'TODO',
    'properties' : [
        ('method', 'str', '0.1',
            'Describe the general method used for photosynthesis (e.g. type of photosynthesis, distinction between C3 and C4 grasses, Nitrogen depencence, etc.)',)
    ]
}

DETAILS['vegetation:autotrophic_respiration'] = {
    'description': 'TODO',
    'properties' : [
        ('maintainance_respiration', 'str', '0.1',
            'Describe the general method used for maintainence respiration'),
        ('growth_respiration', 'str', '0.1',
            'Describe the general method used for growth respiration'),
        ]
    }

DETAILS['vegetation:allocation'] = {
    'description': 'TODO',
    'properties' : [
        ('method', 'str', '1.1',
             'Describe the general principle behind the allocation scheme'),
        ('allocation_bins', 'ENUM:allocation_bin_types', '1.1',
            'Specify distinct carbon bins used in allocation'),
        ('allocation_fractions', 'ENUM:allocation_fraction_types', '1.1',
            'Describe how the fractions of allocation are calculated'),
        ]
    }

DETAILS['vegetation:phenology'] = {
    'description': 'TODO',
    'properties' : [
        ('method', 'str', '1.1',
             'Describe the general principle behind the phenology scheme'),
    ]
}

DETAILS['vegetation:mortality'] = {
    'description': 'TODO',
    'properties' : [
        ('method', 'str', '1.1',
             'Describe the general principle behind the mortality scheme'),
    ]
}

# --------------------------------------------------------------------
# CARBON CYCLE: process
# --------------------------------------------------------------------
DETAILS['litter'] = {
    'description': 'TODO',
    'properties' : [
        ('number_of_carbon_pools', 'int', '1.1',
             'Enter the number of carbon pools used'),
        ('carbon_pools', 'str', '0.1',
             'List the carbon pools used'),
        ('decomposition', 'str', '0.1',
             'List the decomposition methods used'),
        ('method', 'str', '0.1',
             'List the general method used'),
    ]
}

# --------------------------------------------------------------------
# CARBON CYCLE: process
# --------------------------------------------------------------------
DETAILS['soil'] = {
    'description': 'TODO',
    'properties' : [
        ('number_of_carbon_pools', 'int', '1.1',
             'Enter the number of carbon pools used'),
        ('carbon_pools', 'str', '0.1',
             'List the carbon pools used'),
        ('decomposition', 'str', '0.1',
             'List the decomposition methods used'),
        ('method', 'str', '0.1',
             'List the general method used'),
    ]
}


# --------------------------------------------------------------------
# CARBON CYCLE: process
# --------------------------------------------------------------------
DETAILS['permafrost_carbon'] = {
    'description': 'TODO',
    'properties' : [
        ('is_permafrost_included', 'bool', '1.1',
             'Is permafrost included?'),
        ('emitted_greenhouse_gases', 'str', '0.1',
             'List the GHGs emitted'),
        ('decomposition', 'str', '0.1',
             'List the decomposition methods used'),
        ('impact_on_soil_properties', 'str', '0.1',
             'Describe the impact of permafrost on soil properties'),
    ]
}

# --------------------------------------------------------------------
# CARBON CYCLE: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['anthropogenic_carbon_methods'] = {
    'description': 'Treatment of the anthropogenic carbn pool',
    'is_open': True,
    'members': [
        ('grand slam protocol', None),
        ('residence time', None),
        ('decay time', None),
    ]
}

ENUMERATIONS['allocation_bin_types'] = {
    'description': 'Specify the allocation of vegetation carbon bins',
    'is_open': True,
    'members': [
        ('leaves + stems + roots', None),
        ('leaves + stems + roots (leafy + woody)', None),
        ('leaves + fine roots + coarse roots + stems', None),
        ('whole plant (no distinction)', None),
        ]
    }

ENUMERATIONS['allocation_fraction_types'] = {
    'description': 'Describe how the fractions of allocation are calculated',
    'is_open': True,
    'members': [
        ('fixed', None),
        ('function of vegetation type', None),
        ('function of plant allometry', None),
        ('explicitly calculated', None),
    ]
}
