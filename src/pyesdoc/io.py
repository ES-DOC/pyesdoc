"""
.. module:: pyesdoc.io.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document io functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""
import os

from . import constants, serialization, options, extensions



# Output directory option.
_OPT_OUTPUT_DIR = "output_dir"


def _get_doc_path(doc, encoding):
    """Returns path to doc file in the relevant encoding."""
    fpath = '{0}_{1}_{2}.{3}'.format(doc.__class__.type_key,
                                     str(doc.meta.id),
                                     str(doc.meta.version),
                                     encoding)

    return os.path.join(options.get_option(_OPT_OUTPUT_DIR), fpath)


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

    with open(fpath, 'w') as output_file:
        output_file.write(serialization.encode(doc, encoding))

    return fpath


def read(fpath, encoding=None):
    """Opens a document from a previously saved file from file system.

    :param str fpath: Path to previously saved file.
    :param str encoding: Encoding to use during deserialization.
    :param func post_processing_handlers: Callback(s) to invoke after processing.

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    if not os.path.isfile(fpath):
        fpath = os.path.join(options.get_option(_OPT_OUTPUT_DIR), fpath)
        if not os.path.isfile(fpath):
            raise IOError("Document file path does not exist")

    # If encoding is unspecified then derive from file extension.
    if encoding is None:
        encoding = os.path.splitext(fpath)[1][1:]

    with open(fpath, 'r') as input_file:
        return serialization.decode(input_file.read(), encoding)


def convert(in_file, to_encoding, from_encoding=None):
    """Converts a document from one encoding to another.

    :param str in_file: Path to previously saved file.
    :param str encoding: Encoding to use during encoding.

    :returns: Path to converted pyesdoc document instance.
    :rtype: str

    """
    # Validate input file path.
    if not os.path.isfile(in_file):
        in_file = os.path.join(options.get_option(_OPT_OUTPUT_DIR), in_file)
        if not os.path.isfile(in_file):
            raise IOError("Document file path does not exist")

    # Read document.
    doc = read(in_file, from_encoding)

    # Extend document.
    if to_encoding == constants.ESDOC_ENCODING_HTML:
        extensions.extend(doc)

    # Write converted document.
    out_file = "{0}.{1}".format(os.path.splitext(in_file)[0], to_encoding)
    write(doc, to_encoding, out_file)
