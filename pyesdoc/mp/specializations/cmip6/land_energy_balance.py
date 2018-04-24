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
DESCRIPTION = 'Land surface energy balance'

# --------------------------------------------------------------------
# ENERGY BALANCE: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'General properties in land surface energy balance scheme',
    'properties': [
        ('tiling', 'l-str', '0.1',
             'Describe the energy balance tiling, if any.'),        
        ('number_of_surface_temperatures', 'int', '1.1',
            'The maximum number of distinct surface temperatures in a grid cell  (for example, each subgrid tile may have its own temperature)'),
        ('evaporation', 'ENUM:evaporation_formulation_types', '1.N',
             'Specify the formulation method for land surface evaporation, from soil and vegetation'),
        ('processes', 'ENUM:process_types', '1.N',
             'Describe which processes are included in the energy balance scheme'),
        ]
    }

# --------------------------------------------------------------------
# ENERGY BALANCE: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['evaporation_formulation_types'] = {
    'description': 'Specify the formulation method for land surface evaporation',
    'is_open': True,
    'members': [
        ('alpha', None),
        ('beta', None),        
        ('combined', None),
        ('Monteith potential evaporation', None),
    ]
}

ENUMERATIONS['process_types'] = {
    'description': 'Processes which are included in the energy balance scheme',
    'is_open': True,
    'members': [
        ('transpiration', None),
    ]
}
