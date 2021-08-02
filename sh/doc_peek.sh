#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	log "peeking at document ..."

    pushd $PYESDOC_HOME
	if [ "$2" ]; then
		pipenv run python $PYESDOC_HOME/sh/doc_peek.py --file=$1 --encoding=$2
	else
		pipenv run python $PYESDOC_HOME/sh/doc_peek.py --file=$1
	fi
	popd
}

# Invoke entry point.
main $1 $2
