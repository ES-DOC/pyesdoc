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
FILE = 'activity.ensemble_1.xml'


class TestDecodeEnsemble_1(unittest.TestCase):
    """A decoding from xml unit test.

    """
    def test_open_xml(self):
        xml = get_test_file(SCHEMA, SCHEMA_VERSION, FILE)
        assert xml is not None


    def test_decode_obj_from_xml(self):
        obj = decode_obj_from_xml(SCHEMA, SCHEMA_VERSION, FILE, TYPE)

        def assert_overview():
            assert obj.long_name.startswith('Simulation using HIRAM-C360 using future SSTs and RCP 4.5')
            assert obj.short_name == 'sst2030 hiram-c360'
            assert obj.description.startswith('Additional ensemble members were started')
            assert len(obj.types) == 1
            assert obj.types[0] == "Mixed"

        def assert_member(m, is_open, value):
            assert m.ensemble_ids[0].is_open == is_open
            assert m.ensemble_ids[0].value == value

        def assert_member_changes():
            assert len(obj.members[1].simulation_reference.changes) == 2
            
            change = obj.members[1].simulation_reference.changes[0]
            assert change.name == "sea-ice thickness ESM2M"
            assert change.type == "ParameterChange"
            assert change.date is None
            assert len(change.details) == 1
            assert change.details[0].description.startswith("Model was run in AMIP mode with SST")
            assert change.details[0].name == "ice_thickness"
            assert change.details[0].value == "1.74"
            
            change = obj.members[1].simulation_reference.changes[1]
            assert change.name == "IC_C360_F2p1"
            assert change.type == "InitialCondition"
            assert_date(change.date, "2026-01-01T00:00:00Z")
            assert len(change.details) == 1
            assert change.details[0].description.startswith("Initial condition for C360 AMIP")

        def assert_members():
            assert len(obj.members) == 6
            assert_member(obj.members[0], True, "r1i1p1")
            assert_member(obj.members[1], True, "r2i1p1")
            assert_member(obj.members[2], True, "r3i1p1")
            assert_member(obj.members[3], True, "r1i1p2")
            assert_member(obj.members[4], True, "r2i1p2")
            assert_member(obj.members[5], True, "r3i1p2")

        assert_cim(obj, 'f943c050-616d-11e1-bd49-00163e9152a5', '1', '2012-05-17 14:20:29.446090')
        assert_overview()
        assert_members()
        assert_member_changes()
        

    def test_representation_dict(self):
        d = decode_dict_from_xml(SCHEMA, SCHEMA_VERSION, FILE, TYPE)
        assert d is not None
        assert isinstance(d, dict) == True

        # TODO
        




