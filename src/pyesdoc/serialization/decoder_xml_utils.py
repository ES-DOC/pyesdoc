# -*- coding: utf-8 -*-

"""
.. module:: decoder_xml_utils.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: XML decoding utility functions.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2013-08-28 14:41:13.340289.

"""

# Module imports.
import uuid
import types

from dateutil import parser as dateutil_parser
from lxml import etree as et



# Null uuid for checking whether one has to be generated.
NULL_UUID = ['00000000-0000-0000-0000-000000000000']



class PYESDOC_XMLError(Exception):
    """Module exception class.

    """

    def __init__(self, message):
        """Contructor.

        :param message: Exception message.
        :type message: str

        """
        self.message = message


    def __str__(self):
        """Returns a string representation.

        """
        return "ES-DOC PY-CLIENT XML ERROR : {0}".format(repr(self.message))



def _get_value_as_string(xml, nsmap):
    """Converts passed xml fragment to a string."""
    result = None

    # Strip first item from iterables.
    if isinstance(xml, types.ListType):
        if len(xml) > 0:
            xml = xml[0]
        else:
            xml = None

    # Get raw string.
    if xml is None:
        result = None
    elif isinstance(xml, types.StringTypes):
        result = xml.encode('utf-8', 'ignore')
    else:
        result = et.tostring(xml)

    # Format string.
    if result is not None:
        result = result.strip()
        result = result.rstrip('|')

    return result


def _convert_to_string(xml, nsmap=None):
    """Converts an etree element xml representation into a string type."""
    return _get_value_as_string(xml, nsmap)


def _convert_to_bool(xml, nsmap=None):
    """Converts an etree element xml representation into a boolean type."""
    as_string = _get_value_as_string(xml, nsmap)
    if as_string is None:
        return bool()
    else:
        as_string = as_string.upper()
        if as_string in ['TRUE']:
            return True
        elif as_string in ['FALSE']:
            return False
        else:
            return bool()


def _convert_to_integer(xml, nsmap=None):
    """Converts an etree element xml representation into an integer type."""
    as_string = _get_value_as_string(xml, nsmap)
    if as_string is None or as_string.upper() == 'NONE':
        return int()
    else:
        return int(as_string)


def _convert_to_float(xml, nsmap=None):
    """Converts an etree element xml representation into a float type."""
    as_string = _get_value_as_string(xml, nsmap)
    if as_string is None:
        return float()
    else:
        return float(as_string)


def _convert_to_uid(xml, nsmap=None):
    """Converts an etree element xml representation into a uid type."""
    as_string = _get_value_as_string(xml, nsmap)
    if as_string is None or as_string in NULL_UUID:
        return uuid.uuid4()
    else:
        return uuid.UUID(as_string)


def _convert_to_datetime(xml, nsmap=None):
    """Converts an etree element xml representation into a datetime type."""
    as_string = _get_value_as_string(xml, nsmap)
    if as_string is None:
        return None
    else:
        return dateutil_parser.parse(as_string)


# Set of simple type convertors.
_simple_type_decoders = {
    'bool' : _convert_to_bool,
    'date' : _convert_to_datetime,
    'datetime' : _convert_to_datetime,
    'datetime.date' : _convert_to_datetime,
    'datetime.datetime' : _convert_to_datetime,
    'float' : _convert_to_float,
    'int' : _convert_to_integer,
    'str' : _convert_to_string,
    'uri' : _convert_to_string,
    'uuid' : _convert_to_uid,
    'uuid.UUID' : _convert_to_uid,
}


def set_attributes(target, xml, nsmap, decodings):
    """Decodes entity attributes from a collection of decodings.

    :param target: A pyesdoc object with a set of attributes to be assigned.
    :type target: object

    :param xml: An xml element.
    :type xml: lxml.etree._Element

    :param nsmap: Set of xml namespace mappings.
    :type nsmap: dict

    :param decodings: Set of mappings used to perform decoding.
    :type decodings: dict

    :returns: A pyesdoc object with assigned attributes.
    :rtype: object

    """
    attrs = []

    # Iterate & apply decodings.
    for attr, is_iterable, type, xpath in \
        [d for d in decodings if len(d) == 4]:

        # Determine if this is a duplicate assignment.
        is_duplicate = attr in attrs
        if not is_duplicate:
            attrs.append(attr)

        # Determine if type is a simple one.
        is_simple_type = type in _simple_type_decoders

        try:
            _set_attribute(target,
                           xml,
                           nsmap,
                           attr,
                           type,
                           xpath,
                           is_simple_type,
                           is_iterable,
                           is_duplicate)
        except Exception as e:
            msg = "\nES-DOC :: WARNING :: XML DECODING ERROR\n"
            msg += "\tTarget = {0};\n".format(target)
            msg += "\tAttribute name = {0};\n".format(attr)
            msg += "\tAttribute type = {0};\n".format(type)
            msg += "\tAttribute is iterable ? = {0};\n".format(is_iterable)
            msg += "\tAttribute is simple ? = {0};\n".format(is_simple_type)
            msg += "\tAttribute xpath = {0};\n".format(xpath)
            msg += "\tError = {0};\n".format(e)
            print msg

    # Support operation chaining.
    return target


