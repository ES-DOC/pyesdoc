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
DESCRIPTION = 'Characteristics of the cloud scheme'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': "Top level cloud scheme process properties",
    'properties': [
        ('uses_separate_treatment', 'bool', '1.1',
            'Different cloud schemes for the different types of clouds (convective, stratiform and boundary layer clouds'),
        ('cloud_overlap_method', 'ENUM:cloud_overlap_method', '1.1',
            'Method for taking into account overlapping of cloud layers'),
        ('processes', 'ENUM:processes_attributes', '1.N',
            'Processes included in the cloud scheme'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: sub_grid_scale_water_distribution
# --------------------------------------------------------------------
DETAILS['sub_grid_scale_water_distribution'] = {
    'description': 'Sub-grid scale water distribution',
    'properties': [
        ('type', 'ENUM:sub_grid_scale_water_distribution_type', '1.1',
            'Sub-grid scale water distribution type'),
        ('function_name', 'str', '1.1',
            'Sub-grid scale water distribution function name'),
        ('function_order', 'int', '1.1',
            'Sub-grid scale water distribution function type'),
        ('convection_coupling', 'ENUM:sub_grid_scale_water_distribution_convection', '1.N',
            'Sub-grid scale water distribution coupling with convection'),
        ]
    }

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['sub_grid_scale_water_distribution_type'] = {
    'description': 'Approach used for cloud water content and fractional cloud cover',
    'is_open': False,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
        ]
    }

ENUMERATIONS['sub_grid_scale_water_distribution_convection'] = {
    'description': 'Type(s) of convection that the formation of clouds is coupled with',
    'is_open': False,
    'members': [
        ('coupled with deep', None),
        ('coupled with shallow', None),
        ('not coupled with convection', None),
        ]
    }

ENUMERATIONS['cloud_overlap_method'] = {
    'description': 'Cloud scheme cloud overlap method',
    'is_open': True,
    'members': [
        ('random', None),
        ('maximum', None),
        ('arbitrary', 'combination of maximum and random overlap between clouds'),
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

#TODO include horizontal cloud inhomogeneity? Tripple cloud scheme Shank et al 2010