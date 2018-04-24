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
DESCRIPTION = 'Atmospheric chemistry tropospheric heterogeneous chemistry'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Tropospheric heterogenous atmospheric chemistry',
    'properties': [ 
        ('gas_phase_species', 'cs-str', '0.1',
            'List of gas phase species included in the tropospheric heterogeneous chemistry scheme.'),
        ('aerosol_species', 'ENUM:aerosol_species', '0.N',
            'Aerosol species included in the tropospheric heterogeneous chemistry scheme.'),
        ('number_of_steady_state_species', 'int', '1.1',
             'The number of steady state species in the tropospheric heterogeneous chemistry scheme.'),
        ('interactive_dry_deposition', 'bool', '1.1',
            'Is dry deposition interactive (as opposed to prescribed)? Dry deposition describes the dry processes by which gaseous species deposit themselves on solid surfaces thus decreasing their concentration in the air.'),  
        ('coagulation', 'bool', '1.1',
            'Is coagulation is included in the tropospheric heterogeneous chemistry scheme or not?'),       
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['aerosol_species'] = {
    'description': 'Aerosol species included in the stratospheric heterogeneous chemistry scheme',
    'is_open': False,
    'members': [
        ('Sulphate', None),
        ('Nitrate', None),
        ('Sea salt', None),
        ('Dust', None),
        ('Ice', None),
        ('Organic', None),
        ('Black carbon/soot', None),
        ('Polar stratospheric ice', None),
        ('Secondary organic aerosols', None),
        ('Particulate organic matter', None),
    ]
}
