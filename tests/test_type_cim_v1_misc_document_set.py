"""
.. module:: test_type_cim_v1_misc_document_set.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Tests a cim.v1.DocumentSet instance.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
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
DOC_DATE = "2012-04-23 14:59:06.767729"

# Test document project.
DOC_PROJECT = "CMIP5"

# Test document project.
DOC_INSTITUTE = "MOHC"

# Test document author.
DOC_AUTHOR = "Metafor Questionnaire"

# Test supported document encodings.
DOC_ENCODINGS_COUNT = 4


def assert_doc(doc, meta, ext):
    """Asserts a document.

    :param object doc: Document being tested.
    :param object meta: Document meta information.
    :param object ext: Document extension information.

    """
    return


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