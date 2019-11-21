"""
.. module:: factory.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: CIM v1 HTML field set factory.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc._codecs.html.fieldsets import cim_1
from pyesdoc._codecs.html.fieldsets import cim_2



# Fieldsets by ontology type.
_FIELDSETS = dict(cim_1.FIELDSETS.items() + cim_2.FIELDSETS.items())


def create(fieldset):
    """Creates a templating fieldset.

    :param fieldset: Fieldset identifier.
    :ptype fieldset: tuple | str

    :returns: A templating fieldset.
    :rtype: list

    """
    if isinstance(fieldset, tuple):
        key, obj = fieldset
        return _FIELDSETS[key](obj)
    elif isinstance(fieldset, str):
        return _FIELDSETS[fieldset]
    else:
        return fieldset or []
