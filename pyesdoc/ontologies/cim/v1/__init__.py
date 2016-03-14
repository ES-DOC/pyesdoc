
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.__init__.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The cim v1 package initialisor.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from typeset_for_shared_package import *
from typeset_for_software_package import *
from typeset_for_grids_package import *
from typeset_for_quality_package import *
from typeset_for_data_package import *
from typeset_for_activity_package import *
from typeset_for_misc_package import *


import typeset_for_shared_package as shared
import typeset_for_software_package as software
import typeset_for_grids_package as grids
import typeset_for_quality_package as quality
import typeset_for_data_package as data
import typeset_for_activity_package as activity
import typeset_for_misc_package as misc




try:
	import decoder
except ImportError:
	pass
import typeset
import typeinfo as TYPE_INFO
from helptext import HELP
from keys import KEYS

# Typeinfo constants - to be removed.
from typeinfo import PACKAGES
from typeinfo import DOCUMENT_TYPES
from typeinfo import CLASSES
from typeinfo import CLASS_PROPERTIES
from typeinfo import CLASS_OWN_PROPERTIES
from typeinfo import SUB_CLASSES
from typeinfo import SUB_CLASSED
from typeinfo import BASE_CLASSES
from typeinfo import BASE_CLASSED
from typeinfo import CLASS_HIERACHY_DEPTH
from typeinfo import ENUMS
from typeinfo import TOTAL_CLASS_PROPERTIES
from typeinfo import TOTAL_ENUM_MEMBERS
from typeinfo import CONSTRAINTS
from typeinfo import TOTAL_CONSTRAINTS
from typeinfo import TYPES



# Ontology name.
NAME = 'cim'

# Version identifier.
VERSION = '1'

# Full ontology name.
FULL_NAME = 'cim.1'
