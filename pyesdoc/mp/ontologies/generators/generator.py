"""
.. module:: pyesdoc.mp.ontologies.generators.generator
   :platform: Unix, Windows
   :synopsis: Base class encapsulating functionality common to all cim code generators.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from abc import ABCMeta

from pyesdoc.mp.ontologies.generators import generator_utils as gu



class Generator(object):
    """Base class encapsulating functionality common to all code generators.

    """
    # Abstract Base Class module - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def execute(self, ctx):
        """Executes the code generator.

        :param pyesdoc.mp.ontologies.core.Ontology ontology: Ontology being processed.

        """
        # Escape if not required.
        if not self.is_required(ctx):
            return

        # Notify start.
        self.on_start(ctx)

        # Raise parsing events and emit code accordingly.
        self.on_ontology_parse(ctx)
        for pkg in ctx.ontology.packages:
            ctx.set_package(pkg)
            self.on_package_parse(ctx)
        for cls in ctx.ontology.classes:
            ctx.set_class(cls)
            self.on_class_parse(ctx)
        for enum in ctx.ontology.enums:
            ctx.set_enum(enum)
            self.on_enum_parse(ctx)

        # Notify end.
        self.on_end(ctx)


    def _write_code(self, ctx, code):
        """Writes generated code to file system.

        """
        if code:
            for code, dir_, fpath in code:
                gu.write_file(gu.format_code(ctx, code), dir_, fpath)


    def is_required(self, ctx):
        """Predicate determing whether code generation is actually required.

        """
        return True


    def on_start(self, ctx):
        """Event handler for the parsing start event.

        :param pyesdoc.mp.ontologies.generators.generator.GeneratorContext ctx: Generation context information.

        """
        pass


    def on_end(self, ctx):
        """Event handler for the parsing end event.

        :param pyesdoc.mp.ontologies.generators.generator.GeneratorContext ctx: Generation context information.

        """
        pass


    def on_ontology_parse(self, ctx):
        """Event handler for the ontology parse event.

        :param pyesdoc.mp.ontologies.generators.generator.GeneratorContext ctx: Generation context information.

        """
        pass


    def on_package_parse(self, ctx):
        """Event handler for the package parse event.

        :param pyesdoc.mp.ontologies.generators.generator.GeneratorContext ctx: Generation context information.

        """
        pass


    def on_class_parse(self, ctx):
        """Event handler for the class parse event.

        :param pyesdoc.mp.ontologies.generators.generator.GeneratorContext ctx: Generation context information.

        """
        pass


    def on_enum_parse(self, ctx):
        """Event handler for the enum parse event.

        :param pyesdoc.mp.ontologies.generators.generator.GeneratorContext ctx: Generation context information.

        """
        pass
