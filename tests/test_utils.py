# -*- coding: utf-8 -*-

"""
.. module:: test_utils.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes test utility functions.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import datetime, os, random, uuid
from os.path import dirname, abspath, join

import arrow
from nose.tools import nottest
import lxml.etree as et

import pyesdoc
import pyesdoc.ontologies.cim.v1.typeset as cim_v1
import test_types as tt



# Integer assertion constants.
COMPARE_EXACT = "EXACT"
COMPARE_GT = "GT"
COMPARE_GTE = "GTE"
COMPARE_LTE = "LTE"
COMPARE_LT = "LT"
COMPARE_TYPES = (
    COMPARE_EXACT,
    COMPARE_GT,
    COMPARE_GTE,
    COMPARE_LT,
    COMPARE_LTE
)

# Document source.
DOCUMENT_SOURCE = "test-unit"


@nottest
def get_test_file_path(name):
    """Returns file path for a test file.

    :param file_name: Name of file being tested.
    :type file_name: str

    :returns: Test file path.
    :rtype: str

    """
    fpath = dirname(abspath(__file__))
    fpath = join(fpath, 'files')
    fpath = join(fpath, name)

    return fpath


@nottest
def get_test_file(name):
    """Opens & returns a test xml file.

    :param name: Name of file being tested.
    :type name: str

    :returns: Opened file.
    :rtype: file

    """
    with open(get_test_file_path(name), 'r') as in_file:
        return in_file.read()


def init(test, description, mod=None, suffix=None):
    """Initializes a test module prior to a test being executed.

    :param function test: The test to be run.
    :param str description: The description to be applied to the test.
    :param module mod: The associated document test module.

    """
    desc = "ES-DOC :: pyesdoc :: Test {0}"
    if mod is not None and suffix is not None:
        desc += " - {1} ({2})"
        if hasattr(mod, "DOC_TYPE_KEY"):
            desc = desc.format(description, mod.DOC_TYPE_KEY, suffix)
        else:
            desc = desc.format(description, mod.__name__, suffix)
    elif mod is not None:
        desc += " - {1}"
        if hasattr(mod, "DOC_TYPE_KEY"):
            desc = desc.format(description, mod.DOC_TYPE_KEY)
        else:
            desc = desc.format(description, mod.__name__)
    else:
        desc = desc.format(description)
    test.description = desc


def decode(doc, encoding):
    """Decode a document representation."""
    # Decode.
    doc = pyesdoc.decode(doc, encoding)

    # Perform basic assertions.
    assert doc is not None
    assert isinstance(doc, object)

    return doc


def encode(doc, encoding, doc_type=None):
    """Encode a document."""
    doc = pyesdoc.encode(doc, encoding)

    # Perform basic assertions.
    assert doc is not None
    if doc_type is not None:
        assert isinstance(doc, doc_type)
        if isinstance(doc_type, str):
            doc.decode('utf-8')

    return doc


def _decode_from_xml_metafor_cim_v1(as_xml,
                                    doc_type=None,
                                    project=None,
                                    institute=None):
    """Decodes a Metafor CIM v1 document from a file."""
    # Load xml file if necessary.
    if isinstance(as_xml, str):
        as_xml = get_test_file(as_xml)

    # Decode document.
    doc = decode(as_xml, pyesdoc.METAFOR_CIM_XML_ENCODING)
    assert_object(doc, doc_type)

    # Assign document attributes.
    if project is not None:
        doc.meta.project = project
    if institute is not None:
        doc.meta.institute = institute
    doc.meta.source = DOCUMENT_SOURCE

    return doc


def get_doc(mod):
    """Returns a test document."""
    # Reset module state.
    tt.reset(mod)

    # Create.
    doc = _decode_from_xml_metafor_cim_v1(mod.DOC_FILE,
                                          mod.DOC_TYPE,
                                          mod.DOC_PROJECT,
                                          mod.DOC_INSTITUTE)

    # Extend.
    pyesdoc.extend(doc)

    # Verify.
    assert_doc(mod, doc)

    return doc


def get_boolean():
    """Returns a random boolean for testing purposes.

    """
    return True


def get_date(value=None):
    """Returns a random integer for testing purposes.

    """
    if value:
        if len(value) == 4:
            return arrow.get(value, "YYYY").datetime
        else:
            return arrow.get(value).datetime
    else:
        return arrow.utcnow().datetime


def get_int(lower=0, upper=9999999):
    """Returns a random integer for testing purposes.

    """
    return random.randint(lower, upper)


def get_float():
    """Returns a random float for testing purposes.

    """
    return random.random()


def get_string(length):
    """Returns a random string for testing purposes.

    """
    return str(uuid.uuid1())[:length]


def get_unicode(length):
    """Returns a random unicode for testing purposes.

    """
    return unicode(uuid.uuid1())[:length]


def get_uuid():
    """Returns a uuid for testing purposes.

    """
    return str(uuid.uuid1())


def assert_doc(mod, doc):
    """Asserts doc against a test module."""
    # Assert document type information.
    assert_object(doc, mod.DOC_TYPE)
    assert_str(mod.DOC_TYPE_KEY, doc.type_key, True)

    # Assert document meta information.
    meta = doc.meta
    assert_object(meta, cim_v1.DocMetaInfo)
    assert_str(meta.source, DOCUMENT_SOURCE)
    if mod.DOC_UID:
        assert_uuid(meta.id, mod.DOC_UID)
    if mod.DOC_VERSION:
        assert_str(meta.version, mod.DOC_VERSION)
    if mod.DOC_PROJECT:
        assert_str(meta.project, mod.DOC_PROJECT)
    if mod.DOC_INSTITUTE:
        assert_str(meta.institute, mod.DOC_INSTITUTE)
    if mod.DOC_DATE:
        assert_date(meta.create_date, mod.DOC_DATE)
    if mod.DOC_AUTHOR and meta.author:
        assert_str(meta.author.individual_name, mod.DOC_AUTHOR)
    if hasattr(mod, "DOC_TYPE_DISPLAY_NAME"):
        assert_str(meta.type_display_name, mod.DOC_TYPE_DISPLAY_NAME)
    if hasattr(mod, "assert_meta_info"):
        mod.assert_meta_info(meta)

    # Assert extended documents.
    if hasattr(doc, "ext"):
        ext = doc.ext
        assert_str(mod.DOC_TYPE_KEY, ext.type, True)
        if hasattr(mod, "assert_extension_info"):
            mod.assert_extension_info(ext)

    # Perform specific document assertions.
    mod.assert_doc(doc)


def assert_iter(collection,
                length=-1,
                item_type=None,
                length_compare=COMPARE_EXACT):
    """Asserts an object collection.

    :param list collection: An object collection.
    :param int length: Collection size.
    :param str length: Collection size comparason operator.
    :param item_type: Type that each collection item should sub-class.
    :type item_type: class or None

    """
    assert_object(collection)
    assert iter(collection) is not None
    if length != -1:
        assert_int(len(collection), length, length_compare)
    if item_type is not None:
        if isinstance(collection, dict):
            collection = collection.values()
        for instance in collection:
            assert_object(instance, item_type)


def assert_in_collection(collection, item_attr, items):
    """Asserts an item is within a collection.

    :param collection: A collection.
    :type collection: list

    :param item: A collection item.
    :type item: object

    """
    try:
        iter(items)
    except TypeError:
        items = [items]
    targets = None
    if item_attr is not None:
        targets = [getattr(i, item_attr) for i in collection]
    else:
        targets = collection
    for item in items:
        assert item in targets, item


def assert_none(instance):
    """Asserts an instance is none.

    :param instance: An object for testing.
    :type instance: object

    """
    assert instance is None, \
           "Instance null mismatch : actual = {0} - {1} :: expected = None" \
           .format(type(instance), instance)


def assert_object(instance, instance_type=None):
    """Asserts an object instance.

    :param instance: An object for testing.
    :type instance: object

    :param instance_type: Type that object must either be or sub-class from.
    :type instance_type: class

    """
    assert instance is not None
    if instance_type is not None:
        assert isinstance(instance, instance_type), \
               "Instance type mismatch : actual = {0} :: expected = {1}" \
               .format(type(instance), instance_type)


def assert_objects(instance1, instance2):
    """Asserts that 2 object instances are equal.

    :param instance1: An object for testing.
    :type instance1: object

    :param instance2: An object for testing.
    :type instance2: object

    """
    assert instance1 is not None, "Only non-null objects are comparable."
    assert instance2 is not None, "Only non-null objects are comparable."
    assert instance1 == instance2, "Instances are not equal"


def assert_bool(actual, expected):
    """Asserts a boolean.

    :param actual: An expression evaluaed as a boolean.
    :type actual: expr | bool

    :param expected: An expression evaluaed as a boolean.
    :type actual: expr | bool

    """
    assert bool(actual) == bool(expected)


def assert_str(actual, expected, startswith=False):
    """Asserts a string.

    :param actual: A string.
    :type actual: str

    :param expected: Expected string value.
    :type expected: str

    :param startswith: Flag indicating whether to perform startswith test.
    :type startswith: bool

    """
    # Format.
    actual = str(actual).strip()
    expected = str(expected).strip()

    # Assert.
    if startswith == False:
        assert actual == expected, \
               "String mismatch : actual = {0} :: expected = {1}" \
               .format(actual, expected)
    else:
        assert actual.startswith(expected) == True, \
               "String startswith mismatch : actual = {0} :: expected = {1}" \
               .format(actual, expected)


def assert_unicode(actual, expected):
    """Asserts a unicode.

    :param actual: A unicode.
    :type actual: str

    :param expected: Expected unicode value.
    :type expected: str

    """
    assert_object(actual, unicode)
    assert_object(expected, unicode)
    assert actual == expected, \
           "Unicode mismatch : actual = {0} :: expected = {1}" \
           .format(actual, expected)


def assert_date(actual, expected):
    """Asserts a datetime.

    :param actual: A date.
    :type actual: str

    :param expected: Expected date value.
    :type expected: str

    """
    if not isinstance(actual, datetime.datetime):
        actual = get_date(actual)
    if not isinstance(expected, datetime.datetime):
        expected = get_date(expected)

    assert actual == expected, \
           "Date mismatch : actual = {0} :: expected = {1}" \
           .format(actual, expected)


def assert_float(actual, expected):
    """Asserts a float.

    :param float actual: Actual float value.
    :param float expected: Expected float value.

    """
    assert_object(actual, float)
    assert_object(expected, float)
    assert actual == expected, \
           "Float mismatch : actual = {0} :: expected = {1}" \
           .format(actual, expected)


def assert_path(actual):
    """Asserts a filepath.

    :param str actual: Actual file path.

    """
    assert_bool(os.path.exists(actual), True)


def assert_int(actual, expected, assert_type=COMPARE_EXACT, msg=None):
    """Asserts an integer.

    :param actual: An integer.
    :type actual: int

    :param expected: Expected integer value.
    :type expected: int

    """
    # Parse actual value.
    # ... convert string
    if type(actual) == str:
        actual = int(actual)
    # ... collection length checks
    else:
        try:
            iter(actual)
        except TypeError:
            pass
        else:
            actual = len(actual)

    if assert_type == COMPARE_EXACT:
        assert expected == actual, "{0} != {1} {2}".format(actual, expected, msg)
    elif assert_type == COMPARE_GT:
        assert expected > actual, "{0} !> {1} {2}".format(actual, expected, msg)
    elif assert_type == COMPARE_GTE:
        assert expected >= actual, "{0} !>= {1} {2}".format(actual, expected, msg)
    elif assert_type == COMPARE_LT:
        assert expected < actual, "{0} !< {1} {2}".format(actual, expected, msg)
    elif assert_type == COMPARE_LTE:
        assert expected <= actual, "{0} !<= {1} {2}".format(actual, expected, msg)
    else:
        assert expected == actual, "{0} != {1} {2}".format(actual, expected, msg)


def assert_int_negative(actual, expected):
    """Negatively asserts an integer.

    :param actual: An integer.
    :type actual: int

    :param expected: Another integer value.
    :type expected: int

    """
    assert actual != expected


def assert_uuid(actual, expected):
    """Asserts a uuid.

    :param actual: A date.
    :type actual: str

    :param expected: Expected uuid value.
    :type expected: str

    """
    if isinstance(actual, uuid.UUID) == False:
        actual = uuid.UUID(actual)
    if isinstance(expected, uuid.UUID) == False:
        expected = uuid.UUID(expected)

    assert actual == expected, "{0} != {1}".format(actual, expected)
