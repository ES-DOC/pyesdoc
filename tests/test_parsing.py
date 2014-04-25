"""
.. module:: test_parsing.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes pyesdoc document parsing tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import nose

import pyesdoc
import test_utils as tu
import test_types as tt



def _test_custom_parser_count():
    """Test number of parsers."""
    tu.assert_iter(pyesdoc.parsing.SUPPORTED, length=9)


def _test_is_custom_parseable():
    """Test parsers correctly mapped to document types."""
    for doc_type in pyesdoc.ontologies.get_types():
        is_parseable = doc_type.type_key.lower() in pyesdoc.parsing.SUPPORTED
        assert pyesdoc.is_parseable(doc_type.type_key) == is_parseable


def _test(mod):
    """Performs standard document parsing tests,"""
    doc = tu.get_doc(mod)    # Note - returns a parsed document
    tu.assert_object(doc.ext)
    tu.assert_str(doc.type_key, doc.meta.type)
    tu.assert_str(doc.type_key, doc.ext.type)
    if hasattr(mod, "assert_doc_parsing"):
        mod.assert_doc_parsing(doc)


def test():
    """Performs parsing tests over the set of test documents."""
    for f in (
        _test_custom_parser_count,
        _test_is_custom_parseable,
        ):
        tu.init(f, f.__doc__[5:])
        yield f

    for mod in tt.MODULES:
        tu.init(_test, 'parsing', mod)
        yield _test, mod
