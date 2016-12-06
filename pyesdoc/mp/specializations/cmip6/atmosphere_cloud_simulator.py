"""

A realm process sepecialization.

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
DESCRIPTION = 'Characteristics of the cloud simulator'

# --------------------------------------------------------------------
# SUB-PROCESSES
# --------------------------------------------------------------------
DETAILS['isscp_attributes'] = {
    'description': 'ISSCP Characteristics',
    'properties': [
        ('top_height', 'ENUM:isscp_top_height', '1.N',
            'Cloud simulator ISSCP top height'),
        ('top_height_direction', 'ENUM:isscp_top_height_direction', '1.1',
            'Cloud simulator ISSCP top height direction'),
        ]
    }

DETAILS['cosp_attributes'] = {
    'description': 'CFMIP Observational Simulator Package attributes',
    'properties': [
        ('run_configuration', 'ENUM:cosp_run_configuration', '1.1',
            'Cloud simulator COSP run configuration'),
        ('number_of_grid_points', 'int', '1.1',
            'Cloud simulator COSP number of grid points'),
        ('number_of_columns', 'int', '1.1',
            'Cloud simulator COSP number of cloumns'),
        ('number_of_levels', 'int', '1.1',
             'Cloud simulator COSP number of levels'),
        ]
    }

DETAILS['radar_inputs'] = {
    'description': 'Characteristics of the cloud radar simulator',
    'properties': [
        ('frequency', 'float', '1.1',
         'Cloud simulator radar frequency (Hz)'),
        ('type', 'ENUM:inputs_radar_type', '1.1',
         'Cloud simulator radar type'),
        ('gas_absorption', 'bool', '1.1',
         'Cloud simulator radar uses gas absorption'),
        ('effective_radius', 'bool', '1.1',
         'Cloud simulator radar uses effective radius'),
        ]
    }

DETAILS['lidar_inputs'] = {
    'description': 'Characteristics of the cloud lidar simulator',
    'properties': [
        ('ice_types', 'ENUM:inputs_lidar_ice_type', '1.1',
         'Cloud simulator lidar ice type'),
        ('overlap', 'ENUM:inputs_lidar_overlap', '1.N',
         'Cloud simulator lidar overlap'),
        ]
    }

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['isscp_top_height'] = {
    'description': 'Cloud top height management',
    'is_open': True,
    'members': [
        ('no adjustment', None),
        ('IR brightness', None),
        ('visible optical depth', None),
        ]
    }

ENUMERATIONS['isscp_top_height_direction'] = {
    'description': 'Direction for finding the radiance determined cloud-top pressure. '
                   'Atmosphere pressure level with interpolated temperature equal to '
                   'the radiance determined cloud-top pressure.',
    'is_open': True,
    'members': [
        ('lowest altitude level', None),
        ('highest altitude level', None),
        ]
    }

ENUMERATIONS['cosp_run_configuration'] = {
    'description': 'Method used to run the CFMIP Observational Simulator Package',
    'is_open': True,
    'members': [
        ('Inline', None),
        ('Offline', None),
        ]
    }

ENUMERATIONS['inputs_radar_type'] = {
    'description': 'Type of radar',
    'is_open': True,
    'members': [
        ('surface', None),
        ('space borne', None),
        ]
    }

ENUMERATIONS['inputs_lidar_ice_type'] = {
    'description': 'Ice particle shape in lidar calculations',
    'is_open': True,
    'members': [
        ('ice spheres', None),
        ('ice non-spherical', None),
        ]
    }

ENUMERATIONS['inputs_lidar_overlap'] = {
    'description': 'lidar overlap type',
    'is_open': True,
    'members': [
        ('max', None),
        ('random', None),
        ]
    }
