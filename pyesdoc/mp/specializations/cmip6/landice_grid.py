"""A realm grid sepecialization.

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
DESCRIPTION = 'Land ice grid'

# --------------------------------------------------------------------
# 
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Grid of land ice component',
    'properties': [
        ('adaptive_grid', 'bool', '1.1',
             'Is an adative grid being used?'),    
        ('base_resolution', 'float', '1.1',
            'The base resolution (in metres), before any adaption'),
        ('resolution_limit', 'float', '0.1',
             'If an adaptive grid is being used, what is the limit of the resolution (in metres)'),    
        ('projection', 'str', '1.1',
            'The projection of the land ice grid (e.g. albers_equal_area)'),
    ]
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
