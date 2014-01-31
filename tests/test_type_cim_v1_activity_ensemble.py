import pyesdoc.ontologies.cim as cim
from . import test_utils as tu



# Test type.
DOC_TYPE = cim.v1.Ensemble

# Test representation file.
DOC_FILE = 'xml-metafor-cim-v1/cim.1.activity.Ensemble.xml'

# Test document uid.
DOC_UID = 'fd46d094-6fdb-11e1-825e-00163e9152a5'

# Test document version.
DOC_VERSION = '1'

# Test document creation date.
DOC_DATE = '2012-03-17 02:50:59.407620'


def assert_doc(doc):
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


    assert doc.long_name.startswith('historical (no-AIE), GISS-E2-R')
    assert doc.short_name == 'historicalNoAIE GISS-E2-R p1'
    assert doc.description.startswith('Each simulation was started from 20')
    assert len(doc.types) == 1
    assert doc.types[0] == "Initial Condition"
    assert_members()
    assert_member_simulation_reference()
    assert_member_change()


def update_doc(doc):
    pass


def assert_doc_updates(doc):
    pass