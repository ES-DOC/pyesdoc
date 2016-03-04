# -*- coding: utf-8 -*-

"""
.. module:: run_publish_cmip6_documents.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Publishes CMIP6 documents from the CMIP6 experiment spreadsheet.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""
import argparse
import os

import pyesdoc
import pyesdoc.ontologies.cim as cim
import xlrd



# Define command line options.
_ARGS = argparse.ArgumentParser("Publishes CIM documents extracted from CMIP6 experiment spreadsheet.")
_ARGS.add_argument(
    "--archive-dir",
    help="Path to a directory into which documents will be written.",
    dest="archive_dir",
    type=str
    )
_ARGS.add_argument(
    "--spreadsheet",
    help="Path to the CMIP6 experiments worksheet.",
    dest="spreadsheet_filepath",
    type=str
    )



# Name of relevant worksheets to be found within spreadsheet.
_WS_ENSEMBLE_REQUIREMENT = "EnsembleRequirement"
_WS_EXPERIMENT = "experiment"
_WS_FORCING_CONSTRAINT = "ForcingConstraint"
_WS_PARTY = "party"
_WS_PROJECT = "project"
_WS_REFERENCES = "references"
_WS_REQUIREMENT = "requirement"
_WS_TEMPORAL_CONSTRAINT = "TemporalConstraint"
_WS_URL = "url"

# Row offsets.
_WS_ROW_OFFSETS = {
    _WS_ENSEMBLE_REQUIREMENT: 2,
    _WS_EXPERIMENT: 2,
    _WS_FORCING_CONSTRAINT: 2,
    _WS_PARTY: 1,
    _WS_PROJECT: 2,
    _WS_REFERENCES: 1,
    _WS_REQUIREMENT: 2,
    _WS_TEMPORAL_CONSTRAINT: 2,
    _WS_URL: 1
}

# Row offsets.
_WS_ROW_EXCLUSIONS = {
    _WS_ENSEMBLE_REQUIREMENT: [],
    _WS_EXPERIMENT: [3, 5, 7, 9, 11],
    _WS_FORCING_CONSTRAINT: [],
    _WS_PARTY: [],
    _WS_PROJECT: [],
    _WS_REFERENCES: [],
    _WS_REQUIREMENT: [],
    _WS_TEMPORAL_CONSTRAINT: [],
    _WS_URL: []
}

# Default document project code.
_DOC_PROJECT = 'CMIP6-DRAFT'

# Default document source.
_DOC_SOURCE = 'spreadsheet'

# Default document author.
_DOC_AUTHOR = pyesdoc.create(cim.v2.Party,
                             source=_DOC_SOURCE,
                             uid=u'253825f3-fbc8-43fb-b1f6-cc575dc693eb',
                             version=1)
_DOC_AUTHOR.email = u"charlotte.pascoe@stfc.ac.uk"
_DOC_AUTHOR.name = u"Charlotte Pascoe"

# Default document author reference.
_DOC_AUTHOR_REFERENCE = cim.v2.DocReference()
_DOC_AUTHOR_REFERENCE.uid = _DOC_AUTHOR.meta.id
_DOC_AUTHOR_REFERENCE.version = _DOC_AUTHOR.meta.version



def _convert_to_bool(value):
    """Converts a cell value to a boolean.

    """
    return unicode(value).lower() in [u'true', u't', u'yes', u'y', u"1"]


def _convert_to_unicode(value):
    """Converts a cell value to a boolean.

    """
    if value is None:
        return None

    # Null substitutions.
    value = unicode(value)
    if value.lower() in [u"n/a"]:
        return None

    # Strip superfluos suffixes.
    value = value.strip()
    if len(value) > 0 and value[-1] in [u":"]:
        return value[0:-1]

    return value


def _convert_to_int(value):
    """Converts a cell value to an integer.

    """
    if value is None:
        return None

    return int(value)


def _convert_to_string_array(value):
    """Converts a cell value to an array of strings.

    """
    if value is None:
        return []

    return value.split(", ")


def _convert_to_cim_v2_calendar(value):
    """Converts a cell value to a cim.v2.DateTime instance.

    """
    if value is None:
        return None

    return None

    raise NotImplementedError("CIM v2 Calendar value needs to be converted from cell content")


def _convert_to_cim_v2_time_period(value):
    """Converts a cell value to a cim.v2.TimePeriod instance.

    """
    if value is None:
        return None

    instance = cim.v2.TimePeriod()
    instance.length = int(value.split(" ")[0])
    instance.units = value.split(" ")[1]
    instance.date_type = u'unused'

    return instance


def _convert_to_cim_v2_date_time(value, offset):
    """Converts a cell value to a cim.v2.DateTime instance.

    """
    if value is None:
        return None

    instance = cim.v2.DateTime()
    instance.value = value
    instance.offset = _convert_to_bool(offset)

    return instance


def _convert_to_cim_2_responsibilty(role, row, col_idx=6):
    """Returns experiment responsibility info.

    """
    if role is None:
        return None

    party = cim.v2.Responsibility()
    party.role = _convert_to_unicode(role)
    party.party = [r for r in [row(col_idx), row(col_idx + 1), row(col_idx + 2)] if r]

    return party


def _get_doc(collection, name):
    """Retrieves a document from a collection.

    """
    if not collection or name is None or len(name.strip()) == 0:
        return None

    name = name.lower()
    for item in collection:
        for attr in ["citation_str", "canonical_name", "name"]:
            try:
                item_name = getattr(item, attr)
            except AttributeError:
                continue
            else:
                if name == item_name.lower():
                    return item


def _get_docs(names, collection):
    """Retrieves a document from a collection.

    """
    result = [_get_doc(collection, n) for n in names]

    return [d for d in result if d]


class Spreadsheet(object):
    """The spreadhsset from which CIM documents are to be extracted.

    """
    def __init__(self, worksheet_fpath):
        """Instance constructor.

        """
        self.spreadsheet = xlrd.open_workbook(worksheet_fpath)


    def _get_sheet(self, ws_name):
        """Returns pointer to a named worksheet.

        """
        return self.spreadsheet.sheet_by_name(ws_name)


    def _get_rows(self, ws_name):
        """Returns collection of rows within a named worksheet.

        """
        return enumerate(self._get_sheet(ws_name).get_rows())


    def _yield_rows(self, ws_name):
        """Yields rows within a named worksheet.

        """
        for idx, row in self._get_rows(ws_name):
            if idx >= _WS_ROW_OFFSETS[ws_name] and \
               idx not in _WS_ROW_EXCLUSIONS[ws_name]:
                yield row


    def _get_cell_value(self, row, col_idx, convertor):
        """Returns the (converted) value of a worksheet cell.

        """
        # Extract raw cell value.
        value = row[col_idx - 1].value

        # Nullify dead text.
        if isinstance(value, (unicode, str)):
            value = value.strip()
            if len(value) == 0:
                value = None
            elif value.upper() in {u"NONE", u"N/A"}:
                value = None

        # Convert if necessary.
        if convertor:
            try:
                return convertor(value)
            except TypeError:
                return convertor(value, lambda i: row[i - 1].value)

        return value


    def _get_document(self, doc_type, row, mappings):
        """Returns a CIM document from a spreadsheet row.

        """
        # Create document.
        doc = pyesdoc.create(doc_type,
                             project=_DOC_PROJECT,
                             source=_DOC_SOURCE,
                             version=1)

        # Assign document author.
        try:
            doc.meta.author = _DOC_AUTHOR_REFERENCE
        except AttributeError:
            pass

        # Set document atribute from mapped worksheet cells.
        for mapping in mappings:
            # Unpack mapping info.
            try:
                attr, col_idx, convertor = mapping
            except ValueError:
                attr, col_idx = mapping
                convertor = None

            # Convert cell value.
            if isinstance(col_idx, int):
                attr_value = self._get_cell_value(row, col_idx, convertor)
            else:
                attr_value = [i for i in (self._get_cell_value(row, i, convertor)
                              for i in col_idx) if i]

            # Set aattribute value.
            setattr(doc, attr, attr_value)

        return doc


    def _get_documents(self, ws_name, doc_type, mappings):
        """Returns set of CIM documents within a spreadsheet.

        """
        return [self._get_document(doc_type, row, mappings)
                for row in self._yield_rows(ws_name)]


    def get_parties(self):
        """Gets the collection of parties defined within spreadsheet.

        """
        return self._get_documents(_WS_PARTY, cim.v2.Party, [
            ("address", 3),
            ("email", 4),
            ("name", 1),
            ("organisation", 2, _convert_to_bool),
            ("url", 5)
        ])


    def get_citations(self):
        """Gets the collection of citations defined within spreadsheet.

        """
        return self._get_documents(_WS_REFERENCES, cim.v2.ExternalDocument, [
            ("abstract", 6),
            ("citation_str", 4),
            ("context", 3),
            ("doi", 1, _convert_to_unicode),
            ("title", 2),
            ("url", 5)
        ])


    def get_projects(self):
        """Gets the collection of projects defined within spreadsheet.

        """
        return self._get_documents(_WS_PROJECT, cim.v2.Project, [
            ("canonical_name", 3),
            ("description", 5),
            ("keywords", 4),
            ("long_name", 2),
            ("name", 1),
            ("references", range(10, 14)),
            ("requires_experiments", range(22, 57)),
            ("responsible_parties", [6], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 7)),
            ("sub_projects", range(17, 22)),
        ])


    def get_urls(self):
        """Gets the collection of urls defined within spreadsheet.

        """
        return self._get_documents(_WS_URL, cim.v2.OnlineResource, [
            ("description", 4),
            ("name", 1),
            ("linkage", 2),
            ("protocol", 3)
        ])


    def get_ensemble_requirements(self):
        """Gets the collection of ensemble requirements defined within spreadsheet.

        """
        return self._get_documents(_WS_ENSEMBLE_REQUIREMENT, cim.v2.EnsembleRequirement, [
            ("canonical_name", 3),
            ("conformance_is_requested", 12, _convert_to_bool),
            ("description", 5),
            ("ensemble_type", 13),
            ("keywords", 4, _convert_to_string_array),
            ("long_name", 2),
            ("minimum_size", 14, _convert_to_int),
            ("name", 1),
            ("references", [10]),
            ("responsible_parties", [6], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 7))
        ])


    def get_temporal_constraints(self):
        """Gets the collection of temporal constraints defined within spreadsheet.

        """
        return self._get_documents(_WS_TEMPORAL_CONSTRAINT, cim.v2.TemporalConstraint, [
            ("canonical_name", 3),
            ("description", 5),
            ("conformance_is_requested", 12, _convert_to_bool),
            ("required_duration", 13, _convert_to_cim_v2_time_period),
            ("required_calendar", 14, _convert_to_cim_v2_calendar),
            ("keywords", 4, _convert_to_string_array),
            ("long_name", 2),
            ("name", 1),
            ("references", [10]),
            ("responsible_parties", [6], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 7)),
            ("start_date", 15, lambda c, r: _convert_to_cim_v2_date_time(c, r(16))),
            ("start_flexibility", 17, _convert_to_cim_v2_time_period)
        ])


    def get_forcing_constraints(self):
        """Gets the collection of temporal constraints defined within spreadsheet.

        """
        return self._get_documents(_WS_FORCING_CONSTRAINT, cim.v2.ForcingConstraint, [
            ("canonical_name", 3),
            ("description", 5),
            ("conformance_is_requested", 13, _convert_to_bool),
            ("forcing_type", 14),
            ("keywords", 4, _convert_to_string_array),
            ("long_name", 2),
            ("name", 1),
            ("references", range(10, 12)),
            ("responsible_parties", [6], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 7))
        ])


    def get_experiments(self):
        """Gets the collection of experiments defined within spreadsheet.

        """
        # TODO model configuration
        return self._get_documents(_WS_EXPERIMENT, cim.v2.NumericalExperiment, [
            ("canonical_name", 3),
            ("description", 5),
            ("ensembles", [21, 22]),
            ("forcing_constraints", range(24, 37)),
            ("keywords", 4, _convert_to_string_array),
            ("long_name", 2),
            ("name", 1),
            ("references", range(10, 13)),
            ("related_experiments", range(14, 20)),
            ("responsible_parties", [6], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 7)),
            ("temporal_constraint", 20)
        ])


class DocumentSet(object):
    """The set of documents extracted from the workwheet.

    """
    def __init__(self, archive_directory, spreadsheet):
        """Instance constructor.

        """
        self.archive_directory = archive_directory
        self.citations = spreadsheet.get_citations()
        self.citations = []
        self.ensemble_requirements = spreadsheet.get_ensemble_requirements()
        self.experiments = spreadsheet.get_experiments()
        self.forcing_constraints = spreadsheet.get_forcing_constraints()
        self.parties = spreadsheet.get_parties()
        self.temporal_constraints = spreadsheet.get_temporal_constraints()
        self.projects = spreadsheet.get_projects()
        self.urls = spreadsheet.get_urls()
        # TODO load generic requirements
        # self.requirements = []


    @property
    def documents(self):
        """Gets full set of managed documents.

        """
        return self.experiments + \
               self.ensemble_requirements + \
               self.forcing_constraints + \
               self.parties + \
               self.projects + \
               self.temporal_constraints


    @property
    def requirements(self):
        """Gets full set of managed numerical requirements.

        """
        return self.ensemble_requirements + \
               self.forcing_constraints + \
               self.temporal_constraints

    @property
    def citation_containers(self):
        """Gets full set of managed objects that have citation collections.

        """
        return self.ensemble_requirements + \
               self.experiments + \
               self.forcing_constraints + \
               self.projects + \
               self.temporal_constraints


    @property
    def url_containers(self):
        """Gets full set of managed objects that have citation collections.

        """
        return self.parties + self.citations


    @property
    def party_containers(self):
        """Gets full set of managed objects that have responsible partie collections.

        """
        return self.requirements + \
               self.experiments + \
               self.projects


    @property
    def responsible_parties(self):
        """Gets full set of managed responsible parties.

        """
        result = []
        for item in self.requirements + self.experiments + self.projects:
            result += item.responsible_parties

        return result


    def _get_document_link(self, doc):
        """Returns a document link.

        """
        if doc:
            reference = cim.v2.DocReference()
            reference.id = doc.meta.id
            reference.version = doc.meta.version
            reference.type = doc.type_key
            for attr in ["canonical_name", "name"]:
                try:
                    reference.name = getattr(doc, attr)
                except AttributeError:
                    pass
                else:
                    break

            return reference


    def _get_project(self, name):
        """Returns a matching project.

        """
        if name is None or len(name.strip()) == 0:
            return None
        for project in self.projects:
            if project.name.lower() == name.lower():
                return project


    def _get_url(self, name):
        """Returns a matching URL.

        """
        if name is None or len(name.strip()) == 0:
            return None
        for url in self.urls:
            if url.name.lower() == name.lower():
                return url


    def _get_citation(self, name):
        """Returns matching citation.

        """
        if name is None or len(name.strip()) == 0:
            return None
        for citation in self.citations:
            if citation.citation_str.lower() == name.lower():
                return citation


    def _get_experiment(self, name):
        """Returns a matching experiment.

        """
        if name is None or len(name.strip()) == 0:
            return None
        for experiment in self.experiments:
            if experiment.canonical_name.lower() == name.lower():
                return experiment
            if experiment.name.lower() == name.lower():
                return experiment


    def _get_temporal_constraint(self, name):
        """Returns a temporal constraint numerical requirement.

        """
        if name is None or len(name.strip()) == 0:
            return None
        for temporal_constraint in self.temporal_constraints:
            if temporal_constraint.name.lower() == name.lower():
                return temporal_constraint


    def _get_forcing_constraint(self, name):
        """Returns a forcing constraint numerical requirement.

        """
        if name is None or len(name.strip()) == 0:
            return None
        for forcing_constraint in self.forcing_constraints:
            if forcing_constraint.name.lower() == name.lower():
                return forcing_constraint


    def _get_ensemble_requirement(self, name):
        """Returns an ensemble numerical requirement.

        """
        if name is None or len(name.strip()) == 0:
            return None
        for ensemble in self.ensemble_requirements:
            if ensemble.name.lower() == name.lower():
                return ensemble


    def _get_party(self, name):
        """Returns a matching responsible party.

        """
        if name is None or len(name.strip()) == 0:
            return None
        for party in self.parties:
            if party.name.lower() == name.lower():
                return party


    def set_document_connections(self):
        """Sets inter document connections.

        """
        # Set urls.
        for container in self.url_containers:
            container.url = self._get_url(container.url)

        # Set citations.
        for container in self.citation_containers:
            container.references = [self._get_citation(v) for v in container.references]
            container.references = [c for c in container.references if c is not None]

        # Set responsibility parties.
        for responsibility in self.responsible_parties:
            responsibility.party = [self._get_party(v) for v in responsibility.party]

        # Set experiment related experiments.
        for experiment in self.experiments:
            experiment.related_experiments = [self._get_experiment(v) for v in experiment.related_experiments]

        # Set experiment requirements.
        for experiment in self.experiments:
            experiment.requirements.append(self._get_temporal_constraint(experiment.temporal_constraint))
            experiment.requirements += [self._get_forcing_constraint(c) for c in experiment.forcing_constraints]
            experiment.requirements += [self._get_ensemble_requirement(c) for c in experiment.ensembles]
            experiment.requirements = [r for r in experiment.requirements if r]

        # Set sub-projects.
        for project in self.projects:
            project.sub_projects = [self._get_project(v) for v in project.sub_projects]

        # Set project required experiments.
        for project in self.projects:
            project.requires_experiments = [self._get_experiment(v) for v in project.requires_experiments]


    def set_document_links(self):
        """Sets inter document references.

        """
        # Responsibility to party references.
        for responsibility in self.responsible_parties:
            responsibility.party = [self._get_document_link(d) for d in responsibility.party]

        # Experiment to related experiment references.
        for exp in self.experiments:
            exp.related_experiments = [self._get_document_link(d) for d in exp.related_experiments]

        # Experiment to requirement references.
        for exp in self.experiments:
            exp.requirements = [self._get_document_link(d) for d in exp.requirements]

        # Project to sub-projects.
        for project in self.projects:
            project.sub_projects = [self._get_document_link(d) for d in project.sub_projects]

        # Project to required experiments.
        for project in self.projects:
            project.requires_experiments = [self._get_document_link(d) for d in project.requires_experiments]


    def write_documents(self):
        """Writes documents to file system.

        """
        def _get_filepath(doc, encoding):
            """Returns path to document file.

            """
            fname = pyesdoc.get_filename(doc, encoding)
            fpath = os.path.join(self.archive_directory, fname)

            return fpath


        def _write(doc, encoding):
            """Writes document to file system.

            """
            pyesdoc.write(doc, encoding=encoding, fpath=_get_filepath(doc, encoding))


        for doc in self.documents:
            _write(doc, pyesdoc.ESDOC_ENCODING_JSON)
            _write(doc, pyesdoc.ESDOC_ENCODING_XML)


def _main(spreadsheet_filepath, archive_dir):
    """Main entry point.

    """
    if not os.path.isfile(spreadsheet_filepath):
        raise ValueError("Spreadsheet file does not exist")
    if not os.path.isdir(archive_dir):
        raise ValueError("Archive directory does not exist")

    ds = DocumentSet(archive_dir, Spreadsheet(spreadsheet_filepath))
    ds.set_document_connections()
    ds.set_document_links()
    ds.write_documents()


# Entry point.
if __name__ == '__main__':
    args = _ARGS.parse_args()
    _main(args.spreadsheet_filepath, args.archive_dir)
