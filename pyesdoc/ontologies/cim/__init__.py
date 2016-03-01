# -*- coding: utf-8 -*-
"""
.. module:: cim.__init__.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The cim package initializer.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2013-04-17 13:14:13.903808.

"""
import v1
import v2

from v1.typeset import *
from v2.typeset import *


# Ontology name.
NAME = 'cim'

# Ontology versions.
VERSIONS = (v1, v2)

# Ontology types.
TYPES = v1.TYPES + v2.TYPES

# Ontology type keys.
TYPE_KEYS = {}
TYPE_KEYS.update(v1.TYPE_KEYS)
TYPE_KEYS.update(v2.TYPE_KEYS)

# Ontology constraints.
CONSTRAINTS = {}
CONSTRAINTS.update(v1.CONSTRAINTS)
CONSTRAINTS.update(v2.CONSTRAINTS)
