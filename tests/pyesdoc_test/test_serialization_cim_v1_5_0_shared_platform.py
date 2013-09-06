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

import pyesdoc
import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



# Test type.
_TEST_TYPE = cim.v1.Platform

# Test representation file.
_TEST_FILE = 'cim/v1_5_0/shared.platform.xml'


def _assert_doc(doc):
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.assert_pyesdoc_obj(doc, 'b765775a-e2ac-11df-9efb-00163e9152a5', '1', '2012-03-01 13:55:56.232228')

    assert doc.description is None
    assert doc.long_name == 'Machine IBM Power 6 and compiler Other'
    assert doc.short_name == 'IBM Power 6_Other'

    assert len(doc.contacts) == 1
    assert doc.contacts[0].abbreviation == 'MOHC'
    assert doc.contacts[0].organisation_name == 'UK Met Office Hadley Centre'
    assert doc.contacts[0].role == 'contact'

    assert len(doc.units) == 1
    assert doc.units[0].machine is not None
    assert doc.units[0].machine.cores_per_processor == 32
    assert doc.units[0].machine.description is None
    assert doc.units[0].machine.interconnect == 'Infiniband'
    assert doc.units[0].machine.name == 'IBM Power 6'
    assert len(doc.units[0].machine.libraries) == 0
    assert doc.units[0].machine.location is None
    assert doc.units[0].machine.maximum_processors == 2
    assert doc.units[0].machine.operating_system == 'AIX'
    assert doc.units[0].machine.system == 'Parallel'
    assert doc.units[0].machine.type is None
    assert doc.units[0].machine.vendor == 'IBM'
    assert doc.units[0].machine.processor_type == 'Other'
    assert len(doc.units[0].compilers) == 1
    assert doc.units[0].compilers[0].environment_variables is None
    assert doc.units[0].compilers[0].language is None
    assert doc.units[0].compilers[0].name == 'Other'
    assert doc.units[0].compilers[0].options is None
    assert doc.units[0].compilers[0].type is None
    assert doc.units[0].compilers[0].version == '12.1.0.0'


def test_open_test_file():
    assert tu.get_test_file(_TEST_FILE) is not None


def test_serialize():
    for encoding in pyesdoc.ESDOC_ENCODINGS:
        tu.serialize.description = "{0}.test_serialize.{1}".format(__name__, encoding)
        yield tu.serialize, encoding, _TEST_FILE, _TEST_TYPE, _assert_doc
