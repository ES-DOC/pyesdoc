"""A specialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# CONTACT: Set to specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Eric Guilyardi'

# --------------------------------------------------------------------
# AUTHORS: Set to specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Eric Guilyardi, David Hassell, Mark Greenslade'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'CMIP5 version + Julie Dehayes (LOCEAN/IPSL), Steve Griffies (GFDL), Alistair Adcroft (GFDL), Gokhan Danabasoglu (NCAR), Gurvan Madec (LOCEAN/IPSL)'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, who, comment).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2016-07-01", "Eric Guilyardi",
        "Initialised"),
    ("0.2.0", "2016-08-30", "Eric Guilyardi",
        "Update science following inputs from Gokhan Danabasoglu and Steve Griffies", ),
    ("0.3.0", "2016-09-05", "David Hassell",
        "Added hidden CIM2 properties to key_properties and timestepping_framework", ),
    ("0.4.0", "2016-11-08", "Eric Guilyardi et al.",
        "Changed syntax to simplify and remove CIM2 dependencies"),
    ("0.5.0", "2016-11-25", "Mark Greenslade.",
        "Syntax simplification in respect of process/sub-process"),
    ("0.6.0", "2017-01-13", "Eric Guilyardi",
        "Added ocean_short_table.py"),
    ("0.7.0", "2017-11-09", "Eric Guilyardi",
        "Updates following community review"),
    ]

# --------------------------------------------------------------------
# CMIP5_MAPPINGS_SYNCED_AT: Latest version that has been synced with CMIP5 mappings.
# --------------------------------------------------------------------
# TODO
CMIP5_MAPPINGS_SYNCED_AT = "0.4.0"

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this specialization
# --------------------------------------------------------------------
DESCRIPTION = 'Ocean Realm'

# --------------------------------------------------------------------
# KEY PROPERTIES: Key properties
# --------------------------------------------------------------------
KEY_PROPERTIES = 'ocean_key_properties'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'ocean_grid'

# --------------------------------------------------------------------
# PROCESSES: Simulated processes
# --------------------------------------------------------------------
PROCESSES = [
    'ocean_timestepping_framework',
    'ocean_advection',
    'ocean_lateral_physics',
    'ocean_vertical_physics',
    'ocean_uplow_boundaries',
    'ocean_boundary_forcing',
    ]
