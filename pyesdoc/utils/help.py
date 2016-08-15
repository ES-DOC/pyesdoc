# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.utils.inspection.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of library listing functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import inspect
import pyesdoc



def list_constants():
	"""Lists pyesdoc constants.

	"""
	members = [n for n, _ in inspect.getmembers(pyesdoc) if n.upper() == n]
	for member in sorted(members):
	    print "{}\n\t{}\n".format(member, getattr(pyesdoc, member))


def list_functions():
	"""Lists pyesdoc functions.

	"""
	members = [n for n, m in inspect.getmembers(pyesdoc)
			   if n.upper() != n and not n.startswith('_') and inspect.isfunction(m)]
	for member in sorted(members):
	    print "{}\n\t{}\n".format(member, getattr(pyesdoc, member).__doc__.split(".")[0])
