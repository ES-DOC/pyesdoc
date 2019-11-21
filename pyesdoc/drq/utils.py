"""
.. module:: pyesdoc.drq.utils.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulates library utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os
import re
import xml.etree.ElementTree as ET

from pyesdoc.drq import constants



class _State(object):
    """Encpasulates mutable module state.

    """
    # Flag indicating whether state has been initialized.
    _is_initialized = False


def initialize():
    """Loads & parses dreq2Defn.xml & dreq.xml files.

    """
    if _State._is_initialized:
        return

    from pyesdoc.drq.definition import initializer
    initializer.execute()

    from pyesdoc.drq.content import initializer
    initializer.execute()

    _State._is_initialized = True


def init_from_xml(
    instance,
    elem,
    names,
    convertors=None
    ):
    """Initialises set of class instance attributes from an xml element.

    :param object instance: Class instance to be initialized.
    :param xml.etree.Element elem: XML element used to hydrate class instance.
    :param list names: Set of class attribute names.
    :param dict convertors: Map of value convertors keyed by attribute name.

    """
    names = [(n, get_label(n)) for n in names]
    for name_xml, name_py in names:
        # Set value.
        val = None
        try:
            elem.get
        except AttributeError:
            child_elem = elem.find('./{}'.format(name_xml))
            if child_elem:
                val = child_elem.text
        else:
            val = elem.get(name_xml)

        # Set value to None.
        if val and unicode(val).strip().lower() in {u'', u'none'}:
            val = None

        # Convert value.
        if convertors and name_py in convertors:
            try:
                val = convertors[name_py](val)
            except TypeError:
                if val is None:
                    val = convertors[name_py]()

        # Set instance attribute using pythonic name.
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


def get_label(label):
    """Returns a reformatted label.

    """
    if label in constants.LABEL_MAP:
        return constants.LABEL_MAP[label]
    elif label != label.lower():
        return str_to_underscore_case(label)
    return label


_CACHE = set()

def get_link_labels(label):
    """Returns a reformatted link label.

    """
    try:
        return constants.LINK_MAP[label]
    except KeyError:
        if label not in _CACHE:
            _CACHE.add(label)
        return label, label


def str_to_underscore_case(target):
    """Helper function to convert a from camel case string to an underscore case string.

    :param target: A string for conversion.
    :type target: str

    :returns: A string converted to underscore case, e.g. account_number.
    :rtype: str

    """
    if target is None or not len(target):
        return ''

    r = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', target)
    r = re.sub('([a-z0-9])([A-Z])', r'\1_\2', r)
    r = r.lower()

    return r