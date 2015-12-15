# -*- coding: utf-8 -*-

"""
.. module:: test_type_cim_v1_data_data_object_1.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Tests a cim.v1.DataObject instance.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import arrow

import pyesdoc.ontologies.cim as cim
import test_utils as tu



# Test type.
DOC_TYPE = cim.v1.DataObject

# Test type display name.
DOC_TYPE_DISPLAY_NAME = "Data Object"

# Test document type.
DOC_TYPE_KEY = DOC_TYPE.type_key + '-1'

# Test representation file.
DOC_FILE = 'cim.1.data.DataObject-1.xml-metafor-cim-v1'

# Test document uid.
DOC_UID = '8e92715a-5176-11e0-9919-00163e9152a5'

# Test document version.
DOC_VERSION = '1'

# Test document creation date.
DOC_DATE = arrow.get('2012-04-23 14:59:07.146365').datetime

# Test document project.
DOC_PROJECT = "CMIP5"

# Test document project.
DOC_INSTITUTE = "MOHC"

# Test document author.
DOC_AUTHOR = "Metafor Questionnaire"


def assert_extension_info(ext):
    """Asserts a document's extension information.

    :param object ext: Document extension information.

    """
    tu.assert_str(ext.display_name, "fossil_fuel_organic_carbon")
    tu.assert_str(ext.description, "2D gridded monthly-mean", True)
    tu.assert_str(ext.full_display_name, "CMIP5 Data Object : MOHC - fossil_fuel_organic_carbon")
    tu.assert_int(ext.summary_fields, 2)
    tu.assert_str(ext.summary_fields[0], "fossil_fuel_organic_carbon")
    tu.assert_str(ext.summary_fields[1], "2D gridded monthly-mean", True)


def _assert_doc_core(doc, is_update):
    """Assert core information."""
    tu.assert_str(doc.acronym, "fossil_fuel_organic_carbon")
    tu.assert_str(doc.data_status, "complete")
    tu.assert_str(doc.description, "2D gridded monthly-mean", True)
    tu.assert_iter(doc.storage, 1)
    storage = doc.storage[0]
    tu.assert_object(storage, cim.v1.DataStorageIp)
    tu.assert_str(storage.format, "ASCII")
    tu.assert_str(storage.file_name, "emissions of organic", True)


def _assert_doc_content(doc, is_update):
    """Assert content information."""
    tu.assert_iter(doc.content, 1, cim.v1.DataContent)
    c = doc.content[0]
    tu.assert_object(c.topic, cim.v1.DataTopic)
    tu.assert_str(c.topic.description, "missing CF name: tendency_of", True)
    tu.assert_str(c.topic.name, "fossil_fuel_organic_carbon")


def assert_doc(doc, is_update=False):
    """Asserts a document.

    :param object doc: Document being tested.
    :param bool is_update: Flag indicating whether document has been updated.

    """
    for assertor in (
        _assert_doc_core,
        _assert_doc_content,
        ):
        assertor(doc, is_update)


def update_doc(doc):
    """Update a document prior to republishing.

    :param object doc: Document being republished.

    """
    pass


def assert_doc_updates(doc):
    """Asserts a document after being updated.

    :param object doc: Document being tested.

    """
    pass