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
DESCRIPTION = 'Land surface grid'

# --------------------------------------------------------------------
# DISCRETISATION: Description of the numerics of the discretisation.
# --------------------------------------------------------------------
DETAILS['horizontal'] = {
    'description': 'The horizontal grid in the land surface',
    'properties': [
        ('description', 'l-str', '1.1',
             'Describe the general structure of the horizontal grid (not including any tiling)'),
        ('matches_atmosphere_grid', 'bool', '1.1',
             'Does the horizontal grid match the atmosphere?'),
        ]
    }

DETAILS['vertical'] = {
    'description': 'The vertical grid in the soil',
    'properties': [
        ('description', 'l-str', '1.1',
             'Describe the general structure of the  vertical grid in the soil (not including any tiling)'),       
        ('total_depth', 'int', '1.1',
             'The total depth of the soil (in metres)'),
    ]
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
