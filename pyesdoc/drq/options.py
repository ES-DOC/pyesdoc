# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.drq.constants.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Library options.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.drq import constants
from pyesdoc.drq import _utils



# Path to data request config file.
CONFIG_FPATH = _utils.get_fpath(constants.CONFIG_FILENAME, "config")

# Path to data request config file.
CONTENT_FPATH = _utils.get_fpath(constants.CONTENT_FILENAME, "content")
