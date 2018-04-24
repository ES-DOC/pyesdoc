"""A key-properties specialization.

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
DESCRIPTION = 'Ocean key properties'

# --------------------------------------------------------------------
# KEY PROPERTIES: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'General key properties in ocean',
    'properties': [
        ('model_family', 'ENUM:model_family_types', '1.1',
            'Type of ocean model.'),
        ('basic_approximations', 'ENUM:ocean_basic_approx_types', '1.N',
            'Basic approximations made in the ocean.',),
        ('prognostic_variables', 'ENUM:prognostic_vars_types', '1.N',
            'List of prognostic variables in the ocean component.'),
        ]
    }

DETAILS['toplevel:seawater_properties'] = {
    'description': 'Physical properties of seawater in ocean',
    'properties' : [
        ('eos_type', 'ENUM:seawater_eos_types', '1.1',
            'Type of EOS for sea water'),
        ('eos_functional_temp', 'ENUM:seawater_eos_func_temp', '1.1',
            'Temperature used in EOS for sea water'),
        ('eos_functional_salt', 'ENUM:seawater_eos_func_salt', '1.1',
            'Salinity used in EOS for sea water'),
        ('eos_functional_depth', 'ENUM:seawater_eos_func_depth', '1.1',
            'Depth or pressure used in EOS for sea water ?'),
        ('ocean_freezing_point', 'ENUM:seawater_freezing_point', '1.1',
            'Equation used to compute the freezing point (in deg C) of seawater, as a function of salinity and pressure'),
        ('ocean_specific_heat', 'float', '1.1',
            'Specific heat in ocean (cpocean) in J/(kg K)'),
        ('ocean_reference_density', 'float', '1.1',
            'Boussinesq reference density (rhozero) in kg / m3'),
        ]
    }

DETAILS['toplevel:bathymetry'] = {
    'description': 'Properties of bathymetry in ocean',
    'properties' : [
        ('reference_dates', 'ENUM:bathymetry_ref_dates', '1.1',
            'Reference date of bathymetry'),
        ('type', 'bool', '1.1',
            'Is the bathymetry fixed in time in the ocean ?'),
        ('ocean_smoothing', 'l-str', '1.1',
            'Describe any smoothing or hand editing of bathymetry in ocean'),
        ('source', 'str', '1.1',
            'Describe source of bathymetry in ocean'),
        ]
    }

DETAILS['toplevel:nonoceanic_waters'] = {
    'description': 'Non oceanic waters treatement in ocean',
    'properties': [
        ('isolated_seas','l-str', '0.1',
            'Describe if/how isolated seas is performed'),
        ('river_mouth','l-str', '0.1',
            'Describe if/how river mouth mixing or estuaries specific treatment is performed'),
       ]
    }

DETAILS['toplevel:software_properties'] = {
    'description': 'Software properties of ocean code',
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
# SUB-PROCESS: RESOLUTION: The resolution of the grid.
# --------------------------------------------------------------------
DETAILS['resolution'] = {
    'description': 'Resolution in the ocean grid',
    'properties': [
        ('name', 'str', '1.1',
             "This is a string usually used by the modelling group to describe the resolution of this grid, e.g. ORCA025, N512L180, T512L70 etc."),
        ('canonical_horizontal_resolution', 'str', '1.1',
             "Expression quoted for gross comparisons of resolution, eg. 50km or 0.1 degrees etc."),
        ('range_horizontal_resolution', 'str', '1.1',
             "Range of horizontal resolution with spatial details, eg. 50(Equator)-100km or 0.1-0.5 degrees etc."),
        ('number_of_horizontal_gridpoints', 'int', '1.1',
             "Total number of horizontal (XY) points (or degrees of freedom) on computational grid."),
        ('number_of_vertical_levels', 'int', '1.1',
             "Number of vertical levels resolved on computational grid."),
        ('is_adaptive_grid', 'bool', '1.1',
             "Default is False. Set true if grid resolution changes during execution."),
        ('thickness_level_1','float', '1.1',
             "Thickness of first surface ocean level (in meters)")
        ],
    }

# --------------------------------------------------------------------
# SUB-PROCESS: TUNING APPLIED: Any tuning used to optimise the parameters
# --------------------------------------------------------------------
DETAILS['tuning_applied'] = {
    'description': 'Tuning methodology for ocean component',
    'properties': [
        ('description', 'l-str', '1.1',
             """General overview description of tuning: explain and motivate the main targets and metrics retained.
             Document the relative weight given to climate performance metrics versus process oriented metrics,
             and on the possible conflicts with parameterization level tuning. In particular describe any struggle
             with a parameter value that required pushing it to its limits to solve a particular model deficiency.
             """),
        ('global_mean_metrics_used', 'cs-str', '0.1',
             "List set of metrics of the global mean state used in tuning model/component"),
        ('regional_metrics_used', 'cs-str', '0.1',
             "List of regional metrics of mean state (e.g THC, AABW, regional means etc) used in tuning model/component"),
        ('trend_metrics_used', 'cs-str', '0.1',
             "List observed trend metrics used in tuning model/component"),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: CONSERVATION PROPERTIES: Details of methodology needed to conserve variables between processes
# --------------------------------------------------------------------
DETAILS['conservation'] = {
    'description': 'Conservation in the ocean component',
    'properties': [
        ('description', 'l-str', '1.1',
             'Brief description of conservation methodology'),
        ('scheme', 'ENUM:conservation_props_types', '1.N',
            'Properties conserved in the ocean by the numerical schemes'),
        ('consistency_properties', 'cs-str','0.1',
            'Any additional consistency properties (energy conversion, pressure gradient discretisation, ...)?'),
        ('corrected_conserved_prognostic_variables', 'cs-str', '0.1', # Can we constrains these variable
             "Set of variables which are conserved by *more* than the numerical scheme alone."),
        ('was_flux_correction_used', 'bool', '0.1',
             "Does conservation involve flux correction ?"),
        ],
    }

# --------------------------------------------------------------------
# KEY PROPERTIES: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['model_family_types'] = {
    'description': 'Types of ocean models',
    'is_open': True,
    'members': [
        ('OGCM', None),
        ('slab ocean', None),
        ('mixed layer ocean', None)
        ]
    }

ENUMERATIONS['ocean_basic_approx_types'] = {
    'description': 'Types of basic approximation in ocean',
    'is_open': True,
    'members': [
        ('Primitive equations', None),
        ('Non-hydrostatic', None),
        ('Boussinesq', None)
        ]
    }

ENUMERATIONS['prognostic_vars_types'] = {
    'description': 'List of prognostic variables in ocean',
    'is_open': True,
    'members': [
        ('Potential temperature', None),
        ('Conservative temperature', None),
        ('Salinity', None),
        ('U-velocity', None),
        ('V-velocity', None),
        ('W-velocity', None),
        ('SSH', 'Sea Surface Height')
        ]
    }

ENUMERATIONS['seawater_eos_types'] = {
    'description': 'Types of seawater Equation of State in ocean',
    'is_open': True,
    'members': [
        ('Linear', None),
        ('Wright, 1997', None),
        ('Mc Dougall et al.', None),
        ('Jackett et al. 2006', None),
        ('TEOS 2010', None)
        ]
    }

ENUMERATIONS['seawater_eos_func_temp'] = {
    'description': 'Types of temperature used in EOS in ocean',
    'is_open': False,
    'members': [
        ('Potential temperature', None),
        ('Conservative temperature', None),
        ]
    }

ENUMERATIONS['seawater_eos_func_salt'] = {
    'description': 'Types of salinity used in EOS in ocean',
    'is_open': False,
    'members': [
        ('Practical salinity Sp', None),
        ('Absolute salinity Sa', None),
        ]
    }

ENUMERATIONS['seawater_eos_func_depth'] = {
    'description': 'Types of depth used in EOS in ocean',
    'is_open': False,
    'members': [
        ('Pressure (dbars)', None),
        ('Depth (meters)', None),
        ]
    }

ENUMERATIONS['seawater_freezing_point'] = {
    'description': 'Types of seawater freezing point equation in ocean',
    'is_open': True,
    'members': [
        ('TEOS 2010', None)
        ]
    }

ENUMERATIONS['bathymetry_ref_dates'] = {
    'description': 'List of reference dates for bathymetry in ocean',
    'is_open': True,
    'members': [
        ('Present day', None),
        ('21000 years BP', None),
        ('6000 years BP', None),
        ('LGM', 'Last Glacial Maximum'),
        ('Pliocene', None)
        ]
    }

ENUMERATIONS['conservation_props_types'] = {
    'description': 'List of properties that can be conserved in ocean',
    'is_open': True,
    'members': [
        ('Energy', None),
        ('Enstrophy', None),
        ('Salt', None),
        ('Volume of ocean', None),
        ('Momentum', None)
        ]
    }
