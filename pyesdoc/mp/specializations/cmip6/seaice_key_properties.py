"""
A realm key-properties sepecialization.
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
DESCRIPTION = 'Sea Ice key properties'

# --------------------------------------------------------------------
# GENERAL details.
# --------------------------------------------------------------------
DETAILS['variables'] = {
    'description': "List of prognostic variable in the sea ice model.",
    'properties': [
        ('prognostic', 'ENUM:prognostic_variables', '1.N',
            "Select all prognostic variables in the sea ice component."),
        ]
    }

DETAILS['seawater_properties'] = {
    'description': "Properties of seawater relevant to sea ice",
    'properties': [
        ('ocean_freezing_point', 'ENUM:seawater_freezing_point', '1.1',
            "What is the equation used to compute the freezing point (in deg C) of seawater, as a function of salinity and pressure?"),
        ('ocean_freezing_point_value', 'float', '0.1',
            "If using a constant seawater freezing point, specify this value."),
        ]
    }

# --------------------------------------------------------------------
# RESOLUTION: Description of the resolution in the sea ice grid.
# --------------------------------------------------------------------
DETAILS['resolution'] = {
    'description': "Resolution of the sea ice grid",
    'properties': [
        ('name', 'str', '1.1',
            "This is a string usually used by the modelling group to describe the resolution of this grid e.g. N512L180, T512L70, ORCA025 etc."),
        ('canonical_horizontal_resolution', 'str', '1.1',
            "Expression quoted for gross comparisons of resolution, eg. 50km or 0.1 degrees etc."),
        ('number_of_horizontal_gridpoints', 'int', '1.1',
            "What are the total number of horizontal (XY) points (or degrees of freedom) on computational grid?"),
        ]
    }

# --------------------------------------------------------------------
# TUNING APPLIED: Any tuning used to optimise the parameters in this realm
# --------------------------------------------------------------------
DETAILS['tuning_applied'] = {
    'description': "Tuning applied to sea ice model component",
    'properties': [
        ('description', 'l-str', '1.1',
            """Provide a general overview description of tuning: explain and motivate 
            the main targets and metrics retained.  Document the relative weight given 
            to climate performance metrics versus process oriented metrics, and on the 
            possible conflicts with parameterization level tuning. In particular describe 
            any struggle with a parameter value that required pushing it to its limits to 
            solve a particular model deficiency."""),
        ('target', 'str', '1.1',
            "What was the aim of tuning, e.g. correct sea ice minima, correct seasonal cycle?"),
        ('simulations', 'cs-str', '1.1',
            "Which simulations had tuning applied, e.g. all, not historical, only pi-control? "),
        ('metrics_used', 'cs-str', '1.1',
            "List any observed metrics used in tuning model/parameters"),
        ('variables', 'cs-str', '0.1',
             "Which (if any) variables were changed during the tuning process?"),
        ]
    }


# --------------------------------------------------------------------
# PARAMETERISATIONS: Parameter values used in parameterisations
# --------------------------------------------------------------------
DETAILS['key_parameter_values'] = {
    'description': "Values of key parameters",
    'properties': [
        ('ice_strength', 'float', '0.1', "Ice strength (P*) in units of N m{-2}"),
        ('snow_conductivity', 'float', '0.1', 'Snow conductivity (ks) in units of W m{-1} K{-1}'),
        ('ice_thickness_in_leads', 'float', '0.1', 'Minimum thickness of ice created in leads (h0) in units of m'),
        ('additional_parameters', 'cs-str', '0.1',
         """If you have any additional paramterised values that you have used (e.g. minimum open water 
         fraction or bare ice albedo), please provide them here as a comma separated list in the form 
         {parameter1}: {value1}, {parameter2}: {value2}, etc."""),
        ]
}

# --------------------------------------------------------------------
# ASSUMPTIONS: Any key assumptions made in this realm
# --------------------------------------------------------------------
DETAILS['assumptions'] = {
    'description': "Assumptions made in the sea ice model",
    'properties': [
        ('description', 'l-str', '1.1',
            "Provide a general overview description of any *key* assumptions made in this model."),
        ('on_diagnostic_variables', 'cs-str', '1.1',
            "Note any assumptions that specifically affect the CMIP6 diagnostic sea ice variables."),
        ('missing_processes', 'cs-str', '1.1',
             """List any *key* processes missing in this model configuration? Provide full details 
             where this affects the CMIP6 diagnostic sea ice variables?"""),
        ]
    }

# --------------------------------------------------------------------
# EXTRA CONSERVATION PROPERTIES: Details of methodology needed to conserve variables between processes
# --------------------------------------------------------------------
DETAILS['conservation'] = {
    'description': "Conservation in the sea ice component",
    'properties': [
        ('description', 'l-str', '1.1',
            "Provide a general description of conservation methodology."),
        ('properties', 'ENUM:conserved_properties', '1.N',
            "Which properties conserved in sea ice by the numerical schemes?"),
        ('budget', 'cs-str', '1.1',
           """For each conserved property, specify the output variables which close 
           the related budgets. as a comma separated list. For example: 
           Conserved property, variable1, variable2, variable3"""),
        ('was_flux_correction_used', 'bool', '1.1',
            "Does conservation involved flux correction?"),
        ('corrected_conserved_prognostic_variables', 'cs-str', '0.1',
            """List any variables which are conserved by *more* than the numerical scheme alone 
            (e.g. has correction applied)."""),
        ]
    }

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['prognostic_variables'] = {
    'description': 'Prognostic variables in sea ice model',
    'is_open': True,
    'members': [
        ('Sea ice temperature', None),
        ('Sea ice concentration', None),
        ('Sea ice thickness', None),
        ('Sea ice volume per grid cell area', None),
        ('Sea ice u-velocity', None),
        ('Sea ice v-velocity', None),
        ('Sea ice enthalpy', None),
        ('Internal ice stress', None),
        ('Salinity', None),
        ('Snow temperature', 'Snow on ice temperature'),
        ('Snow depth', 'Snow on ice thickness'),
    ]
}

ENUMERATIONS['seawater_freezing_point'] = {
    'description': 'Types of seawater freezing point equation in sea ice.',
    'is_open': True,
    'members': [
        ('TEOS-10', 'Thermodynamic equation of seawater 2010.'),
        ('Constant', 'Constant value of seawater freezing point is used.'),
        ]
}

ENUMERATIONS['conserved_properties'] = {
    'description': 'List of properties that can be conserved in sea ice',
    'is_open': True,
    'members': [
        ('Energy', None),
        ('Mass', None),
        ('Salt', None),
    ]
}

ENUMERATIONS['parameter_values'] = {
    'description': 'Specify the values of the following parameters if used.',
    'is_open': True,
    'members': [
        ('Ice strength (P*) in units of N m{-2}.', None),
        ('Snow conductivity (ks) in units of W m{-1} K{-1}.', None),
        ('Minimum thickness of ice created in leads (h0) in units of m.', None),
    ]
}
