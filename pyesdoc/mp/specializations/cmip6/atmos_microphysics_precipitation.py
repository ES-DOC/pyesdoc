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
DESCRIPTION = 'Cloud Microphysics and Precipitation'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------

# DEFINE HERE IF REQUIRED

# --------------------------------------------------------------------
# SUB-PROCESS: large_scale_precipitation
# --------------------------------------------------------------------
DETAILS['large_scale_precipitation'] = {
    'description': 'Properties of the large scale precipitation scheme',
    'properties': [
        ('scheme_name', 'str', '0.1',
            'Commonly used name of the large scale precipitation parameterisation scheme'),
        ('hydrometeors', 'ENUM:hydrometeor_types', '1.N',
            'Precipitating hydrometeors taken into account in the large scale precipitation scheme'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: cloud_microphysics
# --------------------------------------------------------------------
DETAILS['cloud_microphysics'] = {
    'description': 'Properties of the cloud microphysics scheme',
    'properties': [
        ('scheme_name', 'str', '0.1',
            'Commonly used name of the microphysics parameterisation scheme.'),
        ('processes', 'ENUM:processes_attributes', '1.N',
            'Cloud microphysics processes'),
        ]
    }

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['hydrometeor_types'] = {
    'description': 'Precipitating hydrometeors taken into account in the large scale precipitation scheme',
    'is_open': True,
    'members': [
        ('liquid rain', None),
        ('snow', None),
        ('hail', None),
        ('graupel', None),
        ]
    }

ENUMERATIONS['processes_attributes'] = {
    'description': 'Cloud microphysics processes',
    'is_open': True,
    'members': [
        ('mixed phase', None),
        ('cloud droplets', None),
        ('cloud ice', None),
        ('ice nucleation', None),
        ('water vapour deposition', None),
        ('effect of raindrops', None),
        ('effect of snow', None),
        ('effect of graupel', None),
        ]
    }

