# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.io.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document io functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""
import os

import pyesdoc
from pyesdoc.utils.convert import str_to_unicode



def get_filename(doc, encoding=None):
    """Returns document file name.

    :param object document: A pyesdoc document instance.
    :param str encoding: Document encoding.

    :returns: Document file name.
    :rtype: str

    """
    if encoding is None:
        encoding = pyesdoc.constants.ENCODING_JSON

    return '{0}_{1}_{2}.{3}'.format(doc.__class__.type_key,
                                    doc.meta.id,
                                    doc.meta.version,
                                    encoding)


def _get_filepath(io_dir, doc, encoding):
    """Returns document file path.

    """
    return os.path.join(io_dir, get_filename(doc, encoding))


def write(document, encoding=pyesdoc.constants.ENCODING_JSON, io_dir=None):
    """Writes a document to the file system.

    :param object document: A pyesdoc document instance.
    :param str encoding: Document encoding.
    :param str io_dir: I/O directory path.

    :returns: Path to created file.
    :rtype: str

    """
    # Validate I/O directory.
    if not os.path.isdir(io_dir):
        raise ValueError("Output directory does not exist.")

    fpath = _get_filepath(io_dir, document, encoding)
    with open(fpath, 'w') as fstream:
        fstream.write(pyesdoc.encode(document, encoding))

    return fpath


def read(fpath, encoding=None, decode=True):
    """Reads a document from file system.

    :param str fpath: Path to previously saved file.
    :param str encoding: Encoding to use during deserialization.
    :param bool decode: Flag indicating whether document will be decoded.

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Validate file path.
    if not os.path.isfile(fpath):
        raise IOError("Document file path does not exist")

    # Optionally derive encoding from file extension.
    if encoding is None:
        encoding = os.path.splitext(fpath)[1][1:]

    # Set raw content.
    with open(fpath, 'r') as fstream:
        fcontent = str_to_unicode(fstream.read())

    # Decode upon request.
    return pyesdoc.decode(fcontent, encoding) if decode else fcontent


def convert(fpath, to_encoding, from_encoding=None):
    """Converts a document upon file system.

    :param str fpath: Path to previously saved file.
    :param str to_encoding: Target encoding.
    :param str from_encoding: Source encoding (defaults to json).

    :returns: Path to converted pyesdoc document instance.
    :rtype: str

    """
    if not os.path.isfile(fpath):
        raise IOError("Document file path does not exist")

    document = read(fpath, from_encoding)
    fpath = "{0}.{1}".format(os.path.splitext(fpath)[0], to_encoding)

    return write(document, to_encoding, fpath)
