#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	log "populating archive ..."

	if [ "$1" ]; then
		declare throttle=$1
	else
		declare throttle=0
	fi
	if [ "$2" ]; then
		declare project=$2
	else
		declare project=""
	fi

	activate_venv
	python $ESDOC_HOME/bash/archive/archive_populate.py --throttle=$throttle --project=$project
    deactivate

	log "populated archive ..."
}

# Invoke entry point.
main $1 $2
