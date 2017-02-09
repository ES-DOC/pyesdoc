#!/bin/bash

# Import utils.
source $PYESDOC_HOME/sh/utils.sh

# Main entry point.
main()
{
	# Version of python used by stack.
	declare PYTHON_VERSION=2.7.13

	log "Installing python "$PYTHON_VERSION" (takes approx 2 minutes)"

	# Download source.
	set_working_dir $ESDOC_DIR_PYTHON
	mkdir src
	cd src
	wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz --no-check-certificate
	tar -xvf Python-$PYTHON_VERSION.tgz
	rm Python-$PYTHON_VERSION.tgz

	# Compile.
	cd Python-$PYTHON_VERSION
	./configure --prefix=$ESDOC_DIR_PYTHON
	make
	make install
	export PATH=$ESDOC_DIR_PYTHON/bin:$PATH
	export PYTHONPATH=$PYTHONPATH:$ESDOC_DIR_PYTHON
	export PYTHONPATH=$PYTHONPATH:$ESDOC_DIR_PYTHON/lib/python2.7/site-packages

	# Install setuptools.
	cd $ESDOC_DIR_PYTHON/src
	wget https://bootstrap.pypa.io/ez_setup.py
	python ez_setup.py

	# Install pip.
	easy_install --prefix $ESDOC_DIR_PYTHON pip
	pip install --upgrade pip

	# Install virtualenv.
	pip install virtualenv
}

# Invoke entry point.
main
