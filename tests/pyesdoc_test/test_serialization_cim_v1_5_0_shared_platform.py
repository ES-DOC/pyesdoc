"""
.. module:: test_decoding_cim_v1_5_0_shared_platform.py
   :copyright: Copyright "Aug 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Tests a cim v1.5.0 shared platform document.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import nose
import uuid

from dateutil import parser as dateutil_parser

import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



# Test type.
_TEST_TYPE = cim.v1.Platform

# Test representation file.
_TEST_FILE = 'cim/v1_5_0/shared.platform.xml'


def test_open_test_file():
    assert tu.get_test_file(_TEST_FILE) is not None


def test_decode_from_xml_metafor_cim_v1():
    obj = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.assert_pyesdoc_obj(obj, 'b765775a-e2ac-11df-9efb-00163e9152a5', '1', '2012-03-01 13:55:56.232228')

    assert obj.description is None
    assert obj.long_name == 'Machine IBM Power 6 and compiler Other'
    assert obj.short_name == 'IBM Power 6_Other'

    assert len(obj.contacts) == 1
    assert obj.contacts[0].abbreviation == 'MOHC'
    assert obj.contacts[0].organisation_name == 'UK Met Office Hadley Centre'
    assert obj.contacts[0].role == 'contact'

    assert len(obj.units) == 1
    assert obj.units[0].machine is not None
    assert obj.units[0].machine.cores_per_processor == 32
    assert obj.units[0].machine.description is None
    assert obj.units[0].machine.interconnect == 'Infiniband'
    assert obj.units[0].machine.name == 'IBM Power 6'
    assert len(obj.units[0].machine.libraries) == 0
    assert obj.units[0].machine.location is None
    assert obj.units[0].machine.maximum_processors == 2
    assert obj.units[0].machine.operating_system == 'AIX'
    assert obj.units[0].machine.system == 'Parallel'
    assert obj.units[0].machine.type is None
    assert obj.units[0].machine.vendor == 'IBM'
    assert obj.units[0].machine.processor_type == 'Other'
    assert len(obj.units[0].compilers) == 1
    assert obj.units[0].compilers[0].environment_variables is None
    assert obj.units[0].compilers[0].language is None
    assert obj.units[0].compilers[0].name == 'Other'
    assert obj.units[0].compilers[0].options is None
    assert obj.units[0].compilers[0].type is None
    assert obj.units[0].compilers[0].version == '12.1.0.0'


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

