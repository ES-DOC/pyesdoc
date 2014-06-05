"""
.. module:: pyesdoc.io.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document io functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""
# Module imports.
import os

from . import constants, serialization
from .utils import runtime as rt



# Output directory path.
_output_directory = None


def _get_doc_path(doc, encoding):
    """Returns path to doc file in the relevant encoding."""
    fpath = '{0}_{1}_{2}.{3}'.format(doc.__class__.type_key,
                                     str(doc.meta.id),
                                     str(doc.meta.version),
                                     encoding)

    return os.path.join(_output_directory, fpath)


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


def write(doc, encoding=constants.ESDOC_ENCODING_JSON, fpath=None):
    """Writes a document to the file system in the passed encoding.

    :param object doc: A pyesdoc document instance.
    :param str encoding: Document encoding.
    :param str fpath: Path to file to be written.

    :returns: Path to created file.
    :rtype: str

    """
    if fpath is None:
        fpath = _get_doc_path(doc, encoding)

    doc = serialization.encode(doc, encoding)

    with open(fpath, 'w') as output_file:
        output_file.write(doc)

    return fpath


def read(fpath, encoding=None):
    """Opens a document from a previously saved file from file system.

    :param str fpath: Path to previously saved file.
    :param str encoding: Encoding to use during deserialization.
    :param func post_processing_handlers: Callback(s) to invoke after processing.

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Defensive programming.
    if not os.path.isfile(fpath):
        fpath = os.path.join(_output_directory, fpath)
        if not os.path.isfile(fpath):
            rt.raise_error("File path does not exist.")

    # If encoding is unspecified then derive from file extension.
    if encoding is None:
        encoding = os.path.splitext(fpath)[1][1:]

    with open(fpath, 'r') as input_file:
        return serialization.decode(input_file.read(), encoding)
