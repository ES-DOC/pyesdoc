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
from collections import defaultdict

import pyesdoc
import pyesdoc.ontologies.cim as cim
import xlrd



# Define command line options.
_ARGS = argparse.ArgumentParser("Publishes CIM documents extracted from CMIP6 experiment spreadsheet.")
_ARGS.add_argument(
    "--io-dir",
    help="Path to a directory into which documents will be written.",
    dest="io_dir",
    type=str
    )
_ARGS.add_argument(
    "--spreadsheet",
    help="Path to the CMIP6 experiments worksheet.",
    dest="spreadsheet_filepath",
    type=str
    )



# Spreadsheet worksheet names.
_WS_ENSEMBLE_REQUIREMENT = "EnsembleRequirement"
_WS_EXPERIMENT = "experiment"
_WS_FORCING_CONSTRAINT = "ForcingConstraint"
_WS_MULTI_ENSEMBLE = "MultiEnsemble"
_WS_PARTY = "party"
_WS_PROJECT = "project"
_WS_REFERENCES = "references"
_WS_REQUIREMENT = "requirement"
_WS_TEMPORAL_CONSTRAINT = "TemporalConstraint"
_WS_URL = "url"

# Spreadsheet row offsets.
_WS_ROW_OFFSETS = {
    _WS_ENSEMBLE_REQUIREMENT: 2,
    _WS_EXPERIMENT: 2,
    _WS_FORCING_CONSTRAINT: 2,
    _WS_MULTI_ENSEMBLE: 2,
    _WS_PARTY: 1,
    _WS_PROJECT: 2,
    _WS_REFERENCES: 1,
    _WS_REQUIREMENT: 2,
    _WS_TEMPORAL_CONSTRAINT: 2,
    _WS_URL: 1
}

# Spreadsheet row exclusions.
_WS_ROW_EXCLUSIONS = defaultdict(list)
_WS_ROW_EXCLUSIONS[_WS_EXPERIMENT] = [3, 5, 7, 9, 11]

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
    if value is not None:
        return

    value = unicode(value)

    # Null substitutions.
    if value.lower() in [u"n/a"]:
        return

    # Strip superfluos suffixes.
    value = value.strip()
    if len(value) > 0 and value[-1] in [u":"]:
        return value[0:-1]

    return value


def _convert_to_int(value):
    """Converts a cell value to an integer.

    """
    return None if value is None else int(value)


def _convert_to_string_array(value):
    """Converts a cell value to an array of strings.

    """
    return [] if value is None else value.split(", ")


def _convert_to_cim_v2_calendar(value):
    """Converts a cell value to a cim.v2.DateTime instance.

    """
    if value is None:
        return

    # TODO
    return
    raise NotImplementedError("CIM v2 Calendar value needs to be converted from cell content")


def _convert_to_cim_v2_time_period(value):
    """Converts a cell value to a cim.v2.TimePeriod instance.

    """
    if value is None:
        return

    instance = cim.v2.TimePeriod()
    instance.length = int(value.split(" ")[0])
    instance.units = value.split(" ")[1]
    instance.date_type = u'unused'

    return instance


def _convert_to_cim_v2_date_time(value, offset):
    """Converts a cell value to a cim.v2.DateTime instance.

    """
    if value is None:
        return

    instance = cim.v2.DateTime()
    instance.value = value
    instance.offset = _convert_to_bool(offset)

    return instance


def _convert_to_cim_2_responsibilty(role, row, col_idx=6):
    """Returns experiment responsibility info.

    """
    if role is None:
        return

    party = cim.v2.Responsibility()
    party.role = _convert_to_unicode(role)
    party.party = [r for r in [row(col_idx), row(col_idx + 1), row(col_idx + 2)] if r]

    return party


def _convert_name(name, collection):
    """Retrieves a document from a collection.

    """
    if not collection or name is None:
        return

    try:
        float(name)
    except:
        pass
    else:
        name = str(name).split('.')[0]
    finally:
        if len(name.strip()) == 0:
            return

    name = name.lower()
    for item in collection:
        for attr in ["citation_str", "canonical_name", "name"]:
            try:
                item_name = getattr(item, attr)
            except AttributeError:
                continue
            else:
                if name == unicode(item_name).lower():
                    return item


def _convert_names(names, collection):
    """Converts a set of names to a set of document.

    """
    result = [_convert_name(n, collection) for n in names]

    return [d for d in result if d]


