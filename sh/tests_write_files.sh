#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	log "writing test files ..."

    pushd $PYESDOC_HOME
	pipenv run python $PYESDOC_HOME/sh/tests_write_files.py --outdir=$PYESDOC_HOME/tests/files
	popd

	log "test files written to "$PYESDOC_HOME/tests/files
}

# Invoke entry point.
main
