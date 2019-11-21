"""
.. module:: activity_classes.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 activity package class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""


def activity():
    """An abstract class used as the parent of MeasurementCampaigns, Projects, Experiments, and NumericalActivities.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': True,
        'properties': [
            ('funding_sources', 'str', '0.N'),
            ('projects', 'activity.project_type', '0.N'),
            ('rationales', 'str', '0.N'),
            ('responsible_parties', 'shared.responsible_party', '0.N'),
        ],
        'doc_strings': {
            'funding_sources': 'The entities that funded this activity.',
            'projects': 'The project(s) that this activity is associated with (ie: CMIP5, AMIP, etc).',
            'rationales': 'For what purpose is this activity being performed?',
            'responsible_parties': 'The point of contact(s) for this activity.This includes, among others, the principle investigator.',
        },
        'decodings': [
            ('funding_sources', 'child::cim:fundingSource'),
            ('projects', 'child::cim:project/@value'),
            ('rationales', 'child::cim:rationale'),
            ('responsible_parties', 'child::cim:responsibleParty'),
        ]
    }


def conformance():
    """A conformance class maps how a configured model component met a specific numerical requirement.  For example, for a double CO2 boundary condition, a model component might read a CO2 dataset in which CO2 has been doubled, or it might modify a parameterisation (presumably with a factor of two somewhere).  So, the conformance links a requirement to a DataSource (which can be either an actual DataObject or a property of a model component).  In some cases a model/simulation may _naturally_ conform to a requirement.  In this case there would be no reference to a DataSource but the conformant attribute would be true.  If something is purpopsefully non-conformant then the conformant attribute would be false.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'str', '0.1'),
            ('frequency', 'activity.frequency_type', '0.1'),
            ('is_conformant', 'bool', '1.1'),
            ('requirements', 'activity.numerical_requirement', '1.N'),
            ('sources', 'shared.data_source', '0.N'),
            ('type', 'activity.conformance_type', '0.1'),
        ],
        'doc_strings': {
            'is_conformant': 'Records whether or not this conformance satisfies the requirement.  A simulation should have at least one conformance mapping to every experimental requirement.  If a simulation satisfies the requirement - the usual case - then conformant should have a value of true.  If conformant is true but there is no reference to a source for the conformance, then we can assume that the simulation conforms to the requirement _naturally_, that is without having to modify code or inputs. If a simulation does not conform to a requirement then conformant should be set to false.',
            'requirements': 'Points to the NumericalRequirement that the simulation in question is conforming to.',
            'sources': 'Points to the DataSource used to conform to a particular Requirement.   This may be part of an activity::simulation or a software::component.  It can be either a DataObject or a SoftwareComponent or a ComponentProperty.  It could also be by using particular attributes of, say, a SoftwareComponent, but in that case the recommended practise is to reference the component and add appropriate text in the conformance description attribute.',
            'type': 'Describes the method that this simulation conforms to an experimental requirement (in case it is not specified by the change property of the reference to the source of this conformance)'
        },
        'decodings': [
            ('description', 'child::cim:description'),
            ('frequency', 'child::cim:frequency'),
            ('is_conformant', '@conformant'),
            ('requirements', 'child::cim:requirement/cim:requirement/cim:initialCondition', 'activity.initial_condition'),
            ('requirements', 'child::cim:requirement/cim:requirement/cim:boundaryCondition', 'activity.boundary_condition'),
            ('requirements', 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition', 'activity.lateral_boundary_condition'),
            ('requirements', 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint', 'activity.spatio_temporal_constraint'),
            ('requirements', 'child::cim:requirement/cim:requirement/cim:outputRequirement', 'activity.output_requirement'),
            ('requirements', 'child::cim:requirement/cim:reference', 'shared.doc_reference'),
            ('sources', 'child::cim:source/cim:source/cim:dataObject', 'data.data_object'),
            ('sources', 'child::cim:source/cim:source/cim:dataContent', 'data.data_content'),
            ('sources', 'child::cim:source/cim:source/cim:componentProperty', 'software.component_property'),
            ('sources', 'child::cim:source/cim:source/cim:softwareComponent', 'software.model_component'),
            ('sources', 'child::cim:source/cim:source/cim:softwareComponent', 'software.processor_component'),
            ('sources', 'child::cim:source/cim:source/cim:softwareComponent', 'software.statistical_model_component'),
            ('sources', 'child::cim:source/cim:reference', 'shared.doc_reference'),
            ('type', '@type'),
        ]
    }


def downscaling_simulation():
    """A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

    """
    return {
        'type': 'class',
        'base': 'activity.numerical_activity',
        'is_abstract': True,
        'is_document': True,
        'properties': [
            ('calendar', 'shared.calendar', '1.1'),
            ('inputs', 'software.coupling', '0.N'),
            ('outputs', 'data.data_object', '0.N'),
            ('downscaling_id', 'str', '0.1'),
            ('downscaled_from', 'shared.data_source', '1.1'),
            ('downscaling_type', 'activity.downscaling_type', '0.1')
        ],
        'doc_strings': {
            'inputs': 'Implemented as a mapping from a source to target; can be a forcing file, a boundary condition, etc.',
        },
        'decodings': [
            ('meta', 'self::cim:downscalingSimulation'),
            ('calendar', 'child::cim:calendar/cim:daily-360', 'shared.daily_360'),
            ('calendar', 'child::cim:calendar/cim:perpetualPeriod', 'shared.perpetual_period'),
            ('calendar', 'child::cim:calendar/cim:realCalendar', 'shared.real_calendar'),
            ('inputs', 'child::cim:input'),
            ('outputs', 'child::cim:output/cim:dataObject', 'data.data_object'),
            ('outputs', 'child::cim:output/cim:reference', 'shared.doc_reference'),
            ('downscaling_id', 'child::cim:downscalingID'),
            ('downscaled_from', 'child::cim:downscaledFrom/cim:downscaledFrom/cim:dataObject', 'data.data_object'),
            ('downscaled_from', 'child::cim:downscaledFrom/cim:downscaledFrom/cim:dataContent', 'data.data_content'),
            ('downscaled_from', 'child::cim:downscaledFrom/cim:downscaledFrom/cim:componentProperty', 'software.component_property'),
            ('downscaled_from', 'child::cim:downscaledFrom/cim:downscaledFrom/cim:softwareComponent', 'software.model_component'),
            ('downscaled_from', 'child::cim:downscaledFrom/cim:downscaledFrom/cim:softwareComponent', 'software.processor_component'),
            ('downscaled_from', 'child::cim:downscaledFrom/cim:downscaledFrom/cim:softwareComponent', 'software.statistical_model_component'),
            ('downscaled_from', 'child::cim:downscaledFrom/cim:reference', 'shared.doc_reference'),
            ('downscaling_type', 'self::cim:downscalingSimulation/@downscalingType'),
        ]
    }


def ensemble():
    """An ensemble is made up of two or more simulations which are to be compared against each other to create ensemble statistics. Ensemble members can differ in terms of initial conditions, physical parameterisation and the model used. An ensemble bundles together sets of ensembleMembers, all of which reference the same Simulation(Run) and include one or more changes.

    """
    return {
        'type': 'class',
        'base': 'activity.numerical_activity',
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('members', 'activity.ensemble_member', '1.N'),
            ('types', 'activity.ensemble_type', '1.N'),
            ('outputs', 'shared.data_source', '0.N')
        ],
        'doc_strings': {
            'outputs': 'Points to the DataSource used to conform to a particular Requirement.   This may be part of an activity::simulation or a software::component.  It can be either a DataObject or a SoftwareComponent or a ComponentProperty.  It could also be by using particular attributes of, say, a SoftwareComponent, but in that case the recommended practise is to reference the component and add appropriate text in the conformance description attribute.',
        },
        'decodings': [
            ('meta', 'self::cim:ensemble'),
            ('members', 'child::cim:ensembleMember'),
            ('types', 'child::cim:ensembleType/@value'),
            ('outputs', 'child::cim:output/cim:output/cim:dataObject', 'data.data_object'),
            ('outputs', 'child::cim:output/cim:output/cim:dataContent', 'data.data_content'),
            ('outputs', 'child::cim:output/cim:output/cim:componentProperty', 'software.component_property'),
            ('outputs', 'child::cim:output/cim:output/cim:softwareComponent', 'software.model_component'),
            ('outputs', 'child::cim:output/cim:output/cim:softwareComponent', 'software.processor_component'),
            ('outputs', 'child::cim:output/cim:output/cim:softwareComponent', 'software.statistical_model_component'),
            ('outputs', 'child::cim:output/cim:reference', 'shared.doc_reference')
        ]
    }


def ensemble_member():
    """A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a "simulation composite".  The "parent" simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

    """
    return {
        'type': 'class',
        'base': 'activity.numerical_activity',
        'is_abstract': False,
        'properties': [
            ('ensemble', 'activity.ensemble', '0.1'),
            ('ensemble_ids', 'shared.standard_name', '0.N'),
            ('simulation', 'activity.simulation', '0.1')
        ],
        'decodings': [
            ('ensemble', 'child::cim:ensemble/cim:ensemble'),
            ('ensemble', 'child::cim:ensemble/cim:reference', 'shared.doc_reference'),
            ('ensemble_ids', 'child::cim:ensembleMemberID'),
            ('simulation', 'child::cim:ensemble/cim:simulation'),
            ('simulation', 'child::cim:simulation/cim:reference', 'shared.doc_reference'),
        ]
    }


def experiment():
    """An experiment might be an activity which is both observational and numerical in focus, for example, a measurement campaign and numerical experiments for an alpine experiment.  It is a place for the scientific description of the reason why an experiment was made.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract': True,
        'properties': [
            ('measurement_campaigns', 'activity.measurement_campaign', '0.N'),
            ('requires', 'activity.numerical_activity', '0.N'),
            ('generates', 'str', '0.N'),
            ('supports', 'str', '0.N'),
        ],
    }


