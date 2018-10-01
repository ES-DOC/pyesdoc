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
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Land ice key properties'

# --------------------------------------------------------------------
# KEY PROPERTIES: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'General key properties',
    'properties': [
        ('ice_albedo', 'ENUM:ice_albedo_methods', '1.N',
            'Specify how ice albedo is modelled',),
        ('atmospheric_coupling_variables', 'cs-str', '1.1',
             'Which variables are passed between the atmosphere and ice (e.g. orography, ice mass)'), 
        ('oceanic_coupling_variables', 'cs-str', '1.1',
             'Which variables are passed between the ocean and ice'), 
        ('prognostic_variables', 'ENUM:prognostic_variable_types', '1.N',
             'Which variables are prognostically calculated in the ice model'),
        ]
    }

DETAILS['toplevel:software_properties'] = {
    'description': 'Software properties of land ice code',
    'properties':[
        ('repository','str', '0.1',
            "Location of code for this component."),
        ('code_version','str', '0.1',
            "Code version identifier."),
        ('code_languages','cs-str', '0.1',
            "Code language(s)."),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: TUNING APPLIED: Any tuning used to optimise the parameters
# --------------------------------------------------------------------
DETAILS['tuning_applied'] = {
    'description': 'Tuning methodology for land ice component',
    'properties': [
        ('description', 'l-str', '1.1',
             "General overview description of tuning (if any): explain and motivate the main targets and metrics retained. &"
             "Document the relative weight given to climate performance metrics versus process oriented metrics, &"
             "and on the possible conflicts with parameterization level tuning. In particular describe any struggle &"
             "with a parameter value that required pushing it to its limits to solve a particular model deficiency."),
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


