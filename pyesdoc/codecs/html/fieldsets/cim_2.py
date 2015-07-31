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
    'cim.2.activity.project': {
        FieldInfo('Name', path='name'),
    },
}
