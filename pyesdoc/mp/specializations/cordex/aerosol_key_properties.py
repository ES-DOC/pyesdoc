"""A realm key-properties specialization.

For further information goto http://wordpress.es-doc.org/cordex-model-specializations.

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
DESCRIPTION = 'Key properties of the aerosol model'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Top level key properties in aerosol model',
    'properties': [
        ('scheme_scope', 'ENUM:scheme_scopes', '1.N',
            'Atmospheric domains covered by the aerosol model'),
        ('basic_approximations', 'str', '1.1',
            'Basic approximations made in the aerosol model',),
        ('prognostic_variables_form', 'ENUM:prognostic_vars_types', '1.N',
            'Prognostic variables in the aerosol model'),
        ('number_of_tracers', 'int', '1.1',
            'Number of tracers in the aerosol model'),
        ('family_approach', 'bool', '1.1',
            'Are aerosol calculations generalized into families of species?'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: timestepping framework
# --------------------------------------------------------------------
DETAILS['timestep_framework'] = {
    'description': 'Physical properties of seawater in ocean',
    'properties' : [
        ('method', 'ENUM:timestepping_methods', '1.1',
            'Mathematical method deployed to solve the time evolution of the prognostic variables'),
        ('split_operator_advection_timestep', 'int', '0.1',
            'Timestep for aerosol advection (in seconds)'),
        ('split_operator_physical_timestep', 'int', '0.1',
            'Timestep for aerosol physics (in seconds).'),
        ('integrated_timestep', 'int', '1.1',
            'Timestep for the aerosol model (in seconds)'),
        ('integrated_scheme_type', 'ENUM:integrated_scheme_types', '1.1',
            'Specify the type of timestep scheme'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Meteorological forcings
# --------------------------------------------------------------------
DETAILS['meteorological_forcings'] = {
    'description': '',
    'properties' : [
        ('variables_3D', 'cs-str', '0.1',
            'Three dimensional forcing variables, e.g. U, V, W, T, Q, P, conventive mass flux'),
        ('variables_2D', 'cs-str', '0.1',
            'Two dimensional forcing variables, e.g. land-sea mask definition'),
        ('frequency', 'int', '0.1',
            'Frequency with which meteorological forcings are applied (in seconds).'),
        ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: RESOLUTION: The resolution of the grid.
# --------------------------------------------------------------------
DETAILS['resolution'] = {
    'description': 'Resolution in the aerosol model grid',
    'properties': [
        ('name', 'str', '1.1',
             "This is a string usually used by the modelling group to describe the resolution of this grid, e.g. ORCA025, N512L180, T512L70 etc."),
        ('canonical_horizontal_resolution', 'str', '0.1',
             "Expression quoted for gross comparisons of resolution, eg. 50km or 0.1 degrees etc."),
        ('number_of_horizontal_gridpoints', 'int', '0.1',
             "Total number of horizontal (XY) points (or degrees of freedom) on computational grid."),
        ('number_of_vertical_levels', 'int', '0.1',
             "Number of vertical levels resolved on computational grid."),
        ('is_adaptive_grid', 'bool', '1.1',
             "Set to true if the grid resolution changes during execution."),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: TUNING APPLIED: Any tuning used to optimise the parameters
# --------------------------------------------------------------------
DETAILS['tuning_applied'] = {
    'description': 'Tuning methodology for aerosol model',
    'properties': [
        ('description', 'l-str', '1.1',
             "General overview description of tuning: explain and motivate the main targets and metrics retained. Document the relative weight given to climate performance metrics versus process oriented metrics, and on the possible conflicts with parameterization level tuning. In particular describe any struggle with a parameter value that required pushing it to its limits to solve a particular model deficiency."),
        ('global_mean_metrics_used', 'cs-str', '0.1',
             "List of metrics of the global mean state used in tuning model/component"),
        ('regional_metrics_used', 'cs-str', '0.1',
             "List of metrics of regional mean state used in tuning model/component"),
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
ENUMERATIONS['scheme_scopes'] = {
    'description': 'Atmospheric domains covered by the aerosol model',
    'is_open': True,
    'members': [
        ('troposphere', None),
        ('stratosphere', None),
        ('mesosphere', None),
        ('whole atmosphere', None),
    ]
}

ENUMERATIONS['prognostic_vars_types'] = {
    'description': 'Form of prognostic variables in the aerosol model.',
    'is_open': True,
    'members': [
        ('3D mass/volume ratio for aerosols', None),
        ('3D number concentration for aerosols', None),
    ]
}

ENUMERATIONS['timestepping_methods'] = {
    'description': 'Mathematical method deployed to solve the time evolution of the prognostic variables.',
    'is_open': True,
    'members': [
        ('Uses atmospheric chemistry time stepping', None),
        ('Specific timestepping (operator splitting)', None),
        ('Specific timestepping (integrated)', None),
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
