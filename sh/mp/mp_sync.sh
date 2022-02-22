#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	cp $PYESDOC_PARENT/esdoc-cim-v$1-schema/*.py $PYESDOC_HOME/pyesdoc/mp/ontologies/schemas/cim/v$1
	cp $PYESDOC_PARENT/esdoc-cim-v$1-schema/*.py $PYESDOC_PARENT/esdoc-cim/v$1/schema
}

# Invoke entry point.
main $1
