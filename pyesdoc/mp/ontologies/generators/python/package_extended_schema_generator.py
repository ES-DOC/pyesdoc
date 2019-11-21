"""
.. module:: pyesdoc.mp.ontologies.generators.python.typeset_generator.py
   :platform: Unix, Windows
   :synopsis: Generates code encapsulating an ontology's typeset.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.mp.ontologies.generators.python import utils as pgu
from pyesdoc.mp.ontologies.generators.generator import Generator



class PackageExtendedSchemaGenerator(Generator):
    """Generates code to represent an ontology as a set of types.

    """
    def on_package_parse(self, ctx):
        """Event handler for the package parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        ctx.code.append(
            (
                ctx.get_code("extended_schema_for_package.tornado", pgu),
                pgu.get_ontology_directory(ctx),
                pgu.get_package_module_file_name(ctx.pkg, 'extended_schema')
            )
        )
