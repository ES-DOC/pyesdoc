#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	log "validating document ..."
	activate_venv
	if [ "$2" ]; then
		python $PYESDOC_HOME/sh/validate.py --file=$1 --outfile=$2
	else
		python $PYESDOC_HOME/sh/validate/validate.py --file=$1
	fi
}

# Invoke entry point.
main $1 $2
