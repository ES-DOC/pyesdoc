"""
.. module:: pyesdoc.drq.constants.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Library constants.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Data request definition file name.
DEFINITION_FNAME = "dreq2Defn.xml"

# Data request content file name.
CONTENT_FNAME = "dreq.xml"

# Maps data request labels to pythonic labels.
LABEL_MAP = {
    # Definition table labels.
    'CMORvar': 'cmor_variable',
    'exptgroup': 'experiment_group',
    'miptable': 'mip_table',
    'standardname': 'standard_name',
    'varChoiceLinkC': 'var_choice_link_c',
    'varChoiceLinkR': 'var_choice_link_r',

    # Definition table fieldslabels.
    "labUnique": "is_label_unique",

    # Definition table attribute fields.
    "altLabel": "alternative_label",
    "MIPs": "mips",
    "procComment": "processing_comment",
    "procNote": "processing_note",
    "provNote": "provenance_note",
    "refNote": "reference_note",
    "sliceLen": "slice_length",
    "sliceLenUnit": "slice_length_unit",
    "techNote": "technical_note",
}

# Map of attribute names to link short/long names.
LINK_MAP = {
    "cfgid": ("cfg", "config_option"),
    "cid": ("c", "config_value"),
    "cmid": ("cm", "cell_methods"),
    "dimid": ("dim", None),
    "egid": ("eg", "experiment_group"),
    "esid": ("es", "experiments"),
    "gpid": ("gp", None),
    "mip": ("mip", None),
    "mtid": ("mt", "mip_table"),
    "oid": ("o", "objective"),
    "provmip": ("provmip", "provenance_mip"),
    "refid": ("ref", None),
    "rid": ("r", "request"),
    "rlid": ("rl", "request"),
    "sn": ("sn", "standard_name"),
    "snid": ("sn", "standard_name"),
    "spid": ("sp", "spatial_shape"),
    "stid": ("st", "structure"),
    "tid": ("t", None),
    "tmid": ("tm", "temporal_shape"),
    "tslice": ("tslice", "timeslice"),
    "unid": ("un", "units"),
    "vgid": ("vg", "var_group"),
    "vid": ("v", "var")
}
