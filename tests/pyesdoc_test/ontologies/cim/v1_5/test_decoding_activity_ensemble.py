"""
A set of cim related unit tests.
"""

# Module imports.
import unittest

from pyesdoc.ontologies.cim.v1_5.types import Ensemble as TYPE
from pyesdoc_test.test_utils import *


# Target schema being tested.
SCHEMA = 'cim'

# Target schema version being tested.
SCHEMA_VERSION = '1.5'

# Test representation file.
FILE = 'activity.ensemble.xml'


class TestDecodeEnsemble(unittest.TestCase):
    """A decoding from xml unit test.

    """
    def test_open_xml(self):
        xml = get_test_file(SCHEMA, SCHEMA_VERSION, FILE)
        assert xml is not None


    def test_decode_obj_from_xml(self):
        obj = decode_obj_from_xml(SCHEMA, SCHEMA_VERSION, FILE, TYPE)
        
        assert_cim(obj, 'fd46d094-6fdb-11e1-825e-00163e9152a5', '1', '2012-03-17 02:50:59.407620')

        assert obj.long_name.startswith('historical (no-AIE), GISS-E2-R')
        assert obj.short_name == 'historicalNoAIE GISS-E2-R p1'
        assert obj.description.startswith('Each simulation was started from 20')
        assert len(obj.types) == 1
        assert obj.types[0] == "Initial Condition"


        def assert_member(m, is_open, value):
            assert m.ensemble_ids[0].is_open == is_open
            assert m.ensemble_ids[0].value == value

        def assert_member_simulation_reference():
            ref = obj.members[1].simulation_reference
            assert_uuid(ref.id, "80509692-6fdb-11e1-9bbb-00163e9152a5")
            assert ref.name == "historicalNoAIE GISS-E2-R p1"
            assert ref.type == "simulation"
            assert ref.version == "1"
            assert ref.description == "Reference to a simulation called historicalNoAIE GISS-E2-R p1"
            assert len(ref.changes) == 1

        def assert_member_change():
            change = obj.members[1].simulation_reference.changes[0]
            assert change.name == "IC mod"
            assert change.type == "InitialCondition"
            assert_date(change.date, "1850-01-01T00:00:00Z")
            assert len(change.details) == 1
            assert(change.details[0].description == "ICs come from different points in the control run")

        def assert_members():
            assert len(obj.members) == 5
            assert_member(obj.members[0], True, "r1i1p1")
            assert_member(obj.members[1], True, "r2i1p1")
            assert_member(obj.members[2], True, "r3i1p1")
            assert_member(obj.members[3], True, "r4i1p1")
            assert_member(obj.members[4], True, "r5i1p1")

        assert_members()
        assert_member_simulation_reference()
        assert_member_change()
        

    def test_representation_dict(self):
        d = decode_dict_from_xml(SCHEMA, SCHEMA_VERSION, FILE, TYPE)
        assert d is not None
        assert isinstance(d, dict) == True

        # TODO
        




