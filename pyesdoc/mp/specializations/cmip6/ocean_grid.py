"""A realm grid sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""

# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

# --------------------------------------------------------------------
# CONTACT
#
# Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Eric Guilyardi'

# --------------------------------------------------------------------
# AUTHORS
#
# Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Eric Guilyardi'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# GRID: DESCRIPTION
#
# Scientific context of the grid
# --------------------------------------------------------------------
DESCRIPTION = 'Ocean grid and discretisation'

# --------------------------------------------------------------------
# GRID: DETAILS
#
# Sets of details for the grid
# --------------------------------------------------------------------
DETAILS = OrderedDict()

DETAILS['vertical_grid'] = {
    'description': 'Properties of vertical coordinate in ocean',
    'properties': [
        ('number_of_levels', 'int', '1.1',
            'Number of vertical levels'),
        ]
}

DETAILS['horizontal_grid'] = {
    'description': 'Properties of H coordinate in ocean',
    'properties': [
        ('horizontal_grid_type', 'ENUM:horizontal_grid_types', '1.1',
            'Horizontal grid type'),
        ('number_of_xy_gridpoints', 'int', '0.1',
            'Total number of horizontal points on computational grid'),
        ]
}

# --------------------------------------------------------------------
# DISCRETISATION
#
# Description of the numerics of the discretisation
# --------------------------------------------------------------------
DISCRETISATION = OrderedDict()

DISCRETISATION['discretisation'] = {
    'description': 'Type of discretisation scheme in ocean',
    'details': [
        'horizontal',
        'vertical'
        ]
}

# --------------------------------------------------------------------
# DISCRETISATION: DETAILS
#
# Sets of details for the discretisation
# --------------------------------------------------------------------
DISCRETISATION_DETAILS = OrderedDict()

DISCRETISATION_DETAILS['vertical'] = {
    'description': 'Properties of vertical coordinate in ocean',
    'properties': [
        ('coordinates', 'ENUM:vertical_coordinate_types', '1.1',
            'Type of vertical coordinates in ocean'),
        ('partial_steps', 'bool', '1.1',
            'Using partial steps with Z or Z* vertical coordinate in ocean ?'),
        ]
}

DISCRETISATION_DETAILS['horizontal'] = {
    'description': 'Type of horizontal discretisation scheme in ocean',
    'properties': [
        ('scheme', 'ENUM:horizontal_scheme_types', '1.1',
            'Horizontal discretisation scheme in ocean'),
        ('pole_singularity_treatment', 'str', '1.1',
            'Describe how the North Pole singularity is treated (filter, pole rotation/displacement, artificial island, ...)'),
        ]
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['horizontal_grid_types'] = {
    'description': 'Types of horizonal grid in ocean',
    'is_open': True,
    'members': [
        ('Latlon', None),
        ('Rotated north pole', None),
        ('Two north poles (ORCA-style)', None)
        ]
}

ENUMERATIONS['horizontal_scheme_types'] = {
    'description': 'Types of horizonal scheme in ocean',
    'is_open': True,
    'members': [
        ('Finite difference / Arakawa B-grid', None),
        ('Finite difference / Arakawa C-grid', None),
        ('Finite difference / Arakawa E-grid', None),
        ('Finite volumes', None),
        ('Finite elements', None)
        ]
}

ENUMERATIONS['vertical_coordinate_types'] = {
    'description': 'Types of vertical coordinates in ocean',
    'is_open': True,
    'members': [
        ('Z-coordinate', None),
        ('Z*-coordinate', None),
        ('S-coordinate', None),
        ('Isopycnic - sigma 0', 'Density referenced to the surface'),
        ('Isopycnic - sigma 2', 'Density referenced to 2000 m'),
        ('Isopycnic - sigma 4', 'Density referenced to 4000 m'),
        ('Isopycnic - other', 'Other density-based coordinate'),
        ('Hybrid / Z+S', None),
        ('Hybrid / Z+isopycnic', None),
        ('Hybrid / ALE', None),
        ('Hybrid / other', None),
        ('Pressure referenced (P)', None),
        ('P*', None),
        ('Z**', None)
        ]
}
