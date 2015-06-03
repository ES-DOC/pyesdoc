# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.codecs.json.encoder.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encodes a document as an HTML text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from collections import defaultdict
from os.path import abspath
from os.path import dirname
from os.path import join

import tornado.template as template

import pyesdoc
from pyesdoc.codecs.html.fieldsets import create as create_fieldset
from pyesdoc.utils import rt



# Path to template directory.
_DIR_TEMPLATES = join(dirname(abspath(__file__)), "templates")

# Document templates keyed by document type.
_TEMPLATES = {}


def _init_templates():
    """Initializes templates.

    """
    loader = template.Loader(_DIR_TEMPLATES)
    _TEMPLATES["document_set"] = \
        loader.load("core/document_set.html")
    _TEMPLATES["cim.1.activity.ensemble"] = \
        loader.load("cim_1/activity_ensemble.html")
    _TEMPLATES["cim.1.activity.numericalexperiment"] = \
        loader.load("cim_1/activity_numerical_experiment.html")
    _TEMPLATES["cim.1.activity.simulationrun"] = \
        loader.load("cim_1/activity_simulation_run.html")
    _TEMPLATES["cim.1.data.dataobject"] = \
        loader.load("cim_1/data_data_object.html")
    _TEMPLATES["cim.1.grids.gridspec"] = \
        loader.load("cim_1/grids_grid_spec.html")
    _TEMPLATES["cim.1.shared.platform"] = \
        loader.load("cim_1/shared_platform.html")
    _TEMPLATES["cim.1.software.modelcomponent"] = \
        loader.load("cim_1/software_model_component.html")
    _TEMPLATES["cim.1.quality.cimquality"] = \
        loader.load("cim_1/quality_cimquality.html")


class TemplateInfo(object):
    """Template processing information wrapper.

    """
    def __init__(self,
                 data,
                 header=None,
                 fieldset=None,
                 fieldset_type=None,
                 tag_id=None,
                 tag_css=None,
                 template=None,
                 previous=None,
                 depth=None):
        if isinstance(data, TemplateInfo):
            previous = data
            data = previous.data
        self.data = None
        self.depth = depth or 0
        self.header = header
        self.field = None
        self.fieldset = create_fieldset(fieldset)
        self.fieldset_type = fieldset_type or "namevalue"
        self.previous = previous
        self.tag_css = tag_css
        self.template = template

        self._set_tag_id(tag_id)
        self._set_dataset(data)


    def _set_dataset(self, data):
        """Sets the associated dataset."""
        try:
            iter(data)
        except TypeError:
            self.data = data
            self.dataset = [data]
        else:
            self.dataset = data
        self.dataset = [i for i in self.dataset if i is not None]


    def _set_tag_id(self, id):
        """Sets template tag id."""
        if id is not None:
            self.tag_id = id
        elif self.depth == 0 and self.header:
            self.tag_id = self.header.lower()
        else:
            self.tag_id = None


    def reset_fieldset(self):
        self.fieldset = []


def _generate(document):
    """Returns generated document.

    """
    # Escape if document unsupported.
    template_key = document.meta.type.lower()
    if template_key not in _TEMPLATES:
        msg = u"TODO - document html generator for {0} documents."
        return msg.format(template_key)

    # Generate HTML document.
    try:
        template = _TEMPLATES[template_key]
        return template.generate(doc=document, TemplateInfo=TemplateInfo)
    except Exception as err:
        rt.log_error("Template generation error: {0}".format(err.message))
        raise err


def _get_group_set(document_set):
    """Returns grouped document set.

    """
    def get_sort_key(doc):
        """Returns key used for document sorting."""
        return doc.ext.full_display_name.lower()

    def get_group_key(doc):
        """Returns key used for document grouping."""
        return "{0}-{1}".format(doc.meta.type_sort_key,
                                doc.meta.type_display_name)

    # Initialize group set.
    group_set = defaultdict(list)
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
    # Initialize templates.
    if not _TEMPLATES:
        _init_templates()

    # Convert to sorted iterable.
    try:
        iter(doc)
    except TypeError:
        document_set = [doc]
    else:
        document_set = sorted(doc, key=lambda d: d.meta.sort_key)

    # Filter out documents without a matching template.
    document_set = [d for d in document_set if d.type_key.lower() in _TEMPLATES]

    # Ensure that documents are extended.
    for document in document_set:
        pyesdoc.extend(document)

    # Return generated template.
    return _TEMPLATES["document_set"].generate(
        document_set=document_set,
        document_group_set=_get_group_set(document_set),
        generate_document=_generate)
