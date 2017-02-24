# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc._search.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document search functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import json

import requests

from pyesdoc import _api_proxy as proxy



# API search endpoint.
_ENDPOINT = "/2/summary/search"

# Document type aliases.
_DOC_TYPE_ALIASES = {
    'cmip5': {
        'model': 'cim.1.software.ModelComponent',
        'experiment': 'cim.1.activity.NumericalExperiment'
    },
    'cmip6': {
        'experiment': 'cim.2.designing.NumericalExperiment',
        'machine': 'cim.2.platform.Machine',
        'mip': 'cim.2.designing.Project',
        'model': 'cim.2.science.Model',
        'performance': 'cim.2.platform.Performance',
        'project': 'cim.2.designing.Project',
        'simulation': 'cim.2.data.Simulation'
    }
}


def search(project, document_type):
    """Exposes documentation search endpoint.

    :param str project: Project identifier, e.g. cmip6.
    :param str document_type: Document type identifier, e.g. model.

    :returns: Search results.
    :rtype: pyesdoc._search.SearchResult

    """
    # Format input parameters.
    project = unicode(project).lower()
    if document_type.endswith("s"):
        document_type = document_type[0:-1]

    # Substitute document type short names.
    try:
        document_type = _DOC_TYPE_ALIASES[project][document_type]
    except KeyError:
        pass

    # Temporarily switch cmip6-draft.
    project = "cmip6-draft" if project == "cmip6" else project

    # Invoke web-service.
    response = proxy.invoke(requests.get, _ENDPOINT, params={
        "project": project,
        "document_type": document_type,
        "document_version": "latest"
        })

    # Decode & return results.
    return SearchResult(json.loads(response.text))


class SearchResult(object):
    """A search result wrapper.

    """
    def __init__(self, obj):
        """Instance constructor.

        """
        self.project = obj['project']
        self.total = obj['total']
        self.items = tuple([SearchResultItem(i) for i in obj['results']])


    def __repr__(self):
        """Instance default representation.

        """
        return str({
            "count": len(self)
            })


    def __len__(self):
        """Returns number of items in search results.

        """
        return len(self.items)


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(self.items)



class SearchResultItem(object):
    """A search result item wrapper.

    """
    def __init__(self, obj):
        """Instance constructor.

        """
        self.experiment = obj[0]
        self.institute = obj[1]
        self.long_name = obj[2]
        self.model = obj[3]
        self.name = obj[4]
        self.canonical_name = obj[5]
        self.uid = obj[6]
        self.version = obj[7]
        self.alternative_name = obj[8]


    def __repr__(self):
        """Instance default representation.

        """
        return str(self.__dict__)
