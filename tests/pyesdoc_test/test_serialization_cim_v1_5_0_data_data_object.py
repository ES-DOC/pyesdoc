"""
.. module:: test_decoding_cim_v1_5_0_data_data_object.py
   :copyright: Copyright "Aug 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Tests a cim v1.5.0 data data object document.

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
_TEST_TYPE = cim.v1.DataObject

# Test representation file.
_TEST_FILE = 'cim/v1_5_0/data.data_object.xml'


def _assert_doc(doc):
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.assert_pyesdoc_obj(doc, '834151a4-978d-4627-954e-285916bb907a', '1', '2011-09-28T16:08:41')

    assert doc.acronym == 'HADGEM2_20C3M_1_D0_hus700'
    assert doc.child_object == []
    for i in range(1):
        c = doc.citations[i]
        assert c is not None
        assert isinstance(c, cim.v1.Citation)
        assert c.title.startswith(str(i + 1) + ' - ')
        assert c.date == dateutil_parser.parse('2009-02-11')
    assert len(doc.content) == 1
    assert doc.content[0].aggregation == 'sum'
    assert doc.content[0].frequency == 'Other'
    assert doc.content[0].topic.name == 'specific_humidity'
    assert doc.content[0].topic.description.find('specific" means per unit mass') >= 0
    assert doc.content[0].topic.unit == 'm s-1'
    for i in range(1):
        dp = doc.data_property[i]
        assert isinstance(dp, cim.v1.DataProperty)
        assert dp.name == 'TestProperty' + str(i + 1)
        assert dp.value == str(i + 1)
    assert doc.data_status == 'complete'
    assert doc.description.startswith('This dataset represents daily output: instantaneous daily')
    assert doc.distribution.access == 'OnlineFileHTTP'
    assert doc.distribution.format == 'NetCDF'
    assert doc.distribution.responsible_party.individual_name == 'Met Office (HC)'
    assert doc.distribution.responsible_party.organisation_name == 'Hadley Centre'
    assert doc.distribution.responsible_party.role == 'distributor'
    assert doc.extent.geographical.east == float(360)
    assert doc.extent.geographical.south == float(-90)
    assert doc.extent.geographical.west == float(0)
    assert doc.extent.geographical.north == float(90)
    assert doc.extent.temporal.begin == dateutil_parser.parse('1859-12-1')
    assert doc.extent.temporal.end == dateutil_parser.parse('1999-12-30')
    assert doc.extent.temporal.time_interval.factor == int(-1)
    assert doc.extent.temporal.time_interval.radix == int(50430)
    assert doc.extent.temporal.time_interval.unit == 'day'
    # TODO set type correctly
    # assert obj.geometry_model is None
    assert doc.hierarchy_level.name == 'experiment'
    assert doc.hierarchy_level.value == 'HADGEM2_20C3M_1_D0_hus700'
    assert doc.hierarchy_level.is_open == True
    assert doc.keyword == 'Test keyword'
    assert doc.parent_object is None
    assert doc.parent_object_reference is None
    assert doc.purpose == 'test'
    assert len(doc.restriction) == 0
    # TODO set type correctly
    # assert obj.source_simulation is None
    assert len(doc.storage) == 0


def test_open_test_file():
    assert tu.get_test_file(_TEST_FILE) is not None


def test_serialize():
    for encoding in pyesdoc.ESDOC_ENCODINGS:
        tu.serialize.description = "{0}.test_serialize.{1}".format(__name__, encoding)
        yield tu.serialize, encoding, _TEST_FILE, _TEST_TYPE, _assert_doc
