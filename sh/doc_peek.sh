#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	log "peeking at document ..."
	activate_venv
	if [ "$2" ]; then
		python $PYESDOC_HOME/sh/peek.py --file=$1 --encoding=$2
	else
		python $PYESDOC_HOME/sh/peek.py --file=$1
	fi
}

# Invoke entry point.
main $1 $2
