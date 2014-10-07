# -*- coding: utf-8 -*-

"""
.. module:: utils.config.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Configuration utility functions.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import os

from .convert import json_file_to_namedtuple



# Default configuration file path.
_CONFIG_FPATH = "ops/config/esdoc.json"

# Configuration data.
data = None



def _init():
	"""Initializes configuration."""
	global data

	# Scan up file system hierarchy until reaching ops/config directory.
	dpath = os.path.dirname(os.path.abspath(__file__))
	while dpath != '/':
		fpath = os.path.join(dpath, _CONFIG_FPATH)
		if os.path.exists(fpath):
			break
		dpath = os.path.dirname(dpath)

	# If still not found then exception.
	if not os.path.exists(fpath):
		msg = "ESDOC configuration file ({0}) could not be found".format(_CONFIG_FPATH)
		raise RuntimeError(msg)

	# Config data wrapper.
	data = json_file_to_namedtuple(fpath)


# Auto-initialize.
_init()
