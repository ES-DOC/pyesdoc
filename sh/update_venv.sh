#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	source $PYESDOC_HOME/sh/activate_venv.sh
    pip install --upgrade pip
    pip install --upgrade --no-cache-dir -I -r $PYESDOC_HOME/requirements.txt
    deactivate

    log "virtual environment updated"
}

# Invoke entry point.
main
