#!/bin/bash

# Import utils.
source $ESDOC_DIR_BASH/utils.sh

# Main entry point.
main()
{
	cp $ESDOC_DIR_REPOS_CORE/esdoc-cim-v$1-schema/*.py $ESDOC_DIR_PYESDOC/pyesdoc/mp/ontologies/schemas/cim/v$1
	cp $ESDOC_DIR_REPOS_CORE/esdoc-cim-v$1-schema/*.py $ESDOC_DIR_REPOS_CORE/esdoc-cim/v$1/schema
}

# Invoke entry point.
main $1
