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
import uuid
from collections import defaultdict
from operator import add

import xlrd

import pyesdoc
import pyesdoc.ontologies.cim as cim



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
_ARGS.add_argument(
    "--identifiers",
    help="Path to set of CMIP6 experiments document identifiers.",
    dest="identifiers",
    type=str
    )



# Spreadsheet worksheet names.
_WS_PROJECT = "project"
_WS_EXPERIMENT = "experiment"
_WS_REQUIREMENT = "requirement"
_WS_FORCING_CONSTRAINT = "ForcingConstraint"
_WS_TEMPORAL_CONSTRAINT = "TemporalConstraint"
_WS_ENSEMBLE_REQUIREMENT = "EnsembleRequirement"
_WS_MULTI_ENSEMBLE = "MultiEnsemble"
_WS_START_DATE_ENSEMBLE = "StartDateEnsemble"
_WS_REFERENCES = "references"
_WS_PARTY = "party"
_WS_URL = "url"

# Spreadsheet row offsets.
_WS_ROW_OFFSETS = {
    _WS_PROJECT: 2,
    _WS_EXPERIMENT: 2,
    _WS_REQUIREMENT: 2,
    _WS_FORCING_CONSTRAINT: 2,
    _WS_TEMPORAL_CONSTRAINT: 2,
    _WS_ENSEMBLE_REQUIREMENT: 2,
    _WS_MULTI_ENSEMBLE: 2,
    _WS_START_DATE_ENSEMBLE: 2,
    _WS_REFERENCES: 1,
    _WS_PARTY: 1,
    _WS_URL: 1
}

