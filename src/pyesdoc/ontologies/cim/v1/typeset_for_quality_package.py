"""
.. module:: cim.v1.typeset_for_quality_package.py

   :copyright: @2014 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.quality package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2014-01-07 20:31:23.820445.

"""
# Module imports.
import abc
import datetime
import uuid

import typeset_for_shared_package as shared




class CimQuality(object):
    """A concrete class within the cim v1 type system.

    The starting point for a quality record.  It can contain any number of issues and reports.  An issue is an open-ended description of some issue about a CIM instance.  A record is a prescribed description of some specific quantitative measure that has been applied to a CIM instance.
    """
    def __init__(self):
        """Constructor.

        """
        super(CimQuality, self).__init__()

        self.doc_info = shared.DocInfo()                  # shared.DocInfo
        self.reports = []                                 # quality.Report


class Evaluation(object):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(Evaluation, self).__init__()

        self.date = datetime.datetime.now()               # datetime.datetime
        self.description = str()                          # str
        self.did_pass = bool()                            # bool
        self.explanation = str()                          # str
        self.specification = str()                        # str
        self.specification_hyperlink = str()              # str
        self.title = str()                                # str
        self.type = str()                                 # str
        self.type_hyperlink = str()                       # str


class Measure(object):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(Measure, self).__init__()

        self.description = str()                          # str
        self.identification = str()                       # str
        self.name = str()                                 # str


class Report(object):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(Report, self).__init__()

        self.date = datetime.datetime.now()               # datetime.datetime
        self.evaluation = Evaluation()                    # quality.Evaluation
        self.evaluator = None                             # shared.ResponsibleParty
        self.measure = Measure()                          # quality.Measure


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


