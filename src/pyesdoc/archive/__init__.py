"""
.. module:: __init__.py
   :platform: Unix
   :synopsis: DB document archive operations.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from .write_organized import execute as organize
from .write_parsed import execute as parse
from .write_pulled import execute as seed
from .config import get_project_sources
from .io import (
	yield_ingestable_documents,
	yield_organized_documents,
	get
	)
