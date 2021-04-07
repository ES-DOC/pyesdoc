"""
.. module:: utils_factory.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Takes specialization modules and returns instances of wrapper classes.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from utils import log
from utils_cache import set_specialization as cache_specialization
from utils_constants import *
from utils_model import EnumSpecialization
from utils_model import EnumChoiceSpecialization
from utils_model import PropertySetSpecialization
from utils_model import PropertySpecialization
from utils_model import ShortTable
from utils_model import ShortTableProperty
from utils_model import TopicSpecialization



def get_specialization(modules):
    """Returns a specialization wrapper.

    :param modules: 4 member tuple of python modules: root, grid, key-properties, processes.

    :returns: A specialization wrapper.
    :rtype: TopicSpecialization

    """
    # Create root topic.
    root = _create_topic(modules[0], None)

    # Create sub-topics.
    for module in modules[1:]:
        _create_topic(module, root)

    return root


create_specializations = get_specialization


def _create_topic(spec, parent, key=None):
    """Creates & returns a topic specialization.

    """
    if spec is None:
        return None

    # Hydrate either from a dictionary or a module.
    topic = TopicSpecialization(spec, parent)
    if isinstance(spec, dict):
        _set_topic_from_dict(topic, parent, key)
    else:
        _set_topic_from_module(topic, parent)

    # Set injected properties.
    _set_topic_injected_properties(topic)

    # Cache.
    cache_specialization(topic)

    return topic


def _set_topic_injected_properties(topic):
    """Injects a set of properties into the set of specializations.

    """
    # Model properties.
    if len(topic.path) == 3 and topic.path[1] == 'toplevel' and topic.path[2] == 'key_properties':
        if not topic.has_property('overview'):
            description = 'Top level overview of coupled model'
            _set_injected_property('overview', 'l-str', '1.1', description, topic)

        if not topic.has_property('keywords'):
            description = 'Keywords associated with coupled model'
            _set_injected_property('keywords', 'cs-str', '1.1', description, topic)

        if not topic.has_property('name'):
            description = 'Name of coupled model'
            _set_injected_property('name', 'str', '1.1', description, topic)

    # Topic key properties.
    elif len(topic.path) == 3 and topic.path[2] == 'key_properties':
        if not topic.has_property('overview'):
            description = 'Overview of {} model.'.format(topic.root.name)
            _set_injected_property('overview', 'l-str', '1.1', description, topic)

        if not topic.has_property('keywords'):
            description = 'Keywords associated with {} model code'.format(topic.root.name)
            _set_injected_property('keywords', 'cs-str', '1.1', description, topic)

        if not topic.has_property('name'):
            description = 'Name of {} model code'.format(topic.root.name)
            _set_injected_property('name', 'str', '1.1', description, topic)

    # Topic grid properties.
    elif len(topic.path) == 3 and topic.path[-1] == 'grid':
        if not topic.has_property('overview'):
            description = 'Overview of grid in {} model.'.format(topic.root.name)
            _set_injected_property('overview', 'l-str', '0.1', description, topic)

        if not topic.has_property('name'):
            description = 'Name of grid in {} model.'.format(topic.root.name)
            _set_injected_property('name', 'str', '0.1', description, topic)

    # Topic process properties.
    elif len(topic.path) == 3:
        if not topic.has_property('overview'):
            description = 'Overview of {} in {} model.'.format(topic.description.lower(), topic.root.name)
            _set_injected_property('overview', 'l-str', '0.1', description, topic)

        if not topic.has_property('name'):
            description = 'Commonly used name for the {} in {} model.'.format(topic.name_camel_case_spaced.lower(), topic.root.name)
            _set_injected_property('name', 'str', '0.1', description, topic)

    # Topic sub-process properties.
    elif len(topic.path) == 4:
        pass
        # if not topic.has_property('overview'):
        #     description = 'Overview of {} in {} model.'.format(topic.description.lower(), topic.root.name)
        #     _set_injected_property('overview', 'str', '0.1', description, topic)


def _set_injected_property(name, typeof, cardinality, description, topic):
    """Injects a property into the set of specializations.

    """
    try:
        enums = topic.spec.ENUMERATIONS
    except AttributeError:
        enums = topic.parent.spec.ENUMERATIONS
    _set_property(name, typeof, cardinality, description, topic, enums, False, True)


def _set_topic_from_module(topic, parent):
    """Set topic specialization attributes from a module.

    """
    try:
        topic.authors = topic.spec.AUTHORS
    except AttributeError:
        topic.authors = topic.root.authors
    try:
        topic.contact = topic.spec.CONTACT
    except AttributeError:
        topic.contact = topic.root.contact
    topic.description = topic.spec.DESCRIPTION
    if parent:
        topic.change_history = parent.change_history
        topic.contributors = parent.contributors
        topic.name = "_".join(topic.spec.__name__.split(".")[-1].split("_")[1:])
        topic.id = "{}.{}".format(parent.id, topic.name)
    else:
        topic.change_history = topic.spec.CHANGE_HISTORY
        topic.contributors = topic.spec.CONTRIBUTORS
        topic.name = topic.spec.__name__
        topic.id = "{}.{}".format(topic.spec.__file__.split("/")[-2], topic.name)

    # Assign properties / property sets.
    if hasattr(topic.spec, "DETAILS") and hasattr(topic.spec, "ENUMERATIONS"):
        for key, obj in topic.spec.DETAILS.items():
            # ... toplevel properties
            if key == "toplevel":
                _set_property_collection(topic, obj, topic.spec.ENUMERATIONS)

            # ... toplevel property sets
            elif key.startswith("toplevel"):
                _set_property_set(topic, key, obj, topic.spec.ENUMERATIONS)

            # ... sub-topic properties
            elif len(key.split(":")) == 1:
                # Create sub-sub-processes.
                _create_topic(obj, topic, key)
                _set_property_collection(topic.sub_topics[-1], obj, topic.spec.ENUMERATIONS)

            # ... sub-topic property sets
            elif len(key.split(":")) == 2:
                for st in topic.sub_topics:
                    if st.name == key.split(":")[0]:
                        _set_property_set(st, key, obj, topic.spec.ENUMERATIONS)


def _set_topic_from_dict(topic, parent, name):
    """Set topic specialization attributes from a dictionary.

    """
    topic.authors = parent.authors
    topic.contact = parent.contact
    topic.change_history = parent.change_history
    topic.contributors = parent.contributors
    topic.description = topic.spec['description']
    topic.id = "{}.{}".format(parent.id, name)
    topic.name = name


def _set_property_set(owner, key, obj, enumerations):
    """Set attributes of a property-set attributes from a dictionary.

    """
    ps = PropertySetSpecialization()
    ps.description = obj['description']
    ps.id = "{}.{}".format(owner.id, key.split(":")[-1])
    ps.key = key
    ps.name = key.split(":")[-1]
    ps.owner = owner
    _set_property_collection(ps, obj, enumerations)

    owner.property_sets.append(ps)

    # Cache.
    cache_specialization(ps)


def _set_property_collection(owner, obj, enumerations):
    """Set a collection of topic properties from a dictionary.

    """
    for name, typeof, cardinality, description in obj.get('properties', []):
        _set_property(name, typeof, cardinality, description, owner, enumerations, True, False)


def _set_property(name, typeof, cardinality, description, owner, enumerations, append, was_injected):
    """Returns a topic property.

    """
    p = PropertySpecialization()
    p.cardinality = cardinality
    p.description = description
    p.enum = _create_enum(p, typeof, enumerations) if typeof.startswith("ENUM:") else None
    p.id = "{}.{}".format(owner.id, name)
    p.was_injected = was_injected
    p.key = name
    p.name = name
    p.owner = owner
    p.typeof = typeof

    if append == True:
        owner.properties.append(p)
    else:
        owner.properties.insert(0, p)

    # Cache.
    cache_specialization(p)

    # Log injected.
    # if was_injected:
    #     log('injected property: {}'.format(p.id))

    return p


def _create_enum(detail, typeof, enumerations):
    """Creates & returns an enumeration specialzation wrapper.

    """
    key = typeof.split(":")[-1]
    obj = enumerations[key]

    e = EnumSpecialization()
    e.description = obj['description']
    e.detail = detail
    e.id = "{}.{}".format(detail.id, key)
    e.is_open = obj['is_open']
    e.label = key
    e.name = key
    e.id = key
    e.choices = [_create_enum_choice(e, i[0], i[1]) for i in obj.get('members', [])]

    return e


def _create_enum_choice(enum, value, description):
    """Creates & returns an enumeration choice specialzation wrapper.

    """
    ec = EnumChoiceSpecialization()
    ec.description = description
    ec.enum = enum
    ec.id = "{}.{}".format(enum.id, value)
    ec.value = value

    return ec


def get_short_tables(tables):
    """Returns a set of short table wrappers.

    :param tables: 2 member tuple: name, dict.

    :returns: A specialization wrapper.
    :rtype: tuple

    """
    return [_get_short_table(i, j) for i, j in tables]


create_short_tables = get_short_tables


def _get_short_table(name, obj):
    """Creates & returns a short-table wrapper.

    """
    result = ShortTable()
    result.authors = obj['AUTHORS']
    result.change_history = obj['CHANGE_HISTORY']
    result.contact = obj['CONTACT']
    result.contributors = obj['CONTRIBUTORS']
    result.label = obj['LABEL']
    result.name = name
    result.properties = [_get_short_table_property(i) for i in obj['PROPERTIES']]

    return result


def _get_short_table_property(obj):
    """Returns a short table property wrapper.

    :param modules: 4 member tuple of python modules: root, grid, key-properties, processes.

    :returns: A specialization wrapper.
    :rtype: tuple

    """
    result = ShortTableProperty()
    result.identifier = obj[0]
    result.priority = obj[1]

    return result
