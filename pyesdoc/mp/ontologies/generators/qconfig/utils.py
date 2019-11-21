"""
.. module:: pyesdoc.mp.ontologies.generators.qconfig.utils.py
   :platform: Unix, Windows
   :synopsis: helps generates qconfig file for CIM Ontology

.. moduleauthor:: Allyn Treshansky <allyn.treshansky@colorado.edu>

"""

# from esdoc_mp.ontologies.generators import generator_utils as gu
import os

QCONFIG_ATOMIC_PROPERTY_TYPE = "ATOMIC"
QCONFIG_ENUMERATION_PROPERTY_TYPE = "ENUMERATION"
QCONFIG_RELATIONSHIP_PROPERTY_TYPE = "RELATIONSHIP"

QCONFIG_ATOMIC_TYPE_MAP = {
    # TOOD: WHAT ABOUT 'email' AND 'time' ?
    "bool": "BOOLEAN",
    "date": "DATE",
    "datetime": "DATETIME",
    "float": "DECIMAL",
    "int": "INTEGER",
    "str": "STRING",
    "unicode": "STRING",
    "uri": "URL",
    "uuid": "STRING",
}

#############################################
# begin questionnaire-specific version code #
#############################################

# TODO: THIS CODE COMES FROM "esdoc-questionnaire.Q.questionnaire.q_utils.py" IN THE LONG-TERM I SHOULD USE IT DIRECTLY


class Version(object):

    N_BITS = (8, 8, 16)

    def __init__(self, string):
        self.integer = Version.string_to_int(string)
        self.string = string

    def __str__(self):
        return self.string

    def __int__(self):
        return self.integer

    def __eq__(self, other):
        if not other:
            return False

        if isinstance(other, basestring):
            return self == Version(other)
        else:
            return int(self) == int(other)

    def __gt__(self, other):
        if isinstance(other, basestring):
            other = Version(other)
        return int(self) > int(other)

    def __ge__(self, other):
        if isinstance(other, basestring):
            other = Version(other)
        return int(self) >= int(other)

    def __lt__(self, other):
        if isinstance(other, basestring):
            other = Version(other)
        return int(self) < int(other)

    def __le__(self, other):
        if isinstance(other, basestring):
            other = Version(other)
        return int(self) <= int(other)

    def major(self):
        string = str(self)
        numbers = [int(n) for n in string.split(".")]
        try:
            return numbers[0]
        except IndexError:
            return 0

    def minor(self):
        string = str(self)
        numbers = [int(n) for n in string.split(".")]
        try:
            return numbers[1]
        except IndexError:
            return 0

    def patch(self):
        string = str(self)
        numbers = [int(n) for n in string.split(".")]
        try:
            return numbers[2]
        except IndexError:
            return 0

    def fully_specified(self):
        return "{0}.{1}.{2}".format(
            self.major(),
            self.minor(),
            self.patch(),
        )

    @classmethod
    def string_to_int(cls, string):

        numbers = [int(n) for n in string.split(".")]

        if len(numbers) > len(cls.N_BITS):
            msg = "Versions with more than {0} decimal places are not supported".format(len(Version.N_BITS)-1)
            raise NotImplementedError(msg)

        #  add 0s for missing numbers
        numbers.extend([0] * (len(cls.N_BITS) - len(numbers)))

        #  convert to single int and return
        number = 0
        total_bits = 0
        for n, b in reversed(zip(numbers, cls.N_BITS)):
            max_num = (b+1) - 1
            if n >= 1 << max_num:
                msg = "Number {0} cannot be stored with only {1} bits. Max is {2}".format(n, b, max_num)
                raise ValueError(msg)
            number += n << total_bits
            total_bits += b

        return number

    @classmethod
    def int_to_string(cls, integer):
        number_strings = []
        total_bits = sum(cls.N_BITS)
        for b in Version.N_BITS:
            shift_amount = (total_bits - b)
            number_segment = integer >> shift_amount
            number_strings.append(str(number_segment))
            total_bits = total_bits - b
            integer = integer - (number_segment << shift_amount)

        return ".".join(number_strings)

###########################################
# end questionnaire-specific version code #
###########################################


