"""
.. module:: test_serialization.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes pyesdoc document serialization tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import pyesdoc
import test_utils as tu
import test_types as tt


def _test_encoding(mod, doc, encoding):
    """Perform encoding specific serialization tests."""
    # Encode/decode and re-assert document.
    as_repr = tu.encode(doc, encoding)
    as_doc_1 = tu.decode(as_repr, encoding)
    tu.assert_doc(mod, as_doc_1)

    # Re-encode and assert encodings.
    as_repr_1 = tu.encode(as_doc_1, encoding)
    tu.assert_int(len(as_repr), len(as_repr_1))
    tu.assert_str(as_repr, as_repr_1)


def _test_xml_metafor_cim_v1(mod, doc):
    """Perform metafor cim v1 xml serialization tests."""
    # Simply verify that encoding is not unsupported at this time.
    try:
        as_xml = tu.encode(doc, pyesdoc.METAFOR_CIM_XML_ENCODING)
    except NotImplementedError:
        pass


def _test_html(mod, doc):
    """Perform html serialization tests."""
    try:
        as_html = tu.encode(doc, pyesdoc.ESDOC_ENCODING_HTML)
    except KeyError as e:
        if mod.DOC_TYPE.type_key.lower() in (
            "cim.1.activity.simulationrun",
            "cim.1.misc.documentset",
            "cim.1.software.statisticalmodelcomponent"):
            pass
        else:
            raise e


def test():
    """Performs serialization tests over the set of test documents."""
    for mod in tt.MODULES:
        # Get doc instance.
        doc = tu.get_doc(mod)

        # Test json.
        _test_encoding.description = \
            "Test serialization - {0} (JSON)".format(mod.DOC_TYPE_KEY)
        yield _test_encoding, mod, doc, pyesdoc.ESDOC_ENCODING_JSON

        # Test xml.
        _test_encoding.description = \
            "Test serialization - {0} (XML)".format(mod.DOC_TYPE_KEY)
        yield _test_encoding, mod, doc, pyesdoc.ESDOC_ENCODING_XML

        # Test metafor cim v1 xml.
        _test_xml_metafor_cim_v1.description = \
            "Test serialization - {0} (XML Metafor CIM v1)".format(mod.DOC_TYPE_KEY)
        yield _test_xml_metafor_cim_v1, mod, doc

        # Test html.
        _test_html.description = \
            "Test serialization - {0} (HTML)".format(mod.DOC_TYPE_KEY)
        yield _test_html, mod, doc
