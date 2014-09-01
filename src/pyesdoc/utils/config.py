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



# Config filename.
_CONFIG_FILENAME = '.esdoc'

# Config file path.
_CONFIG_FILEPATH = "{0}/{1}".format(os.environ['HOME'], _CONFIG_FILENAME)

# Search parent directories if config file not found in user's home directory.
if not os.path.exists(_CONFIG_FILEPATH):
	dirname = os.path.dirname(os.path.abspath(__file__))
	for _ in range(3):
		_CONFIG_FILEPATH = "{0}/{1}".format(dirname, _CONFIG_FILENAME)
		if os.path.exists(_CONFIG_FILEPATH):
			break
		dirname = os.path.dirname(dirname)

# Exception if still not found.
if not os.path.exists(_CONFIG_FILEPATH):
    raise IOError("ESDOC configuration file [.esdoc] not found.")

# Config data wrapper.
data = json_file_to_namedtuple(_CONFIG_FILEPATH)
