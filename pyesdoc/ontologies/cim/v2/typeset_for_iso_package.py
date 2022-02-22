"""
.. module:: cim.v2.typeset_for_iso_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.iso package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class Algorithm(object):
    """A concrete class within the cim v2 type system.

    Representation of the LE_Algorithm Class.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Algorithm, self).__init__()

        self.citation = None                              # shared.Citation (0.1)
        self.description = None                           # unicode (0.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.description)


class Lineage(object):
    """A concrete class within the cim v2 type system.

    Representation of the ISO19115 lineage provenance description.

    Information about the events or source data used in constructing a
    dataset

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Lineage, self).__init__()

        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.process_step = []                            # iso.ProcessStep (0.N)
        self.source = []                                  # data.Dataset (0.N)
        self.statement = None                             # unicode (0.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.statement)


class ProcessStep(object):
    """A concrete class within the cim v2 type system.

    Representation of the ISO19115 LE_ProcessStep and parent
    LI_ProcessStep classes.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ProcessStep, self).__init__()

        self.description = None                           # unicode (1.1)
        self.execution_date_time = None                   # time.DateTime (0.1)
        self.processing_information = []                  # iso.Processing (0.N)
        self.processor = None                             # shared.Responsibility (0.1)
        self.rationale = None                             # unicode (0.1)
        self.reference = []                               # shared.Citation (0.N)
        self.report = []                                  # iso.ProcessStepReport (0.N)
        self.source = []                                  # data.Dataset (0.N)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.description)


class ProcessStepReport(object):
    """A concrete class within the cim v2 type system.

    Report of what happened during a processing step.

    Representation of ISO LE_ProcessStepReport, modified to use links or
    body text, rather than files.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ProcessStepReport, self).__init__()

        self.description = None                           # unicode (1.1)
        self.link = None                                  # shared.OnlineResource (0.1)
        self.name = None                                  # unicode (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.name)


class Processing(object):
    """A concrete class within the cim v2 type system.

    Representation of the ISO19115 LE_Processing class Note that the
    algorithm definition has been adjusted to be more generic and less
    "instrument obsessed" than ISO19115.

    Name is an extension, and the identifier is simply a code string
    (id) ... but given there may be no identifier space for this
    processing step, it is made optional, rather than mandatory as in
    ISO. For export to ISO, the recommendation is to use the identifier
    of the CIM document which uses this class.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Processing, self).__init__()

        self.algorithm = []                               # iso.Algorithm (0.N)
        self.documentation = None                         # shared.Citation (0.1)
        self.identifier = None                            # unicode (0.1)
        self.name = None                                  # unicode (1.1)
        self.procedure_description = None                 # unicode (0.1)
        self.runtime_parameters = None                    # unicode (0.1)
        self.software_reference = []                      # shared.Citation (0.N)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.name)


class QualityEvaluationOutput(shared.OnlineResource):
    """A concrete class within the cim v2 type system.

    A specific evaluation output.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(QualityEvaluationOutput, self).__init__()

        self.output_type = None                           # iso.DqEvaluationResultType (1.1)


class QualityEvaluationResult(object):
    """A concrete class within the cim v2 type system.

    The output of some quality evaluation against a specific measure
    for evaluation quality.

    This flattens several ISO classes, including DQ_Result,
    DQ_ConformanceResult, DQ_QuantativeResult, DQ_Element.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(QualityEvaluationResult, self).__init__()

        self.date = None                                  # time.DateTime (0.1)
        self.evaluation_procedure = None                  # unicode (0.1)
        self.evaluator = None                             # shared.Party (0.1)
        self.name = None                                  # unicode (1.1)
        self.passed = None                                # bool (0.1)
        self.results = []                                 # iso.QualityEvaluationOutput (0.N)
        self.specification = None                         # shared.Citation (0.1)
        self.summary_result = None                        # unicode (0.1)


class QualityIssue(object):
    """A concrete class within the cim v2 type system.

    A description of some scientific quality issue known about a
    resource described by this ontology.

    E.g. if a model is known to have a particular problem, or there has
    been a problem found with a dataset. Expect that most such detail
    should be managed in an external (and formal) issue tracker.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(QualityIssue, self).__init__()

        self.description = None                           # unicode (0.1)
        self.reporter = None                              # shared.Party (0.1)
        self.summary = None                               # unicode (1.1)
        self.tracked_issue = None                         # shared.OnlineResource (0.1)


class QualityReport(object):
    """A concrete class within the cim v2 type system.

    A report detailing the quality of some aspect of the target resource.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(QualityReport, self).__init__()

        self.issues = []                                  # iso.QualityIssue (0.N)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.reports = []                                 # iso.QualityEvaluationResult (0.N)
        self.target = None                                # shared.OnlineResource (1.1)


class DqEvaluationResultType(object):
    """An enumeration within the cim v2 type system.

    Classifier of evaluation results.
    """
    is_open = False
    members = [
        "plot",
        "document",
        "dataset"
        ]
    descriptions = [
        "Diagnostic plot, use mime-type to identify what kind of image format is used",
        "Document of some form, use mime-type to identify if PDF etc",
        "Expect a binary target, accessible via a landing page or directly"
        ]


class DsInitiativeTypecode(object):
    """An enumeration within the cim v2 type system.

    Classifier of initiative, to inform ISO19115 metadata.

    Formally a DS_InitiativeTypeCode, from ISO19115_2011.
    """
    is_open = False
    members = [
        "campaign",
        "collection",
        "exercise",
        "experiment",
        "investigation",
        "mission",
        "sensor",
        "operation",
        "platform",
        "process",
        "program",
        "project",
        "study",
        "task",
        "trial"
        ]
    descriptions = [
        "series of organized planned actions",
        "accumulation of datasets assembled for a specific purpose",
        "specific performance of a function or group of functions",
        "process designed to find if something is effective or valid",
        "search or systematic inquiry",
        "specific operation of a data collection system",
        "device or piece of equipment which detects or records",
        "action that is part of a series of actions",
        "vehicle or other support base that holds a sensor",
        " method of doing something involving a number of steps",
        "specific planned activity",
        "organized undertaking, research, or development",
        "examination or investigation",
        "piece of work",
        "process of testing to discover or demonstrate something"
        ]


class MdCellgeometryCode(object):
    """An enumeration within the cim v2 type system.

    Classifier of cells.

    Whether a grid point is point or area.
    """
    is_open = False
    members = [
        "point",
        "area"
        ]
    descriptions = [
        "each cell represents a point",
        "each cell represents an area"
        ]


class MdProgressCode(object):
    """An enumeration within the cim v2 type system.

    Classifier of project or dataset progress.
    """
    is_open = False
    members = [
        "completed",
        "historicalArchive",
        "obsolete",
        "onGoing",
        "planned",
        "required",
        "underDevelopment"
        ]
    descriptions = [
        "production of the data has been completed",
        "data has been stored in an offline storage facility",
        "data is no longer relevant",
        "data is continually being updated",
        "fixed date has been established upon or by which the data will be created or updated",
        "updated",
        "data is currently in the process of being created"
        ]


