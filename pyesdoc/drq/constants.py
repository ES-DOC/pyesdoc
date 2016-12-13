# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.drq.constants.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Library constants.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Configuration filename.
CONFIG_FILENAME = "dreq2Defn.xml"

# Content filename.
CONTENT_FILENAME = "dreq.xml"

# Map of section pythonic label map.
LABEL_MAP = {
    # Content section names.
    'cellMethods': 'cell_methods',
    'CMORvar': 'cmor_variable',
    'exptgroup': 'experiment_group',
    'modelConfig': 'model_config',
    'objectiveLink': 'objective_link',
    'requestItem': 'request_item',
    'requestLink': 'request_link',
    'requestVar': 'request_variable',
    'requestVarGroup': 'request_variable_group',
    'spatialShape': 'spatial_shape',
    'standardname': 'standard_name',
    'tableSection': 'table_section',
    'temporalShape': 'temporal_shape',
    'timeSlice': 'time_slice',
    'varChoice': 'var_choice',
    'varChoiceLinkC': 'var_choice_link_c',
    'varChoiceLinkR': 'var_choice_link_r',

    # Config table fields.
    "itemLabelMode": "item_label_mode",
    "labUnique": "is_lab_unique",
    "maxOccurs": "max_occurs",

    # Config table atribute fields.
    "techNote": "tech_note",
    "useClass":"use_class"
}

# Set of prologue fields.
PROLOGUE_FIELDS = set([
    'title',
    'description',
    'creator',
    'date'
    ])

# Set of section item field names as extracted from pyesdoc.drq.xml.
SECTION_ITEM_FIELDS = set([
    "MIPs"
    "altLabel"
    "axis"
    "bounds"
    "boundsRequested"
    "boundsValues"
    "cell_measures"
    "cell_methods"
    "cfg"
    "cfgid"
    "cid"
    "class"
    "comment"
    "coords"
    "defaultPriority"
    "deflate"
    "deflate_level"
    "description"
    "dimensions"
    "direction"
    "egid"
    "end"
    "endy"
    "ensz"
    "esid"
    "esidComment"
    "expt"
    "flag_meanings"
    "flag_values"
    "frequency"
    "gpid"
    "grid"
    "gridreq"
    "isGrid"
    "isIndex"
    "label"
    "levelFlag"
    "levels"
    "mcfg"
    "mip"
    "mipTable"
    "mipTableSection"
    "modeling_realm"
    "nenmax"
    "nexmax"
    "nstart"
    "ntot"
    "ny"
    "nyears"
    "nymax"
    "objective"
    "odims"
    "oid"
    "ok_max_mean_abs"
    "ok_min_mean_abs"
    "opar"
    "opt"
    "optionList"
    "positive"
    "preset"
    "priority"
    "procComment"
    "procNote"
    "procnote"
    "prov"
    "provNote"
    "provmip"
    "qid"
    "range"
    "rank"
    "ref"
    "refNote"
    "refid"
    "requested"
    "rid"
    "rlid"
    "rowIndex"
    "shape"
    "shuffle"
    "sliceLen"
    "sn"
    "spid"
    "standardName"
    "start"
    "starty"
    "step"
    "stid"
    "tab"
    "tables"
    "tattr"
    "techNote"
    "tid"
    "tier"
    "tierMin"
    "title"
    "tmid"
    "tolRequested"
    "treset"
    "tslice"
    "type"
    "uid"
    "units"
    "url"
    "usage"
    "valid_max"
    "valid_min"
    "value"
    "varList"
    "vgid"
    "vid"
    "yps"
    ])