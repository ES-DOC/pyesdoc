# -*- coding: utf-8 -*-

"""
.. module:: cim_1.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: CIM v1 HTML field sets.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc.codecs.html.fieldsets.field_info import FieldInfo



# Document field sets.
FIELDSETS = {
    'cim.2.designing.numericalexperiment-overview': [
        FieldInfo('Project', path='meta.project'),
        FieldInfo('Institute', path='meta.institute'),
        FieldInfo('Name', path='canonical_name'),
        FieldInfo('Long Name', path='long_name'),
        FieldInfo('Description', path='description'),
        FieldInfo('Keywords', path='keywords', input_formatter=lambda v: " | ".join(v))
    ],

    'cim.2.shared.citation' : [
        FieldInfo('Long Title', path='citation_str', link_path="url.linkage"),
        FieldInfo('Context', path='context'),
        FieldInfo('DOI', path='doi', link_path=lambda i: "https://doi.org/{}".format(i.doi)),
        FieldInfo('Abstract', path='abstract'),
    ]
}
