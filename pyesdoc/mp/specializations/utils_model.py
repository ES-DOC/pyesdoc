# -*- coding: utf-8 -*-

"""
.. module:: model.py
   :platform: Unix, Windows
   :synopsis: A repesentation of CMIP6 specializations.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from itertools import chain

from utils_constants import *



class TopicSpecialization(object):
    """Wraps a topic specialization.

    """
    def __init__(self, spec, type_key):
        """Instance initializer.

        """
        self.authors = None
        self.contact = None
        self.contributors = None
        self.description = None
        self.id = None
        self.qc_status = None
        self.name = None
        self.parent = None
        self.properties = []
        self.property_sets = []
        self.spec = spec
        self.sub_topics = []
        self.type_key = type_key


    def __repr__(self):
        """Instance representation.

        """
        return self.id


    def __getitem__(self, type_key):
        """Returns a child topic.

        """
        result = [i for i in self.sub_topics if i.type_key == type_key]

        if type_key in {TYPE_KEY_PROCESS, TYPE_KEY_SUBPROCESS}:
            return result
        elif len(result) > 1:
            return result
        elif len(result) == 1:
            return result[0]


    @property
    def name_camel_case(self):
        """Gets camel case formatted name.

        """
        return _to_camel_case(self.name)


    @property
    def name_camel_case_spaced(self):
        """Gets spaced camel case formatted name.

        """
        return _to_camel_case_spaced(self.name)


    @property
    def all_topics(self):
        """Returns a flattened topic hierarchy.

        """
        def _get(container):
            result = [container]
            for topic in container.sub_topics:
                result += _get(topic)

            return result

        return _get(self)


    @property
    def all_property_containers(self):
        """Returns flattened list of all property containers, i.e. topics & proeprty-sets.

        """
        result = []
        for t in self.all_topics:
            result += [t] + t.property_sets

        return [i for i in result if i.properties]


    @property
    def all_sub_topics(self):
        """Returns a flattened topic hierarchy.

        """
        return self.all_topics[1:]


    @property
    def all_properties(self):
        """Returns all specialization properties.

        """
        return set(chain.from_iterable(i.properties for i in self.all_property_containers))


    @property
    def all_required_properties(self):
        """Returns all required specialization properties.

        """
        return set([i for i in self.all_properties if i.is_required])


    @property
    def all_optional_properties(self):
        """Returns all optional specialization properties.

        """
        return self.all_properties - self.all_required_properties


    @property
    def ENUMS(self):
        """Gets associated enumeration definitions.

        """
        try:
            return self.spec.ENUMERATIONS
        except AttributeError:
            try:
                return self.parent.spec.ENUMERATIONS
            except AttributeError:
                return []


    def names(self, offset=None, seperator=" --> ", convertor=None):
        """Returns set of topic names derived from topic specialization id.

        """
        if convertor is None:
            convertor = _to_camel_case_spaced
        names = self.id.split(".")
        if offset is not None:
            names = names[offset:]
        names = [convertor(i) for i in names]

        return seperator.join(names)


    def has_property(self, property_id):
        """Returns a flag indicating whether a topic supports a property.

        """
        for prop in self.all_properties:
            if prop.id == property_id:
                return True
        return False


class PropertySetSpecialization(object):
    """Wraps a property set specialization.

    """
    def __init__(self):
        """Instance initializer.

        """
        super(PropertySetSpecialization, self).__init__()

        self.description = None
        self.id = None
        self.name = None
        self.owner = None
        self.properties = []
        self.property_sets = []
        self.topic = None
        self.type_key = "property-set"


    def __repr__(self):
        """Instance representation.

        """
        return self.id


    @property
    def name_camel_case(self):
        """Gets camel case formatted name.

        """
        return _to_camel_case(self.name)


    @property
    def name_camel_case_spaced(self):
        """Gets spaced camel case formatted name.

        """
        return _to_camel_case_spaced(self.name)


    def names(self, offset=None, seperator=" --> ", convertor=None):
        """Returns set of topic names derived from topic specialization id.

        """
        if convertor is None:
            convertor = _to_camel_case_spaced
        names = self.id.split(".")
        if offset is not None:
            names = names[offset:]
        names = [convertor(i) for i in names]
        return seperator.join(names)


class PropertySpecialization(object):
    """Wraps a property specialization.

    """
    def __init__(self):
        """Instance initializer.

        """
        super(PropertySpecialization, self).__init__()

        self.cardinality = None
        self.description = None
        self.enum = None
        self.id = None
        self.name = None
        self.owner = None
        self.topic = None
        self.typeof = None
        self.type_key = "property"


    def __repr__(self):
        """Instance representation.

        """
        return self.id


    @property
    def name_camel_case(self):
        """Gets camel case formatted name.

        """
        return _to_camel_case(self.name)


    @property
    def name_camel_case_spaced(self):
        """Gets spaced camel case formatted name.

        """
        return _to_camel_case_spaced(self.name)


    @property
    def long_name(self):
        """Returns long name derived from id.

        """
        return _get_long_name(self.id, offset=3)


    @property
    def is_required(self):
        """Gets flag indicating whether cardinality is mandatory or not.

        """
        return self.cardinality.split(".")[0] != "0"


    @property
    def is_collection(self):
        """Gets flag indicating whether property is a collection or not.

        """
        try:
            int(self.cardinality.split(".")[1])
        except ValueError:
            return True
        return False


    @property
    def typeof_label(self):
        """Gets label for the property type.

        """
        if self.typeof == 'str':
            return "STRING"
        elif self.typeof == 'bool':
            return "BOOLEAN"
        elif self.typeof == 'int':
            return "INTEGER"
        elif self.typeof == 'float':
            return "FLOAT"
        elif self.enum:
            return "ENUM"
        return self.typeof.split(":")[-1].upper()


    @property
    def root_topic(self):
        """Returns a properties root topic.

        """
        result = self.owner
        while len(result.id.split('.')) != 3:
            try:
                result = result.owner
            except AttributeError:
                result = result.parent

        return result


    def validate_value(self, val):
        """Validates a property value.

        :param object val: Value to be validated.

        """
        if self.enum:
            self.enum.validate_value(val)

        if self.typeof == 'str':
            if not isinstance(val, basestring) or not len(val.strip()):
                raise ValueError("Invalid value: must be a non zero length string")

        if self.typeof == 'bool':
            if not isinstance(val, bool):
                raise ValueError("Invalid value: must be a boolean")

        if self.typeof == 'int':
            if not isinstance(val, int):
                raise ValueError("Invalid value: must be an integer")

        if self.typeof == 'float':
            if not isinstance(val, float):
                raise ValueError("Invalid value: must be a float")


class EnumSpecialization(object):
    """Wraps an enumeration specialization.

    """
    def __init__(self):
        """Instance initializer.

        """
        self.choices = []
        self.description = None
        self.id = None
        self.is_open = False
        self.label = None
        self.name = None
        self.type_key = "enum"


    def __repr__(self):
        """Instance representation.

        """
        return self.id


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(self.choices)


    def is_a_member(self, val):
        """Returns flag indicating whether vlue is a member of the enumeration.

        :param object val: Value to be validated.

        """
        return val in [i.value for i in self.choices]


    def validate_value(self, val):
        """Validates a value against the set of enum choices.

        :param object val: Value to be validated.

        """
        if not isinstance(val, basestring) or not len(val.strip()):
            raise ValueError("Invalid value: must be a non zero length string")
        if self.is_a_member(val):
            return
        if not self.is_open:
            raise ValueError("Invalid value: is not an enumeration member")
        if not val.startswith("Other: "):
            raise ValueError("Invalid value: new enumeration members must be prefixed with: 'Other: '")
        other = val.split("Other: ")[-1]
        if self.is_a_member(other):
            raise ValueError("Invalid value: enumeration member already defined")


class EnumChoiceSpecialization(object):
    """Wraps an enumeration choice specialization.

    """
    def __init__(self):
        """Instance initializer.

        """
        self.description = None
        self.enum = None
        self.id = None
        self.value = None
        self.type_key = "enum-choice"

        self.is_other = False


    def __repr__(self):
        """Instance representation.

        """
        return self.id


class ShortTable(object):
    """Wraps s short-table, i.e. a grouped subset of specializations.

    """
    def __init__(self):
        """Instance initializer.

        """
        self.authors = []
        self.change_history = []
        self.contact = None
        self.contributors = []
        self.groups = []
        self.label = None
        self.name = None
        self.qc_status = None


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(self.groups)


class ShortTableGroup(object):
    """Wraps a grouped set of specializations related to a short table.

    """
    def __init__(self):
        """Instance initializer.

        """
        self.name = None
        self.identifiers = []


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(self.identifiers)


def _to_camel_case_spaced(name, separator='_'):
    """Converts passed name to camel case with space.

    :param str name: A name as specified in ontology specification.
    :param str separator: Separator to use in order to split name into constituent parts.

    """
    if name is None:
        return ''

    r = [_to_camel_case(i, separator) for i in name.split(separator)]

    return ' '.join(r)


def _to_camel_case(name, separator='_'):
    """Converts passed name to camel case.

    :param str name: A name as specified in ontology specification.
    :param str separator: Separator to use in order to split name into constituent parts.

    """
    if name is None:
        return ''

    r = ''
    for s in name.split(separator):
        if len(s) == 0:
            continue
        r += s[0].upper()
        if (len(s) > 1):
            r += s[1:]

    return r


def _get_long_name(identifier, offset=None, seperator=" --> ", convertor=None):
    """Returns long name derived from an identifier.

    """
    if convertor is None:
        convertor = _to_camel_case_spaced
    names = identifier.split(".")
    if offset is not None:
        names = names[offset:]
    names = [convertor(i) for i in names]

    return seperator.join(names)
