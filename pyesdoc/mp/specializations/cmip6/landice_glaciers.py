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
DESCRIPTION = 'Land ice glaciers'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Land ice glaciers top level properties',
    'properties': [
        ('description', 'l-str', '1.1',
             'Describe the treatment of glaciers, if any'),
        ('dynamic_areal_extent', 'bool', '0.1',
             'Does the model include a dynamic glacial extent?'),
    ],
}



## --------------------------------------------------------------------
## SUB-PROCESS: Mass Balance
## --------------------------------------------------------------------
#DETAILS['mass_balance'] = {
#    'description': 'TODO',
#    'properties': [
#        ('calculated_in_atmosphere', 'bool', '1.1',
#             'Is the ice sheet mass balance calculated in the atmosphere/land surface components?'),
#        ('ablation_calculation', 'ENUM:ablation_calculation_types', '0.1',
#             'If mass balance is calculated in land ice model, the type of scheme used to calculate ablation in the ice sheet mass balance'),
#        ('downscaling_technique', 'str', '0.1',
#             'If mass balance is calculated in land ice model, describe how the atmospheric variables are used in the mass balance calculations'),
#    ]
#}
#
#DETAILS['snow_treatment'] = {
#    'description': 'TODO',
#    'properties': [
#        ('calculated_in_atmosphere', 'bool', '1.1',
#             'Is the glacier snow calculated in the atmosphere/land surface components?'),
#        ('number_of_snow_layers', 'int', '0.1',
#             'If glacier snow is calculated in the land ice model, how many layers in the glacier snow model?'),
#        ('processes', 'ENUM:snow_processes', '0.N',
#             'If glacier snow is calculated in the land ice model, describe processes describing snow on glaciers'),
#    ],
#}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
#ENUMERATIONS['ablation_calculation_types'] = {
#    'description': 'Type of scheme used to model glacier ablation',
#    'is_open': True,
#    'members': [
#        ('Energy balance model', None),
#        ('PDD', None),
#    ]
#}
#
#ENUMERATIONS['glacier_snow_methods'] = {
#    'description': 'Treatment of glacier snow',
#    'is_open': True,
#    'members': [
#        ('same as snow in land surface', None),
#        ('different from snow in land surface', None),
#        ]
#    }
#
#ENUMERATIONS['snow_processes'] = {
#    'description': 'Processes describing snow on glaciers',
#    'is_open': True,
#    'members': [
#        ('prognostic snow albedo', None),
#        ('prognostic snow density', None),
#        ('prognostic snow water equivalent', None),
#        ('prognostic snow heat content', None),
#        ('prognostic snow temperature', None),
#        ('prognostic snow liquid water content', None),
#        ('snow melting', None),
#        ('snow refreezing', None),
#        ('blowing snow', None),
#    ]
#}
