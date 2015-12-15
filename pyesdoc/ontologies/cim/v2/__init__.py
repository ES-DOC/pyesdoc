# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.__init__.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The cim v2 package initialisor.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
from typeset import *

try:
	import decoder
except ImportError:
	pass
import typeset



# Version identifier.
ID = '2'

# Set of supported types.
TYPES = typeset.TYPES
