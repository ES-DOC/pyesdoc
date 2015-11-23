# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.__init__.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Package initializer.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Standard package info.
__title__ = 'pyesdoc'
__version__ = '0.9.3.8'
__author__ = 'ES-DOC'
__license__ = 'GPL'
__copyright__ = 'Copyright 2015 ES-DOC'


from pyesdoc.constants import *
from pyesdoc.exceptions import *
from pyesdoc.factory import create
from pyesdoc.io import convert as convert_file
from pyesdoc.io import read
from pyesdoc.io import write
from pyesdoc.ontologies import associate
from pyesdoc.ontologies import get_types
from pyesdoc.ontologies import is_supported
from pyesdoc.ontologies import list_types
from pyesdoc.options import set_option
from pyesdoc.options import get_option
from pyesdoc.options import list_options
from pyesdoc.extensions import extend
from pyesdoc.extensions import is_extendable
from pyesdoc.publishing import publish
from pyesdoc.publishing import retrieve
from pyesdoc.publishing import unpublish
from pyesdoc.serialization import convert
from pyesdoc.serialization import decode
from pyesdoc.serialization import encode
from pyesdoc.utils import runtime as rt
from pyesdoc.utils import config
from pyesdoc.validation import is_valid
from pyesdoc.validation import validate

from pyesdoc import archive
from pyesdoc import io
from pyesdoc import ontologies
from pyesdoc import options
from pyesdoc import publishing
from pyesdoc import serialization
from pyesdoc import utils
from pyesdoc import validation


