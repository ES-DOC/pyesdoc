"""
.. module:: pyesdoc_test.test_utils.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes test utility functions.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""

# Module imports.
import datetime
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
    for path in sys.path:
        if path.endswith('esdoc-py-client/tests'):
            result = path
            result += '/pyesdoc_test/files/'
            result += name
            return result
    return None


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


def encode_to_xml_metafor_cim_v1(doc):
    # Decode.
    as_xml = pyesdoc.encode(doc, pyesdoc.METAFOR_CIM_XML_ENCODING)

    # Perform basic assertions.
    assert as_xml is not None
    assert isinstance(as_xml, str)
    as_xml.decode('utf-8')

    return as_xml


def decode_from_xml_metafor_cim_v1(xml_file, expected_type):
    # Open cim xml file.
    as_xml = get_test_file(xml_file)

    # Decode.
    doc = pyesdoc.decode(as_xml, pyesdoc.METAFOR_CIM_XML_ENCODING)

    # Perform basic assertions.
    assert doc is not None
    assert isinstance(doc, expected_type)

    return doc


def encode_to_dict(doc):
    # Decode.
    as_dict = pyesdoc.encode(doc, pyesdoc.ESDOC_ENCODING_DICT)

    # Perform basic assertions.
    assert as_dict is not None
    assert isinstance(as_dict, dict)

    return as_dict


def decode_from_dict(as_dict):
    # Decode.
    doc = pyesdoc.decode(as_dict, pyesdoc.ESDOC_ENCODING_DICT)

    # Perform basic assertions.
    assert doc is not None
    assert isinstance(doc, object)

    return doc


def encode_to_json(doc):
    # Decode.
    as_json = pyesdoc.encode(doc, pyesdoc.ESDOC_ENCODING_JSON)

    # Perform basic assertions.
    assert as_json is not None
    assert isinstance(as_json, str)
    as_json.decode('utf-8')

    return as_json


def decode_from_json(as_json):
    # Decode.
    doc = pyesdoc.decode(as_json, pyesdoc.ESDOC_ENCODING_JSON)

    # Perform basic assertions.
    assert doc is not None
    assert isinstance(doc, object)

    return doc


def encode_to_xml(doc):
    # Decode.
    as_xml = pyesdoc.encode(doc, pyesdoc.ESDOC_ENCODING_XML)

    # Perform basic assertions.
    assert as_xml is not None
    assert isinstance(as_xml, str)
    as_xml.decode('utf-8')

    return as_xml


def decode_from_xml(as_xml):
    # Decode.
    doc = pyesdoc.decode(as_xml, pyesdoc.ESDOC_ENCODING_XML)

    # Perform basic assertions.
    assert doc is not None
    assert isinstance(doc, object)

    return doc


def get_test_obj():
    """Returns a pyesdoc object for test purposes.

    """
    instance = decode_from_xml_metafor_cim_v1('cim',
                                   '1',
                                   'cim/v1_5_0/software.model_component.xml',
                                   cim_v1.ModelComponent)
    assert_object(instance, cim_v1.ModelComponent)

    return instance


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


def assert_pyesdoc_obj(obj, uid, version, create_date):
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
    assert_object(obj)
    assert_object(obj.cim_info)
    if uid is not None:
        assert_uuid(obj.cim_info.id, uid)
    if version is not None:
        assert_string(obj.cim_info.version, version)
    if create_date is not None:
        assert_date(obj.cim_info.create_date, create_date)


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
    assert actual == dateutil_parser.parse(expected)


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

    assert actual == expected
