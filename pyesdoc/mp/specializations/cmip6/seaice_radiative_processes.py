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
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Sea Ice Radiative Processes'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': "Radiative processes in sea ice.",
    'properties': [
        ('surface_albedo', 'ENUM:seaice_albedo', '1.1',
            "Method used to handle surface albedo?"),
        ('ice_radiation_transmission', 'ENUM:ice_transmission', '1.N',
            "Method by which solar radiation through sea ice is handled?"),
        ]
    }

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['seaice_albedo'] = {
    'description': "Surface albedo of sea ice component.",
    'is_open': True,
    'members': [
        ('Delta-Eddington', None),
        ('Parameterized', 'Sea ice albedo is parameterized.'),
        ('Multi-band albedo', 'Albedo value has a spectral dependence.'),
    ]
}

ENUMERATIONS['ice_transmission'] = {
    'description': "Ice radiative transmission.",
    'is_open': True,
    'members': [
        ('Delta-Eddington', None),
        ('Exponential attenuation', None),
        ('Ice radiation transmission per category', 'Radiation transmission through ice is different for each sea ice category.')
    ]
}
