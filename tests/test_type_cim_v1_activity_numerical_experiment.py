# -*- coding: utf-8 -*-

"""
.. module:: test_type_cim_v1_activity_numerical_experiment.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Tests a cim.v1.NumericalExperiment instance.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import arrow

import pyesdoc.ontologies.cim as cim
import test_utils as tu



# Test type.
DOC_TYPE = cim.v1.NumericalExperiment

# Test type display name.
DOC_TYPE_DISPLAY_NAME = "Experiment"

# Test document type.
DOC_TYPE_KEY = DOC_TYPE.type_key

# Test representation file.
DOC_FILE = 'cim.1.activity.NumericalExperiment.xml-metafor-cim-v1'

# Test document uid.
DOC_UID = '9fa513fc-d3a5-11df-837f-00163e9152a5'

# Test document version.
DOC_VERSION = '1'

# Test document creation date.
DOC_DATE = arrow.get('2012-04-23 14:59:07.048869').datetime

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
    tu.assert_str(ext.display_name, "amip")
    tu.assert_str(ext.description, "AMIP (1979 - at least 2008)", True)
    tu.assert_str(ext.full_display_name, "CMIP5 Experiment : MOHC - amip")
    tu.assert_int(ext.summary_fields, 2)
    tu.assert_str(ext.summary_fields[0], "amip")
    tu.assert_str(ext.summary_fields[1], "AMIP")


def _assert_doc_core(doc, is_update):
    """Assert core information."""
    tu.assert_str(doc.description, "AMIP (1979 - at least 2008)", True)
    tu.assert_str(doc.experiment_id, "3.3")
    tu.assert_str(doc.long_name, "AMIP")
    tu.assert_iter(doc.rationales, 1, str)
    tu.assert_str(doc.rationales[0], "AMIP. Baseline simulation for", True)
    tu.assert_str(doc.short_name, "amip")


def _assert_doc_requirements(doc, is_update):
    """Assert experiment requirements."""
    tu.assert_iter(doc.requirements, 13, cim.v1.NumericalRequirement)

    # Boundary condition.
    req = doc.requirements[0]
    tu.assert_object(req, cim.v1.BoundaryCondition)
    tu.assert_str(req.requirement_type, "boundaryCondition")
    tu.assert_str(req.description, "Imposed changing concentrations", True)
    tu.assert_none(req.id)
    tu.assert_str(req.name, "3.3.bc.sls")

    # Boundary condition - options.
    tu.assert_iter(req.options, 2, cim.v1.NumericalRequirementOption)
    opt = req.options[0]
    tu.assert_str(opt.description, "Concentrations")
    tu.assert_str(opt.id, "bc.013")
    tu.assert_str(opt.name, "3.3.bc.sls_conc")
    tu.assert_str(opt.relationship, "XOR")

    # Initial condition.
    req = doc.requirements[11]
    tu.assert_object(req, cim.v1.InitialCondition)
    tu.assert_str(req.description, "Initial conditions are from", True)
    tu.assert_str(req.id, "ic.003")
    tu.assert_str(req.name, "3.3.ic")
    tu.assert_str(req.requirement_type, "initialCondition")

    # Spatio Temporal Constraint.
    req = doc.requirements[12]
    tu.assert_object(req, cim.v1.SpatioTemporalConstraint)
    tu.assert_object(req.date_range, cim.v1.ClosedDateRange)
    tu.assert_str(req.date_range.duration, "P30Y")
    tu.assert_date(req.date_range.end, "2008-12-30 00:00:00+00:00")
    tu.assert_date(req.date_range.start, "1979-01-01 00:00:00+00:00")
    tu.assert_str(req.description, "Begin in 1979 and", True)
    tu.assert_str(req.id, "stc.027")
    tu.assert_str(req.name, "3.3.stc.1979_30yr")
    tu.assert_str(req.requirement_type, "spatioTemporalConstraint")


def assert_doc(doc, is_update=False):
    """Asserts a document.

    :param object doc: Document being tested.
    :param bool is_update: Flag indicating whether document has been updated.

    """
    for assertor in (
        _assert_doc_core,
        _assert_doc_requirements,
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