from pyesdoc.mp.ontologies.generators.qconfig import utils
from pyesdoc.mp.ontologies.generators.qconfig.qconfig_generator import QConfigGenerator

# Expose utility functions.
UTILS = utils

# Set of supported custom generators or tornado templates.
GENERATORS = {
    QConfigGenerator
}
