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
        # TODO: review whether science.topic works better.
        'base': 'software.component_base',
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('keywords', 'str', '0.N',
                "Keywords to help re-use and discovery of this information."),
            ('model_type', 'science.model_types', '1.1',
                "Generic type for this model."),
            ('key_properties', 'science.topic', '0.1',
                "Model default key properties (may be over-ridden in coupled component and realm properties)."),
            ('activity_properties', 'science.topic', '0.N',
                "Properties specific to the modelling activity in question, e.g. radiative forcing agents for CMIP6."),
            ('realms', 'linked_to(science.realm)', '0.N',
                "The scientific realms which this model simulates internally, i.e. those which are not linked together using a coupler."),
            ('realm_coupling', 'science.realm_coupling', '0.N',
                "Description of a coupling between realms"),

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
        'pstr': ('{}', ('canonical_name',)),
        'properties': [
            ('canonical_name', 'str', '0.1',
                "Canonical name for the realm."),
            ('grid', 'science.topic', '0.1',
                "The grid used to layout the variables (e.g. the Global ENDGAME-grid)."),
            ('key_properties', 'science.topic', '0.1',
                "Realm key properties which differ from model defaults (grid, timestep etc)."),
            ('processes', 'science.topic', '1.N',
                "Processes simulated within the realm."),

            # TODO: review these attributes once software package is peer-reviewed
            ('software_frameworks', 'software.implementation', '0.N',
                "Software framework(s) of the realm."),
        ]
    }

def realm_coupling():
    """Description of a coupling between realms.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('variable', 'str', '1.1',
                 'The variable being coupled (e.g. 10 metre wind)'),
            ('source_realm', 'str', '1.1',
                 'The model realm providing the variable (e.g. ocean)'),
            ('target_realm', 'str', '1.1',
                 'The model realm receiving the variable (e.g. atmosphere)'),
            ('time_frequency', 'int', '1.1',
                 'The time frequency of the coupling (in seconds)'),
            ('coupling_details', 'str', '0.1',
                 'Description of the coupling algorithm, coupler settings, and any other information (e.g. binlinear interpolation')
        ]
    }

def topic():
    """An organized collection of details upon a specific topic, e.g. model key properties.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('{}', ('short_name',)),
        'properties': [
            ('citations', 'shared.citation', '0.N',
                "Set of pertinent citations."),
            ('description', 'str', '0.1',
                "A description (derived from specialization)."),
            ('keywords', 'str', '0.N',
                "Keywords to help re-use and discovery of this information."),
            ('name', 'str', '0.1',
                "A short-name / key (derived from specialization)."),
            ('overview', 'str', '0.1',
                "An overview of topic being described."),
            ('properties', 'science.topic_property', '0.N',
                "Set of associated specialized properties."),
            ('property_sets', 'science.topic_property_set', '0.N',
                "Grouped specialized properties."),
            ('qc_status', 'int', '0.1',
                "Quality control status of topic."),
            ('responsible_parties', 'shared.responsibility', '0.N',
                "People or organisations responsible for providing this information."),
            ('specialization_id', 'str', '1.1',
                "Specialization identifier (derived from specialization)."),
            ('sub_topics', 'science.topic', '0.N',
                "Discrete sub-topic with details.")
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
        'pstr': ('{}', ('specialization_id',)),
        'properties': [
            ('description', 'str', '0.1',
                "A description (derived from specialization)."),
            ('properties', 'science.topic_property', '1.N',
                "Set of associated specialized properties."),
            ('name', 'str', '0.1',
                "A short-name / key (derived from specialization)."),
            ('specialization_id', 'str', '1.1',
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
        'pstr': ('{}: {}', ('specialization_id', 'values',)),
        'properties': [
            ('description', 'str', '0.1',
                "User friendly description (derived from specialization)."),
            ('name', 'str', '0.1',
                "A short-name / key (derived from specialization)."),
            ('specialization_id', 'str', '1.1',
                "Specialization identifier (derived from specialization)."),
            ('values', 'str', '1.N',
                "User value(s)."),
        ]
    }
