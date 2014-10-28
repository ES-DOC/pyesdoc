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
	exists,
	load,
	read,
	write,
	# yield_documents,
	yield_ingestable,
	yield_raw
	)
