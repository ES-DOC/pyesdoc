"""
.. module:: pyesdoc.utils.serializer_html.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes document html serialization functions.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import datetime
import os

import tornado.template as template

from .convertors import convert_to_spaced_case


# Template loader.
_loader = template.Loader(os.path.join(os.path.dirname(os.path.abspath(__file__)), "html_templates"))

# Collection of document templates.
_templates = {
    "cim.1.activity.numericalexperiment": _loader.load("cim_1/activity_numerical_experiment.html"),
    "cim.1.grids.gridspec": _loader.load("cim_1/grids_grid_spec.html"),
    "cim.1.shared.platform": _loader.load("cim_1/shared_platform.html"),
    "cim.1.quality.cimquality": _loader.load("cim_1/quality_cimquality.html")
}



def _format_value(v):
    """Formats a value for document output."""    
    # Convert to string.
    if v is None:
        v = str()
    elif isinstance(v, list):
        v = '  '.join(v)
    elif isinstance(v, datetime.datetime):
        v = str(v)[:10]
    else:
        v = str(v)

    return unicode(v.decode('utf8').strip()) if len(v) else "--"


def _get_value(data, path):
    """Returns formatted value for document output."""
    value = data
    for f in path.split("."):
        if hasattr(value, f):
            value = getattr(value, f) 

    return _format_value(None) if value == data else _format_value(value)


def _get_name(name):
    """Returns formatted name for document output."""
    name = "" if name is None else name.strip()
    if len(name) > 3:
        name = convert_to_spaced_case(name).strip()

    # Name prefixes.
    n = name.lower()
    prefixes = { "number of ": "" }
    for prefix in prefixes.keys():
        if n.startswith(prefix):
            name = prefixes[prefix] + name[len(prefix):]

    # Name replacements.
    replacements = { 
        "_": " ",
        "Second": "2nd",
        "First": "1st"
    }
    for replacement in replacements.keys():
        name = name.replace(replacement, replacements[replacement])

    # Name swaps.
    swaps = { 
        "id": "ID",
    }
    for swap in swaps.keys():
        if name == swap:
            name = swaps[swap]

    return name


class _ContextInfo():
    """Data structure encapsulating template processing information."""
    def __init__(self, data, header=None, fieldset=[], template=None):
        self.data = None
        self.header = header
        self.fieldset = fieldset
        self.template = template
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


class _FieldInfo():
    """Data structure encapsulating document field information."""
    def __init__(self, title, path, link_path=None, is_email=False):
        self.title = title
        self._name = title
        self.path = path
        self.link_path = link_path
        self.is_email = is_email


    def get_name(self):
        """Returns field name for html output."""
        return _get_name(self._name)


    def get_value(self, data):
        """Returns value of field for html output.

        :param object data: An object from which the field value is derived.

        :returns: The derived field value.
        :rtype str:

        """        
        if self.path.startswith("$$$"):
            return _format_value(self.path[3:])
        else:
            return _get_value(data, self.path)


    def get_link(self, data):
        """Returns value of associated hyperlink.

        :param object data: An object from which the hyperlink value is derived.

        :returns: The derived field hyperlink.
        :rtype str:

        """
        return _get_value(data, self.link_path)


def decode(repr):
    """Decodes a pyesdoc document from passed representation.

    :param repr: Metafor CIM v1 XML document representation.
    :type repr: lxml.etree._ElementTree

    """
    raise NotImplementedError()


def encode(doc):
    """Encodes a document to an xml string.

    :param doc: Document being encoded.
    :type doc: object

    :returns: An xml representation of a document.
    :rtype: str

    """
    template = _templates[doc.doc_info.type.lower()]

    return template.generate(doc=doc,
                             ContextInfo=_ContextInfo,
                             FieldInfo=_FieldInfo)
