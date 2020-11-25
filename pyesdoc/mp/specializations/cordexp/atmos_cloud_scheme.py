"""

A realm process specialization.

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
DESCRIPTION = 'Characteristics of the cloud scheme'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': "Top level cloud scheme process properties",
    'properties': [
        ('scheme_type', 'ENUM:cloud_scheme_type', '1.N',
            'Describes the type(s) of cloud scheme: prognostic, diagnostic, other.'),
        ('uses_separate_treatment', 'str', '1.1',
            'Description for when different cloud schemes are used \
            for different types of clouds e.g. convective, stratiform and boundary layer)'),
        ('processes', 'ENUM:processes_attributes', '1.N',
            'Processes included in the cloud scheme'),
        ('prognostic_variables', 'ENUM:prognostic_vars', '0.N',
            'List the prognostic variables used by the cloud scheme, if applicable.'),
        ('atmos_coupling', 'ENUM:atmos_cloud_coupling', '0.N',
            'Atmosphere components that are linked to the cloud scheme'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: optical_cloud_properties
# --------------------------------------------------------------------
DETAILS['optical_cloud_properties'] = {
    'description': "Optical cloud properties",
    'properties': [
        ('cloud_overlap_method', 'ENUM:cloud_overlap_method', '0.1',
            'Method for taking into account overlapping of cloud layers'),
        ('cloud_inhomogeneity', 'str', '0.1',
            'Method for taking into account cloud inhomogeneity')
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: sub_grid_scale_water_distribution
# --------------------------------------------------------------------
DETAILS['sub_grid_scale_water_distribution'] = {
    'description': 'Sub-grid scale water distribution',
    'properties': [
        ('type', 'ENUM:sub_grid_scale_h2o_distribution_type', '1.1',
            'Sub-grid scale water distribution type'),
        ('function_name', 'str', '1.1',
            'Sub-grid scale water distribution function name'),
        ('function_order', 'int', '1.1',
            'Sub-grid scale water distribution function type'),
        ('convection_coupling', 'ENUM:sub_grid_scale_h2o_distribution_convection', '1.N',
            'Sub-grid scale water distribution coupling with convection'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: sub_grid_scale_ice_distribution
# --------------------------------------------------------------------
DETAILS['sub_grid_scale_ice_distribution'] = {
    'description': 'Sub-grid scale ice distribution',
    'properties': [
        ('type', 'ENUM:sub_grid_scale_h2o_distribution_type', '1.1',
            'Sub-grid scale ice distribution type'),
        ('function_name', 'str', '1.1',
            'Sub-grid scale ice distribution function name'),
        ('function_order', 'int', '1.1',
            'Sub-grid scale ice distribution function type'),
        ('convection_coupling', 'ENUM:sub_grid_scale_h2o_distribution_convection', '1.N',
            'Sub-grid scale ice distribution coupling with convection'),
        ]
    }
# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['sub_grid_scale_h2o_distribution_type'] = {
    'description': 'Approach used for cloud H2O content and fractional cloud cover',
    'is_open': False,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
        ]
    }

ENUMERATIONS['sub_grid_scale_h2o_distribution_convection'] = {
    'description': 'Type(s) of convection that the formation of clouds is coupled with',
    'is_open': False,
    'members': [
        ('coupled with deep', None),
        ('coupled with shallow', None),
        ('not coupled with convection', None),
        ]
    }

ENUMERATIONS['atmos_cloud_coupling'] = {
    'description': 'Atmosphere components that are linked to the cloud scheme',
    'is_open': False,
    'members': [
        ('atmosphere_radiation', None),
        ('atmosphere_microphysics_precipitation', None),
        ('atmosphere_turbulence_convection', None),
        ('atmosphere_gravity_waves', None),
        ('atmosphere_natural_forcing', None),
        ('atmosphere_observation_simulation', None)
    ]
}

ENUMERATIONS['cloud_overlap_method'] = {
    'description': 'Cloud scheme cloud overlap method',
    'is_open': True,
    'members': [
        ('random', None),
        ('maximum', None),
        ('maximum-random', 'combination of maximum and random overlap between clouds'),
        ('exponential', None),
        ]
    }

ENUMERATIONS['processes_attributes'] = {
    'description': 'Processes included in the cloud scheme.',
    'is_open': True,
    'members': [
        ('entrainment', None),
        ('detrainment', None),
        ('bulk cloud', None),
        ]
    }

ENUMERATIONS['prognostic_vars'] = {
    'description': 'Prognostic variables included in the cloud scheme.',
    'is_open': True,
    'members': [
        ('cloud amount', None),
        ('liquid', None),
        ('ice', None),
        ('rain', None),
        ('snow', None),
        ('cloud droplet number concentration', 'To document the use of two-moment cloud microphysics schemes'),
        ('ice crystal number concentration', 'To document the use of two-moment cloud microphysics schemes'),
        ]
    }

ENUMERATIONS['cloud_scheme_type'] = {
    'description': 'Type of cloud scheme.',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
        ]
    }