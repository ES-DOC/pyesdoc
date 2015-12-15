# -*- coding: utf-8 -*-

"""
.. module:: test_validation.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes pyesdoc document validation tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import pyesdoc
import test_utils as tu
import test_types as tt
from pyesdoc.utils import runtime as rt



def _set_doc_errors_01(doc):
    """Valid document - i.e. error count = 0."""
    return 0


def _set_doc_errors_02(doc):
    """Invalid document - meta attribute is missing."""
    doc.meta = None

    return 1


def _test(mod):
    """Performs standard document validation tests."""
    # Set test document/error factories.
    error_setters = (
        _set_doc_errors_01,
        _set_doc_errors_02
        )
    if hasattr(mod, "get_document_error_setters"):
        error_setters += mod.get_document_error_setters()

    # Perform validation test.
    for error_setter in error_setters:
        # ... set valid test document.
        doc = tu.get_doc(mod)

        # ... set expected error count.
        expected_error_count = error_setter(doc)

        # ... validate document.
        errors = pyesdoc.validate(doc)

        # ... print errors if mismatch between expected & actual.
        # if len(errors) == expected_error_count:
        #     for error in errors:
        #         rt.log(error, level=rt.LOG_LEVEL_WARNING)

        # ... assert errors.
        tu.assert_iter(errors, expected_error_count, length_compare=tu.COMPARE_LTE)


def test():
    """Performs validation tests over the set of test documents."""
    for mod in tt.MODULES:
        tu.init(_test, 'validation', mod)
        yield _test, mod