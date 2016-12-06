"""A realm sepecialization.

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
CONTACT = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to realm specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = ''

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, comment, who).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
	("0.1.0", "2016-11-29", "Initialised", "Mark Greenslade"),
    ("0.2.0", "2016-12-02", "Updated process names and descriptions, added enumeration TODOs", "Charlotte Pascoe")
]

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this scientific realm
# --------------------------------------------------------------------
DESCRIPTION = 'Atmosphere realm specialization'

# --------------------------------------------------------------------
# REALM: Canonical name for the domain of this scientific realm
# --------------------------------------------------------------------
REALM = 'atmosphere'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'atmosphere_grid'

# --------------------------------------------------------------------
# KEY PROPERTIES: Key properties for the realm which differ from model defaults (grid, timestep etc)
# --------------------------------------------------------------------
KEY_PROPERTIES = 'atmosphere_key_properties'

# --------------------------------------------------------------------
# PROCESSES: Processes simulated within the realm
# --------------------------------------------------------------------
PROCESSES = [
    'atmosphere_dynamical_core',
    'atmosphere_radiation',
    'atmosphere_turbulence_convection',
    'atmosphere_microphysics_precipitation',
	'atmosphere_cloud_scheme',
    'atmosphere_cloud_simulator',
    'atmosphere_gravity_waves',
    'atmosphere_solar',
    'atmosphere_volcanos',
    ]
