
from pyesdoc.mp.ontologies.generators.qxml import utils
from pyesdoc.mp.ontologies.generators.qxml.root_generator import RootGenerator



# Expose utility functions.
UTILS = utils

# Set of supported custom generators or tornado templates.
GENERATORS = {
    RootGenerator
}
