#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "installing virtual environment ..."

    pushd $PYESDOC_HOME

    # Update pip / pipenv to latest versions.
    pip install --upgrade pip
    pip install --upgrade pipenv

	# Install venv using pip env.
	pipenv install
}

# Invoke entry point.
main
