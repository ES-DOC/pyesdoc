from dateutil import parser as dateutil_parser

import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



# Test type.
DOC_TYPE = cim.v1.NumericalExperiment

# Test representation file.
DOC_FILE = 'cim/v1_5_0/activity.numerical_experiment.xml'

# Test document uid.
DOC_UID = 'b464433a-d3a5-11df-837f-00163e9152a5'

# Test document version.
DOC_VERSION = '2'

# Test document creation date.
DOC_DATE = '2012-03-06 10:06:42.266723'


def assert_doc(doc):
    assert doc.long_name == 'RCP2.6'
    assert doc.short_name == 'rcp26'
    assert doc.description.startswith('Future projection (2006-2100) forced by RCP2.6.')

    assert len(doc.rationales) == 1
    assert doc.rationales[0].startswith('Provide estimate of future antrhopogenic')

    assert doc.experiment_id == '4.3'

    assert len(doc.requirements) == 8
    assert doc.requirements[0].id == 'ic.004'
    assert doc.requirements[0].name == '4.3.ic'
    assert doc.requirements[0].description.startswith('Initial conditions are from the end of')
    assert doc.requirements[1].name == '4.3.bc.wmg'
    assert doc.requirements[1].description.startswith('Imposed changing concentrations or emissions')
    assert len(doc.requirements[1].options) == 2
    for r in doc.requirements:
        for o in r.options:
            assert o.relationship == 'XOR'
    assert doc.requirements[1].options[0].requirement.id == 'bc.076'
    assert doc.requirements[1].options[0].requirement.name == '4.3.bc.wmg_conc'
    assert doc.requirements[1].options[0].requirement.description == 'Concentrations'
    assert doc.requirements[1].options[1].requirement.id == 'bc.080'
    assert doc.requirements[1].options[1].requirement.name == '4.3.bc.wmg_em'
    assert doc.requirements[1].options[1].requirement.description == 'Emissions'
    assert doc.requirements[2].name == '4.3.bc.sls_conc'
    assert doc.requirements[2].description.startswith('Imposed changing concentrations or emissions')
    assert doc.requirements[3].name == '4.3.bc.aer'
    assert doc.requirements[3].description.startswith('Imposed changing concentrations or emissions')
    assert doc.requirements[4].name == '4.3.bc.aer_pre'
    assert doc.requirements[4].description.startswith('Imposed changing concentrations or emissions')
    assert doc.requirements[5].name == '4.3.bc.LU'
    assert doc.requirements[5].description.startswith('Imposed changing RCP2.6')
    assert doc.requirements[6].name == '4.3.bc.volc_aer_conc'
    assert doc.requirements[6].description.startswith('Imposed constant background')
    assert doc.requirements[7].name == '4.3.stc.2006_94yr'
    assert doc.requirements[7].description.startswith('Begin in 2006 and run')
    assert doc.requirements[7].date_range is not None
    assert doc.requirements[7].date_range.duration == 'P94Y'
    assert doc.requirements[7].date_range.end == dateutil_parser.parse('2100-01-01 00:00:00Z')
    assert doc.requirements[7].date_range.start == dateutil_parser.parse('2006-01-01 00:00:00Z')


def update_doc(doc):
    pass


def assert_doc_updates(doc):
    pass