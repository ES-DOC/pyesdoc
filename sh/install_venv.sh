#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "installing virtual environment ..."

    pip install --upgrade pip
    pip install --upgrade virtualenv
    virtualenv $PYESDOC_HOME/ops/venv
    activate_venv
    pip install --upgrade pip
    pip install --upgrade --no-cache-dir -I -r $PYESDOC_HOME/requirements.txt
    deactivate
}

# Invoke entry point.
main