"""
.. module:: test_publishing.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes pyesdoc document publishing tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import datetime
import uuid

import pyesdoc
import test_utils as tu
import test_types as tt



def _create_doc(mod):
    """Creates a document for testing."""
    doc = tu.get_doc(mod)
    mod.DOC_ID = doc.meta.id = uuid.uuid4()
    mod.DOC_VERSION = doc.meta.version = 0
    mod.DOC_DATE = doc.meta.create_date = datetime.datetime.now()

    return doc


def _set_api_url(mode='dev'):
    """Assigns the base API url."""
    if mode == 'dev':
        pyesdoc.set_option("api_url", "http://127.0.0.1:5000")
    elif mode == 'test':
        pyesdoc.set_option("api_url", "http://test.api.es-doc.org")
    elif mode == 'prod':
        pyesdoc.set_option("api_url", "http://api.es-doc.org")


def _test(mod):
    """Performs a publishing workflow test."""
    # Create document.
    doc = _create_doc(mod)

    # Publish.
    pyesdoc.publish(doc)
    mod.DOC_VERSION += 1
    mod.assert_doc(doc)

    # Retrieve.
    doc = pyesdoc.retrieve(mod.DOC_ID, mod.DOC_VERSION)
    mod.assert_doc(doc)

    # Update.
    mod.update_doc(doc)
    mod.assert_doc_updates(doc)

    # Republish.
    pyesdoc.publish(doc)
    mod.DOC_VERSION += 1

    # Retrieve.
    doc = pyesdoc.retrieve(mod.DOC_ID, mod.DOC_VERSION)
    mod.assert_doc(doc, True)
    mod.assert_doc_updates(doc)

    # Republish.
    pyesdoc.publish(doc)
    mod.DOC_VERSION += 1

    # Unpublish.
    pyesdoc.unpublish(mod.DOC_ID, mod.DOC_VERSION)
    tu.assert_none(pyesdoc.retrieve(mod.DOC_ID, mod.DOC_VERSION))
    mod.DOC_VERSION -= 1

    # Retrieve specific.
    doc = pyesdoc.retrieve(mod.DOC_ID, mod.DOC_VERSION)
    mod.assert_doc(doc, True)
    mod.assert_doc_updates(doc)

    # Retrieve latest.
    doc = pyesdoc.retrieve(mod.DOC_ID, pyesdoc.ESDOC_DOC_VERSION_LATEST)
    mod.assert_doc(doc, True)
    mod.assert_doc_updates(doc)

    # Unpublish.
    pyesdoc.unpublish(mod.DOC_ID, mod.DOC_VERSION)
    tu.assert_none(pyesdoc.retrieve(mod.DOC_ID, mod.DOC_VERSION))
    mod.DOC_VERSION -= 1

    # Retrieve specific.
    doc = pyesdoc.retrieve(mod.DOC_ID, mod.DOC_VERSION)
    mod.assert_doc(doc)

    # Retrieve latest.
    doc = pyesdoc.retrieve(mod.DOC_ID, pyesdoc.ESDOC_DOC_VERSION_LATEST)
    mod.assert_doc(doc)

    # Unpublish (will delete document altogether).
    pyesdoc.unpublish(mod.DOC_ID, mod.DOC_VERSION)
    tu.assert_none(pyesdoc.retrieve(mod.DOC_ID, mod.DOC_VERSION))
    mod.DOC_VERSION -= 1
    tu.assert_none(pyesdoc.retrieve(mod.DOC_ID, mod.DOC_VERSION))


def test():
    """Performs publishing workflow tests over the set of test documents."""
    _set_api_url('dev')
    for mod in tt.MODULES:
        tu.init(_test, 'publishing', mod)
        yield _test, mod
