"""
.. module:: pyesdoc.mp.ontologies.generators.python.serialization_generator.py
   :platform: Unix, Windows
   :synopsis: Generates code to support serialization.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from operator import add

from pyesdoc.mp.ontologies.generators import generator_utils as gu
from pyesdoc.mp.ontologies.generators.generator import Generator
from pyesdoc.mp.ontologies.generators.python import utils as pgu



# Generator language.
_LANG = 'python'

# Template for main module.
_TEMPLATE_MAIN = "decoder.txt"

# Template for a decoder module.
_TEMPLATE_DECODER_MODULE = 'decoder_module.txt'

# Template for a decoder function.
_TEMPLATE_DECODER_FUNCTION = "decoder_function.txt"

# Template for a decoding xml utilities.
_TEMPLATE_DECODER_XML_UTILS = "decoder_xml_utils.txt"

# Loaded templates.
_TEMPLATES = gu.load_templates(_LANG, (
    _TEMPLATE_MAIN,
    _TEMPLATE_DECODER_MODULE,
    _TEMPLATE_DECODER_FUNCTION,
    _TEMPLATE_DECODER_XML_UTILS,
))



class DecoderGenerator(Generator):
    """Generates code to support decoding.

    """
    def is_required(self, ctx):
        """Predicate determing whether code generation is required.

        :param GeneratorContext ctx: Generation context information.

        """
        return bool(ctx.ontology.decodings)


    def on_ontology_parse(self, ctx):
        """Event handler for the ontology parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        ctx.code.append(
            (
                _emit_module_init(ctx.ontology),
                pgu.get_ontology_directory(ctx),
                pgu.get_module_file_name('decoder')
            )
        )
        ctx.code.append(
            (
                _TEMPLATES[_TEMPLATE_DECODER_XML_UTILS],
                pgu.get_ontology_directory(ctx),
                pgu.get_module_file_name('decoder_xml_utils')
            )
        )


    def on_package_parse(self, ctx):
        """Event handler for the package parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        ctx.code.append(
            (
                _emit_module_decoder_for_pkg(ctx.ontology, ctx.pkg),
                pgu.get_ontology_directory(ctx),
                pgu.get_package_module_file_name(ctx.pkg, 'decoder')
            )
        )


def _emit_module_decoder_for_pkg(o, p):
    """Emits package decoder module."""
    code = _TEMPLATES[_TEMPLATE_DECODER_MODULE]
    code = code.replace('{module-imports}', _emit_snippet_decoder_imports(o, p))
    code = code.replace('{decoding-functions}', _emit_snippet_decoding_fns(p))

    return code


def _emit_snippet_decoder_imports(o, p):
    """Emits set of package decoder imports."""
    imports = []

    def append_import(imp):
        if imp not in imports:
            imports.append(imp)

    # Set type decoding imports.
    for type_ in [t for t in p.external_types if t.is_class]:
        imp = 'from {0} import *'.format(
            pgu.get_package_module_name(type_.name_of_package, 'decoder'))
        append_import(imp)

    if len(imports) > 0:
        return reduce(add, map(lambda i : i + gu.emit_line_return(), sorted(imports)))
    else:
        return ''


def _emit_snippet_decoding_fns(p):
    """Emits set of package class decodings."""
    code = ''
    for c in sorted(p.classes, key=lambda c: c.op_func_name):
        fn = _TEMPLATES[_TEMPLATE_DECODER_FUNCTION]
        fn = fn.replace('{class-name}', c.op_name)
        fn = fn.replace('{class-function-name}', c.op_func_name)
        fn = fn.replace('{package-name}', c.package.op_name)
        fn = fn.replace('{class-doc-name}', c.op_doc_string_name)
        fn = fn.replace('{class-decodings}', _emit_snippet_decodings(c))
        fn += gu.emit_line_return(3)
        code += fn

    return code


def _emit_snippet_decodings(c):
    """Emits a set of class decodings."""
    code = []
    for p in sorted(c.all_properties, key= lambda p: p.name):
        for dc in c.get_property_decodings(p):
            if dc.decoding is not None:
                code.append(_emit_snippet_decoding(p, dc.decoding, dc.type))

    return gu.emit(code)


def _get_decoding_function(prp, type_):
    """Returns decoding function name."""
    # ... simple/enum types - return type functional name
    #     (is directly mapped to a convertor function).
    if prp.type.is_simple or prp.type.is_enum:
        return '\'{0}\''.format(pgu.get_type_functional_name(prp.type))
    # ... complex classes - return class functional name.
    elif prp.type.is_class:
        type_name = prp.type.name if type_ is None else type_
        return _get_decoder_function_name(type_name)


def _emit_snippet_decoding(prp, decoding, type_):
    """Emits a class property decoding."""
    tmpl = '{0}(\'{1}\', {2}, {3}, \'{4}\'),'
    return tmpl.format(
        gu.emit_line_return() + gu.emit_indent(2),
        prp.name,
        prp.is_collection,
        _get_decoding_function(prp, type_),
        '' if decoding is None else decoding)


def _emit_module_init(o):
    """Emits package initializer."""
    def get_imports():
        def get_code(c):
            return "from {0} import {1}".format(
                pgu.get_package_module_name(c.package, 'decoder'),
                _get_decoder_function_name(c)) + gu.emit_line_return()

        return gu.emit(o.entities, get_code)

    code = _TEMPLATES[_TEMPLATE_MAIN]
    code = code.replace('{module-imports}', get_imports())

    return code


def _get_decoder_function_name(name):
    """Converts class name to a decoder function name.

    """
    return 'decode_{0}'.format(pgu.get_type_func_name(name))
