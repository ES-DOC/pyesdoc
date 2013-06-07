"""
.. module:: pyesdoc_test.test_utils.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes test utility functions.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""

# Module imports.
import sys

from dateutil import parser as dateutil_parser
from lxml import etree as et
import uuid

from pyesdoc import decode



def get_test_file_path(schema_name, schema_version, file_name):
    """Returns file path for a test file.

    :param schema_name: Ontology schema name.
    :type schema_name: str

    :param schema_version: Ontology schema version.
    :type schema_version: str

    :param file_name: Name of file being tested.
    :type file_name: str

    :returns: Test file path.
    :rtype: str

    """
    for path in sys.path:
        if path.endswith('esdoc-py-client/tests'):
            result = path
            result += '/pyesdoc_test/ontologies/'
            result += schema_name
            result += '/v'
            result += schema_version.replace('.', '_')
            result += '/files/'
            result += file_name
            return result
    return None


def get_test_file(schema_name, schema_version, name, type='xml'):
    """Opens & returns a test xml file.

    :param schema_name: Ontology schema name.
    :type schema_name: str

    :param schema_version: Ontology schema version.
    :type schema_version: str

    :param name: Name of file being tested.
    :type name: str

    :param type: Type of file being tested.
    :type type: str

    :returns: Opened file.
    :rtype: file

    """
    path = get_test_file_path(schema_name, schema_version, name)
    if type=='xml':
        return et.parse(path)
    else:
        return open(path, 'r')


def decode_obj_from_xml(schema_name, schema_version, xml_file, expected_type):
    """Decodes a test xml file & performs basic assertions.

    :param schema_name: Ontology schema name.
    :type schema_name: str

    :param schema_version: Ontology schema version.
    :type schema_version: str
    
    :param xml_file: Name of xml file to be opened.
    :type xml_file: str

    :param expected_type: Type that the decoded instance should be.
    :type expected_type: class

    :returns: Decoded object.
    :rtype: object

    """    
    # Open cim xml file.
    xml = get_test_file(schema_name, schema_version, xml_file)

    # Decode.
    obj = decode(xml, schema_version, 'xml')

    # Perform basic assertions.
    assert obj is not None
    assert isinstance(obj, expected_type)

    return obj


def decode_dict_from_xml(schema_name, schema_version, xml_file, expected_type):
    """Decodes a dictionary from xml file.

    :param schema_name: Ontology schema name.
    :type schema_name: str

    :param schema_version: Ontology schema version.
    :type schema_version: str

    :param xml_file: Name of xml file to be opened.
    :type xml_file: str

    :param expected_type: Type that the decoded instance should be.
    :type expected_type: class

    :returns: Decoded dictionary.
    :rtype: dict

    """
    obj = decode_obj_from_xml(schema_name, schema_version, xml_file, expected_type)

    # Convert.
    d = obj.as_dict()

    # Perform basic assertions.
    assert d is not None
    assert isinstance(d, dict)

    return d


def assert_cim(as_obj, uid, version, create_date):
    """Tests information associated with a cim object.

    :param as_obj: Object representation of a document.
    :type as_obj: object

    :param uid: UID associated with object.
    :type uid: uuid

    :param version: Version associated with object.
    :type version: str

    :param create_date: Date upon which object was created.
    :type create_date: datetime

    """
    assert_object(as_obj)
    assert_object(as_obj.cim_info)
    if uid is not None:
        assert_uuid(as_obj.cim_info.id, uid)
    if version is not None:
        assert_string(as_obj.cim_info.version, version)
    if create_date is not None:
        assert_date(as_obj.cim_info.create_date, create_date)


def assert_collection(collection, length=-1):
    """Asserts an object collection.

    :param collection: A collection of object instances.
    :type collection: list

    :param length: Expected collection length.
    :type length: int

    """
    assert_object(collection)
    if length >= 0:
        assert len(collection) == length
    

def assert_object(instance, type=None):
    """Asserts an object instance.

    :param instance: An object instance.
    :type instance: object

    :param type: Expected type.
    :type type: class

    """
    assert instance is not None
    if type is not None:
        assert isinstance(instance, type)


def assert_string(actual, expected, startswith=False):
    """Asserts a string.

    :param actual: Actual value.
    :type actual: datetime

    :param expected: Expected value.
    :type expected: datetime

    :param startswith: Flag indicating whether to perform startswith test.
    :type startswith: bool

    """
    # Format.
    actual = actual.strip()
    expected = expected.strip()

    # Assert.
    if startswith == False:
        assert actual == expected
    else:
        assert actual.startswith(expected)


def assert_date(actual, expected):
    """Asserts a datetime.

    :param actual: Actual value.
    :type actual: datetime

    :param expected: Expected value.
    :type expected: datetime

    """
    assert actual == dateutil_parser.parse(expected)



def assert_uuid(actual, expected):
    """Asserts a uuid.

    :param actual: Actual value.
    :type actual: uuid

    :param expected: Expected value.
    :type expected: uuid

    """
    if isinstance(actual, uuid.UUID) == False:
        actual = uuid.UUID(actual)
    if isinstance(expected, uuid.UUID) == False:
        expected = uuid.UUID(expected)
        
    assert actual == expected

