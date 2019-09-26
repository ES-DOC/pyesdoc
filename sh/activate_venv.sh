#!/bin/bash

# Import utils.
source $ERRATA_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	export PYTHONPATH=$PYESDOC_HOME:$PYTHONPATH
	export PYTHONPATH=$PYTHONPATH:$PYESDOC_HOME/tests
	venv_path=${PYESDOC_VENV:-$PYESDOC_HOME/ops/venv}
	source $venv_path/bin/activate
	log "venv activated @ "$venv_path
}

# Invoke entry point.
main
