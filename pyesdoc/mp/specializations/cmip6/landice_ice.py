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
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Ice sheet and ice shelf'

# --------------------------------------------------------------------
# KEY PROPERTIES: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Ice sheet and ice shelf top level properties',
    'properties': [
        ('grounding_line_method', 'ENUM:grounding_line_methods', '1.1',
            'Specify the technique used for modelling the grounding line in the ice sheet-ice shelf coupling'),
        ('ice_sheet', 'bool', '1.1',
            'Are ice sheets simulated?'),
        ('ice_shelf', 'bool', '1.1',
            'Are ice shelves simulated?'),
    ]
}

#where I had calculated the SMB after I run the climate model for a year. Here we used sub-daily atmospheric output. For another model setup, we had calculated the SMB in the atmosphere model component on the atmosphere grid. Since this grid is too coarse to resolve the marginal melting zones, we are planning to couple the atmosphere model component to a higher resolved specialized SMB model. Therefore, we want to transfer the required fields through our coupler, like it is done for the atmosphere-ocean coupling. The SMB model will perform it's own IO. 

# --------------------------------------------------------------------
# SUB-PROCESS: Mass balance
# --------------------------------------------------------------------
DETAILS['mass_balance'] = {
    'description': 'Description of the surface mass balance treatment',
    'properties': [
        ('surface_mass_balance', 'l-str', '1.1',
            'Describe how and where the surface mass balance (SMB) is calulated. Include the temporal coupling frequeny from the atmosphere, whether or not a seperate  SMB model is used, and if so details of this model, such as its resolution'),
    ]
}

DETAILS['mass_balance:basal'] = {
    'description': 'Description of basal melting',
    'properties': [
        ('bedrock', 'l-str', '0.1',
             'Describe the implementation of basal melting over bedrock'),
        ('ocean', 'l-str', '0.1',
             'Describe the implementation of basal melting over the ocean'),
    ]
}

DETAILS['mass_balance:frontal'] = {
    'description': 'Description of claving/melting from the ice shelf front',
    'properties': [
        ('calving', 'l-str', '0.1',
             'Describe the implementation of calving from the front of the ice shelf'),
        ('melting', 'l-str', '0.1',
             'Describe the implementation of melting from the front of the ice shelf'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: Dynamics
# --------------------------------------------------------------------
DETAILS['dynamics'] = {
    'description': '',
    'properties': [
        ('description', 'l-str', '1.1',
            'General description of ice sheet and ice shelf dynamics'),
        ('approximation', 'ENUM:approximation_types', '1.N',
            'Approximation type used in modelling ice dynamics'),
        ('adaptive_timestep', 'bool', '1.1',
             'Is there an adaptive time scheme for the ice scheme?'),
        ('timestep', 'int', '1.1',
             'Timestep (in seconds) of the ice scheme. If the timestep is adaptive, then state a representative timestep.',),
#        ('coupling_wth_atmosphere', 'str', '0.1',
#             'Describe the coupling method between the ice sheet and ice shelf and atmosphe#re'),
#        ('coupling_wth_ocean', 'str', '0.1',
#             'Describe the coupling method between the ice sheet and ice shelf and the ocea#n'),
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
