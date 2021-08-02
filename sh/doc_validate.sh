#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	log "validating document ..."

    pushd $PYESDOC_HOME
	if [ "$2" ]; then
	    pipenv run python $PYESDOC_HOME/sh/doc_validate.py --file=$1 --outfile=$2
	else
	    pipenv run python $PYESDOC_HOME/sh/doc_validate.py --file=$1
	fi
	popd
}

# Invoke entry point.
main $1 $2
