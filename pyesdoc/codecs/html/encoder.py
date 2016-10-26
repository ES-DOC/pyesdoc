# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.codecs.html.encoder.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encodes a document as an HTML text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import collections
import os

import tornado.template as template

import pyesdoc
from pyesdoc.codecs.html import fieldsets
from pyesdoc.codecs.html.templates.type_mappings import TEMPLATE_TYPE_MAPPINGS
from pyesdoc.utils import rt



# Path to template directory.
_DIR_TEMPLATES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

# Document set template.
_DOCUMENT_SET_TEMPLATE = "core/document_set.html"


def _init_templates():
    """Initializes templates.

    """
    global _DOCUMENT_SET_TEMPLATE

    loader = template.Loader(_DIR_TEMPLATES)
    _DOCUMENT_SET_TEMPLATE = loader.load(_DOCUMENT_SET_TEMPLATE)
    for doc_type, template_path in TEMPLATE_TYPE_MAPPINGS.items():
        TEMPLATE_TYPE_MAPPINGS[doc_type] = loader.load(template_path)


def _log(msg):
    """Emits a template logging message - used for debugging.

    """
    print "TEMPLATE:", msg


def load(reference):
    """Loads a referenced document.

    """
    def _load(ref):
        """Inner function to load document from archive.

        """
        try:
            ref.meta
        except AttributeError:
            doc = pyesdoc.archive.read(ref.id, ref.version)
            if doc.meta.type != ref.type:
                doc.meta.type = ref.type
            return doc
        else:
            return ref

    try:
        iter(reference)
    except TypeError:
        return _load(reference)
    else:
        return [_load(i) for i in reference]


class TemplateInfo(object):
    """Template processing information wrapper.

    """
    def __init__(self,
                 data,
                 fieldset=None,
                 fieldset_type=None):
        self.field = None
        self.fieldset = fieldsets.create(fieldset)
        self.fieldset_type = fieldset_type or "namevalue"
        try:
            iter(data)
        except TypeError:
            self.data = data
            self.dataset = [data]
        else:
            self.data = self.dataset = data
        self.dataset = [i for i in self.dataset if i is not None]


def _generate(document):
    """Returns generated document.

    """
    target = TEMPLATE_TYPE_MAPPINGS[type(document)]
    try:
        return target.generate(
            doc=document,
            TemplateInfo=TemplateInfo,
            pyesdoc=pyesdoc,
            load=load,
            cim=pyesdoc.ontologies.cim,
            log=_log
            )
    except Exception as err:
        rt.log_error("Template generation error: {0}".format(err.message))
        raise err


def _get_group_set(document_set):
    """Returns grouped document set.

    """
    def get_sort_key(doc):
        """Returns key used for document sorting.

        """
        return doc.ext.full_display_name.lower()

    def get_group_key(doc):
        """Returns key used for document grouping.

        """
        return "{0}-{1}".format(doc.meta.type_sort_key,
                                doc.meta.type_display_name)

    # Initialize group set.
    group_set = collections.defaultdict(list)
    for document in document_set:
        group_key = get_group_key(document)
        group_set[group_key].append(document)

    # Sort grouped document sets.
    for group_key, document_set in group_set.iteritems():
        group_set[group_key] = sorted(document_set, key=get_sort_key)

    return group_set


def encode(doc):
    """Encodes a document to HTML.

    :param object doc: Document being encoded.

    :returns: An HTML representation of a document.
    :rtype: str

    """
    # Convert to iterable.
    try:
        iter(doc)
    except TypeError:
        document_set = [doc]
    else:
        document_set = doc

    # Filter out fragments & non-templated documents.
    document_set = [d for d in document_set if hasattr(d, "meta")]
    document_set = [d for d in document_set if type(d) in TEMPLATE_TYPE_MAPPINGS]

    # Escape if no documents.
    if not document_set:
        return

    # Sort.
    document_set = sorted(document_set, key=lambda d: d.meta.sort_key)

    # Ensure documents are extended.
    for document in document_set:
        pyesdoc.extend(document)

    # Ensure templates are initialized.
    if isinstance(_DOCUMENT_SET_TEMPLATE, str):
        _init_templates()

    # Return generated template.
    return _DOCUMENT_SET_TEMPLATE.generate(
        document_set=document_set,
        document_group_set=_get_group_set(document_set),
        generate_document=_generate,
        pyesdoc=pyesdoc
        )
