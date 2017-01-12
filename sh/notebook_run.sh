#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	cd $PYESDOC_HOME/notebooks
	activate_venv
	jupyter notebook

    log "virtual environment updated"
}

# Invoke entry point.
main