# Maps of worksheet to cim type & columns.
_WS_MAPS = {
    _WS_PARTY: (cim.v2.Party, [
            ("address", 3),
            ("email", 4),
            ("name", 1),
            ("organisation", 2, _convert_to_bool),
            ("url", 5)
        ]),
    _WS_REFERENCES: (cim.v2.CitationTarget, [
            ("abstract", 6),
            ("citation_str", 4),
            ("context", 3),
            ("doi", 1, _convert_to_unicode),
            ("title", 2),
            ("url", 5)
        ]),
    _WS_PROJECT: (cim.v2.Project, [
            ("canonical_name", 3),
            ("description", 5),
            ("keywords", 4),
            ("long_name", 2),
            ("name", 1),
            ("rationale", 6),
            ("references", range(11, 15)),
            ("requires_experiments", range(36, 69)),
            ("responsible_parties", [7], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 8)),
            ("sub_projects", range(18, 35)),
        ]),
    _WS_URL: (cim.v2.OnlineResource, [
            ("description", 4),
            ("name", 1),
            ("linkage", 2),
            ("protocol", 3)
        ]),
    # TODO: ensemble-member, cols 15, 16, 17
    _WS_ENSEMBLE_REQUIREMENT: (cim.v2.EnsembleRequirement, [
            ("canonical_name", 3),
            ("is_conformance_requested", 12, _convert_to_bool),
            ("description", 5),
            ("ensemble_type", 13),
            ("keywords", 4),
            ("long_name", 2),
            ("minimum_size", 14, _convert_to_int),
            ("name", 1),
            ("references", [10]),
            ("responsible_parties", [6], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 7))
        ]),
    _WS_TEMPORAL_CONSTRAINT: (cim.v2.TemporalConstraint, [
            ("canonical_name", 3),
            ("description", 5),
            ("is_conformance_requested", 12, _convert_to_bool),
            ("required_duration", 13, _convert_to_cim_v2_time_period),
            ("required_calendar", 14, _convert_to_cim_v2_calendar),
            ("keywords", 4),
            ("long_name", 2),
            ("name", 1),
            ("references", [10]),
            ("responsible_parties", [6], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 7)),
            ("start_date", 15, lambda c, r: _convert_to_cim_v2_date_time(c, r(16))),
            ("start_flexibility", 17, _convert_to_cim_v2_time_period)
        ]),
    _WS_FORCING_CONSTRAINT: (cim.v2.ForcingConstraint, [
            ("canonical_name", 3),
            ("description", 5),
            ("is_conformance_requested", 16, _convert_to_bool),
            ("forcing_type", 17),
            ("keywords", 4),
            ("long_name", 2),
            ("name", 1),
            ("rationale", 6),
            ("references", range(11, 14)),
            ("responsible_parties", [7], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 8))
        ]),
    # TODO: additional requirements
    _WS_REQUIREMENT: (cim.v2.NumericalRequirement, [
            ("additional_requirements", range(15, 25)),
            ("canonical_name", 3),
            ("description", 5),
            ("is_conformance_requested", 14, _convert_to_bool),
            ("keywords", 4),
            ("long_name", 2),
            ("name", 1),
            ("rationale", 6),
            ("references", range(11, 13)),
            ("responsible_parties", [7], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 8))
        ]),
    _WS_EXPERIMENT: (cim.v2.NumericalExperiment, [
            ("canonical_name", 3),
            ("description", 5),
            ("ensembles", range(26, 30)),
            ("forcing_constraints", range(36, 49)),
            ("keywords", 4),
            ("long_name", 2),
            ("model_configurations", range(31, 36)),
            ("multi_ensemble", 30),
            ("name", 1),
            ("rationale", 6),
            ("references", range(11, 17)),
            ("related_experiments", range(18, 24)),
            ("responsible_parties", [7], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 8)),
            ("temporal_constraints", range(24, 26))
        ])
}


class Spreadsheet(object):
    """The spreadhsset from which CIM documents are to be extracted.

    """
    def __init__(self, worksheet_fpath):
        """Instance constructor.

        """
        self._spreadsheet = xlrd.open_workbook(worksheet_fpath)


    def _get_sheet(self, ws_name):
        """Returns pointer to a named worksheet.

        """
        return self._spreadsheet.sheet_by_name(ws_name)


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


    def __getitem__(self, ws_name):
        """Returns a child table attribute.

        """
        doc_type, mappings = _WS_MAPS[ws_name]

        return [self._get_document(doc_type, row, mappings)
                for row in self._yield_rows(ws_name)]


    def _set_document_attribute(self, doc, row, mapping):
        """Asssigns a document attribute form a mapping.

        """
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

        # Set document attributes from mapped worksheet cells.
        for mapping in mappings:
            self._set_document_attribute(doc, row, mapping)

        return doc


