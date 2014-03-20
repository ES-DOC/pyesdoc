# Module imports.
from os.path import abspath, join, dirname

import tornado.template as template

import pyesdoc
import test_utils as tu
import test_types as tt



# Output folder.
OP_DEMOS = join(dirname(dirname(abspath(__file__))), "demos")

# Demo document template.
_template = template.Loader(dirname(abspath(__file__))).load("demo_document_template.html")


def _get_file_name(doc):
    path = join(OP_DEMOS, doc.__class__.type_key)

    return path + "." + pyesdoc.ESDOC_ENCODING_HTML


def _write(doc):
    as_html = pyesdoc.encode(doc, pyesdoc.ESDOC_ENCODING_HTML)
    with open(_get_file_name(doc), 'w') as f:
        f.write(_template.generate(body=as_html))


def _main():
    for tm in tt.MODULES:
        doc = tu.get_doc(tm)
        try:
            _write(doc)
        except Exception as err:
            print "ERR ::", doc.type_key, " ::", err    


if __name__ == '__main__':
    _main()
