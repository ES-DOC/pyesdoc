#!/bin/sh
# Runs pyesdoc test suite.
PYESDOC_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $PYESDOC_DIR
export PYTHONPATH=PYTHONPATH:$PYESDOC_DIR
nosetests -v -s tests
