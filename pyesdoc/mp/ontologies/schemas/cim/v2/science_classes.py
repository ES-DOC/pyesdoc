# -*- coding: utf-8 -*-

"""
.. module:: science_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""
def model():
    """A model component: can be executed standalone, and has as
    scientific description available via a link to a science.domain
    document. (A configured model can be understood in terms of a
    simulation, a model, and a configuration.).

    """
    return {
        'type': 'class',
        'base': 'software.component_base',
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('model_type', 'science.model_types', '1.1',
                "Generic type for this model."),
            ('key_properties', 'science.process', '0.1',
                "Model default key properties (may be over-ridden in coupled component and realm properties)."),
            ('realms', 'linked_to(science.realm)', '0.N',
                "The scientific realms which this model simulates internally, i.e. those which are not linked together using a coupler."),

            # TODO: review these attributes once software package is peer-reviewed
            ('coupled_components', 'linked_to(science.model)', '0.N',
                "Software components which are linked together using a coupler to deliver this model."),
            ('coupler', 'software.coupling_framework', '0.1',
                "Overarching coupling framework for model."),
            ('internal_software_components', 'software.software_component', '0.N',
                "Software modules which together provide the functionality for this model."),
        ]
    }


def realm():
    """Scientific area of a numerical model - usually a sub-model or component.

    """
    return {
        'type': 'class',
        'base': 'science.topic',
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('grid', 'science.process', '0.1',
                "The grid used to layout the variables (e.g. the Global ENDGAME-grid)."),
            ('key_properties', 'science.process', '0.1',
                "Realm key properties which differ from model defaults (grid, timestep etc)."),
            ('processes', 'science.process', '1.N',
                "Processes simulated within the realm."),

            ('realm_type', 'str', '0.1',
                "Canonical name for the realm."),
            ('software_frameworks', 'software.implementation', '0.N',
                "Software framework(s) of the realm."),
        ]
    }


def process():
    """Provides structure for description of a process simulated within a
    particular area (or domain/realm/component) of a model. This will
    often be subclassed within a specific implementation so that
    constraints can be used to ensure that the process details
    requested are consistent with project requirements for
    information.
    """
    return {
        'type': 'class',
        'base': 'science.topic',
        'is_abstract': False,
        'properties': [
            ('sub_processes', 'science.topic', '0.N',
                "Discrete portion of a process with common process details.")
        ]
}


def topic():
    """An organized collection of details upon a specific topic, e.g. model key properties.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('citations', 'shared.citation', '0.N',
                "Set of pertinent citations."),
            ('description', 'str', '0.1',
                "A description (possibly derived from specialization)."),
            ('keywords', 'str', '0.N',
                "Keywords to help re-use and discovery of this information."),
            ('overview', 'str', '0.1',
                "General implementation overview."),
            ('properties', 'science.topic_property', '1.N',
                "Set of associated specialized properties."),
            ('property_sets', 'science.topic_property_set', '1.N',
                "Set of associated specialized detail attributes."),
            ('responsible_parties', 'shared.responsibility', '0.N',
                "People or organisations responsible for providing this information."),
            ('short_name', 'str', '0.1',
                "A short-name / key (possibly derived from specialization)."),
            ('specialization_id', 'str', '0.1',
                "Specialization identifier (derived from specialization)."),
        ]
    }


def topic_property_set():
    """Provides specific details related to a topic (i.e. process, sub-process,
    grid, key properties, etc).

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'str', '0.1',
                "A description (possibly derived from specialization)."),
            ('properties', 'science.topic_property', '1.N',
                "Set of associated specialized properties."),
            ('short_name', 'str', '0.1',
                "A short-name / key (possibly derived from specialization)."),
            ('specialization_id', 'str', '0.1',
                "Specialization identifier (derived from specialization)."),
        ]
    }


def topic_property():
    """A specialized question asked of the scientic community.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('specialization_id', 'str', '0.1',
                "Specialization identifier (derived from specialization)."),
            ('value', 'str', '1.1',
                "User value."),
        ]
    }
