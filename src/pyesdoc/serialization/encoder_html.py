"""
.. module:: encoder_html.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: HTML encoder from document.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import datetime
import os

import tornado.template as template

from .. utils import (
    convert,
    functional
    )



# Template loader.
_loader = template.Loader(os.path.join(os.path.dirname(os.path.abspath(__file__)), "html_templates"))


# Document templates keyed by document type.
_templates = {
    "cim.1.activity.ensemble": _loader.load("cim_1/activity_ensemble.html"),
    "cim.1.activity.numericalexperiment": _loader.load("cim_1/activity_numerical_experiment.html"),
    "cim.1.data.dataobject": _loader.load("cim_1/data_data_object.html"),
    "cim.1.grids.gridspec": _loader.load("cim_1/grids_grid_spec.html"),
    "cim.1.shared.platform": _loader.load("cim_1/shared_platform.html"),
    "cim.1.software.modelcomponent": _loader.load("cim_1/software_model_component.html"),
    "cim.1.quality.cimquality": _loader.load("cim_1/quality_cimquality.html")
}


def _format_value(v, formatter=None):
    """Formats values for document output."""
    def _format(s):
        if s is None:
            s = None
        # TODO add support for time formatting.
        elif isinstance(v, datetime.datetime):
            s = str(s)[:10]
        else:
            s = str(s)

        if s and len(s):
            s = unicode(s.decode('utf8').strip())

        if formatter:
            s = formatter(s)

        return s

    return "  ".join(map(_format, v)).strip() if isinstance(v, list) else _format(v)


def _get_value(data, path):
    """Returns formatted value for document output."""
    if data is None:
        return None

    def is_collection_reference(attr):
        try:
            int(attr)
        except ValueError:
            return False
        else:
            return True

    # Initialise return value.
    value = data

    # Walk attribute path.
    for attr in path.split("."):
        # ... collection filter by index
        if is_collection_reference(attr):
            value = value[int(attr)]
        # ... collection filter by attribute
        elif "=" in attr:
            left, right = attr.split("=")
            value = functional.first(value, left, right.lower(), lambda v: str(v).lower())
        # ... item attribute filter
        elif hasattr(value, attr):
            value = getattr(value, attr)
        # Otherwise escape.
        else:
            break

        # Escape at dead-end.
        if value is None:
            break

    return None if value == data else value


def _get_name(name):
    """Returns formatted name for document output."""
    # Initialise.
    name = "" if name is None else name.strip()

    # Convert to spaced case.
    if len(name) > 4:
        name = convert.str_to_spaced_case(name).strip()

    # Prefixes.
    n = name.lower()
    prefixes = { "number of ": "" }
    for prefix in prefixes.keys():
        if n.startswith(prefix):
            name = prefixes[prefix] + name[len(prefix):]

    # Substrings.
    replacements = {
        "_": " ",
        "Second": "2nd",
        "First": "1st"
    }
    for replacement in replacements.keys():
        name = name.replace(replacement, replacements[replacement])

    # Substitutions.
    swaps = {
        "id": "ID",
    }
    for swap in swaps.keys():
        if name == swap:
            name = swaps[swap]

    return name


class _TemplateInfo():
    """Template processing information."""
    def __init__(self,
                 data,
                 header=None,
                 fieldset=[],
                 fieldset_type="namevalue",
                 tag_id=None,
                 template=None,
                 previous=None,
                 depth=0):
        if isinstance(data, _TemplateInfo):
            previous = data
            data = previous.data
        self.data = None
        self.depth = depth
        self.header = header
        self.field = None
        self.fieldset = fieldset
        self.fieldset_type = fieldset_type
        self.previous = previous
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


class _FieldInfo():
    """Document field processing information."""
    def __init__(self,
                 name,
                 email=None,
                 email_path=None,
                 formatter=None,
                 link=None,
                 link_path=None,
                 path=None,
                 tag_id=None,
                 value=None):
        self.name = name
        self.email = email
        self.email_path = email_path
        self.formatter = formatter
        self.link = link
        self.link_path = link_path
        self.path = path
        self.tag_id = tag_id
        self.value = value


    def get_name(self):
        """Returns formatted field name for html output."""
        return _get_name(self.name)


    def get_value(self, data=None):
        """Returns value of field for html output.

        :param object data: An object from which the field value is derived.

        :returns: The derived field value.
        :rtype str:

        """
        v = _get_value(data, self.path) if self.path else self.value
        v = _format_value(v, self.formatter)

        return v


    def get_link(self, data):
        """Returns value of associated hyperlink.

        :param object data: An object from which the hyperlink value is derived.

        :returns: The derived field hyperlink.
        :rtype str:

        """
        v = _get_value(data, self.link_path)
        v = _format_value(v)

        return v


    def get_email(self, data):
        """Returns value of associated email link.

        :param object data: An object from which the email link value is derived.

        :returns: The derived field email link.
        :rtype str:

        """
        v = _get_value(data, self.email_path)
        v = _format_value(v)

        return v


def encode(doc):
    """Encodes a document to HTML.

    :param doc: Document being encoded.
    :type doc: object

    :returns: An HTML representation of a document.
    :rtype: str

    """
    template = _templates[doc.meta.type.lower()]

    return template.generate(doc=doc,
                             FieldInfo=_FieldInfo,
                             TemplateInfo=_TemplateInfo)