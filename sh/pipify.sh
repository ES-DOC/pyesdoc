#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	cd $PYESDOC_HOME
	pipenv run python ./setup.py sdist bdist_wheel
	pipenv run python -m twine upload --repository pypi dist/*
	log "library uploaded to pypi"
}

# Invoke entry point.
main
