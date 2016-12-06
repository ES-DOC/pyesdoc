"""
.. module:: pyesdoc.mp.generate.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: pyesdoc.mp code generator.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse

import pyesdoc



# Define command line arguments.
_parser = argparse.ArgumentParser("ES-DOC Code Generator.")
_parser.add_argument(
    "-s", "--schema-name",
    help="Target ontology schema. [default = cim]",
    dest="schema_name",
    type=str
    )
_parser.add_argument(
    "-v", "--schema-version",
    help="Target ontology schema version. [default = 1]",
    dest="schema_version",
    type=str
    )
_parser.add_argument(
    "-l", "--language",
    help="Target programming language. [default = python]",
    dest="language",
    type=str
    )
_parser.add_argument(
    "-o", "--output-dir",
    help="Path to a directory to which generated code will be written",
    dest="output_dir",
    type=str
    )


# Set command line options.
args = _parser.parse_args()

# Set ontology schema.
schema = pyesdoc.mp.get_schema(args.schema_name, args.schema_version)
if schema is None:
    raise pyesdoc.mp.exceptions.UnsupportedOntologySchema('Unsupported schema: {0} v{1}.'.format(args.schema_name, args.schema_version))

# Generate.
pyesdoc.mp.generate(schema, args.language, args.output_dir)