def _set_attribute(target,
                   xml,
                   nsmap,
                   attr,
                   decoder,
                   xpath,
                   is_simple_type,
                   is_iterable,
                   is_duplicate):
    """Decodes entity attribute from a decoding."""
    # Escape if xpath is unassigned.
    if xpath is None or xpath == '':
        return

    # Format xpath when appropriate.
    if is_simple_type == True and \
       '@' not in xpath and \
       xpath.endswith('/text()') == False:
       xpath += '/text()'

    # Set target object / attribute.
    obj = target
    parts = attr.split('.')
    for i in range(len(parts) - 1):
        obj = getattr(obj, parts[i])
    att_name = parts[len(parts) - 1]

    # Get attribute value.
    att_value = _get_attribute_value(xml, nsmap, decoder, xpath, is_simple_type, is_iterable)

    # Set attribute value.
    # ... simple types
    if is_simple_type:
        # ... iterables
        if is_iterable:
            collection = getattr(obj, att_name)
            for i in att_value:
                collection.append(i)
        # ... non-iterables
        else:
            setattr(obj, att_name, att_value)

    # ... complex types
    else:
        # ... iterables
        if is_iterable:
            collection = getattr(obj, att_name)
            for i in att_value:
                collection.append(i)
        # ... non-iterables
        else:
            # ... do not overwrite previously assigned property values.
            if is_duplicate:
                cur_obj = getattr(obj, att_name)
                if cur_obj is None:
                    setattr(obj, att_name, att_value)
            else:
                setattr(obj, att_name, att_value)

    # Support operation chaining.
    return target


def _get_attribute_value(xml, nsmap, decoder, xpath, is_simple_type, is_iterable):
    """Gets the value of an attribute from xml."""
    result = None

    # Apply xpath (derive xml fragment from value is derived).
    att_xml = xml.xpath(xpath, namespaces=nsmap)

    # From xml derive value.
    # ... simple types.
    if is_simple_type:
        if decoder in _simple_type_decoders:
            decoder = _simple_type_decoders[decoder]
        if is_iterable:
            result = map(lambda i: decoder(i, nsmap), att_xml)
        else:
            result = decoder(att_xml, nsmap)

    # ... complex types.
    else:
        result = decode_xml(decoder, att_xml, nsmap, is_iterable)

    # Workaround - decoding empty xml attributes.
    if is_simple_type and not is_iterable and \
       "@" in xpath and result == str():
        result = None

    return result


def decode_xml(decoder, xml, nsmap, is_iterable):
    """Decodes either an entity or an entity collection from xml.

    :param decoder: Decoder function pointer.
    :type decoder: function

    :param xml: An xml element.
    :type xml: lxml.etree._Element

    :param nsmap: Set of xml namespace mappings.
    :type nsmap: dict

    :param take_first: Flag indicating whether to return only the first entity of a collection.
    :type take_first: bool

    :returns: Decoded entity or entity collection.
    :rtype: miscellaneous

    """
    # None if passed none.
    if xml is None:
        # print 'Nothing to decode ...'
        return None

    # Instance if passed etree element.
    if isinstance(xml, et._Element):
        # print 'Decoding an instance ...'
        return decoder(xml, nsmap)

    # Instance if passed etree element collection and caller wants first only.
    if isinstance(xml, types.ListType) and is_iterable == False:
        # print 'Decoding first instance  from collection ...'
        return None if len(xml) == 0 else decode_xml(decoder, xml[0], nsmap, None)

    # Collection if passed etree element collection.
    if isinstance(xml, types.ListType):
        # print 'Decoding a collection ...'
        collection = []
        for elem in xml:
            instance = decode_xml(decoder, elem, nsmap, None)
            collection.append(instance)
        return collection

    # otherwise exception
    raise PYESDOC_XMLError("xml cannot be decoded.")


def load_xml(xml, return_nsmap=False, default_ns='cim'):
    """Loads etree xml element.

    :param xml: An xml blob.
    :type xml: string

    :param return_nsmap: Flag indicating whether namespace map will be returned or not.
    :type return_nsmap: bool

    :param default_ns: Default namespace.
    :type default_ns: str

    :returns: XML element.
    :rtype: lxml.etree._Element

    """
    # Defensive programming.
    if xml is None:
        raise PYESDOC_XMLError("XML is undefined.")

    nsmap = None
    # ... etree elements.
    if isinstance(xml, et._Element):
        nsmap = xml.nsmap
    # ... etree element trees.
    elif isinstance(xml, et._ElementTree):
        xml = xml.getroot()
        nsmap = xml.nsmap
    else:
        # ... files / URLs.
        try:
            xml = et.parse(xml)
            xml = xml.getroot()
            nsmap = xml.nsmap
        except Exception as e:
            # ... strings.
            if isinstance(xml, basestring):
                try:
                    xml = et.fromstring(xml)
                except Exception:
                    raise PYESDOC_XMLError("Invalid xml string.")
                else:
                    nsmap = xml.nsmap
            else:
                raise PYESDOC_XMLError("Unsupported xml type, must be either a string, file, url or etree.")

    # Set default namespace.
    if nsmap is not None:
        nsmap[default_ns] = nsmap.pop(None)

    # Return either a tuple or single.
    if return_nsmap:
        return xml, nsmap
    else:
        return xml
