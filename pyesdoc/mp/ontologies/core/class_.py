"""
.. module:: pyesdoc.mp.ontologies.core.class
   :platform: Unix, Windows
   :synopsis: Represents an ontological class definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import itertools
from collections import defaultdict

import constants


class Class(object):
    """Represents an ontological class definition.

    """
    def __init__(
        self,
        name,
        base,
        is_abstract,
        is_document,
        doc_string,
        properties,
        computed_properties,
        constraints,
        decodings,
        pstr = None
        ):
        """Instance constructor.

        :param str name: Class name.
        :param str base: Base class used in object hierarchies.
        :param bool is_abstract: Flag indicating whether this is an abstract class or not.
        :param bool is_document: Flag indicating whether this is a document or not.
        :param str doc_string: Class documentation string.
        :param list properties: Set of associated properties.
        :param list computed_properties: Set of associated computed properties.
        :param list constraints: Set of associated constraints.
        :param list decodings: Set of associated property decodings.
        :param ClassPrintString pstr: Class print string information.

        """
        self.base = base
        self.circular_imports = []
        self.cls = None
        self.computed_properties = sorted(computed_properties, key=lambda p: p.name)
        self.constraints = sorted(constraints, key=lambda ct: ct.property_name)
        self.decodings = sorted(decodings, key=lambda dc: dc.property_name)
        self.doc_string = doc_string if doc_string is not None else ''
        self.imports = []
        self.is_abstract = is_abstract
        self.is_document = is_document
        self.is_document_meta = name.endswith("doc_meta_info")
        self.name = name
        self.sub_class_hierachy = tuple()
        self.sub_classes = tuple()
        self.pstr = pstr
        self.op_base_name = None
        self.op_doc_string_name = None
        self.op_file_name = None
        self.op_full_name = None
        self.op_func_name = None
        self.op_import_name = None
        self.op_name = None
        self.properties = sorted(properties, key=lambda p: p.name)
        self.package = None


    def __repr__(self):
        """Instance string representation.

        """
        try:
            return "{}.{}".format(self.package, self.name)
        except:
            return self.name


    @property
    def is_entity(self):
        """Gets a flag indicating whether this class is considered an entity.

        """
        if self.is_document == True:
            return True
        if self.base:
            return self.base.is_entity
        return False


    @property
    def sub_class_hierachy_depth(self):
        """Gets depth of sub-class hierachy.

        """
        return len(self.sub_class_hierachy)


    @property
    def constants(self):
        """Gets collection of constant constraints.

        """
        return [(ct.property_name, ct.value) for ct in self.constraints
                if ct.typeof == constants.CONSTRAINT_TYPE_CONSTANT]


    @property
    def bases(self):
        """Gets collection of constant constraints.

        """
        if self.base:
            return (self.base, ) + self.base.bases
        return tuple()


    @property
    def all_constraints(self):
        """Gets all associated constraints including those of base class (sorted by name).

        Note that child constraints overrides parent constraints.

        """
        result = defaultdict(lambda: defaultdict(list))

        # Own constraints.
        for ct in self.constraints:
            if ct.property_name not in result[ct.typeof]:
                result[ct.typeof][ct.property_name] = (ct.property_name, ct.typeof, ct.value)

        # Base class(es) constraints.
        if self.base:
            for n, t, v in self.base.all_constraints:
                if n not in result[t]:
                    result[t][n] = (n, t, v)

        # Own properties converted to constraints.
        for p in self.all_properties:
            if p.name not in result['cardinality']:
                result['cardinality'][p.name] = (p.name, "cardinality", p.cardinality)
            if p.name not in result['type']:
                result['type'][p.name] = (p.name, "type", p.type)

        return list(itertools.chain.from_iterable([v.values() for v in result.values()]))


    @property
    def all_properties(self):
        """Gets all associated properties including those of base class (sorted by name).

        """
        if self.base:
            return self.properties + self.base.all_properties
        return self.properties


    @property
    def inherited_properties(self):
        """Gets properties inherited from base classes.

        """
        if self.base:
            return self.base.all_properties
        return []


    @property
    def all_computed_properties(self):
        """Gets all associated computed properties including those of base class (sorted by name).

        """
        if self.base:
            return self.computed_properties + self.base.all_computed_properties
        return self.computed_properties


    @property
    def all_decodings(self):
        """Gets class plus base class decodings.

        """
        if self.base:
            return self.decodings + self.base.all_decodings
        return self.decodings


    def get_property_decodings(self, prp):
        """Returns set of property decodings.

        :param pyesdoc.mp.ontologies.core.Property prp: A property being processed.

        """
        return [dc for dc in self.all_decodings if dc.property_name == prp.name]


    def get_property(self, name):
        """Recursively gets associated property either from self or from base class.

        :param str name: Name of a property.

        """
        for prp in self.properties:
            if prp.name == name:
                return prp
        if self.base:
            return self.base.get_property(name)

