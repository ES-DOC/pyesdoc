# -*- coding: utf-8 -*-

"""
.. module:: cim_1.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: CIM v1 HTML field sets.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc.codecs.html.fieldsets.field import Field
from pyesdoc.ontologies import cim



_SEPARATOR = "  |  "


# Document field sets.
FIELDSETS = {
    'cim.2.designing.numericalexperiment-overview': [
        Field('MIP Era', path='meta.project'),
        Field('Related MIPs',
            link_factory=lambda exp: [(i.name, i.viewer_url) for i in \
                                      sorted(exp.related_mips, key=lambda v: v.name)]),
        Field('Institute', path='meta.institute'),
        Field('Canonical Name', path='canonical_name'),
        Field('Alternative Names', path='alternative_names',
            input_formatter=lambda v: _SEPARATOR.join(v)),
        Field('Internal Name', path='internal_name'),
        Field('Long Name', path='long_name'),
        Field('Description', path='description'),
        Field('Rationale', path='rationale'),
        Field('Keywords', path='keywords',
            input_formatter=lambda v: _SEPARATOR.join(v.split(',')) if v else None),
        Field('Related Experiments',
            link_factory=lambda exp: [(i.name, i.viewer_url) for i in \
                                      exp.related_experiments])
    ],

    str(cim.v2.designing.EnsembleRequirement) : [
        Field('Name', path='canonical_name'),
        Field('Description', path='description'),
        Field('Ensemble Type', path='ensemble_type'),
        Field('Minimum Size', path='minimum_size'),
        Field('Conformance Requested ?', path='is_conformance_requested'),
        Field('Keywords', path='keywords',
            input_formatter=lambda v: _SEPARATOR.join(v.split(',')))
    ],

    str(cim.v2.designing.ForcingConstraint) : [
        Field('Name', path='canonical_name'),
        Field('Description', path='description'),
        Field('Forcing Type', path='forcing_type', capitalize_value=True),
        Field('Conformance Requested ?', path='is_conformance_requested'),
        Field('Scope', path='scope', capitalize_value=True),
        Field('Keywords', path='keywords',
            input_formatter=lambda v: _SEPARATOR.join(v.split(',')))
    ],

    str(cim.v2.designing.MultiEnsemble) : [
        Field('Name', path='canonical_name'),
        Field('Description', path='description'),
        Field('Forcing Type', path='forcing_type'),
        Field('Conformance Requested ?', path='is_conformance_requested'),
        Field('Keywords', path='keywords',
            input_formatter=lambda v: _SEPARATOR.join(v.split(',')))
    ],

    str(cim.v2.designing.NumericalRequirement) : [
        Field('Name', path='canonical_name'),
        Field('Description', path='description'),
        Field('Ensemble Type', path='ensemble_type'),
        Field('Minimum Size', path='minimum_size'),
        Field('Conformance Requested ?', path='is_conformance_requested'),
        Field('Keywords', path='keywords',
            input_formatter=lambda v: _SEPARATOR.join(v.split(',')))
    ],

    str(cim.v2.designing.TemporalConstraint) : [
        Field('Start Date', path='start_date.value'),
        Field('Required Duration', path='required_duration',
            input_formatter=lambda v: "{} {}".format(v.length, v.units)),
        Field('Description', path='description'),
        Field('Conformance Requested ?', path='is_conformance_requested'),
        Field('Keywords', path='keywords',
            input_formatter=lambda v: _SEPARATOR.join(v.split(',')))
    ],

    'cim.2.designing.project-overview' : [
        Field('Name', path='name'),
        Field('Long Name', path='long_name'),
        Field('Homepage', path='homepage'),
        Field('Description', path='description'),
        Field('Rationale', path='rationale'),
        Field('Objectives', path='objectives'),
        Field('Sub Projects',
            link_factory=lambda p: [(i.name, i.viewer_url) for i in p.sub_projects]),
        Field('Required Experiments',
            link_factory=lambda e: [(i.name, i.viewer_url) for i in e.requires_experiments]),
        Field('Keywords', path='keywords',
            input_formatter=lambda v: _SEPARATOR.join(v.split(',')))
    ],

    'cim.2.shared.citation' : [
        Field('DOI', path='doi',
            link_path=lambda v: "https://doi.org/{}".format(v.doi)),
        Field('Title', path='citation_detail', link_path="url.linkage"),
        Field('Context', path='context'),
        Field('Abstract', path='abstract'),
    ],

    'cim.2.shared.party' : [
        Field('Name', path='name', link_path="url.linkage"),
        Field('Address', path='address'),
        Field('Email', path='email', email_path='email'),
    ]
}
