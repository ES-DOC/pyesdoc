# -*- coding: utf-8 -*-

"""
.. module:: demo_usage_scenario.py
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
# STEP 1 : Creating numerical experiment.
# **********************************************************************



# **********************************************************************
# Step 2 : Serialization.
# **********************************************************************

# ... encode as json
experiment_as_json = pyesdoc.encode(experiment, pyesdoc.ENCODING_JSON)

# ... encode as xml
experiment_as_xml = pyesdoc.encode(experiment, pyesdoc.ENCODING_XML)

# ... encode as html
experiment_as_html = pyesdoc.encode(experiment, pyesdoc.ENCODING_HTML)

# ... decode from json
experiment = pyesdoc.decode(experiment_as_json, pyesdoc.ENCODING_JSON)

# ... decode from xml
experiment = pyesdoc.decode(experiment_as_xml, pyesdoc.ENCODING_JSON)

# **********************************************************************
# Step 3 : I/O
# **********************************************************************

# ... set I/O path.
pyesdoc.set_option("output_dir", _OUTPUT_DIR)

# Write to file system.
experiment_fpath = pyesdoc.write(experiment, pyesdoc.ENCODING_JSON)

# Read from file system.
experiment = pyesdoc.read(experiment_fpath)

# **********************************************************************
# STEP 4 : Validation
# **********************************************************************

experiment_errors = pyesdoc.validate(experiment)
if experiment_errors:
	print("!!! ERROR !!! {0} EXPERIMENT IS INVALID:")
	for err in experiment_errors:
		print("\t{0}".format(err))
	raise ValueError("Invalid experiment definition")

# **********************************************************************
# STEP 5 : Publishing
# **********************************************************************

# ... publish
pyesdoc.publish(experiment)

print "PUBLISHED EXPERIMENT :: ID = {0} :: VERSION = {1}".format(
	experiment.meta.id, experiment.meta.version)

# ... retrieve latest
experiment = pyesdoc.retrieve(experiment.meta.id)

# ... retrieve specific version
experiment = pyesdoc.retrieve(experiment.meta.id, experiment.meta.version)

# ... update
experiment.name = experiment.name + "-UPDATED"

# ... republish
experiment_version = experiment.meta.version
pyesdoc.publish(experiment)
assert experiment_version + 1 == experiment.meta.version
print "REPUBLISHED EXPERIMENT :: ID = {0} :: VERSION = {1}".format(
	experiment.meta.id, experiment.meta.version)

# ... unpublish
pyesdoc.unpublish(experiment.meta.id)
assert pyesdoc.retrieve(experiment.meta.id) is None
print "UNPUBLISHED EXPERIMENT :: ID = {0} :: VERSION = {1}".format(
	experiment.meta.id, experiment.meta.version)