# Set of worksheet name keys.
_WS_SHEETS = [
    _WS_PROJECT,
    _WS_EXPERIMENT,
    _WS_REQUIREMENT,
    _WS_FORCING_CONSTRAINT,
    _WS_TEMPORAL_CONSTRAINT,
    _WS_ENSEMBLE_REQUIREMENT,
    _WS_MULTI_ENSEMBLE,
    _WS_START_DATE_ENSEMBLE,
    _WS_REFERENCES,
    _WS_PARTY,
    _WS_URL
]

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
    try:
        int(value.split(" ")[0])
    except ValueError:
        print "WARNING", "time-period length is not an integer:", value
        instance.length = value.split(" ")[0]
    else:
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
        for attr in ["citation_detail", "canonical_name", "name"]:
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
    _WS_PROJECT: (cim.v2.Project, [
            ("name", 1),
            ("long_name", 2),
            ("canonical_name", 3),
            ("keywords", 4),
            ("description", 5),
            ("rationale", 6),
            ("responsible_parties", [7], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 8)),
            ("references", range(11, 15 + 1)),
            ("sub_projects", range(19, 36 + 1)),
            ("requires_experiments", range(37, 70 + 1)),
        ]),

    _WS_EXPERIMENT: (cim.v2.NumericalExperiment, [
            ("name", 1),
            ("long_name", 2),
            ("canonical_name", 3),
            ("previously_known_as", 4, lambda v, _: [] if not v else [i.strip() for i in v.split(",")]),
            ("keywords", 5),
            ("description", 6),
            ("rationale", 7),
            ("responsible_parties", [8], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 8)),
            ("references", range(12, 17 + 1)),
            ("related_experiments", range(19, 24 + 1)),
            ("temporal_constraints", range(25, 26 + 1)),
            ("ensembles", range(27, 30 + 1)),
            ("multi_ensemble", range(31, 32 + 1)),
            ("model_configurations", range(33, 37 + 1)),
            ("forcing_constraints", range(38, 50 + 1))
        ]),

    # TODO: additional requirements
    _WS_REQUIREMENT: (cim.v2.NumericalRequirement, [
            ("name", 1),
            ("long_name", 2),
            ("canonical_name", 3),
            ("keywords", 4),
            ("description", 5),
            ("rationale", 6),
            ("responsible_parties", [7], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 8)),
            ("references", range(11, 12 + 1)),
            ("is_conformance_requested", 14, _convert_to_bool),
            ("additional_requirements", range(15, 24 + 1))
        ]),

    _WS_FORCING_CONSTRAINT: (cim.v2.ForcingConstraint, [
            ("name", 1),
            ("long_name", 2),
            ("canonical_name", 3),
            ("keywords", 4),
            ("description", 5),
            ("rationale", 6),
            ("responsible_parties", [7], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 8)),
            ("references", range(11, 14 + 1)),
            ("is_conformance_requested", 16, _convert_to_bool),
            ("forcing_type", 17)
        ]),

    _WS_TEMPORAL_CONSTRAINT: (cim.v2.TemporalConstraint, [
            ("name", 1),
            ("long_name", 2),
            ("canonical_name", 3),
            ("keywords", 4),
            ("description", 5),
            ("responsible_parties", [6], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 7)),
            ("references", range(10, 10 + 1)),
            ("is_conformance_requested", 12, _convert_to_bool),
            ("required_duration", 13, _convert_to_cim_v2_time_period),
            ("required_calendar", 14, _convert_to_cim_v2_calendar),
            ("start_date", 15, lambda c, r: _convert_to_cim_v2_date_time(c, r(16))),
            ("start_flexibility", 17, _convert_to_cim_v2_time_period)
        ]),

    # TODO: ensemble-member, cols 15, 16, 17
    _WS_ENSEMBLE_REQUIREMENT: (cim.v2.EnsembleRequirement, [
            ("name", 1),
            ("long_name", 2),
            ("canonical_name", 3),
            ("keywords", 4),
            ("description", 5),
            ("responsible_parties", [6], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 7)),
            ("references", range(10, 10 + 1)),
            ("is_conformance_requested", 12, _convert_to_bool),
            ("ensemble_type", 13),
            ("minimum_size", 14, _convert_to_int),
            # TODO: map to cim type
            ("members", range(15, 17 + 1)),
        ]),

    # TODO: map to cim type
    _WS_MULTI_ENSEMBLE: (cim.v2.MultiEnsemble, [
            ("name", 1),
            ("long_name", 2),
            ("canonical_name", 3),
            ("keywords", 4),
            ("description", 5),
            ("responsible_parties", [6], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 7)),
            ("references", range(10, 10 + 1)),
            ("is_conformance_requested", 14, _convert_to_bool),
            ("ensemble_axis", range(13, 14 + 1))
        ]),

    # TODO: map to cim type
    _WS_START_DATE_ENSEMBLE: (cim.v2.NumericalRequirement, [
            ("name", 1),
            ("long_name", 2),
            ("canonical_name", 3),
            ("keywords", 4),
            ("description", 5),
            ("responsible_parties", [6], lambda x, y: _convert_to_cim_2_responsibilty(x, y, 7)),
            ("references", range(10, 10 + 1)),
            ("is_conformance_requested", 12, _convert_to_bool),
            # TODO: verify target attributes
            ("regular_timeset_start_date", 13),
            ("regular_timeset_start_length", 14),
            ("regular_timeset_start_increment", 15),
            ("irregular_dateset", 16),
        ]),

    _WS_REFERENCES: (cim.v2.Citation, [
            ("doi", 1),
            ("title", 2),
            ("context", 3),
            ("citation_detail", 4),
            ("url", 5),
            ("abstract", 6)
        ]),

    _WS_PARTY: (cim.v2.Party, [
            ("name", 1),
            ("organisation", 2, _convert_to_bool),
            ("address", 3),
            ("email", 4),
            ("url", 5)
        ]),

    _WS_URL: (cim.v2.OnlineResource, [
            ("name", 1),
            ("linkage", 2),
            ("protocol", 3),
            ("description", 4),
        ])
}


class Spreadsheet(object):
    """The spreadhsset from which CIM documents are to be extracted.

    """
    def __init__(self, worksheet_fpath, identifiers):
        """Instance constructor.

        """
        self.ids = identifiers
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
               len(row[0].value):
                yield idx, row


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

        return [self._get_document(self.ids[ws_name][str(idx)], doc_type, row, mappings)
                for idx, row in self._yield_rows(ws_name)]


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


    def _get_document(self, doc_uid, doc_type, row, mappings):
        """Returns a CIM document from a spreadsheet row.

        """
        # Create document.
        doc = pyesdoc.create(doc_type,
                             project=_DOC_PROJECT,
                             source=_DOC_SOURCE,
                             version=1,
                             uid=doc_uid)

        # Assign document author.
        try:
            doc.meta.author = _DOC_AUTHOR_REFERENCE
        except AttributeError:
            pass

        # Set document attributes from mapped worksheet cells.
        for mapping in mappings:
            self._set_document_attribute(doc, row, mapping)

        return doc


