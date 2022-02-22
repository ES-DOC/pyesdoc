# -*- coding: utf-8 -*-

"""
.. module:: activity_classes.py
   :synopsis: Set of CIM v2 ontology type definitions
   which describe actions within an ES-DOC workflow.

"""


def activity():
    """Base class for activities."""
    return {
        "type": "class",
        "base": None,
        "is_abstract": True,
        "is_document": True,
        "pstr": ("{}", ("canonical_name",)),
        "properties": [
            (
                "alternative_names",
                "str",
                "0.N",
                "List of names by which the activity is also known.",
            ),
            (
                "canonical_name",
                "str",
                "0.1",
                "Community defined identifier or name.",
            ),
            (
                "citations",
                "linked_to(shared.citation)",
                "0.N",
                "Set of pertinent citations.",
            ),
            (
                "description",
                "str",
                "0.1",
                "Description of what is to be done (or was done).",
            ),
            (
                "duration",
                "time.time_period",
                "0.1",
                "Time the activity was (or will be) active.",
            ),
            (
                "internal_name",
                "str",
                "0.1",
                "A name used for internal purposes.",
            ),
            ("keywords", "str", "0.1", "User defined keywords."),
            ("long_name", "str", "0.1", "Longer version of activity name."),
            ("name", "str", "1.1", "Short name or abbreviation."),
            (
                "responsible_parties",
                "shared.responsibility",
                "0.N",
                "People or organisations responsible for activity.",
            ),
            (
                "previously_known_as",
                "str",
                "0.N",
                "List of names by which the activity was formerly known.",
            ),
            (
                "rationale",
                "str",
                "0.1",
                "Explanation of why this activity was carried out and/or what "
                "it was intended to achieve.",
            ),
        ],
    }


