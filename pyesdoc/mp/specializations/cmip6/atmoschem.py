"""A sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# CONTACT: Set to specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Charlotte Pascoe, David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'CMIP5 version + Bill Collins (URead)'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, who, comment).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2017-08-04", "Charlotte Pascoe (NCAS), David Hassell (NCAS)",
         "Initialised from CMIP5"),
    ("0.2.0", "2017-11-22", "David Hassell (NCAS)",
         "Updated with input from Bill Collins (URead), John Scinocca (CCCma)"),
    ("0.3.0", "2018-04-04", "David Hassell",
        "Replaced some occurences of 'str' with 'cs-str' and 'l-str'"),
    ("0.3.1", "2018-04-04", "David Hassell",
        "Removed some l-str"),
    ("1.0.0", "2018-07-11", "David Hassell",
        "No further reports - moving to v1"),

]

# --------------------------------------------------------------------
# CMIP5_MAPPINGS_SYNCED_AT: Latest version that has been synced with CMIP5 mappings.
# --------------------------------------------------------------------
#CMIP5_MAPPINGS_SYNCED_AT = "0.4.0"

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this specialization
# --------------------------------------------------------------------
DESCRIPTION = 'Atmospheric chemistry'

# --------------------------------------------------------------------
# KEY PROPERTIES: Key properties (differing from defaults (grid, timestep etc))
# --------------------------------------------------------------------
KEY_PROPERTIES = 'atmoschem_key_properties'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'atmoschem_grid'

# --------------------------------------------------------------------
# PROCESSES: Simulated processes
# --------------------------------------------------------------------
PROCESSES = [
    'atmoschem_transport',
    'atmoschem_emissions_concentrations',
    'atmoschem_gas_phase_chemistry',
    'atmoschem_stratospheric_heterogeneous_chemistry',
    'atmoschem_tropospheric_heterogeneous_chemistry',
    'atmoschem_photo_chemistry',
    ]
