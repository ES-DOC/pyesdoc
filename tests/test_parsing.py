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



def test_custom_parser_count():
    """Test number of parsers."""
    tu.assert_iter(pyesdoc.parsing.SUPPORTED, length=8)


def test_is_custom_parseable():
    """Test parsers correctly mapped to document types."""
    for doc_type in pyesdoc.ontologies.get_types():
        is_parseable = doc_type.type_key.lower() in pyesdoc.parsing.SUPPORTED
        assert pyesdoc.is_parseable(doc_type.type_key) == is_parseable


def _test_parsing(mod):
    """Performs standard document parsing tests,"""
    doc = tu.get_doc(mod)    # Note - returns a parsed document
    tu.assert_object(doc.ext)
    tu.assert_str(doc.type_key, doc.meta.type)
    tu.assert_str(doc.type_key, doc.ext.type)
    if hasattr(mod, "assert_doc_parsing"):
        mod.assert_doc_parsing(doc)


def test():
    """Performs parsing tests over the set of test documents."""
    for mod in tt.MODULES:
        desc = "Test parsing - {0}".format(mod.DOC_TYPE_KEY)
        _test_parsing.description = desc
        yield _test_parsing, mod
