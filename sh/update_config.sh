#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	cp $PYESDOC_HOME/ops/config/pyesdoc.conf $PYESDOC_HOME/ops/config/pyesdoc.conf.backup
	cp $PYESDOC_HOME/sh/template-pyesdoc.conf $PYESDOC_HOME/ops/config/pyesdoc.conf
	log "configuration file updated"
}

# Invoke entry point.
main
