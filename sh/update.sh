#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "update starts ..."

	cd $PYESDOC_HOME
	git pull
	source $PYESDOC_HOME/sh/update_config.sh
	source $PYESDOC_HOME/sh/update_venv.sh

    log "update complete"
}

# Invoke entry point.
main
