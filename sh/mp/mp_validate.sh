#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	if [ -f $PYESDOC_HOME/sh/mp/mp_validate_report_$1_$2.txt ]; then
		rm $PYESDOC_HOME/sh/mp/mp_validate_report_$1_$2.txt
	fi

    pushd $PYESDOC_HOME
	pipenv run python $PYESDOC_HOME/sh/mp/mp_validate.py --ontology=$1 --version=$2
	popd
}

# Invoke entry point.
main $1 $2
