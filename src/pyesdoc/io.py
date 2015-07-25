# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.io.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document io functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""
import os

import pyesdoc
from pyesdoc.utils.convert import str_to_unicode



# Output directory option.
_OPT_OUTPUT_DIR = "output_dir"



def _get_doc_path(doc, encoding):
    """Returns path to doc file in the relevant encoding.

    """
    fpath = '{0}_{1}_{2}.{3}'.format(doc.__class__.type_key,
                                     str(doc.meta.id),
                                     str(doc.meta.version),
                                     encoding)
    output_dir = pyesdoc.get_option(_OPT_OUTPUT_DIR)

    return os.path.join(output_dir, fpath)


def write(document, encoding=None, fpath=None):
    """Writes a document to the file system in the passed encoding.

    :param object document: A pyesdoc document instance.
    :param str encoding: Document encoding.
    :param str fpath: Path to file to be written.

    :returns: Path to created file.
    :rtype: str

    """
    if encoding is None:
        encoding = pyesdoc.constants.ESDOC_ENCODING_JSON
    if fpath is None:
        fpath = _get_doc_path(document, encoding)
    content = pyesdoc.encode(document, encoding)
    with open(fpath, 'w') as output_file:
        output_file.write(content)

    return fpath


def read(fpath, encoding=None, decode=True):
    """Opens a document from a previously saved file from file system.

    :param str fpath: Path to previously saved file.
    :param str encoding: Encoding to use during deserialization.
    :param bool decode: Flag indicating whether document will be decoded.

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Validate file path.
    if not os.path.isfile(fpath):
        fpath = os.path.join(pyesdoc.get_option(_OPT_OUTPUT_DIR), fpath)
        if not os.path.isfile(fpath):
            raise IOError("Document file path does not exist")

    # If encoding is unspecified then derive from file extension.
    if encoding is None:
        encoding = os.path.splitext(fpath)[1][1:]

    # Set raw content.
    with open(fpath, 'r') as input_file:
        content = str_to_unicode(input_file.read())

    # Decode upon request.
    if decode:
        return pyesdoc.decode(content, encoding)
    else:
        return content


def convert(fpath, to_encoding, from_encoding=None):
    """Converts a document from one encoding to another.

    :param str fpath: Path to previously saved file.
    :param str to_encoding: Target encoding.
    :param str from_encoding: Source encoding (defaults to json).

    :returns: Path to converted pyesdoc document instance.
    :rtype: str

    """
    if not os.path.isfile(fpath):
        fpath = os.path.join(pyesdoc.get_option(_OPT_OUTPUT_DIR), fpath)
        if not os.path.isfile(fpath):
            raise IOError("Document file path does not exist")

    document = read(fpath, from_encoding)
    fpath_out = "{0}.{1}".format(os.path.splitext(fpath)[0], to_encoding)

    return write(document, to_encoding, fpath_out)
