
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.__init__.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The cim v1 package initialisor.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from typeset_for_data_package import *
from typeset_for_software_package import *
from typeset_for_shared_package import *
from typeset_for_grids_package import *
from typeset_for_quality_package import *
from typeset_for_misc_package import *
from typeset_for_activity_package import *


import typeset_for_data_package as data
import typeset_for_software_package as software
import typeset_for_shared_package as shared
import typeset_for_grids_package as grids
import typeset_for_quality_package as quality
import typeset_for_misc_package as misc
import typeset_for_activity_package as activity




# Set of supported packages.
from typeset import PACKAGES

# Set of supported document types.
from typeset import DOCUMENT_TYPES

# Set of supported classes.
from typeset import CLASSES

# Set of class properties.
from typeset import CLASS_PROPERTIES

# Set of class own properties.
from typeset import CLASS_OWN_PROPERTIES

# Map of class to sub-class(es).
from typeset import SUB_CLASSES

# Set of classes with sub class(es).
from typeset import SUB_CLASSED

# Map of class to base-class(es).
from typeset import BASE_CLASSES

# Set of classes with base-class(es).
from typeset import BASE_CLASSED

# Maximum class depth in hierarchy.
from typeset import CLASS_HIERACHY_DEPTH

# Set of supported enum.
from typeset import ENUMS

# Set of supported types.
TYPES = CLASSES + ENUMS

# Help text.
from helptext import HELP

# Set of type keys.
from keys import KEYS

# Set of class constraints.
from constraints import CONSTRAINTS

# Total class properties.
TOTAL_CLASS_PROPERTIES = sum(len(i) for i in CLASS_OWN_PROPERTIES.values())

# Total enum members across all enums.
TOTAL_ENUM_MEMBERS = sum(len(e.members) for e in ENUMS)

# Count of class constraints.
TOTAL_CONSTRAINTS = sum(len(CONSTRAINTS[c]) for c in CLASSES)

try:
	import decoder
except ImportError:
	pass
import typeset

# Ontology name.
NAME = 'cim'

# Version identifier.
VERSION = '1'

# Full ontology name.
FULL_NAME = 'cim.1'

