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
DESCRIPTION = 'Atmospheric chemistry photo chemistry'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': '',
    'properties': [
        ('number_of_reactions', 'int', '1.1',
             'The number of reactions in the photo-chemistry scheme.'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Photolysis
# --------------------------------------------------------------------
DETAILS['photolysis'] = {
    'description': 'Photolysis scheme',
    'properties': [
        ('method', 'ENUM:photolysis_methods', '1.1',
            'Photolysis scheme'),
        ('environmental_conditions', 'str', '0.1',
             'Describe any environmental conditions taken into account by the photolysis scheme (e.g. whether pressure- and temperature-sensitive cross-sections and quantum yields in the photolysis calculations are modified to reflect the modelled conditions.)'),
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['photolysis_methods'] = {
    'description': 'Photolysis scheme',
    'is_open': False,
    'members': [
        ('Offline (clear sky)', None),
        ('Offline (with clouds)', None),
        ('Online', None),
    ]
}

ENUMERATIONS['online_processes'] = {
    'description': 'Processes included in the photolysis scheme.',
    'is_open': False,
    'members': [
        ('Scattering', None),
        ('Radiative transfer', None),
        ('Spectral resolution', None),
        ('Impact of clouds', None),
    ]
}
