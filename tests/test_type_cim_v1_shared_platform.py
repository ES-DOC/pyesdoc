# -*- coding: utf-8 -*-

"""
.. module:: test_type_cim_v1_shared_platform.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Tests a cim.v1.Platform instance.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import arrow

import pyesdoc.ontologies.cim as cim
import test_utils as tu



# Test type.
DOC_TYPE = cim.v1.Platform

# Test type display name.
DOC_TYPE_DISPLAY_NAME = "Platform"

# Test document type.
DOC_TYPE_KEY = DOC_TYPE.type_key

# Test representation file.
DOC_FILE = 'cim.1.shared.Platform.xml-metafor-cim-v1'

# Test document uid.
DOC_UID = 'b765775a-e2ac-11df-9efb-00163e9152a5'

# Test document version.
DOC_VERSION = '1'

# Test document creation date.
DOC_DATE = arrow.get('2012-04-23 14:59:07.049089').datetime

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
    tu.assert_str(ext.display_name, "IBM Power 6_Other")
    tu.assert_str(ext.description, "Machine IBM Power 6", True)
    tu.assert_str(ext.full_display_name, "CMIP5 Platform : MOHC - IBM Power 6_Other")
    tu.assert_int(ext.summary_fields, 2)
    tu.assert_str(ext.summary_fields[0], "IBM Power 6_Other")
    tu.assert_str(ext.summary_fields[1], "Machine IBM Power 6", True)


def _assert_doc_core(doc, is_update):
    """Assert core information."""
    tu.assert_str(doc.long_name, "Machine IBM Power 6 and compiler Other")
    tu.assert_str(doc.short_name, "IBM Power 6_Other")
    tu.assert_iter(doc.contacts, 1, cim.v1.ResponsibleParty)
    tu.assert_str(doc.contacts[0].abbreviation, "MOHC")
    tu.assert_str(doc.contacts[0].organisation_name, "UK Met Office Hadley Centre")
    tu.assert_str(doc.contacts[0].role, "contact")
    tu.assert_iter(doc.units, 1, cim.v1.MachineCompilerUnit)


def _assert_doc_machine(doc, is_update):
    """Assert machine information."""
    tu.assert_object(doc.units[0].machine, cim.v1.Machine)
    m = doc.units[0].machine
    tu.assert_int(m.cores_per_processor, 32)
    tu.assert_str(m.interconnect, "Infiniband")
    tu.assert_str(m.name, "IBM Power 6")
    tu.assert_iter(m.libraries, 0)
    tu.assert_int(m.maximum_processors, 2)
    tu.assert_str(m.operating_system, "AIX")
    tu.assert_str(m.system, "Parallel")
    tu.assert_str(m.vendor, "IBM")
    tu.assert_str(m.processor_type, "Other")


def _assert_doc_compiler(doc, is_update):
    """Assert compiler information."""
    tu.assert_iter(doc.units[0].compilers, 1, cim.v1.Compiler)
    c = doc.units[0].compilers[0]
    tu.assert_str(c.name, "Other")
    tu.assert_str(c.version, "12.1.0.0")


def assert_doc(doc, is_update=False):
    """Asserts a document.

    :param object doc: Document being tested.
    :param bool is_update: Flag indicating whether document has been updated.

    """
    for assertor in (
        _assert_doc_core,
        _assert_doc_machine,
        _assert_doc_compiler,
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