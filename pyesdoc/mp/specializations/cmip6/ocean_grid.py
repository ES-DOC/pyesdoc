"""A grid specialization.

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
DESCRIPTION = 'Ocean grid'

# --------------------------------------------------------------------
# DISCRETISATION: Description of the numerics of the discretisation.
# --------------------------------------------------------------------
DETAILS['discretisation'] = {
    'description': 'Type of discretisation scheme in ocean'
    }

DETAILS['discretisation:vertical'] = {
    'description': 'Properties of vertical discretisation in ocean',
    'properties': [
        ('coordinates', 'ENUM:vertical_coordinate_types', '1.1',
            'Type of vertical coordinates in ocean'),
        ('partial_steps', 'bool', '1.1',
            'Using partial steps with Z or Z* vertical coordinate in ocean ?'),
        ]
    }

DETAILS['discretisation:horizontal'] = {
    'description': 'Type of horizontal discretisation scheme in ocean',
    'properties': [
        ('type', 'ENUM:horizontal_grid_types', '1.1',
            'Horizontal grid type'),
        ('staggering', 'ENUM:horizontal_staggering_types', '0.1',
            'Horizontal grid staggering type'),
        ('scheme', 'ENUM:horizontal_scheme_types', '1.1',
            'Horizontal discretisation scheme in ocean'),
        ]
    }

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['horizontal_grid_types'] = {
    'description': 'Types of horizonal grid in ocean',
    'is_open': True,
    'members': [
        ('Lat-lon', None),
        ('Rotated north pole', None),
        ('Two north poles (ORCA-style)', None)
        ]
    }

ENUMERATIONS['horizontal_scheme_types'] = {
    'description': 'Types of horizonal scheme in ocean',
    'is_open': True,
    'members': [
        ('Finite difference', None),
        ('Finite volumes', None),
        ('Finite elements', None),
        ('Unstructured grid', None)
        ]
    }

ENUMERATIONS['horizontal_staggering_types'] = {
    'description': 'Types of horizonal staggering in ocean',
    'is_open': True,
    'members': [
        ('Arakawa B-grid', None),
        ('Arakawa C-grid', None),
        ('Arakawa E-grid', None),
        ('N/a', None),
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
        ('Hybrid / other', None),
        ('Pressure referenced (P)', None),
        ('P*', None),
        ('Z**', None)
        ]
    }
