"""
.. module:: __init__.py
   :platform: Unix
   :synopsis: DB document archive operations.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from .write_organized import execute as organize
from .write_raw_from_feeds import execute as populate
from .config import get_project_sources
from .io import (
	delete,
	delete_files,
    DIR_INGESTED,
    DIR_INGESTED_ERROR,
    DIR_ORGANIZED,
    DIR_ORGANIZED_ERROR,
    DIR_PARSED,
    DIR_PARSED_ERROR,
    DIR_RAW,
    DIR_RAW_ERROR,
	exists,
    get_doc_file,
	load,
	read,
	write,
	yield_ingestable,
	yield_raw
	)
