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
DESCRIPTION = 'Aerosol optical and radiative properties'

# --------------------------------------------------------------------
# PROCESS: Optical and radiative properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Optical and radiative properties',
    'properties': [
        ('overview', 'str', '1.1',
             'Overview of optical and radiative properties'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Absorption
# --------------------------------------------------------------------
DETAILS['absorption'] = {
    'description': 'Absortion properties in aerosol scheme',
    'properties': [
        ('black_carbon', 'float', '0.1',
             'Absorption mass coefficient of black carbon at 550nm (if non-absorbing enter 0)'),
        ('dust', 'float', '0.1',
             'Absorption mass coefficient of dust at 550nm (if non-absorbing enter 0)'),
        ('organics', 'float', '0.1',
             'Absorption mass coefficient of organics at 550nm (if non-absorbing enter 0)'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Mixtures
# --------------------------------------------------------------------
DETAILS['mixtures'] = {
    'description': '',
    'properties': [
        ('external', 'bool', '1.1',
            'Is there external mixing with respect to chemical composition?'),
        ('internal', 'bool', '1.1',
            'Is there internal mixing with respect to chemical composition?'),
        ('mixing_rule', 'str', '0.1',
             'If there is internal mixing with respect to chemical composition then indicate the mixinrg rule'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Impact of H2O
# --------------------------------------------------------------------
DETAILS['impact_of_h2o'] = {
    'description': '',
    'properties': [
        ('size', 'bool', '1.1',
            'Does H2O impact size?'),
        ('internal_mixture', 'bool', '1.1',
            'Does H2O impact internal mixture?'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Radiative scheme for aerosol
# --------------------------------------------------------------------
DETAILS['radiative_scheme'] = {
    'description': 'Radiative scheme for aerosol',
    'properties': [
        ('overview', 'str', '1.1',
             'Overview of radiative scheme'),      
        ('shortwave_bands', 'int', '1.1',
            'Number of shortwave bands'),
        ('longwave_bands', 'int', '1.1',
            'Number of longwave bands'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Radiative scheme for aerosol
# --------------------------------------------------------------------
DETAILS['cloud_interactions'] = {
    'description': 'Aerosol-cloud interactions',
    'properties': [
        ('overview', 'str', '1.1',
             'Overview of aerosol-cloud interactions'),
        ('twomey', 'bool', '1.1',
            'Is the Twomey effect included?'),
        ('twomey_minimum_ccn', 'int', '0.1',
            'If the Twomey effect is included, then what is the minimum CCN number?'),
        ('drizzle', 'bool', '1.1',
            'Does the scheme affect drizzle?'),
        ('cloud_lifetime', 'bool', '1.1',
            'Does the scheme affect cloud lifetime?'),
        ('longwave_bands', 'int', '1.1',
            'Number of longwave bands'),
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
