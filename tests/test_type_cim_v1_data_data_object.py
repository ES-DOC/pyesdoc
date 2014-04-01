from dateutil import parser as dateutil_parser

import pyesdoc.ontologies.cim as cim
import test_utils as tu



# Test type.
DOC_TYPE = cim.v1.DataObject

# Test representation file.
DOC_FILE = 'cim.1.data.DataObject.xml-metafor-cim-v1'

# Test document uid.
DOC_UID = '8e92715a-5176-11e0-9919-00163e9152a5'

# Test document version.
DOC_VERSION = '1'

# Test document creation date.
DOC_DATE = '2012-04-23 14:59:07.146365'

# Test document project.
DOC_PROJECT = "CMIP5"

# Test document project.
DOC_INSTITUTE = "MOHC"

# Test document author.
DOC_AUTHOR = "Metafor Questionnaire"


def assert_doc(doc):
    return
    
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


def update_doc(doc):
    pass


def assert_doc_updates(doc):
    pass