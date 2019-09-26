#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	log "converting document ..."

	source $PYESDOC_HOME/sh/activate_venv.sh
	python $PYESDOC_HOME/sh/doc_convert.py --file=$1 --encoding=$2
}

# Invoke entry point.
main $1 $2
