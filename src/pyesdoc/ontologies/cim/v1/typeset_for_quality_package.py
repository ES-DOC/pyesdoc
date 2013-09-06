"""
.. module:: cim.v1.typeset_for_quality_package.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.quality package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-09-06 15:59:51.493325.

"""
# Module imports.
import abc
import datetime
import uuid





class CimQuality(object):
    """A concrete class within the cim v1 type system.

    The starting point for a quality record.  It can contain any number of issues and reports.  An issue is an open-ended description of some issue about a CIM instance.  A record is a prescribed description of some specific quantitative measure that has been applied to a CIM instance.
    """
    def __init__(self):
        """Constructor.

        """
        super(CimQuality, self).__init__()

        self.cim_info = None                         # type = shared.CimInfo
        self.reports = []                            # type = quality.Report


class Evaluation(object):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(Evaluation, self).__init__()

        self.date = datetime.datetime.now()          # type = datetime.datetime
        self.description = str()                     # type = str
        self.did_pass = bool()                       # type = bool
        self.explanation = str()                     # type = str
        self.specification = str()                   # type = str
        self.specification_hyperlink = str()         # type = str
        self.title = str()                           # type = str
        self.type = str()                            # type = str
        self.type_hyperlink = str()                  # type = str


class Measure(object):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(Measure, self).__init__()

        self.description = str()                     # type = str
        self.identification = str()                  # type = str
        self.name = str()                            # type = str


class Report(object):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(Report, self).__init__()

        self.date = datetime.datetime.now()          # type = datetime.datetime
        self.evaluation = None                       # type = quality.Evaluation
        self.evaluator = None                        # type = shared.ResponsibleParty
        self.measure = None                          # type = quality.Measure


class CimFeatureType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class CimResultType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class CimScopeCodeType(object):
    """An enumeration within the cim v1 type system.

    This would cover quality issues with the CIM itself
    """

    pass


class QualityIssueType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class QualitySeverityType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class QualityStatusType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


