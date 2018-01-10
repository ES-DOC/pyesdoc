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
# CONTACT: Set to specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

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
        ('overview', 'str', '1.1',
             'Overview of concentrations in atmosperic aerosol model'),
        ('prescribed_lower_boundary', 'str', '0.1',
            'List of species prescribed at the lower boundary.'),
        ('prescribed_upper_boundary', 'str', '0.1',
            'List of species prescribed at the upper boundary.'),
        ('prescribed_fields_mmr', 'str', '0.1',
            'List of species prescribed as mass mixing ratios.'),
        ('prescribed_fields_mmr', 'str', '0.1',
            'List of species prescribed as AOD plus CCNs.'),
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
