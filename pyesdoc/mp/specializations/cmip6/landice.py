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
AUTHORS = 'David Hassell'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to realm specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'Sophie Nowicki, Steve George'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, who, comment).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2016-04-11", "David Hassell (NCAS)",
         "Initialised from CMIP5 mind map"),
    ("0.2.0", "2017-04-25", "David Hassell (NCAS)",
         "Updated with input from Steve George (NCAS)"),
    ("0.3.0", "2017-05-22", "David Hassell",
         "Updated with input from Sophie Nowicki (NASA)"),
    ("0.4.0", "2017-06-28", "David Hassell (NCAS)",
         "Reorganisation of grid info; first draft of short table"),
    ("0.5.0", "2017-12-15", "David Hassell (NCAS)",
         "Updated with input from Christian Rodehacke (DMI)"),
    ("1.0.0", "2018-04-04", "David Hassell (NCAS)",
         "Moved to v1"),
    ("1.0.1", "2018-04-04", "David Hassell",
        "Removed some l-str"),
    ("1.1.0", "2018-09-27", "David Hassell (NCAS)",
         "Added key_propoerties.tuning_applied"),
]

# --------------------------------------------------------------------
# CMIP5_MAPPINGS_SYNCED_AT: Latest version that has been synced with CMIP5 mappings.
# --------------------------------------------------------------------
CMIP5_MAPPINGS_SYNCED_AT = "N/A"

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this scientific realm
# --------------------------------------------------------------------
DESCRIPTION = 'Land Ice'

# --------------------------------------------------------------------
# KEY PROPERTIES: Key properties for the realm which differ from model defaults (grid, timestep etc)
# --------------------------------------------------------------------
KEY_PROPERTIES = 'landice_key_properties'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'landice_grid'

# PROCESSES: Processes simulated within the realm
# --------------------------------------------------------------------
PROCESSES = [
    'landice_glaciers',
    'landice_ice',
]
