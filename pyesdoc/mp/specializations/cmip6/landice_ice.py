"""A realm process sepecialization.

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
DESCRIPTION = 'Ice sheet and ice shelf'

# --------------------------------------------------------------------
# KEY PROPERTIES: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'General key properties in ice sheets and ice shelves',
    'properties': [
        ('grounding_line_method', 'ENUM:grounding_line_methods', '1.1',
            'Specify the technique used for modelling the grounding line in the ice sheet-ice shelf coupling'),
        ('ice_sheet', 'bool', '1.1',
            'Are ice sheets simulated?'),
        ('ice_shelf', 'bool', '1.1',
            'Are ice shelves simulated?'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: Mass balance
# --------------------------------------------------------------------
DETAILS['mass_balance'] = {
    'description': 'TODO',
    'properties': [],
    'detail_sets': [
        'basal',
        'frontal'
    ],
}

DETAILS['mass_balance:basal'] = {
    'description': 'TODO',
    'properties': [
        ('bedrock', 'str', '0.1',
             'Describe the implementation of basal melting over bedrock'),
        ('ocean', 'str', '0.1',
             'Describe the implementation of basal melting over the ocean'),
    ]
}

DETAILS['mass_balance:frontal'] = {
    'description': 'TODO',
    'properties': [
        ('calving', 'str', '0.1',
             'Describe the implementation of calving from the front of the ice shelf'),
        ('melting', 'str', '0.1',
             'Describe the implementation of melting from the front of the ice shelf'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: Dynamics
# --------------------------------------------------------------------
DETAILS['dynamics'] = {
    'description': '',
    'properties': [
        ('description', 'str', '1.1',
            'General description if ice sheet and ice shelf dynamics'),
        ('approximation', 'ENUM:approximation_types', '1.N',
            'Approximation type used in modelling ice dynamics'),
        ('timestep', 'int', '1.1',
             'Timestep (in seconds) of the ice scheme',),        
#        ('coupling_wth_atmosphere', 'str', '0.1',
#             'Describe the coupling method between the ice sheet and ice shelf and atmosphe#re'),
#        ('coupling_wth_ocean', 'str', '0.1',
#             'Describe the coupling method between the ice sheet and ice shelf and the ocea#n'),
#    ],
#    'detail_sets': [
#        'numerics',
    ]
}

#DETAILS['dynamics:numerics'] = {
#    'description': 'TODO',
#    'properties': [
#        ('timestep', 'int', '1.1',
#             'Timestep (in seconds) of the ice scheme',),        
#        ('approximation', 'ENUM:approximation_types', '1.N',
#            'Approximation type used in modelling ice dynamics'),
#   ],
#}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['grounding_line_methods'] = {
    'description': 'Specify the technique used for modelling the grounding line in the ice sheet-ice shelf coupling',
    'is_open': True,
    'members': [
        ('grounding line prescribed', None),
        ('flux prescribed (Schoof)', None),
        ('fixed grid size', None),
        ('moving grid', None),
    ]
}

ENUMERATIONS['ablation_calculation_types'] = {
    'description': 'Type of scheme used to model ice sheet ablation',
    'is_open': True,
    'members': [
        ('Energy balance model', None),
        ('PDD', 'positive degree days'),
    ]
}

ENUMERATIONS['approximation_types'] = {
    'description': 'Approximation type used in modelling ice sheet dynamics',
    'is_open': True,
    'members': [
        ('SIA', None),
        ('SAA', None),
        ('full stokes', None),
    ]
}

ENUMERATIONS['ice_sheet_snow_processes'] = {
    'description': 'Processes describing snow on ice sheets',
    'is_open': True,
    'members': [
        ('snow melting', None),
        ('snow refreezing', None),
        ('blowing snow', None),
    ]
}