def experiment_relationship():
    """Contains a set of relationship types specific to a experiment document that can be used to describe its genealogy.

    """
    return {
        'type': 'class',
        'base': 'shared.relationship',
        'is_abstract': False,
        'properties': [
            ('target', 'activity.experiment_relationship_target', '1.1'),
            ('type', 'activity.experiment_relationship_type', '1.1'),
        ],
    }


def experiment_relationship_target():
    """Creates and returns instance of experiment_relationship_target class.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('numerical_experiment', 'activity.numerical_experiment', '0.1')
        ],
    }


def lateral_boundary_condition():
    """A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).

    """
    return {
        'type': 'class',
        'base': 'activity.numerical_requirement',
        'is_abstract': False,
        'constraints': [
            ('requirement_type', 'constant', 'lateralBoundaryCondition'),
        ]
    }


def measurement_campaign():
    """Creates and returns instance of measurement_campaign class.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract': False,
        'properties': [
            ('duration', 'int', '1.1'),
        ],
    }


def numerical_activity():
    """Creates and returns instance of numerical_activity class.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract': True,
        'properties': [
            ('description', 'str', '0.1'),
            ('long_name', 'str', '0.1'),
            ('short_name', 'str', '1.1'),
            ('supports', 'activity.experiment', '0.N'),
        ],
        'doc_strings': {
            'description': 'A free-text description of the experiment.',
            'long_name': 'The name of the experiment (that is recognized externally).',
            'short_name': 'The name of the experiment (that is used internally).'
        },
        'decodings': [
            ('description', 'child::cim:description'),
            ('long_name', 'child::cim:longName'),
            ('short_name', 'child::cim:shortName'),
            ('supports', 'child::cim:supports/cim:experiment'),
            ('supports', 'child::cim:supports/cim:reference', 'shared.doc_reference'),
        ]
    }


def numerical_experiment():
    """A numerical experiment may be generated by an experiment, in which case it is inSupportOf the experiment. But a numerical experiment may also exist as an activity in its own right (as it might be if it were needed for a MIP). Examples: AR4 individual experiments, AR5 individual experiments, RAPID THC experiments etc.

    """
    return {
        'type': 'class',
        'base': 'activity.experiment',
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('description', 'str', '0.1'),
            ('experiment_id', 'str', '0.1'),
            ('long_name', 'str', '0.1'),
            ('requirements', 'activity.numerical_requirement', '0.N'),
            ('short_name', 'str', '1.1'),
        ],
        'doc_strings': {
            'description': 'A free-text description of the experiment.',
            'experiment_id': 'An experiment ID takes the form <number>.<number>[-<letter>].',
            'long_name': 'The name of the experiment (that is recognized externally).',
            'requirements': 'The name of the experiment (that is used internally).',
            'short_name': 'The name of the experiment (that is used internally).',
        },
        'decodings': [
            ('meta', 'self::cim:numericalExperiment'),
            ('description', 'child::cim:description'),
            ('experiment_id', 'child::cim:experimentID'),
            ('long_name', 'child::cim:longName'),
            ('short_name', 'child::cim:shortName'),
            # Metafor CMIP5 questionnaire - standalone
            ('requirements', 'child::cim:numericalRequirement[@xsi:type="InitialCondition"]', 'activity.initial_condition'),
            ('requirements', 'child::cim:numericalRequirement[@xsi:type="BoundaryCondition"]', 'activity.boundary_condition'),
            ('requirements', 'child::cim:numericalRequirement[@xsi:type="LateralBoundaryCondition"]', 'activity.lateral_boundary_condition'),
            ('requirements', 'child::cim:numericalRequirement[@xsi:type="SpatioTemporalConstraint"]', 'activity.spatio_temporal_constraint'),
            ('requirements', 'child::cim:numericalRequirement[@xsi:type="OutputRequirement"]', 'activity.output_requirement'),
            # Metafor CMIP5 questionnaire - simulation bundle
            ('requirements', 'child::cim:numericalRequirement/cim:initialCondition', 'activity.initial_condition'),
            ('requirements', 'child::cim:numericalRequirement/cim:boundaryCondition', 'activity.boundary_condition'),
            ('requirements', 'child::cim:numericalRequirement/cim:lateralBoundaryCondition', 'activity.lateral_boundary_condition'),
            ('requirements', 'child::cim:numericalRequirement/cim:spatioTemporalConstraint', 'activity.spatio_temporal_constraint'),
            ('requirements', 'child::cim:numericalRequirement/cim:outputRequirement', 'activity.output_requirement'),
        ]
    }


def numerical_requirement():
    """A description of the requirements of particular experiments.  Numerical Requirements can be initial conditions, boundary conditions, or physical modificiations.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': True,
        'properties': [
            ('description', 'str', '0.1'),
            ('id', 'str', '0.1'),
            ('name', 'str', '1.1'),
            ('options', 'activity.numerical_requirement_option', '0.N'),
            ('requirement_type', 'str', '1.1'),
            ('source', 'shared.data_source', '0.1')
        ],
        'doc_strings': {
            'requirement_type': 'Type of reqirement to which the experiment must conform.',
        },
        'decodings': [
            ('description', 'child::cim:description'),
            ('id', 'child::cim:id'),
            ('name', 'child::cim:name'),
            ('options', 'child::cim:requirementOption'),
            ('source', 'child::cim:source/cim:source/cim:dataObject', 'data.data_object'),
            ('source', 'child::cim:source/cim:source/cim:dataContent', 'data.data_content'),
            ('source', 'child::cim:source/cim:source/cim:componentProperty', 'software.component_property'),
            ('source', 'child::cim:source/cim:source/cim:softwareComponent', 'software.model_component'),
            ('source', 'child::cim:source/cim:source/cim:softwareComponent', 'software.processor_component'),
            ('source', 'child::cim:source/cim:source/cim:softwareComponent', 'software.statistical_model_component'),
            ('source', 'child::cim:source/cim:reference', 'shared.doc_reference')
        ]
    }


