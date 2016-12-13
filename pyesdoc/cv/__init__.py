# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.cv.__init__.py

   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL / CeCILL
   :platform: Unix
   :synopsis: Python earth science standard vocabulary package intializer.

.. moduleauthor:: IPSL (ES-DOC) <dev@esdocumentation.org>

"""
from pyesdoc.cv import archive
from pyesdoc.cv.io_mgr import read_authority
from pyesdoc.cv.io_mgr import write_authority
from pyesdoc.cv.codecs import from_dict
from pyesdoc.cv.codecs import from_json
from pyesdoc.cv.codecs import to_dict
from pyesdoc.cv.codecs import to_json
from pyesdoc.cv.constants import *
from pyesdoc.cv.exceptions import *
from pyesdoc.cv.factory import create_authority
from pyesdoc.cv.factory import create_scope
from pyesdoc.cv.factory import create_collection
from pyesdoc.cv.factory import create_term
from pyesdoc.cv.model import Term
from pyesdoc.cv.model import Authority
from pyesdoc.cv.model import Collection
from pyesdoc.cv.model import Scope


