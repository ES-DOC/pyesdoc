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
# CONTACT: Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Atmosphere grid'

# --------------------------------------------------------------------
# DISCRETISATION: Description of the horizontal discretization and numerics.
# --------------------------------------------------------------------
DETAILS['discretisation'] = {
    'description': 'Atmosphere grid discretisation',
    'properties': [],
    'detail_sets': [
        'horizontal',
        'vertical',
        ]
    }

DETAILS['discretisation:horizontal'] = {
    'description': 'Atmosphere discretisation in the horizontal',
    'properties': [
        ('scheme_type', 'ENUM:dynamical_core_discretisation_horizontal_type', '1.1',
            'Horizontal discretisation type'),
        ('scheme_method', 'ENUM:dynamical_core_discretisation_horizontal_method', '1.1',
            'Horizontal discretisation method'),
        ('scheme_order', 'int', '1.1',
            'Horizontal discretisation function order'),
        ('horizontal_pole', 'ENUM:dynamical_core_discretisation_horizontal_pole', '1.1',
            'Horizontal discretisation pole singularity treatment'),
        ]
    }

DETAILS['discretisation:vertical'] = {
    'description': 'Atmosphere discretisation in the vertical',
    'properties': [
        ('coordinate_type', 'ENUM:dynamical_core_discretisation_vertical_type', '1.N',
            'Type of vertical coordinate system'),
        ]
    }

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['dynamical_core_discretisation_horizontal_type'] = {
    'description': 'Type of horizontal discretisation scheme',
    'is_open': True,
    'members': [
        ('spectral', None),
        ('fixed grid', None),
        ]
    }

ENUMERATIONS['dynamical_core_discretisation_horizontal_method'] = {
    'description': 'If the scheme type is fixed grid, describe the scheme method for the horizontal discretisation scheme',
    'is_open': False,
    'members': [
        ('finite elements', None),
        ('finite volumes', None),
        ('finite difference', None),
        ('centered finite difference', None),
        ]
    }

ENUMERATIONS['dynamical_core_discretisation_horizontal_pole'] = {
    'description': 'Method used to handle the pole singularities',
    'is_open': True,
    'members': [
        ('filter', None),
        ('pole rotation', None),
        ('artificial island', None),
        ]
    }

ENUMERATIONS['dynamical_core_discretisation_vertical_type'] = {
    'description': 'Type of vertical coordinate system',
    'is_open': True,
    'members': [
        ('isobaric', 'vertical coordinate on pressure levels'),
        ('sigma', 'allows vertical coordinate to follow model terrain'),
        ('hybrid sigma-pressure', 'sigma system near terrain and isobaric above'),
    ]
}