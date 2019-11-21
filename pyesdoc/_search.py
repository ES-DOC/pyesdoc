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
from pyesdoc import constants
from pyesdoc._publishing import retrieve



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


def search(
    project,
    document_type,
    document_version=constants.DOC_VERSION_LATEST,
    institute=None,
    sub_project=None,
    model=None,
    experiment=None,
    ):
    """Exposes documentation search endpoint.

    :param str project: Project identifier, e.g. cmip6.
    :param str document_type: Document type identifier, e.g. model.
    :param str document_version: Document version filter, i.e. latest | all.
    :param str institute: Institute identifer, e.g. ipsl.
    :param str sub_project: Sub-project identifer, e.g. damip.
    :param str model: Model identifer, e.g. ipsl-cm5a-lr.
    :param str experiment: Experiment identifer, e.g. piControl.

    :returns: Search results.
    :rtype: pyesdoc._search.SearchResult

    """
    # Set criteria.
    criteria = SearchCriteria(
        project,
        document_type,
        document_version,
        institute,
        sub_project,
        model,
        experiment
        )

    # Invoke web-service.
    params = criteria.get_url_params()
    response = proxy.invoke(requests.get, _ENDPOINT, params=params)

    # Decode & return results.
    return SearchResult(json.loads(response.text))


class SearchCriteria(object):
    """Search criteria wrapper.

    """
    def __init__(self, \
        project,
        document_type,
        document_version=constants.DOC_VERSION_LATEST,
        institute=None,
        sub_project=None,
        model=None,
        experiment=None
        ):
        """Instance constructor.

        """
        self.project = project
        self.document_type = document_type
        if self.document_type[-1] in {"s", "S"}:
            self.document_type = self.document_type[0:-1]
        self.document_version = document_version
        self.institute = institute
        self.sub_project = sub_project
        self.model = model
        self.experiment = experiment


    def get_url_params(self):
        """Returns url parameters to be sent to web-service.

        """
        params = {
            k: unicode(v).strip().lower() for k, v in (
                ("document_type", self.document_type),
                ("document_version", self.document_version),
                ("experiment", self.experiment),
                ("institute", self.institute),
                ("model", self.model),
                ("project", self.project),
                ("sub_project", self.sub_project)
                ) if v is not None
        }
        try:
            params['document_type'] = _DOC_TYPE_ALIASES[params['project']][params['document_type']]
        except KeyError:
            pass

        return params


class SearchResult(object):
    """Search result wrapper.

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


    def load_document(self, identifier):
        """Loads document from remote archive.

        """
        item = None

        if isinstance(identifier, int):
            assert identifier >= 0, 'Item identifier out of bounds'
            assert identifier <= len(self.items), 'Item identifier out of bounds'
            item = self.items[identifer]
        elif isinstance(identifier, basestring):
            identifier = identifier.lower()
            for i in self.items:
                if identifier in (n.lower() for n in i.names):
                    item = i

        if item:
            return item.load_document()


class SearchResultItem(object):
    """A search result item wrapper.

    """
    def __init__(self, obj):
        """Instance constructor.

        """
        self.document = None
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


    @property
    def names(self):
        """Returns set of names.

        """
        names = (
            self.canonical_name,
            self.name,
            self.alternative_name,
            self.long_name
            )

        return (i for i in names if i is not None and len(i) > 0)


    def load_document(self):
        """Loads document from remote archive.

        """
        if self.document is None:
            self.document = retrieve(self.uid, self.version)

        return self.document

