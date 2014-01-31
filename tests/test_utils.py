"""
.. module:: pyesdoc_test.test_utils.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes test utility functions.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""

# Module imports.
import datetime
from os.path import dirname, abspath, join
import random
import sys
import uuid

from nose.tools import nottest
import dateutil.parser as dateutil_parser
import lxml.etree as et

import pyesdoc
import pyesdoc.ontologies.cim.v1.typeset as cim_v1



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


@nottest
def get_test_file_path(name):
    """Returns file path for a test file.

    :param file_name: Name of file being tested.
    :type file_name: str

    :returns: Test file path.
    :rtype: str

    """
    fp = dirname(abspath(__file__))
    fp = join(fp, 'files')
    fp = join(fp, name)

    return fp


@nottest
def get_test_file(name, type='xml'):
    """Opens & returns a test xml file.

    :param name: Name of file being tested.
    :type name: str

    :param type: Type of file being tested.
    :type type: str

    :returns: Opened file.
    :rtype: file

    """
    path = get_test_file_path(name)
    if type=='xml':
        return et.parse(path)
    else:
        return open(path, 'r')


def serialize(encoding, file, type, assertion):
    doc = decode_from_xml_metafor_cim_v1(file, type)
    assertion(doc)
    type = doc.__class__
    repr = encode(doc, encoding)
    if encoding not in (pyesdoc.ESDOC_ENCODING_XML):
        doc = decode(repr, encoding)
        assert isinstance(doc, type), "Decoded type mismatch"
        assertion(doc)
    

def decode(repr, encoding):
    # Decode.
    doc = pyesdoc.decode(repr, encoding)

    # Perform basic assertions.
    assert doc is not None
    assert isinstance(doc, object)

    return doc


def encode(doc, encoding, type=None):
    repr = pyesdoc.encode(doc, encoding)

    # Perform basic assertions.
    assert repr is not None
    if type is not None:
        assert isinstance(repr, type)
        if isinstance(type, str):
            repr.decode('utf-8')

    return repr


def decode_from_xml_metafor_cim_v1(as_xml, type=None):
    # Open cim xml file.
    if isinstance(as_xml, str):
        as_xml = get_test_file(as_xml)

    doc = decode(as_xml, pyesdoc.METAFOR_CIM_XML_ENCODING)
    if doc is not None:
        doc.doc_info.language = pyesdoc.ESDOC_DEFAULT_LANGUAGE

    return doc


def encode_to_xml_metafor_cim_v1(doc):
    return encode(doc, pyesdoc.METAFOR_CIM_XML_ENCODING, str)


def get_boolean():
    """Returns a random boolean for testing purposes.

    """
    return True


def get_date():
    """Returns a random integer for testing purposes.

    """
    return datetime.datetime.now()


def get_int(lower=0, upper=9999999):
    """Returns a random integer for testing purposes.

    """
    return random.randint(lower, upper)


def get_float():
    """Returns a random float for testing purposes.

    """
    return random.random()


def get_string(len):
    """Returns a random string for testing purposes.

    """
    return str(uuid.uuid1())[:len]


def get_unicode(len):
    """Returns a random unicode for testing purposes.

    """
    return unicode(uuid.uuid1())[:len]


def get_uuid():
    """Returns a uuid for testing purposes.

    """
    return str(uuid.uuid1())


def assert_pyesdoc_obj(doc, uid, version, create_date):
    """Tests information associated with a pyesdoc object.

    :param obj: Document pyesdoc object representation.
    :type obj: object

    :param uid: Document UID.
    :type uid: uuid

    :param version: Document version.
    :type version: str

    :param create_date: Document create date.
    :type create_date: datetime

    """
    assert_object(doc)
    assert_object(doc.doc_info)
    if uid is not None:
        assert_uuid(doc.doc_info.id, uid)
    if version is not None:
        assert_string(doc.doc_info.version, version)
    if create_date is not None:
        assert_date(doc.doc_info.create_date, create_date)


def assert_collection(collection,
                      length = -1,
                      length_compare = COMPARE_GTE,
                      item_type=None):
    """Asserts an object collection.

    :param collection: An object collection.
    :type collection: list

    :param length: Collection size.
    :type length: int

    :param length: Collection size comparason operator.
    :type length: str

    :param item_type: Type that each collection item should sub-class.
    :type item_type: class or None

    """
    assert_object(collection)
    assert iter(collection) is not None
    if length != -1:
        assert_integer(len(collection), length, length_compare)
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
    except:
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
    assert instance is None


def assert_object(instance, type=None):
    """Asserts an object instance.

    :param instance: An object for testing.
    :type instance: object

    :param type: Type that object must either be or sub-class from.
    :type type: class

    """
    assert instance is not None
    if type is not None:
        assert isinstance(instance, type)


def assert_objects(instance1, instance2):
    """Asserts that 2 object instances are equal.

    :param instance1: An object for testing.
    :type instance1: object

    :param instance2: An object for testing.
    :type instance2: object

    """
    assert instance1 is not None
    assert instance2 is not None
    assert instance1 == instance2


def assert_string(actual, expected, startswith=False):
    """Asserts a string.

    :param actual: A string.
    :type actual: str

    :param expected: Expected string value.
    :type expected: str

    :param expected: Flag indicating whether to perform startswith test.
    :type expected: bool

    """
    # Format.
    actual = str(actual).strip()
    expected = str(expected).strip()

    # Assert.
    if startswith == False:
        assert actual == expected, \
               "String mismatch : actual = {0} :: expected = {1}".format(actual, expected)
    else:
        assert actual.startswith(expected), \
               "String startswith mismatch : actual = {0} :: expected = {1}".format(actual, expected)


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
           "Unicode mismatch : actual = {0} :: expected = {1}".format(actual, expected)


def assert_date(actual, expected):
    """Asserts a datetime.

    :param actual: A date.
    :type actual: str

    :param expected: Expected date value.
    :type expected: str

    """
    if isinstance(actual, datetime.datetime) and \
       isinstance(expected, datetime.datetime):
       assert actual == expected
    elif isinstance(actual, datetime.datetime):
        assert actual == dateutil_parser.parse(expected)
    else:
        assert dateutil_parser.parse(actual) == expected


def assert_integer(actual, expected, assert_type=COMPARE_EXACT):
    """Asserts an integer.

    :param actual: An integer.
    :type actual: int

    :param expected: Expected integer value.
    :type expected: int

    """
    if assert_type == COMPARE_EXACT:
        assert actual == expected, "{0} != {1}".format(actual, expected)
    elif assert_type == COMPARE_GT:
        assert actual > expected, "{0} !> {1}".format(actual, expected)
    elif assert_type == COMPARE_GTE:
        assert actual >= expected, "{0} !>= {1}".format(actual, expected)
    elif assert_type == COMPARE_LE:
        assert actual < expected, "{0} !< {1}".format(actual, expected)
    elif assert_type == COMPARE_LTE:
        assert actual <= expected, "{0} !<= {1}".format(actual, expected)
    else:
        assert actual == expected, "{0} != {1}".format(actual, expected)


def assert_integer_negative(actual, expected):
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
