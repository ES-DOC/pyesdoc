# -*- coding: utf-8 -*-

"""
.. module:: test_extensions.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes pyesdoc document extension tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import nose

import pyesdoc
import test_utils as tu
import test_types as tt



def _test_custom_extender_count():
    """Test number of extenders."""
    tu.assert_iter(pyesdoc.extensions.SUPPORTED, length=10)


def _test_is_custom_extendable():
    """Test extenders correctly mapped to document types."""
    for doc_type in pyesdoc.ontologies.get_types():
        is_extendable = doc_type.type_key.lower() in pyesdoc.extensions.SUPPORTED
        assert pyesdoc.is_extendable(doc_type.type_key) == is_extendable


def _test(mod):
    """Performs standard document extensions tests,"""
    doc = tu.get_doc(mod)    # Note - returns an extended document
    tu.assert_object(doc.ext)
    tu.assert_str(doc.type_key, doc.meta.type)
    tu.assert_str(doc.type_key, doc.ext.type)
    if hasattr(mod, "assert_doc_extensions"):
        mod.assert_doc_extensions(doc)


def test():
    """Performs extension tests over the set of test documents."""
    for func in (
        _test_custom_extender_count,
        _test_is_custom_extendable,
        ):
        tu.init(func, func.__doc__[5:])
        yield func

    for mod in tt.MODULES:
        tu.init(_test, 'extensions', mod)
        yield _test, mod
