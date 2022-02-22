#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	source $PYESDOC_HOME/sh/mp/mp_generate.sh cim 1 python
}

# Invoke entry point.
main
