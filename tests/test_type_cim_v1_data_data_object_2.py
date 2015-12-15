# -*- coding: utf-8 -*-

"""
.. module:: test_type_cim_v1_data_data_object_2.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Tests a cim.v1.DataObject instance.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import arrow

import pyesdoc.ontologies.cim as cim
import test_utils as tu



# Test type.
DOC_TYPE = cim.v1.DataObject

# Test type display name.
DOC_TYPE_DISPLAY_NAME = "Data Object"

# Test document type.
DOC_TYPE_KEY = DOC_TYPE.type_key + '-2'

# Test representation file.
DOC_FILE = 'cim.1.data.DataObject-2.xml-metafor-cim-v1'

# Test document uid.
DOC_UID = '834151a4-978d-4627-954e-285916bb907a'

# Test document version.
DOC_VERSION = '1'

# Test document creation date.
DOC_DATE = arrow.get('2011-09-28 16:08:41').datetime

# Test document project.
DOC_PROJECT = "CMIP5"

# Test document project.
DOC_INSTITUTE = "MOHC"

# Test document author.
DOC_AUTHOR = "Metafor Questionnaire"


def _assert_doc_core(doc, is_update):
    """Assert core information."""
    tu.assert_iter(doc.citations, 2, cim.v1.Citation)


def _assert_doc_content(doc, is_update):
    """Assert content information."""
    tu.assert_iter(doc.content, 1, cim.v1.DataContent)
    c = doc.content[0]
    tu.assert_str(c.aggregation, "sum")
    tu.assert_str(c.frequency, "Other")


def _assert_doc_data_properties(doc, is_update):
    """Assert properties."""
    tu.assert_iter(doc.properties, 2, cim.v1.DataProperty)
    p = doc.properties[0]
    tu.assert_str(p.name, "TestProperty1")
    tu.assert_str(p.value, "1")


def _assert_doc_distribution(doc, is_update):
    """Assert distribution information."""
    tu.assert_object(doc.distribution, cim.v1.DataDistribution)
    tu.assert_str(doc.distribution.access, "OnlineFileHTTP")
    tu.assert_str(doc.distribution.format, "NetCDF")
    tu.assert_object(doc.distribution.responsible_party, cim.v1.ResponsibleParty)


def _assert_doc_extent(doc, is_update):
    """Assert extent information."""
    tu.assert_object(doc.extent, cim.v1.DataExtent)
    e = doc.extent
    tu.assert_object(e.geographical, cim.v1.DataExtentGeographical)
    tu.assert_float(e.geographical.east, 360.0)
    tu.assert_float(e.geographical.north, 90.0)
    tu.assert_float(e.geographical.south, -90.0)
    tu.assert_object(e.temporal, cim.v1.DataExtentTemporal)
    tu.assert_date(e.temporal.begin, "1859-12-01 00:00:00")
    tu.assert_date(e.temporal.end, "1999-12-30 00:00:00")
    tu.assert_object(e.temporal.time_interval, cim.v1.DataExtentTimeInterval)
    ti = e.temporal.time_interval
    tu.assert_int(ti.factor, -1)
    tu.assert_int(ti.radix, 50430)
    tu.assert_str(ti.unit, "day")


def _assert_doc_hierarchy_level(doc, is_update):
    """Assert hierarchy level information."""
    tu.assert_object(doc.hierarchy_level, cim.v1.DataHierarchyLevel)
    h = doc.hierarchy_level
    tu.assert_bool(h.is_open, True)
    tu.assert_str(h.name, "experiment")
    tu.assert_str(h.value, "HADGEM2_20C3M_1_D0_hus700")


def assert_doc(doc, is_update=False):
    """Asserts a document.

    :param object doc: Document being tested.
    :param bool is_update: Flag indicating whether document has been updated.

    """
    for assertor in (
        _assert_doc_core,
        _assert_doc_content,
        _assert_doc_data_properties,
        _assert_doc_extent,
        _assert_doc_hierarchy_level,
        ):
        assertor(doc, is_update)


def assert_doc1(doc, meta, ext):
    """Asserts a document.

    :param object doc: Document being tested.
    :param object meta: Document meta information.
    :param object ext: Document extension information.

    """
    return
    assert doc.child_object == []
    for i in range(1):
        c = doc.citations[i]
        assert c is not None
        assert isinstance(c, cim.v1.Citation)
        assert c.title.startswith(str(i + 1) + ' - ')
        assert c.date == arrow.get('2009-02-11').datetime
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
    assert doc.extent.temporal.begin == arrow.get('1859-12-1').datetime
    assert doc.extent.temporal.end == arrow.get('1999-12-30').datetime
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