"""
.. module:: cim.v1.typeset_for_quality_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.quality package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class CimQuality(object):
    """A concrete class within the cim v1 type system.

    The starting point for a quality record.  It can contain any number of issues and reports.  An issue is an open-ended description of some issue about a CIM instance.  A record is a prescribed description of some specific quantitative measure that has been applied to a CIM instance.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(CimQuality, self).__init__()

        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.reports = []                                 # quality.Report (0.N)


class Evaluation(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of evaluation class.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Evaluation, self).__init__()

        self.date = None                                  # datetime.datetime (0.1)
        self.description = None                           # unicode (0.1)
        self.did_pass = None                              # bool (0.1)
        self.explanation = None                           # unicode (0.1)
        self.specification = None                         # unicode (0.1)
        self.specification_hyperlink = None               # unicode (0.1)
        self.title = None                                 # unicode (0.1)
        self.type = None                                  # unicode (0.1)
        self.type_hyperlink = None                        # unicode (0.1)


class Measure(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of measure class.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Measure, self).__init__()

        self.description = None                           # unicode (0.1)
        self.identification = None                        # unicode (0.1)
        self.name = None                                  # unicode (0.1)


class Report(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of report class.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Report, self).__init__()

        self.date = None                                  # datetime.datetime (0.1)
        self.evaluation = None                            # quality.Evaluation (1.1)
        self.evaluator = None                             # shared.ResponsibleParty (0.1)
        self.measure = None                               # quality.Measure (1.1)


class CimFeatureType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of cim_feature_type enum.
    """
    is_open = False
    members = [
        "file",
        "diagnostic"
        ]
    descriptions = [
        "None",
        "None"
        ]


class CimResultType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of cim_result_type enum.
    """
    is_open = False
    members = [
        "plot",
        "document",
        "logfile"
        ]
    descriptions = [
        "None",
        "None",
        "None"
        ]


class CimScopeCodeType(object):
    """An enumeration within the cim v1 type system.

    This would cover quality issues with the CIM itself.
    """
    is_open = False
    members = [
        "dataset",
        "software",
        "service",
        "model",
        "modelComponent",
        "simulation",
        "experiment",
        "numericalRequirement",
        "ensemble",
        "file"
        ]
    descriptions = [
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None"
        ]


class QualityIssueType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of quality_issue_type enum.
    """
    is_open = False
    members = [
        "metadata",
        "data_format",
        "data_content",
        "data_indexing",
        "science"
        ]
    descriptions = [
        "None",
        "None",
        "None",
        "None",
        "None"
        ]


class QualitySeverityType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of quality_severity_type enum.
    """
    is_open = False
    members = [
        "cosmetic",
        "minor",
        "major"
        ]
    descriptions = [
        "None",
        "None",
        "None"
        ]


class QualityStatusType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of quality_status_type enum.
    """
    is_open = False
    members = [
        "reported",
        "confirmed",
        "partially_resolved",
        "resolved"
        ]
    descriptions = [
        "None",
        "None",
        "None",
        "None"
        ]


