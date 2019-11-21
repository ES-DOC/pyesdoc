"""
.. module:: pyesdoc.mp.ontologies.generators.python.typeset_generator.py
   :platform: Unix, Windows
   :synopsis: Generates code encapsulating an ontology's typeset.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.mp.ontologies import core
from pyesdoc.mp.ontologies.generators import generator_utils as gu
from pyesdoc.mp.ontologies.generators.python import utils as pgu
from pyesdoc.mp.ontologies.generators.generator import Generator
from pyesdoc.mp import utils



# Generator language.
_LANG = 'python'

# Template for a typeset module.
_TEMPLATE_TYPESET = 'typeset_for_package.txt'

# Template for a concrete class.
_TEMPLATE_CLASS_CONCRETE = "typeset_class_concrete.txt"

# Template for an abstract class.
_TEMPLATE_CLASS_ABSTRACT = "typeset_class_abstract.txt"

# Template for a class print string.
_TEMPLATE_CLASS_PSTR = "typeset_class_pstr.txt"

# Template for an enumeration.
_TEMPLATE_ENUM = "typeset_enum.txt"

# Template for a computed class property.
_TEMPLATE_CLASS_COMPUTED_PROPERTY = "typeset_class_computed_property.txt"

# Loaded templates.
_TEMPLATES = gu.load_templates(_LANG, (
    _TEMPLATE_TYPESET,
    _TEMPLATE_CLASS_CONCRETE,
    _TEMPLATE_CLASS_ABSTRACT,
    _TEMPLATE_CLASS_PSTR,
    _TEMPLATE_ENUM,
    _TEMPLATE_CLASS_COMPUTED_PROPERTY
))


class PackageTypeSetGenerator(Generator):
    """Generates code to represent an ontology as a set of types.

    """
    def on_package_parse(self, ctx):
        """Event handler for the package parse event.

        :param GeneratorContext ctx: Generation context information.

        """
        ctx.code.append(
            (
                _emit_module_typeset_for_pkg(ctx.ontology, ctx.pkg),
                pgu.get_ontology_directory(ctx),
                pgu.get_package_module_file_name(ctx.pkg, 'typeset')
            )
        )


def _emit_module_typeset_for_pkg(o, p):
    """Emits typeset module for an ontology package.

    """
    def emit_imports():
        def get_code(ap):
            return "import {} as {}{}".format(
                pgu.get_package_module_name(ap, 'typeset'),
                ap.op_name,
                gu.emit_line_return())

            return code

        return gu.emit(p.associated_for_import, get_code)


    def get_classes(p):
        # Return list of classes sorted in dependency order.
        result = [c for c in p.classes if c.base is None or c.base.package != p]
        result = sorted(result, key=lambda c: c.name)

        while len(result) < len(p.classes):
            n = len(result)
            for c in [c for c in sorted(p.classes, key=lambda c: c.name) if c not in result]:
                if c.base in result:
                    result.append(c)

            # Error if parse revels unresolvable dependencies.
            if n == len(result):
                msg = "Package {0} has circular class dependencies."
                msg = msg.format(p)
                utils.raise_error(msg.format(p))

        return result


    def emit_types():
        def get_code(t):
            if isinstance(t, core.Class):
                code = _emit_snippet_class(t)
            else:
                code = _emit_snippet_enum(t)
            code += gu.emit_line_return(2)

            return code

        return gu.emit(get_classes(p), get_code, sort=False) + \
               gu.emit(p.enums, get_code)


    code = _TEMPLATES[_TEMPLATE_TYPESET]
    code = code.replace('{imports}', emit_imports())
    code = code.replace('{types}', emit_types())
    code = code.replace('{package-name}', p.op_name)

    return code


def _emit_snippet_enum(e):
    """Emits code corresponding to a python enum.

    """
    def emit_members():
        def get_code(m):
            code = gu.emit_line_return()
            code += gu.emit_indent(2)
            code += '"{}"'.format(m.name)

            return code

        code = gu.emit(e.members, get_code, joiner=",", sort=False)
        code += gu.emit_line_return()
        code += gu.emit_indent(2)

        return code


    def emit_descriptions():
        def get_code(m):
            code = gu.emit_line_return()
            code += gu.emit_indent(2)
            code += '"{}"'.format(m.doc_string)

            return code

        code = gu.emit(e.members, get_code, joiner=",", sort=False)
        code += gu.emit_line_return()
        code += gu.emit_indent(2)

        return code


    code = _TEMPLATES[_TEMPLATE_ENUM]
    code = code.replace('{enum-name}', e.op_name)
    code = code.replace('{enum-doc-string}', e.doc_string)
    code = code.replace('{enum-is-open}', str(e.is_open))
    code = code.replace('{enum-members}', emit_members() if e.members else "")
    code = code.replace('{enum-descriptions}', emit_descriptions() if e.members else "")

    return code


def _emit_snippet_class(c):
    """Emits code corresponding to a python class."""
    # Open template.
    if c.is_abstract:
        code = _TEMPLATES[_TEMPLATE_CLASS_ABSTRACT]
    else:
        code = _TEMPLATES[_TEMPLATE_CLASS_CONCRETE]

    # Generate code.
    code = code.replace('{class-name}', c.op_name)
    code = code.replace('{base-class-name}', c.op_base_name)
    code = code.replace('{class-doc-string}', _emit_snippet_class_doc_string(c))
    code = code.replace('{class_constants}', _emit_snippet_class_property_constants(c))
    code = code.replace('{class-properties}', _emit_snippet_class_properties(c))
    code = code.replace('{class-computed-properties}', _emit_snippet_class_computed_properties(c))
    code = code.replace('{class-pstr}', _emit_snippet_class_pstr(c))

    return code


def _emit_snippet_class_pstr(c):
    """Emits class print string.

    """
    code = ""
    if c.pstr:
        code = _TEMPLATES[_TEMPLATE_CLASS_PSTR]
        code = code.replace('{text}', c.pstr.text)
        code = code.replace('{fields}', ", ".join(["self.{}".format(f) for f in c.pstr.fields]))

    return code


def _emit_snippet_class_doc_string(c):
    """Emits class doc string."""
    doc_string = "" if not c.doc_string else c.doc_string

    if doc_string:
        doc_string = "{0}{1}{2}".format(doc_string,
                                        gu.emit_line_return(2),
                                        gu.emit_indent())

    return "{0}{1}{2}".format(gu.emit_line_return(2),
                              gu.emit_indent(),
                              doc_string)



def _emit_snippet_class_properties(c):
    """Emits set of class properties."""
    def get_code(p):
        return "{0}{1}{2}# {3} ({4}){5}".format(
            gu.emit_indent(2),
            pgu.get_property_ctor(p),
            ''.ljust(50 - len(pgu.get_property_ctor(p))),
            pgu.get_type_doc_name(p.type),
            p.cardinality,
            gu.emit_line_return()
        )

    return gu.emit(c.properties, get_code)


def _emit_snippet_class_computed_properties(c):
    """Emits set of class computed properties."""
    def get_code(cp):
        # Open template.
        code = _TEMPLATES[_TEMPLATE_CLASS_COMPUTED_PROPERTY]

        # Generate code.
        code = code.replace('{computed-property-name}', cp.name)
        code = code.replace('{computed-property-computation}', cp.computation)

        return code

    return gu.emit(c.computed_properties, get_code)


def _emit_snippet_class_property_constants(c):
    """Emits set of class property constants."""
    def get_code(cnt):
        prp = c.get_property(cnt[0])
        if prp is not None:
            return '{0}self.{1} = {2}("{3}"){4}'.format(
                gu.emit_indent(2),
                cnt[0],
                pgu.get_type_functional_name(prp.type),
                cnt[1],
                gu.emit_line_return()
            )

    return gu.emit(c.constants, get_code)
