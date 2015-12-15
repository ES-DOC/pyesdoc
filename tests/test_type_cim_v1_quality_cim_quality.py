# -*- coding: utf-8 -*-

"""
.. module:: test_type_cim_v1_quality_cim_quality.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Tests a cim.v1.CimQuality instance.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import arrow

import pyesdoc.ontologies.cim as cim
import test_utils as tu



# Test type.
DOC_TYPE = cim.v1.CimQuality

# Test type display name.
DOC_TYPE_DISPLAY_NAME = "Dataset QC"

# Test document type.
DOC_TYPE_KEY = DOC_TYPE.type_key

# Test representation file.
DOC_FILE = 'cim.1.quality.CimQuality.xml-metafor-cim-v1'

# Test document uid.
DOC_UID = 'c1debb66-2737-11e2-bc06-0010185b3f28'

# Test document version.
DOC_VERSION = '2'

# Test document creation date.
DOC_DATE = arrow.get('2012-11-05T09:51:25').datetime

# Test document project.
DOC_PROJECT = "CMIP5"

# Test document project.
DOC_INSTITUTE = "MOHC"

# Test document author.
DOC_AUTHOR = "Metafor Questionnaire"


def assert_extension_info(ext):
    """Asserts a document's extension information.

    :param object ext: Document extension information.

    """
    tu.assert_str(ext.display_name, "CMIP5 Dataset Quality Control Report")
    tu.assert_str(ext.description, "CMIP5 Quality Control", True)
    tu.assert_str(ext.full_display_name, " CMIP5 Dataset Quality Control Report")
    tu.assert_int(ext.summary_fields, 1)
    tu.assert_str(ext.summary_fields[0], "cmip5.output1.", True)


def _assert_doc_core(doc, is_update):
    """Assert core information."""
    tu.assert_iter(doc.reports, 1)
    r = doc.reports[0]
    tu.assert_date(r.date, '2011-05-01 12:00:00')
    tu.assert_object(r.evaluator, cim.v1.ResponsibleParty)
    tu.assert_str(r.evaluator.individual_name, 'stockhause@dkrz.de')
    tu.assert_str(r.evaluator.role, 'pointofContact')


def _assert_doc_report_evaluation(doc, is_update):
    """Assert report evaluation information."""
    r = doc.reports[0]
    tu.assert_object(r.evaluation, cim.v1.Evaluation)
    e = r.evaluation
    tu.assert_date(e.date, '2012-11-05')
    tu.assert_str(e.description, 'evaluationMethodType=indirect', True)
    tu.assert_str(e.explanation, 'The quality results for this ESG', True)
    tu.assert_str(e.specification, 'The CMIP5/AR5 Model Data Quality Control')
    tu.assert_str(e.specification_hyperlink, 'http://cmip5qc.wdc-climate.de')
    tu.assert_str(e.type, 'QC Level 2 Results')
    tu.assert_str(e.type_hyperlink, 'http://cera-www.dkrz.de/WDCC/CMIP5/QCResult.jsp?experiment=cmip5/output1/NCC/NorESM1-ME/rcp45')


def _assert_doc_report_measure(doc, is_update):
    """Assert report measure information."""
    r = doc.reports[0]
    tu.assert_object(r.measure, cim.v1.Measure)
    m = r.measure
    tu.assert_str(m.description, 'WDCC Conformance', True)
    tu.assert_str(m.identification, 'cmip5-qc-2d')
    tu.assert_str(m.name, 'CMIP5 Quality Control Data Level 2')


def assert_doc(doc, is_update=False):
    """Asserts a document.

    :param object doc: Document being tested.
    :param bool is_update: Flag indicating whether document has been updated.

    """
    for assertor in (
        _assert_doc_core,
        _assert_doc_report_evaluation,
        _assert_doc_report_measure,
        ):
        assertor(doc, is_update)


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