# -*- coding: utf-8 -*-

"""
.. module:: test_type_cim_v1_activity_ensemble_1.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Tests a cim.v1.Ensemble instance.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import arrow

import pyesdoc.ontologies.cim as cim
import test_utils as tu



# Test type.
DOC_TYPE = cim.v1.Ensemble

# Test type display name.
DOC_TYPE_DISPLAY_NAME = "Ensemble"

# Test document type.
DOC_TYPE_KEY = DOC_TYPE.type_key + '-1'

# Test representation file.
DOC_FILE = 'cim.1.activity.Ensemble-1.xml-metafor-cim-v1'

# Test document uid.
DOC_UID = '4c95e1c8-5d79-11e1-83af-00163e9152a5'

# Test document version.
DOC_VERSION = '1'

# Test document creation date.
DOC_DATE = arrow.get('2012-04-23 14:59:07.019144').datetime

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
    tu.assert_str(ext.display_name, u"amip")
    tu.assert_str(ext.description, u"Six element ensemble", True)
    tu.assert_str(ext.full_display_name, u"CMIP5 Ensemble : MOHC - amip")
    tu.assert_int(ext.summary_fields, 2)
    tu.assert_str(ext.summary_fields[0], u"amip")
    tu.assert_str(ext.summary_fields[1], u"3.3 AMIP and AMIP Ensemble")


def _assert_doc_core(doc, is_update):
    """Assert core information."""
    if not is_update:
        tu.assert_str(doc.description, "Six element ensemble", True)
    tu.assert_iter(doc.members, 6, cim.v1.EnsembleMember)
    tu.assert_str(doc.long_name, "3.3 AMIP and AMIP Ensemble")
    tu.assert_str(doc.short_name, "amip")
    tu.assert_iter(doc.types, 1)
    tu.assert_str(doc.types[0], "Initial Condition")

def _assert_doc_member(doc, is_update):
    """Assert ensemble members information."""
    # ... ensemble member id.
    member = doc.members[0]
    tu.assert_iter(member.ensemble_ids, 1, cim.v1.StandardName)
    tu.assert_str(member.ensemble_ids[0].is_open, True)
    tu.assert_str(member.ensemble_ids[0].value, "r1i1p1")

    # ... ensemble member simulation reference.
    tu.assert_object(member.simulation_reference, cim.v1.DocReference)
    ref = member.simulation_reference
    tu.assert_str(ref.description, "Reference to a simulation called amip")
    tu.assert_uuid(ref.id, "e4155a28-268e-11e1-9a0e-00163e9152a5")
    tu.assert_str(ref.name, "amip")
    tu.assert_str(ref.type, "simulation")
    tu.assert_str(ref.version, 2)


def assert_doc(doc, is_update=False):
    """Asserts a document.

    :param object doc: Document being tested.
    :param bool is_update: Flag indicating whether document has been updated.

    """
    for assertor in (
        _assert_doc_core,
        _assert_doc_member,
        ):
        assertor(doc, is_update)


def update_doc(doc):
    """Update a document prior to republishing.

    :param object doc: Document being republished.

    """
    doc.description = "X"


def assert_doc_updates(doc):
    """Asserts a document after being updated.

    :param object doc: Document being tested.

    """
    tu.assert_str(doc.description, "X")
