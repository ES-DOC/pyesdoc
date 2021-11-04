#!/bin/bash

# Import utils.
source $ESDOC_DIR_BASH/utils.sh

# Main entry point.
main()
{
	source $ESDOC_DIR_BASH/pyesdoc/mp_generate.sh cim 2 python
}

# Invoke entry point.
main
