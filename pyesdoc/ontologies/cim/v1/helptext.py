
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.helptext.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The ontology help text.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import typeset_for_shared_package as shared
import typeset_for_software_package as software
import typeset_for_grids_package as grids
import typeset_for_quality_package as quality
import typeset_for_data_package as data
import typeset_for_activity_package as activity
import typeset_for_misc_package as misc



HELP = {
	# ------------------------------------------------
	# Packages.
	# ------------------------------------------------

	shared: """
        Shared types that might be imported from other packages within the ontology.

        """,

	software: """
        Types that describe the climate models software.

        """,

	grids: """
        Types that describe the grids that climate models plot.

        """,

	quality: """
        Types that describe the quailty of output that climate models emit.

        """,

	data: """
        Types that describe output that climate models emit.

        """,

	activity: """
        Types that describe context against which climate models are run.

        """,

	misc: """
        Miscellaneous types.

        """,

	# ------------------------------------------------
	# Classes.
	# ------------------------------------------------


	shared.DocReference: """
		A reference to another cim entity.

	""",

	shared.Compiler: """
		A description of a compiler used on a particular platform.

	""",

	shared.DateRange: """
		Creates and returns instance of date_range class.

	""",

	shared.Change: """
		A description of [a set of] changes applied at a particular time, by a particular party, to a particular unit of metadata.

	""",

	shared.Standard: """
		Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

	""",

	shared.DocRelationship: """
		Contains the set of relationships supported by a Document.

	""",

	shared.Citation: """
		An academic reference to published work.

	""",

	shared.RealCalendar: """
		Creates and returns instance of real_calendar class.

	""",

	shared.DocRelationshipTarget: """
		Creates and returns instance of doc_relationship_target class.

	""",

	shared.Property: """
		A simple name/value pair representing a property of some entity or other.

	""",

	shared.License: """
		A description of a license restricting access to a unit of data or software.

	""",

	shared.Machine: """
		A description of a machine used by a particular platform.

	""",

	shared.DataSource: """
		A DataSource can be realised by either a DataObject (file), a DataContent (variable), a Component (model), or a ComponentProperty (variable); all of those can supply data.

	""",

	shared.DocGenealogy: """
		A record of a document's history. A genealogy element contains a textual description and a set of relationships. Each relationship has a type and a reference to some target. There are different relationships for different document types.

	""",

	shared.MachineCompilerUnit: """
		Associates a machine with a [set of] compilers.  This is a separate class in case a platform needs to specify more than one machine/compiler pair.

	""",

	shared.Relationship: """
		A record of a relationship between one document and another. This class is abstract; specific document types must specialise this class for their relationshipTypes to be included in a document's genealogy.

	""",

	shared.Calendar: """
		Describes a method of calculating a span of dates.

	""",

	shared.PerpetualPeriod: """
		Creates and returns instance of perpetual_period class.

	""",

	shared.Platform: """
		A platform is a description of resources used to deploy a component/simulation.  A platform pairs a machine with a (set of) compilers.  There is also a point of contact for the platform.

	""",

	shared.ClosedDateRange: """
		A date range with specified start and end points.

	""",

	shared.ResponsibleParty: """
		A person/organsiation responsible for some aspect of a climate science artefact.

	""",

	shared.StandardName: """
		Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

	""",

	shared.DocMetaInfo: """
		Encapsulates document meta information.

	""",

	shared.ChangeProperty: """
		A description of a single change applied to a single target.  Every ChangeProperty has a description, and may also have a name from a controlled vocabulary and a value.

	""",

	shared.Daily360: """
		Creates and returns instance of daily_360 class.

	""",

	shared.OpenDateRange: """
		A date range without a specified start and/or end point.

	""",



	software.Rank: """
		Creates and returns instance of rank class.

	""",

	software.Timing: """
		Provides information about the rate of couplings and connections and/or the timing characteristics of individual components - for example, the start and stop times that the component was run for or the units of time that a component is able to model (in a single timestep).

	""",

	software.Parallelisation: """
		Describes how a deployment has been parallelised across a computing platform.

	""",

	software.EntryPoint: """
		Describes a function or subroutine of a SoftwareComponent. BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model. Currently, a very basic schedule can be approximated by using the 'proceeds' and 'follows' attributes, however a more complete system is required for full BFG compatibility. Every EntryPoint can have a set of arguments associated with it. These reference (previously defined) ComponentProperties.

	""",

	software.ConnectionProperty: """
		A ConnectionProperty is a name/value pair used to specify OASIS-specific properties.

	""",

	software.Coupling: """
		A coupling represents a set of Connections between a source and target component. Couplings can be complete or incomplete. If they are complete then they must include all Connections between model properties. If they are incomplete then the connections can be underspecified or not listed at all.

	""",

	software.ProcessorComponent: """
		A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.

	""",

	software.ComponentLanguage: """
		Details of the programming language a component is written in. There is an assumption that all EntryPoints use the same ComponentLanguage.

	""",

	software.Composition: """
		The set of Couplings used by a Component. Couplings can only occur between child components. That is, a composition must belong to an ancestor component of the components whose fields are being connected.

	""",

	software.SpatialRegriddingUserMethod: """
		Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.

	""",

	software.ComponentLanguageProperty: """
		This provides a place to include language-specific information. Every property is basically a name/value pair, where the names are things like: moduleName, reservedUnits, reservedNames (these are all examples of Fortran-specific properties).

	""",

	software.SpatialRegriddingProperty: """
		Used for OASIS-specific regridding information (ie: masked, order, normalisation, etc.)

	""",

	software.ComponentProperty: """
		ComponentProperties include things that a component simulates (ie: pressure, humidity) and things that prescribe that simulation (ie: gravity, choice of advection scheme). Note that this is a specialisation of shared::DataSource. data::DataObject is also a specialisation of shared::DataSource. This allows software::Connections and/or activity::Conformance to refer to either ComponentProperties or DataObjects.

	""",

	software.StatisticalModelComponent: """
		Creates and returns instance of statistical_model_component class.

	""",

	software.TimeTransformation: """
		The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.

	""",

	software.CouplingEndpoint: """
		The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).

	""",

	software.Deployment: """
		Gives information about the technical properties of a component: what machine it was run on, which compilers were used, how it was parallised, etc. A deployment basically associates a deploymentDate with a Platform. A deployment only exists if something has been deployed. A platform, in contrast, can exist independently, waiting to be used in deployments.

	""",

	software.Component: """
		A SofwareComponent is an abstract component from which all other components derive. It represents an element that takes input data and generates output data. A SoftwareCompnent can include nested 'child' components. Every component can have 'componentProperties' which describe the scientific properties that a component simulates (for example, temperature, pressure, etc.) and the numerical properties that influence how a component performs its simulation (for example, the force of gravity). A SoftwareComponent can also have a Deployment, which describes how software is deployed onto computing resources. And a SoftwareComponent can have a composition, which describes how ComponentProperties are coupled together either to/from other SoftwareComponents or external data files. The properties specified by a component's composition must be owned by that component or a child of that component; child components cannot couple together their parents' properties.

	""",

	software.ModelComponent: """
		A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.

	""",

	software.TimeLag: """
		The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.

	""",

	software.CouplingProperty: """
		A CouplingProperty is a name/value pair used to specify OASIS-specific properties.

	""",

	software.Connection: """
		A Connection represents a link from a source DataSource to a target DataSource.  These can either be ComponentProperties (ie: the values come from an internal component) or DataObjects (ie: the values come from an external file).   It can be associated with another software component (a transformer).  If present, the rate, lag, timeTransformation, and spatialRegridding override that of the parent coupling.  Note that there is the potential for multiple connectionSource & connectionTarget and multiple couplingSources & couplingTargets.  This may lead users to wonder how to match up a connection source (a ComponentProperty) with its coupling source (a SoftwareComponent). Clever logic is not required though; because the sources and targets are listed by reference, they can be found in a CIM document and the parent can be navigated to from there - there is no need to consult the source or target of the coupling.

	""",

	software.ConnectionEndpoint: """
		The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).

	""",

	software.SpatialRegridding: """
		Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.

	""",



	grids.GridTileResolutionType: """
		Provides a description and set of named properties for the horizontal or vertical resolution.

	""",

	grids.GridMosaic: """
		The GridMosaic class is used to define the geometry properties of an earth system model grid or an exchange grid. Such a grid definition may then be referenced by any number of earth system models. A GridMosaic object consists either of 1 or more child GridMosaics, or one or more child GridTiles, but not both. In the latter case the isLeaf property should be set to true, indicating that the mosaic is a leaf mosaic.

	""",

	grids.VerticalCoordinateList: """
		There are some specific attributes that are associated with vertical coordinates.

	""",

	grids.GridSpec: """
		This is a container class for GridSpec objects. A GridSpec object can contain one or more esmModelGrid objects, and one or more esmExchangeGrid objects. These objects may be serialised to one or possibly several files according to taste. Since GridSpec is sub-typed from GML's AbstractGeometryType it can, and should, be identified using a gml:id attribute.

	""",

	grids.GridExtent: """
		DataType for recording the geographic extent of a gridMosaic or gridTile.

	""",

	grids.CoordinateList: """
		The CoordList type may be used to specify a list of coordinates, typically for the purpose of defining coordinates along the X, Y or Z axes. The length of the coordinate list is given by the attribute of that name. This may be used by software to allocate memory in advance of storing the coordinate values. The hasConstantOffset attribute may be used to indicate that the coordinate list consists of values with constant offset (spacing). In this case only the first coordinate value and the offset (spacing) value need to be specified; however, the length attribute must still define the final as-built size of the coordinate list.

	""",

	grids.GridTile: """
		The GridTile class is used to model an individual grid tile contained within a grid mosaic. A GridTile consists of an array of grid cells which may be defined in one of four ways: 1) for simple grids, by use of the SimpleGridGeometry data type; 2) by defining an array of GridCell objects; 3) by specifying an array of references to externally defined GridCell objects; or 4) by specifying a URI to a remote data file containing the grid cell definitions.  For all but the simplest grid tiles, it is envisaged that method 4 above will be the most frequently used option. However, it should be remembered that the CIM is primarily concerned with encoding climate model metadata. Specifying the coordinates of individual grid tiles and cells will most likely not be required as part of such metadata descriptions.  A GridTile object is associated with a geodetic or projected CRS via the horizontalCRS property, and with a vertical CRS via the verticalCRS property.

	""",

	grids.GridProperty: """
		Creates and returns instance of grid_property class.

	""",

	grids.SimpleGridGeometry: """
		SimpleGridGeometry:This property may be used to define the coordinates of the nodes or cells making up a simple (i.e. uniform or regular) grid tile. More details are provided in the description of the SimpleGridGeometry data type.

	""",



	quality.CimQuality: """
		The starting point for a quality record.  It can contain any number of issues and reports.  An issue is an open-ended description of some issue about a CIM instance.  A record is a prescribed description of some specific quantitative measure that has been applied to a CIM instance.

	""",

	quality.Report: """
		Creates and returns instance of report class.

	""",

	quality.Evaluation: """
		Creates and returns instance of evaluation class.

	""",

	quality.Measure: """
		Creates and returns instance of measure class.

	""",



	data.DataTopic: """
		Describes the content of a data object: the variable name, units, etc.

	""",

	data.DataExtent: """
		A data object extent represents the geographical and temporal coverage associated with a data object.

	""",

	data.DataObject: """
		A DataObject describes a unit of data.  DataObjects can be grouped hierarchically.  The attributes hierarchyLevelName and hierarchyLevelValue describe how objects are grouped.

	""",

	data.DataHierarchyLevel: """
		The type of data object that is grouped together into a particular hierarchy.  Currently, this is made up of terms describing how the Met Office splits up archived data and how THREDDS categorises variables.

	""",

	data.DataStorage: """
		Describes the method that the DataObject is stored. An abstract class with specific child classes for each supported method.

	""",

	data.DataExtentGeographical: """
		A data object geographical extent represents the geographical coverage associated with a data object.

	""",

	data.DataProperty: """
		A property of a DataObject. Currently this is intended to be used to record CF specific information (like packing, scaling, etc.) for OASIS4.

	""",

	data.DataStorageFile: """
		Contains attributes to describe a DataObject stored as a single file.

	""",

	data.DataContent: """
		The contents of the data object; like ISO: MD_ContentInformation.

	""",

	data.DataDistribution: """
		Describes how a DataObject is distributed.

	""",

	data.DataRestriction: """
		An access or use restriction on some element of the DataObject actual data.

	""",

	data.DataExtentTimeInterval: """
		A data object temporal extent represents the temporal coverage associated with a data object.

	""",

	data.DataStorageIp: """
		Contains attributes to describe a DataObject stored as a database file.

	""",

	data.DataExtentTemporal: """
		A data object temporal extent represents the temporal coverage associated with a data object.

	""",

	data.DataStorageDb: """
		Contains attributes to describe a DataObject stored as a database file.

	""",



	activity.Experiment: """
		An experiment might be an activity which is both observational and numerical in focus, for example, a measurement campaign and numerical experiments for an alpine experiment.  It is a place for the scientific description of the reason why an experiment was made.

	""",

	activity.SimulationRelationship: """
		Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

	""",

	activity.EnsembleMember: """
		A simulation is the implementation of a numerical experiment.  A simulation can be made up of 'child' simulations aggregated together to form a 'simulation composite'.  The 'parent' simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

	""",

	activity.NumericalRequirement: """
		A description of the requirements of particular experiments.  Numerical Requirements can be initial conditions, boundary conditions, or physical modificiations.

	""",

	activity.LateralBoundaryCondition: """
		A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).

	""",

	activity.DownscalingSimulation: """
		A simulation is the implementation of a numerical experiment.  A simulation can be made up of 'child' simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

	""",

	activity.NumericalActivity: """
		Creates and returns instance of numerical_activity class.

	""",

	activity.Simulation: """
		A simulation is the implementation of a numerical experiment.  A simulation can be made up of 'child' simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

	""",

	activity.ExperimentRelationship: """
		Contains a set of relationship types specific to a experiment document that can be used to describe its genealogy.

	""",

	activity.ExperimentRelationshipTarget: """
		Creates and returns instance of experiment_relationship_target class.

	""",

	activity.NumericalRequirementOption: """
		A NumericalRequirement that is being used as a set of related requirements; For example if a requirement is to use 1 of 3 boundary conditions, then that 'parent' requirement would have three 'child' RequirmentOptions (each of one with the XOR optionRelationship).

	""",

	activity.Activity: """
		An abstract class used as the parent of MeasurementCampaigns, Projects, Experiments, and NumericalActivities.

	""",

	activity.MeasurementCampaign: """
		Creates and returns instance of measurement_campaign class.

	""",

	activity.SimulationRelationshipTarget: """
		Creates and returns instance of simulation_relationship_target class.

	""",

	activity.SimulationRun: """
		A SimulationRun is, as the name implies, one single model run. A SimulationRun is a Simulation. There is a one to one association between SimulationRun and (a top-level) SoftwarePackage::ModelComponent.

	""",

	activity.OutputRequirement: """
		Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

	""",

	activity.Conformance: """
		A conformance class maps how a configured model component met a specific numerical requirement.  For example, for a double CO2 boundary condition, a model component might read a CO2 dataset in which CO2 has been doubled, or it might modify a parameterisation (presumably with a factor of two somewhere).  So, the conformance links a requirement to a DataSource (which can be either an actual DataObject or a property of a model component).  In some cases a model/simulation may _naturally_ conform to a requirement.  In this case there would be no reference to a DataSource but the conformant attribute would be true.  If something is purpopsefully non-conformant then the conformant attribute would be false.

	""",

	activity.BoundaryCondition: """
		A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).

	""",

	activity.Ensemble: """
		An ensemble is made up of two or more simulations which are to be compared against each other to create ensemble statistics. Ensemble members can differ in terms of initial conditions, physical parameterisation and the model used. An ensemble bundles together sets of ensembleMembers, all of which reference the same Simulation(Run) and include one or more changes.

	""",

	activity.PhysicalModification: """
		Physical modification is the implementation of a boundary condition numerical requirement that is achieved within the model code rather than from some external source file. It  might include, for example,  a specific rate constant within a chemical reaction, or coefficient value(s) in a parameterisation.  For example, one might require a numerical experiment where specific chemical reactions were turned off - e.g. no heterogeneous chemistry.

	""",

	activity.SimulationComposite: """
		A SimulationComposite is an aggregation of Simulations. With the aggreation connector between Simulation and SimulationComposite(SC) the SC can be made up of both SimulationRuns and SCs. The SimulationComposite is the new name for the concept of SimulationCollection: A simulation can be made up of 'child' simulations aggregated together to form a 'simulation composite'.  The 'parent' simulation can be made up of whole or partial child simulations and the SimulationComposite attributes need to be able to capture this.

	""",

	activity.InitialCondition: """
		An initial condition is a numerical requirement on a model prognostic variable value at time zero.

	""",

	activity.NumericalExperiment: """
		A numerical experiment may be generated by an experiment, in which case it is inSupportOf the experiment. But a numerical experiment may also exist as an activity in its own right (as it might be if it were needed for a MIP). Examples: AR4 individual experiments, AR5 individual experiments, RAPID THC experiments etc.

	""",

	activity.SpatioTemporalConstraint: """
		Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

	""",



	misc.DocumentSet: """
		Represents a bundled set of documents.

	""",


	# ------------------------------------------------
	# Class properties.
	# ------------------------------------------------



	(shared.DocReference, 'version'):
		"The version of the element being referenced.",

	(shared.DocReference, 'name'):
		"The name of the element being referenced.",

	(shared.DocReference, 'type'):
		"The type of the element being referenced.",

	(shared.DocReference, 'description'):
		"A description of the element being referenced, in the context of the current class.",

	(shared.DocReference, 'url'):
		"A URL associated witht he document reference.",

	(shared.DocReference, 'external_id'):
		"A non-CIM (non-GUID) id used to reference the element in question.",

	(shared.DocReference, 'id'):
		"The ID of the element being referenced.",

	(shared.DocReference, 'changes'):
		"An optional description of how the item being referenced has been modified.  This is particularly useful for dealing with Ensembles (a set of simulations where something about each simulation has changed) or Conformances.",



	(shared.Compiler, 'language'):
		None,

	(shared.Compiler, 'version'):
		None,

	(shared.Compiler, 'name'):
		None,

	(shared.Compiler, 'options'):
		"The set of options used during compilation (recorded here as a single string rather than separate elements)",

	(shared.Compiler, 'type'):
		None,

	(shared.Compiler, 'environment_variables'):
		"The set of environment_variables used during compilation (recorded here as a single string rather than separate elements)",



	(shared.DateRange, 'duration'):
		None,



	(shared.Change, 'details'):
		None,

	(shared.Change, 'name'):
		"A mnemonic for describing a particular change.",

	(shared.Change, 'author'):
		"The person that made the change.",

	(shared.Change, 'type'):
		None,

	(shared.Change, 'description'):
		None,

	(shared.Change, 'date'):
		"The date the change was implemented.",



	(shared.Standard, 'description'):
		"The version of the standard",

	(shared.Standard, 'version'):
		"The version of the standard",

	(shared.Standard, 'name'):
		"The name of the standard",



	(shared.DocRelationship, 'target'):
		None,

	(shared.DocRelationship, 'type'):
		None,



	(shared.Citation, 'type'):
		None,

	(shared.Citation, 'collective_title'):
		None,

	(shared.Citation, 'organisation'):
		None,

	(shared.Citation, 'location'):
		None,

	(shared.Citation, 'alternative_title'):
		None,

	(shared.Citation, 'role'):
		None,

	(shared.Citation, 'date'):
		None,

	(shared.Citation, 'title'):
		None,

	(shared.Citation, 'date_type'):
		None,





	(shared.DocRelationshipTarget, 'reference'):
		None,



	(shared.Property, 'name'):
		None,

	(shared.Property, 'value'):
		None,



	(shared.License, 'name'):
		"The name that the license goes by (ie: 'GPL')",

	(shared.License, 'contact'):
		"The point of contact for access to this artifact; may be either a person or an institution.",

	(shared.License, 'is_unrestricted'):
		"If unrestricted='true' then the artifact can be downloaded with no restrictions (ie: there are no administrative steps for the user to deal with; code or data can be downloaded and used directly).",

	(shared.License, 'description'):
		"A textual description of the license; might be the full text of the license, more likely to be a brief summary",



	(shared.Machine, 'system'):
		None,

	(shared.Machine, 'location'):
		None,

	(shared.Machine, 'interconnect'):
		None,

	(shared.Machine, 'type'):
		None,

	(shared.Machine, 'maximum_processors'):
		None,

	(shared.Machine, 'cores_per_processor'):
		None,

	(shared.Machine, 'vendor'):
		None,

	(shared.Machine, 'name'):
		None,

	(shared.Machine, 'operating_system'):
		None,

	(shared.Machine, 'processor_type'):
		None,

	(shared.Machine, 'libraries'):
		"The libraries residing on this machine.",

	(shared.Machine, 'description'):
		None,



	(shared.DataSource, 'purpose'):
		None,



	(shared.DocGenealogy, 'relationships'):
		None,



	(shared.MachineCompilerUnit, 'compilers'):
		None,

	(shared.MachineCompilerUnit, 'machine'):
		None,



	(shared.Relationship, 'description'):
		None,

	(shared.Relationship, 'direction'):
		None,



	(shared.Calendar, 'description'):
		"Describes the finer details of the calendar, in case they are not-obvious.  For example, if an experiment has changing conditions within it (ie: 1% CO2 increase until 2100, then hold fixed for the remaining period of the  experment)",

	(shared.Calendar, 'range'):
		None,

	(shared.Calendar, 'length'):
		None,





	(shared.Platform, 'meta'):
		None,

	(shared.Platform, 'short_name'):
		None,

	(shared.Platform, 'contacts'):
		None,

	(shared.Platform, 'description'):
		None,

	(shared.Platform, 'units'):
		None,

	(shared.Platform, 'long_name'):
		None,



	(shared.ClosedDateRange, 'end'):
		"End date is optional becuase the length of a ClosedDateRange can be calculated from the StartDate plus the Duration element.",

	(shared.ClosedDateRange, 'start'):
		None,



	(shared.ResponsibleParty, 'individual_name'):
		None,

	(shared.ResponsibleParty, 'abbreviation'):
		None,

	(shared.ResponsibleParty, 'organisation_name'):
		None,

	(shared.ResponsibleParty, 'address'):
		None,

	(shared.ResponsibleParty, 'role'):
		None,

	(shared.ResponsibleParty, 'email'):
		None,

	(shared.ResponsibleParty, 'url'):
		None,



	(shared.StandardName, 'is_open'):
		None,

	(shared.StandardName, 'value'):
		None,

	(shared.StandardName, 'standards'):
		"Details of the standard being used.",



	(shared.DocMetaInfo, 'version'):
		"Document version identifier.",

	(shared.DocMetaInfo, 'id'):
		"Universal document identifier.",

	(shared.DocMetaInfo, 'project'):
		"Name of project with which instance is associated with.",

	(shared.DocMetaInfo, 'update_date'):
		"Date upon which the instance was last updated",

	(shared.DocMetaInfo, 'language'):
		"Language with which instance is associated with.",

	(shared.DocMetaInfo, 'status'):
		"Document status.",

	(shared.DocMetaInfo, 'drs_keys'):
		"DRS related keys to support correlation of documents with datasets.",

	(shared.DocMetaInfo, 'type_sort_key'):
		"Document type sort key.",

	(shared.DocMetaInfo, 'author'):
		"Associated document author.",

	(shared.DocMetaInfo, 'source'):
		"Application that created the instance.",

	(shared.DocMetaInfo, 'type_display_name'):
		"Document type display name.",

	(shared.DocMetaInfo, 'external_ids'):
		"Set of identifiers used to reference the document by external parties.",

	(shared.DocMetaInfo, 'create_date'):
		"Date upon which the instance was created",

	(shared.DocMetaInfo, 'institute'):
		"Name of institute with which instance is associated with.",

	(shared.DocMetaInfo, 'source_key'):
		"Key of application that created the instance.",

	(shared.DocMetaInfo, 'genealogy'):
		"Specifies the relationship of this document with another document. Various relationship types (depending on the type of document; ie: simulation, component, etc.) are supported.",

	(shared.DocMetaInfo, 'drs_path'):
		"DRS related path to support documents with datasets.",

	(shared.DocMetaInfo, 'sort_key'):
		"Document sort key.",

	(shared.DocMetaInfo, 'type'):
		"Document ontology type.",



	(shared.ChangeProperty, 'description'):
		"A text description of the change.  May be used in addition to, or instead of, the more formal description provided by the 'value' attribute.",

	(shared.ChangeProperty, 'id'):
		None,





	(shared.OpenDateRange, 'end'):
		None,

	(shared.OpenDateRange, 'start'):
		None,





	(software.Rank, 'value'):
		None,

	(software.Rank, 'increment'):
		None,

	(software.Rank, 'min'):
		None,

	(software.Rank, 'max'):
		None,



	(software.Timing, 'start'):
		None,

	(software.Timing, 'end'):
		None,

	(software.Timing, 'units'):
		None,

	(software.Timing, 'rate'):
		None,

	(software.Timing, 'is_variable_rate'):
		"Describes whether or not the model supports a variable timestep. If set to true, then rate should not be specified.",



	(software.Parallelisation, 'processes'):
		None,

	(software.Parallelisation, 'ranks'):
		None,



	(software.EntryPoint, 'name'):
		None,





	(software.Coupling, 'priming'):
		"A priming source is one that is active on the first available timestep only (before 'proper' coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created.",

	(software.Coupling, 'time_lag'):
		"The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time.",

	(software.Coupling, 'sources'):
		"The source component of the coupling. (note that there can be multiple sources).",

	(software.Coupling, 'spatial_regriddings'):
		"Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).",

	(software.Coupling, 'is_fully_specified'):
		"If true then the coupling is fully-specified.  If false then not every Connection has been described within the coupling.",

	(software.Coupling, 'connections'):
		None,

	(software.Coupling, 'transformers'):
		"An 'in-line' transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here.",

	(software.Coupling, 'properties'):
		None,

	(software.Coupling, 'type'):
		"Describes the method of coupling.",

	(software.Coupling, 'target'):
		"The target component of the coupling.",

	(software.Coupling, 'time_profile'):
		"Describes how often the coupling takes place.",

	(software.Coupling, 'description'):
		"A free-text description of the coupling.",

	(software.Coupling, 'purpose'):
		None,

	(software.Coupling, 'time_transformation'):
		"Temporal transformation performed on the coupling field before or after regridding onto the target grid.",



	(software.ProcessorComponent, 'meta'):
		None,



	(software.ComponentLanguage, 'name'):
		"The name of the language.",

	(software.ComponentLanguage, 'properties'):
		None,



	(software.Composition, 'couplings'):
		None,

	(software.Composition, 'description'):
		None,



	(software.SpatialRegriddingUserMethod, 'file'):
		None,

	(software.SpatialRegriddingUserMethod, 'name'):
		None,







	(software.ComponentProperty, 'short_name'):
		None,

	(software.ComponentProperty, 'grid'):
		"A reference to the grid that is used by this component.",

	(software.ComponentProperty, 'is_represented'):
		"When set to false, means that this property is not used by the component. Covers the case when, for instance, a modeler chooses not to represent some property in their model. (But still allows meaningful comparisons between components which _do_ model this property.)",

	(software.ComponentProperty, 'intent'):
		"The direction that this property is intended to be coupled: in, out, or inout.",

	(software.ComponentProperty, 'values'):
		"The value of the property (not applicable to fields).",

	(software.ComponentProperty, 'sub_properties'):
		None,

	(software.ComponentProperty, 'standard_names'):
		None,

	(software.ComponentProperty, 'citations'):
		None,

	(software.ComponentProperty, 'description'):
		None,

	(software.ComponentProperty, 'long_name'):
		None,

	(software.ComponentProperty, 'units'):
		"The standard name that this property is known as (for example, its CF name).",



	(software.StatisticalModelComponent, 'type'):
		"Describes the type of component. There can be multiple types.",

	(software.StatisticalModelComponent, 'types'):
		"Describes the type of component. There can be multiple types.",

	(software.StatisticalModelComponent, 'meta'):
		None,

	(software.StatisticalModelComponent, 'timing'):
		"Describes information about how this component simulates time.",



	(software.TimeTransformation, 'description'):
		None,

	(software.TimeTransformation, 'mapping_type'):
		None,



	(software.CouplingEndpoint, 'data_source'):
		None,

	(software.CouplingEndpoint, 'properties'):
		"A place to describe features specific to the source/target of a coupling",

	(software.CouplingEndpoint, 'instance_id'):
		"If the same datasource is used more than once in a coupled model then a method for identifying which particular instance is being referenced is needed (for BFG).",



	(software.Deployment, 'parallelisation'):
		None,

	(software.Deployment, 'executable_name'):
		None,

	(software.Deployment, 'platform'):
		"The platform that this deployment has been run on. It is optional to allow for 'unconfigured' models, that nonetheless specify their parallelisation constraints (a feature needed by OASIS).",

	(software.Deployment, 'deployment_date'):
		None,

	(software.Deployment, 'description'):
		None,

	(software.Deployment, 'executable_arguments'):
		None,



	(software.Component, 'dependencies'):
		None,

	(software.Component, 'version'):
		"A free text description of the component version #.",

	(software.Component, 'deployments'):
		None,

	(software.Component, 'description'):
		"A free-text description of the component.",

	(software.Component, 'funding_sources'):
		"The entities that funded this software component.",

	(software.Component, 'grid'):
		"A reference to the grid that is used by this component.",

	(software.Component, 'is_embedded'):
		"An embedded component cannot exist on its own as an atomic piece of software; instead it is embedded within another (parent) component. When embedded equals 'true', the SoftwareComponent has a corresponding piece of software (otherwise it is acting as a 'virtual' component which may be inexorably nested within a piece of software along with several other virtual components).",

	(software.Component, 'language'):
		None,

	(software.Component, 'license'):
		"The license held by this piece of software.",

	(software.Component, 'long_name'):
		"The name of the model (that is recognized externally).",

	(software.Component, 'online_resource'):
		"Provides a URL location for this model.",

	(software.Component, 'parent'):
		None,

	(software.Component, 'sub_components'):
		None,

	(software.Component, 'previous_version'):
		None,

	(software.Component, 'citations'):
		None,

	(software.Component, 'properties'):
		"The properties that this model simulates and/or couples.",

	(software.Component, 'code_access'):
		"Instructions on how to access the source code for this component.",

	(software.Component, 'release_date'):
		"The date of publication of the software component code (as opposed to the date of publication of the metadata document, or the date of deployment of the model)",

	(software.Component, 'composition'):
		None,

	(software.Component, 'responsible_parties'):
		None,

	(software.Component, 'coupling_framework'):
		"The coupling framework that this entire component conforms to.",

	(software.Component, 'short_name'):
		"The name of the model (that is used internally).",



	(software.ModelComponent, 'meta'):
		None,

	(software.ModelComponent, 'type'):
		"Describes the type of component. There can be multiple types.",

	(software.ModelComponent, 'types'):
		"Describes the type of component. There can be multiple types.",

	(software.ModelComponent, 'activity'):
		None,

	(software.ModelComponent, 'timing'):
		"Describes information about how this component simulates time.",



	(software.TimeLag, 'units'):
		None,

	(software.TimeLag, 'value'):
		None,





	(software.Connection, 'time_lag'):
		"The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time.",

	(software.Connection, 'time_transformation'):
		"Temporal transformation performed on the coupling field before or after regridding onto the target grid.",

	(software.Connection, 'type'):
		"The type of Connection",

	(software.Connection, 'description'):
		None,

	(software.Connection, 'properties'):
		None,

	(software.Connection, 'priming'):
		"A priming source is one that is active on the first available timestep only (before 'proper' coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created.",

	(software.Connection, 'time_profile'):
		"All information having to do with the rate of this connection; the times that it is active.  This overrides any rate of a Coupling.",

	(software.Connection, 'transformers'):
		"An 'in-line' transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here.",

	(software.Connection, 'spatial_regridding'):
		"Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid)",

	(software.Connection, 'target'):
		"The target property being connected.  This is optional to support the way that input is handled in the CMIP5 questionnaire.",

	(software.Connection, 'sources'):
		"The source property being connected.  (note that there can be multiple sources)  This is optional; the file/component source may have already been specified by the couplingSource.",



	(software.ConnectionEndpoint, 'data_source'):
		None,

	(software.ConnectionEndpoint, 'properties'):
		"The place to describe features specific to the source/target of a connection.",

	(software.ConnectionEndpoint, 'instance_id'):
		"If the same datasource is used more than once in a coupled model then a method for identifying which particular instance is being referenced is needed (for BFG).",



	(software.SpatialRegridding, 'user_method'):
		None,

	(software.SpatialRegridding, 'dimension'):
		None,

	(software.SpatialRegridding, 'standard_method'):
		None,

	(software.SpatialRegridding, 'properties'):
		None,





	(grids.GridTileResolutionType, 'description'):
		"A description of the resolution.",

	(grids.GridTileResolutionType, 'properties'):
		None,



	(grids.GridMosaic, 'mosaic_count'):
		"Specifies the number of mosaics associated with a non-leaf grid mosaic. Set to zero if the grid mosaic is a leaf mosaic, i.e. it contains child grid tiles not mosaics.",

	(grids.GridMosaic, 'citations'):
		"Optional container element for specifying a list of references that describe the grid.",

	(grids.GridMosaic, 'id'):
		"Specifies a globally unique identifier for a grid mosaic instance. By globally we mean across all GridSpec instances/records within a given modelling activity (such as CMIP5).",

	(grids.GridMosaic, 'type'):
		"Specifies the type of all the grid tiles contained in a grid mosaic. It is assumed that all of the tiles comprising a given grid mosaic are of the same type. The value domain is as per the specified enumeration list.",

	(grids.GridMosaic, 'is_leaf'):
		"Indicates whether or not a grid mosaic is a leaf mosaic, that is, it only contains child grid tiles not further mosaics.",

	(grids.GridMosaic, 'short_name'):
		"Specifies the short name associated with a grid mosaic. The short name will typically be a convenient abbreviation used to refer to a grid mosaic, e.g. 'UM ATM N96'.",

	(grids.GridMosaic, 'mnemonic'):
		None,

	(grids.GridMosaic, 'mosaics'):
		None,

	(grids.GridMosaic, 'extent'):
		None,

	(grids.GridMosaic, 'description'):
		"A free-text description of a grid mosaic.",

	(grids.GridMosaic, 'tiles'):
		None,

	(grids.GridMosaic, 'has_congruent_tiles'):
		"Indicates whether or not all the tiles contained within a grid mosaic are congruent, that is, of the same size and shape.",

	(grids.GridMosaic, 'tile_count'):
		"Specifies the number of tiles associated with a leaf grid mosaic. Set to zero if the grid mosaic is not a leaf mosaic, i.e. it contains child grid mosaics rather than tiles. (Added to align with equivalent ESG/Curator property.)",

	(grids.GridMosaic, 'long_name'):
		"Specifies the long name associated with a grid mosaic. The long name will typically be a human-readable string, with acronyms expanded, used for labelling purposes.",



	(grids.VerticalCoordinateList, 'form'):
		"Units of measure used by the coordinates.",

	(grids.VerticalCoordinateList, 'type'):
		"Specifies the length of the coordinate array. This should always be the final, as-built length of the array if the hasConstantOffset property is set to true and the compact notation (start coordinate plus offset) is used.",

	(grids.VerticalCoordinateList, 'properties'):
		None,



	(grids.GridSpec, 'esm_exchange_grids'):
		None,

	(grids.GridSpec, 'meta'):
		None,

	(grids.GridSpec, 'esm_model_grids'):
		None,



	(grids.GridExtent, 'maximum_latitude'):
		None,

	(grids.GridExtent, 'minimum_longitude'):
		None,

	(grids.GridExtent, 'minimum_latitude'):
		None,

	(grids.GridExtent, 'units'):
		None,

	(grids.GridExtent, 'maximum_longitude'):
		None,



	(grids.CoordinateList, 'uom'):
		"Units of measure used by the coordinates.",

	(grids.CoordinateList, 'has_constant_offset'):
		"Set to true if coordinates in the built array have constant offset.",

	(grids.CoordinateList, 'length'):
		"Specifies the length of the coordinate array. This should always be the final, as-built length of the array if the hasConstantOffset property is set to true and the compact notation (start coordinate plus offset) is used.",



	(grids.GridTile, 'zcoords'):
		"This optional property may be used to specify the vertical coordinates (e.g. heights or model levels) at which a grid tile is utilised or realised. In the case of simple grid tiles the equivalent zcoords property on the SimpleGridGeometry data type would be used instead. The current property is intended to be used when the horizontal grid coordinates are defined by one of the other methods.",

	(grids.GridTile, 'horizontal_resolution'):
		"Provides an indication of the approximate spatial sampling size of the grid tile, i.e. the size of the underlying grid cells. (Note: the maximum spatial resolution of the grid is twice the sampling size (e.g. 2 km for a 1 km x 1 km grid pitch).",

	(grids.GridTile, 'id'):
		"Specifies an identifer for a grid tile that is unique within its parent grid mosaic. It is not required for this identifier to be unique either across all mosaics in a GridSpec or across all GridSpecs, though if that were the case it would not be detrimental.",

	(grids.GridTile, 'area'):
		"gml:MeasureType:Specifies the area of the grid tile in the units defined by the uom attribute that is attached to the GML MeasureType data type.",

	(grids.GridTile, 'is_conformal'):
		"This property is used to indicate if the grid tile is conformal, i.e. angle-preserving. If so, angles measured on the grid are equal to the equivalent angles on the Earth.",

	(grids.GridTile, 'cell_array'):
		"GridCellArray:This property may be used to specify an array of grid cell definitions which together define the coordinate geometry of a grid tile. Depending on context, any of the existing sub-types of GridCell may be used. Mixing types is, however, not currently permitted.",

	(grids.GridTile, 'is_regular'):
		"If true, indicates that the horizontal coordinates of the grid can be defined using 1D arrays (vectors). This means that grid node locations are defined by the cartesian product of the X/Lon and Y/Lat coordinate vectors. It also means that grid cells are logically rectangular (they may also be physically rectangular in the case of projected coordinates).",

	(grids.GridTile, 'cell_ref_array'):
		"GridCellArray:This property may be used to define the coordinate geometry of a grid tile by specifying an array of references to remotely defined grid cells. Depending on context, any of the existing sub-types of GridCell may be referenced.",

	(grids.GridTile, 'is_terrain_following'):
		"Set to true if the vertical coordinate system is terrain-following even if, as is often the case, this only applies to the lower levels of the grid.",

	(grids.GridTile, 'vertical_crs'):
		"gml:CRSPropertyType:Specifies the vertical coordinate reference system used in the definition of the grid tile coordinates. This property should normally be an xlink reference to an external vertical CRS definition (e.g. in a separate CRS dictionary). If required, however, the property may be defined in situ within a CIM document.",

	(grids.GridTile, 'coord_file'):
		"This property may be used to specify the URI of a file containing grid coordinates that define the geometry of a a grid tile. It is envisaged that this will be the preferred mechanism for specifying the geometry of complex grids.",

	(grids.GridTile, 'is_uniform'):
		"If true, indicates that horizontal coordinates have fixed offsets in the X and Y directions. If the offset is the same in both directions then the grids are logically square, otherwise they are logically rectangular. The offsets can be specified by two scalar values (or three values in the case of 3D grids).",

	(grids.GridTile, 'coordinate_pole'):
		"gml:PointType:The coordinatePole property may be used to specify the lat-long position of any coordinate poles (in the mathematical sense) that form part of the definition of a grid tile. Not to be confused with the gridNorthPole property.  If required, two or more coordinate pole definitions may be distinguished by setting the gml:id attribute to appropriate values, such as spole, npole, etc.",

	(grids.GridTile, 'long_name'):
		None,

	(grids.GridTile, 'horizontal_crs'):
		"gml:CRSPropertyType:Specifies the horizontal coordinate reference system used in the definition of the grid tile coordinates. This property should normally be an xlink reference to an external horizontal CRS definition (e.g. in a separate CRS dictionary). If required, however, the property may be defined in situ within a CIM document.",

	(grids.GridTile, 'mnemonic'):
		None,

	(grids.GridTile, 'grid_north_pole'):
		"gml:PointType:If required, defines the lat-long position of the north pole used by the grid tile in the case of rotated/displaced pole grids. Not to be confused with the coordinatePole property.",

	(grids.GridTile, 'nx'):
		"Specifies the length of the X, or longitude, dimension of the grid tile.",

	(grids.GridTile, 'simple_grid_geom'):
		"SimpleGridGeometry:This property may be used to define the coordinates of the nodes or cells making up a simple (i.e. uniform or regular) grid tile. More details are provided in the description of the SimpleGridGeometry data type.",

	(grids.GridTile, 'ny'):
		"Specifies the length of the Y, or latitude, dimension of the grid tile.",

	(grids.GridTile, 'nz'):
		"Specifies the length of the Z, or height/level, dimension of the grid tile. The zcoords coordinate list property, if specified, should have this length.",

	(grids.GridTile, 'refinement_scheme'):
		None,

	(grids.GridTile, 'description'):
		"A free-text description of a grid tile.",

	(grids.GridTile, 'discretization_type'):
		"Indicates the type of discretization applied to the grid tile, e.g. 'logically_rectangular'.",

	(grids.GridTile, 'short_name'):
		None,

	(grids.GridTile, 'extent'):
		None,

	(grids.GridTile, 'vertical_resolution'):
		"Provides an indication of the approximate resolution of the grid tile in the vertical dimension. (Added to align with corresponding ESG/Curator and DIF property).",

	(grids.GridTile, 'geometry_type'):
		"Indicates the geometric figure used to approximate the figure of the Earth, e.g. 'sphere'.",





	(grids.SimpleGridGeometry, 'xcoords'):
		"X-Co-ordinates",

	(grids.SimpleGridGeometry, 'dim_order'):
		None,

	(grids.SimpleGridGeometry, 'ycoords'):
		"Y-Co-ordinates",

	(grids.SimpleGridGeometry, 'is_mesh'):
		None,

	(grids.SimpleGridGeometry, 'zcoords'):
		"Z-Co-ordinates",

	(grids.SimpleGridGeometry, 'num_dims'):
		None,





	(quality.CimQuality, 'meta'):
		None,

	(quality.CimQuality, 'reports'):
		None,



	(quality.Report, 'date'):
		None,

	(quality.Report, 'measure'):
		None,

	(quality.Report, 'evaluator'):
		None,

	(quality.Report, 'evaluation'):
		None,



	(quality.Evaluation, 'specification_hyperlink'):
		None,

	(quality.Evaluation, 'description'):
		None,

	(quality.Evaluation, 'did_pass'):
		None,

	(quality.Evaluation, 'type'):
		None,

	(quality.Evaluation, 'type_hyperlink'):
		None,

	(quality.Evaluation, 'explanation'):
		None,

	(quality.Evaluation, 'specification'):
		None,

	(quality.Evaluation, 'date'):
		None,

	(quality.Evaluation, 'title'):
		None,



	(quality.Measure, 'name'):
		None,

	(quality.Measure, 'description'):
		None,

	(quality.Measure, 'identification'):
		None,





	(data.DataTopic, 'description'):
		None,

	(data.DataTopic, 'unit'):
		None,

	(data.DataTopic, 'name'):
		None,



	(data.DataExtent, 'geographical'):
		None,

	(data.DataExtent, 'temporal'):
		None,



	(data.DataObject, 'geometry_model'):
		None,

	(data.DataObject, 'properties'):
		None,

	(data.DataObject, 'description'):
		None,

	(data.DataObject, 'hierarchy_level'):
		None,

	(data.DataObject, 'keyword'):
		None,

	(data.DataObject, 'purpose'):
		None,

	(data.DataObject, 'citations'):
		None,

	(data.DataObject, 'distribution'):
		None,

	(data.DataObject, 'storage'):
		None,

	(data.DataObject, 'extent'):
		None,

	(data.DataObject, 'restriction'):
		None,

	(data.DataObject, 'content'):
		"The content of a DataObject corresponds to a variable (in THREDDS, ...etc.)",

	(data.DataObject, 'parent_object'):
		None,

	(data.DataObject, 'source_simulation'):
		None,

	(data.DataObject, 'acronym'):
		None,

	(data.DataObject, 'meta'):
		None,

	(data.DataObject, 'data_status'):
		None,

	(data.DataObject, 'child_object'):
		None,



	(data.DataHierarchyLevel, 'is_open'):
		None,

	(data.DataHierarchyLevel, 'value'):
		"What is the name of the specific HierarchyLevel this DataObject is being organised at (ie: if the HierarchyLevel is 'run' then the name might be the runid).",

	(data.DataHierarchyLevel, 'name'):
		"What level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.",



	(data.DataStorage, 'format'):
		None,

	(data.DataStorage, 'modification_date'):
		None,

	(data.DataStorage, 'size'):
		None,

	(data.DataStorage, 'location'):
		None,



	(data.DataExtentGeographical, 'west'):
		None,

	(data.DataExtentGeographical, 'south'):
		None,

	(data.DataExtentGeographical, 'east'):
		None,

	(data.DataExtentGeographical, 'north'):
		None,



	(data.DataProperty, 'description'):
		None,



	(data.DataStorageFile, 'path'):
		None,

	(data.DataStorageFile, 'file_name'):
		None,

	(data.DataStorageFile, 'file_system'):
		None,



	(data.DataContent, 'aggregation'):
		"Describes how the content has been aggregated together: sum, min, mean, max, ...",

	(data.DataContent, 'topic'):
		None,

	(data.DataContent, 'frequency'):
		"Describes the frequency of the data content: daily, hourly, ...",



	(data.DataDistribution, 'access'):
		None,

	(data.DataDistribution, 'responsible_party'):
		None,

	(data.DataDistribution, 'format'):
		None,

	(data.DataDistribution, 'fee'):
		None,



	(data.DataRestriction, 'scope'):
		"The thing (data or metadata, access or use) that this restriction is applied to.",

	(data.DataRestriction, 'license'):
		"The thing (data or metadata, access or use) that this restriction is applied to.",

	(data.DataRestriction, 'restriction'):
		"The thing (data or metadata, access or use) that this restriction is applied to.",



	(data.DataExtentTimeInterval, 'factor'):
		None,

	(data.DataExtentTimeInterval, 'unit'):
		None,

	(data.DataExtentTimeInterval, 'radix'):
		None,



	(data.DataStorageIp, 'protocol'):
		None,

	(data.DataStorageIp, 'file_name'):
		None,

	(data.DataStorageIp, 'path'):
		None,

	(data.DataStorageIp, 'host'):
		None,



	(data.DataExtentTemporal, 'begin'):
		None,

	(data.DataExtentTemporal, 'time_interval'):
		None,

	(data.DataExtentTemporal, 'end'):
		None,



	(data.DataStorageDb, 'access_string'):
		None,

	(data.DataStorageDb, 'table'):
		None,

	(data.DataStorageDb, 'owner'):
		None,

	(data.DataStorageDb, 'name'):
		None,





	(activity.Experiment, 'generates'):
		None,

	(activity.Experiment, 'supports'):
		None,

	(activity.Experiment, 'measurement_campaigns'):
		None,

	(activity.Experiment, 'requires'):
		None,



	(activity.SimulationRelationship, 'target'):
		None,

	(activity.SimulationRelationship, 'type'):
		None,



	(activity.EnsembleMember, 'ensemble'):
		None,

	(activity.EnsembleMember, 'simulation'):
		None,

	(activity.EnsembleMember, 'ensemble_ids'):
		None,



	(activity.NumericalRequirement, 'requirement_type'):
		"Type of reqirement to which the experiment must conform.",

	(activity.NumericalRequirement, 'source'):
		None,

	(activity.NumericalRequirement, 'id'):
		None,

	(activity.NumericalRequirement, 'name'):
		None,

	(activity.NumericalRequirement, 'options'):
		None,

	(activity.NumericalRequirement, 'description'):
		None,





	(activity.DownscalingSimulation, 'downscaling_type'):
		None,

	(activity.DownscalingSimulation, 'outputs'):
		None,

	(activity.DownscalingSimulation, 'downscaling_id'):
		None,

	(activity.DownscalingSimulation, 'meta'):
		None,

	(activity.DownscalingSimulation, 'calendar'):
		None,

	(activity.DownscalingSimulation, 'inputs'):
		"Implemented as a mapping from a source to target; can be a forcing file, a boundary condition, etc.",

	(activity.DownscalingSimulation, 'downscaled_from'):
		None,



	(activity.NumericalActivity, 'supports'):
		None,

	(activity.NumericalActivity, 'description'):
		"A free-text description of the experiment.",

	(activity.NumericalActivity, 'short_name'):
		"The name of the experiment (that is used internally).",

	(activity.NumericalActivity, 'long_name'):
		"The name of the experiment (that is recognized externally).",



	(activity.Simulation, 'inputs'):
		"Implemented as a mapping from a source to target; can be a forcing file, a boundary condition, etc.",

	(activity.Simulation, 'spinup_date_range'):
		"The date range that a simulation is engaged in spinup.",

	(activity.Simulation, 'calendar'):
		None,

	(activity.Simulation, 'control_simulation'):
		"Points to a simulation being used as the basis (control) run.  Note that only 'derived' simulations can describe something as being control; a simulation should not know if it is being used itself as the control of some other run.",

	(activity.Simulation, 'restarts'):
		None,

	(activity.Simulation, 'spinup_simulation'):
		"The (external) simulation used during 'spinup.'  Note that this element can be used in conjuntion with spinupDateRange.  If a simulation has the latter but not the former, then one can assume that the simulation is performing its own spinup.",

	(activity.Simulation, 'conformances'):
		None,

	(activity.Simulation, 'deployments'):
		None,

	(activity.Simulation, 'authors'):
		"List of associated authors.",

	(activity.Simulation, 'simulation_id'):
		None,

	(activity.Simulation, 'outputs'):
		None,



	(activity.ExperimentRelationship, 'target'):
		None,

	(activity.ExperimentRelationship, 'type'):
		None,



	(activity.ExperimentRelationshipTarget, 'numerical_experiment'):
		None,



	(activity.NumericalRequirementOption, 'sub_options'):
		None,

	(activity.NumericalRequirementOption, 'description'):
		None,

	(activity.NumericalRequirementOption, 'name'):
		None,

	(activity.NumericalRequirementOption, 'relationship'):
		"Describes how this optional (child) requirement is related to its sibling requirements.  For example, a NumericalRequirement could consist of a set of optional requirements each with an 'OR' relationship meaning use this boundary condition _or_ that one.",

	(activity.NumericalRequirementOption, 'id'):
		None,



	(activity.Activity, 'responsible_parties'):
		"The point of contact(s) for this activity.This includes, among others, the principle investigator.",

	(activity.Activity, 'funding_sources'):
		"The entities that funded this activity.",

	(activity.Activity, 'rationales'):
		"For what purpose is this activity being performed?",

	(activity.Activity, 'projects'):
		"The project(s) that this activity is associated with (ie: CMIP5, AMIP, etc).",



	(activity.MeasurementCampaign, 'duration'):
		None,



	(activity.SimulationRelationshipTarget, 'simulation'):
		None,

	(activity.SimulationRelationshipTarget, 'target'):
		None,



	(activity.SimulationRun, 'model'):
		None,

	(activity.SimulationRun, 'date_range'):
		None,

	(activity.SimulationRun, 'meta'):
		None,





	(activity.Conformance, 'description'):
		None,

	(activity.Conformance, 'sources'):
		"Points to the DataSource used to conform to a particular Requirement.   This may be part of an activity::simulation or a software::component.  It can be either a DataObject or a SoftwareComponent or a ComponentProperty.  It could also be by using particular attributes of, say, a SoftwareComponent, but in that case the recommended practise is to reference the component and add appropriate text in the conformance description attribute.",

	(activity.Conformance, 'frequency'):
		None,

	(activity.Conformance, 'type'):
		"Describes the method that this simulation conforms to an experimental requirement (in case it is not specified by the change property of the reference to the source of this conformance)",

	(activity.Conformance, 'is_conformant'):
		"Records whether or not this conformance satisfies the requirement.  A simulation should have at least one conformance mapping to every experimental requirement.  If a simulation satisfies the requirement - the usual case - then conformant should have a value of true.  If conformant is true but there is no reference to a source for the conformance, then we can assume that the simulation conforms to the requirement _naturally_, that is without having to modify code or inputs. If a simulation does not conform to a requirement then conformant should be set to false.",

	(activity.Conformance, 'requirements'):
		"Points to the NumericalRequirement that the simulation in question is conforming to.",





	(activity.Ensemble, 'outputs'):
		"Points to the DataSource used to conform to a particular Requirement.   This may be part of an activity::simulation or a software::component.  It can be either a DataObject or a SoftwareComponent or a ComponentProperty.  It could also be by using particular attributes of, say, a SoftwareComponent, but in that case the recommended practise is to reference the component and add appropriate text in the conformance description attribute.",

	(activity.Ensemble, 'members'):
		None,

	(activity.Ensemble, 'types'):
		None,

	(activity.Ensemble, 'meta'):
		None,





	(activity.SimulationComposite, 'date_range'):
		None,

	(activity.SimulationComposite, 'rank'):
		"Position of a simulation in the SimulationComposite timeline. eg:  Is this the first (rank = 1) or second (rank = 2) simulation",

	(activity.SimulationComposite, 'child'):
		None,

	(activity.SimulationComposite, 'meta'):
		None,





	(activity.NumericalExperiment, 'description'):
		"A free-text description of the experiment.",

	(activity.NumericalExperiment, 'short_name'):
		"The name of the experiment (that is used internally).",

	(activity.NumericalExperiment, 'experiment_id'):
		"An experiment ID takes the form <number>.<number>[-<letter>].",

	(activity.NumericalExperiment, 'requirements'):
		"The name of the experiment (that is used internally).",

	(activity.NumericalExperiment, 'long_name'):
		"The name of the experiment (that is recognized externally).",

	(activity.NumericalExperiment, 'meta'):
		None,



	(activity.SpatioTemporalConstraint, 'date_range'):
		None,

	(activity.SpatioTemporalConstraint, 'spatial_resolution'):
		None,





	(misc.DocumentSet, 'model'):
		"Associated model component.",

	(misc.DocumentSet, 'experiment'):
		"Associated numerical experiment.",

	(misc.DocumentSet, 'meta'):
		None,

	(misc.DocumentSet, 'platform'):
		"Associated simulation execution platform.",

	(misc.DocumentSet, 'data'):
		"Associated input/output data.",

	(misc.DocumentSet, 'ensembles'):
		"Associated ensemble runs.",

	(misc.DocumentSet, 'simulation'):
		"Associated simulation run.",

	(misc.DocumentSet, 'grids'):
		"Associated grid-spec.",



	# ------------------------------------------------
	# Enums.
	# ------------------------------------------------


	shared.DocRelationshipDirectionType: """
		Creates and returns instance of relationship_direction_type enum.

	""",

	shared.DocStatusType: """
		Status of cim document.

	""",

	shared.MachineType: """
		A list of known machines.

	""",

	shared.CompilerType: """
		Creates and returns instance of compiler_type enum.

	""",

	shared.OperatingSystemType: """
		A list of common operating systems.

	""",

	shared.DocRelationshipType: """
		Creates and returns instance of document_relationship_type enum.

	""",

	shared.DataPurpose: """
		Purpose of the data - i.e. ancillaryFile, boundaryCondition or initialCondition.

	""",

	shared.MachineVendorType: """
		A list of organisations that create machines.

	""",

	shared.ChangePropertyType: """
		Creates and returns instance of change_property_type enum.

	""",

	shared.ProcessorType: """
		A list of known cpu's.

	""",

	shared.UnitType: """
		A list of scientific units.

	""",

	shared.InterconnectType: """
		A list of connectors between machines.

	""",

	shared.DocType: """
		Creates and returns instance of doc_type enum.

	""",



	software.SpatialRegriddingDimensionType: """
		Creates and returns instance of spatial_regridding_dimension_type enum.

	""",

	software.SpatialRegriddingStandardMethodType: """
		Creates and returns instance of spatial_regridding_standard_method_type enum.

	""",

	software.StatisticalModelComponentType: """
		An enumeration of types of ProcessorComponent.  This includes things like transformers and post-processors.

	""",

	software.CouplingFrameworkType: """
		Creates and returns instance of coupling_framework_type enum.

	""",

	software.ComponentPropertyIntentType: """
		The direction that the associated component property is intended to be coupled: in, out, or inout.

	""",

	software.ConnectionType: """
		The ConnectionType enumeration describes the mechanism of transport for a connection.

	""",

	software.TimeMappingType: """
		Enumerates the different ways that time can be mapped when transforming from one field to another.

	""",

	software.TimingUnits: """
		Creates and returns instance of timing_units enum.

	""",

	software.ModelComponentType: """
		An enumeration of types of ModelComponent. This includes things like atmosphere & ocean models, radiation schemes, etc. CIM best-practice is to describe every component for which there is a named ComponentType as a separate component, even if it is not a separate unit of software (ie: even if it is embedded), instead of as a (set of) ModelParameters. This codelist is synonomous with 'realm' for the purposes of CMIP5.

	""",



	grids.HorizontalCsEnum: """
		Creates and returns instance of horizontal_cs_enum enum.

	""",

	grids.GridNodePositionEnum: """
		Creates and returns instance of grid_node_position_enum enum.

	""",

	grids.DiscretizationEnum: """
		Creates and returns instance of discretization_enum enum.

	""",

	grids.FeatureTypeEnum: """
		Creates and returns instance of feature_type_enum enum.

	""",

	grids.ArcTypeEnum: """
		Creates and returns instance of arc_type_enum enum.

	""",

	grids.RefinementTypeEnum: """
		Creates and returns instance of refinement_type_enum enum.

	""",

	grids.GeometryTypeEnum: """
		Creates and returns instance of geometry_type_enum enum.

	""",

	grids.VerticalCsEnum: """
		Creates and returns instance of vertical_cs_enum enum.

	""",

	grids.GridTypeEnum: """
		Creates and returns instance of grid_type_enum enum.

	""",



	quality.CimResultType: """
		Creates and returns instance of cim_result_type enum.

	""",

	quality.CimFeatureType: """
		Creates and returns instance of cim_feature_type enum.

	""",

	quality.QualitySeverityType: """
		Creates and returns instance of quality_severity_type enum.

	""",

	quality.QualityStatusType: """
		Creates and returns instance of quality_status_type enum.

	""",

	quality.QualityIssueType: """
		Creates and returns instance of quality_issue_type enum.

	""",

	quality.CimScopeCodeType: """
		This would cover quality issues with the CIM itself.

	""",



	data.DataStatusType: """
		Enumerates status of a data object.

	""",

	data.DataHierarchyType: """
		Enumerates the level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.

	""",



	activity.ExperimentRelationshipType: """
		Creates and returns instance of experiment_relationship_type enum.

	""",

	activity.DownscalingType: """
		Creates and returns instance of downscaling_type enum.

	""",

	activity.SimulationRelationshipType: """
		Creates and returns instance of simulation_relationship_type enum.

	""",

	activity.FrequencyType: """
		Creates and returns instance of frequency_type enum.

	""",

	activity.ProjectType: """
		Creates and returns instance of project_type enum.

	""",

	activity.ResolutionType: """
		Creates and returns instance of resolution_type enum.

	""",

	activity.ConformanceType: """
		Creates and returns instance of conformance_type enum.

	""",

	activity.EnsembleType: """
		Creates and returns instance of ensemble_type enum.

	""",

	activity.SimulationType: """
		Creates and returns instance of simulation_type enum.

	""",




	# ------------------------------------------------
	# Enum members.
	# ------------------------------------------------



	(shared.DocRelationshipDirectionType, 'fromTarget'):
		None,

	(shared.DocRelationshipDirectionType, 'toTarget'):
		None,



	(shared.DocStatusType, 'complete'):
		None,

	(shared.DocStatusType, 'incomplete'):
		None,

	(shared.DocStatusType, 'in-progress'):
		None,



	(shared.MachineType, 'Vector'):
		None,

	(shared.MachineType, 'Beowulf'):
		None,

	(shared.MachineType, 'Parallel'):
		None,







	(shared.DocRelationshipType, 'similarTo'):
		None,

	(shared.DocRelationshipType, 'fixedVersionOf'):
		None,

	(shared.DocRelationshipType, 'previousVersionOf'):
		None,

	(shared.DocRelationshipType, 'other'):
		None,

	(shared.DocRelationshipType, 'laterVersionOf'):
		None,



	(shared.DataPurpose, 'ancillaryFile'):
		None,

	(shared.DataPurpose, 'boundaryCondition'):
		None,

	(shared.DataPurpose, 'initialCondition'):
		None,





	(shared.ChangePropertyType, 'Decrement'):
		None,

	(shared.ChangePropertyType, 'Increment'):
		None,

	(shared.ChangePropertyType, 'InitialCondition'):
		"A specific type of ModelMod",

	(shared.ChangePropertyType, 'Redistribution'):
		None,

	(shared.ChangePropertyType, 'Replacement'):
		None,

	(shared.ChangePropertyType, 'ModelMod'):
		None,

	(shared.ChangePropertyType, 'ParameterChange'):
		"A specific type of ModelMod",

	(shared.ChangePropertyType, 'CodeChange'):
		"A specific type of ModelMod",

	(shared.ChangePropertyType, 'InputMod'):
		None,

	(shared.ChangePropertyType, 'AncillaryFile'):
		"A specific type of ModelMod",

	(shared.ChangePropertyType, 'BoundaryCondition'):
		"A specific type of ModelMod",

	(shared.ChangePropertyType, 'Unused'):
		None,









	(shared.DocType, 'gridSpec'):
		None,

	(shared.DocType, 'cimQuality'):
		None,

	(shared.DocType, 'numericalExperiment'):
		None,

	(shared.DocType, 'platform'):
		None,

	(shared.DocType, 'assimilation'):
		None,

	(shared.DocType, 'processorComponent'):
		None,

	(shared.DocType, 'simulationComposite'):
		None,

	(shared.DocType, 'modelComponent'):
		None,

	(shared.DocType, 'statisticalModelComponent'):
		None,

	(shared.DocType, 'dataProcessing'):
		None,

	(shared.DocType, 'downscalingSimulation'):
		None,

	(shared.DocType, 'ensemble'):
		None,

	(shared.DocType, 'dataObject'):
		None,

	(shared.DocType, 'simulationRun'):
		None,





	(software.SpatialRegriddingDimensionType, '2D'):
		None,

	(software.SpatialRegriddingDimensionType, '1D'):
		None,

	(software.SpatialRegriddingDimensionType, '3D'):
		None,



	(software.SpatialRegriddingStandardMethodType, 'conservative-first-order'):
		None,

	(software.SpatialRegriddingStandardMethodType, 'conservative-second-order'):
		None,

	(software.SpatialRegriddingStandardMethodType, 'conservative'):
		None,

	(software.SpatialRegriddingStandardMethodType, 'non-conservative'):
		None,

	(software.SpatialRegriddingStandardMethodType, 'linear'):
		None,

	(software.SpatialRegriddingStandardMethodType, 'near-neighbour'):
		None,

	(software.SpatialRegriddingStandardMethodType, 'cubic'):
		None,





	(software.CouplingFrameworkType, 'BFG'):
		None,

	(software.CouplingFrameworkType, 'ESMF'):
		None,

	(software.CouplingFrameworkType, 'OASIS'):
		None,



	(software.ComponentPropertyIntentType, 'out'):
		None,

	(software.ComponentPropertyIntentType, 'in'):
		None,

	(software.ComponentPropertyIntentType, 'inout'):
		None,







	(software.TimingUnits, 'minutes'):
		None,

	(software.TimingUnits, 'hours'):
		None,

	(software.TimingUnits, 'days'):
		None,

	(software.TimingUnits, 'months'):
		None,

	(software.TimingUnits, 'years'):
		None,

	(software.TimingUnits, 'decades'):
		None,

	(software.TimingUnits, 'centuries'):
		None,

	(software.TimingUnits, 'seconds'):
		None,







	(grids.HorizontalCsEnum, 'spherical'):
		None,

	(grids.HorizontalCsEnum, 'ellipsoidal'):
		None,

	(grids.HorizontalCsEnum, 'cartesian'):
		None,

	(grids.HorizontalCsEnum, 'polar'):
		None,



	(grids.GridNodePositionEnum, 'centre'):
		None,

	(grids.GridNodePositionEnum, 'plane'):
		None,

	(grids.GridNodePositionEnum, 'sphere'):
		None,



	(grids.DiscretizationEnum, 'unstructured_triangular'):
		None,

	(grids.DiscretizationEnum, 'pixel-based_catchment'):
		None,

	(grids.DiscretizationEnum, 'unstructured_polygonal'):
		None,

	(grids.DiscretizationEnum, 'spherical_harmonics'):
		None,

	(grids.DiscretizationEnum, 'other'):
		None,

	(grids.DiscretizationEnum, 'logically_rectangular'):
		None,

	(grids.DiscretizationEnum, 'structured_triangular'):
		None,



	(grids.FeatureTypeEnum, 'point'):
		None,

	(grids.FeatureTypeEnum, 'edge'):
		None,



	(grids.ArcTypeEnum, 'geodesic'):
		None,

	(grids.ArcTypeEnum, 'complex'):
		None,

	(grids.ArcTypeEnum, 'small_circle'):
		None,

	(grids.ArcTypeEnum, 'great_circle'):
		None,



	(grids.RefinementTypeEnum, 'integer'):
		"The refinement is integer when grid lines from the coarser grid are continuous on the finer grid, but not vice versa.",

	(grids.RefinementTypeEnum, 'none'):
		"Tile boundaries have no refinement when the grid lines meeting at the tile boundary are continuous.",

	(grids.RefinementTypeEnum, 'rational'):
		"The refinement is rational when the adjacent or overlapping grid tiles have grid line counts that are coprime (i.e. no common factor other than 1).",



	(grids.GeometryTypeEnum, 'ellipsoid'):
		None,

	(grids.GeometryTypeEnum, 'plane'):
		None,

	(grids.GeometryTypeEnum, 'sphere'):
		None,



	(grids.VerticalCsEnum, 'space-based'):
		None,

	(grids.VerticalCsEnum, 'mass-based'):
		None,



	(grids.GridTypeEnum, 'icosahedral_geodesic'):
		None,

	(grids.GridTypeEnum, 'reduced_gaussian'):
		None,

	(grids.GridTypeEnum, 'regular_lat_lon'):
		None,

	(grids.GridTypeEnum, 'spectral_gaussian'):
		None,

	(grids.GridTypeEnum, 'displaced_pole'):
		None,

	(grids.GridTypeEnum, 'tripolar'):
		None,

	(grids.GridTypeEnum, 'yin_yang'):
		None,

	(grids.GridTypeEnum, 'cubed_sphere'):
		None,

	(grids.GridTypeEnum, 'composite'):
		None,

	(grids.GridTypeEnum, 'other'):
		None,





	(quality.CimResultType, 'document'):
		None,

	(quality.CimResultType, 'logfile'):
		None,

	(quality.CimResultType, 'plot'):
		None,



	(quality.CimFeatureType, 'diagnostic'):
		None,

	(quality.CimFeatureType, 'file'):
		None,



	(quality.QualitySeverityType, 'cosmetic'):
		None,

	(quality.QualitySeverityType, 'minor'):
		None,

	(quality.QualitySeverityType, 'major'):
		None,



	(quality.QualityStatusType, 'partially_resolved'):
		None,

	(quality.QualityStatusType, 'resolved'):
		None,

	(quality.QualityStatusType, 'confirmed'):
		None,

	(quality.QualityStatusType, 'reported'):
		None,



	(quality.QualityIssueType, 'data_format'):
		None,

	(quality.QualityIssueType, 'metadata'):
		None,

	(quality.QualityIssueType, 'data_content'):
		None,

	(quality.QualityIssueType, 'science'):
		None,

	(quality.QualityIssueType, 'data_indexing'):
		None,



	(quality.CimScopeCodeType, 'dataset'):
		None,

	(quality.CimScopeCodeType, 'file'):
		None,

	(quality.CimScopeCodeType, 'ensemble'):
		None,

	(quality.CimScopeCodeType, 'service'):
		None,

	(quality.CimScopeCodeType, 'model'):
		None,

	(quality.CimScopeCodeType, 'modelComponent'):
		None,

	(quality.CimScopeCodeType, 'simulation'):
		None,

	(quality.CimScopeCodeType, 'experiment'):
		None,

	(quality.CimScopeCodeType, 'numericalRequirement'):
		None,

	(quality.CimScopeCodeType, 'software'):
		None,





	(data.DataStatusType, 'metadataOnly'):
		"This DataObject is incomplete - it is described in metadata but the actual data has not yet been linked to it.",

	(data.DataStatusType, 'complete'):
		"This DataObject is complete.",

	(data.DataStatusType, 'continuouslySupplemented'):
		"This DataObject's actual data is continuously updated.",







	(activity.ExperimentRelationshipType, 'shorterVersionOf'):
		None,

	(activity.ExperimentRelationshipType, 'extensionOf'):
		None,

	(activity.ExperimentRelationshipType, 'continuationOf'):
		None,

	(activity.ExperimentRelationshipType, 'controlExperiment'):
		None,

	(activity.ExperimentRelationshipType, 'higherResolutionVersionOf'):
		None,

	(activity.ExperimentRelationshipType, 'lowerResolutionVersionOf'):
		None,

	(activity.ExperimentRelationshipType, 'increaseEnsembleOf'):
		None,

	(activity.ExperimentRelationshipType, 'modifiedInputMethodOf'):
		None,

	(activity.ExperimentRelationshipType, 'previousRealisation'):
		None,



	(activity.DownscalingType, 'statistical'):
		None,

	(activity.DownscalingType, 'dynamic'):
		None,



	(activity.SimulationRelationshipType, 'previousSimulation'):
		None,

	(activity.SimulationRelationshipType, 'higherResolutionVersionOf'):
		None,

	(activity.SimulationRelationshipType, 'lowerResolutionVersionOf'):
		None,

	(activity.SimulationRelationshipType, 'fixedVersionOf'):
		None,

	(activity.SimulationRelationshipType, 'followingSimulation'):
		None,

	(activity.SimulationRelationshipType, 'extensionOf'):
		None,

	(activity.SimulationRelationshipType, 'responseTo'):
		None,

	(activity.SimulationRelationshipType, 'continuationOf'):
		None,









	(activity.ConformanceType, 'standard config'):
		"Describes a simulation that is 'naturally' conformant to an experimental requirement.",

	(activity.ConformanceType, 'via inputs'):
		"Describes a simulation that conforms to an experimental requirement by using particular inputs.",

	(activity.ConformanceType, 'via model mods'):
		"Describes a simulation that conforms to an experimental requirement by changing the configuration of the software model implementing that simulation.",

	(activity.ConformanceType, 'combination'):
		"Describes a simulation that conforms to an experimental requirement by using more than one method.",

	(activity.ConformanceType, 'not-xxx'):
		None,

	(activity.ConformanceType, 'not conformant'):
		"Describes a simulation that is purpefully non-conformant to an experimental requirement.",





	(activity.SimulationType, 'simulationComposite'):
		None,

	(activity.SimulationType, 'assimilation'):
		None,

	(activity.SimulationType, 'simulationRun'):
		None,





}
