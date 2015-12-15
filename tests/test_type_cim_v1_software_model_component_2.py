# -*- coding: utf-8 -*-

"""
.. module:: test_type_cim_v1_sofware_model_component.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Tests a cim.v1.ModelComponent instance.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import arrow

import pyesdoc.ontologies.cim as cim
import test_utils as tu



# Test document type.
DOC_TYPE = cim.v1.ModelComponent

# Test type display name.
DOC_TYPE_DISPLAY_NAME = "Model"

# Test document type.
DOC_TYPE_KEY = DOC_TYPE.type_key

# Test representation file.
DOC_FILE = 'cim.1.software.ModelComponent-2.xml-metafor-cim-v1'

# Test document uid.
DOC_UID = '4b29d25e-2968-11e0-8517-00163e9152a5'

# Test document version.
DOC_VERSION = '9'

# Test document creation date.
DOC_DATE = arrow.get('2013-03-22 17:54:48.178304').datetime

# Test document project.
DOC_PROJECT = "CMIP5"

# Test document project.
DOC_INSTITUTE = "IPSL"

# Test document author.
DOC_AUTHOR = "Metafor Questionnaire"


def assert_doc(doc, is_update=False):
    """Asserts a document.

    :param object doc: Document being tested.
    :param bool is_update: Flag indicating whether document has been updated.

    """
    pass
  

def update_doc(doc):
    """Update a document prior to republishing.

    :param object doc: Document being republished.

    """
    doc.long_name = "X"


def assert_doc_updates(doc):
    """Asserts a document after being updated.

    :param object doc: Document being tested.

    """
    tu.assert_str(doc.long_name, "X")


def assert_doc_extensions(doc):
    """Asserts a document after being extended.

    :param object doc: Document being tested.

    """
    pass
