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
DESCRIPTION = 'Atmospheric aerosol concentrations'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Properties of aerosol concentrations',
    'properties': [
        ('prescribed_lower_boundary', 'cs-str', '0.1',
            'List of species prescribed at the lower boundary.'),
        ('prescribed_upper_boundary', 'cs-str', '0.1',
            'List of species prescribed at the upper boundary.'),
        ('prescribed_fields_mmr', 'cs-str', '0.1',
            'List of species prescribed as mass mixing ratios.'),
        ('prescribed_fields_aod_plus_ccn', 'cs-str', '0.1',
            'List of species prescribed as AOD plus CCNs.'),
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
