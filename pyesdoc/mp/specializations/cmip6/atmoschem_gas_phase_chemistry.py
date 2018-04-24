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
DESCRIPTION = 'Atmospheric gas phase chemistry transport'

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
        ('number_of_tropospheric_heterogenous_reactions', 'int', '1.1',
             'The number of reactions in the tropospheric heterogeneous chemistry scheme.'),
        ('number_of_stratospheric_heterogenous_reactions', 'int', '1.1',
             'The number of reactions in the stratospheric heterogeneous chemistry scheme.'),
        ('number_of_advected_species', 'int', '1.1',
             'The number of advected species in the gas phase chemistry scheme.'),
        ('number_of_steady_state_species', 'int', '1.1',
             'The number of gas phase species for which the concentration is updated in the chemical solver assuming photochemical steady state'),
        ('interactive_dry_deposition', 'bool', '1.1',
            'Is dry deposition interactive (as opposed to prescribed)? Dry deposition describes the dry processes by which gaseous species deposit themselves on solid surfaces thus decreasing their concentration in the air.'),  
        ('wet_deposition', 'bool', '1.1',
            'Is wet deposition included? Wet deposition describes the moist processes by which gaseous species deposit themselves on solid surfaces thus decreasing their concentration in the air.'), 
        ('wet_oxidation', 'bool', '1.1',
            'Is wet oxidation included? Oxidation describes the loss of electrons or an increase in oxidation state by a molecule'),
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
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
