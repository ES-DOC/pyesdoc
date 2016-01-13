# -*- coding: utf-8 -*-

"""
.. module:: designing_numerical_experiment.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: CIM v2 PDF encoder.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc import archive
from pyesdoc import ontologies
from pyesdoc.codecs.pdf import encoder_utils as u



# Set of numerical requirement types.
_REQUIREMENT_TYPES = [
	(ontologies.cim.v2.TemporalConstraint, "Temporal Constraints"),
	(ontologies.cim.v2.EnsembleRequirement, "Ensemble Requirements"),
	(ontologies.cim.v2.ForcingConstraint, "Forcing Constraints"),
]


def _format_description(desc):
	"""Formats a description.

	"""
	return "{}\n{}".format(
		desc[desc.find("What:"):desc.find("Why:")].strip(),
		desc[desc.find("Why:"):].strip()
		).strip()


def _set_overview(doc):
	"""Emits numerical experiment overview.

	"""
	fieldset = [
		('Name', doc.canonical_name),
		('Long Name', doc.long_name),
		('Description', doc.description),
		('Keywords', "  |  ".join(doc.keywords)),
		('Related Experiments', " | ".join([i.name for i in doc.related_experiments]))
	]

	u.section_header("Overview")
	u.table(fieldset)


def _set_requirement(doc, req):
	"""Emits numerical requirement.

	"""
	if type(req) == ontologies.cim.v2.EnsembleRequirement:
		fieldset = [
			('Name', req.canonical_name),
			('Description', req.description),
			('Ensemble Type', req.ensemble_type),
			('Minimum Size', req.minimum_size),
			('Conformance Requested ?', req.conformance_is_requested),
			('Description', req.description),
			('Keywords', "  |  ".join(req.keywords))
			]


	elif type(req) == ontologies.cim.v2.ForcingConstraint:
		fieldset = [
			('Name', req.canonical_name),
			('Description', req.description),
			('Forcing Type', req.forcing_type),
			('Conformance Requested ?', req.conformance_is_requested),
			('Keywords', "  |  ".join(req.keywords))
			]

	elif type(req) == ontologies.cim.v2.TemporalConstraint:
		fieldset = [
			('Start Date', req.start_date.value),
			('Required Duration', "{} {}".format(req.required_duration.length, req.required_duration.units)),
			('Description', req.description),
			('Conformance Requested ?', req.conformance_is_requested),
			('Keywords', "  |  ".join(req.keywords))
			]

	else:
		fieldset = []

	u.section_header(req.long_name, level=2)
	u.table(fieldset)


def _set_requirements(doc):
	"""Emits numerical requirement set.

	"""
	# Load from archive if necessary.
	doc.requirements = archive.load_references(doc.requirements)

	# Emit requirements according to type.
	for typeof, description in _REQUIREMENT_TYPES:
		requirements = [r for r in doc.requirements if isinstance(r, typeof)]
		if requirements:
			u.section_header(description)
			for requirement in requirements:
				_set_requirement(doc, requirement)


def set_content(doc):
	"""Returns numerical experiment document transformed to PDF content.

	"""
	_set_overview(doc)
	if doc.requirements:
		_set_requirements(doc)
