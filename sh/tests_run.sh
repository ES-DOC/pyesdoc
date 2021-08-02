#!/bin/bash

# Import utils.
source $PYESDOC_HOME/bash/utils.sh

# Main entry point.
main()
{
    log "PYESDOC : running tests ..."
	
    pushd $PYESDOC_HOME

	# All tests.
	if [ ! "$1" ]; then
	    log "pyesdoc :: Executing all pyesdoc tests"
	    pipenv run nosetests -v -s $PYESDOC_HOME/tests

	# Archive tests.
	elif [ $1 = "a" ]; then
	    log "pyesdoc :: Executing pyesdoc archive tests"
	    pipenv run nosetests -v -s $PYESDOC_HOME/tests/test_archive.py

	# Extension tests.
	elif [ $1 = "e" ]; then
	    log "pyesdoc :: Executing pyesdoc extension tests"
	    pipenv run nosetests -v -s $PYESDOC_HOME/tests/test_extensions.py

	# Factory tests.
	elif [ $1 = "f" ]; then
	    log "pyesdoc :: Executing pyesdoc factory tests"
	    pipenv run nosetests -v -s $PYESDOC_HOME/tests/test_factory.py

	# General tests.
	elif [ $1 = "g" ]; then
	    log "pyesdoc :: Executing pyesdoc general tests"
	    pipenv run nosetests -v -s $PYESDOC_HOME/tests/test_general.py

	# Publishing tests.
	elif [ $1 = "p" ]; then
	    log "pyesdoc :: Executing pyesdoc publishing tests"
	    pipenv run nosetests -v -s $PYESDOC_HOME/tests/test_publishing.py

	# Serialization tests.
	elif [ $1 = "s" ]; then
	    log "pyesdoc :: Executing pyesdoc serialization tests"
	    pipenv run nosetests -v -s $PYESDOC_HOME/tests/test_serialization.py

	# Serialization non-ascii tests.
	elif [ $1 = "s-na" ]; then
	    log "pyesdoc :: Executing pyesdoc serialization non-ascii tests"
	    pipenv run nosetests -v -s $PYESDOC_HOME/tests/test_serialization_non_ascii.py

	# Validation tests.
	elif [ $1 = "v" ]; then
	    log "pyesdoc :: Executing pyesdoc validation tests"
	    pipenv run nosetests -v -s $PYESDOC_HOME/tests/test_validation.py
	fi

	popd
}

# Invoke entry point.
main $1
