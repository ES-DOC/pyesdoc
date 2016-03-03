
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.__init__.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The cim v1 package initialisor.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from typeset_for_activity_package import *
from typeset_for_data_package import *
from typeset_for_shared_package import *
from typeset_for_software_package import *
from typeset_for_grids_package import *
from typeset_for_misc_package import *
from typeset_for_quality_package import *


import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_shared_package as shared
import typeset_for_software_package as software
import typeset_for_grids_package as grids
import typeset_for_misc_package as misc
import typeset_for_quality_package as quality




# Set of supported packages.
from typeset import PACKAGES

# Set of supported document types.
from typeset import DOCUMENT_TYPES

# Set of supported packages.
from typeset import CLASSES

# Set of supported packages.
from typeset import ENUMS

# Set of supported types.
TYPES = CLASSES + ENUMS

# Help text.
from helptext import HELP

# Set of type keys.
from keys import KEYS

# Set of type constraints.
# TODO class & property constraints
from constraints import CONSTRAINTS

try:
	import decoder
except ImportError:
	pass
import typeset

# Ontology name.
NAME = 'cim'

# Version identifier.
VERSION = '1'
