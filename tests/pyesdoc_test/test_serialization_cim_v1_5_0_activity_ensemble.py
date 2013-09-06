"""
.. module:: test_decoding_cim_v1_5_0_activity_ensemble.py
   :copyright: Copyright "Aug 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Tests a cim v1.5.0 activity ensemble document.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
import pyesdoc
# Module imports.
import nose

import pyesdoc
import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



# Test type.
_TEST_TYPE = cim.v1.Ensemble

# Test representation file.
_TEST_FILE = 'cim/v1_5_0/activity.ensemble.xml'



def _assert_doc(doc):
    def assert_member(m, is_open, value):
        assert m.ensemble_ids[0].is_open == is_open
        assert m.ensemble_ids[0].value == value

    def assert_member_simulation_reference():
        ref = doc.members[1].simulation_reference
        tu.assert_uuid(ref.id, "80509692-6fdb-11e1-9bbb-00163e9152a5")
        assert ref.name == "historicalNoAIE GISS-E2-R p1"
        assert ref.type == "simulation"
        assert ref.version == "1"
        assert ref.description == "Reference to a simulation called historicalNoAIE GISS-E2-R p1"
        assert len(ref.changes) == 1

    def assert_member_change():
        change = doc.members[1].simulation_reference.changes[0]
        assert change.name == "IC mod"
        assert change.type == "InitialCondition"
        tu.assert_date(change.date, "1850-01-01T00:00:00Z")
        assert len(change.details) == 1
        assert(change.details[0].description == "ICs come from different points in the control run")

    def assert_members():
        assert len(doc.members) == 5
        assert_member(doc.members[0], True, "r1i1p1")
        assert_member(doc.members[1], True, "r2i1p1")
        assert_member(doc.members[2], True, "r3i1p1")
        assert_member(doc.members[3], True, "r4i1p1")
        assert_member(doc.members[4], True, "r5i1p1")


    tu.assert_pyesdoc_obj(doc, 'fd46d094-6fdb-11e1-825e-00163e9152a5', '1', '2012-03-17 02:50:59.407620')
    assert doc.long_name.startswith('historical (no-AIE), GISS-E2-R')
    assert doc.short_name == 'historicalNoAIE GISS-E2-R p1'
    assert doc.description.startswith('Each simulation was started from 20')
    assert len(doc.types) == 1
    assert doc.types[0] == "Initial Condition"
    assert_members()
    assert_member_simulation_reference()
    assert_member_change()


def test_open_test_file():
    assert tu.get_test_file(_TEST_FILE) is not None


def test_serialize():
    for encoding in pyesdoc.ESDOC_ENCODINGS:
        tu.serialize.description = "{0}.test_serialize.{1}".format(__name__, encoding)
        yield tu.serialize, encoding, _TEST_FILE, _TEST_TYPE, _assert_doc
