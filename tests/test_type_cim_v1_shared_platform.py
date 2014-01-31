import pyesdoc.ontologies.cim as cim
from . import test_utils as tu



# Test type.
DOC_TYPE = cim.v1.Platform

# Test representation file.
DOC_FILE = 'xml-metafor-cim-v1/cim.1.shared.Platform.xml'

# Test document uid.
DOC_UID = 'b765775a-e2ac-11df-9efb-00163e9152a5'

# Test document version.
DOC_VERSION = '1'

# Test document creation date.
DOC_DATE = '2012-03-01 13:55:56.232228'


def assert_doc(doc):
    assert doc.description in [None, '']
    assert doc.long_name == 'Machine IBM Power 6 and compiler Other'
    assert doc.short_name == 'IBM Power 6_Other'

    assert len(doc.contacts) == 1
    assert doc.contacts[0].abbreviation == 'MOHC'
    assert doc.contacts[0].organisation_name == 'UK Met Office Hadley Centre'
    assert doc.contacts[0].role == 'contact'

    assert len(doc.units) == 1
    assert doc.units[0].machine is not None
    assert doc.units[0].machine.cores_per_processor == 32
    assert doc.units[0].machine.description in [None, '']
    assert doc.units[0].machine.interconnect == 'Infiniband'
    assert doc.units[0].machine.name == 'IBM Power 6'
    assert len(doc.units[0].machine.libraries) == 0
    assert doc.units[0].machine.location in [None, '']
    assert doc.units[0].machine.maximum_processors == 2
    assert doc.units[0].machine.operating_system == 'AIX'
    assert doc.units[0].machine.system == 'Parallel'
    assert doc.units[0].machine.type in [None, '']
    assert doc.units[0].machine.vendor == 'IBM'
    assert doc.units[0].machine.processor_type == 'Other'
    assert len(doc.units[0].compilers) == 1
    assert doc.units[0].compilers[0].environment_variables in [None, '']
    assert doc.units[0].compilers[0].language in [None, '']
    assert doc.units[0].compilers[0].name == 'Other'
    assert doc.units[0].compilers[0].options in [None, '']
    assert doc.units[0].compilers[0].type in [None, '']
    assert doc.units[0].compilers[0].version == '12.1.0.0'


def update_doc(doc):
    pass


def assert_doc_updates(doc):
    pass