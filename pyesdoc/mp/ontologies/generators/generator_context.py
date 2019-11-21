"""
.. module:: pyesdoc.mp.ontologies.generators.generator_context
   :platform: Unix, Windows
   :synopsis: Encpasulates contextual information used by generators.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os

import tornado



# Cache of tornado template loaders.
_TEMPLATE_LOADERS = {}

# Cache of loaded tornado templates.
_TEMPLATE_CACHE = {}


class GeneratorContext(object):
    """Encpasulates contextual information passed to generators.

    :ivar generator: Generator being executed.
    :ivar ontology: Ontology being processed.
    :ivar language: Language of generation, e.g. python.
    :ivar io_dir: Directory to which output will be written.

    """
    def __init__(self, generator, ontology, language, io_dir):
        """Instance constructor.

        """
        self.generator = generator
        self.language = language
        self.output_dir = io_dir
        self.key = generator if isinstance(generator, str) else generator.__name__
        self.ontology = ontology
        self.pkg = None
        self.cls = None
        self.enum = None
        self.code = []


    def set_package(self, pkg):
        """Sets current package being processed.

        :param pyesdoc.mp.ontologies.core.Package pkg: An ontology package being processed.

        """
        self.pkg = pkg
        self.cls = None
        self.enum = None


    def set_class(self, cls):
        """Sets current class type being processed.

        :param pyesdoc.mp.ontologies.core.Class cls: An ontology class being processed.

        """
        self.pkg = cls.package
        self.cls = cls
        self.enum = None


    def set_enum(self, enum):
        """Sets current enumerated type being processed.

        :param pyesdoc.mp.ontologies.core.Enum enum: An ontology enum being processed.

        """
        self.pkg = enum.package
        self.cls = None
        self.enum = enum


    def set_node(self, node):
        """Sets current node being processed.

        :param lxml.Element node: An XML node

        """
        # TODO: CONSIDER MOVING THIS FUNCTIONALITY TO THE pyesdoc.mp.ontologies.generators.qxml PACKAGE
        self.node = node


    def get_code(self, template, lu):
        """Generates code from a template.

        :param str template: Name of a template file.
        :module lu: Lanaugage specific utility functions passed to template.

        """
        # Set the template loader.
        template_dir = "{}/{}/templates".format(os.path.dirname(__file__), self.language)
        if template_dir not in _TEMPLATE_LOADERS:
            _TEMPLATE_LOADERS[template_dir] = tornado.template.Loader(template_dir)
        template_loader = _TEMPLATE_LOADERS[template_dir]

        # Load template & return generated code.
        template = template_loader.load(template)

        return template.generate(
            o=self.ontology,
            pkg=self.pkg,
            cls=self.cls,
            enum=self.enum,
            escape=lambda s: s.strip().replace('"', "'"),
            lu=lu
            )
