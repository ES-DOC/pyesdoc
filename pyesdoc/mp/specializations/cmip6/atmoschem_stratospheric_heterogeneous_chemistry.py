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
DESCRIPTION = 'Atmospheric chemistry startospheric heterogeneous chemistry'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Gas phase chemistry attributes',
    'properties': [
        ('gas_phase_species', 'ENUM:gas_phase_species', '0.N',
            'Gas phase species included in the stratospheric heterogeneous chemistry scheme.'),
        ('aerosol_species', 'ENUM:aerosol_species', '0.N',
            'Aerosol species included in the stratospheric heterogeneous chemistry scheme.'),
        ('number_of_steady_state_species', 'int', '1.1',
             'The number of steady state species in the stratospheric heterogeneous chemistry scheme.'),
        ('sedimentation', 'bool', '1.1',
            'Is sedimentation is included in the stratospheric heterogeneous chemistry scheme or not?'),       
        ('coagulation', 'bool', '1.1',
            'Is coagulation is included in the stratospheric heterogeneous chemistry scheme or not?'),       
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['gas_phase_species'] = {
    'description': 'Gas phase species included in the stratospheric heterogeneous chemistry scheme',
    'is_open': False,
    'members': [
        ('Cly', None),
        ('Bry', None),
        ('NOy', None),
    ]
}

ENUMERATIONS['aerosol_species'] = {
    'description': 'Aerosol species included in the stratospheric heterogeneous chemistry scheme',
    'is_open': False,
    'members': [
        ('Sulphate', None),
        ('Polar stratospheric ice', None),
        ('NAT (Nitric acid trihydrate)', None),
        ('NAD (Nitric acid dihydrate)', None),
        ('STS (supercooled ternary solution aerosol particule))', None),
    ]
}
