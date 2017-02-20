"""
.. module:: pyesdoc.mp.ontologies.generators.__init__.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: pyesdoc.mp generators sub-package initializer.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os

from pyesdoc.mp import utils
from pyesdoc.mp.ontologies.core.factory import create_ontology
from pyesdoc.mp.ontologies.core.schema_validation import validate as validate_schema
from pyesdoc.mp.ontologies.generators import generator_utils as gu
from pyesdoc.mp.ontologies.generators import python
from pyesdoc.mp.ontologies.generators import qxml
from pyesdoc.mp.ontologies.generators import qconfig
from pyesdoc.mp.ontologies.generators.generator_context import GeneratorContext


# Map of generator handlers.
_HANDLERS = { i.__name__.split('.')[-1]: i for i in (python, qxml, qconfig) }


def _log_start(schema, language, io_dir):
    """Informs user that generation is about to begin.

    """
    utils.log("Welcome to the ES-DOC meta-programming code generator !")
    utils.log("GENERATION OPTION : ontology schema = {0} v{1}".format(schema.NAME, schema.VERSION))
    utils.log("GENERATION OPTION : programming language = {0}".format(language))
    utils.log("GENERATION OPTION : output directory = {0}".format(io_dir))


def _log_end():
    """Informs user that generation is complete.

    """
    utils.log("Thank you for using the ES-DOC code generator")


def _can_generate(schema, language, output_dir):
    """Verifies whether the generation options are in a state such that generation can occur.

    :param module schema: Ontology schema definition.
    :param str language: Target programming language.
    :param str io_dir: Target I/O directory.

    :returns: True if generation can occur, False otherwise.
    :rtype: bool

    """
    if not language in _HANDLERS:
        err = "Programming language is unsupported [{}].  Supported languages are {}."
        err = err.format(language, _HANDLERS.keys())
        raise ValueError(err)
    if not os.path.exists(output_dir):
        raise IOError("Output directory does not exist [{0}].".format(output_dir))

    errors = validate_schema(schema)
    if errors:
        utils.log("-------------------------------------------------------------------")
        for error in errors:
            utils.log("VALIDATION ERROR :: {0}".format(error))
        return False

    return True


def _generate_from_template(ctx, template):
    """Generates code from a tornado template.

    """
    lu = _HANDLERS[ctx.language].UTILS
    utils.log("GENERATOR = {0} :: generation begins".format(ctx.key))
    code = ctx.get_code(template, lu)
    if code:
        gu.write_file(gu.format_code(ctx, code),
                      lu.get_ontology_directory(ctx),
                      lu.get_module_file_name(template.split('.')[0]))
    utils.log("GENERATOR = {0} :: generation complete".format(ctx.key))


def _generate_from_parser(ctx, parser_type):
    """Generates code from an ontology parser.

    """
    parser = parser_type()
    if not parser.is_required(ctx):
        utils.log("GENERATOR = {0} :: generation skipped".format(ctx.key))
    else:
        utils.log("GENERATOR = {0} :: generation begins".format(ctx.key))
        parser.execute(ctx)
        for code, dir_, fpath in ctx.code:
            gu.write_file(gu.format_code(ctx, code), dir_, fpath)
        utils.log("GENERATOR = {0} :: generation complete".format(ctx.key))


def generate(schema, language, io_dir):
    """Generates code.

    :param module schema: Ontology schema definition.
    :param str language: Target programming language.
    :param str io_dir: Target I/O directory.

    """
    if not _can_generate(schema, language, io_dir):
        return

    _log_start(schema, language, io_dir)

    # Initialise ontology.
    ontology = create_ontology(schema)
    utils.log("ONTOLOGY :: {0} (packages={1}, classes={2}, enums={3})".format(
        ontology, len(ontology.packages), len(ontology.classes), len(ontology.enums)))

    # Apply language specific pre-generator formatter.
    try:
        formatter = _HANDLERS[language].UTILS.format
    except AttributeError:
        pass
    else:
        formatter(ontology)
        utils.log("ONTOLOGY :: formatted for {0}".format(language))

    # Invoke language specific generators.
    for generator in _HANDLERS[language].GENERATORS:
        func = _generate_from_template if isinstance(generator, str) else _generate_from_parser
        func(GeneratorContext(generator, ontology, language, io_dir), generator)

    _log_end()

