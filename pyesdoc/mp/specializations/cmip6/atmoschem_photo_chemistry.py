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
CONTACT = 'Charlotte Pascoe, David Hassell'

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
DESCRIPTION = 'Atmospheric chemistry photo chemistry'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'TO DO',
    'properties': [
        ('number_of_reactions', 'int', '1.1',
             'The number of reactions in the photo-chemistry scheme.'),
        ('number_of_species', 'int', '1.1',
             'The number of species in the photo-chemistry scheme.'),
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
        ('online_processes', 'ENUM:online_processes', '0.N',
             'Processes included in the photolysis scheme.'),
        ('reaction_data', 'ENUM:reaction_data', '0.N',
             'Reaction information taken into account by the photolysis scheme.'),
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

ENUMERATIONS['reaction_data'] = {
    'description': 'Reaction information taken into account by the photolysis scheme.',
    'is_open': False,
    'members': [
        ('Updated reaction absorptio cross sections', None),
        ('Updated reaction quantum yields', None),
    ]
}
