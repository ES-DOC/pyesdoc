#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
    pushd $PYESDOC_HOME
    pip install --upgrade pip
    pip install --upgrade --no-cache-dir -I -r $PYESDOC_HOME/requirements.txt
    popd

    log "virtual environment updated"
}

# Invoke entry point.
main
