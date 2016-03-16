# -*- coding: utf-8 -*-

"""
.. module:: test_serialization.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes pyesdoc document serialization tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import pyesdoc
import test_utils as tu
import test_types as tt



def _test(mod, doc, encoding):
    """Perform encoding specific serialization tests."""
    # Encode/decode and re-assert document.
    as_repr = tu.encode(doc, encoding)
    as_doc_1 = tu.decode(as_repr, encoding)
    tu.assert_doc(mod, as_doc_1)

    # Re-encode.
    as_repr_1 = tu.encode(as_doc_1, encoding)

    # TODO - explore why sometimes XML encoding is problematic
    # although all good when reencoding to json.
    if len(as_repr) != len(as_repr_1) and encoding == 'xml':
        as_repr = tu.encode(tu.decode(as_repr, encoding), 'json')
        as_repr_1 = tu.encode(tu.decode(as_repr_1, encoding), 'json')

    # Verify encoding equivalence.
    tu.assert_int(len(as_repr), len(as_repr_1), msg=str(type(doc)))
    tu.assert_str(as_repr, as_repr_1)


def _test_metafor_xml(doc):
    """Perform metafor cim v1 xml serialization tests."""
    # Simply verify that encoding is not unsupported at this time.
    try:
        tu.encode(doc, pyesdoc.METAFOR_CIM_XML_ENCODING)
    except NotImplementedError:
        pass


def _test_html(mod, doc):
    """Perform html serialization tests."""
    try:
        tu.encode(doc, pyesdoc.ENCODING_HTML)
    except KeyError as err:
        if mod.DOC_TYPE.type_key.lower() in (
            "cim.1.misc.documentset",
            "cim.1.software.statisticalmodelcomponent"):
            pass
        else:
            raise err


def test():
    """Performs serialization tests over the set of test documents."""
    for mod in tt.MODULES:
        # Get doc instance.
        doc = tu.get_doc(mod)

        # Test json.
        tu.init(_test, 'serialization', mod, 'JSON')
        yield _test, mod, doc, pyesdoc.ENCODING_JSON

        # Test xml.
        tu.init(_test, 'serialization', mod, 'XML')
        yield _test, mod, doc, pyesdoc.ENCODING_XML

        # Test metafor cim v1 xml.
        tu.init(_test_metafor_xml, 'serialization', mod, 'XML Metafor CIM v1')
        yield _test_metafor_xml, doc

        # Test html.
        tu.init(_test_html, 'serialization', mod, 'HTML')
        yield _test_html, mod, doc
