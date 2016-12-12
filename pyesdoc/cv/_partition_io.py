# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv._partition_io.py
   :copyright: Copyright "December 01, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Manages partition terms I/O.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""
import os

from pyesdoc.cv import constants
from pyesdoc.cv.codecs import from_json
from pyesdoc.cv.codecs import to_json
from pyesdoc.cv.utils.logger import log



class PartitionIO(object):
    """Encapsulates partition I/O operations.

    """
    def __init__(self, domain, io_dir):
        """Instance constructor.

        """
        self.domain = domain
        self.root_dir = os.path.join(io_dir, domain)
        self.set_dir = os.path.join(self.root_dir, "sets")
        self.map_dir = os.path.join(self.root_dir, "maps")


    def _get_term_io_path(self, term):
        """Returns term's I/O path, i.e. location on file system to which the term will be written.

        """
        # Set root directory.
        path = self.set_dir
        path = os.path.join(path, term.kind)
        if not os.path.exists(path):
            os.makedirs(path)

        # Set term directory.
        if term.name:
            path = os.path.join(path, term.name)
        else:
            path = os.path.join(path, "--")

        return path


    def delete(self, term):
        """Deletes a term to file system.

        :param pyesdoc.cv.Term term: Term to be deleted from file system.

        """
        if term.io_path and os.path.isfile(term.io_path):
            os.remove(term.io_path)
            term.io_path = None
            log("term removed from file system: {}".format(term))


    def exists(self, term):
        """Returns a flag indicating whether the term is written to the file system or not.

        :param pyesdoc.cv.Term term: A term.

        """
        return os.path.isfile(term.io_path) if term.io_path else False


    def write(self, term):
    	"""Writes a term to file system.

    	:param pyesdoc.cv.Term term: Term to be written to file system.

    	"""
        # Write new.
        path = self._get_term_io_path(term)
        with open(path, 'w') as fstream:
            fstream.write(to_json(term))

        # Remove old (if ncessary).
        if term.io_path is not None and term.io_path != path:
            os.remove(term.io_path)

        # Update io path.
        term.io_path = path

        log("term written to f-sys: {}".format(term))


    def read(self, path):
        """Reads a term from local file system.

        :param str path: Path to term persisted to local file system.

        :returns: Term read from local file system.
        :rtype: pyesdoc.cv.Term

        """
        with open(path, 'r') as file_in:
            return from_json(file_in.read())


    def yield_all(self):
        """Yields terms read from local file system.

        :returns: Generator enumerating terms persisted to local file system.
        :rtype: generator

        """
        for termset_dir, termset_files in ((i[0], i[2]) for i in os.walk(self.set_dir)):
            for path in (os.path.join(termset_dir, f) for f in termset_files):
                term = self.read(path)
                term.io_path = path
                yield term
