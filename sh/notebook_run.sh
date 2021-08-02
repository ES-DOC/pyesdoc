#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
    pushd $PYESDOC_HOME
	cd $PYESDOC_HOME/notebooks
	pipenv run jupyter notebook
	popd

    log "virtual environment updated"
}

# Invoke entry point.
main