def get_property_type(prop):
    prop_type = prop.type
    # TODO: ARE THERE FINER DISTINCTIONS HERE?
    # TODO: WHAT ABOUT "is_simple" AND "is_complex"?
    if prop_type.is_class:
        return QCONFIG_RELATIONSHIP_PROPERTY_TYPE
    elif prop_type.is_enum:
        return QCONFIG_ENUMERATION_PROPERTY_TYPE
    else:
        return QCONFIG_ATOMIC_PROPERTY_TYPE


def get_atomic_type(prop):
    assert get_property_type(prop) == QCONFIG_ATOMIC_PROPERTY_TYPE
    prop_type_name = prop.type.name_of_type
    try:
        return QCONFIG_ATOMIC_TYPE_MAP[prop_type_name]
    except KeyError:
        raise ValueError("Unable to locate '{0}' in ATOMIC TYPE MAP for {1}".format(prop_type_name, prop))


# def get_enumeration_target(prop):
#     assert get_property_type(prop) == QCONFIG_ATOMIC_PROPERTY_TYPE
#     prop_type = prop.type
#     return "{0}.{1}".format(
#         prop_type.name_of_package,
#         prop_type.name_of_type
#     )


def get_relationship_target_classes(prop):
    """
    Returns a list of all classes a property can point to
    (It is a list instead of a single instance b/c of the possibility of pointing to classes which have children)
    :param prop:
    :return:
    """
    assert get_property_type(prop) == QCONFIG_RELATIONSHIP_PROPERTY_TYPE
    relationship_target_classes = []
    target_class = prop.type.cls
    if not target_class.is_abstract:
        relationship_target_classes.append(target_class)
    relationship_target_classes += [
        # TODO: DOES target_class.sub_classes RETURN THE FULL HIERARCHY OF CHILDREN?
        # TODO: OR DO I NEED TO CHECK IF target_class IS IN bases OF ANY CONCRETE CLASS IN THE HIERARCHY?
        target_class for target_class in target_class.sub_classes
        if not target_class.is_abstract
    ]
    return relationship_target_classes


def get_ontology_name(name):
    """Converts name to an ontology name suitable for qconfig.

    Keyword Arguments:
    name - name being converted.

    """
    if isinstance(name, str) == False:
        name = name.name

    return name.lower()


def get_ontology_version(version):
    """Converts version identifier to a version suitable for the questionnaire

    Keyword Arguments:
    name - name of version identifier being converted.

    """
    if isinstance(version, str) == False:
        version = version.version

    q_version = Version(version)
    return q_version.fully_specified()


def get_ontology_key(ontology):
    return "{0}_{1}".format(
        get_ontology_name(ontology),
        get_ontology_version(ontology),
    )


def _get_ontology_directory(ctx, include_version=True):
    """
    Returns ontology directory into which code is generated.

    :param GeneratorContext ctx: Generation context information.
    :param bool include_version: should version info be included in the directory

    """
    _dir = ''
    if ctx.output_dir is not None:
        _dir += ctx.output_dir + '/'
    _dir += get_ontology_name(ctx.ontology)
    if include_version:
        # _dir += '/v' + get_ontology_version(ctx.ontology)
        _dir += "/v{0}".format(Version(ctx.ontology.version).major())
    return _dir


def _get_ontology_filename(ctx, include_version=True):
    """
    Returns ontology filename for generated code file

    :param GeneratorContext ctx: Generation context information.
    :param bool include_version: should version info be included in the filename
    :return:
    """
    ontology = ctx.ontology
    ontology_filename = get_ontology_name(ontology)
    if include_version:
        # ontology_filename += "_{0}".format(get_ontology_version(ontology).replace('.', '_'))
        version = Version(ontology.version).major()
        ontology_filename += "_{0}".format(version)
    ontology_filename += ".json"
    return ontology_filename


def get_ontology_path(ctx):
    """
    Returns full ontology path for generated QXML file

    :param GeneratorContext ctx: Generation context information.
    :return:
    """
    ontology_path = os.path.join(
        _get_ontology_directory(ctx, include_version=True),
        _get_ontology_filename(ctx, include_version=True)
    )
    return ontology_path
