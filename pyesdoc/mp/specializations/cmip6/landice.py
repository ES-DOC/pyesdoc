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
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, who, comment).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2016-04-11", "David Hassell",
         "Initialised from CMIP5 mind map + a bit of reorganising (but no logical difference)"),
    ("0.2.0", "2017-04-25", "David Hassell",
         "Updated with input from Steve George (NCAS)"),
    ("0.3.0", "2017-05-22", "David Hassell",
         "Updated with input from Sophie Nowicki (NASA)"),
    ("0.4.0", "2017-06-28", "David Hassell",
         "Reorganisation of grid info; first draft of short table"),
]

# --------------------------------------------------------------------
# CMIP5_MAPPINGS_SYNCED_AT: Latest version that has been synced with CMIP5 mappings.
# --------------------------------------------------------------------
CMIP5_MAPPINGS_SYNCED_AT = "N/A"

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this scientific realm
# --------------------------------------------------------------------
DESCRIPTION = 'Land Ice Realm'

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

# --------------------------------------------------------------------
# DETAILS: top level realm details
# --------------------------------------------------------------------
DETAILS = OrderedDict()

# --------------------------------------------------------------------
# ENUMERATIONS: top level realm enumerations
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()