def axis_member():
    """Description of a given ensemble member.

    It will normally be related to a specific ensemble requirement. Note
    that start dates can be extracted directly from the simulations and
    do not need to be recorded with an axis member description.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            (
                "description",
                "str",
                "0.1",
                "Description of the member (or name of parameter varied).",
            ),
            (
                "extra_detail",
                "str",
                "0.1",
                "If necessary: further information about ensemble member "
                "conformance.",
            ),
            ("index", "int", "1.1", "The ensemble member index."),
            (
                "value",
                "float",
                "0.1",
                "If parameter varied; value for this member.",
            ),
            (
                "conformance",
                "linked_to(activity.conformance)",
                "0.1",
                "Conformance document for the target requirement that defines "
                "this member, if any.",
            ),
            (
                "axis",
                "linked_to(activity.ensemble_axis)",
                "1.1",
                "The parent axis of this ensemble member",
            ),
        ],
    }


def conformance():
    """A specific conformance.

    Describes how a particular numerical requirement has been
    implemented.  Will normally be linked from an ensemble descriptor.

    """
    return {
        "type": "class",
        "base": "activity.activity",
        "is_abstract": False,
        "properties": [
            (
                "conformance_achieved",
                "activity.conformance_type",
                "1.1",
                "Summary of conformance status.",
            ),
            (
                "datasets",
                "linked_to(data.dataset)",
                "0.N",
                "The datasets (including any modifications made to them) used "
                "for conforming to the target requirement.",
            ),
            # FIXME:
            # Should this be a URI of the target numerical requirement, or
            # a linked_to reference? Either the docstring, or the target
            # type is wrong.
            (
                "target_requirement",
                "linked_to(designing.numerical_requirement)",
                "1.1",
                "URI of the target numerical requirement.",
            ),
            (
                "models",
                "linked_to(science.model)",
                "1.N",
                "The models to which this conformance applies.",
            ),
        ],
        "constraints": [
            ("cardinality", "rationale", "0.0"),
            ("cardinality", "duration", "0.0"),
            ("cardinality", "canonical_name", "0.0"),
            ("cardinality", "keywords", "0.0"),
            ("cardinality", "description", "1.1"),
        ],
    }


def conformance_type():
    """Standardised set of conformance responses."""
    return {
        "type": "enum",
        "is_open": False,
        "members": [
            ("Conformed", "Simulation (or ensemble) conformed to requirement"),
            (
                "Partially Conformed",
                "Simulation (or ensemble) partially conformed to requirement "
                "- details in description",
            ),
            (
                "Not Conformed",
                "Simulation (or ensemble) was unable to conform to "
                "requirement",
            ),
            ("Not Applicable", "Requirement is not relevant"),
        ],
    }


def ensemble():
    """Generic ensemble definition.

    Holds the definition of how the various ensemble members have been
    configured. If ensemble axes are not present, then this is either a
    single member ensemble, or part of an uber ensemble.

    """
    return {
        "type": "class",
        "base": "activity.activity",
        "is_abstract": False,
        "properties": [
            (
                "common_conformances",
                "linked_to(activity.conformance)",
                "0.N",
                "Conformance documents for requirements common across "
                "ensemble.",
            ),
            (
                "representative_performance",
                "linked_to(platform.performance)",
                "0.1",
                "Representative model performance across ensemble.",
            ),
            (
                "documentation",
                "shared.online_resource",
                "0.N",
                "Links to web-pages and other ensemble specific documentation "
                "(including workflow descriptions).",
            ),
            (
                "ensemble_axes",
                "linked_to(activity.ensemble_axis)",
                "0.N",
                "Set of axes for the ensemble.",
            ),
            (
                "uber_ensembles",
                "linked_to(activity.uber_ensemble)",
                "0.N",
                "Link to one or more over-arching ensembles that might "
                "includes this one.",
            ),
            (
                "experiments",
                "linked_to(designing.numerical_experiment)",
                "1.N",
                "Experiments with which the ensemble is associated (may "
                "differ from constituent simulations).",
            ),
            (
                "members",
                "linked_to(activity.simulation)",
                "0.N",
                "Simulations within ensemble (should only be zero while "
                "ensemble is being defined)",
            ),
        ],
        "constraints": [
            ("cardinality", "rationale", "0.0"),
            ("cardinality", "canonical_name", "0.0"),
            ("cardinality", "keywords", "0.0"),
            ("cardinality", "duration", "0.0"),
        ],
    }


def ensemble_axis():
    """Defines the meaning of r/i/p indices in an ensemble."""
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "is_document": True,
        "pstr": ("{}", ("name",)),
        "properties": [
            ("name", "str", "1.1", "Short handle/name for the axis"),
            (
                "extra_detail",
                "str",
                "0.1",
                "Any extra detail required to describe how this ensemble axis "
                "was delivered.",
            ),
            (
                "members",
                "activity.axis_member",
                "0.N",
                "Individual member descriptions along axis. 0.N cardinality "
                "is only acceptable during design",
            ),
            (
                "short_identifier",
                "str",
                "1.1",
                "e.g. 'r', 'i', 'p' or 'f' to conform with simulation "
                "ensemble variant identifiers.",
            ),
            (
                "target_requirement",
                "linked_to(designing.numerical_requirement)",
                "0.1",
                "URI of the target numerical requirement, if any",
            ),
        ],
    }


def child_simulation():
    """Defines the relationship between a simulation and its parent."""
    return {
        "type": "class",
        "base": "activity.simulation",
        "is_abstract": False,
        "pstr": ("{}", ("parent",)),
        "properties": [
            (
                "branch_method",
                "str",
                "0.1",
                "Description of how the simulation was branched from a parent "
                "simulation, e.g. 'standard', 'none provided'.",
            ),
            (
                "branch_time_in_child",
                "time.date_time",
                "0.1",
                "The time at which the present simulation started in the "
                "child calendar.",
            ),
            (
                "branch_time_in_parent",
                "time.date_time",
                "0.1",
                "The time in parent simulation calendar at which this "
                "simulation was branched.",
            ),
            (
                "parent",
                "linked_to(activity.simulation)",
                "1.1",
                "The parent simulation of this child.",
            ),
        ],
    }


def simulation():

    """Simulation class provides the integrating link about what models
    were run and wny."""

    return {
        "type": "class",
        "base": "iso.process_step",
        "is_abstract": False,
        "is_document": True,
        "pstr": ("({}/{}/{})", ("used", "ran_for_experiments", "ensemble_id")),
        "properties": [
            (
                "part_of_project",
                "linked_to(designing.project)",
                "1.N",
                "Project or projects for which simulation was run",
            ),
            (
                "ran_for_experiments",
                "linked_to(designing.numerical_experiment)",
                "1.N",
                "One or more experiments with which the simulation is "
                "associated",
            ),
            (
                "sub_experiment",
                "linked_to(designing.numerical_experiment)",
                "0.1",
                "For start-date ensembles, this will indicate the beginning "
                "year; for offline models driven by output from another "
                "model, this will provide the source_id and variant_label "
                "for the 'driving' model.",
            ),
            (
                "used",
                "linked_to(science.model)",
                "1.1",
                "The model used to run the simulation",
            ),
            (
                "primary_ensemble",
                "linked_to(activity.ensemble)",
                "0.1",
                "Primary Ensemble (ensemble for which this simulation was "
                "first run).",
            ),
            (
                "institution",
                "linked_to(shared.party)",
                "0.1",
                "institution which carried out the simulation",
            ),
            (
                "parent_of",
                "linked_to(activity.child_simulation)",
                "0.N",
                "If appropriate, links to simulations which branched from "
                "this one",
            ),
            (
                "produced",
                "linked_to(data.dataset)",
                "0.N",
                "Products of the simulation",
            ),
            (
                "had_performance",
                "linked_to(platform.performance)",
                "0.1",
                "Performance of the simulation.",
            ),
            (
                "ran_on",
                "linked_to(platform.machine)",
                "0.1",
                "The machine on which the simulation was run.",
            ),
            (
                "errata",
                "shared.online_resource",
                "0.1",
                "Link to errata associated with this simulation.",
            ),
            (
                "ensemble_id",
                "activity.axis_member",
                "0.N",
                "Identification within ensemble axes via axis member. "
                "(Multiple axis members within a simulation cannot share the "
                "same ensemble_axis.) (There must be an axis_member instance "
                "for each ensemble axis in a parent ensemble.)",
            ),
            # Time
            (
                "start_time",
                "time.date_time",
                "0.1",
                "The start date-time of the simulation. e.g. "
                "2012-04-01 00:00:00",
            ),
            (
                "end_time",
                "time.date_time",
                "0.1",
                "The end date-time of the simulation. e.g. "
                "2087-11-30 12:00:00",
            ),
            (
                "calendar",
                "time.calendar",
                "0.1",
                "The calendar used in the simulation",
            ),
            # Further Info URL
            (
                "documentation",
                "shared.online_resource",
                "0.1",
                "On-line location of additional documentation",
            ),
            # Extra attributes
            (
                "extra_attributes",
                "shared.extra_attribute",
                "0.N",
                "Additional attributes provided with simulation.",
            ),
        ],
        "constraints": [
            ("cardinality", "rationale", "0.0"),
        ],
    }


def uber_ensemble():
    """An ensemble made up of other ensembles.

    Often used where parts of an ensemble were run by different
    institutes. Could also be used when a new experiment is designed
    which can use ensemble members from previous experiments and/or
    projects.

    """
    return {
        "type": "class",
        "base": "activity.ensemble",
        "is_abstract": False,
        "properties": [
            (
                "child_ensembles",
                "linked_to(activity.ensemble)",
                "1.N",
                "Ensemble which are aggregated into this one.",
            )
        ],
        "constraints": [
            ("cardinality", "ensemble_axes", "1.N"),
            ("cardinality", "common_conformances", "0.0"),
            ("cardinality", "members", "0.0"),
        ],
    }
