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
DESCRIPTION = 'Atmospheric chemistry transport'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Top level lateral physics properties',
    'properties': [
        ('use_atmospheric_transport', 'bool', '1.1',
            'Is transport handled by the atmosphere, rather than within atmospheric cehmistry?'),      
        ('transport_details', 'l-str', '0.1',
             'If transport is handled within the atmospheric chemistry scheme, describe it.'),
    ]
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
