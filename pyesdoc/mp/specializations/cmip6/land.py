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
CONTACT = 'David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell, Eric Guilyardi'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to realm specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'CMIP5 version, Rich Ellis (CEH), Phillipe Peylin (IPSL)'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, who, comment).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2016-04-05", "David Hassell",
        "Initialised from CMIP5 mind map + incorporating initital feedback from Rich Ellis and Pillipe Peylin"),
    ("0.2.0", "2016-06-01", "David Hassell",
         "Incorporating comments from Christine Delire (CNRM), Bark van de Hurk (KNMI), Sergey Malyshev (GFDL), Chris Milly (GFDL)"),
    ("0.3.0", "2018-04-04", "David Hassell",
        "Replaced some occurences of str with cs-str and l-str"),
    ("1.0.0", "2018-04-04", "David Hassell",
        "Moved to v1"),
    ("1.0.1", "2018-04-04", "David Hassell",
        "Removed some l-str"),
    ("1.1.0", "2018-09-27", "David Hassell (NCAS)",
         "Added key_propoerties.tuning_applied"),
]

# --------------------------------------------------------------------
# CMIP5_MAPPINGS_SYNCED_AT: Latest version that has been synced with CMIP5 mappings.
# --------------------------------------------------------------------
CMIP5_MAPPINGS_SYNCED_AT = "0.2.0"

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
