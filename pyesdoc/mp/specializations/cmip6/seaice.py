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
CONTACT = 'Ruth Petrie'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Ruth Petrie, Bryan Lawrence, David Hassell, Mark Greenslade'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to realm specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'Jamie Rae (UKMO), Martin Vancopppenolle (IPSL), Alexandra Jahn (University of Colorado)'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, comment, who).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
	("0.1.0", "2016-05-24", "Initialised", "David Hassell"),
	("0.1.1", "2016-09-28", "Modified to include work done by Bryan Lawerence", "Petrie"),
	("0.1.2", "2016-11-07", "Updated on the basis of discussion with Jamie Rae (UKMO)", "Ruth Petrie"),
    ("0.1.3", "2016-11-15", "Refactored based to fit in the new schema", "Mark Greenslade"),
    ("0.1.4", "2016-11-17", "Update DETAILS and SUBPROCESS names", "Ruth Petrie"),
    ("0.1.5", "2016-11-18", "Update based on discussions with Martin Vancopppenolle (IPSL)", "Ruth Petrie"),
    ("0.1.6", "2016-11-23", "Update based on discussions with Alexandra Jahn (University of Colorado)", "Ruth Petrie"),
]

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this scientific realm
# --------------------------------------------------------------------
DESCRIPTION = 'Sea ice realm specialization'

# --------------------------------------------------------------------
# REALM: Canonical name for the domain of this scientific realm
# --------------------------------------------------------------------
REALM = 'seaice'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'seaice_grid'

# --------------------------------------------------------------------
# KEY PROPERTIES: Key properties for the realm which differ from model defaults (grid, timestep etc)
# --------------------------------------------------------------------
KEY_PROPERTIES = 'seaice_key_properties'

# --------------------------------------------------------------------
# PROCESSES: Processes simulated within the realm
# --------------------------------------------------------------------
PROCESSES = [
    'seaice_dynamics',
    'seaice_thermodynamics',
    'seaice_radiative_processes',
]

# --------------------------------------------------------------------
# REALM: top level details
# --------------------------------------------------------------------
DETAILS = OrderedDict()

# --------------------------------------------------------------------
# REALM: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

