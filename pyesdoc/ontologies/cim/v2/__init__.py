
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.__init__.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The cim v2 package initialisor.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from typeset_for_designing_package import *
from typeset_for_shared_package import *
from typeset_for_activity_package import *
from typeset_for_software_package import *
from typeset_for_science_package import *
from typeset_for_data_package import *
from typeset_for_drs_package import *
from typeset_for_platform_package import *


import typeset_for_designing_package as designing
import typeset_for_shared_package as shared
import typeset_for_activity_package as activity
import typeset_for_software_package as software
import typeset_for_science_package as science
import typeset_for_data_package as data
import typeset_for_drs_package as drs
import typeset_for_platform_package as platform




try:
	import decoder
except ImportError:
	pass
import typeset
import type_info as TYPE_INFO
from type_help import HELP
from type_keys import KEYS

# Typeinfo constants - to be removed.
from type_info import PACKAGES
from type_info import DOCUMENT_TYPES
from type_info import CLASSES
from type_info import CLASS_PROPERTIES
from type_info import CLASS_OWN_PROPERTIES
from type_info import SUB_CLASSES
from type_info import SUB_CLASSED
from type_info import BASE_CLASSES
from type_info import BASE_CLASSED
from type_info import CLASS_HIERACHY_DEPTH
from type_info import ENUMS
from type_info import TOTAL_CLASS_PROPERTIES
from type_info import TOTAL_ENUM_MEMBERS
from type_info import CONSTRAINTS
from type_info import TOTAL_CONSTRAINTS
from type_info import TYPES



# Ontology name.
NAME = 'cim'

# Version identifier.
VERSION = '2'

# Full ontology name.
FULL_NAME = 'cim.2'
