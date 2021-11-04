#!/bin/bash

# Import utils.
source $ESDOC_DIR_BASH/utils.sh

# Main entry point.
main()
{
	source $ESDOC_DIR_BASH/pyesdoc/mp_sync.sh 2
}

# Invoke entry point.
main
