"""A realm key-properties sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# CONTACT: Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Land ice key properties'

# --------------------------------------------------------------------
# KEY PROPERTIES: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'General key properties',
    'properties': [
        ('model_name', 'str', '1.1',
             'Name of land surface model code'),
        ('ice_albedo', 'ENUM:ice_albedo_methods', '1.N',
            'Specify how ice albedo is modelled',),
        ('atmospheric_coupling_variables', 'str', '1.1',
             'Which variables are passed between the atmosphere and ice (e.g. orography, ice mass)'), 
        ('oceanic_coupling_variables', 'str', '1.1',
             'Which variables are passed between the ocean and ice'), 
        ('prognostic_variables', 'ENUM:prognostic_variable_types', '1.N',
             'Which variables are prognostically calculated in the ice model'),
        ]
    }

# --------------------------------------------------------------------
# KEY PROPERTIES: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['ice_albedo_methods'] = {
    'description': 'Specify how ice albedo is modelled',
    'is_open': True,
    'members': [
        ('prescribed', None),
        ('function of ice age', None),
        ('function of ice density', None),
    ]
}

ENUMERATIONS['prognostic_variable_types'] = {
    'description': 'Which variables are prognostically calculated in the ice model',
    'is_open': True,
    'members': [
        ('ice velocity', None),
        ('ice thickness', None),
        ('ice temperature', None),
    ]
}


