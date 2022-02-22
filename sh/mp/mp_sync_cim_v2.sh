#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	source $PYESDOC_HOME/sh/mp/mp_sync.sh 2
}

# Invoke entry point.
main
