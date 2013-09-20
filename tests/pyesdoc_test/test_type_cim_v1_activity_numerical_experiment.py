import uuid

from dateutil import parser as dateutil_parser

import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



# Test type.
DOC_TYPE = cim.v1.NumericalExperiment

# Test representation file.
DOC_FILE = 'xml-metafor-cim-v1/cim.1.activity.NumericalExperiment.xml'

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

    assert len(doc.requirements) == 9
    for requirement in doc.requirements:
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


def update_doc(doc):
    pass


def assert_doc_updates(doc):
    pass