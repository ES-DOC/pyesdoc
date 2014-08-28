"""
.. module:: handlers_metafor_q.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes Metafor Questionnaire document processing handlers.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from ...utils import runtime as rt



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
    """Returns flag inidcating whether a document is of matched type."""
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
        msg = "WARNING :: model name overidden :: from {0} to {1}"
        msg = msg.format(name, _MODEL_OVERRIDES[name])
        rt.log(msg)
        name = _MODEL_OVERRIDES[name]

    return name


def _format_institute_name(name):
    """Returns parsed institute name."""
    name = name.upper()
    if name in _INSTITUTE_OVERRIDES:
        msg = "WARNING :: institute name overidden :: from {0} to {1}"
        msg = msg.format(name, _INSTITUTE_OVERRIDES[name])
        rt.log(msg)
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
    """Formats institute name so as to confirm to DRS."""
    if doc.meta.institute is None:
        return

    doc.meta.institute = _format_institute_name(doc.meta.institute)


def _set_model_name(doc):
    """Formats model name so as to confirm to DRS."""
    if not _is_of_type(doc, _TYPE_KEY_MODEL_COMPONENT):
        return

    doc.short_name = _format_model_name(doc.short_name)


def _delete_model_properties(doc):
    """Deletes top level model properties as these were supposed to be hidden for CMIP5."""
    if _is_of_type(doc, _TYPE_KEY_MODEL_COMPONENT):
        doc.properties = []


# Set of document parsers.
PARSERS = (
    _set_drs,
    _set_institute_1,
    _set_institute_2,
    _set_model_name,
    _delete_model_properties
    )
