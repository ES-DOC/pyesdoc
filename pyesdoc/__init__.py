# -*- coding: utf-8 -*-
#                            __
#  _ __  _   _  ___  ___  __| | ___   ___
# | '_ \| | | |/ _ \/ __|/ _` |/ _ \ / __|
# | |_) | |_| |  __/\__ \ (_| | (_) | (__
# | .__/ \__, |\___||___/\__,_|\___/ \___|
# |_|    |___/
#
"""
.. module:: pyesdoc.__init__.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Package initializer.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
__title__ = 'pyesdoc'
__version__ = '0.14.0.0'
__author__ = 'ES-DOC'
__license__ = 'GPL'
__copyright__ = 'Copyright 2018 ES-DOC'


from pyesdoc import archive
from pyesdoc import constants
from pyesdoc import drq
from pyesdoc import exceptions
from pyesdoc import mp
from pyesdoc import ontologies
from pyesdoc import utils

from pyesdoc._associating import associate
from pyesdoc._associating import associate_by_id
from pyesdoc._associating import associate_by_id_and_version
from pyesdoc._associating import associate_by_name

from pyesdoc._extensions import extend
from pyesdoc._extensions import is_extendable

from pyesdoc._factory import create

from pyesdoc._io import convert as convert_file
from pyesdoc._io import get_filename
from pyesdoc._io import read
from pyesdoc._io import seek
from pyesdoc._io import write

from pyesdoc.mp.specializations.utils_cache import get_topic_specialization
from pyesdoc.mp.specializations.utils_cache import get_property_specialization

from pyesdoc._publishing import publish
from pyesdoc._publishing import retrieve
from pyesdoc._publishing import unpublish

from pyesdoc._search import search
from pyesdoc._search import SearchResult
from pyesdoc._search import SearchResultItem

from pyesdoc._security import authenticate_user
from pyesdoc._security import AuthenticationError
from pyesdoc._security import authorize_user
from pyesdoc._security import AuthorizationError
from pyesdoc._security import strip_credentials

from pyesdoc._serialization import convert
from pyesdoc._serialization import decode
from pyesdoc._serialization import encode

from pyesdoc.utils import config
from pyesdoc.utils.logger import log
from pyesdoc.utils.logger import log_error
from pyesdoc.utils.logger import log_warning

from pyesdoc._validation import is_valid
from pyesdoc._validation import validate
