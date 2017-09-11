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
DESCRIPTION = 'Atmospheric chemistry transport'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Gas phase chemistry attributes',
    'properties': [
        ('species', 'ENUM:species_types', '0.N',
            'Species included in the gas phase chemistry scheme.'),
        ('number_of_bimolecular_reactions', 'int', '1.1',
             'The number of bi-molecular reactions in the gas phase chemistry scheme.'),
        ('number_of_termolecular_reactions', 'int', '1.1',
             'The number of ter-molecular reactions in the gas phase chemistry scheme.'),
        ('number_of_advected_species', 'int', '1.1',
             'The number of advected species in the gas phase chemistry scheme.'),
        ('number_of_steady_state_species', 'int', '1.1',
             'The number of steady state species in the gas phase chemistry scheme.'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Dry deposotion
# --------------------------------------------------------------------
DETAILS['dry_deposition'] = {
    'description': 'Dry deposition describes the dry processes by which gaseous species deposit themselves on solid surfaces thus decreasing their concentration in the air.',
    'properties': [
        ('interactive', 'bool', '1.1',
            'Is dry deposition interactive (as opposed to prescribed)?'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Wet deposotion
# --------------------------------------------------------------------
DETAILS['wet_deposition'] = {
    'description': 'Wet deposition describes the moist processes by which gaseous species deposit themselves on solid surfaces thus decreasing their concentration in the air.',
    'properties': [
        ('included', 'bool', '1.1',
            'Is wet deposition included?'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Oxidation
# --------------------------------------------------------------------
DETAILS['oxidation'] = {
    'description': 'Oxidation describes the loss of electrons or an increase in oxidation state by a molecule.',
    'properties': [
        ('included', 'bool', '1.1',
            'Is wet oxidation included?'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Washout-rainout
# --------------------------------------------------------------------
DETAILS['washout_rainout'] = {
    'description': 'Downward transport of soluble chemistry species in clouds.',
    'properties': [
        ('methods', 'ENUM:washout_methods', '0.N',
            'Methods of downward transport of soluble chemistry species in clouds.'),
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['washout_methods'] = {
    'description': 'Methods of downward transport of soluble chemistry species in clouds.',
    'is_open': False,
    'members': [
        ('In-cloud scavenging', None),
        ('Below-cloud scavenging', None),
        ]
    }

ENUMERATIONS['species_types'] = {
    'description':'Species included in the gas phase chemistry scheme.',
    'is_open': True,
    'members':[
        ('HOx', None),
        ('NOy', None),
        ('Ox', None),
        ('Cly', None),
        ('HSOx', None),
        ('Bry', None),
        ('VOCs', None),
        ('isoprene', None),
        ('H2O', None),
    ]
}
