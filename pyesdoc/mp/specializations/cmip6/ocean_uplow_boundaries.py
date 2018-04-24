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
DESCRIPTION = 'Ocean upper / lower boundaries'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel:free_surface'] = {
    'description': 'Properties of free surface in ocean',
    'properties': [
        ('scheme', 'ENUM:free_surface_types', '1.1',
            'Free surface scheme in ocean'),
        ('embeded_seaice', 'bool', '1.1',
            'Is the sea-ice embeded in the ocean model (instead of levitating) ?'),
        ]
    }

DETAILS['toplevel:bottom_boundary_layer'] = {
    'description': 'Properties of bottom boundary layer in ocean',
    'properties': [
        ('overview','l-str','1.1',
            'Overview of bottom boundary layer in ocean'),
        ('type_of_bbl', 'ENUM:bottom_bl_types', '1.1',
            'Type of bottom boundary layer in ocean'),
        ('lateral_mixing_coef', 'int', '0.1',
            'If bottom BL is diffusive, specify value of lateral mixing coefficient (in m2/s)'),
        ('sill_overflow', 'l-str', '1.1',
            'Describe any specific treatment of sill overflows')
        ]
    }

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['free_surface_types'] = {
    'description': 'Type of free surface in ocean',
    'is_open': True,
    'members': [
        ('Linear implicit', None),
        ('Linear filtered', None),
        ('Linear semi-explicit', None),
        ('Non-linear implicit', None),
        ('Non-linear filtered', None),
        ('Non-linear semi-explicit', None),
        ('Fully explicit', None),
        ]
    }

ENUMERATIONS['bottom_bl_types'] = {
    'description': 'Type of bottom boundary layer in ocean',
    'is_open': True,
    'members': [
        ('Diffusive', None),
        ('Acvective', None)
        ]
    }
