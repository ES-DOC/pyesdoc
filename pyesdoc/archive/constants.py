"""
.. module:: constants.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package constants.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# All files filter.
FILE_FILTER_ALL = "*.*"

# Error file filter.
FILE_FILTER_ERROR = "*.ERROR"

# Accepted file filter.
FILE_FILTER_INGESTED = "*_*_*_*.*"

# Set of all file filters.
FILE_FILTER_SET = {
	FILE_FILTER_ALL,
	FILE_FILTER_ERROR,
	FILE_FILTER_INGESTED
}

