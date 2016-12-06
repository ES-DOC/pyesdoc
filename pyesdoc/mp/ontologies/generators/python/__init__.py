from pyesdoc.mp.ontologies.generators.python import utils
from pyesdoc.mp.ontologies.generators.python.decoder_generator import DecoderGenerator
from pyesdoc.mp.ontologies.generators.python.package_extended_schema_generator import PackageExtendedSchemaGenerator
from pyesdoc.mp.ontologies.generators.python.package_typeset_generator import PackageTypeSetGenerator



# Expose utility functions.
UTILS = utils

# Set of supported custom generators or tornado templates.
GENERATORS = {
    '__init__.tornado',
    'type_info.tornado',
    'typeset.tornado',
    PackageExtendedSchemaGenerator,
    PackageTypeSetGenerator,
    DecoderGenerator
}
