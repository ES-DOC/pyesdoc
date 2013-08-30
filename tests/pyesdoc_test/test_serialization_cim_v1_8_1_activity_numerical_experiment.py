"""
.. module:: test_decoding_cim_v1_8_1_activity_numerical_experiment.py
   :copyright: Copyright "Aug 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Tests a cim v1.8.1 activity numerical experiment document.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import nose
import uuid

from dateutil import parser as dateutil_parser

import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



# Test type.
_TEST_TYPE = cim.v1.NumericalExperiment

# Test representation file.
_TEST_FILE = 'cim/v1_8_1/activity.numerical_experiment.xml'


def test_open_test_file():
    assert tu.get_test_file(_TEST_FILE) is not None


def test_decode_from_xml_metafor_cim_v1():
    obj = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.assert_pyesdoc_obj(obj, 'b464433a-d3a5-11df-837f-00163e9152a5', '2', '2012-03-06 10:06:42.266723')

    assert obj.long_name == 'RCP2.6'
    assert obj.short_name == 'rcp26'
    assert obj.description.startswith('Future projection (2006-2100) forced by RCP2.6.')

    assert len(obj.rationales) == 1
    assert obj.rationales[0].startswith('Provide estimate of future antrhopogenic')

    assert obj.experiment_id == '4.3'

    assert len(obj.requirements) == 9
    for requirement in obj.requirements:
        if requirement.id == 'ic.004':
            assert isinstance(requirement, cim.v1.InitialCondition)
            assert requirement.name == '4.3.ic'
            assert requirement.description.startswith('Initial conditions are from the end of')
        elif requirement.id == '4.3.bc.wmg':
            assert isinstance(requirement, cim.v1.BoundaryCondition)
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
            assert isinstance(requirement, cim.v1.LateralBoundaryCondition)
        elif requirement.id == 'stc.030':
            assert isinstance(requirement, cim.v1.SpatioTemporalConstraint)


@nose.tools.raises(NotImplementedError)
def test_encode_xml_metafor_cim_v1():
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.encode_to_xml_metafor_cim_v1(doc)


def test_decode_dict():
    doc1 = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    as_dict = tu.encode_to_dict(doc1)

    doc = tu.decode_from_dict(as_dict)


def test_encode_dict():
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    d = tu.encode_to_dict(doc)


def test_decode_json():
    doc1 = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    as_json = tu.encode_to_json(doc1)

    doc = tu.decode_from_json(as_json)


def test_encode_json():
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.encode_to_json(doc)


@nose.tools.raises(NotImplementedError)
def test_decode_xml():
    doc1 = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    as_xml = tu.encode_to_xml(doc1)

    doc = tu.decode_from_xml(as_xml)


def test_encode_xml():
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.encode_to_xml(doc)
