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
DESCRIPTION = 'Key properties of the aerosol model'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS = OrderedDict()

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
        ('variables_3D', 'str', '0.1',
            'Three dimensionsal forcing variables, e.g. U, V, W, T, Q, P, conventive mass flux'),
        ('variables_2D', 'str', '0.1',
            'Two dimensionsal forcing variables, e.g. land-sea mask definition'),
        ('frequency', 'int', '0.1',
            'Frequency with which meteological forcings are applied (in seconds).'),
        ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: RESOLUTION: The resolution of the grid.
# --------------------------------------------------------------------
DETAILS['resolution'] = {
    'description': 'Resolution in the aersosol model grid',
    'properties': [
        ('name', 'str', '1.1',
             "This is a string usually used by the modelling group to describe the resolution of this grid, e.g. ORCA025, N512L180, T512L70 etc."),
        ('canonical_horizontal_resolution', 'str', '0.1',
             "Expression quoted for gross comparisons of resolution, eg. 50km or 0.1 degrees etc."),
        ('number_of_horizontal_gridpoints', 'int', '0.1',
             "Total number of horizontal (XY) points (or degrees of freedom) on computational grid."),
        ('number_of_vertical_levels', 'int', '0.1',
             "Number of vertical levels resolved on computational grid."),
        ('is_adaptive_grid', 'bool', '0.1',
             "Default is False. Set true if grid resolution changes during execution."),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: TUNING APPLIED: Any tuning used to optimise the parameters
# --------------------------------------------------------------------
DETAILS['tuning_applied'] = {
    'description': 'Tuning methodology for aerosol model',
    'properties': [
        ('description', 'str', '1.1',
             "General overview description of tuning: explain and motivate the main targets and metrics retained. &"
             "Document the relative weight given to climate performance metrics versus process oriented metrics, &"
             "and on the possible conflicts with parameterization level tuning. In particular describe any struggle &"
             "with a parameter value that required pushing it to its limits to solve a particular model deficiency."),
        ('global_mean_metrics_used', 'str', '0.N',
             "List set of metrics of the global mean state used in tuning model/component"),
        ('regional_metrics_used', 'str', '0.N',
             "List of regional metrics of mean state used in tuning model/component"),
        ('trend_metrics_used', 'str', '0.N',
             "List observed trend metrics used in tuning model/component"),
    ]
}

# --------------------------------------------------------------------
# KEY PROPERTIES: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['scheme_scopes'] = {
    'description': 'Atmospheric domains covered by the aerosol model',
    'is_open': True,
    'members': [
        ('troposhere', None),
        ('stratosphere', None),
        ('mesosphere', None),
        ('mesosphere', None),
        ('whole atmosphere', None),
    ]
}

ENUMERATIONS['prognostic_vars_types'] = {
    'description': 'Form of prognostic variables in the aerosol model.',
    'is_open': True,
    'members': [
        ('3D mass/volume ratio for aerosols', None),
        ('3D number concenttration for aerosols', None),
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
