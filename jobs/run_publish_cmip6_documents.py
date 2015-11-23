# -*- coding: utf-8 -*-

"""
.. module:: run_publish_cmip6_documents.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
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
_parser = argparse.ArgumentParser("Publishes CIM documents extracted from CMIP6 experiment spreadsheet.")
_parser.add_argument(
    "--archive-dir",
    help="Path to a directory into which documents will be written.",
    dest="archive_dir",
    type=str
    )
_parser.add_argument(
    "--worksheet",
    help="Path to the CMIP6 experiments worksheet.",
    dest="worksheet",
    type=str
    )



# Workbook being converted to CIM v2 documents.
_WORKBOOK = None

# Name of relevant worksheets to be found within workbook.
_WS_ENSEMBLE_REQUIREMENT = "EnsembleRequirement"
_WS_EXPERIMENT = "experiment"
_WS_FORCING_CONSTRAINT = "ForcingConstraint"
_WS_PARTY = "party"
_WS_PROJECT = "project"
_WS_REFERENCES = "references"
_WS_REQUIREMENT = "requirement"
_WS_TEMPORAL_CONSTRAINT = "TemporalConstraint"
_WS_URL = "url"

# Default document project code.
_DOC_PROJECT = 'CMIP6-DRAFT'

# Default document source.
_DOC_SOURCE = 'spreadsheet'

# Default document author.
_DOC_AUTHOR = pyesdoc.create(cim.v2.Party,
                             source=_DOC_SOURCE,
                             uid=u'253825f3-fbc8-43fb-b1f6-cc575dc693eb')
_DOC_AUTHOR.email = u"charlotte.pascoe@stfc.ac.uk"
_DOC_AUTHOR.name = u"Charlotte Pascoe"



def _get_ws(ws_name):
    """Returns pointer to a named worksheet.

    """
    return _WORKBOOK.sheet_by_name(ws_name)


def _get_ws_rows(ws_name):
    """Returns collection of rows within a named worksheet.

    """
    return enumerate(_get_ws(ws_name).get_rows())


def _get_ws_data(ws_name):
    """Returns collection of rows within a named worksheet that correspond to actual data.

    """
    for idx, row in _get_ws_rows(ws_name):
        if idx > 0 and len(row[0].value) > 0:
            yield row


def _get_ws_col_map(ws_name):
    """Returns map of column index to column names - supports situation when user reorders columns.

    """
    for idx, row in _get_ws_rows(ws_name):
        if idx == 0:
            return {col.value: col_idx for col_idx, col in enumerate(row)}


def _get_cim_document_from_ws(ws_row, ws_col_map, doc_type, mappings):
    """Returns a CIM document from a spreadsheet row.

    """
    def _get_cell_value(cell_name):
        """Returns a cells value.

        """
        if cell_name not in ws_col_map:
            return None
        return ws_row[ws_col_map[cell_name]]

    # Create document.
    doc = pyesdoc.create(doc_type,
                         project=_DOC_PROJECT,
                         source=_DOC_SOURCE,
                         author=_DOC_AUTHOR,
                         version=1)

    # Set document atribute from worksheet cell values.
    for mapping in mappings:
        # Unpack mapping info.
        cell_value_convertor = None
        if isinstance(mapping, tuple):
            mapping, cell_value_convertor = mapping
        mapping = mapping.split(":")
        doc_attr = mapping[0]
        col_name = mapping[0] if len(mapping) == 1 else mapping[1]

        # Get cell value.
        cell_value = ws_row[ws_col_map[col_name]].value
        if isinstance(cell_value, (unicode, str)):
            cell_value = cell_value.strip()
            if len(cell_value) == 0:
                cell_value = None
            elif cell_value.upper() == u"NONE":
                cell_value = None

        # Convert cell value.
        if cell_value_convertor:
            try:
                cell_value = cell_value_convertor(cell_value)
            except TypeError:
                cell_value = cell_value_convertor(cell_value, _get_cell_value)

        # Assign document attribute.
        setattr(doc, doc_attr, cell_value)

    return doc


def _get_cim_document_set_from_ws(ws_name, doc_type, mappings):
    """Returns set of CIM documents within a spreadsheet.

    """
    result = list()
    ws_col_map = _get_ws_col_map(ws_name)
    for ws_row in _get_ws_data(ws_name):
        result.append(_get_cim_document_from_ws(ws_row, ws_col_map, doc_type, mappings))

    return result


def _convert_to_bool(value):
    """Converts a cell value to a boolean.

    """
    return unicode(value).lower() in [u'true', u't', u'yes', u'y', u"1"]


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


def _convert_to_cim_v2_date_time(value, _get_cell):
    """Converts a cell value to a cim.v2.DateTime instance.

    """
    if value is None:
        return None

    instance = cim.v2.DateTime()
    instance.value = value
    instance.offset = _convert_to_bool(_get_cell("start_date_offset"))

    return instance


def _convert_to_cim_v2_calendar(value):
    """Converts a cell value to a cim.v2.DateTime instance.

    """
    if value is None:
        return None

    raise NotImplementedError("CIM v2 Calendar value needs to be converted from cell content")


def _validate(target):
    """Displays document validation errors.

    """
    # Set document collection.
    try:
        iter(target)
    except TypeError:
        docs = [target]
    else:
        docs = target

    # Validate document collection.
    for doc in docs:
        for err_idx, err in enumerate(pyesdoc.validate(doc)):
            if err:
                print("\t{}".format(err))
        #     if err_idx == 0:
        #         print("Document errors: {} :: {} :: v{}".format(doc.type_key, doc.meta.id, doc.meta.version))
        #     print("\t{}".format(err))


def _get_urls():
    """Gets the collection of urls defined within spreadsheet.

    """
    return _get_cim_document_set_from_ws(_WS_URL, cim.v2.OnlineResource, [
        ("description"),
        ("name"),
        ("linkage"),
        ("protocol")
    ])


def _get_citations():
    """Gets the collection of citations defined within spreadsheet.

    """
    return _get_cim_document_set_from_ws(_WS_REFERENCES, cim.v2.Citation, [
        ("abstract"),
        ("citation_str"),
        ("context"),
        ("doi"),
        ("title"),
        ("url")
    ])


def _get_parties():
    """Gets the collection of parties defined within spreadsheet.

    """
    return _get_cim_document_set_from_ws(_WS_PARTY, cim.v2.Party, [
        ("address"),
        ("email"),
        ("name"),
        ("organisation", _convert_to_bool),
        ("url")
    ])


def _get_temporal_constraints():
    """Gets the collection of temporal constraints defined within spreadsheet.

    """
    return _get_cim_document_set_from_ws(_WS_TEMPORAL_CONSTRAINT, cim.v2.TemporalConstraint, [
        ("canonical_name"),
        ("description"),
        ("conformance_is_requested:conformance_requested", _convert_to_bool),
        ("required_duration", _convert_to_cim_v2_time_period),
        ("required_calendar", _convert_to_cim_v2_calendar),
        ("keywords"),
        ("long_name"),
        ("name"),
        ("references"),
        ("start_date", _convert_to_cim_v2_date_time),
        ("start_flexibility:start_flexiblility", _convert_to_cim_v2_time_period)
    ])


def _get_forcing_constraints():
    """Gets the collection of temporal constraints defined within spreadsheet.

    """
    return _get_cim_document_set_from_ws(_WS_FORCING_CONSTRAINT, cim.v2.ForcingConstraint, [
        ("canonical_name"),
        ("description"),
        ("conformance_is_requested:conformance_requested", _convert_to_bool),
        ("forcing_type"),
        ("keywords"),
        ("long_name"),
        ("name"),
        ("references"),
    ])


class DocumentSet(object):
    """The set of documents extracted from the workwheet.

    """
    def __init__(self, worksheet_fpath, archive_directory):
        """Instance constructor.

        """
        global _WORKBOOK

        pyesdoc.set_option("output_dir", archive_directory)
        _WORKBOOK = xlrd.open_workbook(worksheet_fpath)
        self.citations = _get_citations()
        self.forcing_constraints = _get_forcing_constraints()
        self.parties = _get_parties()
        self.temporal_constraints = _get_temporal_constraints()
        self.urls = _get_urls()


    @property
    def documents(self):
        """Gets full set of managed documents.

        """
        return self.forcing_constraints + \
               self.parties + \
               self.temporal_constraints


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


    def set_inter_document_references(self):
        """Sets inter document references.

        """
        # Set party urls.
        for party in [p for p in self.parties]:
            party.url = self._get_url(party.url)

        # # Set reference urls.
        for citation in [c for c in self.citations if c.url]:
            citation.url = self._get_url(citation.url)

        # Forcing constraint citations.
        for fc in self.forcing_constraints:
            fc.references = [self._get_citation(fc.references)] if fc.references else []

        # Temporal constraint citations.
        for tc in self.temporal_constraints:
            tc.references = [self._get_citation(tc.references)] if tc.references else []


    def write_documents(self):
        """Writes documents to file system.

        """
        for document in self.documents:
            pyesdoc.write(document)


def _main(worksheet_fpath, archive_dir):
    """Main entry point.

    """
    if not os.path.isfile(worksheet_fpath):
        raise ValueError("Worksheet file does not exist")
    if not os.path.isdir(archive_dir):
        raise ValueError("Archive directory does not exist")

    ds = DocumentSet(worksheet_fpath, archive_dir)
    ds.set_inter_document_references()
    ds.write_documents()


# Entry point.
if __name__ == '__main__':
    args = _parser.parse_args()
    _main(args.worksheet, args.archive_dir)
