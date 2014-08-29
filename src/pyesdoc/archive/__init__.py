"""
.. module:: __init__.py
   :platform: Unix
   :synopsis: DB document archive operations.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from . import (
	write_organized as _organize,
	write_pulled as _seed
	)
from .config import get_project_sources
from .io import (
	yield_organized_documents,
	get
	)



def organize(throttle=0):
	"""Organizes archived documents in readiness for further processing.

    :param int throttle: Limits number of documents to be processed.

	"""
	_organize.execute(throttle)


def seed(throttle=0):
	"""Seeds document archive with documents pulled from atom feeds.

    :param int throttle: Limits number of documents to be processed.

	"""
	_seed.execute(throttle)
