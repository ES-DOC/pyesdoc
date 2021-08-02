"""A realm sepecialization.

For further information goto http://wordpress.es-doc.org/cordex-model-specializations.

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
CONTACT = 'David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell, Eric Guilyardi'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to realm specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'Rich Ellis (CEH), Phillipe Peylin (IPSL)'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, who, comment).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2021-06-01", "Mark A. Greenslade",
        "Initialised from CMIP6"),
]

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this scientific realm
# --------------------------------------------------------------------
DESCRIPTION = 'Land Surface'

# --------------------------------------------------------------------
# KEY PROPERTIES: Key properties for the realm which differ from model defaults (grid, timestep etc)
# --------------------------------------------------------------------
KEY_PROPERTIES = 'land_key_properties'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'land_grid'

# --------------------------------------------------------------------
# PROCESSES: Processes simulated within the realm
# --------------------------------------------------------------------
PROCESSES = [
    'land_soil',
    'land_snow',
    'land_vegetation',
    'land_energy_balance',
    'land_carbon_cycle',
    'land_nitrogen_cycle',
    'land_river_routing',
    'land_lakes',
    ]
