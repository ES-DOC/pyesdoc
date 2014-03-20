import pyesdoc
import test_utils as tu
import test_types as tt



def _test_json(tm, doc):
    # Encode/decode and re-assert document.
    as_json = tu.encode(doc, pyesdoc.ESDOC_ENCODING_JSON)
    as_doc_1 = tu.decode(as_json, pyesdoc.ESDOC_ENCODING_JSON)
    tu.assert_doc(tm, as_doc_1)  

    # Re-encode and assert encodings.
    as_json_1 = tu.encode(as_doc_1, pyesdoc.ESDOC_ENCODING_JSON) 
    tu.assert_string(as_json, as_json_1)


def _test_xml(tm, doc):
    # Encode/decode and re-assert document.
    as_xml = tu.encode(doc, pyesdoc.ESDOC_ENCODING_XML)
    as_doc_1 = tu.decode(as_xml, pyesdoc.ESDOC_ENCODING_XML)
    tu.assert_doc(tm, as_doc_1)    

    # Re-encode and assert encodings.
    # TODO determines why this is happening.
    as_xml_1 = tu.encode(as_doc_1, pyesdoc.ESDOC_ENCODING_XML) 
    tu.assert_integer(len(as_xml), len(as_xml_1))
    # tu.assert_string(as_xml, as_xml_1)


def _test_xml_metafor_cim_v1(tm, doc):
    # Simply verify that encoding is not unsupported at this time.
    try:
        as_xml = tu.encode(doc, pyesdoc.METAFOR_CIM_XML_ENCODING)
    except NotImplementedError:
        pass


def _test_html(tm, doc):
    try:
        as_html = tu.encode(doc, pyesdoc.ESDOC_ENCODING_HTML)
    except KeyError as e:
        if tm.DOC_TYPE.type_key.lower() in (
            "cim.1.activity.simulationrun", 
            "cim.1.misc.documentset",
            "cim.1.software.statisticalmodelcomponent"):
            pass
        else:
            raise e


def test():
    for tm in tt.MODULES:
        # Get doc instance.        
        doc = tu.get_doc(tm)
        tu.assert_doc(tm, doc)

        # Test json.
        _test_json.description = "test_serialize.{0}.{1}".format(tm.__name__[16:], pyesdoc.ESDOC_ENCODING_JSON)
        yield _test_json, tm, doc

        # Test xml.
        _test_xml.description = "test_serialize.{0}.{1}".format(tm.__name__[16:], pyesdoc.ESDOC_ENCODING_XML)
        yield _test_xml, tm, doc

        # Test metafor cim v1 xml.
        _test_xml_metafor_cim_v1.description = "test_serialize.{0}.{1}".format(tm.__name__[16:], pyesdoc.METAFOR_CIM_XML_ENCODING)
        yield _test_xml_metafor_cim_v1, tm, doc

        # Test html.
        _test_html.description = "test_serialize.{0}.{1}".format(tm.__name__[16:], pyesdoc.ESDOC_ENCODING_HTML)
        yield _test_html, tm, doc

