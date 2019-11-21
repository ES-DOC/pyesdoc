"""
.. module:: field.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: HTML encoding template field information.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import datetime
import inspect

from pyesdoc.utils import convert
from pyesdoc.utils import runtime



class Field(object):
    """Document field processing information.

    """
    def __init__(
        self,
        name,
        email=None,
        email_path=None,
        input_formatter=None,
        output_formatter=None,
        link=None,
        link_factory=None,
        link_path=None,
        path=None,
        tag_id=None,
        value=None,
        capitalize_value=False,
        predicate=None
        ):
        """Instance constructor.

        """
        self.name = name
        self.email = email
        self.email_path = email_path
        self.input_formatter = input_formatter
        self.output_formatter = output_formatter
        self.link = link
        self.link_factory = link_factory
        self.link_path = link_path
        self.path = path
        self.tag_id = tag_id
        self.value = value
        self.capitalize_value = capitalize_value
        self.predicate = predicate


    def get_name(self):
        """Returns formatted field name for html output.

        """
        return _get_name(self.name)


    def get_value(self, data=None):
        """Returns value of field for html output.

        :param object data: An object from which the field value is derived.

        :returns: The derived field value.
        :rtype str:

        """
        if self.link_factory:
            if inspect.isfunction(self.link_factory):
                return self.link_factory(data)
            return self.link_factory

        v = _get_value(data, self.path) if self.path else self.value
        v = _format_value(v, self.input_formatter, self.output_formatter)

        return v


    def get_link(self, data):
        """Returns value of associated hyperlink.

        :param object data: An object from which the hyperlink value is derived.

        :returns: The derived field hyperlink.
        :rtype str:

        """
        if inspect.isfunction(self.link_path):
            v = self.link_path(data)
        else:
            v = _get_value(data, self.link_path)
        v = _format_value(v)

        return v


    def get_email(self, data):
        """Returns value of associated email link.

        :param object data: An object from which the email link value is derived.

        :returns: The derived field email link.
        :rtype str:

        """
        if inspect.isfunction(self.email_path):
            v = self.email_path(data)
        else:
            v = _get_value(data, self.email_path)
        v = _format_value(v)

        return v


def _format_value(v, input_formatter=None, output_formatter=None):
    """Formats values for document output.

    """
    def _format(s):
        if s is None:
            s = None
        # TODO add support for time formatting.
        elif isinstance(v, datetime.datetime):
            s = str(s)[:10]
        else:
            s = str(s)

        if s and len(s):
            s = convert.str_to_unicode(s)
            if output_formatter:
                s = output_formatter(s)

        if s and len(s):
            s = s.strip()

        return s

    if input_formatter:
        v = input_formatter(v)

    if isinstance(v, list):
        return [_format(i) for i in v]
    else:
        return _format(v)


def _get_value(data, path):
    """Returns formatted value for document output.

    """
    if data is None:
        return None

    def is_collection_reference(attr):
        """Returns flag indicating whether attribute refers to a collection.

        """
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
            value = runtime.first(value, left, right.lower(), lambda v: unicode(v).lower())
        # ... item attribute filter
        elif hasattr(value, attr):
            value = getattr(value, attr)
        # Otherwise escape.
        else:
            break
        # Escape at dead-end.
        if value is None:
            break

    # Tornado templating requires 'strings'.
    if isinstance(value, unicode):
        value = convert.unicode_to_str(value)

    return None if value == data else value


def _get_name(name):
    """Returns formatted name for document output.

    """
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
