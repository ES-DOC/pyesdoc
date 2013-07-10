"""
A set of cim related unit tests.
"""
import pyesdoc.ontologies.cim.v1.types

# Module imports.
import datetime
from dateutil import parser as dateutil_parser
import unittest
import uuid

from pyesdoc.ontologies.cim.v1.types import NumericalExperiment as TYPE
from pyesdoc_test.test_utils import *



# Target schema being tested.
_SCHEMA_NAME = 'cim'

# Target schema version being tested.
_SCHEMA_VERSION = '1'

# Test representation file.
_TEST_FILE = '/v1_8_1/files/activity.numerical_experiment.xml'


class TestDecodeCIM_v1_8_1_NumericalExperiment(unittest.TestCase):
    """A decoding from xml unit test.

    """
    def test_open_xml(self):
        assert get_test_file(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE) is not None


    def test_decode_obj_from_xml(self):
        obj = decode_obj_from_xml(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE, TYPE)
        
        assert_cim(obj, 'b464433a-d3a5-11df-837f-00163e9152a5', '2', '2012-03-06 10:06:42.266723')

        assert obj.long_name == 'RCP2.6'
        assert obj.short_name == 'rcp26'
        assert obj.description.startswith('Future projection (2006-2100) forced by RCP2.6.')

        assert len(obj.rationales) == 1
        assert obj.rationales[0].startswith('Provide estimate of future antrhopogenic')

        assert obj.experiment_id == '4.3'

        assert len(obj.requirements) == 9
        for requirement in obj.requirements:
            if requirement.id == 'ic.004':
                assert isinstance(requirement, pyesdoc.ontologies.cim.v1.types.InitialCondition)
                assert requirement.name == '4.3.ic'
                assert requirement.description.startswith('Initial conditions are from the end of')
            elif requirement.id == '4.3.bc.wmg':
                assert isinstance(requirement, pyesdoc.ontologies.cim.v1.types.BoundaryCondition)
                assert len(requirement.options) == 2
                assert requirement.options[0].relationship == 'XOR'
                assert requirement.options[0].requirement.id == 'bc.076'
                assert requirement.options[0].requirement.name == '4.3.bc.wmg_conc'
                assert requirement.options[0].requirement.description == 'Concentrations'
                assert requirement.options[1].relationship == 'XOR'
                assert requirement.options[1].requirement.id == 'bc.080'
                assert requirement.options[1].requirement.name == '4.3.bc.wmg_em'
                assert requirement.options[1].requirement.description == 'Emissions'
            elif requirement.id == '4.3.stc.2006_94yr':
                assert requirement.description.startswith('Begin in 2006 and run')
                assert requirement.date_range is not None
                assert requirement.date_range.duration == 'P94Y'
                assert requirement.date_range.end == dateutil_parser.parse('2100-01-01 00:00:00Z')
                assert requirement.date_range.start == dateutil_parser.parse('2006-01-01 00:00:00Z')
            elif requirement.id == 'bc.093':
                assert isinstance(requirement, pyesdoc.ontologies.cim.v1.types.LateralBoundaryCondition)
            elif requirement.id == 'stc.030':
                assert isinstance(requirement, pyesdoc.ontologies.cim.v1.types.SpatioTemporalConstraint)


    def test_representation_dict(self):
        d = decode_dict_from_xml(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE, TYPE)
        assert d is not None
        assert isinstance(d, dict) == True

        # TODO
        






