# -*- coding: utf-8 -*-

"""
.. module:: demo_usage_scenario.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Demonstrates usage of pyesdoc library

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from tornado.options import define, options


# Define command line options.
define("outdir", help="Path to directory to which to write outputs")
options.parse_command_line()

# Constants.
_INSTITUTE = 'IPSL'
_PROJECT = 'CMIP5'
_OUTPUT_DIR = options.outdir


# **********************************************************************
# STEP 0 : Importing modules.
# **********************************************************************
import pyesdoc
import pyesdoc.ontologies.cim as cim


# **********************************************************************
# STEP 1 : Creating "documents", i.e. plain old python objects (POPO's).
# **********************************************************************

# ... create model
model = pyesdoc.create(cim.v1.ModelComponent, _PROJECT, _INSTITUTE)
model.short_name = "IPSL-CDX-LR"
model.type = "Model"
model.types.append(model.type)
print "CREATED DOC :: ID = {0} :: VERSION = {1}".format(model.meta.id,
														model.meta.version)

# ... create responsible party.
rp = pyesdoc.create(cim.v1.ResponsibleParty, _PROJECT, _INSTITUTE)
rp.individual_name = "Mark A. Greenslade"
rp.organisation_name = "IPSL"
rp.email = "momipsl@ipsl.jussieu.fr"
model.responsible_parties.append(rp)

# ... create citation.
citation = pyesdoc.create(cim.v1.Citation, _PROJECT, _INSTITUTE)
citation.location = "http://dx.doi.org/10.1007/s00382-006-0158-0"
citation.title = "A generated citation."
model.citations.append(citation)

# ... create component
component = pyesdoc.create(cim.v1.ModelComponent, _PROJECT, _INSTITUTE)
component.type = "Atmosphere"
component.types.append(component.type)
component.short_name = "Atmosphere"
component.long_name = "Atmosphere"
model.sub_components.append(component)

# ... create component property
prop = pyesdoc.create(cim.v1.ComponentProperty, _PROJECT, _INSTITUTE)
prop.is_represented = True
prop.short_name = "Basic Approximations"
prop.values = ["hydrostatic | primitive equations"]
component.properties.append(prop)

# ... create sub-component
component1 = pyesdoc.create(cim.v1.ModelComponent, _PROJECT, _INSTITUTE)
component1.type = "Atmosphere.ConvectionCloudTurbulence"
component1.types.append(component1.type)
component1.short_name = "Convection Cloud Turbulence"
component1.long_name = "Convection Cloud Turbulence"
component1.sub_components.append(component1)

# ... create sub-component property
prop1 = pyesdoc.create(cim.v1.ComponentProperty, _PROJECT, _INSTITUTE)
prop1.is_represented = True
prop1.short_name = "Deep Convection"
component1.properties.append(prop1)

# ... create sub-component sub-property
prop11 = pyesdoc.create(cim.v1.ComponentProperty, _PROJECT, _INSTITUTE)
prop11.short_name = "Processes"
prop11.values = ["detrainment | entrainment | penetrative convection | updrafts and downdrafts | vertical momentum transport"]
prop1.sub_properties.append(prop11)

# ...etc

# ... create simulation
simulation = pyesdoc.create(cim.v1.SimulationRun, _PROJECT, _INSTITUTE)
simulation.short_name = "IPSL-CDX-LR.piControl"

# ... create simulation execution date range / calendar
simulation.calendar = cim.v1.Calendar()
simulation.date_range = cim.v1.OpenDateRange()

# ... associate model & simulation.
pyesdoc.associate(simulation, 'model_reference', model)

# ...etc


# **********************************************************************
# Step 2 : Serialization.
# **********************************************************************

# ... encode as json
model_as_json = pyesdoc.encode(model, pyesdoc.ESDOC_ENCODING_JSON)
simulation_as_json = pyesdoc.encode(simulation, pyesdoc.ESDOC_ENCODING_JSON)

# ... encode as xml
model_as_XML = pyesdoc.encode(model, pyesdoc.ESDOC_ENCODING_XML)
simulation_as_XML = pyesdoc.encode(simulation, pyesdoc.ESDOC_ENCODING_XML)

# ... decode from json
model = pyesdoc.decode(model_as_json, pyesdoc.ESDOC_ENCODING_JSON)
simulation = pyesdoc.decode(simulation_as_json, pyesdoc.ESDOC_ENCODING_JSON)


# **********************************************************************
# Step 3 : I/O
# **********************************************************************
def _do_io(doc):
	"""Performs document io."""
	# Write to file system.
	fpath = pyesdoc.write(model, pyesdoc.ESDOC_ENCODING_JSON)

	# Read from file system.
	doc = pyesdoc.read(fpath)

	return doc

# ... set output path.
pyesdoc.set_option("output_dir", _OUTPUT_DIR)

# ... perform document io.
model = _do_io(model)
simulation = _do_io(simulation)


# **********************************************************************
# STEP 4 : Validation
# **********************************************************************
def _validate(doc):
	"""Performs document validation."""
	validation_errors = pyesdoc.validate(doc)
	if validation_errors:
		print("!!! ERROR !!! {0} DOCUMENT IS INVALID:".format(doc.type_key))
		for err in validation_errors:
			print("\t{0}".format(err))
		raise ValueError("Invalid document")

_validate(model)
_validate(simulation)


# **********************************************************************
# STEP 5 : Publishing
# **********************************************************************

# ... publish
pyesdoc.publish(model)
pyesdoc.publish(simulation)

print "PUBLISHED DOC :: ID = {0} :: VERSION = {1}".format(
	model.meta.id, model.meta.version)

# ... retrieve
model = pyesdoc.retrieve(model.meta.id)
model = pyesdoc.retrieve(model.meta.id, model.meta.version)

# ... republish
model_version = model.meta.version
model.short_name = "IPSL-CDX-MR"
pyesdoc.publish(model)
assert model_version + 1 == model.meta.version

print "REPUBLISHED DOC :: ID = {0} :: VERSION = {1}".format(
	model.meta.id, model.meta.version)

# ... unpublish
pyesdoc.unpublish(model.meta.id)
pyesdoc.unpublish(simulation.meta.id)

