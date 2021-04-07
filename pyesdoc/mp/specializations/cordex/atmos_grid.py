"""A realm grid specialization.

For further information goto http://es-doc.org/cordex-model-specializations.

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
DESCRIPTION = 'Atmosphere grid'

# --------------------------------------------------------------------
# DISCRETISATION: Description of the horizontal discretisation and numerics.
# --------------------------------------------------------------------
DETAILS['discretisation'] = {
    'description': 'Atmosphere grid discretisation',
    'properties': [
        ]
    }
    
DETAILS['discretisation:horizontal'] = {
    'description': 'Atmosphere discretisation in the horizontal',
    'properties': [
        ('coordinate_system', 'ENUM:horizontal_coordinate_system', '1.1',
            'Name of horizontal coordinate system/projection'),
        ('coordinate_system_details', 'str', '1.1',
             'Details of horizontal coordinate system/projection (e.g. rotated pole, longitude of central meridian, false easting, etc.)'),
        ('horizontal_resolution', 'str', '0.1',
             'Resolution (in deg or km)'),
        ('full_domain', 'str', '0.1',
             'Size of full domain (Nlon x Nlat)'),
        ('relaxation_zone', 'str', '1.1',
             'Lateral Boundary Relaxation Zone (type, relaxation function, number of grid points (west, south, east, north) and other details)'),
        ('inner_domain', 'str', '0.1',
             'Size of inner domain (Nlon x Nlat)'),                          
        ('scheme_type', 'ENUM:dynamical_core_discretisation_horizontal_type', '1.1',
            'Horizontal discretisation type'),
        ('scheme_method', 'ENUM:dynamical_core_discretisation_horizontal_method', '1.1',
            'Horizontal discretisation method'),
        ('scheme_order', 'ENUM:function_order', '1.1',
            'Horizontal discretisation function order'),
        ('horizontal_pole', 'ENUM:dynamical_core_discretisation_horizontal_pole', '0.1',
            'Horizontal discretisation pole singularity treatment'),
        ('grid_type', 'ENUM:grid_type', '1.1',
            'Horizontal grid type')
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
        ('hybrid pressure', None),
        ('vertically lagrangian', None),

    ]
}
# "Vertically-lagrangian hybrid-pressure"

ENUMERATIONS['function_order'] = {
    'description': 'Discretisation function order',
    'is_open': True,
    'members': [
        ('second', None),
        ('third', None),
        ('fourth', None),
        ]
    }

ENUMERATIONS['grid_type'] = {
    'description': 'Type of horizontal grid',
    'is_open': True,
    'members': [
        ('Gaussian', None),
        ('Latitude-Longitude', None),
        ('Cubed-Sphere', None),
        ('Icosahedral', None),
        ]
    }
    
ENUMERATIONS['horizontal_coordinate_system'] = {
    'description': 'Type of horizontal projection',
    'is_open': True,
    'members': [
        ('Rotated Polar', None),
        ('Lambert Conformal Conic', None),
        ('Others', None),
        ]
    }   
