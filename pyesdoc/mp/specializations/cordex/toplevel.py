"""A top level model.

"""
# --------------------------------------------------------------------
# CONTACT: Set to top-level specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Guillaume Levavasseur (IPSL)'

# --------------------------------------------------------------------
# AUTHORS: Set to top-level specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Guillaume Levavasseur (IPSL)'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to top-level specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'Guillaume Levavasseur (IPSL), Mark Greenslade (IPSL)'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, who, comment).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2018-12-01", "Guillaume Levavasseur (IPSL)",
        "Initialised"),
    ]

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this scientific top-level
# --------------------------------------------------------------------
DESCRIPTION = 'Model top level'

# --------------------------------------------------------------------
# KEY PROPERTIES: File name (without the .py suffix) containing key properties of the top level model.
# --------------------------------------------------------------------
KEY_PROPERTIES = 'toplevel_key_properties'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = None

# --------------------------------------------------------------------
# PROCESSES: Processes simulated within the model
# --------------------------------------------------------------------
PROCESSES = [
    'toplevel_radiative_forcings',
    ]

# --------------------------------------------------------------------
# SIMULATES: Realms simulated by the model
# --------------------------------------------------------------------
SIMULATES = [
    "atmos",
]
