
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.type_help.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The ontology help text.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import typeset_for_designing_package as designing
import typeset_for_shared_package as shared
import typeset_for_activity_package as activity
import typeset_for_software_package as software
import typeset_for_science_package as science
import typeset_for_data_package as data
import typeset_for_drs_package as drs
import typeset_for_platform_package as platform



HELP = {
	# ------------------------------------------------
	# Packages.
	# ------------------------------------------------

	designing: """
        Types that describe project design features.

        """,

	shared: """
        Shared types that might be imported from other packages within the ontology.

        """,

	activity: """
        Types that describe context against which climate models are run.

        """,

	software: """
        Types that describe the software that constiutes a climate model.

        """,

	science: """
        Types that describe the science being performed.

        """,

	data: """
        Types that describe output that climate models emit.

        """,

	drs: """
        Types that describe the directory structures to which climate model output is written.

        """,

	platform: """
        Types that describe hardware upon which climate models are run.

        """,

	# ------------------------------------------------
	# Classes.
	# ------------------------------------------------


	designing.NumericalExperiment: """
		Defines a numerical experiment.

	""",

	designing.Project: """
		Describes a scientific project.

	""",

	designing.ForcingConstraint: """
		Identifies a model forcing constraint.

	""",

	designing.MultiTimeEnsemble: """
		Defines an experiment ensemble with multiple start dates.

	""",

	designing.TemporalConstraint: """
		A temporal constraint on a numerical experiment.

	""",

	designing.NumericalRequirement: """
		A numerical requirement associated with a numerical experiment.

	""",

	designing.EnsembleRequirement: """
		Defines an experiment ensemble.

	""",

	designing.OutputTemporalRequirement: """
		Provides details of when output is required from an experiment.
    Typically output will be required in one of three modes:
    (1) continuous,
    (2) continuous for a set of subset periods, or
    (3) sliced for a set of months in a year or days in a month.

	""",

	designing.MultiEnsemble: """
		In the case of multiple ensemble axes, defines how they
    are set up and ordered.

	""",

	designing.SimulationPlan: """
		Describes a simulation that needs to be run.

	""",

	designing.DomainProperties: """
		Properties of the domain which needs to be simulated, extend and/or resolution.

	""",



	shared.Pid: """
		A permanent identifier (with a resolution service).

	""",

	shared.NumberArray: """
		Provides a class for entering an array of numbers.

	""",

	shared.OnlineResource: """
		A minimal approximation of ISO19115 CI_ONLINERESOURCE, provides a link and details
    of how to use that link.

	""",

	shared.Party: """
		Implements minimal material for an ISO19115-1 (2014) compliant party.
    For our purposes this is a much better animal than the previous responsibleParty 
    which munged roles together with people. Note we have collapsed CI_Contact,
    CI_Individual and CI_Organisation as well as the abstract CI_Party.

	""",

	shared.KeyFloat: """
		Holds a key and a float value.

	""",

	shared.DatetimeSet: """
		Base class for a set of dates or times.
    Note that we assume either a periodic set of dates which can
    be date and/or time, or an irregular set which can only be dates.

	""",

	shared.DocReference: """
		Specialisation of online resource for link between CIM documents, whether the
    remote document exists when complete, or not.

	""",

	shared.DateTime: """
		A date or time. Either in simulation time with the simulation
    calendar, or with reference to a simulation start, in which
    case the datetime is an interval after the start date.

	""",

	shared.TimesliceList: """
		A list of referential dates, 
        e.g. yearlist, 1,4,5 would refer to jan,april,may,
             monthlist, 1,5,6 would refer to the 1st, 5th and 6th of the month.

	""",

	shared.DocMetaInfo: """
		Encapsulates document meta information used by es-doc machinery. Will not normally be
    populated by humans. May duplicate information held in 'visible' metadata.

	""",

	shared.TimePeriod: """
		A time period class aka a temporal extent.

	""",

	shared.RegularTimeset: """
		A regularly spaced set of times.

	""",

	shared.ExternalDocument: """
		A real world document, could be a book, a journal article, a manual, a web page ... it might or might
    not be online, although preferably it would be. We expect a typical citation to be built up
    as in the following 'authorship, date: title, publication_detail (doi if present)'.

	""",

	shared.QualityReview: """
		Assertations as to the completeness and quality of a document.

	""",

	shared.Reference: """
		An external document which can have a context associated with it.

	""",

	shared.Responsibility: """
		Implements the ISO19115-1 (2014) CI_Responsibility (which replaces
    responsibleParty). Combines a person and their role in doing something.

	""",

	shared.Cimtext: """
		Provides a text class which supports plaintext, html, and
    friends (or will do).

	""",

	shared.Calendar: """
		Describes the calendar required/used in an experiment/simulation.
    This class is based on the calendar attributes and properties found in the
    CF netCDF conventions.

	""",

	shared.IrregularDateset: """
		A set of irregularly spaced times.

	""",



	activity.Conformance: """
		A specific conformance. Describes how a particular numerical requirement has been implemented.
    Will normally be linked from an ensemble descriptor.

	""",

	activity.Ensemble: """
		Generic ensemble definition.
    Holds the definition of how the various ensemble members have been configured.
    If ensemble axes are not present, then this is either a single member ensemble,
    or part of an uber ensemble.

	""",

	activity.UberEnsemble: """
		An ensemble made up of other ensembles. Often used where parts of an ensemble were run by
    different institutes. Could also be used when a new experiment is designed which can use
    ensemble members from previous experiments and/or projects.

	""",

	activity.EnsembleMember: """
		An ensemble may be a complicated interplay of axes, for example, r/i/p, not all of which
    are populated, so we need a list of the actual simulations and how they map onto the ensemble
    axes.

	""",

	activity.ParentSimulation: """
		Defines the relationship between a simulation and its parent.

	""",

	activity.EnsembleAxis: """
		Defines the meaning of r/i/p indices in an ensemble.

	""",

	activity.Activity: """
		Base class for activities.

	""",

	activity.AxisMember: """
		Description of a given ensemble member. It will normally be related to a specific
    ensemble requirement. Note that start dates can be extracted directly from the simulations
    and do not need to be recorded with an axis member description.

	""",



	software.DevelopmentPath: """
		Describes the software development path for this model/component.

	""",

	software.EntryPoint: """
		Describes a function or subroutine of a SoftwareComponent.
    BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model.
    Currently, a very basic schedule can be approximated by using the 'proceeds' and 'follows' attributes,
    however a more complete system is required for full BFG compatibility.
    Every EntryPoint can have a set of arguments associated with it.
    These reference (previously defined) variables.

	""",

	software.Variable: """
		An instance of a model software variable which may be prognostic or diagnostic, and which is
    available as a connection to other software components. Note that these variables may only exist
    within the software workflow as interim quantities or coupling endpoints. Input and output
    variables will be a subset of these software variables.

	""",

	software.SoftwareComponent: """
		An embedded piece of software that does not normally function as a standalone model (although
    it may be used standalone in a test harness).

	""",

	software.Composition: """
		Describes how component variables are coupled together either to/from other
    SoftwareComponents or external data files. The variables specified by a component's
    composition must be owned by that component, or a  child of that component;
    child components cannot couple together parent variables.

	""",

	software.ComponentBase: """
		Base class for software component properties, whether a top level model,
    or a specific piece of code known as a component. In software terms, a
    component is a discrete set of code that takes input data and generates output data.
    Components may or may not have scientific descriptions.

	""",

	software.Gridspec: """
		Fully defines the computational grid used.

	""",



	science.Extent: """
		Key scientific characteristics of the grid use to simulate a specific domain.
    Note that the extent does not itself describe a grid, so, for example, a polar
    stereographic grid may have an extent of northern boundary 90N, southern boundary
    45N, but the fact that it is PS comes from the grid_type.

	""",

	science.Grid: """
		This describes the numerical grid used for the calculations.
    It is not necessarily the grid upon which the data is output.
    It is NOT the resolution, which is a property of a specific domain.

	""",

	science.Process: """
		Provides structure for description of a process simulated within a particular
    area (or domain/realm/component) of a model. This will often be subclassed
    within a specific implementation so that constraints can be used to ensure
    that the process details requested are consistent with project requirements
    for information.

	""",

	science.Algorithm: """
		Used to hold information associated with an algorithm which implements some key
    part of a process. In most cases this is quite a high level concept and isn't intended
    to describe the gory detail of how the code implements the algorithm rather the key
    scientific aspects of the algorithm. In particular, it provides a method
    of grouping variables which take part in an algorithm within a process.

	""",

	science.ScientificDomain: """
		Scientific area of a numerical model - usually a sub-model or component.
    Can also be known as a realm.

	""",

	science.ConservationProperties: """
		Describes how prognostic variables are conserved.

	""",

	science.Resolution: """
		Describes the computational spatial resolution of a component or process.
    Not intended to replace or replicate the output grid description.
    When it appears as part of a process description, provide only properties that differ from parent domain.
    Note that this is supposed to capture gross features of the grid, we expect many grids will have
    different variable layouts, those should be described in the grid description, and the exact resolution
    is not required. Note that many properties are not appropriate for adaptive grids.

	""",

	science.KeyProperties: """
		High level list of key properties. It can be specialised in
    extension packages using the detail extensions.

	""",

	science.ScienceContext: """
		This is the base class for the science mixins, that is the classes which
    we expect to be specialised and extended by project specific vocabularies.
    It is expected that values of these will be provided within vocabulary
    definitions.

	""",

	science.SubProcess: """
		Provides structure for description of part of process simulated within a particular
    area (or domain/realm/component) of a model. Typically this will be a part of process
    which shares common properties. It will normally be sub classed within a specific
    implementation so that constraints can be used to ensure that the process details requested are
    consistent with projects requirements for information.

	""",

	science.Detail: """
		Provides detail of specific properties, there are two possible specialisations
    expected: (1) A detail_vocabulary is identified, and a cardinality is assigned to that
    for possible responses, or (2) Detail is used to provide a collection for a set of
    properties which are defined in the sub-class. However, those properties must have a type
    which is selected from the classmap (that is, standard 'non-es-doc' types).

	""",

	science.Tuning: """
		Method used to optimise equation parameters in model component (aka 'tuning').

	""",

	science.Model: """
		A model component: can be executed standalone, and has as scientific
    description available via a link to a science.domain document. (A configured model can
     be understood in terms of a simulation, a model, and a configuration.).

	""",



	data.Dataset: """
		Dataset discovery information.

	""",

	data.Simulation: """
		Simulation class provides the integrating link about what models were run and wny.
    In many cases this should be auto-generated from output file headers.

	""",

	data.VariableCollection: """
		A collection of variables within the scope of a code or process element.

	""",

	data.Downscaling: """
		Defines a downscaling activity.

	""",



	drs.DrsEnsembleIdentifier: """
		Identifies an ensemble realisation.

	""",

	drs.DrsPublicationDataset: """
		A collection of atomic datasets which share a single combination of DRS component values.

	""",

	drs.DrsAtomicDataset: """
		An entity in a DRS file system.

	""",

	drs.DrsTemporalIdentifier: """
		Provides information about temporal subsetting and/or averaging.
    If only N1 is present, it a temporal instant,
    If N1-N2 are present with no suffix, it is a temporal subset,
    If N1-N2 with a suffix are present, then some sort of temporal averaging has been applied across
    the period.

	""",

	drs.DrsGeographicalIndicator: """
		Specifies geographical subsets described by bounding boxes or by named regions.
     One of spatial domain or bounding box must appear.

	""",



	platform.StoragePool: """
		Homogeneous storage pool on a computing machine.

	""",

	platform.StorageVolume: """
		Volume and units.

	""",

	platform.Machine: """
		A computer/system/platform/machine which is used for simulation.

	""",

	platform.ComputePool: """
		Homogeneous pool of nodes within a computing machine.

	""",

	platform.ComponentPerformance: """
		Describes the simulation rate of a component in seconds per model day.

	""",

	platform.Performance: """
		Describes the properties of a performance of a configured model on a particular system/machine.

	""",

	platform.Partition: """
		A major partition (component) of a computing system (aka machine).

	""",


	# ------------------------------------------------
	# Class properties.
	# ------------------------------------------------



	(designing.NumericalExperiment, 'related_experiments'):
		"A related experiment.",

	(designing.NumericalExperiment, 'requirements'):
		"Requirements that conformant simulations need to satisfy.",



	(designing.Project, 'previous_projects'):
		"Previous projects with similar aims.",

	(designing.Project, 'sub_projects'):
		"Activities within the project with their own name and aim(s).",

	(designing.Project, 'requires_experiments'):
		"Experiments required to deliver project.",



	(designing.ForcingConstraint, 'group'):
		"Sub-Category (e.g. GHG).",

	(designing.ForcingConstraint, 'code'):
		"Programme wide code from a controlled vocabulary (e.g. N2O).",

	(designing.ForcingConstraint, 'data_link'):
		"Link to actual data record if possible.",

	(designing.ForcingConstraint, 'additional_constraint'):
		"Additional information, e.g. hold constant from 2100-01-01.",

	(designing.ForcingConstraint, 'origin'):
		"Pointer to origin, e.g. CMIP6 RCP database.",

	(designing.ForcingConstraint, 'forcing_type'):
		"Type of integration.",

	(designing.ForcingConstraint, 'category'):
		"Category to which this belongs (from a CV, e.g. GASES).",



	(designing.MultiTimeEnsemble, 'ensemble_members'):
		"Description of date or time set of start dates.",



	(designing.TemporalConstraint, 'start_date'):
		"Required start date.",

	(designing.TemporalConstraint, 'required_calendar'):
		"Required calendar (e.g. for paleo simulations).",

	(designing.TemporalConstraint, 'start_flexibility'):
		"Amount of time before required start date that it is permissible to begin integration.",

	(designing.TemporalConstraint, 'required_duration'):
		"Constraint on time or length of simulation.",



	(designing.NumericalRequirement, 'additional_requirements'):
		"Additional detail for this requirement.",

	(designing.NumericalRequirement, 'conformance_is_requested'):
		"Indicator as to whether ensemble documentation should include conformance information for this requirement.",



	(designing.EnsembleRequirement, 'ensemble_type'):
		"Type of ensemble.",

	(designing.EnsembleRequirement, 'ensemble_member'):
		"Constraint on each ensemble member.",

	(designing.EnsembleRequirement, 'minimum_size'):
		"Minimum number of members.",



	(designing.OutputTemporalRequirement, 'continuous_subset'):
		"Set of periods for which continuous output is required.",

	(designing.OutputTemporalRequirement, 'throughout'):
		"Whether or not output is required throughout simulation.",

	(designing.OutputTemporalRequirement, 'sliced_subset'):
		"Description of how slices are laid out.",



	(designing.MultiEnsemble, 'ensemble_axis'):
		"List of orthogonal ensembles.",



	(designing.SimulationPlan, 'will_support_experiments'):
		"An experiment with which the planned simulation will be associated.",

	(designing.SimulationPlan, 'expected_platform'):
		"The machine on which the simulation will be run.",

	(designing.SimulationPlan, 'expected_model'):
		"The model used to run the simulation.",

	(designing.SimulationPlan, 'expected_performance_sypd'):
		"Expected performance in simulated years per real day.",



	(designing.DomainProperties, 'required_extent'):
		"Constraint on extent of domain to be simulated.",

	(designing.DomainProperties, 'required_resolution'):
		"Constraint on resolution required in simulated domain.",





	(shared.Pid, 'id'):
		"The identifier.",

	(shared.Pid, 'resolution_service'):
		"The resolution service.",



	(shared.NumberArray, 'values'):
		"A space separated list of numbers.",



	(shared.OnlineResource, 'description'):
		"Detail of how to access the resource.",

	(shared.OnlineResource, 'name'):
		"Name of online resource.",

	(shared.OnlineResource, 'protocol'):
		"Protocol to use at the linkage.",

	(shared.OnlineResource, 'linkage'):
		"A URL.",



	(shared.Party, 'meta'):
		"Provides a unique identifier for the party.",

	(shared.Party, 'name'):
		"Name of person or organisation.",

	(shared.Party, 'email'):
		"Email address.",

	(shared.Party, 'orcid_id'):
		"Orcid ID if available.",

	(shared.Party, 'url'):
		"URL of person or institution.",

	(shared.Party, 'organisation'):
		"True if an organisation not a person.",

	(shared.Party, 'address'):
		"Institutional address.",



	(shared.KeyFloat, 'key'):
		"User defined key.",

	(shared.KeyFloat, 'value'):
		"Value associated with a key (real number).",



	(shared.DatetimeSet, 'length'):
		"Number of times in set.",



	(shared.DocReference, 'id'):
		"Identifier of remote resource, if known.",

	(shared.DocReference, 'type'):
		"The type of the remote record.",

	(shared.DocReference, 'relationship'):
		"Predicate - relationship of the object target as seen from the subject resource.",

	(shared.DocReference, 'constraint_vocabulary'):
		"A constraint vocabulary for the relationship.",

	(shared.DocReference, 'context'):
		"Information about remote record in context of reference.",

	(shared.DocReference, 'version'):
		"The version of the remote record.",



	(shared.DateTime, 'offset'):
		"Date is offset from start of an integration.",

	(shared.DateTime, 'value'):
		"Date or time - some of (from left to right): yyyy-mm-dd:hh:mm:ss.",



	(shared.TimesliceList, 'members'):
		"Values as integers.",

	(shared.TimesliceList, 'units'):
		"Interval against which members refer.",



	(shared.DocMetaInfo, 'type'):
		"Document ontology type.",

	(shared.DocMetaInfo, 'institute'):
		"Name of institute with which instance is associated with.",

	(shared.DocMetaInfo, 'source'):
		"Name of application that created the instance.",

	(shared.DocMetaInfo, 'type_sort_key'):
		"Document type sort key.",

	(shared.DocMetaInfo, 'drs_keys'):
		"DRS related keys to support correlation of documents with datasets.",

	(shared.DocMetaInfo, 'sort_key'):
		"Document sort key.",

	(shared.DocMetaInfo, 'drs_path'):
		"DRS related path to support documents with datasets.",

	(shared.DocMetaInfo, 'create_date'):
		"Date upon which the instance was created.",

	(shared.DocMetaInfo, 'type_display_name'):
		"Document type display name.",

	(shared.DocMetaInfo, 'language'):
		"Language with which instance is associated with.",

	(shared.DocMetaInfo, 'source_key'):
		"Key of application that created the instance.",

	(shared.DocMetaInfo, 'update_date'):
		"Date upon which the instance was last updated.",

	(shared.DocMetaInfo, 'author'):
		"Author of the metadata in the parent document.",

	(shared.DocMetaInfo, 'project'):
		"Name of project with which instance is associated with.",

	(shared.DocMetaInfo, 'version'):
		"Document version identifier.",

	(shared.DocMetaInfo, 'id'):
		"Universal document identifier (normally a UUID).",

	(shared.DocMetaInfo, 'external_ids'):
		"Set of identifiers used to reference the document by external parties.",



	(shared.TimePeriod, 'units'):
		"Appropriate time units.",

	(shared.TimePeriod, 'date'):
		"Optional start/end date of time period.",

	(shared.TimePeriod, 'length'):
		"Duration of the time period.",

	(shared.TimePeriod, 'calendar'):
		"Calendar, default is standard aka gregorian.",

	(shared.TimePeriod, 'date_type'):
		"Describes how the date is used to define the period.",



	(shared.RegularTimeset, 'increment'):
		"Interval between members of set.",

	(shared.RegularTimeset, 'start_date'):
		"Beginning of time set.",

	(shared.RegularTimeset, 'length'):
		"Number of times in set.",



	(shared.ExternalDocument, 'online_at'):
		"Location of electronic version.",

	(shared.ExternalDocument, 'title'):
		"Title or name of the document.",

	(shared.ExternalDocument, 'date'):
		"Date of publication, or of access in the case of a URL.",

	(shared.ExternalDocument, 'doi'):
		"Digital Object Identifier, if it exists.",

	(shared.ExternalDocument, 'meta'):
		"Metadata about the creation of this document description.",

	(shared.ExternalDocument, 'publication_detail'):
		"Journal/publisher, page and volume information as appropriate.",

	(shared.ExternalDocument, 'name'):
		"A name for the citation: short hand description, e.g. Meehl et al (2014).",

	(shared.ExternalDocument, 'authorship'):
		"List of authors expressed using an appropriate syntax.",



	(shared.QualityReview, 'quality_description'):
		"Assessment of quality of this document.",

	(shared.QualityReview, 'date'):
		"Date upon which review was made.",

	(shared.QualityReview, 'quality_status'):
		"Status from a controlled vocabulary.",

	(shared.QualityReview, 'metadata_reviewer'):
		"Party who made the metadata quality assessment.",



	(shared.Reference, 'context'):
		"Brief text description of why this resource is being cited.",

	(shared.Reference, 'document'):
		"Reference Target.",



	(shared.Responsibility, 'when'):
		"Period when role was active, if no longer.",

	(shared.Responsibility, 'party'):
		"Parties delivering responsibility.",

	(shared.Responsibility, 'role'):
		"Role that the party plays or played.",



	(shared.Cimtext, 'content'):
		"Raw content (including markup).",

	(shared.Cimtext, 'content_type'):
		"Type of content.",



	(shared.Calendar, 'description'):
		"Extra information about the calendar.",

	(shared.Calendar, 'name'):
		"Can be used to name a special calendar type.",

	(shared.Calendar, 'standard_name'):
		"Type of calendar used.",

	(shared.Calendar, 'month_lengths'):
		"Used for special calendars to provide month lengths.",



	(shared.IrregularDateset, 'date_set'):
		"Set of dates, comma separated yyyy-mm-dd.",





	(activity.Conformance, 'target_requirement'):
		"URI of the target numerical requirement.",



	(activity.Ensemble, 'has_ensemble_axes'):
		"Set of axes for the ensemble.",

	(activity.Ensemble, 'common_conformances'):
		"Conformance documents for requirements common across ensemble.",

	(activity.Ensemble, 'part_of'):
		"Link to one or more over-arching ensembles that might includes this one.",

	(activity.Ensemble, 'documentation'):
		"Links to web-pages and other ensemble specific documentation (including workflow descriptions).",

	(activity.Ensemble, 'members'):
		"The set of ensemble members.",

	(activity.Ensemble, 'supported'):
		"Experiments with which the ensemble is associated (may differ from constituent simulations).",



	(activity.UberEnsemble, 'child_ensembles'):
		"Ensemble which are aggregated into this one.",



	(activity.EnsembleMember, 'errata'):
		"Link to errata associated with this simulation.",

	(activity.EnsembleMember, 'simulation'):
		"Actual simulation description for an ensemble member.",

	(activity.EnsembleMember, 'had_performance'):
		"Performance of the simulation.",

	(activity.EnsembleMember, 'variant_id'):
		"A string which concatenates axis member short identiers (e.g r1i1p1f1).",

	(activity.EnsembleMember, 'ran_on'):
		"The machine on which the simulation was run.",



	(activity.ParentSimulation, 'parent'):
		"The parent simulation of this child.",

	(activity.ParentSimulation, 'branch_time_in_child'):
		"The time at which the present simulation started in the child calendar.",

	(activity.ParentSimulation, 'branch_time_in_parent'):
		"The time in parent simulation calendar at which this simulation was branched.",



	(activity.EnsembleAxis, 'extra_detail'):
		"Any extra detail required to describe how this ensemble axis was delivered.",

	(activity.EnsembleAxis, 'short_identifier'):
		"e.g. 'r' or 'i' or 'p' to conform with simulation ensemble variant identifiers.",

	(activity.EnsembleAxis, 'target_requirement'):
		"URI of the target numerical requirement.",

	(activity.EnsembleAxis, 'member'):
		"Individual member descriptions along axis.",



	(activity.Activity, 'canonical_name'):
		"Community defined identifier or name.",

	(activity.Activity, 'references'):
		"Relevant documentation.",

	(activity.Activity, 'long_name'):
		"Longer version of activity name.",

	(activity.Activity, 'meta'):
		"Metadata describing how this document was created.",

	(activity.Activity, 'name'):
		"Short name or abbreviation.",

	(activity.Activity, 'duration'):
		"Time the activity was (or will be) active.",

	(activity.Activity, 'responsible_parties'):
		"People or organisations responsible for activity.",

	(activity.Activity, 'description'):
		"Description of what is to be done (or was done).",

	(activity.Activity, 'keywords'):
		"User defined keywords.",

	(activity.Activity, 'rationale'):
		"Explanation of why this activity was carried out and/or what it was intended to achieve.",



	(activity.AxisMember, 'description'):
		"Description of the member (or name of parameter varied).",

	(activity.AxisMember, 'index'):
		"The ensemble member index.",

	(activity.AxisMember, 'value'):
		"If parameter varied, value thereof for this member.",

	(activity.AxisMember, 'extra_detail'):
		"If necessary: further information about ensemble member conformance.",





	(software.DevelopmentPath, 'consortium_name'):
		"If model/component is developed as part of a consortium, provide consortium name.",

	(software.DevelopmentPath, 'previous_version'):
		"Name of a previous version.",

	(software.DevelopmentPath, 'developed_in_house'):
		"Model or component was mostly developed in house.",

	(software.DevelopmentPath, 'funding_sources'):
		"The entities that funded this software component.",

	(software.DevelopmentPath, 'creators'):
		"Those responsible for creating this component.",



	(software.EntryPoint, 'name'):
		"#FIXME.",



	(software.Variable, 'prognostic'):
		"Whether or not prognostic or diagnostic.",

	(software.Variable, 'description'):
		"Description of how the variable is being used in the s/w.",

	(software.Variable, 'name'):
		"Short name for the variable.",



	(software.SoftwareComponent, 'coupling_framework'):
		"The coupling framework that this entire component conforms to.",

	(software.SoftwareComponent, 'license'):
		"The license held by this piece of software.",

	(software.SoftwareComponent, 'dependencies'):
		"#FIXME.",

	(software.SoftwareComponent, 'connection_points'):
		"The set of data entities which are available for I/O and/or coupling.",

	(software.SoftwareComponent, 'sub_components'):
		"Internal software sub-components of this component.",

	(software.SoftwareComponent, 'composition'):
		"#FIXME.",

	(software.SoftwareComponent, 'language'):
		"Language the component is written in.",

	(software.SoftwareComponent, 'grid'):
		"A reference to the grid that is used by this component.",



	(software.Composition, 'couplings'):
		"#FIXME.",

	(software.Composition, 'description'):
		"#FIXME.",



	(software.ComponentBase, 'repository'):
		"Location of code for this component.",

	(software.ComponentBase, 'long_name'):
		"Long name for component.",

	(software.ComponentBase, 'development_history'):
		"History of the development of this component.",

	(software.ComponentBase, 'name'):
		"Short name of component.",

	(software.ComponentBase, 'description'):
		"Textural description of component.",

	(software.ComponentBase, 'version'):
		"Version identifier.",

	(software.ComponentBase, 'release_date'):
		"The date of publication of the component code (as opposed to the date of publication of the metadata document, or the date of deployment of the model).",

	(software.ComponentBase, 'documentation'):
		"Descriptions of the component functionality.",



	(software.Gridspec, 'description'):
		"Textural description.",





	(science.Extent, 'bottom_vertical_level'):
		"Bottom vertical level centre (e.g. level near land surface or level ocean floor).",

	(science.Extent, 'z_units'):
		"Units of vertical measure (e.g. m, Pa, sigma_level.",

	(science.Extent, 'southern_boundary'):
		"If not global, southern boundary in degrees of latitude.",

	(science.Extent, 'western_boundary'):
		"If not global, western boundary in degrees of longitude.",

	(science.Extent, 'eastern_boundary'):
		"If not global, eastern boundary in degrees of longitude.",

	(science.Extent, 'is_global'):
		"True if horizontal coverage is global.",

	(science.Extent, 'northern_boundary'):
		"If not global, northern boundary in degrees of latitude.",

	(science.Extent, 'top_vertical_level'):
		"Top vertical level centre (e.g. level at TOA or level near ocean surface).",

	(science.Extent, 'region_known_as'):
		"Identifier or identifiers for the region covered by the extent.",



	(science.Grid, 'name'):
		"This is a string usually used by the modelling group to describe the grid.(e.g. the ENDGAME/New Dynamics dynamical cores have their own grids describing variable layouts.",

	(science.Grid, 'vertical_grid_type'):
		"Description of basic vertical grid (e.g. 'atmosphere_hybrid_height_coordinate').",

	(science.Grid, 'horizontal_grid_layout'):
		"Type of horizontal grid-layout (e.g. Arakawa C-Grid.",

	(science.Grid, 'horizontal_grid_type'):
		"Description of basic horizontal grid (e.g. 'cubed-sphere').",

	(science.Grid, 'additional_details'):
		"Additional grid properties.",

	(science.Grid, 'vertical_grid_layout'):
		"Type of vertical grid-layout (e.g. Charney-Phillips.",

	(science.Grid, 'meta'):
		"Metadata about how the model description was constructed.",

	(science.Grid, 'grid_extent'):
		"Key geographic characteristics of the grid use to simulate a specific domain.",



	(science.Process, 'properties'):
		"Sets of properties for this process.",

	(science.Process, 'algorithms'):
		"Descriptions of algorithms and their properties used in the process.",

	(science.Process, 'references'):
		"Any relevant references describing this process and/or it's implementation.",

	(science.Process, 'implementation_overview'):
		"General overview description of the implementation of this process.",

	(science.Process, 'sub_processes'):
		"Discrete portion of a process with common process details.",

	(science.Process, 'keywords'):
		"keywords to help re-use and discovery of this information.",



	(science.Algorithm, 'implementation_overview'):
		"Overview of the algorithm implementation.",

	(science.Algorithm, 'diagnostic_variables'):
		"Diagnostic variables associated with this algorithm.",

	(science.Algorithm, 'prognostic_variables'):
		"Prognostic variables associated with this algorithm.",

	(science.Algorithm, 'references'):
		"Relevant references.",

	(science.Algorithm, 'forced_variables'):
		"Variables held constant within algorithm.",



	(science.ScientificDomain, 'meta'):
		"Metadata describing the construction of this domain description.",

	(science.ScientificDomain, 'overview'):
		"Free text overview description of key properties of domain.",

	(science.ScientificDomain, 'name'):
		"Name of the scientific domain (e.g. ocean).",

	(science.ScientificDomain, 'simulates'):
		"Processes simulated within the domain.",

	(science.ScientificDomain, 'differing_key_properties'):
		"Key properties for the domain which differ from model defaults (grid, timestep etc).",

	(science.ScientificDomain, 'id'):
		"Vocabulary identifier, where this domain description was constructed via a  controlled vocabulary.",

	(science.ScientificDomain, 'realm'):
		"Canonical name for the domain of this scientific area.",

	(science.ScientificDomain, 'references'):
		"Any relevant references describing the implementation of this domain in a relevant model.",



	(science.ConservationProperties, 'flux_correction_was_used'):
		"Flag to indicate if correction involved flux correction.",

	(science.ConservationProperties, 'corrected_conserved_prognostic_variables'):
		"Set of variables which are conserved by *more* than the numerical scheme alone.",

	(science.ConservationProperties, 'correction_methodology'):
		"Description of method by which correction was achieved.",



	(science.Resolution, 'typical_x_degrees'):
		"Horizontal X resolution in degrees of grid cells, if applicable eg. 3.75.",

	(science.Resolution, 'is_adaptive_grid'):
		"Default is False. Set true if grid resolution changes during execution.",

	(science.Resolution, 'name'):
		"This is a string usually used by the modelling group to describe the resolution of this grid,  e.g. N512L180 or T512L70 etc.",

	(science.Resolution, 'number_of_levels'):
		"Number of vertical levels resolved.",

	(science.Resolution, 'number_of_xy_gridpoints'):
		"Total number of horizontal points on computational grids.",

	(science.Resolution, 'equivalent_resolution_km'):
		"Resolution in km of 'typical grid cell' (at the equator, for gross comparisons of resolution), eg. 50.",

	(science.Resolution, 'typical_y_degrees'):
		"Horizontal Y resolution in degrees of grid cells, if applicable eg. 2.5.",



	(science.KeyProperties, 'extra_conservation_properties'):
		"Details of methodology needed to conserve variables between processes.",

	(science.KeyProperties, 'tuning_applied'):
		"Describe any tuning used to optimise the parameters in this domain.",

	(science.KeyProperties, 'grid'):
		"The grid used to layout the variables (e.g. the Global ENDGAME-grid).",

	(science.KeyProperties, 'resolution'):
		"The resolution of the grid (e.g. N512L180).",

	(science.KeyProperties, 'additional_detail'):
		"Additional property details.",

	(science.KeyProperties, 'time_step'):
		"Timestep (in seconds) of overall component.",



	(science.ScienceContext, 'name'):
		"The name of this process/algorithm/sub-process/detail.",

	(science.ScienceContext, 'context'):
		"Scientific context for which this description is provided.",

	(science.ScienceContext, 'id'):
		"Identifier for this collection of properties.",



	(science.SubProcess, 'references'):
		"Any relevant references describing this part of the process and/or it's implementation.",

	(science.SubProcess, 'implementation_overview'):
		"General overview description of the implementation of this part of the process.",

	(science.SubProcess, 'properties'):
		"Sets of properties for this process.",



	(science.Detail, 'from_vocab'):
		"Name of an enumeration vocabulary of possible detail options.",

	(science.Detail, 'with_cardinality'):
		"Required cardinality of selection from vocabulary.",

	(science.Detail, 'content'):
		"Free text description of process detail (if required).",

	(science.Detail, 'select'):
		"Name of property to be selected from vocab.",

	(science.Detail, 'detail_selection'):
		"List of choices from the vocabulary of possible detailed options.",



	(science.Tuning, 'trend_metrics_used'):
		"Which observed trend metrics have been used in tuning model parameters.",

	(science.Tuning, 'description'):
		"Brief description of tuning methodology. Include information about observational period(s) used.",

	(science.Tuning, 'regional_metrics_used'):
		"Which regional metrics of mean state (e.g Monsoons, tropical means etc) have been used in tuning.",

	(science.Tuning, 'global_mean_metrics_used'):
		"Set of metrics of the global mean state used in tuning model parameters.",



	(science.Model, 'coupler'):
		"Overarching coupling framework for model.",

	(science.Model, 'simulates'):
		"The scientific domains which this model simulates.",

	(science.Model, 'id'):
		"Vocabulary identifier, where this model description was constructed via a controlled vocabulary.",

	(science.Model, 'coupled_components'):
		"Software components which are linked together using a coupler to deliver this model.",

	(science.Model, 'internal_software_components'):
		"Software modules which together provide the functionality for this model.",

	(science.Model, 'model_default_properties'):
		"Model default key properties (may be over-ridden in domain properties).",

	(science.Model, 'meta'):
		"Metadata about how the model description was constructed.",

	(science.Model, 'category'):
		"Generic type for this model.",





	(data.Dataset, 'meta'):
		"Metadata describing the creation of this dataset description document.",

	(data.Dataset, 'availability'):
		"Where the data is located, and how it is accessed.",

	(data.Dataset, 'name'):
		"Name of dataset.",

	(data.Dataset, 'description'):
		"Textural description of dataset.",

	(data.Dataset, 'responsible_parties'):
		"Individuals and organisations reponsible for the data.",

	(data.Dataset, 'produced_by'):
		"Makes a link back to originating activity.",

	(data.Dataset, 'drs_datasets'):
		"Data available in the DRS.",

	(data.Dataset, 'references'):
		"Relevant reference document.",

	(data.Dataset, 'related_to_dataset'):
		"Related dataset.",



	(data.Simulation, 'ran_for_experiments'):
		"One or more experiments with which the simulation is associated.",

	(data.Simulation, 'parent_simulation'):
		"If appropriate, detailed information about how this simulation branched from a previous one.",

	(data.Simulation, 'calendar'):
		"The calendar used in the simulation.",

	(data.Simulation, 'used'):
		"The model used to run the simulation.",

	(data.Simulation, 'part_of_project'):
		"Project or projects for which simulation was run.",

	(data.Simulation, 'primary_ensemble'):
		"Primary Ensemble (ensemble for which this simulation was first run).",

	(data.Simulation, 'ensemble_identifier'):
		"String that can be used to extract ensemble axis membership from the primary ensemble(e.g. cmip6 rip string as in the DRS).",



	(data.VariableCollection, 'collection_name'):
		"Name for this variable collection.",

	(data.VariableCollection, 'variables'):
		"Set of variable names.",



	(data.Downscaling, 'downscaled_from'):
		"The simulation that was downscaled by this downscaling activity.",





	(drs.DrsEnsembleIdentifier, 'realisation_number'):
		"Standard ensemble axis realisation number (usually an initial condition ensemble).",

	(drs.DrsEnsembleIdentifier, 'initialisation_method_number'):
		"Identifies which method of initialisation was used, if multiple methods used.",

	(drs.DrsEnsembleIdentifier, 'perturbation_number'):
		"Identifies different members of a perturbed physics ensemble.",



	(drs.DrsPublicationDataset, 'institute'):
		"The institute responsible for this data entity.",

	(drs.DrsPublicationDataset, 'experiment'):
		"An experiment (or experiment family and type, e.g. rcp45).",

	(drs.DrsPublicationDataset, 'model'):
		"A model identifier (sans blanks/periods and parenthesis).",

	(drs.DrsPublicationDataset, 'realm'):
		"Modelling realm.",

	(drs.DrsPublicationDataset, 'product'):
		"Used to provide categories of data products within the activity.",

	(drs.DrsPublicationDataset, 'activity'):
		"A model intercomparison activity or other project which aggregates or collects data.",

	(drs.DrsPublicationDataset, 'frequency'):
		"Frequency of data stored in this entity.",

	(drs.DrsPublicationDataset, 'version_number'):
		"Uniquely identifies a particular version of a publication level dataset.",



	(drs.DrsAtomicDataset, 'ensemble_member'):
		"Unambiguously identifiers ensemble realisation information.",

	(drs.DrsAtomicDataset, 'temporal_constraint'):
		"Identifies temporal subsets or means.",

	(drs.DrsAtomicDataset, 'geographical_constraint'):
		"Identifies geographical subsets and spatial means.",

	(drs.DrsAtomicDataset, 'variable_name'):
		"Identifies the physical quantity (when used in conjunction with the MIP table).",

	(drs.DrsAtomicDataset, 'mip_table'):
		"The MIP table, together with the variable defines the physical quantity.",



	(drs.DrsTemporalIdentifier, 'suffix'):
		"If present, used to indicate climatology or average.",

	(drs.DrsTemporalIdentifier, 'end'):
		"N2, required to indicate a period.",

	(drs.DrsTemporalIdentifier, 'start'):
		"N1,  of the form yyyy[MM[dd[hh[mm[ss]]]]].",



	(drs.DrsGeographicalIndicator, 'bounding_box'):
		"DRS bounding box of the form 'latJHJJHHlonMZMMZZ' where H, HH, Z, ZZ are from {NS} {EW} respectively.",

	(drs.DrsGeographicalIndicator, 'spatial_domain'):
		"Geographical indicator (currently only 'global' is acceptable).",

	(drs.DrsGeographicalIndicator, 'operator'):
		"Spatial averagin applied to the geographical region.",





	(platform.StoragePool, 'type'):
		"Type of storage.",

	(platform.StoragePool, 'volume_available'):
		"Storage capacity.",

	(platform.StoragePool, 'vendor'):
		"Vendor of the storage unit.",

	(platform.StoragePool, 'description'):
		"Description of the technology used.",

	(platform.StoragePool, 'name'):
		"Name of storage pool.",



	(platform.StorageVolume, 'units'):
		"Volume units.",

	(platform.StorageVolume, 'volume'):
		"Numeric value.",



	(platform.Machine, 'meta'):
		"Document description.",



	(platform.ComputePool, 'compute_cores_per_node'):
		"Number of CPU cores per node.",

	(platform.ComputePool, 'memory_per_node'):
		"Memory per node.",

	(platform.ComputePool, 'accelerator_type'):
		"Type of accelerator.",

	(platform.ComputePool, 'cpu_type'):
		"CPU type.",

	(platform.ComputePool, 'model_number'):
		"Model/Board number/type.",

	(platform.ComputePool, 'description'):
		"Textural description of pool.",

	(platform.ComputePool, 'name'):
		"Name of compute pool within a machine.",

	(platform.ComputePool, 'accelerators_per_node'):
		"Number of accelerator units on a node.",

	(platform.ComputePool, 'interconnect'):
		"Interconnect used.",

	(platform.ComputePool, 'number_of_nodes'):
		"Number of nodes.",

	(platform.ComputePool, 'operating_system'):
		"Operating system.",



	(platform.ComponentPerformance, 'cores_used'):
		"Number of cores used for this component.",

	(platform.ComponentPerformance, 'component'):
		"Link to a CIM software component description.",

	(platform.ComponentPerformance, 'speed'):
		"Time taken to simulate one real day (s).",

	(platform.ComponentPerformance, 'nodes_used'):
		"Number of nodes used for this component.",

	(platform.ComponentPerformance, 'component_name'):
		"Short name of component.",



	(platform.Performance, 'io_load'):
		"Percentage of time spent in I/O.",

	(platform.Performance, 'sypd'):
		"Simulated years per wall-clock day.",

	(platform.Performance, 'memory_bloat'):
		"Percentage of extra memory needed.",

	(platform.Performance, 'chsy'):
		"Core-Hours per simulated year.",

	(platform.Performance, 'subcomponent_performance'):
		"Describes the performance of each subcomponent.",

	(platform.Performance, 'meta'):
		"Document metadata.",

	(platform.Performance, 'name'):
		"Short name for performance (experiment/test/whatever).",

	(platform.Performance, 'total_nodes_used'):
		"Number of nodes used.",

	(platform.Performance, 'compiler'):
		"Compiler used.",

	(platform.Performance, 'load_imbalance'):
		"Load imbalance.",

	(platform.Performance, 'coupler_load'):
		"Percentage of time spent in coupler.",

	(platform.Performance, 'platform'):
		"Platform on which performance was tested.",

	(platform.Performance, 'asypd'):
		"Actual simulated years per wall-clock day, all-in.",

	(platform.Performance, 'model'):
		"Model for which performance was tested.",



	(platform.Partition, 'online_documentation'):
		"Links to documentation.",

	(platform.Partition, 'when_used'):
		"If no longer in use, the time period it was in use.",

	(platform.Partition, 'description'):
		"Textural description of machine.",

	(platform.Partition, 'partition'):
		"If machine is partitioned, treat subpartitions as machines.",

	(platform.Partition, 'institution'):
		"Institutional location.",

	(platform.Partition, 'vendor'):
		"The system integrator or vendor.",

	(platform.Partition, 'model_number'):
		"Vendor's model number/name - if it exists.",

	(platform.Partition, 'name'):
		"Name of partition (or machine).",

	(platform.Partition, 'storage_pools'):
		"Storage resource available.",

	(platform.Partition, 'compute_pools'):
		"Layout of compute nodes.",



	# ------------------------------------------------
	# Enums.
	# ------------------------------------------------


	designing.ExperimentalRelationships: """
		Defines the canonical set of experimental relationships.

	""",

	designing.EnsembleTypes: """
		Defines the various axes along which one can set up an ensemble.

	""",

	designing.ForcingTypes: """
		Defines the possible set of forcing types for a forcing constraint.

	""",



	shared.TimeUnits: """
		Appropriate Time units for experiment durations in NWP and Climate Modelling.

	""",

	shared.TextCode: """
		Types of text understood by the CIM notebook. Currently only
    plaintext, but we expect safe HTML to be supported as soon as practicable.

	""",

	shared.PeriodDateTypes: """
		A period date type enum (used by time_period).

	""",

	shared.RoleCode: """
		Responsibility role codes: roles that a party may play in delivering a responsibility.

	""",

	shared.CalendarTypes: """
		CF calendar types as defined in CF 1.6.

	""",

	shared.QualityStatus: """
		Assertion as to the review status of document.

	""",

	shared.DocumentTypes: """
		The complete set of CIM document types, that is, all classes which carry the
    document metadata attributes.

	""",

	shared.SlicetimeUnits: """
		Units for integers in a timeslice.

	""",

	shared.NilReason: """
		Provides an enumeration of possible reasons why a property has not been defined
    Based on GML nilReason as discussed here: https://www.seegrid.csiro.au/wiki/AppSchemas/NilValues.

	""",



	activity.ForcingTypes: """
		Defines the possible set of forcing types for a forcing constraint.

	""",

	activity.EnsembleTypes: """
		Defines the various axes along which one can set up an ensemble.

	""",



	software.ProgrammingLanguage: """
		The set of terms which define programming languages used for earth
    system simulation.

	""",

	software.CouplingFramework: """
		The set of terms which define known coupling frameworks.

	""",



	science.ModelTypes: """
		Defines a set of gross model classes.

	""",

	science.SelectionCardinality: """
		Provides the possible cardinalities for selecting from a controlled vocabulary.

	""",



	data.DataAssociationTypes: """
		Set of possible dataset associations.
    Selected from, and extended from,  ISO19115 (2014) DS_AssociationTypeCode.

	""",



	drs.DrsFrequencyTypes: """
		Set of allowed DRS frequency types.

	""",

	drs.DrsTimeSuffixes: """
		Set of permitted time averaging suffixes for drs temporal identifiers.

	""",

	drs.DrsRealms: """
		Set of allowed DRS modelling realms.

	""",

	drs.DrsGeographicalOperators: """
		Set of permitted spatial averaging operator suffixes for drs spatial indicators (yyyy-zzzz).

	""",



	platform.StorageSystems: """
		Controlled vocabulary for storage  types (including filesystems).

	""",

	platform.VolumeUnits: """
		Appropriate storage volume units.

	""",


	# ------------------------------------------------
	# Enum members.
	# ------------------------------------------------



	(designing.ExperimentalRelationships, 'initialisation_for'):
		"This experiment provides initialisation for the target experiment",

	(designing.ExperimentalRelationships, 'provides_constraints'):
		"This experiment provides constraint(s) for the target experiment (e.g SST forcing)",

	(designing.ExperimentalRelationships, 'control_for'):
		"This experiment provides a control for the target experiment",

	(designing.ExperimentalRelationships, 'is_sibling'):
		"Part of a family (e.g. experiments where solar forcing is either increased or reduced)",



	(designing.EnsembleTypes, 'Initialisation'):
		"Members are initialised to sample possible starting states",

	(designing.EnsembleTypes, 'Staggered Start'):
		"Members are initialised at different starting dates",

	(designing.EnsembleTypes, 'Forced'):
		"Members used differing forcing data",

	(designing.EnsembleTypes, 'Resolution'):
		"Members are run at different resolutions",

	(designing.EnsembleTypes, 'Perturbed Physics'):
		"Members differ in some aspects of their physics",

	(designing.EnsembleTypes, 'Initialisation Method'):
		"Members differ in how they are initialised",



	(designing.ForcingTypes, 'another simulation'):
		"From another simulation",

	(designing.ForcingTypes, 'scenario'):
		"Intended to represent a possible future, e.g. RCP4.5",

	(designing.ForcingTypes, 'historical'):
		"Best estimates of actual state (included synthesized)",

	(designing.ForcingTypes, 'idealised'):
		"Simplified and/or exemplar, e.g. 1%C02",





	(shared.TimeUnits, 'years'):
		None,

	(shared.TimeUnits, 'months'):
		None,

	(shared.TimeUnits, 'days'):
		None,

	(shared.TimeUnits, 'seconds'):
		None,



	(shared.TextCode, 'plaintext'):
		"Normal plain text",



	(shared.PeriodDateTypes, 'date is start'):
		"The date defines the start of the period",

	(shared.PeriodDateTypes, 'date is end'):
		"The date is the end of the period",

	(shared.PeriodDateTypes, 'unused'):
		"Date is not used",



	(shared.RoleCode, 'metadata_reviewer'):
		"Party who carried out an independent review of (this) documentation",

	(shared.RoleCode, 'user'):
		"Party who uses the resource",

	(shared.RoleCode, 'metadata_author'):
		"Party who created (this) documentation",

	(shared.RoleCode, 'owner'):
		"Party with legal ownership of the resource",

	(shared.RoleCode, 'distributor'):
		"Party who distributes the resource",

	(shared.RoleCode, 'sponsor'):
		"Party who has invested in the production of the resource",

	(shared.RoleCode, 'Principal Investigator'):
		"Key party responsible for the existence of the resource",

	(shared.RoleCode, 'publisher'):
		"Party who published the resource",

	(shared.RoleCode, 'originator'):
		"Original source for the resource if obtained from elsewhere",

	(shared.RoleCode, 'author'):
		"Party who created (or co-created) resource",

	(shared.RoleCode, 'resource provider'):
		"Party that supplies the resource",

	(shared.RoleCode, 'collaborator'):
		"Contributor to the production of the resource",

	(shared.RoleCode, 'processor'):
		"Party who has taken part in the workflow that resulted in this resource",

	(shared.RoleCode, 'custodian'):
		"Party that accepts accountability and responsibility for the source resource",

	(shared.RoleCode, 'point of contact'):
		"Party who can be contacted for acquiring knowledge about or acquisition of the resource",



	(shared.CalendarTypes, '365_day'):
		"Synonym for noleap:Gregorian calendar without leap years, i.e., all years are 365 days long.",

	(shared.CalendarTypes, 'all_leap'):
		"Gregorian calendar with every year being a leap year, i.e., all years are 366 days long.",

	(shared.CalendarTypes, 'gregorian'):
		"Mixed Gregorian/Julian calendar as defined by Udunits",

	(shared.CalendarTypes, '366_day'):
		"Synonym for all_leap:Gregorian calendar with every year being a leap year, i.e., all years are 366 days long.",

	(shared.CalendarTypes, '360_day'):
		"All years are 360 days divided into 30 day months.",

	(shared.CalendarTypes, 'julian'):
		"Julian Calendar",

	(shared.CalendarTypes, 'none'):
		"Perpetual time axis",

	(shared.CalendarTypes, 'proleptic_gregorian'):
		"A Gregorian calendar extended to dates before 1582-10-15. That is, a year is a leap year if either (i) it is divisible by 4 but not by 100 or (ii) it is divisible by 400.",

	(shared.CalendarTypes, 'noleap'):
		"Gregorian calendar without leap years, i.e., all years are 365 days long.",

	(shared.CalendarTypes, 'standard'):
		"Synonym for gregorian: Mixed Gregorian/Julian calendar as defined by Udunits",



	(shared.QualityStatus, 'finalised'):
		"Author has completed document, prior to review",

	(shared.QualityStatus, 'under_review'):
		"Document is being reviewed",

	(shared.QualityStatus, 'incomplete'):
		"Currently being worked on",

	(shared.QualityStatus, 'reviewed'):
		"Document has been formally reviewed and assessed as complete and accurate",



	(shared.DocumentTypes, 'Project'):
		"An umbrella for a set of numerical experiments (e.g. a MIP)",

	(shared.DocumentTypes, 'ScientificDomain'):
		"A scientifically coherent realm of a numerical model (typically modelled independently).",

	(shared.DocumentTypes, 'Simulation'):
		"A simulation carried out as part of an ensemble for a numerical experiment.",

	(shared.DocumentTypes, 'SimulationPlan'):
		"A plan to carry out a simulations for a numerical experiment.",

	(shared.DocumentTypes, 'TemporalConstraint'):
		"A constraint on the real time simulations need to represent for a numerical experiment.",

	(shared.DocumentTypes, 'UberEnsemble'):
		"An ensemble description that crosses multiple modelling groups.",

	(shared.DocumentTypes, 'Conformance'):
		"Used to hold information about how simulations and ensemble met experimental requirements",

	(shared.DocumentTypes, 'Dataset'):
		"An Atomic Dataset description, that is the minimal set of files with common publication characteristics.",

	(shared.DocumentTypes, 'DomainProperties'):
		"SpatioTemporal domain requirements for a numerical experiment.",

	(shared.DocumentTypes, 'Downscaling'):
		"Description of the techniques and software used to downscale data.",

	(shared.DocumentTypes, 'Ensemble'):
		"Parent  description for set of runs conforming to a numerical experiment.",

	(shared.DocumentTypes, 'EnsembleRequirement'):
		"Description of the ensemble requirements of a numerical experiment.",

	(shared.DocumentTypes, 'ExternalDocument'):
		"A document held outside of es-doc.",

	(shared.DocumentTypes, 'ForcingConstraint'):
		"A constraint on how a model must be forced to meet the requirements of a numerical experiment.",

	(shared.DocumentTypes, 'Grid'):
		"The sampling discretisation used by a model or dataset.",

	(shared.DocumentTypes, 'Machine'):
		"A computer used for numerical experimentation (and/or post-processing).",

	(shared.DocumentTypes, 'Model'):
		"A piece of software used to carry out simulations.",

	(shared.DocumentTypes, 'MultiEnsemble'):
		"An ensemble requirement describing multiple ensemble axes.",

	(shared.DocumentTypes, 'MultiTimeEnsemble'):
		"An ensemble requirement with multple time axes.",

	(shared.DocumentTypes, 'NumericalExperiment'):
		"The scientific description of a numerical experiment",

	(shared.DocumentTypes, 'NumericalRequirement'):
		"A numerical requirement of a numerical experiment.",

	(shared.DocumentTypes, 'OutputTemporalRequirement'):
		"The output requirements for one or more numerical experiments",

	(shared.DocumentTypes, 'Party'):
		"A person or organisation which has a role in the documentation of the simulation workflow",

	(shared.DocumentTypes, 'Performance'):
		"A formal set of criteria describing how a model performed on a given machine.",



	(shared.SlicetimeUnits, 'monthly'):
		None,

	(shared.SlicetimeUnits, 'yearly'):
		None,



	(shared.NilReason, 'nil:missing'):
		"The correct value is not available. Furthermore, a correct value may not exist",

	(shared.NilReason, 'nil:unknown'):
		"The correct value is not known at this time. However, a correct value probably exists",

	(shared.NilReason, 'nil:withheld'):
		"The value is not divulged",

	(shared.NilReason, 'nil:inapplicable'):
		"There is no value",

	(shared.NilReason, 'nil:template'):
		"The value will be available later",





	(activity.ForcingTypes, 'another simulation'):
		"From another simulation",

	(activity.ForcingTypes, 'scenario'):
		"Intended to represent a possible future, e.g. RCP4.5",

	(activity.ForcingTypes, 'historical'):
		"Best estimates of actual state (included synthesized)",

	(activity.ForcingTypes, 'idealised'):
		"Simplified and/or exemplar, e.g. 1%C02",



	(activity.EnsembleTypes, 'Perturbed Physics'):
		"Members differ in some aspects of their physics",

	(activity.EnsembleTypes, 'Initialisation Method'):
		"Members differ in how they are initialised",

	(activity.EnsembleTypes, 'Initialisation'):
		"Members are initialised to sample possible starting states",

	(activity.EnsembleTypes, 'Staggered Start'):
		"Members are initialised at different starting dates",

	(activity.EnsembleTypes, 'Forced'):
		"Members used differing forcing data",

	(activity.EnsembleTypes, 'Resolution'):
		"Members are run at different resolutions",





	(software.ProgrammingLanguage, 'C'):
		None,

	(software.ProgrammingLanguage, 'Python'):
		None,

	(software.ProgrammingLanguage, 'C++'):
		None,

	(software.ProgrammingLanguage, 'Fortran'):
		None,



	(software.CouplingFramework, 'OASIS'):
		None,

	(software.CouplingFramework, 'OASIS3-MCT'):
		None,

	(software.CouplingFramework, 'ESMF'):
		None,

	(software.CouplingFramework, 'NUOPC'):
		None,

	(software.CouplingFramework, 'Bespoke'):
		"Customised coupler developed for this model",

	(software.CouplingFramework, 'Unknown'):
		"It is not known what/if-a coupler is used",

	(software.CouplingFramework, 'None'):
		"No coupler is used",





	(science.ModelTypes, 'Atm Only'):
		"Atmosphere Only",

	(science.ModelTypes, 'Ocean Only'):
		"Ocean Only",

	(science.ModelTypes, 'Planetary'):
		"Non-Earth model",

	(science.ModelTypes, 'Regional'):
		"Regional Model",

	(science.ModelTypes, 'GCM'):
		"Global Climate Model (Atmosphere, Ocean, no carbon cycle)",

	(science.ModelTypes, 'IGCM'):
		"Intermediate Complexity GCM",

	(science.ModelTypes, 'GCM-MLO'):
		"GCM with mixed layer ocean",

	(science.ModelTypes, 'Mesoscale'):
		"Mesoscale Model",

	(science.ModelTypes, 'Process'):
		"Limited Area process model",



	(science.SelectionCardinality, '1.N'):
		"At least one, and possibly many, selections are required",

	(science.SelectionCardinality, '0.1'):
		"Zero or one selections are permitted",

	(science.SelectionCardinality, '0.N'):
		"Zero or many selections are permitted",

	(science.SelectionCardinality, '1.1'):
		"One and only one selection is required",





	(data.DataAssociationTypes, 'isComposedOf'):
		None,

	(data.DataAssociationTypes, 'partOf'):
		None,

	(data.DataAssociationTypes, 'revisonOf'):
		None,





	(drs.DrsFrequencyTypes, 'subhr'):
		"Sampling frequency less than an hour",

	(drs.DrsFrequencyTypes, 'monClim'):
		"Climatological Monthly Mean",

	(drs.DrsFrequencyTypes, 'fx'):
		"Fixed Time independent",

	(drs.DrsFrequencyTypes, 'yr'):
		"Yearly",

	(drs.DrsFrequencyTypes, 'mon'):
		"Monthly",

	(drs.DrsFrequencyTypes, 'day'):
		"Daily",

	(drs.DrsFrequencyTypes, '6hr'):
		"Every six hours",

	(drs.DrsFrequencyTypes, '3hr'):
		"Every three hours",



	(drs.DrsTimeSuffixes, 'avg'):
		"Indicates data is a single average of DRS frequency data across temporal period N1-N2",

	(drs.DrsTimeSuffixes, 'clim'):
		"Indicates data is climatological average data at the DRS frequency from the period N1-N2",



	(drs.DrsRealms, 'atmosChem'):
		"Atmospheric Chemistry",

	(drs.DrsRealms, 'ocnBgchem'):
		"Ocean Biogeochemistry",

	(drs.DrsRealms, 'atmos'):
		"Atmosphere",

	(drs.DrsRealms, 'ocean'):
		"Ocean",

	(drs.DrsRealms, 'land'):
		"Land",

	(drs.DrsRealms, 'landIce'):
		"Land Ice",

	(drs.DrsRealms, 'seaIce'):
		"Sea Ice",

	(drs.DrsRealms, 'aerosol'):
		"Aerosol",



	(drs.DrsGeographicalOperators, 'lnd-zonalavg'):
		"Data is zonally averaged over land in region",

	(drs.DrsGeographicalOperators, 'ocn-zonalavg'):
		"Data is zonally averaged over oceans in region",

	(drs.DrsGeographicalOperators, 'areaavg'):
		"Data is averaged over the area of the region",

	(drs.DrsGeographicalOperators, 'lnd-areaavg'):
		"Data is averaged over the land area of the region",

	(drs.DrsGeographicalOperators, 'ocn-areaavg'):
		"Data is averaged over the ocean area of the region",

	(drs.DrsGeographicalOperators, 'zonalavg'):
		"Data is zonally averaged",





	(platform.StorageSystems, 'Other Disk'):
		None,

	(platform.StorageSystems, 'Tape - MARS'):
		None,

	(platform.StorageSystems, 'Tape - Other'):
		None,

	(platform.StorageSystems, 'Tape - MASS'):
		None,

	(platform.StorageSystems, 'Tape - Castor'):
		None,

	(platform.StorageSystems, 'Lustre'):
		None,

	(platform.StorageSystems, 'GPFS'):
		None,

	(platform.StorageSystems, 'Unknown'):
		None,

	(platform.StorageSystems, 'NFS'):
		None,

	(platform.StorageSystems, 'Panasas'):
		None,

	(platform.StorageSystems, 'isilon'):
		None,



	(platform.VolumeUnits, 'PiB'):
		"Pebibytes (1024^5)",

	(platform.VolumeUnits, 'EiB'):
		"Exbibytes (1024^6)",

	(platform.VolumeUnits, 'GB'):
		"Gigabytes (1000^3)",

	(platform.VolumeUnits, 'TB'):
		"Terabytes (1000^4)",

	(platform.VolumeUnits, 'PB'):
		"Petabytes (1000^5)",

	(platform.VolumeUnits, 'EB'):
		"Exabytes (1000^6)",

	(platform.VolumeUnits, 'TiB'):
		"Tebibytes (1024^4)",



}
