"""
.. module:: factory.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Takes specialization modules and returns instances of wrapper classes.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from utils_constants import *
import utils_model as model



# Map of specializations by id.
CACHE = dict()


def get_short_tables(tables):
    """Returns a set of short table wrappers.

    :param modules: 4 member tuple of python modules: root, grid, key-properties, processes.

    :returns: A specialization wrapper.
    :rtype: tuple

    """
    return [_get_short_table(i, j) for i, j in tables]


def _get_short_table(name, obj):
    """Creates & returns a short-table wrapper.

    """
    result = model.ShortTable()
    result.authors = obj['AUTHORS']
    result.change_history = obj['CHANGE_HISTORY']
    result.contact = obj['CONTACT']
    result.contributors = obj['CONTRIBUTORS']
    result.label = obj.get('LABEL', name)
    result.name = name
    result.qc_status = obj['QC_STATUS']
    result.groups = [_get_short_table_group(i, j) for i, j in obj['PROPERTIES'].items()]

    return result


def _get_short_table_group(key, identifiers):
    """Creates & returns a short-table group wrapper.

    """
    result = model.ShortTableGroup()
    result.name = key
    result.identifiers = identifiers

    return result

def get_specialization(modules):
    """Returns a specialization wrapper.

    :param modules: 4 member tuple of python modules: root, grid, key-properties, processes.

    :returns: A specialization wrapper.
    :rtype: tuple

    """
    # Unpack modules.
    mod_root, mod_grid, mod_keyprops, mod_processes = modules

    # Set root type key.
    type_key = TYPE_KEY_REALM if mod_root.__name__ != "model" else TYPE_KEY_MODEL

    # Create topic tree.
    result = _create_topic(None, mod_root, type_key)
    if mod_grid is not None:
        _create_topic(result, mod_grid, TYPE_KEY_GRID)
    _create_topic(result, mod_keyprops, TYPE_KEY_KEYPROPS)
    for i in mod_processes:
        _create_topic(result, i, TYPE_KEY_PROCESS)

    return result


def _create_topic(parent, spec, type_key, key=None):
    """Creates & returns a topic specialization wrapper.

    """
    if spec is None:
        return None

    # Instantiate.
    topic = model.TopicSpecialization(spec, type_key)
    if isinstance(spec, dict):
        _set_topic_from_dict(parent, topic, key)
    else:
        _set_topic_from_module(parent, topic)

    # Update hierachy.
    if parent:
        topic.parent = parent
        parent.sub_topics.append(topic)

    # Cache (used in downstream tooling chain).
    CACHE[topic.id] = topic

    return topic


def _set_topic_from_module(parent, topic):
    """Set topic specialization attributes from a module.

    """
    topic.authors = topic.spec.AUTHORS
    topic.contact = topic.spec.CONTACT
    topic.qc_status = topic.spec.QC_STATUS
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
        topic.id = "cmip6.{}".format(topic.name)

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
                _create_topic(topic, obj, TYPE_KEY_SUBPROCESS, key)
                _set_property_collection(topic.sub_topics[-1], obj, topic.spec.ENUMERATIONS)

            # ... sub-topic property sets
            elif len(key.split(":")) == 2:
                for st in topic.sub_topics:
                    if st.name == key.split(":")[0]:
                        _set_property_set(st, key, obj, topic.spec.ENUMERATIONS)


def _set_topic_from_dict(parent, topic, name):
    """Set topic specialization attributes from a dictionary.

    """
    topic.authors = parent.authors
    topic.contact = parent.contact
    topic.change_history = parent.change_history
    topic.contributors = parent.contributors
    topic.description = topic.spec['description']
    topic.id = "{}.{}".format(parent.id, name)
    topic.name = name
    topic.qc_status = parent.qc_status


def _set_property_set(owner, key, obj, enumerations):
    """Set attributes of a property-set attributes from a dictionary.

    """
    ps = model.PropertySetSpecialization()
    ps.description = obj['description']
    ps.id = "{}.{}".format(owner.id, key.split(":")[-1])
    ps.key = key
    ps.name = key.split(":")[-1]
    ps.owner = owner
    _set_property_collection(ps, obj, enumerations)

    owner.property_sets.append(ps)

    # Cache.
    CACHE[ps.id] = ps


def _set_property_collection(owner, obj, enumerations):
    """Set a collection of topic properties from a dictionary.

    """
    for name, typeof, cardinality, description in obj.get('properties', []):
        p = model.PropertySpecialization()
        p.cardinality = cardinality
        p.description = description
        p.enum = _create_enum(p, typeof, enumerations) if typeof.startswith("ENUM:") else None
        p.id = "{}.{}".format(owner.id, name)
        p.key = name
        p.name = name
        p.owner = owner
        p.typeof = typeof

        owner.properties.append(p)

        # Cache.
        CACHE[p.id] = p


def _create_enum(detail, typeof, enumerations):
    """Creates & returns an enumeration specialzation wrapper.

    """
    key = typeof.split(":")[-1]
    obj = enumerations[key]

    e = model.EnumSpecialization()
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
    ec = model.EnumChoiceSpecialization()
    ec.description = description
    ec.enum = enum
    ec.id = "{}.{}".format(enum.id, value)
    ec.value = value

    return ec