class DocumentIdentifiers(object):
    """Wraps the set of predefined document identifiers.

    """
    def __init__(self, fpath):
        """Instance constructor.

        """
        self._uids = defaultdict(lambda: defaultdict(int))
        with open(fpath, 'r') as fstream:
            for line in fstream.readlines():
                ws_name, ws_row, doc_uid = line.split("::")
                self._uids[ws_name][ws_row] = uuid.UUID(doc_uid.replace("\n", ""))


    def __getitem__(self, ws_name):
        """Returns document collection.

        """
        return self._uids[ws_name]


class DocumentSet(object):
    """The set of documents extracted from the workwheet.

    """
    def __init__(self, spreadsheet):
        """Instance constructor.

        """
        self.docs = defaultdict(list)
        for sheet in _WS_SHEETS:
            self[sheet] = spreadsheet[sheet]


    def __getitem__(self, ws_name):
        """Returns document collection.

        """
        return self.docs[ws_name]


    def __setitem__(self, ws_name, collection):
        """Set document collection.

        """
        self.docs[ws_name] = collection


    @property
    def documents(self):
        """Gets full set of managed documents.

        """
        return self[_WS_PROJECT] + \
               self[_WS_EXPERIMENT] + \
               self.numerical_requirements + \
               self[_WS_REFERENCES] + \
               self[_WS_PARTY]


    @property
    def numerical_requirements(self):
        """Gets full set of managed numerical requirements.

        """
        return self[_WS_REQUIREMENT] + \
               self[_WS_FORCING_CONSTRAINT] + \
               self[_WS_TEMPORAL_CONSTRAINT] + \
               self[_WS_ENSEMBLE_REQUIREMENT] + \
               self[_WS_MULTI_ENSEMBLE] + \
               self[_WS_START_DATE_ENSEMBLE]


    @property
    def citation_containers(self):
        """Gets full set of managed objects that have citation collections.

        """
        return self[_WS_EXPERIMENT] + \
               self.numerical_requirements + \
               self[_WS_PROJECT]


    @property
    def url_containers(self):
        """Gets full set of managed objects that have citation collections.

        """
        return self[_WS_PARTY] + self[_WS_REFERENCES]


    @property
    def responsible_party_containers(self):
        """Gets full set of managed objects that have responsible partie collections.

        """
        return self[_WS_EXPERIMENT] + \
               self.numerical_requirements + \
               self[_WS_PROJECT]


    @property
    def responsible_parties(self):
        """Gets full set of managed responsible parties.

        """
        return reduce(add, [i.responsible_parties for i in self.responsible_party_containers])


    @property
    def urls(self):
        """Gets full set of managed url's.

        """
        return reduce(add, [i.url for i in self.url_containers])


    def _get_doc_link(self, doc, type_note=None):
        """Returns a document link.

        """
        if not doc:
            return

        reference = cim.v2.DocReference()
        reference.id = doc.meta.id
        reference.version = doc.meta.version
        if type_note:
            reference.type = "{}:{}".format(doc.type_key, type_note)
        else:
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
        for x in self.url_containers:
            x.url = _convert_name(x.url, self[_WS_URL])

        # Set citations.
        for x in self.citation_containers:
            x.references = _convert_names(x.references, self[_WS_REFERENCES])

        # Set responsibility parties.
        for rp in self.responsible_parties:
            rp.party = _convert_names(rp.party, self[_WS_PARTY])

        # Set experiment related experiments.
        for e in self[_WS_EXPERIMENT]:
            e.related_experiments = _convert_names(e.related_experiments, self[_WS_EXPERIMENT])

        # Set experiment requirements.
        for e in self[_WS_EXPERIMENT]:
            e.temporal_constraints = \
                _convert_names(e.temporal_constraints, self[_WS_TEMPORAL_CONSTRAINT])
            forcing_constraints = e.forcing_constraints
            e.forcing_constraints = \
                _convert_names(forcing_constraints, self[_WS_FORCING_CONSTRAINT])
            e.forcing_constraints += \
                _convert_names(forcing_constraints, self[_WS_REQUIREMENT])
            e.ensembles = \
                _convert_names(e.ensembles, self[_WS_ENSEMBLE_REQUIREMENT])
            e.model_configurations = \
                _convert_names(e.model_configurations, self[_WS_REQUIREMENT])

        # Set project sub-projects.
        for p in self[_WS_PROJECT]:
            pass

        # Set experiment sub-projects.
        for e in self[_WS_EXPERIMENT]:
            for project in self[_WS_PROJECT]:
                if e.canonical_name in project.requires_experiments:
                    e.meta.sub_projects.append(project.name)
            e.meta.sub_projects = sorted(e.meta.sub_projects)

        # Set additional experimental requirements.
        for rq in self[_WS_REQUIREMENT]:
            rq.additional_requirements = _convert_names(rq.additional_requirements, self.numerical_requirements)

        # Set sub-projects.
        for p in self[_WS_PROJECT]:
            p.meta.sub_projects = sorted(p.sub_projects)
            p.sub_projects = _convert_names(p.sub_projects, self[_WS_PROJECT])

        # Set project required experiments.
        for p in self[_WS_PROJECT]:
            p.requires_experiments = _convert_names(p.requires_experiments, self[_WS_EXPERIMENT])

        # Set multi-ensemble axis.
        for me in self[_WS_MULTI_ENSEMBLE]:
            me.ensemble_axis = _convert_names(me.ensemble_axis, self.numerical_requirements)



    def set_doc_links(self):
        """Sets inter document references.

        """
        # Responsibility to party references.
        for rp in self.responsible_parties:
            rp.party = [self._get_doc_link(d) for d in rp.party]

        # Responsibility to party references.
        for c in self.citation_containers:
            c.references = [self._get_doc_link(d) for d in c.references]

        # Experiment to related experiment references.
        for e in self[_WS_EXPERIMENT]:
            e.related_experiments = [self._get_doc_link(d) for d in e.related_experiments]

        # Experiment to requirement references.
        for e in self[_WS_EXPERIMENT]:
            e.requirements += [self._get_doc_link(d) for d in e.temporal_constraints]
            for fc in e.forcing_constraints:
                if isinstance(fc, cim.v2.ForcingConstraint):
                    e.requirements.append(self._get_doc_link(fc))
                else:
                    e.requirements.append(self._get_doc_link(fc, "forcing_constraint"))
            e.requirements += [self._get_doc_link(d) for d in e.ensembles]
            e.requirements += [self._get_doc_link(d, "model_configuration") for d in e.model_configurations]

        # Set additional experimental requirements.
        for r in self[_WS_REQUIREMENT]:
            r.additional_requirements = [self._get_doc_link(d) for d in r.additional_requirements]

        # Project to sub-projects.
        for p in self[_WS_PROJECT]:
            p.sub_projects = [self._get_doc_link(d) for d in p.sub_projects]

        # Project to required experiments.
        for p in self[_WS_PROJECT]:
            p.requires_experiments = [self._get_doc_link(d) for d in p.requires_experiments]


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
        for experiment in self[_WS_EXPERIMENT]:
            del experiment.temporal_constraints
            del experiment.forcing_constraints
            del experiment.ensembles
            del experiment.model_configurations

        for doc in self.documents:
            _write(doc, pyesdoc.ENCODING_JSON)


def _main(args):
    """Main entry point.

    """
    if not os.path.isfile(args.spreadsheet_filepath):
        raise ValueError("Spreadsheet file does not exist")
    if not os.path.isdir(args.io_dir):
        raise ValueError("Archive directory does not exist")

    docs = DocumentSet(
        Spreadsheet(args.spreadsheet_filepath, DocumentIdentifiers(args.identifiers))
            )
    docs.set_document_connections()
    docs.set_doc_links()
    docs.write(args.io_dir)


# Entry point.
if __name__ == '__main__':
    args = _ARGS.parse_args()
    _main(_ARGS.parse_args())
