#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	cd $PYESDOC_HOME
	python ./setup.py sdist upload
	log "library uploaded to pypi"
}

# Invoke entry point.
main
