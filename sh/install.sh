#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "install starts ..."

	source $PYESDOC_HOME/sh/install_config.sh
	source $PYESDOC_HOME/sh/install_venv.sh

    log "install complete"
}

# Invoke entry point.
main
