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
DESCRIPTION = 'Land ice shelves'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'TODO',
    'properties': [
        ('adaptive_grid', 'bool', '1.1',
             'Is an adative grid being used?'),    
        ('resolution_limit', 'float', '0.1',
             'If an adative grid is being used, what is the limit of the resolution (in metres)'),    
        ('basal_melting', 'str', '1.1',
            'Describe the land ice shelf basal melting scheme'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Mass Balance
# --------------------------------------------------------------------
DETAILS['mass_balance'] = {
    'description': 'TODO',
    'properties': [
        ('calculated_in_atmosphere', 'bool', '1.1',
             'Is the ice shelf mass balance calculated in the atmosphere component?'),        
        ('ablation_calculation', 'ENUM:ablation_calculation_types', '1.1',
             'If mass balance is calculated in land ice model, the type of scheme used to calcualte ablation in the ice shelf mass balance'),
        ('downscaling_technique', 'str', '1.1',
             'If mass balance is calculated in land ice model, describe how the atmospheric variables are used in the mass balance calculations'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Dynamics
# --------------------------------------------------------------------
DETAILS['dynamics'] = {
    'description': 'TODO',
    'properties': [
        ('coupling_wth_ocean', 'str', '1.1',
             'Describe the coupling method between the land ice shelf and ocean'),
    ],
    'detail_sets': [
        'model_numerics',
    ]
}

DETAILS['dynamics:model_numerics'] = {
    'description': 'TODO',
    'properties': [
        ('timestep', 'int', '1.1',
             'Timestep (in seconds) of the land ice shelf scheme',),        
        ('uses_ocean_timestep', 'bool', '1.1',
             'Is the timestep the same as land surface timestep?'),
        ('uses_land_surface_timestep', 'bool', '1.1',
             'Is the timestep the same as land surface timestep?'),
        ('approximation', 'ENUM:approximation_types', '1.1',
            'Approximation type used in modelling ice shelf dynamics'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Snow treatment
# --------------------------------------------------------------------
DETAILS['snow_treatment'] = {
    'description': 'TODO',
    'properties': [
        ('calculated_in_atmosphere', 'bool', '1.1',
             'Is the ice shelf snow calculated in the atmosphere/land surface components?'),
        ('subgrid_hipsometry', 'str', '0.1',
             'Describe any subgrid-scale hipsometry in land ice shelf snow'),
        ('number_of_snow_layers', 'int', '0.1',
             'If mass balance is calculated in land ice model, how many layers in the ice shelf snow model?'),
        ('prognostic_variables', 'ENUM:snow_prognostic_variables', '0.N',
             'If mass balance is calculated in land ice model, list the prognostic variables the ice shelf snow model'),
        ('processes', 'ENUM:ice_shelf_snow_processes', '0.N',
             'If mass balance is calculated in land ice model, describe processes describing snow on ice shelves'),
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['bottom_types'] = {
    'description': 'TODO',
    'is_open': True,
    'members': [
        ('basal melting', None),
    ]
}

ENUMERATIONS['ablation_calculation_types'] = {
    'description': 'Type of scheme used to model ice shelf ablation',
    'is_open': True,
    'members': [
        ('Energy balance model', None),
        ('PDD', 'positive degree days'),
    ]
}

ENUMERATIONS['approximation_types'] = {
    'description': 'Approximation type used in modelling ice shelf dynamics',
    'is_open': True,
    'members': [
        ('SIA', None),
        ('SAA', None),
        ('full stokes', None),
        ]
    }

ENUMERATIONS['ice_shelf_snow_methods'] = {
    'description': 'Treatment of ice shelf snow',
    'is_open': True,
    'members': [
        ('same as snow in land surface', None),
        ('different from snow in land surface', None),
    ]
}

ENUMERATIONS['snow_prognostic_variables'] = {
    'description': 'Prognostic variables the ice shelf snow model',
    'is_open': True,
    'members': [
        ('snow albedo', None),
        ('snow density', None),
        ('snow water equivalent', None),
        ('snow heat content', None),
        ('snow temperature', None),
        ('snow liquid water content', None),
    ]
}

ENUMERATIONS['ice_shelf_snow_processes'] = {
    'description': 'Processes describing snow on ice shelves',
    'is_open': True,
    'members': [
        ('snow melting', None),
        ('snow refreezing', None),
        ('blowing snow', None),
    ]
}
