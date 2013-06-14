"""
.. module:: cim.v1.decoding.decoder_for_quality_package.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:07.994674.

"""

# Module imports.
from lxml import etree as et

from pyesdoc.serialization.decoder_xml_utils import *
from pyesdoc.ontologies.cim.v1.serialization.decoder_for_shared_package import *
from pyesdoc.ontologies.cim.v1.types.quality import *




def decode_cim_quality(xml, nsmap):
    """Decodes an instance of the following type: cim quality.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.CimQuality

    """
    decodings = [
        ('cim_info', False, decode_cim_info, 'self::cim:cIM_Quality'),
        ('reports', True, decode_report, 'child::cim:report'),
    ]

    return set_attributes(CimQuality(), xml, nsmap, decodings)


def decode_evaluation(xml, nsmap):
    """Decodes an instance of the following type: evaluation.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Evaluation

    """
    decodings = [
        ('date', False, 'datetime', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:Date'),
        ('description', False, 'str', 'gmd:evaluationMethodDescription/gco:CharacterString'),
        ('did_pass', False, 'bool', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:pass/gco:Boolean'),
        ('explanation', False, 'str', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:explanation/gco:CharacterString'),
        ('specification', False, 'str', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/@xlink:title'),
        ('specification_hyperlink', False, 'str', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/@xlink:href'),
        ('title', False, 'str', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation/gmd:title'),
        ('type', False, 'str', 'child::gmd:result/@xlink:title'),
        ('type_hyperlink', False, 'str', 'child::gmd:result/@xlink:href'),
    ]

    return set_attributes(Evaluation(), xml, nsmap, decodings)


def decode_measure(xml, nsmap):
    """Decodes an instance of the following type: measure.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Measure

    """
    decodings = [
        ('description', False, 'str', 'child::cim:measureDescription'),
        ('description', False, 'str', 'parent::cim:report/child::gmd:measureDescription/gco:CharacterString'),
        ('identification', False, 'str', 'child::cim:measureIdentification/gmd:code/gco:CharacterString'),
        ('name', False, 'str', 'child::cim:nameOfMeasure'),
        ('name', False, 'str', 'parent::cim:report/child::gmd:nameOfMeasure/gco:CharacterString'),
    ]

    return set_attributes(Measure(), xml, nsmap, decodings)


def decode_report(xml, nsmap):
    """Decodes an instance of the following type: report.

    :param xml: XML from which type is to be decoded.
    :param nsmap: XML namespace mappings.
    :type xml: lxml.etree
    :type nsmap: dict
    :returns: A decoded type instance.
    :rtype: cim.v1.types.{package-name}.Report

    """
    decodings = [
        ('date', False, 'datetime', 'child::gmd:dateTime/gco:DateTime'),
        ('evaluation', False, decode_evaluation, 'self::cim:report'),
        ('evaluator', False, decode_responsible_party, 'child::cim:evaluator'),
        ('measure', False, decode_measure, 'self::cim:report/cim:measure'),
    ]

    return set_attributes(Report(), xml, nsmap, decodings)


