# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.__init__.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Package initializer.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from .constants import *
from .factory import (
    create
    )
from .io import (
    write,
    read,
    convert as convert_file
    )
from .ontologies import (
    associate,
    get_types,
    is_supported,
    list_types
    )
from .options import (
    set_option,
    get_option,
    list_options
    )
from .extensions import (
    extend,
    is_extendable
    )
from .publishing import (
    publish,
    retrieve,
    unpublish
    )
from .serialization import (
    convert,
    decode,
    encode,
    PYESDOC_XMLError,
    )
from .utils import (
    PYESDOC_Exception,
    runtime as rt,
    config
    )
from .validation import (
    is_valid,
    validate
    )

from . import archive
from . import io
from . import ontologies
from . import options
from . import publishing
from . import serialization
from . import utils
from . import validation


# Module exports.
__all__ = [
    'create',
    'decode',
    'encode',
    'ESDOC_DEFAULT_ENCODING',
    'ESDOC_DEFAULT_LANGUAGE',
    'ESDOC_DOC_VERSION_LATEST',
    'ESDOC_DOC_VERSION_ALL',
    'ESDOC_ENCODINGS',
    'ESDOC_ENCODINGS_CUSTOM',
    'ESDOC_ENCODING_DICT',
    'ESDOC_ENCODING_JSON',
    'ESDOC_ENCODING_XML',
    'get_option',
    'io',
    'is_supported',
    'is_valid',
    'list_options',
    'list_types',
    'METAFOR_CIM_XML_ENCODING',
    'ontologies',
    'publish',
    'PYESDOC_Exception',
    'retrieve',
    'set_option',
    'unpublish',
    'validate',
]


# Standard package info.
__title__ = 'pyesdoc'
__version__ = '0.9.1.0'
__author__ = 'ES-DOC'
__license__ = 'GPL'
__copyright__ = 'Copyright 2015 ES-DOC'