def numerical_requirement_option():
    """A NumericalRequirement that is being used as a set of related requirements; For example if a requirement is to use 1 of 3 boundary conditions, then that "parent" requirement would have three "child" RequirmentOptions (each of one with the XOR optionRelationship).

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'str', '0.1'),
            ('id', 'str', '0.1'),
            ('name', 'str', '1.1'),
            ('sub_options', 'activity.numerical_requirement_option', '0.N'),
            ('relationship', 'str', '0.1'),
        ],
        'doc_strings': {
            'relationship': 'Describes how this optional (child) requirement is related to its sibling requirements.  For example, a NumericalRequirement could consist of a set of optional requirements each with an "OR" relationship meaning use this boundary condition _or_ that one.'
        },
        'decodings': [
            ('description', 'child::cim:description'),
            ('id', 'child::cim:id'),
            ('name', 'child::cim:name'),
            ('relationship', 'self::cim:requirementOption/@optionRelationship'),
            # Metafor CMIP5 questionnaire - simulation bundle
            ('description', 'child::cim:requirement/cim:requirement/cim:boundaryCondition/cim:description'),
            ('description', 'child::cim:requirement/cim:requirement/cim:initialCondition/cim:description'),
            ('description', 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition/cim:description'),
            ('description', 'child::cim:requirement/cim:requirement/cim:outputRequirement/cim:description'),
            ('description', 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint/cim:description'),
            # Metafor CMIP5 questionnaire - simulation bundle
            ('id', 'child::cim:requirement/cim:requirement/cim:boundaryCondition/cim:id'),
            ('id', 'child::cim:requirement/cim:requirement/cim:initialCondition/cim:id'),
            ('id', 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition/cim:id'),
            ('id', 'child::cim:requirement/cim:requirement/cim:outputRequirement/cim:id'),
            ('id', 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint/cim:id'),
            # Metafor CMIP5 questionnaire - simulation bundle
            ('name', 'child::cim:requirement/cim:requirement/cim:boundaryCondition/cim:name'),
            ('name', 'child::cim:requirement/cim:requirement/cim:initialCondition/cim:name'),
            ('name', 'child::cim:requirement/cim:requirement/cim:lateralBoundaryCondition/cim:name'),
            ('name', 'child::cim:requirement/cim:requirement/cim:outputRequirement/cim:name'),
            ('name', 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint/cim:name'),
        ]
    }


def boundary_condition():
    """A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).

    """
    return {
        'type': 'class',
        'base': 'activity.numerical_requirement',
        'is_abstract': False,
        'constraints': [
            ('requirement_type', 'constant', 'boundaryCondition'),
        ]
    }


def initial_condition():
    """An initial condition is a numerical requirement on a model prognostic variable value at time zero.

    """
    return {
        'type': 'class',
        'base': 'activity.numerical_requirement',
        'is_abstract': False,
        'constraints': [
            ('requirement_type', 'constant', 'initialCondition'),
        ]
    }


def spatio_temporal_constraint():
    """Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

    """
    return {
        'type': 'class',
        'base': 'activity.numerical_requirement',
        'is_abstract': False,
        'properties': [
            ('date_range', 'shared.date_range', '0.1'),
            ('spatial_resolution', 'activity.resolution_type', '0.1'),
        ],
        'constraints': [
            ('requirement_type', 'constant', 'spatioTemporalConstraint'),
        ],
        'decodings': [
            ('date_range', 'child::cim:requiredDuration/cim:closedDateRange', 'shared.closed_date_range'),
            ('date_range', 'child::cim:requiredDuration/cim:openDateRange', 'shared.open_date_range'),
            ('spatial_resolution', 'child::cim:spatialResolution'),
        ]
    }


def output_requirement():
    """Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

    """
    return {
        'type': 'class',
        'base': 'activity.numerical_requirement',
        'is_abstract': False,
        'constraints': [
            ('requirement_type', 'constant', 'outputRequirement'),
        ]
    }


def physical_modification():
    """Physical modification is the implementation of a boundary condition numerical requirement that is achieved within the model code rather than from some external source file. It  might include, for example,  a specific rate constant within a chemical reaction, or coefficient value(s) in a parameterisation.  For example, one might require a numerical experiment where specific chemical reactions were turned off - e.g. no heterogeneous chemistry.

    """
    return {
        'type': 'class',
        'base': 'activity.conformance',
        'is_abstract': False
    }


def simulation():
    """A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

    """
    return {
        'type': 'class',
        'base': 'activity.numerical_activity',
        'is_abstract': True,
        'properties': [
            ('authors', 'str', '0.1'),
            ('calendar', 'shared.calendar', '1.1'),
            ('control_simulation', 'activity.simulation', '0.1'),
            ('conformances', 'activity.conformance', '0.N'),
            ('deployments', 'software.deployment', '0.N'),
            ('inputs', 'software.coupling', '0.N'),
            ('outputs', 'data.data_object', '0.N'),
            ('restarts', 'data.data_object', '0.N'),
            ('simulation_id', 'str', '0.1'),
            ('spinup_date_range', 'shared.closed_date_range', '0.1'),
            ('spinup_simulation', 'activity.simulation', '0.1'),
        ],
        'doc_strings': {
            'authors': 'List of associated authors.',
            'control_simulation': 'Points to a simulation being used as the basis (control) run.  Note that only "derived" simulations can describe something as being control; a simulation should not know if it is being used itself as the control of some other run.',
            'inputs': 'Implemented as a mapping from a source to target; can be a forcing file, a boundary condition, etc.',
            'spinup_date_range': 'The date range that a simulation is engaged in spinup.',
            'spinup_simulation': 'The (external) simulation used during "spinup."  Note that this element can be used in conjuntion with spinupDateRange.  If a simulation has the latter but not the former, then one can assume that the simulation is performing its own spinup.',
        },
        'decodings': [
            ('calendar', 'child::cim:calendar/cim:daily-360', 'shared.daily_360'),
            ('calendar', 'child::cim:calendar/cim:perpetualPeriod', 'shared.perpetual_period'),
            ('calendar', 'child::cim:calendar/cim:realCalendar', 'shared.real_calendar'),
            ('authors', 'child::cim:authorsList/cim:list'),
            ('conformances', 'child::cim:conformance/cim:conformance', 'activity.conformance'),
            ('conformances', 'child::cim:conformance/cim:physicalModification', 'activity.physical_modification'),
            ('control_simulation', 'child::cim:controlSimulation/cim:controlSimulation'),
            ('control_simulation', 'child::cim:controlSimulation/cim:reference', 'shared.doc_reference'),
            ('deployments', 'child::cim:deployment'),
            ('inputs', 'child::cim:input'),
            ('simulation_id', 'child::cim:simulationID'),
            ('spinup_date_range', 'child::cim:dateRange/cim:closedDateRange'),
        ]
    }


def simulation_composite():
    """A SimulationComposite is an aggregation of Simulations. With the aggreation connector between Simulation and SimulationComposite(SC) the SC can be made up of both SimulationRuns and SCs. The SimulationComposite is the new name for the concept of SimulationCollection: A simulation can be made up of "child" simulations aggregated together to form a "simulation composite".  The "parent" simulation can be made up of whole or partial child simulations and the SimulationComposite attributes need to be able to capture this.

    """
    return {
        'type': 'class',
        'base': 'activity.simulation',
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('child', 'activity.simulation', '0.N'),
            ('date_range', 'shared.date_range', '1.1'),
            ('rank', 'int', '1.1'),
        ],
        'doc_strings': {
            'rank': 'Position of a simulation in the SimulationComposite timeline. eg:  Is this the first (rank = 1) or second (rank = 2) simulation'
        },
        'decodings': [
            ('meta', 'self::cim:simulationRun'),
            ('child', 'child::cim:child', 'activity.simulation_run'),
            ('child', 'child::cim:child', 'activity.simulation_composite'),
            ('date_range', 'child::cim:dateRange/cim:closedDateRange', 'shared.closed_date_range'),
            ('date_range', 'child::cim:dateRange/cim:openDateRange', 'shared.open_date_range'),
            ('rank', 'child::cim:rank'),
        ]
    }


def simulation_relationship():
    """Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

    """
    return {
        'type': 'class',
        'base': 'shared.relationship',
        'is_abstract': False,
        'properties': [
            ('target', 'activity.simulation_relationship_target', '1.1'),
            ('type', 'activity.simulation_relationship_type', '1.1'),
        ],
    }


def simulation_relationship_target():
    """Creates and returns instance of simulation_relationship_target class.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('simulation', 'shared.doc_reference', '0.1'),
            ('target', 'activity.simulation_type', '0.1')
        ],
    }


def simulation_run():
    """A SimulationRun is, as the name implies, one single model run. A SimulationRun is a Simulation. There is a one to one association between SimulationRun and (a top-level) SoftwarePackage::ModelComponent.

    """
    return {
        'type': 'class',
        'base': 'activity.simulation',
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('date_range', 'shared.date_range', '1.1'),
            ('model', 'software.model_component', '0.1')
        ],
        'decodings': [
            ('meta', 'self::cim:simulationRun'),
            ('date_range', 'child::cim:dateRange/cim:closedDateRange', 'shared.closed_date_range'),
            ('date_range', 'child::cim:dateRange/cim:openDateRange', 'shared.open_date_range'),
            ('model', 'child::cim:model/cim:modelComponent'),
            ('model', 'child::cim:model/cim:reference', 'shared.doc_reference')
        ]
    }
