#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	log "converting document ..."

    pushd $PYESDOC_HOME
	pipenv run python $PYESDOC_HOME/sh/doc_convert.py --file=$1 --encoding=$2
	popd
}

# Invoke entry point.
main $1 $2
