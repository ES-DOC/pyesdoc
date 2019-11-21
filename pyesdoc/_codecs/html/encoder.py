"""
.. module:: html.encoder.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encodes a document as an HTML text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import collections
import inspect
import os

import tornado.template as template

import pyesdoc
from pyesdoc import exceptions
from pyesdoc._codecs.html import fieldsets
from pyesdoc.ontologies import cim



# Path to template directory.
_DIR_TEMPLATES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

# Document set template.
_DOCUMENT_SET_TEMPLATE = "core/document_set.html"

# Mapping of doucment type to template.
_TEMPLATE_TYPE_MAPPINGS = {
    # CIM v1 templates.
    cim.v1.activity.Ensemble: "cim_1/activity_ensemble.html",
    cim.v1.activity.NumericalExperiment: "cim_1/activity_numerical_experiment.html",
    cim.v1.activity.SimulationRun: "cim_1/activity_simulation_run.html",
    cim.v1.data.DataObject: "cim_1/data_data_object.html",
    cim.v1.grids.GridSpec: "cim_1/grids_grid_spec.html",
    cim.v1.shared.Platform: "cim_1/shared_platform.html",
    cim.v1.software.ModelComponent: "cim_1/software_model_component.html",
    cim.v1.quality.CimQuality: "cim_1/quality_cimquality.html",
    # CIM v2 templates.
    cim.v2.designing.NumericalExperiment: "cim_2/designing_numerical_experiment.html",
    cim.v2.designing.Project: "cim_2/designing_project.html",
    cim.v2.science.Model: "cim_2/science_model.html",
    cim.v2.shared.Citation: "cim_2/shared_citation.html",
    cim.v2.shared.Party: "cim_2/shared_party.html"
}


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
    document_set = [d for d in document_set if hasattr(d, "meta") and \
                                               isinstance(d, tuple(_TEMPLATE_TYPE_MAPPINGS.keys()))]

    # Escape if no documents.
    if not document_set:
        return

    # Sort.
    document_set = sorted(document_set, key=lambda d: d.meta.sort_key)

    # Extend.
    for document in document_set:
        pyesdoc.extend(document)

    # JIT initialize templates.
    if isinstance(_DOCUMENT_SET_TEMPLATE, str):
        _init_templates()

    # Return generated template.
    try:
        return _DOCUMENT_SET_TEMPLATE.generate(
            document_set=document_set,
            document_group_set=_get_group_set(document_set),
            generate_document=_generate,
            pyesdoc=pyesdoc
            )
    except Exception as error:
        raise exceptions.EncodingException('html', doc, error)


def _init_templates():
    """Initializes templates.

    """
    global _DOCUMENT_SET_TEMPLATE

    loader = template.Loader(_DIR_TEMPLATES)
    _DOCUMENT_SET_TEMPLATE = loader.load(_DOCUMENT_SET_TEMPLATE)
    for doc_type, template_path in _TEMPLATE_TYPE_MAPPINGS.items():
        _TEMPLATE_TYPE_MAPPINGS[doc_type] = loader.load(template_path)


def _log(msg):
    """Emits a template logging message - used for debugging.

    """
    print "TEMPLATE:", msg


class TemplateInfo(object):
    """Template processing information wrapper.

    """
    def __init__(self,
                 data,
                 fieldset=None,
                 fieldset_type=None):
        self.field = None
        self.fieldset = fieldsets.create(fieldset)
        if inspect.isfunction(self.fieldset):
            self.fieldset = self.fieldset(data)
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
    try:
        return _TEMPLATE_TYPE_MAPPINGS[type(document)].generate(
            doc=document,
            TemplateInfo=TemplateInfo,
            pyesdoc=pyesdoc,
            load=pyesdoc.archive.load_references,
            cim=pyesdoc.ontologies.cim,
            log=_log,
            collections=collections
            )
    except Exception as err:
        pyesdoc.log_error("Template generation error: {0}".format(err.message))
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

    # Initialize group sets.
    group_set = collections.defaultdict(list)
    for document in document_set:
        group_key = get_group_key(document)
        group_set[group_key].append(document)

    # Sort group sets.
    for group_key, document_set in group_set.iteritems():
        group_set[group_key] = sorted(document_set, key=get_sort_key)

    return group_set
