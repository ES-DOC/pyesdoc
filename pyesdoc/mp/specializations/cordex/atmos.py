"""A realm specialization.

For further information goto http://es-doc.org/cordex-model-specializations.

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
    ("0.1.0", "2018-12-01", "Guillaume Levavasseur (IPSL)",
        "Initialised"),
    ]

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
    'atmos_gravity_waves',
    'atmos_natural_forcing',
    ]
