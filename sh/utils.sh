#!/bin/bash

# Wraps standard echo by adding application prefix.
log()
{
	declare now=`date +%Y-%m-%dT%H:%M:%S`
	declare tabs=''
	if [ "$1" ]; then
		if [ "$2" ]; then
			for ((i=0; i<$2; i++))
			do
				declare tabs+='\t'
			done
	    	echo -e $now" [INFO] :: PYESDOC > "$tabs$1
	    else
	    	echo -e $now" [INFO] :: PYESDOC > "$1
	    fi
	else
	    echo -e $now" [INFO] :: PYESDOC > "
	fi
}

# Outputs a line to split up logging.
log_banner()
{
	echo "-------------------------------------------------------------------------------"
}

# Resets temporary folder.
reset_tmp()
{
	rm -rf $PYESDOC_HOME/ops/tmp
	mkdir -p $PYESDOC_HOME/ops/tmp
}

# Wraps pushd command to suppress stdout.
function pushd () {
    command pushd "$@" > /dev/null
}

# Wraps popd command to suppress stdout.
function popd () {
    command popd "$@" > /dev/null
}
