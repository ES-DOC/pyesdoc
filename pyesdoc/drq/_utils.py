# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.drq._utils.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulates library utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os
import xml.etree.ElementTree as ET

from pyesdoc.drq import constants



def init_from_xml(instance, elem, names, convertors=None, from_xml_attribute=True):
    """Initialises set of class instance attributes from an xml element.

    :param object obj: Class instance to be hydrated.
    :param xml.etree.Element elem: XML element used to hydrate class instance.
    :param list names: Set of class attribute names.
    :param dict convertors: Map of value convertors keyed by attribute name.
    :param bool from_xml_attribute: Flag indicating whether obtaining value from an xml attribute.

    """
    names = [n if n not in constants.LABEL_MAP else "{}:{}".format(n, constants.LABEL_MAP[n]) for n in names]
    for name in names:
        # Derive xml name & python name.
        try:
            name_xml, name_py = name.split(':')
        except ValueError:
            name_xml = name_py = name

        # Set value.
        val = None
        if from_xml_attribute:
            val = elem.get(name_xml)
        else:
            child_elem = elem.find('./{}'.format(name_xml))
            if child_elem:
                val = child_elem.text

        if val == '':
            val = None

        if convertors and name_py in convertors:
            try:
                val =  convertors[name_py](val)
            except TypeError:
                if val is None:
                    val = convertors[name_py]()

        # Set instance attribute.
        setattr(instance, name_py, val)


def load_xml(fpath):
    """Loads an XML document from file system stripping out namespaces as it does so.

    """
    if not os.path.exists(fpath):
      raise IOError("Invalid data request file path: {}".format(fpath))

    iterator = ET.iterparse(fpath)
    for _, elem in iterator:
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]

    return iterator.root


def get_fpath(fname, subfolder):
    """Returns path to a data request file.

    """
    fpath = os.path.dirname(os.path.abspath(__file__))
    fpath = os.path.join(fpath, subfolder)
    fpath = os.path.join(fpath, fname)

    return fpath
