# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_for_quality_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.quality package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
import abc
import datetime
import uuid

import typeset_for_quality_package as quality
import typeset_for_shared_package as shared



class CimQuality(object):
    """A concrete class within the cim v1 type system.

    The starting point for a quality record.  It can contain any number of issues and reports.  An issue is an open-ended description of some issue about a CIM instance.  A record is a prescribed description of some specific quantitative measure that has been applied to a CIM instance.

    """
    def __init__(self):
        """Constructor.

        """
        super(CimQuality, self).__init__()

        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.reports = []                                 # quality.Report


class Evaluation(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of evaluation class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Evaluation, self).__init__()

        self.date = None                                  # datetime.datetime
        self.description = None                           # unicode
        self.did_pass = None                              # bool
        self.explanation = None                           # unicode
        self.specification = None                         # unicode
        self.specification_hyperlink = None               # unicode
        self.title = None                                 # unicode
        self.type = None                                  # unicode
        self.type_hyperlink = None                        # unicode


class Measure(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of measure class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Measure, self).__init__()

        self.description = None                           # unicode
        self.identification = None                        # unicode
        self.name = None                                  # unicode


class Report(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of report class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Report, self).__init__()

        self.date = None                                  # datetime.datetime
        self.evaluation = None                            # quality.Evaluation
        self.evaluator = None                             # shared.ResponsibleParty
        self.measure = None                               # quality.Measure


class CimFeatureType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of cim_feature_type enum.
    """

    pass


class CimResultType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of cim_result_type enum.
    """

    pass


class CimScopeCodeType(object):
    """An enumeration within the cim v1 type system.

    This would cover quality issues with the CIM itself.
    """

    pass


class QualityIssueType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of quality_issue_type enum.
    """

    pass


class QualitySeverityType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of quality_severity_type enum.
    """

    pass


class QualityStatusType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of quality_status_type enum.
    """

    pass


