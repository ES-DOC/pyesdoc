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
DESCRIPTION = 'Land surface energy balance'

# --------------------------------------------------------------------
# ENERGY BALANCE: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'General properties in land surface energy balance scheme',
    'properties': [
        ('tiling', 'str', '0.1',
             'Describe the energy balance tiling, if any.'),        
        ('number_of_surface_temperature', 'int', '1.1',
            'The numnber of surface temperatures used'),
        ('evaporation_formulation', 'ENUM:evaporation_formulation_types', '1.1',
             'Specify the formulation method for land surface evaporation'),
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
