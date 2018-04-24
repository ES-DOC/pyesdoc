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
DESCRIPTION = 'Sea Ice Dynamics'

# --------------------------------------------------------------------
# DETAILS : General process details.
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Dynamic processes in sea ice.',
    'properties': [
        ('horizontal_transport', 'ENUM:transport_methods', '1.1',
            "What is the method of horizontal advection of sea ice?"),
        ('transport_in_thickness_space', 'ENUM:transport_methods', '1.1',
            "What is the method of sea ice transport in thickness space (i.e. in thickness categories)?"),
        ('ice_strength_formulation', 'ENUM:ice_strength', '1.1',
             "Which method of sea ice strength formulation is used?"),
        ('redistribution', 'ENUM:redistribution_types', '1.N',
             "Which processes can redistribute sea ice (including thickness)?"),
        ('rheology', 'ENUM:rheology_types', '1.1',
             "Rheology, what is the ice deformation formulation?"),
        ]
    }

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['transport_methods'] = {
    'description': 'Transport Methods',
    'is_open': True,
    'members': [
        ('Incremental Re-mapping', '(including Semi-Lagrangian)'),
        ('Prather', None),
        ('Eulerian', None),
    ]
}

ENUMERATIONS['redistribution_types'] = {
    'description': 'Sea Ice Redistribution types',
    'is_open': True,
    'members': [
        ('Rafting', None),
        ('Ridging', None),
    ]
}

ENUMERATIONS['ice_strength'] = {
    'description': 'Ice strength formulation methods',
    'is_open': True,
    'members': [
        ('Hibler 1979', None),
        ('Rothrock 1975', None),
    ]
}

ENUMERATIONS['rheology_types'] = {
    'description': 'Sea ice rheology types',
    'is_open': True,
    'members': [
        ('Free-drift', None),
        ('Mohr-Coloumb', None),
        ('Visco-plastic', 'VP'),
        ('Elastic-visco-plastic', 'EVP'),
        ('Elastic-anisotropic-plastic', None,),
        ('Granular', None),
    ]
}


