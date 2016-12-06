"""A realm process sepecialization.

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
# PROCESS: DESCRIPTION
#
# Scientific context of the process
# --------------------------------------------------------------------
DESCRIPTION = 'Properties of ocean upper and lower boundaries'

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# Sets of details for the process
# --------------------------------------------------------------------
DETAILS = OrderedDict()

DETAILS['free_surface'] = {
    'description': 'Properties of free surface in ocean',
    'properties': [
        ('scheme', 'ENUM:free_surface_types', '1.1',
            'Free surface scheme in ocean'),
        ('ocean_embeded_seaice', 'bool', '1.1',
            'Is the sea-ice embeded in the ocean model (instead of levitating) ?'),
     ]
}

DETAILS['bottom_boundary_layer'] = {
    'description': 'Properties of bottom boundary layer in ocean',
    'properties': [
        ('type', 'ENUM:bottom_bl_types', '1.1',
            'Type of bottom boundary layer in ocean'),
        ('ocean_bbl_lateral_mixing_coef', 'int', '0.1',
            'If bottom BL is diffusive, specify value of lateral mixing coefficient (in m2/s)'),
        ('ocean_sill_overflow', 'str', '1.1',
            'Describe any specific treatment of sill overflows')
     ]
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['free_surface_types'] = {
    'description': 'Type of free surface in ocean',
    'is_open': True,
    'members': [
        ('Linear implicit', None),
        ('Linear filtered', None),
        ('Linear semi-explicit', None),
        ('Non-linear implicit', None),
        ('Non-linear filtered', None),
        ('Non-linear semi-explicit', None)
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
