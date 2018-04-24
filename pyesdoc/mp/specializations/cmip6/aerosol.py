"""A sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# CONTACT: Set to specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'CMIP5 version, Yves Balkanski (LSCE), Michael Schulz (MET Norway)'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, who, comment).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
	("0.1.0", "2017-08-04", "Charlotte Pascoe (NCAS), David Hassell (NCAS)",
         "Initialised from CMIP5"),
	("0.2.0", "2017-12-18", "David Hassell (NCAS)",
         "Updated with input from Yves Balkanski (LSCE) and Michael Schulz (MET Norway)"),
	("1.0.0", "2018-03-06", "David Hassell (NCAS)",
         "Copied grid from atmoschem"),
	("1.0.1", "2018-04-04", "David Hassell (NCAS)",
         "Replaced some 'occurences of str' with 'cs-str' and 'l-str'"),
	("1.0.2", "2018-04-10", "David Hassell (NCAS)",
         "Changed cardinality of is_adaptive_grid to 1.1, and fixed typos"),
        ("1.0.2", "2018-04-04", "David Hassell",
            "Removed some l-str"),
    ]

# --------------------------------------------------------------------
# CMIP5_MAPPINGS_SYNCED_AT: Latest version that has been synced with CMIP5 mappings.
# --------------------------------------------------------------------
CMIP5_MAPPINGS_SYNCED_AT = "1.0.0"

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this specialization
# --------------------------------------------------------------------
DESCRIPTION = 'Atmospheric aerosols'

# --------------------------------------------------------------------
# KEY PROPERTIES: Key properties (differing from defaults (grid, timestep etc))
# --------------------------------------------------------------------
KEY_PROPERTIES = 'aerosol_key_properties'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'aerosol_grid'

# --------------------------------------------------------------------
# PROCESSES: Simulated processes
# --------------------------------------------------------------------
PROCESSES = [
    'aerosol_transport',
    'aerosol_emissions',
    'aerosol_concentrations',
    'aerosol_optical_radiative_properties',
    'aerosol_model',
    ]
