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



# Configuration file name.
_CONFIG_FNAME = ".esdoc-config"

# Configuration file path.
_CONFIG_FPATH = "{0}/{1}".format(os.environ['HOME'], _CONFIG_FNAME)

# Exception if still not found.
if not os.path.exists(_CONFIG_FPATH):
	msg = "ESDOC configuration file does not exist :: {0}"
	raise RuntimeError(msg.format(_CONFIG_FPATH))

# Config data wrapper.
data = json_file_to_namedtuple(_CONFIG_FPATH)
