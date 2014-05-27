# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.decoder_for_quality_package.py

   :copyright: @2014 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2014-05-27 15:15:32.818332.

"""

# Module imports.
from decoder_xml_utils import set_attributes
from decoder_for_shared_package import *
import typeset



def decode_cim_quality(xml, nsmap):
    """Decodes an instance of the following type: cim quality.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.quality.CimQuality

    """
    decodings = [
        ('meta', False, decode_doc_meta_info, 'self::cim:cIM_Quality'),
        ('reports', True, decode_report, 'child::cim:report'),
    ]

    return set_attributes(typeset.quality.CimQuality(), xml, nsmap, decodings)


def decode_evaluation(xml, nsmap):
    """Decodes an instance of the following type: evaluation.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.quality.Evaluation

    """
    decodings = [
        ('date', False, 'datetime.datetime', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:Date'),
        ('description', False, 'str', 'gmd:evaluationMethodDescription/gco:CharacterString'),
        ('did_pass', False, 'bool', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:pass/gco:Boolean'),
        ('explanation', False, 'str', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:explanation/gco:CharacterString'),
        ('specification', False, 'str', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/@xlink:title'),
        ('specification_hyperlink', False, 'str', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/@xlink:href'),
        ('title', False, 'str', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation/gmd:title/gco:CharacterString'),
        ('type', False, 'str', 'child::gmd:result/@xlink:title'),
        ('type_hyperlink', False, 'str', 'child::gmd:result/@xlink:href'),
    ]

    return set_attributes(typeset.quality.Evaluation(), xml, nsmap, decodings)


def decode_measure(xml, nsmap):
    """Decodes an instance of the following type: measure.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.quality.Measure

    """
    decodings = [
        ('description', False, 'str', 'child::cim:measureDescription'),
        ('description', False, 'str', 'parent::cim:report/child::gmd:measureDescription/gco:CharacterString'),
        ('identification', False, 'str', 'child::cim:measureIdentification/gmd:code/gco:CharacterString'),
        ('name', False, 'str', 'child::cim:nameOfMeasure'),
        ('name', False, 'str', 'parent::cim:report/child::gmd:nameOfMeasure/gco:CharacterString'),
    ]

    return set_attributes(typeset.quality.Measure(), xml, nsmap, decodings)


def decode_report(xml, nsmap):
    """Decodes an instance of the following type: report.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.quality.Report

    """
    decodings = [
        ('date', False, 'datetime.datetime', 'child::gmd:dateTime/gco:DateTime'),
        ('evaluation', False, decode_evaluation, 'self::cim:report'),
        ('evaluator', False, decode_responsible_party, 'child::cim:evaluator'),
        ('measure', False, decode_measure, 'self::cim:report/cim:measure'),
    ]

    return set_attributes(typeset.quality.Report(), xml, nsmap, decodings)


