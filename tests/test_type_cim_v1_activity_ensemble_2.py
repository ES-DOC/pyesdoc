# -*- coding: utf-8 -*-

"""
.. module:: test_type_cim_v1_activity_ensemble_2.py

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
DOC_TYPE_KEY = DOC_TYPE.type_key + '-2'

# Test representation file.
DOC_FILE = 'cim.1.activity.Ensemble-2.xml-metafor-cim-v1'

# Test document uid.
DOC_UID = 'fd46d094-6fdb-11e1-825e-00163e9152a5'

# Test document version.
DOC_VERSION = '1'

# Test document creation date.
DOC_DATE = arrow.get('2012-06-13 13:28:36.407863').datetime

# Test document project.
DOC_PROJECT = "CMIP5"

# Test document project.
DOC_INSTITUTE = "MOHC"

# Test document author.
DOC_AUTHOR = "Metafor Questionnaire"


def _assert_doc_member_change(doc, is_update):
    """Assert ensemble members information."""
    member = doc.members[1]
    
    tu.assert_iter(member.simulation_reference.changes, 1, cim.v1.Change)
    c = member.simulation_reference.changes[0]
    tu.assert_str(c.name, "IC mod")
    tu.assert_str(c.type, "InitialCondition")
    tu.assert_date(c.date, "1850-01-01T00:00:00Z")

    tu.assert_iter(c.details, 1, cim.v1.ChangeProperty)
    cp = c.details[0]
    tu.assert_str(cp.description, "ICs come from different points in the control run")


def assert_doc(doc, is_update=False):
    """Asserts a document.

    :param object doc: Document being tested.
    :param bool is_update: Flag indicating whether document has been updated.

    """
    for assertor in (
        _assert_doc_member_change,
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

