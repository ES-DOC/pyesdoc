# -*- coding: utf-8 -*-
"""
.. module:: handlers_metafor_q.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes Metafor Questionnaire document processing handlers.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# CIM v1 type keys.
_TYPE_KEY_MODEL_COMPONENT = 'cim.1.software.modelcomponent'
_TYPE_KEY_SIMULATION_RUN = 'cim.1.activity.simulationrun'
_TYPE_KEY_DOCUMENT_SET = 'cim.1.misc.documentset'

# Institute name overrides.
_INSTITUTE_OVERRIDES = {
    'CMA-BCC' : 'BCC',
    'CNRM-GAME' : 'CNRM-CERFACS',
    'GFDL' : 'NOAA-GFDL',
    'GISS' : 'NASA-GISS',
    'NASA GISS' : 'NASA-GISS',
    'NASA' : 'NASA-GISS',
    'NIMR/KMA' : 'NIMR-KMA',
    'STEVE' : 'CSIRO-QCCCE',
    'ESPS-TEAM': None
}

# Model name overrides.
_MODEL_OVERRIDES = {
    'BCC_CSM1.1' : 'BCC-CSM1.1'
}

# Default drs split.
_DRS_SPLIT_01 = '_'
_DRS_SPLIT_02 = '/'

# Name of drs tag.
_DRS_NAME_TAG = "DRS"


def _is_of_type(doc, type_key):
    """Helper function: returns document type match."""
    return doc.type_key.lower() == type_key


def _get_drs_path(doc):
    """Returns a drs path."""
    # Escape if there is no associated simulation.
    if not doc.simulation:
        return

    for external_id in doc.simulation.meta.external_ids:
        for standard in external_id.standards:
            try:
                standard.name.index(_DRS_NAME_TAG)
            except ValueError:
                continue
            else:
                return external_id.value.upper()


def _get_drs_keys(doc):
    """Returns a set of drs keys."""
    # Escape if there is no DRS defined.
    path = _get_drs_path(doc)
    if not path:
        return

    keys = []
    for key in path.split(_DRS_SPLIT_01):
        key = key.split(" ")
        keys.append(key[-1])

    return keys


def _format_model_name(name):
    """Returns parsed model name."""
    name = name.upper()
    if name in _MODEL_OVERRIDES:
        name = _MODEL_OVERRIDES[name]

    return name


def _format_institute_name(name):
    """Returns parsed institute name."""
    if name is not None:
        name = name.upper()
        if name in _INSTITUTE_OVERRIDES:
            name = _INSTITUTE_OVERRIDES[name]

    return name


def _set_drs(doc):
    """Sets DRS information."""
    if not _is_of_type(doc, _TYPE_KEY_DOCUMENT_SET):
        return

    doc.meta.drs_keys = _get_drs_keys(doc)
    if doc.meta.drs_keys:
        doc.meta.drs_path = _DRS_SPLIT_02.join(doc.meta.drs_keys)
        doc.meta.drs_keys[0] = _format_institute_name(doc.meta.drs_keys[0])
        doc.meta.drs_keys[1] = _format_model_name(doc.meta.drs_keys[1])


def _set_institute_1(doc):
    """Sets institute derived from DRS."""
    if not _is_of_type(doc, _TYPE_KEY_DOCUMENT_SET):
        return

    if doc.meta.drs_keys:
        doc.meta.institute = doc.meta.drs_keys[0]


def _set_institute_2(doc):
    """Sets institute derived from contacts."""
    if doc.meta.institute is not None:
        return

    def get_institute(contacts):
        """Returns institute code derived from contact list."""
        for contact in contacts:
            if contact.role == 'centre':
                return contact.abbreviation
        for contact in contacts:
            if contact.role == 'contact' and contact.abbreviation is not None:
                return contact.abbreviation

        return None

    try:
        doc.meta.institute = get_institute(doc.responsible_parties)
    except AttributeError:
        try:
            doc.meta.institute = get_institute(doc.contacts)
        except AttributeError:
            pass


def _set_institute_3(doc):
    """Formats institute name so as to confirm to DRS.

    """
    doc.meta.institute = _format_institute_name(doc.meta.institute)


def _propogate_meta_attributes(doc):
    """Propogates meta attributes to child documents."""
    if not _is_of_type(doc, _TYPE_KEY_DOCUMENT_SET):
        return
    if doc.meta.institute is None:
        return

    child_docs = [
        ctx.doc.experiment,
        ctx.doc.model,
        ctx.doc.platform,
        ctx.doc.simulation
        ]
    # child_docs += ctx.doc.data
    child_docs += ctx.doc.ensembles
    child_docs += ctx.doc.grids

    for child in child_docs:
        child.meta.institute = ctx.doc.meta.institute


def _set_model_name(doc):
    """Formats model name so as to confirm to DRS."""
    if not _is_of_type(doc, _TYPE_KEY_MODEL_COMPONENT):
        return

    doc.short_name = _format_model_name(doc.short_name)


def _set_model_name_inpe_hadgem2es(doc):
    """Overrides model name for the INPE HADGEM2-ES model run.

    """
    if not _is_of_type(doc, _TYPE_KEY_MODEL_COMPONENT):
        return

    if doc.meta.institute == 'INPE' and \
       doc.short_name == 'HADGEM2-ES':
        doc.short_name = 'INPE-HADGEM2-ES'


def _delete_model_properties(doc):
    """Deletes top level model properties as these were supposed to be hidden for CMIP5."""
    if _is_of_type(doc, _TYPE_KEY_MODEL_COMPONENT):
        doc.properties = []


# Set of document parsers.
PARSERS = (
    _set_drs,
    _set_institute_1,
    _set_institute_2,
    _set_institute_3,
    # _propogate_meta_attributes,
    _set_model_name,
    _set_model_name_inpe_hadgem2es,
    _delete_model_properties
    )
