# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.utils.__init__.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package init.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from runtime import PYESDOC_Exception

from . import (
    convert,
    functional,
    runtime,
    runtime as rt,
    )

from .config import data as config
