"""A grid specialization.

For further information goto http://wordpress.es-doc.org/cordex-model-specializations.

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
DESCRIPTION = 'Aerosol grid'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Type of grid in the aerosol scheme',
    'properties': [
        ('matches_atmosphere_grid', 'bool', '1.1',
            ' Does the atmospheric aerosol grid match the atmosphere grid?'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: RESOLUTION: The resolution of the grid.
# --------------------------------------------------------------------
DETAILS['resolution'] = {
    'description': 'Resolution in the atmospheric aerosol grid',
    'properties': [
        ('name', 'str', '1.1',
             "This is a string usually used by the modelling group to describe the resolution of this grid, e.g. ORCA025, N512L180, T512L70 etc."),
        ('canonical_horizontal_resolution', 'str', '0.1',
             "Expression quoted for gross comparisons of resolution, e.g. 50km or 0.1 degrees etc."),
        ('number_of_horizontal_gridpoints', 'int', '0.1',
             "Total number of horizontal (XY) points (or degrees of freedom) on computational grid."),
        ('number_of_vertical_levels', 'int', '0.1',
             "Number of vertical levels resolved on computational grid."),
        ('is_adaptive_grid', 'bool', '1.1',
             "Set to true if grid resolution changes during execution."),
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
