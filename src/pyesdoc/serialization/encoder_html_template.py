"""
.. module:: encoder_html_template.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: HTML encoding template information.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from encoder_html_template_field import load as load_fieldset



class TemplateInfo():
    """Template processing information."""
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
        self.fieldset = load_fieldset(fieldset)
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
