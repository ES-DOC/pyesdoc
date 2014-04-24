"""
.. module:: test_validation.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes pyesdoc document validation tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import nose

import pyesdoc
import test_utils as tu
import test_types as tt



def _get_doc_01(mod):
    return tu.get_doc(mod), 0


def _get_doc_02(mod):
    doc = tu.get_doc(mod)
    doc.meta = None

    return doc, 1


def _test_validation(mod):
    """Performs standard document validation tests,"""
    for factory in (
        _get_doc_01,
        _get_doc_02
        ):
        doc, expected_error_count = factory(mod)
        errors = pyesdoc.validate(doc)
        if len(errors) != expected_error_count:
            for error in errors:
                print error

        tu.assert_iter(pyesdoc.validate(doc), expected_error_count)


def test():
    """Performs parsing tests over the set of test documents."""
    for mod in tt.MODULES:
        desc = "Test validation - {0}".format(mod.DOC_TYPE_KEY)
        _test_validation.description = desc
        yield _test_validation, mod
