"""
.. module:: pyesdoc.io.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document io functions.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>

"""
# Module imports.
import os

from . import serialization
from .utils import runtime as rt



# Output directory path.
_output_directory = None


def _get_doc_path(doc, encoding):
    """Returns path to doc file in the relevant encoding."""
    path = '{0}_{1}_{2}.{3}'.format(
        doc.__class__.type_key,
        str(doc.doc_info.id),
        str(doc.doc_info.version),
        encoding)

    return os.path.join(_output_directory, path)


def set_output_directory(path):
    """Sets io output directory.

    :param path: Output directory path.
    :type path: str

    """
    global _output_directory

    # Defensive programming.
    if not os.path.isdir(path):
        rt.raise_error("Invalid directory path :: {0}.".format(path))

    _output_directory = path


def write(doc, encoding=serialization.ESDOC_ENCODING_JSON):
    """Writes a document to the file system in the passed encoding.

    :param doc: A pyesdoc document instance.
    :type doc: object

    :param encoding: Document encoding.
    :type encoding: str

    :returns: Path to created file.
    :rtype: str

    """
    path = _get_doc_path(doc, encoding)
    with open(path, 'w') as f:
        f.write(serialization.encode(doc, encoding))

    return path


def read(path):
    """Opens a document from a previously saved file from file system.

    :param path: Path to previously saved file.
    :type path: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Defensive programming.
    if not os.path.isfile(path):
        path = os.path.join(_output_directory, path)
        if not os.path.isfile(path):
            rt.raise_error("File path does not exist.")

    encoding = os.path.splitext(path)[1][1:]
    with open(path, 'r') as f:
        return serialization.decode(f.read(), encoding)
