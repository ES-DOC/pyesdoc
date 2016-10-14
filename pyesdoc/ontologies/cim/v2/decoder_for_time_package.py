# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.decoder_for_time_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 2 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from decoder_xml_utils import set_attributes
import typeset



def decode_calendar(xml, nsmap):
    """Decodes an instance of the following type: calendar.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.time.Calendar

    """
    decodings = [
    ]

    return set_attributes(typeset.time.Calendar(), xml, nsmap, decodings)


def decode_date_time(xml, nsmap):
    """Decodes an instance of the following type: date time.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.time.DateTime

    """
    decodings = [
    ]

    return set_attributes(typeset.time.DateTime(), xml, nsmap, decodings)


def decode_datetime_set(xml, nsmap):
    """Decodes an instance of the following type: datetime set.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.time.DatetimeSet

    """
    decodings = [
    ]

    return set_attributes(typeset.time.DatetimeSet(), xml, nsmap, decodings)


def decode_irregular_dateset(xml, nsmap):
    """Decodes an instance of the following type: irregular dateset.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.time.IrregularDateset

    """
    decodings = [
    ]

    return set_attributes(typeset.time.IrregularDateset(), xml, nsmap, decodings)


def decode_regular_timeset(xml, nsmap):
    """Decodes an instance of the following type: regular timeset.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.time.RegularTimeset

    """
    decodings = [
    ]

    return set_attributes(typeset.time.RegularTimeset(), xml, nsmap, decodings)


def decode_time_period(xml, nsmap):
    """Decodes an instance of the following type: time period.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v2.typeset.time.TimePeriod

    """
    decodings = [
    ]

    return set_attributes(typeset.time.TimePeriod(), xml, nsmap, decodings)


