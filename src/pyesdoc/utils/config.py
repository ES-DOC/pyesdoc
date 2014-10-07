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



# Default configuration file name.
_CONFIG_FNAME = ".esdoc-config"

# Default configuration file directory.
_CONFIG_DIR = os.environ['HOME']

# Configuration data.
data = None



def _init():
	"""Initializes configuration."""
	global data

	# Default location is in users home directory.
	fpath = "{0}/{1}".format(_CONFIG_DIR, _CONFIG_FNAME)

	# If not found in default then scan up file system hierarchy.
	if not os.path.exists(fpath):
		dpath = os.path.dirname(os.path.abspath(__file__))
		while dirpath != '/':
			fpath = os.path.join(dpath, _CONFIG_FNAME)
			if os.path.exists(fpath):
				break
			dpath = os.path.dirname(dpath)

	# If still not found then exception.
	if not os.path.exists(fpath):
		msg = "ESDOC configuration file (.esdoc-config) could not be found"
		raise RuntimeError(msg)

	# Config data wrapper.
	data = json_file_to_namedtuple(fpath)


# Auto-initialize.
_init()
