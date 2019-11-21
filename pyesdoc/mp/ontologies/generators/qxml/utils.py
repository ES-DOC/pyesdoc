"""Encapsualtes a set of qxml specific name conversion operations.

"""
import os

from pyesdoc.mp.ontologies.generators.generator_utils import *



# Language name constant.
LANGUAGE = 'qxml'

# Language file extension constant.
FILE_EXTENSION = '.xml'

# Set of simple type mappings.
_SIMPLE_TYPE_MAPPINGS = {
    # TODO: THE Q ALSO INCLUDES 'EMAIL' & 'TIME'
    # TODO: CIM2 IS SUPPOSED TO INCLUDE 'email'
    # TODO: CHECK THE STATUS OF THIS
    'bool' : 'BOOLEAN',
    'date' : 'DATE',
    'datetime' : 'DATETIME',
    'float' : 'DECIMAL',
    'int' : 'INTEGER',
    'str' : 'STRING',
    'unicode' : 'STRING',
    'uri' : 'URL',
    'uuid' : 'STRING',
}

QXML_ATOMIC_TYPE = "ATOMIC"
QXML_ENUMERATION_TYPE = "ENUMERATION"
QXML_RELATIONSHIP_TYPE = "RELATIONSHIP"


def _strip(name):
    """Returns stripped name.

    Keyword Arguments:
    name - name being converted.

    """
    if isinstance(name, str) == False:
        name = name.name
    return name


def _strip_class_name(name):
    """Returns stripped class name.

    Keyword Arguments:
    name - name being converted.

    """
    name = _strip(name)
    if name.find('.') != -1:
        name = name.split('.')[len(name.split('.')) - 1]
    return name


def get_ontology_name(name):
    """Converts name to an ontology name suitable for QXML.

    Keyword Arguments:
    name - name being converted.

    """
    if isinstance(name, str) == False:
        name = name.name

    return name.lower()


def get_ontology_version(name):
    """Converts version identifier to a version suitable for QXML.

    Keyword Arguments:
    name - name of version identifier being converted.

    """
    if isinstance(name, str) == False:
        name = name.version

    return name


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
        _dir += '/'
        _dir += 'v' + get_ontology_version(ctx.ontology)
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
        ontology_filename += "_{0}".format(get_ontology_version(ontology).replace('.', '_'))
    ontology_filename += ".xml"
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


def get_package_name(name):
    """Converts name to a package name suitable for QXML.

    :param str name: Package name being converted.

    """
    return _strip_package_name(name)


def get_full_class_name(c):
    """Converts name to a qualified class name.
    (This is only used for printing info via "format" below)

    :param str name: Class name being converted.

    """
    return get_package_name(c.package) + "." + get_class_name(c)


def get_class_name(name):
    """Converts name to a python class name.

    :param str name: Class name being converted.

    """
    return convert_to_camel_case(_strip_class_name(name))


def get_class_doc_string_name(name):
    """Converts name to one suitable for use in QXML documentation.

    :param str name: Class name being converted.

    """
    name = _strip_class_name(name)
    return name.replace('_', ' ')


def _get_class_base_name(c):
    """Converts name to a python base class name.

    """
    if c.base is None:
        return 'object'
    elif c.base.package == c.package:
        return get_class_name(c.base)
    else:
        return get_full_class_name(c.base)


def _strip_package_name(name):
    """Returns stripped package name.

    """
    name = _strip(name)
    if name.find('.') != -1:
        name = name.split('.')[0]
    return name


def get_qualified_enum_name(enum):
    """
    Returns qualified (ie: package + enum name) enumeration name.

    """
    if enum.package:
        return "{0}.{1}".format(enum.package, enum.name)
    else:
        return enum.name

def get_atomic_property_type(property):
    """
    returns the corresponding QXML atomic property type
    :param property: property
    :return: string
    """
    property_type = property.type
    property_type_name = property_type.name_of_type
    if property_type_name not in _SIMPLE_TYPE_MAPPINGS:
        # TODO: REMOVE THIS ONCE I'M SURE EVERYTHING WORKS
        raise ValueError("Unable to locate '{0}' in ATOMIC TYPE MAP for {1}".format(property_type, property))
    return _SIMPLE_TYPE_MAPPINGS[property_type_name]


def get_relationship_property_target(property):
    """
    Returns a QXML compatible name of the class that this property points to
    :param property:
    :return:
    """
    property_type = property.type
    property_type_name = property_type.name_of_type
    return property_type_name


def get_relationship_property_target_classes(property):
    """
    Returns a list of all classes this property can point to
    (It is a list instead of a single instance b/c of the possibility of pointing to classes which have children)
    :param property:
    :return:
    """
    property_type = property.type
    property_target_class = property_type.cls
    assert property_target_class is not None

    property_target_classes = []
    if not property_target_class.is_abstract:
        property_target_classes.append(property_target_class)

    concrete_classes = [cls for cls in property_type.ontology.classes if not cls.is_abstract]
    property_target_classes += [
        cls for cls in concrete_classes
        if property_target_class in cls.bases
    ]

    return property_target_classes


def get_property_type(property):
    """
    Returns the corresponding QXML property type
    :param property:
    :return:
    """
    property_type = property.type
    if property_type.is_class:
        return QXML_RELATIONSHIP_TYPE
    elif property_type.is_enum:
        return QXML_ENUMERATION_TYPE
    else:
        return QXML_ATOMIC_TYPE


def clean_xml_text(text):
    """
    escapes any non-xml-compatible text prior to adding it to an lxml element node
    (as per: http://stackoverflow.com/a/4181222)
    :param text: input text to clean
    :return: cleaned text to return
    """
    return text.decode('utf-8')


def format(o):
    """
    Configure ontology names.

    """
    o.op_name = get_ontology_name(o)
    o.op_version = get_ontology_version(o)

    for p in o.packages:
        p.op_name = get_package_name(p)

    for c in o.classes:
        c.op_base_name = _get_class_base_name(c)
        c.op_doc_string_name = get_class_doc_string_name(c)
        c.op_name = get_class_name(c)
        c.op_full_name = get_full_class_name(c)
