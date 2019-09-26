#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	source $PYESDOC_HOME/sh/activate_venv.sh
	cd $PYESDOC_HOME/notebooks
	jupyter notebook

    log "virtual environment updated"
}

# Invoke entry point.
main