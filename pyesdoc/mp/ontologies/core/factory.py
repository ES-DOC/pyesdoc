"""
.. module:: pyesdoc.mp.utils.factory
   :platform: Unix, Windows
   :synopsis: Encapsulates process of instantiating objects, i.e. generators, schemas and ontologies.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import inspect
import re

from pyesdoc.mp.ontologies.core import Class
from pyesdoc.mp.ontologies.core import ClassConstraint
from pyesdoc.mp.ontologies.core import ClassPrintString
from pyesdoc.mp.ontologies.core import ComputedProperty
from pyesdoc.mp.ontologies.core import Decoding
from pyesdoc.mp.ontologies.core import Enum
from pyesdoc.mp.ontologies.core import EnumMember
from pyesdoc.mp.ontologies.core import Ontology
from pyesdoc.mp.ontologies.core import Package
from pyesdoc.mp.ontologies.core import Property



# Comutation element reg-ex.
_RE_COMPUTED_ELEMENT = '^[a-z]+$'


def _get_functions(modules):
    """Returns a collection of function pointers declared within a module.

    """
    try:
        iter(modules)
    except TypeError:
        modules = [modules]

    result = set()
    for module in modules:
        result.update({m[1] for m in inspect.getmembers(module) if inspect.isfunction(m[1])})

    return result


def _get_type_definitions(modules):
    """Returns set of type definitions instantiated from a set of modules.

    """
    def _get_definition(func):
        """Returns a type definition."""
        result = func()
        result['name'] = func.__name__
        result['doc'] = func.__doc__.strip()

        return result

    return [_get_definition(i) for i in _get_functions(modules)]


def _get_package_definitions(schema):
    """Returns set of package definitions.

    """
    def _get_definition(func):
        """Returns a package definition.

        """
        defn = {
            'name': func.__name__,
            'doc': func.__doc__.strip(),
            'types': func()
        }

        return defn

    return [_get_definition(f) for f in _get_functions(schema)]


def _get_class_properties(class_):
    """Returns class property definitions.

    """
    result = []
    doc_strings = class_.get('doc_strings', dict())
    for prop in class_.get('properties', []):
        if len(prop) == 4:
            name, type_name, cardinality, doc_string = prop
        elif len(prop) == 3:
            name, type_name, cardinality = prop
            doc_string = doc_strings.get(name, None)
        result.append(Property(name, type_name, cardinality, doc_string))
    if class_.get('is_document', False):
        result.append(Property('meta', 'shared.doc_meta_info', '1.1', "Injected document metadata."))

    return result


def _get_class_computed_properties(class_):
    """Returns class computed property definitions.

    """
    def get_computation(computation):
        """Returns parsed computation statement.

        """
        return " ".join(["self.{}".format(e) if re.match(_RE_COMPUTED_ELEMENT, e[0]) else e 
                        for e in computation.split(" ")])

    return [ComputedProperty(name, get_computation(computation)) for name, computation in
            class_.get('derived', []) + class_.get('computed', [])]


def _get_class_constraints(class_):
    """Returns class constraint definitions.

    """
    def get_constraint(defn):
        """Returns parsed computation statement.

        """
        property_name, typeof, value = defn

        return ClassConstraint(property_name, typeof, value)

    return [get_constraint(defn) for defn in class_.get('constraints', [])]


def _get_class_decodings(class_):
    """Returns class decoding definitions.

    """
    result = []
    for decoding in class_.get('decodings', []):
        result.append(Decoding(decoding[0],
                               decoding[1],
                               None if len(decoding) == 2 else decoding[2]))

    return result


def _get_class_pstr(class_):
    """Returns class decoding definitions.

    """
    pstr = class_.get('pstr')
    if pstr:
        return ClassPrintString(pstr[0], pstr[1])


def _get_package_classes(schema, package, types):
    """Returns package class definitions.

    """
    result = []
    for cls in [t for t in types if t['type'] == 'class']:
        result.append(
            Class(cls['name'],
                  cls.get('base', None),
                  cls.get('is_abstract', False),
                  cls.get('is_document', False),
                  cls.get('doc', None),
                  _get_class_properties(cls),
                  _get_class_computed_properties(cls),
                  _get_class_constraints(cls),
                  _get_class_decodings(cls),
                  _get_class_pstr(cls)
                  )
        )

    return result


def _get_package_enums(schema, package, types):
    """Returns package enum definitions.

    """
    result = []
    for enum in [t for t in types if t['type'] == 'enum']:
        result.append(
            Enum(enum['name'],
                 enum.get('is_open', True),
                 enum.get('doc', None),
                 [EnumMember(m[0], m[1]) for m in enum.get('members', [])])
            )

    return result


def _get_package_types(schema, package):
    """Returns package type definitions.

    """
    types = _get_type_definitions(package.get('types', []))

    return _get_package_classes(schema, package, types), \
           _get_package_enums(schema, package, types)


def _get_ontology_packages(schema):
    """Returns ontology package definitions.

    """
    result = []
    for package in _get_package_definitions(schema):
        classes, enums = _get_package_types(schema, package)
        result.append(
            Package(package['name'],
                    package['doc'],
                    classes,
                    enums
                    )
            )

    return result


def create_ontology(schema):
    """Factory method to instantiate an ontology instance from a schema declaration.

    :param module schema: An ontology schema declaration.

    :returns: An ontology declaration.
    :rtype: pyesdoc.mp.ontologies.core.Ontology

    """
    return Ontology(schema.NAME,
                    schema.VERSION,
                    schema.DOC,
                    _get_ontology_packages(schema))
