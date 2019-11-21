"""
.. module:: pyesdoc.mp.ontologies.generators.generator_utils
   :platform: Unix, Windows
   :synopsis: Set of common generator utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import datetime
import os
import pwd

import tornado



# Templates folder.
_TEMPLATE_FOLDER = os.path.dirname(__file__)

# Standard 4 character python indent.
_INDENT = '    '

# Standard line return.
_LINE_RETURN = '\n'

# Set of loaded templates.
_loaded_templates = dict()

# Set of loaded tornado templates.
_loaded_tornado_templates = dict()


def convert_to_camel_case(name, separator='_'):
    """Converts passed name to camel case.

    :param str name: A name as specified in ontology specification.
    :param str separator: Separator to use in order to split name into constituent parts.

    """
    r = ''
    if name is not None:
        s = name.split(separator)
        for s in s:
            if (len(s) > 0):
                r += s[0].upper()
                if (len(s) > 1):
                    r += s[1:]
    return r


def convert_to_pascal_case(name, separator='_'):
    """Converts passed name to camel case.

    :param str name: A name as specified in ontology specification.
    :param str separator: Separator to use in order to split name into constituent parts.

    """
    r = ''
    s = convert_to_camel_case(name, separator)
    if (len(s) > 0):
        r += s[0].lower()
        if (len(s) > 1):
            r += s[1:]
    return r


def emit(iterable, func=None, sort=True, joiner=""):
    """Returns code (sorted).

    """
    if len(iterable) == 0:
        return ""

    if func:
        code = [func(i) for i in iterable]
    else:
        code = iterable
    code = [l for l in code if l is not None]

    return joiner.join(sorted(code)) if sort else joiner.join(code)


def _load_template(language, filename):
    """Returns code template.

    :param str language: Generator language.
    :param str filename: Name of template file.

    """
    path = _TEMPLATE_FOLDER + "/{0}/templates/{1}".format(language, filename)

    if path not in _loaded_templates:
        tmpl = open(path)
        _loaded_templates[path] = tmpl.read()
        tmpl.close()

    return _loaded_templates[path]


def load_templates(language, filenames):
    """Returns a dictionary of loaded code templates.

    :param str language: Generator language.
    :param str filenames: Set of template file names.

    """
    templates = {}
    for filename in filenames:
        templates[filename] = _load_template(language, filename)

    return templates


def load_tornado_template(language, fname):
    """Returns tornado code template.

    :param str language: Generator language.
    :param str fname: Name of template file.

    """
    dir_ = _TEMPLATE_FOLDER + "/{0}/templates".format(language)

    fpath = os.path.join(dir_, fname)
    if fpath not in _loaded_tornado_templates:
        loader = tornado.template.Loader(dir_)
        _loaded_tornado_templates[fpath] = loader.load(fpath)

    return _loaded_tornado_templates[fpath]


def load_tornado_templates(language, fnames):
    """Returns a dictionary of loaded tornado code templates.

    :param str language: Generator language.
    :param str fnames: Set of template file names.

    """
    return {fname: load_tornado_template(language, fname) for fname in fnames}


def get_username():
    """Returns name of current user.

    """
    try:
        return pwd.getpwuid(os.getuid()).pw_name
    except ImportError:
        return os.environ.get("USERNAME")


def emit_indent(count=1):
    """Emits code corresponding to a code indentation.

    :param int count: Number of indentations to emit.

    """
    return reduce(lambda x, y: x + _INDENT, range(count), '')


def emit_tab():
    """Emits code corresponding to a code tab.

    """
    return emit_indent(4)


def emit_line_return(count=1):
    """Emits code corresponding to a code line return.

    :param int count: Number of line returns to emit.

    """
    return reduce(lambda x, y: x + _LINE_RETURN, range(count), '')


def create_directory(dir):
    """Generates a directory into which code will be generated.

    :param str dir: Target code generation directory.

    """
    try:
        os.makedirs(dir)
    except:
        pass


def write_file(code, dir, file):
    """Writes code to a file.

    :param str code: Code to be written to a file.
    :param str dir: Directory into which code is to be generated.
    :param str file: Name of code file being written.

    """
    # Create directory.
    create_directory(dir)

    # Update code.
    code = code.replace('{file-name}', file)

    # Write file.
    file = open(dir + "/" + file, 'w')
    file.writelines(code)
    file.close()


def format_code(ctx, code):
    """Formats code prior to being written to file system.

    :param pyesdoc.mp.ontologies.generators.generator.GeneratorContext ctx: Generation context information.
    :param str code: Code to be injected with standard params.

    """
    # Ontology related params.
    code = code.replace('{ontology-name}', ctx.ontology.op_name)
    code = code.replace('{ontology-version}', ctx.ontology.op_version)
    code = code.replace('{ontology-version-packagename}', ctx.ontology.op_version.replace('.', '_'))

    # Misceallaneous params.
    code = code.replace('{datetime-year}', str(datetime.datetime.now().year))
    code = code.replace('{user-name}', get_username())

    return code
