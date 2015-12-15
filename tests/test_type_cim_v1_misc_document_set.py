# -*- coding: utf-8 -*-

"""
.. module:: test_type_cim_v1_misc_document_set.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Tests a cim.v1.DocumentSet instance.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import arrow

import pyesdoc.ontologies.cim as cim
import test_utils as tu



# Test type.
DOC_TYPE = cim.v1.DocumentSet

# Test document type.
DOC_TYPE_KEY = DOC_TYPE.type_key

# Test representation file.
DOC_FILE = 'cim.1.misc.DocumentSet.xml-metafor-cim-v1'

# Test document uid.
DOC_UID = "e4155a28-268e-11e1-9a0e-00163e9152a5"

# Test document version.
DOC_VERSION = 2

# Test document creation date.
DOC_DATE = arrow.get("2012-04-23 14:59:06.767729").datetime

# Test document project.
DOC_PROJECT = "CMIP5"

# Test document project.
DOC_INSTITUTE = "MOHC"

# Test document author.
DOC_AUTHOR = "Metafor Questionnaire"


def assert_doc(doc, is_update=False):
    """Asserts a document.

    :param object doc: Document being tested.
    :param bool is_update: Flag indicating whether document has been updated.

    """
    tu.assert_iter(doc.data, 18, cim.v1.DataObject)
    tu.assert_iter(doc.ensembles, 1, cim.v1.Ensemble)
    tu.assert_object(doc.experiment, cim.v1.NumericalExperiment)
    tu.assert_iter(doc.grids, 1, cim.v1.GridSpec)
    tu.assert_object(doc.model, cim.v1.ModelComponent)
    tu.assert_object(doc.platform, cim.v1.Platform)
    tu.assert_object(doc.simulation, cim.v1.SimulationRun)


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