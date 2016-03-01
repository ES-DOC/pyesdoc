# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.__init__.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The cim v1 package initialisor.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
# Set of types.
from typeset import *

# Set of supported types.
from typeset import TYPES

# Set of type keys.
from typekey import TYPE_KEYS

# Set of type constraints.
from constraints import CONSTRAINTS

try:
	import decoder
except ImportError:
	pass
import typeset

# Version identifier.
ID = '1'
