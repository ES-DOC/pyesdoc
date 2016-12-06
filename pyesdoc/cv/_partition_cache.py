# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv._partition_cache.py
   :copyright: Copyright "December 01, 2014", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Manages a cache of partition terms.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""
import collections

from pyesdoc.cv.utils.logger import log



class PartitionCache(object):
    def __init__(self, io):
        """Instance constructor.

        """
        self._data = collections.defaultdict(list)
        self._io = io


    def add(self, term, emit_log_entry=False):
        """Adds a term to the cache.

        """
        self._data[term.namespace].append(term)
        if emit_log_entry:
            log("term written to cache: {}".format(term))


    def remove(self, term, emit_log_entry=True):
        """Removes a term from the cache.

        """
        self._data[term.namespace].remove(term)
        if emit_log_entry:
            log("term removed from cache: {}".format(term))


    def exists(self, term):
        """Return flag indicating whether term exists within cache or not.

        """
        return term in self._data[term.namespace]


    def init(self):
        """Loads cache from terms written to file system.

        """
        self._data.clear()
        log("partition cache loaded from @ {0}".format(self._io.root_dir))
        for term in self._io.yield_all():
            self.add(term)
        self.sort()


    def sort(self):
        """Sorts cache data.

        """
        for namespace, termset in iter(self._data.items()):
            self._data[namespace] = sorted(termset, key=lambda t: t.sort_key)


    def get_namespaces(self, kind=None):
        """Returns set of partition namespaces.

        :param str kind: Term kind.

        :returns: Set of term namespaces.
        :rtype: set

        """
        if kind is None:
            result = self._data.keys()
        else:
            result = []
            for namespace in self._data.keys():
                if namespace.split(":")[1].lower() == kind.lower():
                    result.append(namespace)
                    break

        return set(sorted(result))


    def query(self, kind=None, name=None):
        """Executes a term query.

        :param str kind: Term kind.
        :param str name: Term Name.

        :returns: Sorted set of terms.
        :rtype: pyesssv.Term | list

        """
        if kind is None:
            return self._get_termsets()
        elif name is None:
            return sorted(self._get_termset(kind))
        else:
            return self._get_term(kind, name)


    def _get_termset(self, kind, sort=True):
        """Returns a set of terms.

        :param str kind: Term kind.

        :returns: Sorted set of terms.
        :rtype: list

        """
        result = []
        for namespace in self._data.keys():
            if namespace.split(":")[1].lower() == kind.lower():
                result = self._data[namespace]
                break

        return sorted(result) if sort else result


    def _get_termsets(self, kind=None):
        """Returns map of termsets keyed by namespace.

        :param str kind: Term kind.

        :returns: Map of termsets keyed by namespace.
        :rtype: dict

        """
        return {ns: self._data[ns] for ns in self.get_namespaces(kind)}


    def _get_term(self, kind, name):
        """Returns first matching term.

        :param str kind: Term kind.
        :param str name: Term Name.

        :returns: A term if matched, otherwise None.
        :rtype: pyesdoc.cv.Term | None

        """
        termset = self._get_termset(kind)
        for term in termset:
            if term.name == name:
                return term


    def get_count(self, kind=None, name=None):
        """Returns count of terms.

        :param str kind: Term kind.

        :returns: Count of terms.
        :rtype: int

        """
        data = self.query(kind, name)
        if kind is None:
            return sum(len(data[namespace]) for namespace in data)
        elif name is None:
            return len(data)
        else:
            return 0 if data is None else 1


    def show(self, kind=None, name=None):
        """Writes to stdout query results.

        :param str kind: Term kind.
        :param str name: Term Name.

        """
        data = self.query(kind, name)
        if not data:
            print("No term data to display")
        elif kind is None:
            for namespace, termset  in data.items():
                print("{} -> {}".format(namespace, len(termset)))
        elif name is None:
            for term in data:
                print("{}".format(term))
        else:
            print("{}".format(data))

