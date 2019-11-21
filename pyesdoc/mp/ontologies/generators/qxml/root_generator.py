"""
.. module:: pyesdoc.mp.ontologies.generators.qxml.root_generator.py
   :platform: Unix, Windows
   :synopsis: Generates root package initialisation code.

.. moduleauthor:: Allyn Treshansky <allyn.treshansky@noaa.gov>


"""
from pyesdoc.mp.ontologies.generators import generator_utils as gu
from pyesdoc.mp.ontologies.generators.generator import Generator
from pyesdoc.mp.ontologies.generators.qxml import utils as qgu

from lxml import etree as et
from functools import reduce
from errno import EEXIST as PATH_EXISTS
import datetime
import os

# Generator language.
_LANG = 'qxml'


class RootGenerator(Generator):
    """Generates root level packages.

    """
    def on_ontology_parse(self, ctx):
        """Event handler for the ontology parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        ontology = ctx.ontology

        name_node = et.Element("name")
        name_node.text = qgu.get_ontology_name(ontology)
        version_node = et.Element("version")
        version_node.text = qgu.get_ontology_version(ontology)
        classes_node = et.Element("classes")

        root_node = ctx.node
        root_node.append(name_node)
        root_node.append(version_node)
        root_node.append(classes_node)

    # QXML is a single construct; it is not separated into packages
    # def on_package_parse(self, ctx):
    #     pass

    def on_class_parse(self, ctx):
        """Event handler for the class parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        kls = ctx.cls

        if not kls.is_abstract:  # and not kls.is_document_meta:

            class_node = et.Element("class")

            is_meta_class = kls.is_document_meta
            class_node.set("is_meta", "true" if is_meta_class else "false")

            if kls.is_entity:
                class_node.set("stereotype", "document")

            class_node.set("package", ctx.pkg.name)
            class_name_node = et.Element("name")
            class_name_node.text = kls.name
            class_node.append(class_name_node)
            class_description_node = et.Element("description")
            class_description_node.text = qgu.clean_xml_text(kls.doc_string)
            class_node.append(class_description_node)

            class_label = kls.pstr
            if class_label is not None:
                class_label_node = et.Element("label")
                class_label_text_node = et.Element("text")
                class_label_text_node.text = class_label.text
                class_label_node.append(class_label_text_node)
                class_label_fields_node = et.Element("fields")
                for class_label_field in class_label.fields:
                    class_label_field_node = et.Element("field")
                    class_label_field_node.text = class_label_field
                    class_label_fields_node.append(class_label_field_node)
                class_label_node.append(class_label_fields_node)
                class_node.append(class_label_node)

            class_attributes_node = et.Element("attributes")
            all_attributes = kls.all_properties
            # non_meta_attributes = [a for a in all_attributes if not a.is_linked_document]
            for attribute in all_attributes:
                attribute_node = et.Element("attribute")
                is_meta_property = attribute.is_linked_document
                attribute_node.set("is_meta", "true" if is_meta_property else "false")
                attribute_node.set("package", attribute.package.name)
                attribute_node.set("is_nillable", "true" if attribute.min_occurs == '0' else "false")
                attribute_name_node = et.Element("name")
                attribute_name_node.text = attribute.name
                attribute_description_node = et.Element("description")
                attribute_description_node.text = qgu.clean_xml_text(attribute.doc_string)
                attribute_cardinality_node = et.Element("cardinality")
                attribute_cardinality_node.set("min", attribute.min_occurs)
                attribute_cardinality_node.set("max", attribute.max_occurs)

                attribute_type = qgu.get_property_type(attribute)
                attribute_type_node = et.Element("type")
                attribute_type_node.text = attribute_type

                attribute_node.append(attribute_name_node)
                attribute_node.append(attribute_description_node)
                attribute_node.append(attribute_cardinality_node)
                attribute_node.append(attribute_type_node)

                if attribute_type == qgu.QXML_ATOMIC_TYPE:
                    attribute_atomic_node = et.Element("atomic")
                    attribute_atomic_type_node = et.Element("atomic_type")
                    attribute_atomic_type_node.text = qgu.get_atomic_property_type(attribute)
                    attribute_atomic_node.append(attribute_atomic_type_node)
                    attribute_node.append(attribute_atomic_node)

                elif attribute_type == qgu.QXML_ENUMERATION_TYPE:
                    attribute_enumeration_node = et.Element("enumeration")
                    attribute_enumeration_node.set("enumeration_name", attribute.type.name)
                    # TODO: WORK OUT HOW "is_open" IS SET...
                    attribute_is_open = False
                    attribute_is_multi = attribute.max_occurs != '0'
                    attribute_enumeration_node.set("is_open", "true" if attribute_is_open else "false")
                    attribute_enumeration_node.set("is_multi", "true" if attribute_is_multi else "false")
                    attribute_choices_node = et.Element("choices")
                    # attribute_node is completed (ie: the choices are added) in the 'on_enum_parse' fn below...
                    # (that is why I record the fully-qualified "enumeration_name" XML attribute above)
                    attribute_enumeration_node.append(attribute_choices_node)
                    attribute_node.append(attribute_enumeration_node)

                elif attribute_type == qgu.QXML_RELATIONSHIP_TYPE:
                    attribute_relationship_node = et.Element("relationship")
                    attribute_relationship_targets_node = et.Element("targets")
                    attribute_relationship_targets = qgu.get_relationship_property_target_classes(attribute)
                    for attribute_relationship_target in attribute_relationship_targets:
                        attribute_relationship_target_node = et.Element("target")
                        attribute_relationship_target_node.text = "{0}.{1}".format(attribute_relationship_target.package, attribute_relationship_target.name)
                        attribute_relationship_targets_node.append(attribute_relationship_target_node)
                    attribute_relationship_node.append(attribute_relationship_targets_node)
                    attribute_node.append(attribute_relationship_node)

                class_attributes_node.append(attribute_node)

            class_node.append(class_attributes_node)

            classes_node = ctx.node.xpath("//classes")[0]
            classes_node.append(class_node)

    def on_enum_parse(self, ctx):
        """Event handler for the enum parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        return

        enum = ctx.enum
        enum_name = qgu.get_qualified_enum_name(enum)
        enum_choices = enum.members
        enum_xpath = "//attribute[enumeration/@enumeration_name='{0}']".format(enum_name)

        attribute_nodes = ctx.node.xpath(enum_xpath)
        for attribute_node in attribute_nodes:
            enumeration_choices_node = attribute_node.xpath("enumeration/choices")[0]

            for choice in enum_choices:
                enumeration_choice_node = et.Element("choice")
                choice_value = choice.name
                choice_description = qgu.clean_xml_text(choice.doc_string)
                enumeration_choice_value_node = et.Element("value")
                enumeration_choice_value_node.text = choice_value
                enumeration_choice_description_node = et.Element("description")
                if choice_description:
                    enumeration_choice_description_node.text = choice_description
                enumeration_choice_node.append(enumeration_choice_value_node)
                enumeration_choice_node.append(enumeration_choice_description_node)
                enumeration_choices_node.append(enumeration_choice_node)

    def on_start(self, ctx):
        """Event handler for the start parse event.

        :param GeneratorContext ctx: Generation context information.

        """

        root_node = et.Element("ontology")
        comment_node = et.Comment(" created by esdoc-mp ")
        root_node.append(comment_node)
        ctx.set_node(root_node)

    def on_end(self, ctx):
        """Event handler for the end parse event.

        :param GeneratorContext ctx: Generation context information.

        """

        output_filepath = qgu.get_ontology_path(ctx)
        if not os.path.exists(os.path.dirname(output_filepath)):
            try:
                os.makedirs(os.path.dirname(output_filepath))
            except OSError as error:  # handle race condition, as per http://stackoverflow.com/a/12517490
                if error.errno != PATH_EXISTS:
                    raise error
        with open(output_filepath, 'w') as f:
            qxml_content = et.tostring(ctx.node, pretty_print=True)
            f.write(qxml_content)
        f.closed
