"""A realm key-properties specialization.

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
DESCRIPTION = 'Key properties of the atmospheric chemistry'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Top level key properties in atmospheric chemistry model',
    'properties': [
        ('chemistry_scheme_scope', 'ENUM:chemistry_scheme_scopes', '1.N',
            'Atmospheric domains covered by the atmospheric chemistry model'),
        ('basic_approximations', 'str', '1.1',
            'Basic approximations made in the atmospheric chemistry model',),
        ('prognostic_variables_form', 'ENUM:prognostic_vars_types', '1.N',
            'Form of prognostic variables in the atmospheric chemistry component.'),
        ('number_of_tracers', 'int', '1.1',
            'Number of advected tracers in the atmospheric chemistry model'),
        ('family_approach', 'bool', '1.1',
            'Atmospheric chemistry calculations (not advection) generalized into families of species?'),
        ('coupling_with_chemical_reactivity', 'bool', '1.1',
            'Atmospheric chemistry transport scheme turbulence is couple with chemical reactivity?'),
        ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: timestepping framework
# --------------------------------------------------------------------
DETAILS['timestep_framework'] = {
    'description': 'Timestepping in the atmospheric chemistry model',
    'properties' : [
        ('method', 'ENUM:timestepping_methods', '1.1',
            'Mathematical method deployed to solve the evolution of a given variable'),
        ('split_operator_advection_timestep', 'int', '0.1',
            'Timestep for chemical species advection (in seconds)'),
        ('split_operator_physical_timestep', 'int', '0.1',
            'Timestep for physics (in seconds).'),
        ('split_operator_chemistry_timestep', 'int', '0.1',
            'Timestep for chemistry (in seconds).'),
        ('split_operator_alternate_order', 'bool', '0.1',
            '?'),
        ('integrated_timestep', 'int', '1.1',
            'Timestep for the atmospheric chemistry model (in seconds)'),
        ('integrated_scheme_type', 'ENUM:integrated_scheme_types', '1.1',
            'Specify the type of timestep scheme'),
    ]
}

_note1 = ' This should be an integer greater than zero, and may be the same value as for another process if they are calculated at the same time.'


DETAILS['timestep_framework:split_operator_order'] = {
    'description': '',
    'properties' : [
        ('turbulence', 'int', '0.1',
            'Call order for turbulence scheme.'+_note1),
        ('convection', 'int', '0.1',
            'Call order for convection scheme'+_note1),
        ('precipitation', 'int', '0.1',
            'Call order for precipitation scheme.'+_note1),
        ('emissions', 'int', '0.1',
            'Call order for emissions scheme.'+_note1),
        ('deposition', 'int', '0.1',
            'Call order for deposition scheme.'+_note1),
        ('gas_phase_chemistry', 'int', '0.1',
            'Call order for gas phase chemistry scheme.'+_note1),
        ('tropospheric_heterogeneous_phase_chemistry', 'int', '0.1',
            'Call order for tropospheric heterogeneous phase chemistry scheme.'+_note1),
        ('stratospheric_heterogeneous_phase_chemistry', 'int', '0.1',
            'Call order for stratospheric heterogeneous phase chemistry scheme.'+_note1),
        ('photo_chemistry', 'int', '0.1',
            'Call order for photo chemistry scheme.'+_note1),
        ('aerosols', 'int', '0.1',
            'Call order for aerosols scheme.'+_note1),
    ]
}

## --------------------------------------------------------------------
## SUB-PROCESS: Meteorological forcings
## --------------------------------------------------------------------
#DETAILS['meteorological_forcings'] = {
#    'description': '',
#    'properties' : [
#        ('variables_3D', 'str', '0.1',
#            'Three dimensionsal forcing variables, e.g. U, V, W, T, Q, P, conventive mass flux'),
#        ('variables_2D', 'str', '0.1',
#            'Two dimensionsal forcing variables, e.g. land-sea mask definition'),
#        ('frequency', 'int', '1.1',
#            'Frequency with which meteological forcings are applied (in seconds).'),
#        ]
#}

# --------------------------------------------------------------------
# SUB-PROCESS: TUNING APPLIED: Any tuning used to optimise the parameters
# --------------------------------------------------------------------
DETAILS['tuning_applied'] = {
    'description': 'Tuning methodology for atmospheric chemistry component',
    'properties': [
        ('description', 'l-str', '1.1',
             "General overview description of tuning: explain and motivate the main targets and metrics retained. &"
             "Document the relative weight given to climate performance metrics versus process oriented metrics, &"
             "and on the possible conflicts with parameterization level tuning. In particular describe any struggle &"
             "with a parameter value that required pushing it to its limits to solve a particular model deficiency."),
        ('global_mean_metrics_used', 'cs-str', '0.1',
             "List set of metrics of the global mean state used in tuning model/component"),
        ('regional_metrics_used', 'cs-str', '0.1',
             "List of regional metrics of mean state used in tuning model/component"),
        ('trend_metrics_used', 'cs-str', '0.1',
             "List observed trend metrics used in tuning model/component"),
        ]
    }

DETAILS['toplevel:software_properties'] = {
    'description': 'Software properties of aerosol code',
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
# KEY PROPERTIES: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['chemistry_scheme_scopes'] = {
    'description': 'Atmospheric domains covered by the atmospheric chemistry model',
    'is_open': True,
    'members': [
        ('troposphere', None),
        ('stratosphere', None),
        ('mesosphere', None),
        ('mesosphere', None),
        ('whole atmosphere', None),
    ]
}

ENUMERATIONS['prognostic_vars_types'] = {
    'description': 'Form of prognostic variables in the atmospheric chemistry component.',
    'is_open': True,
    'members': [
        ('3D mass/mixing ratio for gas', None),
    ]
}

ENUMERATIONS['timestepping_methods'] = {
    'description': 'Mathematical method deployed to solve the evolution of a given variable',
    'is_open': True,
    'members': [
        ('Operator splitting', None),
        ('Integrated', None),
    ]
}

ENUMERATIONS['integrated_scheme_types'] = {
    'description': 'Specify the type of timestep scheme',
    'is_open': True,
    'members': [
        ('Explicit', None),
        ('Implicit', None),
        ('Semi-implicit', None),
        ('Semi-analytic', None),
        ('Impact solver', None),
        ('Back Euler', None),
        ('Newton Raphson', None),
        ('Rosenbrock', None),
    ]
}
