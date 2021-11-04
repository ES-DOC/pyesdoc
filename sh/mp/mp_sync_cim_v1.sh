#!/bin/bash

# Import utils.
source $ESDOC_DIR_BASH/utils.sh

# Main entry point.
main()
{
	source $ESDOC_DIR_BASH/pyesdoc/mp_sync.sh 1
}

# Invoke entry point.
main