class DocumentSet(object):
    """The set of documents extracted from the workwheet.

    """
    def __init__(self, spreadsheet):
        """Instance constructor.

        """
        self.citations = spreadsheet[_WS_REFERENCES]
        self.ensemble_requirements = spreadsheet[_WS_ENSEMBLE_REQUIREMENT]
        self.experiments = spreadsheet[_WS_EXPERIMENT]
        self.forcing_constraints = spreadsheet[_WS_FORCING_CONSTRAINT]
        self.parties = spreadsheet[_WS_PARTY]
        self.temporal_constraints = spreadsheet[_WS_TEMPORAL_CONSTRAINT]
        self.projects = spreadsheet[_WS_PROJECT]
        self.requirements = spreadsheet[_WS_REQUIREMENT]
        self.urls = spreadsheet[_WS_URL]

        # TODO rebuild citations after citation review is complete
        self.citations = []


    @property
    def documents(self):
        """Gets full set of managed documents.

        """
        return self.citations + \
               self.experiments + \
               self.numerical_requirements + \
               self.parties + \
               self.projects


    @property
    def numerical_requirements(self):
        """Gets full set of managed numerical requirements.

        """
        return self.ensemble_requirements + \
               self.forcing_constraints + \
               self.requirements + \
               self.temporal_constraints


    @property
    def citation_containers(self):
        """Gets full set of managed objects that have citation collections.

        """
        return self.experiments + \
               self.numerical_requirements + \
               self.projects


    @property
    def url_containers(self):
        """Gets full set of managed objects that have citation collections.

        """
        return self.parties + self.citations


    @property
    def responsible_party_containers(self):
        """Gets full set of managed objects that have responsible partie collections.

        """
        return self.numerical_requirements + \
               self.experiments + \
               self.projects


    @property
    def responsible_parties(self):
        """Gets full set of managed responsible parties.

        """
        result = []
        for item in self.responsible_party_containers:
            result += item.responsible_parties

        return result


    def _get_document_link(self, doc):
        """Returns a document link.

        """
        if not doc:
            return

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


    def set_document_connections(self):
        """Sets inter document connections.

        """
        # Set urls.
        for container in self.url_containers:
            container.url = _convert_name(container.url, self.urls)

        # Set citations.
        for container in self.citation_containers:
            container.references = _convert_names(container.references, self.citations)

        # Set responsibility parties.
        for responsibility in self.responsible_parties:
            responsibility.party = _convert_names(responsibility.party, self.parties)

        # Set experiment related experiments.
        for experiment in self.experiments:
            experiment.related_experiments = _convert_names(experiment.related_experiments, self.experiments)

        # Set experiment requirements.
        for experiment in self.experiments:
            experiment.requirements += \
                _convert_names(experiment.temporal_constraints, self.temporal_constraints)
            experiment.requirements += \
                _convert_names(experiment.forcing_constraints, self.forcing_constraints)
            experiment.requirements += \
                _convert_names(experiment.ensembles, self.ensemble_requirements)
            experiment.requirements += \
                _convert_names(experiment.model_configurations, self.requirements)

        # Set additional experimental requirements.
        for requirement in self.requirements:
            requirement.additional_requirements = _convert_names(requirement.additional_requirements, self.numerical_requirements)

        # Set sub-projects.
        for project in self.projects:
            project.sub_projects = _convert_names(project.sub_projects, self.projects)

        # Set project required experiments.
        for project in self.projects:
            project.requires_experiments = _convert_names(project.requires_experiments, self.experiments)


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
            # if exp.name == "DECK1":
            #     print exp.meta.id

        # Set additional experimental requirements.
        for requirement in self.requirements:
            requirement.additional_requirements = [self._get_document_link(d) for d in requirement.additional_requirements]

        # Project to sub-projects.
        for project in self.projects:
            project.sub_projects = [self._get_document_link(d) for d in project.sub_projects]

        # Project to required experiments.
        for project in self.projects:
            project.requires_experiments = [self._get_document_link(d) for d in project.requires_experiments]


    def write(self, io_dir):
        """Writes documents to file system.

        """
        def _get_filepath(doc, encoding):
            """Returns path to document file.

            """
            fname = pyesdoc.get_filename(doc, encoding)
            fpath = os.path.join(io_dir, fname)

            return fpath


        def _write(doc, encoding):
            """Writes document to file system.

            """
            pyesdoc.write(doc, encoding=encoding, fpath=_get_filepath(doc, encoding))

        # Remove helper attributes that do not need to be serialzed.
        for experiment in self.experiments:
            del experiment.temporal_constraints
            del experiment.forcing_constraints
            del experiment.ensembles
            del experiment.model_configurations

        for doc in self.documents:
            _write(doc, pyesdoc.ENCODING_JSON)


def _main(spreadsheet_filepath, io_dir):
    """Main entry point.

    """
    if not os.path.isfile(spreadsheet_filepath):
        raise ValueError("Spreadsheet file does not exist")
    if not os.path.isdir(io_dir):
        raise ValueError("Archive directory does not exist")

    ds = DocumentSet(Spreadsheet(spreadsheet_filepath))
    ds.set_document_connections()
    ds.set_document_links()
    ds.write(io_dir)


# Entry point.
if __name__ == '__main__':
    args = _ARGS.parse_args()
    _main(args.spreadsheet_filepath, args.io_dir)
