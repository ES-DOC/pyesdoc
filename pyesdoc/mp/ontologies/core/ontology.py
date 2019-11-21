"""
.. module:: pyesdoc.mp.ontologies.core.ontology
   :platform: Unix, Windows
   :synopsis: Represents an ontology definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from operator import add
from functools import reduce

from pyesdoc.mp.ontologies.core.class_ import Class
from pyesdoc.mp import utils



class Ontology(object):
    """Represents an ontology, i.e. a set of classes organised into packages.

    """
    def __init__(self, name, version, doc_string, packages):
        """Instance constructor.

        :param str name: Ontology name.
        :param str version: Ontology version.
        :param str doc_string: Ontology documentation string.
        :param iterable packages: Set of associated packages.

        """
        self.classes = reduce(add, [p.classes for p in packages])
        self.decodings = reduce(add, [p.decodings for p in packages])
        self.doc_string = doc_string
        self.entities = []
        self.enums = reduce(add, [p.enums for p in packages])
        self.enum_members = reduce(add, [e.members for e in self.enums])
        self.name = name
        self.op_name = None
        self.op_version = None
        self.packages = sorted(packages, key=lambda p: p.name)
        self.properties = reduce(add, [c.properties for c in self.classes])
        self.property_types = [p.type for p in self.properties]
        self.sub_classed = tuple()
        self.types = sorted(self.classes + self.enums)
        self.version = version

        # Set derived information.
        for setter in [
            _set_relations,
            _set_base_classes,
            _set_sub_classes,
            _set_entities,
            _set_property_type_info,
            _set_class_imports,
            _set_circular_imports,
            _set_associated_packages,
            _set_associated_packages_for_import,
            _set_package_external_type_refs,
            _set_collection_sort_orders,
        ]:
            setter(self)


    def __repr__(self):
        """Instance string representation.

        """
        return "{0} v{1}".format(self.name, self.version)


    def get_type(self, name):
        """Returns type with matching name.

        :param str name: Fully qualified name of target type.

        """
        pkg_name = name.split('.')[0]
        type_name = name.split('.')[1]
        for t in self.types:
            if t.package.name == pkg_name and t.name == type_name:
                return t


def _set_relations(ontology):
    """Sets relations between various nodes within an ontology.

    """
    for pkg in ontology.packages:
        pkg.ontology = ontology
        for cls in pkg.classes:
            cls.package = pkg
            for prp in cls.properties + cls.computed_properties + cls.constraints:
                prp.package = pkg
                prp.cls = cls
        for enum in pkg.enums:
            enum.package = pkg
            for enum_member in enum.members:
                enum_member.enum = enum


def _set_base_classes(ontology):
    """Sets base classes.

    """
    for cls in [c for c in ontology.classes if c.base]:
        base_cls = ontology.get_type(cls.base)
        if base_cls:
            cls.base = base_cls
        else:
            msg = "Base class not found :: class = {0}.{1} :: base = {2}"
            msg = msg.format(cls.package, cls, cls.base)
            utils.log(msg)


def _set_sub_classes(ontology):
    """Sets sub classes.

    """
    # Identify classes with a base class as these are potential targets.
    with_base = [c for c in ontology.classes if c.base]

    # Set sub-classed classes.
    sub_classed = {}
    for i in ontology.classes:
        sub_classed[i] = [(c.bases.index(i), c) for c in with_base if i in c.bases]
    sub_classed = {k: v for k, v in sub_classed.items() if v}

    # Set ontology & package sub-class sets.
    ontology.sub_classed = sorted(sub_classed.keys(), key=lambda i: str(i))
    for pkg in ontology.packages:
        pkg.sub_classed = [c for c in ontology.sub_classed if c.package == pkg]

    # Set sub-class hierachies.
    for i in sub_classed:
        depth = max([sc[0] for sc in sub_classed[i]]) + 1
        hierachy = {k: sorted(sc[1] for sc in sub_classed[i] if sc[0] == k) for k in range(depth)}
        i.sub_class_hierachy = [(level, hierachy[level]) for level in hierachy]
        i.sub_classes = [sc[1] for sc in sorted(sub_classed[i], key=lambda i: str(i))]


def _set_entities(ontology):
    """Sets package entities (i..e classes with a meta attribute).

    """
    for pkg in ontology.packages:
        pkg.entities = sorted([c for c in pkg.classes if c.is_entity])
        ontology.entities += pkg.entities


def _set_property_type_info(ontology):
    """Sets a property type information.

    """
    for pt in ontology.property_types:
        pt.cls = pt.package = None
        if pt.is_complex:
            type_ = ontology.get_type(pt.name)
            if type_ is not None:
                pt.is_class = isinstance(type_, Class)
                pt.ontology = ontology
                pt.package = type_.package
                pt.cls = type_


def _set_class_imports(ontology):
    """Assigns set of intra-class imports.

    """
    def _append(cls, pkg, type_):
        """Appends an import to the classes set of imports.

        """
        if pkg != cls.package.name or type_ != cls.name:
            cls.imports.append((pkg, type_))

    for cls in ontology.classes:
        if cls.base is not None:
            _append(cls, cls.base.package.name, cls.base.name)
        for p in [p for p in cls.properties if p.type.is_complex]:
            _append(cls, p.type.name_of_package, p.type.name_of_type)


def _set_circular_imports(ontology):
    """Assigns set of intra-class circular imports.

    """
    for c in ontology.classes:
        c_import = (c.package.name, c.name)
        for prp in [p for p in c.properties if p.type.is_class]:
            p_type = ontology.get_type(prp.type.name)
            if c_import in p_type.imports:
                p_type.imports.remove(c_import)
                p_type.circular_imports.append(c_import)


def _set_associated_packages(ontology):
    """Assigns set of intra-package associations.

    """
    for pkg in ontology.packages:
        pkg.associated += [c.base.package for c in pkg.classes if c.base and c.base.package != pkg]
        pkg.associated += [prp.type.package for prp in pkg.properties if prp.type.package and prp.type.package != pkg]
        pkg.associated = list(set(pkg.associated))


def _set_associated_packages_for_import(ontology):
    """Assigns set of intra-package associations required for import.

    """
    for pkg in ontology.packages:
        pkg.associated_for_import += [c.base.package for c in pkg.classes if c.base and c.base.package != pkg]
        pkg.associated_for_import += [prp.type.package for prp in pkg.properties if prp.type.package and prp.type.package != pkg and prp.name == "meta"]
        pkg.associated_for_import = list(set(pkg.associated_for_import))


def _set_package_external_type_refs(ontology):
    """Assigns set of a package's external type references so that .

    """
    for pkg in ontology.packages:
        for prp in pkg.properties:
            if prp.type.is_complex and \
               prp.type.name_of_package != pkg.name:
                pkg.external_types.append(prp.type)


def _set_collection_sort_orders(ontology):
    """Sets sort order of various collections.

    """
    ontology.classes = sorted(ontology.classes, key=str)
    ontology.enums = sorted(ontology.enums, key=str)
    ontology.types = sorted(ontology.types, key=str)
    ontology.enum_members = sorted(ontology.enum_members, key=str)
    ontology.entities = sorted(ontology.entities, key=str)
    ontology.properties = sorted(ontology.properties, key=str)
