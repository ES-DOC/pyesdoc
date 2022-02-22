#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	declare ontology=$1
	declare version=$2
	declare language=$3
	declare target=$PYESDOC_HOME/ops/tmp

	log_banner
    pushd $PYESDOC_HOME
	pipenv run python "$PYESDOC_HOME/pyesdoc/mp" -s $ontology -v $version -l $language -o $target
	popd

	log_banner
	
	if [ $language = "python" ]; then
		declare dest=$PYESDOC_HOME/pyesdoc/ontologies/$ontology/v$version

		cp $target/* $dest
		rm $dest/extended_schema*
		log "pyesdoc artefacts copied to @ $dest"

		declare dest=$PYESDOC_PARENT/esdoc-cim/v$version/schema-extended
		cp -r $target/extended_schema* $dest
		log "extended schema copied to @ "$dest
	fi

	log_banner

	find $PYESDOC_HOME -type f -name "*.pyc" -exec rm -f {} \;
	find $PYESDOC_HOME -type f -name "*.pye" -exec rm -f {} \;
	reset_tmp
}

# Invoke entry point.
main $1 $2 $3
