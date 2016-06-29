# -*- coding: utf-8 -*-

"""
.. module:: cim_1.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: CIM v1 HTML field sets.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc.codecs.html.fieldsets.field_info import FieldInfo
from pyesdoc.ontologies import cim



_SEPARATOR = "  |  "


# Document field sets.
FIELDSETS = {
    'cim.2.designing.numericalexperiment-overview': [
        FieldInfo('MIP Era', path='meta.project'),
        FieldInfo('Sub MIPs', path='meta.sub_projects',
                  input_formatter=lambda v: _SEPARATOR.join(v)),
        FieldInfo('Institute', path='meta.institute'),
        FieldInfo('Canonical Name', path='canonical_name'),
        FieldInfo('Alternative Names', path='alternative_names',
                  input_formatter=lambda v: _SEPARATOR.join(v)),
        FieldInfo('Internal Name', path='internal_name'),
        FieldInfo('Long Name', path='long_name'),
        FieldInfo('Description', path='description'),
        FieldInfo('Rationale', path='rationale'),
        FieldInfo('Keywords', path='keywords',
                  input_formatter=lambda v: _SEPARATOR.join(v.split(','))),
        FieldInfo('Related Experiments',
                  link_factory=lambda exp: [(i.name, i.viewer_url) for i in \
                                            sorted(exp.related_experiments, key=lambda v: v.name)])
    ],

    str(cim.v2.designing.EnsembleRequirement) : [
        FieldInfo('Name', path='canonical_name'),
        FieldInfo('Description', path='description'),
        FieldInfo('Ensemble Type', path='ensemble_type'),
        FieldInfo('Minimum Size', path='minimum_size'),
        FieldInfo('Conformance Requested ?', path='is_conformance_requested'),
        FieldInfo('Keywords', path='keywords', input_formatter=lambda v: _SEPARATOR.join(v.split(',')))
    ],

    str(cim.v2.designing.ForcingConstraint) : [
        FieldInfo('Name', path='canonical_name'),
        FieldInfo('Description', path='description'),
        FieldInfo('Forcing Type', path='forcing_type'),
        FieldInfo('Conformance Requested ?', path='is_conformance_requested'),
        FieldInfo('Keywords', path='keywords', input_formatter=lambda v: _SEPARATOR.join(v.split(',')))
    ],

    str(cim.v2.designing.NumericalRequirement) : [
        FieldInfo('Name', path='canonical_name'),
        FieldInfo('Description', path='description'),
        FieldInfo('Ensemble Type', path='ensemble_type'),
        FieldInfo('Minimum Size', path='minimum_size'),
        FieldInfo('Conformance Requested ?', path='is_conformance_requested'),
        FieldInfo('Keywords', path='keywords', input_formatter=lambda v: _SEPARATOR.join(v.split(',')))
    ],

    str(cim.v2.designing.TemporalConstraint) : [
        FieldInfo('Start Date', path='start_date.value'),
        FieldInfo('Required Duration', path='required_duration',
          input_formatter=lambda v: "{} {}".format(v.length, v.units)),
        FieldInfo('Description', path='description'),
        FieldInfo('Conformance Requested ?', path='is_conformance_requested'),
        FieldInfo('Keywords', path='keywords', input_formatter=lambda v: _SEPARATOR.join(v.split(',')))
    ],

    'cim.2.shared.citation' : [
        FieldInfo('DOI', path='doi', link_path=lambda v: "https://doi.org/{}".format(v.doi)),
        FieldInfo('Long Title', path='citation_detail', link_path="url.linkage"),
        FieldInfo('Context', path='context'),
        FieldInfo('Abstract', path='abstract'),
    ],

    'cim.2.shared.party' : [
        FieldInfo('Name', path='name', link_path="url.linkage"),
        FieldInfo('Address', path='address'),
        FieldInfo('Email', path='email', email_path='email'),

    ]
}
