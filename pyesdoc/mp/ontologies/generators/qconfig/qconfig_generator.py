# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.mp.ontologies.generators.qconfig.qconfig_generator.py
   :platform: Unix, Windows
   :synopsis: Generates qconfig file for an ES-DOC Questionnaire Ontology

.. moduleauthor:: Allyn Treshansky <allyn.treshansky@colorado.edu>

"""


from pyesdoc.mp.ontologies.generators import generator_utils as gu
from pyesdoc.mp.ontologies.generators.generator import Generator
from pyesdoc.mp.ontologies.generators.qconfig import utils as qgu

from collections import OrderedDict
from errno import EEXIST as PATH_EXISTS
import datetime
import json
import os


class QConfigGenerator(Generator):

    def on_start(self, ctx):
        """Event handler for the start parse event.

        :param GeneratorContext ctx: Generation context information.

        """

        qconfig = OrderedDict()
        ctx.qconfig = qconfig

    def on_end(self, ctx):
        """Event handler for the end parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        qconfig = ctx.qconfig
        output_filepath = qgu.get_ontology_path(ctx)
        if not os.path.exists(os.path.dirname(output_filepath)):
            try:
                os.makedirs(os.path.dirname(output_filepath))
            except OSError as error:  # handle race condition, as per http://stackoverflow.com/a/12517490
                if error.errno != PATH_EXISTS:
                    raise error
        with open(output_filepath, 'w') as f:
            json.dump(qconfig, f)
        f.closed

    def on_ontology_parse(self, ctx):
        """Event handler for the ontology parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        ontology = ctx.ontology
        qconfig = ctx.qconfig

        qconfig["name"] = ontology.name
        qconfig["version"] = qgu.get_ontology_version(ontology.version)
        qconfig["documentation"] = ontology.doc_string
        qconfig["ontology_type"] = "SCHEMA"
        # qconfig["ontology_base"] = no base for schemas
        qconfig["date"] = str(datetime.datetime.now())
        qconfig["classes"] = {
            "inherited": [],
            "excluded": [],
            "defined": [],
        }

    def on_class_parse(self, ctx):
        """Event handler for the class parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        cls = ctx.cls
        qconfig = ctx.qconfig
        qconfig_classes = qconfig["classes"]["defined"]

        if not cls.is_abstract:

            ontology_key = qgu.get_ontology_key(ctx.ontology)

            new_qconfig_class = OrderedDict()
            new_qconfig_class["name"] = cls.name
            new_qconfig_class["package"] = cls.package.name
            new_qconfig_class["documentation"] = cls.doc_string
            new_qconfig_class["is_document"] = cls.is_entity
            new_qconfig_class["is_meta"] = cls.is_document_meta

            class_id = getattr(
                cls,
                "id",
                "{0}.{1}.{2}".format(
                    ontology_key,
                    new_qconfig_class["package"],
                    new_qconfig_class["name"],
                )
            )
            new_qconfig_class["id"] = class_id

            potential_labels = [cls.pstr] + [b.pstr for b in cls.bases]
            for label in potential_labels:
                if label is not None:
                    new_qconfig_class["label"] = OrderedDict()
                    new_qconfig_class["label"]["text"] = label.text
                    new_qconfig_class["label"]["fields"] = []
                    for field in label.fields:
                        new_qconfig_class["label"]["fields"].append(field)
                    break  # stop as soon as you've found a label

            new_qconfig_class["categories"] = {
                "inherited": [],
                "excluded": [],
                "defined": [],
            }
            new_qconfig_class["properties"] = {
                "inherited": [],
                "excluded": [],
                "defined": [],
            }
            for prop in cls.all_properties:

                new_qconfig_property = OrderedDict()
                new_qconfig_property["name"] = prop.name
                # new_qconfig_property["package"] = prop.package.name
                new_qconfig_property["is_meta"] = prop.is_linked_document
                new_qconfig_property["documentation"] = prop.doc_string
                new_qconfig_property["cardinality"] = prop.cardinality
                new_qconfig_property["is_nillable"] = not prop.is_required

                property_id = getattr(prop, "id", None)
                if property_id is None:
                    property_id = "{0}.{1}".format(
                        class_id,
                        prop.name,
                    )
                new_qconfig_property["id"] = property_id

                property_type = qgu.get_property_type(prop)
                new_qconfig_property["property_type"] = property_type
                if property_type == qgu.QCONFIG_ATOMIC_PROPERTY_TYPE:
                    new_qconfig_property["atomic_type"] = qgu.get_atomic_type(prop)
                elif property_type == qgu.QCONFIG_ENUMERATION_PROPERTY_TYPE:
                    # enumeration_target is used as a placeholder for enumeration member values
                    # it is referenced in "on_enum_parse" below and then removed
                    new_qconfig_property["enumeration_target"] = "{0}.{1}".format(
                        prop.type.name_of_package,
                        prop.type.name_of_type
                    )
                    new_qconfig_property["enumeration_is_open"] = True  # TODO: HOW ARE OPEN ENUMERATIONS ENCODED?
                elif property_type == qgu.QCONFIG_RELATIONSHIP_PROPERTY_TYPE:
                    new_qconfig_property["relationship_targets"] = []
                    for relationship_target_class in qgu.get_relationship_target_classes(prop):
                        new_qconfig_property["relationship_targets"].append("{0}.{1}.{2}".format(
                            ontology_key,
                            relationship_target_class.package,
                            relationship_target_class.name
                        ))

                new_qconfig_class["properties"]["defined"].append(new_qconfig_property)

            qconfig_classes.append(new_qconfig_class)

    def on_enum_parse(self, ctx):
        """Event handler for the enum parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        enum = ctx.enum
        fully_qualified_enum_name = "{0}.{1}".format(enum.package.name, enum.name)
        qconfig = ctx.qconfig
        for qconfig_class in qconfig["classes"]["defined"]:
            for qconfig_property in qconfig_class["properties"]["defined"]:
                if qconfig_property["property_type"] == qgu.QCONFIG_ENUMERATION_PROPERTY_TYPE:
                    if "enumeration_target" in qconfig_property and qconfig_property["enumeration_target"] == fully_qualified_enum_name:
                        qconfig_property.pop("enumeration_target")
                        new_qconfig_enum_members = []
                        for i, member in enumerate(enum.members, start=1):
                            new_qconfig_enum_member = OrderedDict()
                            new_qconfig_enum_member["value"] = member.name
                            new_qconfig_enum_member["documentation"] = member.doc_string
                            new_qconfig_enum_member["order"] = i
                            new_qconfig_enum_members.append(new_qconfig_enum_member)
                        qconfig_property["enumeration_members"] = new_qconfig_enum_members
