"""
.. module:: decoder_utils.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: XML decoding utility functions.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using pyesdoc @ 2013-08-28 14:41:13.340289.

"""
import uuid
import types

import arrow
from lxml import etree as et

from pyesdoc import exceptions
from pyesdoc.utils import convert



# Null uuid for checking whether one has to be generated.
NULL_UUID = u'00000000-0000-0000-0000-000000000000'



def _get_value(xml, rtype=unicode):
    """Returns xml node value."""
    # Get xml value.
    if isinstance(xml, types.ListType):
        xml = None if len(xml) == 0 else xml[0]
    if xml is None:
        return None

    # Get unicode.
    if rtype is unicode:
        if isinstance(xml, types.StringTypes):
            result = convert.str_to_unicode(xml)
        else:
            result = convert.str_to_unicode(et.tostring(xml))
    else:
        if isinstance(xml, types.StringTypes):
            result = convert.unicode_to_str(xml)
        else:
            result = et.tostring(xml)

    # Format.
    result = result.strip()
    result = result.rstrip('|')

    return result


def _convert_to_unicode(xml, nsmap=None):
    """Converts an etree element xml representation into a unicode type."""
    return _get_value(xml, str)


def _convert_to_bool(xml, nsmap=None):
    """Converts an etree element xml representation into a boolean type."""
    value = _get_value(xml)

    return True if value is not None and value.lower() in [u'true'] else bool()


def _convert_to_integer(xml, nsmap=None):
    """Converts an etree element xml representation into an integer type."""
    value = _get_value(xml)

    return int(value) if value is not None and value.upper() != u'NONE' else int()


def _convert_to_float(xml, nsmap=None):
    """Converts an etree element xml representation into a float type."""
    value = _get_value(xml)

    return float(value) if value is not None else float()


def _convert_to_uid(xml, nsmap=None):
    """Converts an etree element xml representation into a uid type."""
    value = _get_value(xml)
    if value is None or value == NULL_UUID:
        return uuid.uuid4()
    try:
        return uuid.UUID(value)
    except ValueError:
        return uuid.UUID(value[0:36])


def _convert_to_datetime(xml, nsmap=None):
    """Converts an etree element xml representation into a datetime type."""
    value = _get_value(xml)
    if value is None:
        return None
    if len(value) == 4:
        return arrow.get(value, u"YYYY").datetime
    else:
        return arrow.get(value).datetime


# Set of simple type convertors.
_SIMPLE_TYPE_DECODERS = {
    'bool' : _convert_to_bool,
    'date' : _convert_to_datetime,
    'datetime' : _convert_to_datetime,
    'datetime.date' : _convert_to_datetime,
    'datetime.datetime' : _convert_to_datetime,
    'float' : _convert_to_float,
    'int' : _convert_to_integer,
    'str' : _convert_to_unicode,
    'unicode' : _convert_to_unicode,
    'uri' : _convert_to_unicode,
    'uuid' : _convert_to_uid,
    'uuid.UUID' : _convert_to_uid,
}


