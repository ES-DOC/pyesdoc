
# Test document author.
DOC_AUTHOR = "Metafor Questionnaire"
import pyesdoc.ontologies.cim as cim
import test_utils as tu



# Test type.
DOC_TYPE = cim.v1.CimQuality

# Test representation file.
DOC_FILE = 'cim.1.quality.CimQuality.xml-metafor-cim-v1'

# Test document uid.
DOC_UID = 'c1debb66-2737-11e2-bc06-0010185b3f28'

# Test document version.
DOC_VERSION = '2'

# Test document creation date.
DOC_DATE = '2012-11-05T09:51:25'

# Test document project.
DOC_PROJECT = "CMIP5"

# Test document project.
DOC_INSTITUTE = "MOHC"

# Test document author.
DOC_AUTHOR = "Metafor Questionnaire"


def assert_doc(doc):
    tu.assert_collection(doc.reports, 1)
    r1 = doc.reports[0]
    tu.assert_date(r1.date, '2011-05-01 12:00:00')

    tu.assert_object(r1.evaluator)
    tu.assert_string(r1.evaluator.individual_name, 'stockhause@dkrz.de')
    tu.assert_string(r1.evaluator.role, 'pointofContact')

    tu.assert_object(r1.measure)
    tu.assert_string(r1.measure.identification, 'cmip5-qc-2d')
    tu.assert_string(r1.measure.description, 'WDCC Conformance', True)
    tu.assert_string(r1.measure.name, 'CMIP5 Quality Control Data Level 2')

    tu.assert_object(r1.evaluation)
    tu.assert_date(r1.evaluation.date, '2012-11-05')
    tu.assert_string(r1.evaluation.description, 'evaluationMethodType=indirect', True)

    tu.assert_string(r1.evaluation.type, 'QC Level 2 Results')
    tu.assert_string(r1.evaluation.type_hyperlink, 'http://cera-www.dkrz.de/WDCC/CMIP5/QCResult.jsp?experiment=cmip5/output1/NCC/NorESM1-ME/rcp45')
    tu.assert_string(r1.evaluation.specification, 'The CMIP5/AR5 Model Data Quality Control')
    tu.assert_string(r1.evaluation.specification_hyperlink, 'http://cmip5qc.wdc-climate.de')


def update_doc(doc):
    pass


def assert_doc_updates(doc):
    pass