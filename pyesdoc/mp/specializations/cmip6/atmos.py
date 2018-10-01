"""A realm specialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# CONTACT: Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Charlotte Pascoe, Robert Pincus (NOAA)'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to realm specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = ''

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, who, comment).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2016-11-29", "Mark Greenslade",
        "Initialised"),
    ("0.2.0", "2016-12-02", "Charlotte Pascoe",
        "Updated process names and descriptions, added enumeration TODOs"),
    ("0.3.0", "2017-11-08", "Charlotte Pascoe",
        "Updated following community feedback"),
    ("1.0.0", "2018-03-28", "Charlotte Pascoe and Eric Guilyardi",
        "Review of atmosphere components"),
    ("1.0.1", "2018-04-04", "David Hassell",
        "Replaced some occurences of 'str' with 'cs-str' and 'l-str'"),
    ("1.0.2", "2018-04-04", "David Hassell",
        "Removed some l-str"),
    ("1.1.0", "2018-09-27", "David Hassell (NCAS)",
         "Added key_propoerties.tuning_applied"),
    ]

# --------------------------------------------------------------------
# CMIP5_MAPPINGS_SYNCED_AT: Latest version that has been synced with CMIP5 mappings.
# --------------------------------------------------------------------
CMIP5_MAPPINGS_SYNCED_AT = "1.0.0"

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this scientific realm
# --------------------------------------------------------------------
DESCRIPTION = 'Atmosphere'

# --------------------------------------------------------------------
# KEY PROPERTIES: Key properties for the realm which differ from model defaults (grid, timestep etc)
# --------------------------------------------------------------------
KEY_PROPERTIES = 'atmos_key_properties'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'atmos_grid'

# --------------------------------------------------------------------
# PROCESSES: Processes simulated within the realm
# --------------------------------------------------------------------
PROCESSES = [
    'atmos_dynamical_core',
    'atmos_radiation',
    'atmos_turbulence_convection',
    'atmos_microphysics_precipitation',
	'atmos_cloud_scheme',
    'atmos_observation_simulation',
    'atmos_gravity_waves',
    'atmos_natural_forcing',
    ]
