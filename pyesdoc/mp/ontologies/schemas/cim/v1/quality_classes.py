"""
.. module:: quality_classes.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 quality package class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def evaluation():
    """Creates and returns instance of evaluation class.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('date', 'datetime', '0.1'),
            ('description', 'str', '0.1'),
            ('did_pass', 'bool', '0.1'),
            ('explanation', 'str', '0.1'),
            ('specification', 'str', '0.1'),
            ('specification_hyperlink', 'str', '0.1'),
            ('type', 'str', '0.1'),
            ('type_hyperlink', 'str', '0.1'),
            ('title', 'str', '0.1'),
        ],
        'decodings' : [
            ('date', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:Date'),
            ('description', 'gmd:evaluationMethodDescription/gco:CharacterString'),
            ('did_pass', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:pass/gco:Boolean'),
            ('explanation', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:explanation/gco:CharacterString'),
            ('type', 'child::gmd:result/@xlink:title'),
            ('type_hyperlink', 'child::gmd:result/@xlink:href'),
            ('specification', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/@xlink:title'),
            ('specification_hyperlink', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/@xlink:href'),
            ('title', 'child::gmd:result/gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation/gmd:title/gco:CharacterString'),
        ]
    }


def measure():
    """Creates and returns instance of measure class.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('description', 'str', '0.1'),
            ('identification', 'str', '0.1'),
            ('name', 'str', '0.1'),
        ],
        'decodings' : [
            ('description', 'child::cim:measureDescription'),
            ('identification', 'child::cim:measureIdentification/gmd:code/gco:CharacterString'),
            ('name', 'child::cim:nameOfMeasure'),

            # Hacks due to DKRZ misimplementation.
            ('description', 'parent::cim:report/child::gmd:measureDescription/gco:CharacterString'),
            ('name', 'parent::cim:report/child::gmd:nameOfMeasure/gco:CharacterString'),
        ]
    }


def cim_quality():
    """The starting point for a quality record.  It can contain any number of issues and reports.  An issue is an open-ended description of some issue about a CIM instance.  A record is a prescribed description of some specific quantitative measure that has been applied to a CIM instance.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'is_document': True,
        'properties' : [
            ('reports', 'quality.report', '0.N'),
        ],
        'decodings' : [
            ('meta', 'self::cim:cIM_Quality'),
            ('reports', 'child::cim:report'),
        ]
    }


def report():
    """Creates and returns instance of report class.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('date', 'datetime', '0.1'),
            ('evaluation', 'quality.evaluation', '1.1'),
            ('evaluator', 'shared.responsible_party', '0.1'),
            ('measure', 'quality.measure', '1.1'),
        ],
        'decodings' : [
            ('date', 'child::gmd:dateTime/gco:DateTime'),
            ('evaluation', 'self::cim:report'),
            ('evaluator', 'child::cim:evaluator'),
            ('measure', 'self::cim:report/cim:measure'),
        ]
    }


