
import os
import sys

from setuptools import setup, find_packages

# Place the package src directory at the begining of sys.path
here = os.path.dirname(__file__)
sys.path[:0] = [os.path.join(here, 'src')]

from pyesdoc import __version__

# Since README.md is in Markdown using this as the long_description isn't ideal
# However, it is better than the two getting out of sync.
long_description = open(os.path.join(here, 'README.md')).read()

requirements = [x.strip() for x in open(os.path.join(here, 'requirements.txt')).readlines()]

setup(name='esdoc-py-client',
      version=__version__,
      description='Python client for the esdoc eco-system, more commonly referred to as pyesdoc.',
      long_description=long_description,
      author='Earth System Documentation (ES-DOC)',
      author_email='dev@es-doc.org',
      url='http://es-doc.org',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=requirements,
      )