def set_attributes(target, xml, nsmap, decodings):
    """Decodes entity attributes from a collection of decodings.

    :param object target: A pyesdoc object with a set of attributes to be assigned.
    :param lxml.etree._Element xml: An xml element.
    :param dict nsmap: Set of xml namespace mappings.
    :param dict decodings: Set of mappings used to perform decoding.

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
        is_simple_type = type in _SIMPLE_TYPE_DECODERS

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
    if not xpath:
        return

    # Set target object / attribute.
    obj = target
    parts = attr.split('.')
    for i in range(len(parts) - 1):
        obj = getattr(obj, parts[i])
    att_name = parts[len(parts) - 1]

    # Get current attribute value.
    cur_value = getattr(obj, att_name)

    # Escape if processing a duplicate and the target is already assigned.
    if is_duplicate and not is_iterable and cur_value is not None:
        return

    # Format xpath when appropriate.
    if is_simple_type == True and \
       '@' not in xpath and \
       xpath.endswith('/text()') == False:
       xpath += '/text()'

    # Get attribute value.
    att_value = _get_attribute_value(xml, nsmap, decoder, xpath, is_simple_type, is_iterable)
    if is_iterable and isinstance(att_value, list):
        att_value = [v for v in att_value if v]

    # Set attribute value.
    setattr(obj, att_name,
            att_value if not is_iterable else cur_value + att_value)


def _get_attribute_value(xml, nsmap, decoder, xpath, is_simple_type, is_iterable):
    """Gets the value of an attribute from xml."""
    # Apply xpath (derive xml fragment from value is derived).
    att_xml = xml.xpath(xpath, namespaces=nsmap)
    if not att_xml:
        return [] if is_iterable else None

    # From xml derive value.
    # ... simple types.
    if is_simple_type:
        if decoder in _SIMPLE_TYPE_DECODERS:
            decoder = _SIMPLE_TYPE_DECODERS[decoder]
        if is_iterable:
            return [decoder(i, nsmap) for i in att_xml]
        else:
            decoded = decoder(att_xml, nsmap)
            return None if decoded == str() else decoded

    # ... complex types.
    else:
        return decode_xml(decoder, att_xml, nsmap, is_iterable)


def decode_xml(decoder, xml, nsmap, is_iterable):
    """Decodes either an entity or an entity collection from xml.

    :param function decoder: Decoder function pointer.
    :param lxml.etree._Element xml: An xml element.
    :param dict nsmap: Set of xml namespace mappings.
    :param bool take_first: Flag indicating whether to return only the first entity of a collection.

    :returns: Decoded entity or entity collection.
    :rtype: miscellaneous

    """
    # None if passed none.
    if xml is None:
        return None

    # Instance if passed etree element.
    if isinstance(xml, et._Element):
        return decoder(xml, nsmap)

    # Instance if passed etree element collection and caller wants first only.
    if isinstance(xml, types.ListType) and is_iterable == False:
        return None if len(xml) == 0 else decode_xml(decoder, xml[0], nsmap, None)

    # Collection if passed etree element collection.
    if isinstance(xml, types.ListType):
        collection = []
        for elem in xml:
            instance = decode_xml(decoder, elem, nsmap, None)
            collection.append(instance)
        return collection

    # otherwise exception
    raise exceptions.DecodingException("xml cannot be decoded.")


def load_xml(xml, return_nsmap=False, default_ns='cim'):
    """Loads etree xml element.

    :param string xml: An xml blob.
    :param bool return_nsmap: Flag indicating whether namespace map will be returned or not.
    :param str default_ns: Default namespace.

    :returns: XML element.
    :rtype: lxml.etree._Element

    """
    # Defensive programming.
    if xml is None:
        raise exceptions.DecodingException("XML is undefined.")

    # ... etree elements.
    nsmap = None
    if isinstance(xml, et._Element):
        nsmap = xml.nsmap

    # ... etree element trees.
    elif isinstance(xml, et._ElementTree):
        xml = xml.getroot()
        nsmap = xml.nsmap

    else:
        # ... files / url's
        try:
            xml = et.parse(xml)
            xml = xml.getroot()
            nsmap = xml.nsmap
        except Exception as e:
            # ... unicode
            if isinstance(xml, unicode):
                xml = convert.unicode_to_str(xml)

            # ... strings
            if isinstance(xml, str):
                try:
                    xml = et.fromstring(xml)
                except Exception as err:
                    raise exceptions.DecodingException("Invalid xml string.")
                else:
                    nsmap = xml.nsmap

            # Unsupported
            else:
                raise exceptions.DecodingException("Unsupported xml type, must be either a string, file, url or etree.")


    # Set default namespace.
    if nsmap is not None:
        nsmap[default_ns] = nsmap.pop(None)

    # Return either a tuple or single.
    if return_nsmap:
        return xml, nsmap
    else:
        return xml
